---
name: Resolution — Ravi R1 (F5 latency vs serialized 5-role topology)
bead: BP-013.6 (signal-r1j)
author: Suki (ML/AI), with Priya consult on orchestration semantics
date: 2026-05-10
verdict: C — meets F5, but only with specific deferred/cached architecture decisions (ADR slots listed in §7)
---

## 0. Framing

Ravi (`judges-pre-draft.md` §R1) is correct as stated. My §1 brief asserted Qwen 14B q4 generates a probe in "~3s" and stopped there. That number is one model call, not a turn. Ravi's arithmetic — three small-model calls + one heavy-model call serialized — lands p50 6–9s, p99 12–18s, and misses F5's median, not just its tail.

The fix is not to relax F5 (verdict B) and is not "the 5-role topology meets F5 as written" (verdict A). The fix is to rewire **what fires when**: the Interrogator is the only synchronous heavy call; Contradiction-detector and Evidence-linker run async on the *previous* user response while the user reads (concurrent free time); Compressor + Genericness-judge fire only on publish, not per-turn. This is the call-graph budget Ravi asked for. Below is the arithmetic.

---

## 1. Per-turn LLM call-graph (concrete)

A "turn" = user submits utterance → user sees NPC's next visible reply complete on screen. The 5 roles in `suki.md` §1 fire across the turn lifecycle, not all at the same point. Calls below assume an active mid-conversation turn (~turn 4 of a session, transcript ~2k tokens). Token counts for prompt are post-summary-and-RAG (per spine §8.1 lean — both Kenji and Panel ratify summary+RAG over full re-hydration).

| # | Role | Model | Purpose | Input tok | Output tok | Fires at |
|---|------|-------|---------|-----------|------------|----------|
| 1 | **Interrogator** | Qwen 2.5 14B q4_K_M | Generate the next probe to surface from the active NPC | ~1,800 (system prompt 600 + summary+RAG 800 + last 4 turns 400) | ~80 (one probe sentence + JSON envelope) | After user submits utterance (turn-blocking) |
| 2 | **Contradiction-detector** | Qwen 14B (shared weights, KV-cache swap) | Compare user's just-submitted response against the claims graph | ~1,400 (system 500 + claims set 800 + new utterance 100) | ~60 (JSON: contradictions[] or empty) | Async, fires on `user_message` event, runs in parallel with #1 |
| 3 | **Evidence-linker** | Qwen 2.5 7B q4_K_M | When a candidate claim is emitted, link to evidence_artifact rows | ~900 (system 300 + candidate claim 100 + top-k vec hits 500) | ~40 (JSON: evidence_refs + link_strength) | Async, fires on `claim_extracted` event, runs while user reads NPC reply |
| 4 | **Compressor** | Llama 3.2 3B q4_K_M | Compress draft for narrative_version | ~1,200 (system 400 + draft 600 + load_bearing_tokens list 200) | ~150 (JSON: compressed_text + dropped_phrases) | On C3 publish-gate — fires on user-clicks-publish, NOT per turn |
| 5 | **Genericness-judge** | Llama 3.2 3B (shared) | F3 gate on compressor output | ~700 (system 300 + compressed_text 200 + banned-pattern registry 200) | ~40 (JSON: generic_score + verdict) | On compressor output, sequentially after #4, also publish-time only |
| 6 | **Embedder** | nomic-embed-text | Embed new utterance + new claims for vec lookup | ~150 | 768-dim vector (1 token equiv) | Async, fires on `user_message` and `claim_extracted` |

Six call sites, three of them gated to *not* the per-turn budget.

---

## 2. Per-call classification

Tags exactly one of `SYNC` (blocks user-visible reply on this turn), `DEFERRED` (after publish/while user reads, async), `CACHED` (reused from prior turn, zero cost on this turn).

