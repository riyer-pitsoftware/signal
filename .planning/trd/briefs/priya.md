---
name: Priya — Backend Brief
bead: BP-006 (signal-k9x)
date: 2026-05-09
---

# 1. Domain model

C2 owns the provenance graph; C3 owns mutable narrative state. They communicate only through `claim_id` references (spine §2 ACL).

**C2:** `source` (origin: job/project/document) → `evidence_artifact` (typed payload, one source) → `claim` (atomic statement; `draft|linked|published|retired`) ↔ `claim_evidence_link` (M:N, `relation` ∈ supports/contradicts/contextualizes, `confidence` 0..1). `witness` records NPC + probe + raw utterance per claim (PRD §4.1 audit trail).

**C3:** `narrative_draft` (working surface, `target_audience`, `compression_budget`) → `narrative_version` (immutable, append-only snapshot). `compression` (per draft×claim; stores `short_text` + `load_bearing_tokens` JSON Suki was told to preserve — F8 reads this). `contradiction` (pairwise claims + status + resolving version).

**Rule (enforced by trigger + gate):** a claim cannot reach `published` without ≥1 `claim_evidence_link` with `relation='supports'`. F1 in two places — schema CHECK (mechanical) and gate function (rich error). Defense in depth.

# 2. Schema (DDL)

SQLite + sqlite-vec, loaded via `conn.load_extension('vec0')`. `PRAGMA foreign_keys=ON`.

```sql
CREATE TABLE source (
  id TEXT PRIMARY KEY, kind TEXT NOT NULL CHECK (kind IN ('job','project','document','conversation')),
  label TEXT NOT NULL, started_at TEXT, ended_at TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')));

CREATE TABLE evidence_artifact (
  id TEXT PRIMARY KEY,
  source_id TEXT NOT NULL REFERENCES source(id) ON DELETE CASCADE,
  artifact_type TEXT NOT NULL CHECK (artifact_type IN ('utterance','pasted_text','structured')),
  body TEXT NOT NULL, body_hash TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE (source_id, body_hash));
CREATE INDEX ix_artifact_source ON evidence_artifact(source_id);

CREATE TABLE claim (
  id TEXT PRIMARY KEY, text TEXT NOT NULL,
  state TEXT NOT NULL CHECK (state IN ('draft','linked','published','retired')),
  created_at TEXT NOT NULL DEFAULT (datetime('now')), retired_at TEXT);
CREATE INDEX ix_claim_state ON claim(state);

CREATE TABLE claim_evidence_link (
  id TEXT PRIMARY KEY,
  claim_id TEXT NOT NULL REFERENCES claim(id) ON DELETE CASCADE,
  artifact_id TEXT NOT NULL REFERENCES evidence_artifact(id) ON DELETE RESTRICT,
  relation TEXT NOT NULL CHECK (relation IN ('supports','contradicts','contextualizes')),
  confidence REAL NOT NULL CHECK (confidence BETWEEN 0 AND 1),
  UNIQUE (claim_id, artifact_id, relation));
CREATE INDEX ix_link_claim ON claim_evidence_link(claim_id);

CREATE TABLE witness (
  id TEXT PRIMARY KEY,
  claim_id TEXT NOT NULL REFERENCES claim(id) ON DELETE CASCADE,
  npc_id TEXT NOT NULL, probe_id TEXT NOT NULL, turn_id TEXT NOT NULL,
  raw_utterance TEXT NOT NULL);

CREATE TABLE narrative_draft (
  id TEXT PRIMARY KEY, target_audience TEXT NOT NULL,
  compression_budget INTEGER NOT NULL,
  updated_at TEXT NOT NULL DEFAULT (datetime('now')));

CREATE TABLE narrative_version (
  id TEXT PRIMARY KEY,
  draft_id TEXT NOT NULL REFERENCES narrative_draft(id),
  rendered_text TEXT NOT NULL,
  published_at TEXT NOT NULL DEFAULT (datetime('now')),
  claim_ids_json TEXT NOT NULL);

CREATE TABLE compression (
  draft_id TEXT NOT NULL REFERENCES narrative_draft(id),
  claim_id TEXT NOT NULL REFERENCES claim(id),
  short_text TEXT NOT NULL, load_bearing_tokens TEXT NOT NULL,
  PRIMARY KEY (draft_id, claim_id));

CREATE TABLE contradiction (
  id TEXT PRIMARY KEY,
  claim_a TEXT NOT NULL REFERENCES claim(id),
  claim_b TEXT NOT NULL REFERENCES claim(id),
  status TEXT NOT NULL CHECK (status IN ('open','acknowledged','resolved')),
  resolved_in TEXT REFERENCES narrative_version(id));

CREATE TABLE session (
  id TEXT PRIMARY KEY,
  started_at TEXT NOT NULL DEFAULT (datetime('now')),
  last_seen_at TEXT NOT NULL, state_blob TEXT NOT NULL);

CREATE VIRTUAL TABLE artifact_vec USING vec0(
  artifact_id TEXT PRIMARY KEY, embedding FLOAT[768]);
```

A trigger `claim_publish_guard` rejects any `narrative_version` insert whose `claim_ids_json` references a claim missing a `supports` link.

# 3. API surface

26 routes under `/api/v1`, FastAPI, bound to 127.0.0.1 only (F2).

**Conversation (C1 facade):** `POST /conversations` start; `GET /conversations/{id}` state+tail; `POST /conversations/{id}/turns` user utterance, streams NPC reply; `POST /conversations/{id}/probe` request named probe; `POST /conversations/{id}/resume` rehydrate.

