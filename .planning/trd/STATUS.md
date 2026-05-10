# Signal — TRD Process Status (resume bookmark)

**Last updated:** 2026-05-10
**Phase:** Round A & A.5 closed; voice tool shipped; Kenji MVP cut closed; **Judge Panel pre-draft closed (verdict: cut more, 6.5/10); BP-014 synthesis now blocked only on user gold-set (b0d) + Suki corpus (kv5)**

This file is the durable resume bookmark. Read this first after a context compact.

---

## What this is

Signal is being scoped via a beads-managed TRD process before any product code is written. The PRD is at `/PRD.md`. The architectural spine is at `.planning/trd/spine.md`. Round A delivered seven role briefs at `.planning/trd/briefs/`. The voice-interview tool for collecting gold personas is at `tools/interview/`. The TRD itself does not yet exist — it gets drafted at BP-015 (Haiku) after synthesis at BP-014.

## Bead-ID map (process beads)

Process beads use prefix `signal-`. The plan numbers them BP-NNN.

| BP | bd ID | Layer | Owner | Status |
|---|---|---|---|---|
| BP-001 | signal-2j3 | 0 bootstrap | opus | ✓ closed |
| BP-002 | signal-1qp | 0 bootstrap | opus | ✓ closed |
| BP-003 | signal-j3a | 0 bootstrap | user | ✓ closed |
| BP-004 | signal-mo3 | 1 architecture | opus | ✓ closed |
| BP-005 | signal-qa8 | 2 ml | suki | ✓ closed |
| BP-005a | signal-3pj | 2 corpus | opus | ✓ closed |
| BP-005b | signal-b0d | 2 corpus | **user** | **○ open** |
| BP-005c | signal-kv5 | 2 corpus | suki | ○ open |
| BP-005d | signal-4cd | 2 tooling | suki/opus | ✓ closed |
| BP-006 | signal-k9x | 2 backend | priya | ✓ closed |
| BP-007 | signal-0t6 | 2 frontend | marcus | ✓ closed |
| BP-008 | signal-a9w | 2 creative | dash | ✓ closed |
| BP-009 | signal-c1m | 2 game-design | vesper | ✓ closed |
| BP-010 | signal-16f | 2 visual | design-for-ai | ✓ closed |
| BP-011 | signal-iep | 2 devops | devon | ✓ closed |
| BP-012 | signal-trq | 3 pm | kenji | ✓ closed |
| BP-013 | signal-k2w | 3 review | judges | ✓ closed |
| BP-014 | signal-59z | 4 synthesis | opus | ○ blocked by b0d, k2w, kv5 |
| BP-015 | signal-499 | 5 drafting | haiku | ○ blocked by 59z |
| BP-016 | signal-1zg | 6 qa | judges | ○ blocked by 499 |
| BP-017 | signal-wwu | 6 qa | simplify | ○ blocked by 499 |
| BP-018 | signal-d8q | 7 final | opus | ○ blocked by 1zg, wwu |
| BP-019 | signal-v5f | 8 spawn | opus | ○ blocked by d8q |

`bd ready` shows currently unblocked work. `bd show <id>` for details. `bd dep tree <id>` to visualize.

## Currently ready (2 beads)

1. **BP-005b `signal-b0d` (user)** — author 5 gold personas via voice-interview tool. Use `tools/interview/run.py`. See SPEC at `.planning/trd/test-corpus/SPEC.md` and 2 sample gold personas in `.planning/trd/test-corpus/gold/`. **Blocks BP-014 synthesis.**
2. **BP-005c `signal-kv5` (suki)** — generate 30 synthetic personas + curate 10 public-figure bios per SPEC.md. Output to `.planning/trd/test-corpus/synthetic/` and `.planning/trd/test-corpus/public/`. **Blocks BP-014 synthesis.**

## Judge Panel verdict (BP-013, closed)

**Verdict: cut more.** Panel weighted 6.5/10 vs Kenji's self-score 8.5/10. The 2-point gap reflects integrated build risk (latency arithmetic, calibration timing, demo legibility) that Kenji's cut-discipline correctly didn't address. Three blocker-severity objections — all must be resolved at BP-014 synthesis:

- **Ravi R1 (Tech):** F5 p50≤4s does not survive Suki's serialized 5-role topology. Realistic p50 ≈ 6–9s, p99 ≈ 12–18s. **Fix demanded:** per-turn LLM call-graph budget specifying sync vs deferred vs cached calls.
- **Mara M3 (UX):** Marlow as first-90-seconds NPC is a single point of failure — hardest probe with no orientation beat.
- **Sofia S1 (Demo):** load-bearing differentiators (provenance, dual gate, genericness) are invisible-by-design and demo-hostile. Need designated visible moments per minute.