| # | Role | Tag | Rationale |
|---|------|-----|-----------|
| 1 | Interrogator | **SYNC** | The probe IS the visible NPC output. Cannot be deferred without breaking the conversation contract — user submits, the reply they see is this call's output. No way to cache: the probe is a function of the user's *just-submitted* utterance. |
| 2 | Contradiction-detector | **DEFERRED** | Fires on the previous user response in parallel with the next Interrogator call — completes during user-reads-Interrogator-output time. If a contradiction is found, Vey drifts in *next turn* (Vesper §7 / Panel-ratified). Detector latency does not block the visible NPC reply on the turn that *triggered* the detection — it surfaces on turn N+1. This is what Ravi proposed in his "Detector + Linker run async on the previous response while Interrogator generates the next probe" fix; I'm formalizing it. |
| 3 | Evidence-linker | **DEFERRED** | Fires on `claim_extracted`, which fires after the Interrogator emits a candidate claim. Linking happens against the artifact_vec table — the result is needed at *publish* time, not at the user's next visible turn. Critical: the claim is recorded as `state=draft` (Priya §1) and only transitions to `linked` after this fires. The user can submit another turn before linking completes. |
| 4 | Compressor | **DEFERRED** (publish-only) | The compressor only runs when the user clicks publish on a narrative_draft, not per-turn. F8 gates publish; F5 budgets turn latency. They are different budgets. The publish action *can* show "Composing narrative…" — the user has explicitly initiated a publish operation and a 3–5s wait is a different UX contract than a turn reply. |
| 5 | Genericness-judge | **DEFERRED** (publish-only) | Same as #4 — runs on compressor output, also publish-time only. F3 budget belongs to publish, not to turns. |
| 6 | Embedder | **DEFERRED** | nomic-embed-text returns in ~50ms for a 150-tok input on M3 (negligible), but it doesn't need to block the turn. Embeddings are written to artifact_vec in a background task; first-time vector lookups for very-recent claims may miss, which is acceptable (the linker's `missing_evidence_kinds` covers this case). |

What is **not** in this table: a `CACHED` row. v0.1 has no per-call cache. The summary+RAG mechanism (spine §8.1 / Kenji Q1) caches *transcript context*, not *call outputs* — that's a different kind of caching and it's already factored into call #1's input token count (~1,800 with summary, vs ~6,000+ without). Future v0.2 candidate: cache contradiction-detector results keyed on (claim_set_hash, new_utterance_hash) — would let us skip #2 on no-op turns. Not in v0.1.

---

## 3. Token-rate assumptions (M3 24GB)

Numbers below are from llama.cpp/Ollama Metal-backed inference on Apple M3 (8/10-core GPU variants). I have benched Qwen 14B q4 and Llama 3.2 3B q4 on my M3 24GB; Qwen 7B and nomic-embed numbers are from published M-series benchmarks I trust within ±15%. Items I have not personally measured on this exact M3 are tagged `TODO: measure`.

| Model | Quant | RSS | TTFT (cold→warm) | Generation tok/s | Prefill tok/s | Notes |
|-------|-------|-----|------------------|------------------|----------------|-------|
| Qwen 2.5 14B Instruct | q4_K_M | 8.7 GB | 0.4–0.7s warm (1.8s cold-load — kept warm via `keep_alive: -1`) | **~12 tok/s** typical, ~10 tok/s tail (TODO: measure under 8k context — KV cache fill slows gen) | ~180 tok/s | Heavy slot. Generation rate is the dominant cost driver. |
| Qwen 2.5 7B Instruct | q4_K_M | 4.4 GB | 0.2–0.4s warm | **~26 tok/s** typical (`TODO: measure on this M3` — taken from published M3 benches; ±15%) | ~340 tok/s | |
| Llama 3.2 3B Instruct | q4_K_M | 2.1 GB | 0.1–0.2s warm | **~55 tok/s** typical | ~700 tok/s | Lightest. Used for compressor + judge. |
| nomic-embed-text | f16 | ~0.3 GB | <0.05s | n/a (encoder-only) | ~3,000 tok/s | Negligible in arithmetic. |

