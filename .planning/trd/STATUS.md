# Signal — TRD Process Status (resume bookmark)

**Last updated:** 2026-05-10
**Phase:** Round A & A.5 closed; voice tool shipped; Kenji MVP cut closed; Judge Panel pre-draft closed (verdict: cut more, 6.5/10); Suki BP-005c corpus delivered (30 synthetic + 10 public, T_g initial 0.30); **judge-flagged blockers (R1 latency / M3 orientation / S1 demo) + UV methodology gap (M4 elevation) + room-cut governance gap (M1+M2 elevation under Rule B) now formally encoded as resolution beads + folded signoff gate (BP-013.6 / 013.7 / 013.8 / 013.10 / 013.11 / 013.9). BP-014 synthesis blocked on TWO parallel chains: corpus (b0d → g3d) and architecture+methodology+governance (R1+M3+S1+UV+M1M2 → zph).**

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
| BP-005b | signal-b0d | 2 corpus | **user** | **○ READY** |
| BP-005c | signal-kv5 | 2 corpus | suki | ✓ closed |
| BP-005d | signal-4cd | 2 tooling | suki/opus | ✓ closed |
| BP-006 | signal-k9x | 2 backend | priya | ✓ closed |
| BP-007 | signal-0t6 | 2 frontend | marcus | ✓ closed |
| BP-008 | signal-a9w | 2 creative | dash | ✓ closed |
| BP-009 | signal-c1m | 2 game-design | vesper | ✓ closed |
| BP-010 | signal-16f | 2 visual | design-for-ai | ✓ closed |
| BP-011 | signal-iep | 2 devops | devon | ✓ closed |
| BP-012 | signal-trq | 3 pm | kenji | ✓ closed |
| BP-013 | signal-k2w | 3 review | judges | ✓ closed |
| BP-013.5 | signal-g3d | 3.5 corpus-gate | **user** | ○ blocked by b0d (kv5 ✓) |
| BP-013.6 | signal-r1j | 3.6 R1 latency | suki | **○ READY** |
| BP-013.7 | signal-b5x | 3.7 M3 orientation | dash | **○ READY** |
| BP-013.8 | signal-aar | 3.8 S1 demo | kenji | **○ READY** |
| BP-013.10 | signal-sd9 | 3.10 UV methodology | kenji | **○ READY** |
| BP-013.11 | signal-ne9 | 3.11 M1/M2 rooms governance | dash | **○ READY** |
| BP-013.9 | signal-zph | 3.9 blocker-gate | **user** | ○ blocked by r1j, b5x, aar, sd9, ne9 |
| BP-014 | signal-59z | 4 synthesis | opus | ○ blocked by g3d, zph (corpus + architecture chains) |
| BP-015 | signal-499 | 5 drafting | haiku | ○ blocked by 59z |
| BP-016 | signal-1zg | 6 qa | judges | ○ blocked by 499 |
| BP-017 | signal-wwu | 6 qa | simplify | ○ blocked by 499 |
| BP-018 | signal-d8q | 7 final | opus | ○ blocked by 1zg, wwu |
| BP-019 | signal-v5f | 8 spawn | opus | ○ blocked by d8q |

`bd ready` shows currently unblocked work. `bd show <id>` for details. `bd dep tree <id>` to visualize.

## Currently ready (4 beads, all P0)

**Corpus chain:**

1. **BP-005b `signal-b0d` (user)** — author 5 gold personas via voice-interview tool. Use `tools/interview/run.py` (see Quickstart in `tools/interview/README.md`). SPEC at `.planning/trd/test-corpus/SPEC.md`; 2 sample gold personas in `.planning/trd/test-corpus/gold/`. **Blocks BP-013.5 signoff → BP-014 synthesis.**

**Architecture + methodology chain (parallelizable, can dispatch as sub-agents):**