Full review with numbered objections, demo cold-open script, and pressure-test of Kenji's 6 open questions: `.planning/trd/briefs/judges-pre-draft.md`.

## File map

```
PRD.md                                    — product spec (input, do not edit)
.planning/
  trd/
    STATUS.md                             — this file
    spine.md                              — architectural skeleton (BP-004 output)
    briefs/                               — Round A + A.5 briefs (BP-005..011 outputs)
      suki.md          (6.6k)  — local multi-agent LLM topology + eval
      priya.md         (9.8k)  — domain model, provenance graph, FastAPI, SQLite
      marcus.md        (7.5k)  — Phaser↔React bridge, asset pipeline
      dash.md          (7.1k)  — memory-palace, 7 rooms, 4 NPCs (Lenore/Cassady/Vey/Marlow)
      vesper.md        (6.9k)  — core loop, mechanics, pacing, failure modes
      devon.md         (7.5k)  — local packaging, sizing matrix, privacy verification
      design-system.md (6.9k)  — type, color, motion, accessibility
    test-corpus/
      SPEC.md                             — gold-persona format + authoring rules
      gold/
        gold-001-maya-c.md                — sample (Opus, fictional)
        gold-002-david-o.md               — sample (Opus, fictional)
        raw/                              — voice-interview output lands here
      synthetic/                          — populated by BP-005c
      public/                             — populated by BP-005c
tools/
  interview/                              — BP-005d output, complete
    run.py                                — PEP 723 inline deps; uv run
    questions.yaml                        — 33 prompts × 7 shapes
    CONSENT.md                            — consent form (sign before recording)
    README.md                             — install, usage, troubleshooting
.beads/                                   — beads database (auto-managed)
~/.claude/projects/-Users-riyer-code-signal/memory/team/
  ROSTER.md                               — team roster
  backend.md, frontend.md, ml.md, devops.md, creative-director.md,
  game-designer.md, pm.md, writer.md, judge-panel.md
```

## Critical path

```
        [briefs done]                                                      [ready to publish TRD]
            ↓                                                                       ↓
   ┌── BP-012 Kenji MVP cut ──→ BP-013 Judges pre-draft ──┐
   │                                                       ├──→ BP-014 Opus synthesis (ADRs, risk, fitness)
   ├── BP-005b User gold-set ─────────────────────────────┤        ↓
   │                                                       │   BP-015 Haiku TRD draft
   └── BP-005c Suki synthetic + public corpus ────────────┘        ↓
                                                              BP-016 Judges post-draft  ──┐
                                                                                          ├──→ BP-018 Opus final ──→ BP-019 spawn product beads
                                                              BP-017 simplify ────────────┘
```

## Open questions awaiting user

1. **BP-005b** — author 5 gold personas. Tool is ready. User runs interviews.
2. **Decision after Round A.5** — proceed with Kenji (BP-012) main-thread or as sub-agent? Sub-agent costs usage; main-thread costs context. Default: dispatch as sub-agent (matches Round A pattern).

## Open architectural questions (deferred to BP-014 synthesis)

From spine §8:
1. Conversation persistence model (full-rehydrate vs summarise+RAG)
2. Contradiction surfacing UX (interrupt / queue / world-tension)
3. Evidence ingestion modality (typed only, or paste/import)
4. Versioning granularity (snapshot vs diff)

Plus open questions surfaced in each Round A brief — read each `briefs/*.md` for the "Open questions" section.

## Stack (decided)

- **Backend:** Python 3.11 / FastAPI / SQLAlchemy 2.x / Alembic
- **Persistence:** SQLite + sqlite-vec (single file, single process)
- **AI runtime:** local Ollama only — Qwen 2.5 14B q4 (heavy reasoning, contradiction-detector), Qwen 2.5 7B (evidence linker), Llama 3.2 3B (compressor), `nomic-embed-text` (embeddings)
- **Frontend:** Phaser 3 (game layer) + React 18 (UI overlay) + TypeScript + Vite
- **Styling/state:** Tailwind + shadcn (overlay) + Zustand (Phaser↔React bridge)
- **Local audio (gold-set tooling only, NOT product runtime):** mlx-whisper large-v3 (ASR) + Kokoro 82M (TTS) + sounddevice
- **Devops:** docker-compose, GitHub Actions lint+test only, no IaC, no cloud
- **Hardware target:** Apple Silicon M3 24 GB
- **Privacy:** local-only, F2 zero-outbound-bytes is a hard CI gate