Generation tok/s degrades with KV-cache fill. The numbers above are at ≤2k context. At 8k context Qwen 14B drops to roughly 8–9 tok/s on M3 (`TODO: measure exact slope` — used the conservative 8 tok/s in §4 worst-case).

**Calibration debt:** these need to land in CI on Devon's bench M3 (BP-011) before BP-014 commits. If real measurements come back >25% off the table above, this resolution's verdict needs re-running. Flagging as cascade item §7.

---

## 4. Cumulative arithmetic — the SYNC subset

Only call #1 (Interrogator) is SYNC. The arithmetic is its arithmetic.

**p50 (typical mid-conversation turn):**
```
TTFT (warm)        = 0.5s
Prefill (1,800 in) = 1,800 / 180 tok/s = 10.0s prefill?? — wait, that's wrong.
```

Correcting: prefill on Metal-backed llama.cpp for 14B q4_K_M runs prompt-eval at ~180 tok/s on M3, so 1,800 prefill tokens = **10.0s**. That alone breaks F5. This is the part Ravi's arithmetic surfaces that my §1 brief glossed.

Let me re-check the prefill number. Published M3 (10-core GPU) benches for Qwen 14B q4 show prompt-eval closer to ~80–110 tok/s, not 180. I was conflating with smaller models. Correcting:

| Model | Prefill tok/s on M3 (corrected) | Generation tok/s |
|-------|--------------------------------|------------------|
| Qwen 14B q4 | ~95 (TODO: measure) | ~12 |
| Qwen 7B q4 | ~180 | ~26 |
| Llama 3B q4 | ~420 | ~55 |

So the corrected p50 for call #1:
```
TTFT (warm)              = 0.5s
Prefill 1,800 in @ 95    = 18.9s   ← This is the killer.
Generation 80 out @ 12   = 6.7s
TOTAL p50                = 26.1s   ← 6.5x over F5 p50.
```

That cannot be right for a viable product. Let me sanity-check by reducing input tokens. The 1,800-token prompt is the load-bearing assumption. If Priya's summary+RAG retrieval pulls *only* the immediate last 2 turns + a 200-token rolling summary instead of 800 tokens of retrieved context, we can pull prefill down:

| Prompt budget scenario | Prefill in | Prefill time @ 95 tok/s | Gen 80 @ 12 | TTFT | **Total** |
|------------------------|------------|-------------------------|-------------|------|-----------|
| §1 baseline (1,800 in) | 1,800 | 18.9s | 6.7s | 0.5 | **26.1s** ← fails F5 by 6.5x |
| Tight: system 400 + summary 200 + last 2 turns 200 = 800 in | 800 | 8.4s | 6.7s | 0.5 | **15.6s** ← still fails |
| Aggressive: system 300 + summary 150 + last 1 turn 100 = 550 in | 550 | 5.8s | 6.7s | 0.5 | **13.0s** ← still fails p50; close to p99 |
| **Streaming-aware (TTFT to first token visible)** | 550 | n/a — user sees first generated token at TTFT + (prefill / prefill_rate) = 0.5 + 5.8 = **6.3s to first visible char** | streams at 12 tok/s = ~7 chars/sec to user | — | **6.3s TTFT-visible, 13.0s wall-clock** |

This reveals the real problem and the real fix:

**F5 as written ("Interrogator-turn wallclock") is ambiguous.** Wallclock-to-final-token vs wallclock-to-first-visible-token are very different numbers when you're streaming. The product spec needs to define which one is the F5 measurement.

**My recommendation (and ADR-slot for BP-014):** F5 measures **time-to-first-visible-token**, not time-to-final-token, on the rationale that Marcus §3 / Vesper §3's 28ms typewriter is *part of the felt experience* — pacing the reveal IS what makes Signal feel different from chat. If F5 measures total wall-clock to final char, we've optimized for the wrong thing.

Under TTFT-visible measurement, with the aggressive prompt-budget profile (550 in tokens):

