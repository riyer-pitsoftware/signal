# Signal — Architectural Spine

**Bead:** BP-004 (signal-mo3)
**Author:** Opus (architect)
**Date:** 2026-05-09
**Status:** draft, blocking Round A

This document is the load-bearing skeleton for Signal's TRD. It does **not** specify implementation. It specifies the slots that Round A agents (Suki, Priya, Marcus, Dash, Vesper, design-for-ai, Devon) must fill, and the constraints those fills must satisfy.

The TRD that follows is judged not by the elegance of any individual slot, but by whether the spine — taken as a whole — mechanically enforces the principles in PRD §4.

---

## 1. Architectural drivers

Four problems define this architecture. Every downstream decision either serves one of these or it is decoration.

### 1.1 Auditability is a graph problem (PRD §4.1)

A narrative claim without a traceable evidence link is a defect. Prose discipline is insufficient — the data model itself must enforce the constraint. Unsupported claims are physically prevented from being published.

**Implication:** evidence-claim-source linkage is part of the schema, not part of a UI affordance.

### 1.2 "Socratic" is a multi-agent topology (PRD §4.2)

Single-prompt LLM dialogue collapses into the model's stylistic prior — fluent, unspecific, unaccountable. Socratic interrogation requires *adversarial roles in tension*: an interrogator that probes, a contradiction-detector that flags inconsistency, a compressor that strips inflation, an evidence-linker that refuses unsupported claims.

These roles must be *distinct in prompt and verifiable in output*. If swapping them produces identical results, the topology is decorative.

**Implication:** the AI subsystem is a routed pipeline of N specialised models, not one chat agent.

### 1.3 "Signal over performance" is a fitness function (PRD §4.4)

Without a measurable, automated definition of "generic," the principle decays into individual taste. Signal must run an automated genericness check on its own outputs and refuse to ship slop. This check is a system component, not a stylistic aspiration.

**Implication:** evaluation is a first-class subsystem, not a dev-time tooling concern.

### 1.4 The corpus is sensitive PII under implicit NDA (PRD §10 implicit)

Career history contains employer names, internal initiative names, confidential outcomes, and identifying detail about colleagues. The architecture's privacy posture is "data does not leave the user's machine, by construction." This is upstream of every other decision — it eliminates remote APIs, cloud storage, telemetry, and most observability patterns.

**Implication:** local-only is a hard architectural constraint, not a v0.1 simplification.

---

## 2. Bounded contexts

Seven contexts, classified DDD-style as core / supporting / generic.

| # | Context | Class | Owns | Boundary signal |
|---|---------|-------|------|-----------------|
| C1 | **Conversation & Probing** | Core | NPC interlocutors, probe selection, dialogue state, turn protocol | Vocabulary: probe, response, turn, interrogator |
| C2 | **Evidence & Provenance** | Core | Evidence artifacts, claims, claim↔evidence links, source ingestion, version history | Vocabulary: artifact, claim, link, source, witness |
| C3 | **Narrative Authoring** | Core | Narrative drafts, compression operations, contradictions, narrative versions, publish gate | Vocabulary: draft, compression, contradiction, publish |
| C4 | **World & Spatial** | Supporting | Memory-palace map, room-to-theme binding, NPC placement, artifact rendering position | Vocabulary: room, palace, placement, threshold |
| C5 | **Quality Evaluation** | Supporting | Fitness functions, genericness scoring, traceability check, eval harness | Vocabulary: score, threshold, gate, fitness |
| C6 | **AI Inference** | Generic | Ollama client, model routing, prompt registry, token streaming, fallback | Vocabulary: model, prompt, slot, fallback |
| C7 | **Identity & Session** | Generic | Local user profile, session resume, save/load | Vocabulary: session, profile, snapshot |

**Anti-corruption layers:** C1↔C6 is brokered through a Prompt Contract object — Conversation does not import LLM specifics. C2↔C3 is brokered through a Claim Reference type — Narrative does not mutate evidence directly.

**Cores get the most architectural attention.** Supporting contexts get well-defined contracts but accept v0.1 simplifications. Generic contexts use off-the-shelf patterns.

---

## 3. Fitness functions