## Fitness functions (from spine §3 — final thresholds calibrated at BP-014)

| ID | Name | Threshold | Hard/Soft |
|---|---|---|---|
| F1 | Provenance integrity | 100% claims with evidence link | **Hard** |
| F2 | Privacy invariant | 0 outbound bytes (data path) | **Hard** |
| F3 | Genericness ceiling | T_g (TBD by Suki via gold corpus) | **Hard** |
| F4 | Compression efficiency | ≥ 1.3× single-shot LLM baseline | Soft |
| F5 | Latency budget | p50 ≤ 4s, p99 ≤ 12s on M3 24GB | Soft |
| F6 | Memory ceiling | ≤ 18 GB peak RSS | **Hard** |
| F7 | Contradiction recall | ≥ 80% recall at ≥ 70% precision | Soft |
| F8 | Nuance preservation | ≥ 90% load-bearing detail retained | **Hard** |

## How to resume after compact

```bash
cd /Users/riyer/code/signal
bd ready                               # see currently unblocked beads
cat .planning/trd/STATUS.md            # this file
ls .planning/trd/briefs/               # confirm briefs landed
ls .planning/trd/test-corpus/          # corpus state
```

**Next architectural action:** the user authors 5 gold personas (BP-005b) and Suki produces 30 synthetic + 10 public-figure bios (BP-005c). Once both land, BP-014 Opus synthesis can run with the full corpus + Kenji's cut + judges' objections, and will need to:
- Resolve the three judge-panel blockers (Ravi R1 latency arithmetic, Mara M3 first-90-second orientation, Sofia S1 demo-visible differentiators)
- Calibrate F3 (genericness ceiling T_g) against the actual gold/synthetic/public corpus
- Answer Kenji's 6 open questions (the panel already pressure-tested which are load-bearing — see judges-pre-draft.md)
- Produce ADRs, risk register, and final fitness-function thresholds for the TRD draft (BP-015 Haiku)

**Kenji's MVP-cut headline (recap from briefs/kenji.md):** Load-bearing core = multi-agent topology + provenance graph + dual publish gate (F1+F8) + genericness gate (F3). Cut Dash's 7 rooms → 4 (Foyer, Workshop, Library, Glasshouse). Killed the 8 GB tier outright. 8.5/10 scorecard. 6 open questions for BP-014 synthesis.

**For BP-005b (user gold-set authoring):**

```bash
cd tools/interview
uv run run.py --list-shapes --shape any --interviewee any   # see shapes
uv run run.py --shape stated-vs-admitted --interviewee gold-003
# After session, mark up transcript per .planning/trd/test-corpus/SPEC.md authoring workflow
```

## Lessons captured

1. **Sub-agents need explicit close instructions AND verification.** Round A agents wrote briefs but did not always run `bd close` despite being told to. Always verify with `bd list --status in_progress` after a wave of sub-agents and manually close stuck ones.
2. **The "out of extra usage" footer on agent notifications is a status banner, not a failure indicator.** Agents can still complete substantive work after this banner appears.
3. **`--deps blocks:X` semantics are inverted from intuition.** When creating Y with `--deps blocks:X`, Y blocks X (Y is upstream). For "Y depends on X," create Y without deps and run `bd dep add Y X` afterwards (which records "X blocks Y").

## Skills installed for this project

- `team-game-designer` (new) — Vesper. Authored at `~/.claude/skills/team-game-designer/SKILL.md`. Registered in `~/.claude/skills/team-onboard/SKILL.md` roster slot 9. Reusable for any UI/game project.

## Ledger of throwaways already named (sacrificial — see spine §5)

- Single-user, single-process monolith → split when multi-user demand
- Naive top-K cosine retrieval on sqlite-vec → hybrid retrieval when narrative quality plateaus
- Single-prompt-per-agent → reflexion / verifier loops when behaviour demands
- Hardcoded NPC roster (4) → user-defined NPCs at v0.2
- File-based session save → cloud sync would re-open privacy posture
- Banned-words list as sole genericness signal → trained classifier when adversarial paraphrase appears
- Voice-interview as gold-set-collection-only → NOT a product modality in v0.1; deferred-with-intent to v0.2 if useful