**Evidence (C2):** `POST /sources`, `GET /sources`, `GET /sources/{id}`; `POST /sources/{id}/artifacts`, `GET /artifacts/{id}`, `POST /artifacts/search` (vector+keyword); `POST /claims`, `GET /claims/{id}`, `PATCH /claims/{id}`; `POST /claims/{id}/links`, `DELETE /claims/{id}/links/{link_id}`; `POST /claims/{id}/retire`.

**Narrative (C3):** `POST /drafts`, `GET /drafts/{id}`, `PATCH /drafts/{id}`; `POST /drafts/{id}/compress`; `POST /drafts/{id}/contradictions/scan`; `POST /drafts/{id}/publish` (runs gate); `GET /versions/{id}`.

**Session (C7):** `POST /sessions/snapshot`; `GET /sessions/{id}`; `DELETE /sessions/{id}`; `GET /health`; `GET /privacy/audit` (confirms zero outbound bytes since boot — F2).

# 4. Conversation state machine

States: `idle → probing → awaiting_response → response_received → claim_extracted → contradiction_surfaced → narrative_draft → published → idle`. Plus `paused` (any → paused) and `error` (recoverable). Transitions are pure `(state, event) → state`. Events: `user_message`, `npc_reply`, `claim_created`, `contradiction_detected`, `compression_requested`, `publish_attempted/_rejected/_accepted`, `pause`, `resume`.

State lives in two places. Authoritative copy: `session.state_blob` JSON in SQLite (survives crash, satisfies C7 resume). In-memory mirror in the FastAPI process holds the working copy for the active turn; write-through on every transition. No Redis, no separate cache (single-process monolith, spine §4). A Pydantic `SessionState` model serializes both ways.

# 5. Publish gate

Returns `version | RejectionReport`. Never raises on policy failure.

```python
def publish(draft_id: str) -> Result[NarrativeVersion, RejectionReport]:
    claim_ids = drafts.included_claim_ids(draft_id)
    failures: list[Failure] = []
    # F1 — provenance integrity (PRD §4.1, spine §3)
    for cid in claim_ids:
        if not links_repo.supports_for(cid):
            failures.append(Failure(cid, "F1", "no supporting evidence link"))
    # F8 — nuance preservation (PRD §4.5)
    for cid in claim_ids:
        comp = compressions.get(draft_id, cid)
        if comp is None:
            failures.append(Failure(cid, "F8", "no compression record")); continue
        marked = set(comp.load_bearing_tokens)
        kept = tokens_present_in(comp.short_text, marked)
        ratio = len(kept) / max(len(marked), 1)
        if ratio < 0.90:
            failures.append(Failure(cid, "F8",
              f"nuance ratio {ratio:.2f} < 0.90; missing {marked - kept}"))
    if failures:
        return Err(RejectionReport(draft_id, failures))
    rendered = renderer.compose(draft_id, claim_ids)
    version = versions.insert(draft_id, rendered, claim_ids)  # trigger re-checks F1
    claims.mark_published(claim_ids, version.id)
    return Ok(version)
```

The DB trigger is the floor; the gate function is the ceiling. Both must agree before a version row exists.

# 6. Reversibility tags

| Decision | Reversibility | Note |
|---|---|---|
| SQLAlchemy 2.x ORM | Easy | Adapter under repos |
| sqlite-vec virtual table | Easy | Swap to FAISS via embedding repo |
| ULID primary keys | Easy | Alembic |
| Trigger-based F1 enforcement | Medium | Gate function portable |
| `claim`↔`evidence_artifact` graph shape | **Hard** | ADR-001 — every later table assumes this topology |
| `state_blob` JSON | Easy | Promote to columns when queries demand it |
| Streaming transport (WS vs SSE) | Medium | Marcus owns; coordinate |
| Gate as Python fn + SQL CHECK | Medium | Both exist; Python is source of truth |

# 7. Open questions

**SQLAlchemy 2.x vs raw sqlite3 — recommendation: SQLAlchemy 2.x for everything except `artifact_vec`.** (1) Alembic migrations are non-negotiable on a Hard-reversibility schema (spine §4); raw migrations rot. (2) 2.x typed Core gives readable repos without 1.x lazy-load footguns. (3) sqlite-vec is a virtual table — SQLAlchemy reads/writes it via `text()`, so we don't ORM-map `vec0` and keep index hints (`MATCH`, `k=`) direct. (4) Extension load is a `do_connect` event handler, ten lines. ~5% perf overhead on hot paths; we're nowhere near that ceiling on a single-user laptop.

**Need from Suki (BP-005):** JSON shape for compressor output (must include `load_bearing_tokens`); contract on malformed output — what Suki guarantees vs what my gate must defend against.
**Need from Marcus (BP-007):** WS vs SSE for `/conversations/{id}/turns`. I lean SSE — one-way, simple reconnect, no upgrade.
**Need from Devon (BP-011):** verification the process binds 127.0.0.1 only; that F2's runtime guard hooks any HTTP client Suki imports (I import none).

# 8. Sacrificial choices

| Choice | Throwaway trigger | Replacement |
|---|---|---|
| Single-user, no auth on local API | Multi-user demand | Session-scoped tokens (spine §5) |
| `state_blob` opaque JSON | Cross-session state queries | Columns + dedicated FSM table |
| Top-K cosine on `artifact_vec` | Retrieval quality plateaus | Hybrid BM25 + reranker (spine §5) |
| Synchronous publish gate | Latency on large drafts | Background worker + SSE notify |
| `claim_ids_json` denormalized in `narrative_version` | Cross-version analytics | Junction table `narrative_version_claim` |