Each is measurable, automated, and tied to a PRD principle. Hard = blocks publish/merge. Soft = warning, telemetry, regression flag.

| ID | Name | PRD ref | Measurement | Threshold | Hard/Soft |
|----|------|---------|-------------|-----------|-----------|
| F1 | **Provenance integrity** | §4.1 | published_claims_with_evidence_link / published_claims | 100% | **Hard** — publish blocked |
| F2 | **Privacy invariant** | §4.4 implicit | Outbound bytes from data-path processes during a session | 0 | **Hard** — CI test, runtime guard |
| F3 | **Genericness ceiling** | §4.4 | LLM-as-judge buzzword/cliché score on every compression output, against banned-vocabulary list + structural patterns | ≤ T<sub>g</sub> *(calibrate empirically; Suki sets initial)* | **Hard** — output rejected, recompose |
| F4 | **Compression efficiency** | §4.3 | specificity-per-100-tokens (unique entities + concrete claims) on final narrative ÷ same metric on single-shot LLM baseline | ≥ 1.3× | Soft |
| F5 | **Latency budget** | §4.2 implicit | Interrogator-turn wallclock on M3 24GB, default model selection | p50 ≤ 4s, p99 ≤ 12s | Soft |
| F6 | **Memory ceiling** | §4.4 implicit | Peak RSS of inference process during a session | ≤ 18 GB | **Hard** — leaves headroom on 24GB target |
| F7 | **Contradiction recall** | §4.2 / 7.6 | Recall on a seeded test set of N user histories with planted contradictions | ≥ 80% at ≥ 70% precision | Soft |
| F8 | **Nuance-preservation** | §4.5 | Diff between user-marked load-bearing detail and final narrative — preserved-detail count / marked-detail count | ≥ 90% | **Hard** — publish blocked |

**These are mandatory test fixtures, not aspirational targets.** Every CI run executes F1, F2, F6 as automated gates. F3, F8 run on every publish action. F4, F5, F7 run nightly against a fixed corpus.

---

## 4. Reversibility ledger

Decisions ranked by cost to change. Easy decisions get fast v0.1 choices. Hard decisions get explicit ADRs.

| Decision | Reversibility | Cost to change | Notes |
|----------|---------------|----------------|-------|
| Local-only LLM (no remote API) | **Easy** | Add a provider adapter + change privacy contract | The contract is the costly part, not the code |
| SQLite vs Postgres | Easy | Alembic migration, ~1 day | SQL stays SQL |
| sqlite-vec for vector search | Easy | Swap to FAISS/Chroma; embeddings preserved | Adapter pattern |
| Ollama vs llama.cpp / vLLM | Easy | Inference adapter swap | Behind C6 boundary |
| Single-process FastAPI monolith | Easy | Standard split when usage demands | v0.1 doesn't need it |
| Banned-words style guide | Easy | Update list, re-run audit | F3 absorbs the change |
| Multi-agent role boundaries (4 roles) | Medium | Prompt rewrite + topology rewire | Cost grows with stored conversation history |
| Phaser 3 as game engine | Medium | UI rewrite, ~1-2 weeks | Game logic separable from rendering |
| Python on backend | Medium | Project-level rewrite if migrating to Node/Go | Most logic is glue, not algorithm |
| TypeScript end-to-end on frontend | Medium | Mid-cost rewrite | Phaser+React are TS-native |
| **Provenance graph schema (C2)** | **Hard** | Migration cost grows linearly with stored claims | This is where ADRs earn their keep |
| **Memory-palace metaphor as primary UI** | **Hard** | Defines product identity per Dash/Vesper | Cuts to "list of probes" if reverted |
| **Multi-agent topology over single-LLM** | **Hard** | Re-architects C1; contradicts driver §1.2 | The topology IS the differentiator |
| **Local-only privacy posture** | **Hard** | Reversal changes regulatory surface, threat model, target user | Don't reverse |

ADR slots required (one per Hard row): ADR-001 Provenance graph schema · ADR-002 Memory-palace primary UI · ADR-003 Multi-agent topology · ADR-004 Local-only posture.

Round A agents add ADRs for their Medium decisions (model selection, framework boundaries, asset pipeline, etc.).