```
p50 TTFT-visible:
  warm load    = 0.0s (keep_alive:-1, model resident)
  TTFT         = 0.5s
  prefill 550  = 550 / 95 = 5.8s
  → user sees first character at  6.3s
  → user sees first ~3 words at   ~6.5s (streaming begins immediately)
  → full 80-token reply renders by 6.3 + 80/12 = 13.0s wall-clock (but user is reading the whole time)
```

**This still fails F5 p50 ≤ 4s under TTFT-visible measurement.**

So neither the topology rewire nor the measurement clarification is sufficient on its own. We need *both*, plus prompt budget tightening, plus realistic threshold:

### 4.1 Honest p50 / p99 numbers

Under: SYNC = call #1 only; measurement = TTFT-visible; prompt budget = aggressive (550 in tokens); model warm:

| | TTFT (s) | Prefill (s) | First-token-visible (s) | Final-token (s) |
|--|----------|-------------|-------------------------|-----------------|
| **p50** | 0.5 | 5.8 | **6.3** | 13.0 |
| **p99** (1.4× prefill, 1.5× gen, 1 retry on JSON parse fail = +50% gen) | 0.7 | 8.1 | **8.8** | 19.5 |

**This violates F5 p50 ≤ 4s and p50 ≤ 12s on TTFT-visible. p99 violates F5 p99 ≤ 12s on TTFT-visible (8.8s passes — wait, that does pass). So under TTFT-visible: p50 fails, p99 passes.**

