---
name: Judge Panel — Adversarial pre-draft review
bead: BP-013 (signal-k2w)
date: 2026-05-09
panel: Mara (UX 40%) · Ravi (Tech 35%) · Sofia (Demo 25%)
under_review: Kenji's MVP cut (BP-012) + integrated picture across 7 Round A briefs
---

## Executive verdict

**Cut more.** The cut is directionally right — multi-agent topology, provenance graph, dual gate, local-only — and the kill list is unusually disciplined. But the integrated picture serializes too many synchronous LLM calls behind a single user turn for F5's p50≤4s to hold on the named 24 GB M3, and the 4-room cut leaves Marlow (no-memory by design) bearing the entire load of the felt-experience proof in turn one. **One change flips us to ship-as-cut:** publish a per-turn LLM call-graph budget — which roles fire synchronously vs deferred vs cached — that mechanically holds F5 *before* implementation starts. Without that arithmetic, BP-014 is synthesizing on optimism.

---

## Mara — UX

**M1. The 7→4 room cut decapitates Dash's user-type coverage. [serious]**
Dash §2 binds each room to a PRD §5 user type. Kenji §1.5 keeps Foyer (TPL), Workshop (architect), Library (staff/principal), Glasshouse (transformation lead) — explicitly drops **Bridge (engineering manager)** and **Switchyard (technical program leader)**, two of seven listed primary user types. Kenji argues Cassady/Lenore can cover the probe needs from their resident rooms. I disagree: Dash made the room *be* the metaphor — a TPL walking into a Library is the wrong felt experience even if the probe class matches. **Fix:** promote to 5 by reinstating the Bridge — lowest-cost room, no resident NPC needed, Vey already drifts there per Vesper §2.

**M2. Glasshouse-as-Vey-default conflates two distinct UX functions. [serious]**
Kenji §1.5 frames Glasshouse as "the empty-room default Vey drifts into." But Dash §2 binds it to *transformation lead* as a user type. Anchoring a homeless contradiction-NPC to a load-bearing user-type room means the transformation-lead user enters their room and finds only contradiction-surfacing — not their primary need. **Fix:** keep Glasshouse as a theme room; let Vey drift into any empty room equally.

**M3. Marlow is a single point of failure for the first-90-seconds hook. [blocker]**
Vesper §4: "The lamp is on. Marlow looks up: 'I don't know you. One sentence.'" Combined with Kenji §3's correct kill of Marlow's cross-visit memory, *every first-time user lands on the hardest probe in the system*. If a user can't produce a one-sentence pitch in 30 seconds, they bounce believing Signal is "an AI that won't accept my answer." Vesper §4 says "turn one accepts anything and pins it" — but this is aspirational, not contractual. **Fix:** synthesis pins this as a Suki-side gate that disables F3 rejection on turn 1, and Dash adds a building-voice orientation beat before Marlow looks up.

**M4. The "feels more accurate" success metric has N=3 but no falsification protocol. [serious]**
Kenji §5: three out-of-team users post-interview. §6 Q6 honestly surfaces the unfalsifiable-failure scenario. But the cut doesn't define *what counts as a "no" that escalates*. One user out of three? Without pre-registration, "feels accurate" decays into subjective debrief under deadline pressure. **Fix:** pre-register. My recommendation: 2/3 "no" delays launch; 1/3 "no" ships with a written postmortem.

**M5. The publish gate's rejection UX is unspecified. [nit]**
Priya §5 returns a `RejectionReport`. Dash §5 voice samples don't include a publish-rejection line. **Fix:** Dash adds the voice sample; Marcus specs the rejection UI. Make rejection a felt experience, not a modal.

---

## Ravi — Tech

**R1. F5 p50≤4s does not hold under Suki's serialized 5-role topology. [blocker]**
Suki §1's per-turn happy path serializes Interrogator (Qwen 14B q4) → Contradiction-detector (Qwen 14B shared) → Evidence-linker (Qwen 7B q4) → Compressor (Llama 3B) → Genericness-judge (Llama 3B shared). Suki's "~3s" is *one model call*, not a turn. Even if the smaller models run at 60–80 tok/s with sub-second TTFT and produce <100-token outputs (~1.5–2s each), three serialized small-model calls + one heavy-model call land at **p50 ≈ 6–9s, p99 ≈ 12–18s wall-clock** before the user sees a complete answer. F5 misses the median, not just the tail. **Fix:** synthesis must specify (a) which calls run *during* user-read of NPC reply (overlapped, free latency), (b) which fire on publish (out-of-band, F5-irrelevant), (c) which are truly turn-blocking. My read: Interrogator is turn-blocking; Detector + Linker run async on the *previous* response while Interrogator generates the next probe; Compressor + Judge fire on publish, not per-turn. Say so explicitly or F5 fails.