---

## 5. Sacrificial architecture (v0.1 throwaways)

Choices we expect to discard. Naming them reduces emotional cost when the time comes.

| Choice | Throwaway trigger | Replacement direction |
|--------|-------------------|----------------------|
| Single-user, single-process monolith | Multi-user demand | Split inference + API + frontend processes; standard service decomposition |
| Naive vector retrieval (top-K cosine on sqlite-vec) | Narrative quality plateaus | Hybrid retrieval: BM25 + dense + cross-encoder reranker |
| Single-prompt-per-agent role | Behavior demands self-critique loops | Chain-of-thought / reflexion / verifier-prover patterns inside each role |
| Hardcoded NPC roster (4–5 fixed) | Users want to assemble their own interlocutors | NPC marketplace / user-defined personalities |
| File-based session save | Multi-device demand | Cloud sync (would require revisiting §1.4 — privacy posture re-negotiation) |
| Banned-words list as sole genericness signal | Adversarial inputs paraphrase around the list | Trained classifier on positive/negative narrative samples |

**These are not technical debt.** Technical debt is unintentional. Sacrificial architecture is intentional, named, and budgeted.

---

## 6. Architectural drivers → context map

| Driver | Touches | Lives mostly in |
|--------|---------|-----------------|
| §1.1 Auditability as graph | C2, C3 | C2 (provenance) |
| §1.2 Socratic = multi-agent | C1, C6 | C1 (conversation orchestration) |
| §1.3 Signal = fitness function | C5 | C5 (eval as subsystem) |
| §1.4 Local privacy by construction | All | Cross-cutting; enforced in C7 + Devon's deployment |

---

## 7. Slots for Round A

What each Round A agent must produce, and what the spine has already constrained.

### BP-005 — Suki (ML/AI)
**Owns:** C1 + C6 implementation strategy.
**Must produce:** model-per-role assignment, RAM budget table, prompt-strategy doc per role, eval harness wiring (F3, F4, F7), fallback chain when a model OOMs or returns malformed output.
**Pre-constrained:** local-only (§1.4); multi-agent topology mandatory (§1.2); ≥4 distinct roles; F6 hard ceiling 18GB.
**Open question to resolve:** Qwen 2.5 14B q4 vs Llama 3.1 8B Instruct for heavy slot — pick based on contradiction-recall on Suki's test set.

### BP-006 — Priya (Backend)
**Owns:** C2 + C3 + C7 implementation, plus the API surface that connects C1 to the outside world.
**Must produce:** entity-relationship diagram for C2 + C3, SQLite schema DDL with sqlite-vec extension, conversation state machine, FastAPI route map (≤30 endpoints), publish-gate logic that enforces F1 and F8.
**Pre-constrained:** SQLite + sqlite-vec; provenance graph schema is HARD-reversibility (gets ADR-001); single-process monolith for v0.1.
**Open question to resolve:** SQLAlchemy 2.x vs raw sqlite3 + sqlite-vec for the provenance graph. Tradeoff: ORM ergonomics vs vec-extension control.

### BP-007 — Marcus (Frontend)
**Owns:** game-engine ↔ React ↔ backend wiring; the Phaser↔React state bridge contract.
**Must produce:** Zustand store contract shared between Phaser scenes and React components, event protocol for AI dialogue → game-event mapping, asset pipeline (Tiled tilemaps, sprite sources, build flow), backend transport choice (WebSocket / SSE / REST).
**Pre-constrained:** Phaser 3 + React 18 + TS + Vite; Tailwind + shadcn for overlay; Zustand bridge.
**Open question to resolve:** WebSocket vs SSE for streaming LLM output into the game world; latency profile under §F5 budget.