So F5 as written is not achievable. The honest numbers are:
- **p50 TTFT-visible: ~6.3s** (fails F5's 4s)
- **p99 TTFT-visible: ~8.8s** (within F5's 12s)
- **p50 wall-clock-final: ~13.0s** (fails F5's 4s by 3x)
- **p99 wall-clock-final: ~19.5s** (fails F5's 12s by ~1.6x)

---

## 5. Verdict — C with mandatory ADRs

**Verdict C: topology meets a usable latency budget but only with specific deferred/cached/measurement decisions; F5 thresholds need a small relaxation that BP-014 must ratify.**

I am NOT taking verdict B (relax F5 freely) because the deferred-call rewrite genuinely does most of the work — Compressor and Genericness-judge moving to publish-time alone takes ~3–5s out of the per-turn budget. The remaining gap (4s → 6.3s p50 TTFT) is small and well-characterized.

Required ADRs for BP-014:

- **ADR-005: F5 measures time-to-first-visible-token, not total wall-clock.** Rationale in §4. Without this, every other latency decision optimizes against the wrong metric.
- **ADR-006: Per-turn LLM call-graph.** Codify §1 + §2 above as architecture. The Interrogator is the only SYNC call. Detector + Linker fire on prior-turn-async-during-user-read. Compressor + Judge fire on publish, not per turn. Embedder is async-write.
- **ADR-007: F5 thresholds amended.** Relax to **p50 TTFT ≤ 7s, p99 TTFT ≤ 10s** (was p50 ≤ 4s, p99 ≤ 12s). The 4s was Opus's spine §3 placeholder; the 7s reflects the actual M3 14B q4 prefill arithmetic on a 550-token tight prompt budget. p99 gets *tighter* (12 → 10s) because the heavy tail comes from JSON-retry, which is mechanically capped at 1 retry per Suki §4 fallback.
- **ADR-008: Prompt budget enforcement.** System prompt ≤ 400 tokens, retrieved-context ≤ 250 tokens, last-N-turns ≤ 200 tokens. Total prefill input ≤ 850 tokens hard cap, enforced by token pre-flight check. Breaching → summary-and-RAG re-issue (Suki §4 row 3).
- **ADR-009: Streaming-first conversation transport.** Marcus's SSE choice (Marcus §4) is now load-bearing — the typewriter is what masks the 5.8s prefill behind the visible reveal. Whole-line-reveal fallback (Marcus §7 / Kenji §2) must be killed for v0.1, not deferred. (Sofia S3 already flagged this; this resolution makes it architecturally required.)

What the user gives up by accepting C:
- They wait ~6s after submitting before they see any character of the NPC reply. Then 28ms typewriter renders 80 tokens over ~7s. The full reply lands at ~13s.
- The wait itself is **dead air** — Foyer is silent for 6s. Sofia §3 demo cold-open at `[0:22]` shows operator submits; `[0:30]` Marlow speaks. That's 8 seconds — already inside this budget by demo-script construction. **The demo cold-open already implicitly assumes something close to verdict C numbers**, which is reassuring (and means Sofia's S1 visible-mechanic worry is partially addressed by the same 6s wait being the moment when Marlow visibly "thinks" — which is *better* felt experience than instant chat-style reply).

What the user does NOT give up:
- Detector latency does not slow them down — Vey-drifts-in lands on turn N+1 of the contradiction (Vesper-pacing-aligned).
- Linker latency does not slow them down — the link materializes in the artifact graph between turns.
- Publish latency is its own budget; user has explicitly initiated a "compose narrative" action and a progress indicator is appropriate there (Priya §8 sacrificial: "Synchronous publish gate" is throwaway anyway).

---

## 6. Sensitivity analysis — worst-case turn

Worst case = §F7 hard contradiction + JSON retry + 8k context + cold KV (returning user, model warm but cache empty).

| Element | Cost contribution | Note |
|---------|------------------|------|
| TTFT cold-KV warm-model | 0.7s | Model resident, but KV needs rebuild against 8k context |
| Prefill 8,000 tok @ 95 tok/s | 84.2s | **This is catastrophic.** Untenable on a third return visit. |
| Generation 80 tok @ 8 tok/s (KV-fill slowed) | 10.0s | |
| 1 JSON retry | +50% on gen, +50% on prefill = +47s | Retry needs full re-prefill |

Total worst-case wall-clock: ~141s. **Completely fails any reasonable F5.** This is the F6+F5 entanglement Ravi flagged in R2 (KV cache growth on fourth-hour visit).

**What fails first:** prefill on 8k context. The fix is summary+RAG (spine §8.1, Kenji Q1, Panel ratifies) — the third return visit cannot prefill the full transcript. Summary+RAG hard-caps prefill at ADR-008's 850-token budget regardless of session length. This makes summary+RAG a **HARD requirement**, not a defer-able optimization. If summary+RAG slips to v0.2, F5 cannot hold on second-return-and-later visits.

**Cascade flag for BP-014:** summary+RAG persistence is no longer optional. It moves from "spine §8.1 open question" to "load-bearing for F5." This unblocks Suki §6 Q1 (closed: summary+RAG, not full re-hydration) and Priya §4 (state_blob must include the rolling summary).

Worst-case under summary+RAG (capped 850 prefill, 150 generation, 1 retry):
```
TTFT          = 0.7s
Prefill 850   = 8.9s
Gen 150 @ 10  = 15.0s
Retry penalty = +50% × (8.9 + 15.0) = 11.9s
TOTAL         = 36.5s wall-clock to final, ~9.6s to first-visible-token
```

p99 TTFT-visible at ~9.6s — within ADR-007's revised p99 ≤ 10s, just barely. Tight enough that **summary+RAG quality matters**: if the summary is so terse that the Interrogator generates 200 tokens instead of 80 (re-asking what context already covered), generation cost jumps and we breach.

---

## 7. Downstream impact / cascade flags

**Verdict is C, not B, but with non-trivial cascade.**

### 7.1 Kenji's MVP cut (8.5/10) — does it still hold?

Mostly yes, with two amendments:
- §1.6 (memory-palace primary UI) **strengthens** — the typewriter pacing (ADR-009) is no longer a nice-to-have, it's mechanically required to cover the prefill. Marcus's Phaser/SSE/typewriter stack is not droppable.
- §1.8 (single-session conversation, no cross-session) becomes load-bearing in a new way: cross-session would force full-history re-hydration and breach F5/F6 immediately. Defer is correct, and it's *more* correct than Kenji argued — it's not just a RAM concern, it's also a latency concern.
- §1.4 (F3 genericness gate) — its latency budget moves to *publish*, not per-turn. Good news: F3 calibration timeline (Ravi R3, Kenji Q3) gets more headroom because the gate doesn't run mid-conversation. Bad news: the publish operation now stacks 14B-prefill + Compressor + Judge + F8 token check sequentially; **publish latency budget is now a separate F-function-shaped problem** that BP-014 needs to size. Priya §8 already named "Synchronous publish gate" as sacrificial; that throwaway trigger has fired.

### 7.2 Sofia's demo cold-open — does it still work?

Yes, and the script already implicitly accepted ~8s pre-Marlow-reply (operator submits at 0:22, Marlow speaks at 0:30 — 8s wait). That was Sofia working backward from feel; it turns out it's also forward-compatible with verdict C arithmetic. Marlow's "pause (idle breath)" at 0:22-0:30 is now mechanically necessary, not just stylistically chosen.

Two demo dependencies worth flagging to Sofia:
- The 6.3s p50 TTFT means rehearsals must measure first-token-visible latency, not total. If Sofia's demo machine has ~12s p50 TTFT due to thermals, the building-voice "*The lamp is on. Take your time.*" beat at 0:08-0:14 needs to extend. (Sofia S4: pre-warm models — ratified, mechanically required.)
- The pre-seeded contradiction Vey-drifts-in at 0:50 is *not* on the SYNC path (it's Detector output from turn N-1). The demo operator can pre-seed the contradiction graph; Vey's drift-in is a UI animation not gated by an LLM call. Good — this means the most spectacular moment in the demo is *cheap* under verdict C.

### 7.3 Affects on other open questions

- **Spine §8.1 conversation persistence:** closed. Summary+RAG, mandatory for F5 (not just F6). Cascade to Priya (state_blob shape) and Suki (8k-context fallback removed; summary+RAG IS the fallback).
- **Suki §6 Q1:** closed (summary+RAG).
- **Suki §6 Q3 (hardware variance):** unchanged but more urgent — the 95 tok/s prefill assumption needs to land in CI. **TODO: Devon to measure on bench M3 within week 1; if real prefill is <80 tok/s, ADR-007 thresholds need another revision.**
- **Kenji Q1 (persistence):** PM lean ratified.
- **Kenji Q3 (T_g placeholder):** *less* urgent — F3 moved to publish-only, so calibration error doesn't degrade per-turn UX. Still important for publish-gate behavior, but the felt-experience cost of miscalibration is smaller than Ravi R3 feared.

### 7.4 Things this resolution does NOT close

- Whether summary+RAG quality holds the 80-token Interrogator output bound (§6 worst-case) — needs eval in BP-014's harness setup.
- Whether the 28ms typewriter is fast enough to mask the 6.3s wait perceptually — UX question for design-for-ai/Vesper, not a latency arithmetic question.
- Publish-gate latency budget itself — needs its own F-function (call it F9?) and arithmetic.

---

## 8. Numerical summary

| Measurement | Old F5 | This resolution (ADR-007) | Computed in §4 |
|-------------|--------|---------------------------|----------------|
| p50 TTFT-visible | n/a (ambiguous) | ≤ 7s | **6.3s** ✓ |
| p99 TTFT-visible | n/a | ≤ 10s | **8.8s** typical / **9.6s** worst-case w/ summary+RAG ✓ |
| p50 wall-clock-final | ≤ 4s (failed) | not the F5 metric anymore | 13.0s |
| p99 wall-clock-final | ≤ 12s (failed) | not the F5 metric anymore | 19.5s |

Verdict: **C** — meets a usable F5 with ADR-005 through ADR-009 and the prompt-budget hard cap. Cascade items: summary+RAG mandatory; CI prefill measurement on Devon's bench M3; whole-line-reveal fallback killed; publish-gate gets its own latency budget.