2. **BP-013.6 `signal-r1j` (suki)** — resolve Ravi R1: per-turn LLM call-graph budget vs F5. Deliverable: `briefs/resolution-r1-latency.md` with concrete arithmetic and verdict A/B/C. **Highest-likelihood-of-news-changing-cut.** May force F5 relaxation, which cascades to Kenji's MVP cut and Sofia's demo.
3. **BP-013.7 `signal-b5x` (dash)** — resolve Mara M3: first-90-seconds orientation design. Deliverable: `briefs/resolution-m3-orientation.md` with literal timestamped narration + first-NPC decision + failure-mode coverage.
4. **BP-013.8 `signal-aar` (kenji)** — resolve Sofia S1: demo legibility. Deliverable: `briefs/resolution-s1-demo.md` with pasteable 60-90s cold-open + designated visible moments per differentiator + demo failure-mode plan.
5. **BP-013.10 `signal-sd9` (kenji)** — resolve M4 + cohort gap: pre-registered user-validation methodology. Deliverable: `briefs/resolution-uv-methodology.md` with cohort N defended-or-revised, pre-registered success/failure criteria per PRD §9 metric, and a verbatim-quotable falsification statement. **The validation-truth gate.** Without pre-registration, "feels accurate" decays into post-hoc subjective debrief.
6. **BP-013.11 `signal-ne9` (dash)** — resolve M1/M2 + room-cut governance under Rule B (lesson #8). Deliverable: `briefs/resolution-m1m2-rooms.md` with room-count decision (4/5/6/other), Glasshouse-role decision, and — if holding at 4 — an explicit override doc per Rule B (cost named, value justification, Mara-objection-on-the-record, judge-panel re-acknowledgment hook). **Governance precedent.** Establishes how future spine-Soft-constraint overrides get tracked.

**Manual gates (P0, will become ready when their dependencies close):**

- **BP-013.5 `signal-g3d` (user)** — corpus signoff. Blocked by b0d only (kv5 already closed).
- **BP-013.9 `signal-zph` (user)** — blocker-resolution + methodology + governance signoff. Blocked by r1j + b5x + aar + sd9 + ne9. Two gates intentionally parallel and decoupled: corpus quality (g3d) is a different judgment domain from architectural truth (zph), so each chain progresses independently. Per user decisions (2026-05-10), UV methodology and M1/M2 governance both folded into zph rather than getting their own gates.

## BP-005c corpus delivered (Suki, kv5 closed 2026-05-10)

Files at `.planning/trd/test-corpus/synthetic/` (30 personas) and `public/` (10 figures). INDEX.md per directory; full session notes at `SUKI-BP-005C-NOTES.md`.

**Synthetic shape distribution achieved:** stated-vs-admitted 4 · title-vs-work 5 · evidence-light-influence-heavy 5 (HARD) · sparse-narrative-rich-evidence 4 (HARD) · contradictory-praise 5 (HARD) · domain-pivoter 4 · burnout-and-return 4. Hard-case total **14/30** (target ≥12). One double-shape (synth-014 Felix C.).

**Synthetic seniority:** staff=5 (target 6, slight under), principal=11 (target 10, slight over), director=7, vp=7. Suki declined the rewrite — staff personas are load-bearing on sparse-narrative-rich-evidence (hardest F8 territory).

**Public-figure picks:** Hopper, Knuth, Hamilton, Dijkstra, Shannon, Liskov, Engelbart, Bush, Lovelace, Sagan. 8 deceased, 2 living (Knuth, Liskov) with substantial autobiographical record. Gender 4/6 W/M. Era 1815–2025. Source-material citations in each file.

**T_g recommendation: 0.30** (down from Suki's brief placeholder of 0.35) — corpus's hard-case shapes are exactly where the compressor will reach for buzzwords, so T_g must force back to specifics. Empirical calibration expected to land 0.25–0.32. Cross-persona "always-banned" floor is 5–8 phrases ("transformational," "drove [X]," "best-in-class," "thought leader," "championed," "scaled the [X]"). Per-persona lists carry the long-tail.

**Main-thread spot-check (not full signoff — that's g3d):** sampled `synth-004-david-r.md` (sparse-narrative) and `public-001-hopper.md`. Both pass SPEC discipline — authentic first-person voice with stumbles/hedges, ground-truth contradictions are real (David's claimed sparse career vs his actually-rich evidence; Hopper's documented self-corrections of bug-coinage and COBOL-motherhood legend), source citations in public bios are specific and verifiable. Not slop. Full signoff is still required at g3d before synthesis.

**Specific failure modes Suki flags for BP-014 to test:**
- "I will not endorse the framing" pattern (Hopper, Liskov, Bush, Sagan, Knuth refuse external praise)
- "Metric-with-disclaim" pattern (Priya S., Anders R., Omar K., Bea L., Marisol C. give a strong outcome and immediately disclaim attribution)
- Voice preservation under compression (David R.'s "I just kept fixing things" must not sand to "spearheaded reliability initiatives")

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

Two parallel chains feed BP-014. Both must clear before synthesis runs.

```
   CORPUS CHAIN
   ┌── BP-005b User gold-set ──────────┐
   │                                    ├──→ BP-013.5 g3d (user signoff) ──┐
   └── BP-005c Suki synthetic ✓ ───────┘                                    │
                                                                            │
   ARCHITECTURE + METHODOLOGY + GOVERNANCE CHAIN                            │
   ┌── BP-013.6 r1j: Ravi R1 latency arithmetic       (suki)  ─┐            │
   ├── BP-013.7 b5x: Mara M3 first-90s orientation     (dash)  ┤            │
   ├── BP-013.8 aar: Sofia S1 demo legibility          (kenji) ┤            │
   ├── BP-013.10 sd9: M4 user-validation methodology   (kenji) ┼─→ BP-013.9 │
   └── BP-013.11 ne9: M1/M2 room-cut governance (Rule B)(dash) ┘   zph     │
                                                                  (user)    │
                                                                  │         │
                                                                  ↓         ↓
                                                            BP-014 Opus synthesis (ADRs, risk, fitness)
                                                                  ↓
                                                            BP-015 Haiku TRD draft
                                                                  ↓
                                                            BP-016 Judges post-draft  ──┐
                                                                                        ├──→ BP-018 Opus final ──→ BP-019 spawn product beads
                                                            BP-017 simplify ────────────┘
```

Closed upstream: BP-012 Kenji MVP cut ✓ · BP-013 Judges pre-draft ✓ · BP-005c Suki corpus ✓.

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

**Next architectural actions (parallel):**

1. **User authors gold-set (b0d).** Voice-interview tool ready. Five personas. Blocks corpus signoff (g3d).
2. **Dispatch Suki for R1 latency resolution (r1j).** Highest-leverage architecture work — may force F5 relaxation, which cascades to Kenji's MVP cut, Sofia's demo, and Dash's room-count math. Should land first among the architecture beads.
3. **Dispatch Dash for M3 orientation resolution (b5x).** Independent of R1; can run in parallel.
4. **Dispatch Kenji for S1 demo resolution (aar).** Coordinates with M3 (first 90s of a session and first 90s of a demo overlap). Read M3's resolution first if it lands first.
5. **Dispatch Kenji for UV methodology (sd9).** Independent of R1/M3/S1. Pre-registration discipline is purely PM territory.
6. **Dispatch Dash + Kenji for M1/M2 room-cut governance (ne9).** Coordinates with M3 (rooms anchor the orientation experience). Decision could change room count from 4, which cascades to Vesper room layout, Marcus assets, Kenji budget. Open-ended — Dash + Kenji weigh M1's room-as-metaphor argument against the original cost rationale and choose with full justification (no auto-acceptance of Mara's recommendation).

Once b0d closes, user runs corpus signoff (g3d). Once R1+M3+S1+UV+M1M2 close, user runs blocker/methodology/governance signoff (zph). When both gates close, BP-014 Opus synthesis fires with: full corpus + Kenji's cut + judges' objections + five resolution documents. Synthesis still needs to:
- Calibrate F3 (genericness ceiling T_g) against the actual gold/synthetic/public corpus
- Answer Kenji's 6 open questions (panel already pressure-tested which are load-bearing — see `briefs/judges-pre-draft.md`)
- Integrate the five blocker/methodology/governance resolutions into ADRs and a final fitness-function table (especially if R1 verdict is B and F5 relaxes; or if M1/M2 reinstates rooms and budget shifts)
- Produce a **Spine constraint precedence ledger** ADR (Hard / Soft / Negotiable classification of every spine "Must produce" line, plus override-path text per type — see BP-014 notes for full requirement)
- Produce ADRs, risk register, and final fitness thresholds for the TRD draft (BP-015 Haiku)

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
4. **Sub-agent sandbox blocks `bd close`.** Background sub-agents (e.g., Suki on BP-005c) cannot run `bd close` due to the harness's permission policy. Pattern: agent reports completion, main thread runs `bd close` with the reason the agent supplied. Verify with `bd show` after.
5. **Track blocker-resolution as rigorously as artifact-completion.** When the judge panel (or any review gate) flags blocker-severity objections, those blockers MUST get explicit resolution beads with falsifiable deliverables that gate downstream work — not a tacit "the next person upstream will figure it out at synthesis time." Otherwise the optimism the reviewer was protesting against gets baked in. Discovered 2026-05-10: g3d corpus-signoff existed but no equivalent gate existed for the three judge-flagged architecture blockers (Ravi R1 latency, Mara M3 orientation, Sofia S1 demo legibility). Fix: BP-013.6/7/8 resolution beads + BP-013.9 signoff gate added in parallel to the corpus chain. **Generalize:** any future judge / reviewer / panel output that includes "blocker"-severity objections should generate a dedicated resolution bead per blocker before downstream work proceeds, not be treated as an input to synthesis.
6. **Two parallel signoff gates over one bundled gate.** When two independent quality concerns block the same downstream work (e.g., corpus quality vs architecture-blocker resolution at BP-014), keep the gates separate. Bundling them means a single rejection on one stalls the other; separating lets each chain progress independently and surfaces precisely which gate failed if downstream stays blocked.
7. **Severity ratings are starting points, not floors.** The judge panel rated Mara M4 (cohort sizing + falsification protocol) as "serious" rather than "blocker," which caused the first blocker-sweep to miss it. Discovered 2026-05-10 (user surfaced): for an experiential product whose main claim is felt, the validation methodology IS the truth condition of the claim, so M4 is load-bearing in a way the panel's severity scale didn't capture. **Generalize:** when sweeping for blockers, also re-read every "serious" objection through the lens of *whether the failure mode it names is load-bearing for the product's truth claim*, not just whether the panel said "blocker." Severity is the panel's inference; load-bearing-ness is the product's actual structure. Applied retroactively the same day to Mara M1+M2 (room-cut decapitates user-type coverage; Glasshouse role conflation) — both rated "serious" but trace to the load-bearing room-IS-metaphor mechanic. Elevated to BP-013.11 resolution bead.

8. **Spine constraints are Soft-by-default unless marked HARD; PM cuts that touch Soft constraints require explicit override docs (Rule B).** Discovered 2026-05-10 (user surfaced) when Kenji's MVP cut overrode `spine.md:164` (Dash's ≥6-rooms requirement) by going to 4 rooms with only a one-line acknowledgment in the defer list, no ADR-class override doc. Spine line 170 already uses an explicit "HARD reversibility — ADR-002" marker for Vesper's memory-palace metaphor — convention exists but is applied inconsistently. **The rule (Rule B):**
   - **Hard** (marked explicitly in spine, e.g., "HARD reversibility — ADR-XXX"): override requires spine revision + judge re-review as a separate process beat. Cannot be overridden by a later role brief alone.
   - **Soft** (no marker; default for "Must produce" lines): override requires an explicit ADR-class override doc — name the spine line, justify under what value, name the cost concretely, get judge-panel re-acknowledgment. Tracked as a deliverable, not a footnote.
   - **Negotiable** (introduce explicit "negotiable" annotation in spine for genuinely flexible constraints): override is fine without ADR; just note in role brief.
   **Generalize:** any future PM cut that touches a "Must produce" line in spine must produce an explicit override doc unless the constraint is marked Negotiable. Stealth-overrides via defer-list footnotes count as governance failures and should be reopened. The full Hard/Soft/Negotiable classification across all spine constraints is a required ADR for BP-014 synthesis (the "Spine constraint precedence ledger") — added to BP-014's notes 2026-05-10.

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