### BP-008 — Dash (Creative Direction)
**Owns:** memory-palace metaphor, NPC roster identities, world tone, every line of UI copy that the user reads.
**Must produce:** room-to-theme map (≥6 rooms aligned to PRD §5 user types), NPC roster (≥4 with distinct probing styles), world-tone document, calibrated voice samples for system messages.
**Pre-constrained:** contemplative + intimate feel (Vesper's non-negotiable); references Disco Elysium / KRZ / Outer Wilds / Hammett; banned tone: coaching/buzzword.

### BP-009 — Vesper (Game / Interaction Design)
**Owns:** core loop, mechanics, pacing, failure modes.
**Must produce:** loop diagram (action → feedback → consequence → next action), spatial layout per room, NPC mechanic spec (what each NPC can/cannot do), failure-mode catalogue (what happens when the LLM hallucinates, when the user disengages, when the metaphor leaks), pacing for the first 90 seconds vs the third return vs the tenth.
**Pre-constrained:** memory-palace metaphor (HARD reversibility — ADR-002); failure design from project memory (coherence yes, evidence loss no); Socratic friction valued.
**Depends on:** BP-008 (Dash — world tone shapes mechanics).

### BP-010 — design-for-ai:design (Visual System)
**Owns:** type, color, motion, accessibility floor, hone checklist.
**Must produce:** type system, color system grounded in mood (contemplative + intimate), motion principles (when does the world animate, when does it stay still), accessibility floor (color contrast, keyboard nav, reduced-motion), pass against `design-for-ai:hone` checklist.
**Pre-constrained:** Tailwind + shadcn as implementation primitive; world-tone from Dash drives palette mood.
**Depends on:** BP-008 (Dash — visual system serves creative direction).

### BP-011 — Devon (DevOps)
**Owns:** local packaging, hardware sizing matrix, privacy posture verification, audit logging.
**Must produce:** docker-compose.yml + native install script, hardware sizing matrix (8 / 16 / 24 / 32 / 64 GB tiers — what runs at each), privacy verification test (F2 automated check), audit log schema, secret strategy (none in v0.1, but documented), degradation strategy below 16 GB floor.
**Pre-constrained:** local-only; no Terraform; GitHub Actions lint+test only; 24 GB M3 is the primary target.
**Open question to resolve:** is the 8 GB tier supportable, or does Signal require a 16 GB floor? This decides addressable user base.

---

## 8. Open spine-level questions (left for Opus synthesis at BP-014)

1. **Conversation persistence model.** Conversations span sessions. Do we re-hydrate the full transcript into the LLM context window each turn (simple, expensive), or summarise+RAG (complex, cheaper)? Decision affects C1, C2, C6 simultaneously.
2. **Contradiction surfacing UX.** When C3 detects a contradiction, does it interrupt the current dialogue, queue a probe for later, or render as a visible tension in the world? Affects C1, C3, C4. Vesper has strong opinions; Dash ratifies.
3. **Evidence ingestion modality.** Free-text typed into NPC dialogue only, OR also: paste a résumé / paste a project description / link to GitHub repos? Each input mode adds parsing and provenance complexity. Defer-list candidate.
4. **Versioning granularity.** Is a "narrative version" a snapshot of all claims at a moment, or a fine-grained diff? Affects C3 storage cost and undo UX.

---

## 9. Style guide reminders for downstream agents

When you write your brief:

- **Cite the spine.** Reference §1, §3, etc. when you make a constrained choice.
- **Cite the PRD.** Every architectural claim links to a PRD section or a fitness function.
- **No buzzwords.** "Robust," "scalable," "leverages," "best-in-class" — banned. Specific verbs and concrete numbers only.
- **Name your throwaways.** If your brief contains a v0.1 simplification, add it to §5 sacrificial.
- **Surface your open questions.** Don't hide them behind hedge words. If you don't know, say so.
- **Length budget.** Round A briefs target 600–1000 words each. Compression is a product principle; embody it.

---

## 10. Definition of done (this spine)

- [x] 4 architectural drivers stated, each linked to a PRD section
- [x] 7 bounded contexts named and classified
- [x] 8 fitness functions, each measurable, with thresholds and hard/soft tags
- [x] Reversibility ledger with ≥10 entries, ≥3 marked Hard
- [x] Sacrificial architecture call-outs ≥4
- [x] Per-Round-A-agent slot definition with pre-constraints and open questions
- [x] Open spine-level questions surfaced for synthesis

This document closes BP-004. Round A (BP-005, BP-006, BP-007, BP-008, BP-011) is unblocked. BP-009 and BP-010 unblock when BP-008 closes.