**R2. Suki's 17.5 GB RSS does not include 4-hour KV cache growth. [serious]**
Suki §1: peak co-resident RSS = 17.5 GB; F6 ceiling 18 GB; headroom 0.5 GB. Devon §9 Q2 already flags this. Suki's number is *cold-cache*. With `keep_alive: -1` and Qwen 14B KV cache growing toward 8k tokens, marginal KV is ~1–1.5 GB; *we are past 18 GB on the third return visit Vesper §4 specifies*. **Fix:** Suki publishes RSS at session minutes 5/30/120/240. If 240-minute breaches F6, summary+RAG persistence (Kenji Q1 — agree) lands in v0.1 or heavy slot drops to 7B and we eat the F7 hit.

**R3. T_g calibration as "ship with placeholder" makes F3 theater. [serious]**
Kenji §6 Q3 recommends shipping with placeholder + audit-log banner. I disagree. F3 is one of two PRD §4.4 enforcement mechanisms. If T_g is a guess, the gate either rejects everything (user can't publish) or accepts everything (gate is decorative). Suki's κ ≥ 0.78 is *on a comparable task*, not this corpus. A user-visible "calibration in progress" banner is itself a kill-list violation — reads as "AI may make mistakes" boilerplate (design-system §6 forbids). **Fix:** synthesis requires BP-005c gold corpus in week 1–2 of the four-week window, OR F3 is *soft* (advisory, audit-logged) until calibrated and *hard* only post-calibration. "Hard gate with guess threshold" is the worst of both worlds.

**R4. Publish-gate latency is unbounded. [nit]**
Priya §5 is synchronous; Priya §8 lists this sacrificial. Fine for 6–12 claims; on a power user's third return with 30+ claims, F1 + F8 token-presence becomes O(claims × tokens). **Fix:** synthesis sizes the typical/worst-case latency. <500ms ships sync; >2s moves to background worker now, not later.

**R5. SSE cancel semantics hand-waved. [nit]**
Marcus §4: `POST /turn/{id}/cancel` if needed. If user cancels mid-stream while Compressor is running and F3 has rejected, what state does Priya §4's FSM end in? **Fix:** FSM gains a `cancelled` terminal; Suki §4 fallback table adds a "user-cancel mid-stream" row.

**R6. Anti-collapse audit threshold is unprincipled. [nit]**
Suki §2: "cosine > 0.7 = decorative" — on what embedder, what corpus? **Fix:** specify `nomic-embed-text` (Devon §1) and calibrate against a known-decorative baseline (single-prompt-three-times) so 0.7 isn't a vibes number.

---

## Sofia — Demo

**S1. The load-bearing core is invisible-by-design. [blocker]**
Kenji §4's differentiators (30% weight) produce a felt experience that is *the absence of slop*. Showing-the-absence-of-something to a stranger in 90 seconds is the hardest demo category. Compare to chat: I prompt, it streams 200 fluent words, "wow." Signal: I prompt, Marlow says be shorter, I struggle, I get a 22-word claim. Architecturally correct, demo-hostile. **Fix:** synthesis designates one *visible* moment per minute. Candidates: (a) Vey drifts in on a seeded contradiction, (b) publish-gate refusal (building voice: "Two of these claims have no receipts"), (c) genericness-judge reject visible. Pick two; pre-seed the demo session.

**S2. The memory-palace UI is the demo's biggest asset and biggest risk. [serious]**
Marcus §3 ships placeholder Kenney/Mana Seed sprites in v0.1; bespoke art deferred. Dash §1 sells KRZ-grade interiority. Placeholder pixel art reads as "indie game prototype," not "private archive." On stage this is the difference between "what is this" and "I want to know what's in the next room." **Fix:** spend ~3 days art budget on the *Foyer only* — bespoke. Other rooms can stay placeholder. The Foyer is the demo's first frame.

**S3. The 28ms typewriter is the demo's pacing weapon — don't let it fall back. [nit]**
Vesper §3 / Kenji §2: streaming may fall back to whole-line reveal under reduced-motion or back-pressure. Whole-line reveal kills the felt experience — the slow typewriter IS the "this is not chat" tell. **Fix:** demo machine ships with reduced-motion off; back-pressure failure mode reproducible-or-fixed before any external demo.

**S4. There is no demo failure-mode catalogue. [serious]**
Vesper §5 catalogues *user* failures. Devon §2 catalogues hardware tiers. Nobody has catalogued *demo* failures: model OOMs on stage, Ollama unreachable, F2 runtime guard fires on conference Wi-Fi captive portal, Marlow's first response is 18s because the model cold-loaded. **Fix:** demo-readiness checklist — pre-warm models, disable captive-portal probes, three green-room rehearsals, fail-deadly to a recorded video if any rehearsal fails.

---

## Cross-cutting

- **F5 + first-90-seconds (R1 + M3 + S3):** latency budget, Marlow-as-only-greeter, and typewriter pacing are entangled. If R1 is right, Marlow's first 90 seconds *is* a 12–18s wait staring at an empty Foyer.
- **T_g + felt experience (R3 + M4 + S1):** F3 is the load-bearing differentiator; calibrated on a corpus that doesn't yet exist; if it ships miscalibrated, every other gate's value depends on it. Users can't validate F3 — the gate is silent on success.
- **Visible-on-rejection (M5 + S1):** publish-gate success path is invisible-by-design. Both UX and demo cases want a visible-on-rejection moment. Synthesis ratifies rejection-as-felt-experience.
- **Room cut + EM/TPL users (M1 + M2):** Bridge-defer + Glasshouse-as-Vey-default leave EM and TPL unserved at the spatial level even if probe-served — 2/7 of PRD §5.

---

## Pressure-test of Kenji's 6 open questions

1. **Conversation persistence.** Load-bearing. Panel agrees with Kenji's summary+RAG lean (only realistic answer given F6 + Devon §9 Q2).
2. **Contradiction surfacing UX.** Load-bearing. Panel agrees with Kenji's "both" lean — Vey in canvas, margin in narrative editor. Don't add a third popup.
3. **T_g calibration timeline.** Load-bearing. Panel **disagrees** with Kenji — see R3. Either BP-005c lands in week 1–2 or F3 ships soft until calibrated.
4. **Probe rotation budget.** Load-bearing, lower urgency. Agree with Kenji's 5 seeds per NPC; tenth-visit is a v0.2 problem.
5. **Out-of-team user-test logistics.** Load-bearing. Ratify the calendar ask. Pre-register failure threshold per M4.
6. **Unfalsifiable-failure (gates pass, users say no).** Most important question Kenji asks. Agree with his instinct: delay, don't ship. Synthesis must adopt this in writing.

---

## Demo cold-open script — Sofia, 90 seconds, v0.1-as-cut

> **[0:00]** Black. White serif: *"Signal — a memory palace for what you actually did."* Cut to Foyer. Low light, paper-yellow, one warm lamp on a coat rack. No UI chrome.
>
> **[0:08]** Building voice (Inter): *"The lamp is on. Take your time."* Pixel-art Marlow at the door, coat on. Looks up.
>
> **[0:14]** Marlow (EB Garamond, 28ms typewriter): *"I don't know you. In one sentence — what should I have hired you to do, last year?"*
>
> **[0:22]** Demo operator types: *"I led platform architecture for a 200-engineer org and drove transformation across our cloud migration."* Submits. Lamp glows on focus, dims on submit. Marlow pauses (idle breath).
>
> **[0:30]** Marlow: *"That sentence had three jobs in it. Pick the one that pays you."* The first sentence pins to the coat rack — visible artifact. **(Compression test landing as physical state.)**
>
> **[0:42]** Operator: *"I was the technical owner of our migration to Kubernetes for the largest service in the company."* Previous sentence dims; new pins above.
>
> **[0:50]** Door creaks. Vey walks in. **(Pre-seeded contradiction.)** Vey: *"Earlier you said you 'drove transformation.' Now you're describing one service. Which is."*
>
> **[1:05]** Operator pauses. Building voice: *"Two things you said don't sit next to each other."* **(Visible mechanic — what the topology does that ChatGPT can't.)**
>
> **[1:15]** Operator types one corrected sentence. Marlow nods. Building voice: *"Filed. The room remembers."* Coat rack now shows one pinned claim, dated, with a witness ref as marginalia.
>
> **[1:25]** Title card: *"No buzzwords were generated in the making of this narrative. The genericness gate caught seven."* **(Visible counter — turns invisible work into demo evidence.)**
>
> **[1:30]** End.

Critical demo dependencies: pre-seeded Vey trigger; bespoke Foyer art (S2); F3 reject-counter exposed in audit log; cable unplugged on stage (strongest privacy proof).

---

## Score

| Judge | Weight | Score | Rationale |
|---|---|---|---|
| **Mara (UX)** | 40% | **7** | Topology + provenance is the right product; Marlow-as-only-greeter and 4-room cut leave unserved user types; falsification protocol absent. |
| **Ravi (Tech)** | 35% | **6** | Spine sound; F5 p50≤4s does not survive serialized 5-role arithmetic; F6 risks 4-hour KV growth; F3 ships on placeholder. |
| **Sofia (Demo)** | 25% | **6** | Differentiators correct and demo-hostile; needs visible mechanics, Foyer art upgraded, demo failure modes catalogued. |
| **Weighted total** | | **6.5 / 10** | Below Kenji's 8.5/10 self-score by 2 points. |

Kenji's 8.5 reflects MVP-cut discipline (real). Our 6.5 reflects integrated build risk — latency arithmetic, calibration timing, demo legibility. Both correct from their vantage. Synthesis closes the gap by *deciding* on R1 (call-graph budget), R3 (F3 timing), M3 (Marlow turn-1 contract), S1 (designated visible moments) — none require further scope cuts, only specificity.

**The cut is right. The arithmetic isn't done. Make Opus do the arithmetic.**
