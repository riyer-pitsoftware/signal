---
name: Resolution — Sofia S1 (demo legibility for load-bearing differentiators)
bead: BP-013.8 (signal-aar)
date: 2026-05-10
owner: Kenji (PM, primary)
collaborator: Dash (creative — voice + sensory texture)
supersedes: judges-pre-draft.md §"Demo cold-open script — Sofia, 90 seconds, v0.1-as-cut" (lines 92–116)
---

## Why Sofia's draft failed (one paragraph, then move on)

Sofia's cold-open shows Marlow asking, the user trying, Vey drifting in, the building filing the result. It is correct shape. It fails because the **two beats that distinguish Signal from a chat UI with a memory feature** — the publish gate refusing a claim *and the user seeing the refusal* — are missing. Vey's contradiction lands as dialogue, not as a *system refusing to ship*. The closing buzzword counter is a stat card; stat cards are what AI demos do. The demo earns "interesting room" but not "this is not the same product as ChatGPT-with-a-character." We need a moment where **the system says no** in a way only Signal's architecture can say no — claim → no receipt → publish refused, on stage, watchable.

---

## 1. The cold-open — pasteable narration (90 seconds)

**Cast.** ONE demonstrator (DEMO). Audience watches a screen. No co-presenter. The demonstrator types live; the screen is mirrored.

**Pre-seed (off-stage, before doors open).** Local Signal session has three pre-existing artifacts pinned in Workshop from a prior session, in this order:
1. *"Avoided org politics during 2024 platform rewrite."* — pinned 14 days ago, witnessed by `slack-thread-eng-leads-2024-q3.txt`.
2. *"Drove transformation across cloud migration."* — pinned 9 days ago, **no witness, no artifact link** (deliberately seeded as a generic, unwitnessed claim — F1 will refuse this on publish; F3 will catch the genericness).
3. *"Decided which 2 of 14 services migrated to Kubernetes first; documented the call in `migration-rfc-007`."* — pinned 3 days ago, witnessed.

The audience does not know any of this. They will see it surface.

**Stage state.** Demo machine cable-unplugged from the network (`signal privacy audit` open in a corner panel reads `outbound bytes since boot: 0`). Reduced-motion off. Models pre-warmed.

---

> **[t=0s] [VISUAL]** Black screen. White serif (EB Garamond, 28px), centered, fades up over 600ms:
>
> > *Signal. A memory palace for what you actually did.*
>
> **[DEMO]** *(quiet, doesn't oversell)* "This is Signal. It runs on this laptop. The cable's out."
>
> **[t=6s] [VISUAL]** Cut to Foyer — paper-yellow `--paper`, single warm `--lamp` glow on a coat rack stage-right. Marlow, pixel-art, coat on, at the door. No UI chrome. A small `audit:0↑0↓` chip lives in the bottom-right corner the whole demo.
>
> **[t=10s] [BUILDING VOICE]** *(Inter, fade-in not typed)* "The lamp is on. Take your time."
>
> **[DEMO]** "I'm going to walk into the Workshop. There's work pinned there from last week."
>
> **[t=15s] [VISUAL]** Camera pans 240 px/s left to Workshop. 480ms cross-dissolve at threshold. Cassady is at the bench, back to camera. Three pinned cards on the schematic board — their text is **legible from the audience seats**. Cards 1 and 3 have a small `—` glyph in `--shadow` next to a date. Card 2 has nothing in that slot.
>
> **[t=22s] [DEMO]** *(reading off card 2)* "I want to publish this one — *'drove transformation across cloud migration.'* Let's see what happens."
>
> Demo clicks card 2. Right-side `Publish` affordance is a single line of plain text in `--lamp`: `publish this claim`.
>
> **[t=26s] [DEMO]** Clicks it.
>
> **[t=27s] [VISUAL]** **The card does not move.** Lamp on the bench dims one notch. Building voice writes, line by line, 28ms typewriter, in `--ember`:
>
> > *"This claim has no receipt. The Library has nothing in its name."*
> >
> > *"And: 'drove transformation' is a sentence anyone can say."*
> >
> > *"Out the front door, this becomes someone else's résumé."*
>
> **[t=38s] [DEMO]** *(beat — let it land)* "Two refusals. One for missing evidence. One for sounding like everyone else. The system won't publish this. I can't override it from the UI."
>
> **[t=44s] [VISUAL]** A small `RejectionReport` panel slides in 200ms from stage-right. Two rows, monospace (Berkeley Mono):
>
> ```
> F1  provenance        FAIL   no claim_evidence_link
> F3  genericness       FAIL   T_g 0.71 > 0.35
>                              ("drove transformation" matched
>                               banned-vocabulary list)
> ```
>
> **[DEMO]** "F1 is the receipt gate. F3 is the genericness gate. Two different judges had to agree this could ship. Neither did."
>
> **[t=58s] [VISUAL]** Demo clicks card 3 — *"Decided which 2 of 14 services migrated to Kubernetes first; documented the call in `migration-rfc-007`."* Hovers `publish this claim`. Hesitates one second. Clicks.
>
> **[t=62s] [VISUAL]** Card 3 lifts off the schematic board, holds mid-air 240ms, then slides through the doorframe. As it crosses the threshold, a thin line draws in `--lamp` from the card to a small **document icon** that materializes labeled `migration-rfc-007` — the provenance link, drawn live. Building voice (Inter, no `--ember` this time):
>
> > *"Filed. The claims have receipts. The receipts have rooms."*
>
> **[DEMO]** "That arc you just saw? That's the provenance graph. Every published claim has to be tied — physically — to something in this house."
>
> **[t=75s] [VISUAL]** Door creaks (text only — *(door)* in `--shadow`). Vey enters from stage-right, drifts toward card 1 — *"avoided org politics during 2024 platform rewrite"* — and stops between it and card 3. A faint `--ember` line appears between the two cards. Vey, 28ms typewriter:
>
> > *"Earlier you said you avoided politics. The RFC has you on it. Which is."*
>
> **[t=85s] [DEMO]** *(half-smile, doesn't answer)* "She's not wrong. There's a contradiction in my own work history I haven't reconciled. The system already knew. It was waiting for me to come back."
>
> **[t=90s] [VISUAL]** Hold on Foyer + Workshop split-frame. Audit chip still reads `outbound bytes since boot: 0`. Cut to title:
>
> > *Signal. A memory palace for what you actually did.*
>
> **[END.]**

---

## 2. Designated visible moments per minute

For each load-bearing differentiator: the **second** the audience sees it operate, and **what is visually onscreen** at that second.

| Differentiator | Visible at | What the audience sees | Mechanism on stage |
|---|---|---|---|
| **Dual publish gate (F1 + F8 / here F1 + F3)** | **t=27s–55s** | Card refuses to leave the board. Building voice writes two refusal lines in `--ember`. `RejectionReport` panel surfaces F1 + F3 as named, separate gates. | This is the **holy-shit moment.** See §6. |
| **Genericness gate (F3) — "before/after"** | **t=33s** (refusal cited) and **t=62s** (the *good* claim — already specific — passes) | Audience sees the **same publish action** taken twice: once on a generic phrase that's refused with an explicit `T_g 0.71 > 0.35`, once on a specific phrase that passes. Before/after is implicit by adjacency. | F3 score visible in `RejectionReport`; banned-vocabulary match is named. |
| **Provenance graph** | **t=62s–72s** | Card 3 physically traverses the doorframe; a `--lamp` line draws live from the card to the `migration-rfc-007` document icon. The link is **drawn** as a stroke, not asserted as a label. | C2 schema's `claim_evidence_link` rendered as a literal connecting line at publish-time. |
| **Multi-agent topology** | **t=44s** (RejectionReport names two judges) and **t=75s–85s** (Vey enters) | Audience sees that **F1 and F3 are separate gates** (two named verdicts, not one composite "AI says no"). Then Vey, a *third agent*, enters as a different physical character with a different probe class — not as a voice from the same Marlow box. | The topology is legible because **distinct system actors take distinct visible actions**: Cassady's room as the stage, the building voice as the gate, Vey as the contradiction-detector embodied. Multi-agent is shown as multi-actor, not explained as multi-model. |

**Rule of thumb the demonstrator follows:** every 15–20 seconds, *something the audience can point at* must change because *Signal's architecture made it change.* If 20 seconds pass with only the user typing, the demo collapses into "person types into chat."

---

## 3. Beat-by-beat storyboard

Eight beats over 90 seconds. Per beat: **VISIBLE** / **AUDIBLE-OR-TEXTUAL** / **DEMONSTRATOR LINE** / **BACKSTAGE** (what the system is actually doing).

| # | t (s) | VISIBLE | TEXTUAL | DEMO LINE | BACKSTAGE |
|---|---|---|---|---|---|
| **1** | 0–10 | Black → Foyer fade-up. Lamp lit. Marlow at the door. Audit chip `0↑0↓` corner-bottom. | "Signal. A memory palace for what you actually did." → "The lamp is on. Take your time." | "This is Signal. It runs on this laptop. The cable's out." | None — pre-loaded scene. F2 runtime guard verified at boot; chip is reading the audit log. |
| **2** | 10–22 | 240px/s pan to Workshop. Cassady's bench. Three pinned cards, all text legible. | (silence — pacing weapon) | "I want to publish this one." | None — UI state read. |
| **3** | 22–27 | Card 2 selected. `publish this claim` affordance highlights. Click. | (silence — let the click sound) | (no line — let the silence hold) | Backend fires F1 check (no `claim_evidence_link` row → FAIL) and F3 check on card text (genericness-judge, Llama 3.2 3B; banned-vocabulary match on "drove transformation" → T_g 0.71). Both run in <800ms. |
| **4** | 27–43 | Card stays put. Bench lamp dims one notch. Building voice writes 3 lines in `--ember` over 12s. | "This claim has no receipt..." / "...is a sentence anyone can say." / "...this becomes someone else's résumé." | (let the voice finish; no demonstrator line over the building voice — sacrilege) | F1 and F3 verdicts compose into the rejection narration. Building-voice is a deterministic template, not LLM-generated, so the demo cannot fail here. |
| **5** | 43–58 | `RejectionReport` panel slides in. Two rows, monospace. F1 / F3 / verdict / reason. | (panel text is the audible content) | "F1 is the receipt gate. F3 is the genericness gate. Two different judges had to agree this could ship. Neither did." | Panel reads from the `RejectionReport` Priya §5 returns. |
| **6** | 58–75 | Card 3 selected. Click. Card lifts, holds 240ms, slides through doorframe. `--lamp` line draws from card to `migration-rfc-007` icon as it crosses. | "Filed. The claims have receipts. The receipts have rooms." | "That arc you just saw? That's the provenance graph. Every published claim has to be tied — physically — to something in this house." | F1 PASS (link exists). F3 PASS (specific verb, named system, named document, count-noun). Compressor runs but is not gated this turn. F8 PASS trivially (single claim). Publish writes the version. |
| **7** | 75–88 | Vey enters from stage-right, drifts to between card 1 and card 3. `--ember` line draws between them. Vey speaks 28ms typewriter. | "Earlier you said you avoided politics. The RFC has you on it. Which is." | (half-smile) "She's not wrong. The system already knew. It was waiting for me to come back." | F7 contradiction-detector ran *deferred* on prior session's compressor output (per R1's anticipated verdict). Vey's appearance is the **render** of a contradiction the system found *earlier*. Not live — pre-computed. |
| **8** | 88–90 | Hold. Audit chip still `0↑0↓`. Title card. | "Signal. A memory palace for what you actually did." | (no line) | None. |

---

## 4. Demo failure-mode plan — top 3 break scenarios

Each: trigger, detection on stage, **demonstrator's exact words** to pivot. No "graceful recovery" — actual sentences a human can say while the screen is wrong.

### Failure A: F3 fires but the rejection narration is empty / malformed (LLM-generated portion)

**Trigger.** Building voice in beat 4 is a deterministic template per §3 backstage — *but* if a future iteration hooks an LLM into the rejection-reason prose, the model could return empty / garbled text.

**Mitigation.** v0.1 demo uses the deterministic template, not LLM-generated rejection prose. **This is a hard demo-cut precondition.** If anyone proposes hooking the LLM into the rejection narration before launch, the demo cold-open's beat 4 is at risk and this resolution must be revised.

**On-stage pivot if it fails anyway.** The `RejectionReport` panel (beat 5) is independent of the narration and uses raw `F1 / F3` verdicts from the schema — those will render. Demonstrator skips the building voice and goes straight to:

> *"The narration didn't render — that part's a UI polish issue. But here's the actual rejection (gestures to RejectionReport). F1: no receipt. F3: matched the banned-vocabulary list. The publish is refused. That's the gate."*

The **gate still operated**; only the *prose explaining it* failed. The demo survives.

### Failure B: Latency spike — beat 6 publish takes >8s

**Trigger.** Cold cache, KV pressure, or background process competing for CPU. The `publish this claim` click in beat 6 must produce the card-lift animation in <2s for the demo to feel like a system, not a request to a server.

**Detection on stage.** If 3s pass after click with no card movement, the demonstrator pivots before the audience reads it as broken.

**Demonstrator line at t=61s if no animation by t=61s+3s:**

> *"While that's resolving — and it's local, so 'resolving' here means CPU not network — let me tell you what the system is doing right now. It's checking that the claim has a receipt, that the receipt is a real artifact in this house, and that the prose hasn't drifted from the source. That's three checks per publish, on a laptop, with no internet."*

Buys 6–10 seconds of narration. By t=68s the publish either landed or didn't. If it didn't, fall through to Failure C.

### Failure C: Hard failure — model OOM, Ollama unreachable, or animation pipeline frozen

**Trigger.** Worst case: Workshop scene frozen, no animation, no rejection panel. Audience can see the screen is stuck.

**On-stage pivot.** Demonstrator does NOT try to recover. The pivot is **to the audit chip, which is still rendering** because it reads the OS-level packet counter, not the app:

> *"The application's misbehaving — that's a real risk on a laptop with four agents running locally. But notice the bottom-right corner: the network counter is still zero. Whatever broke, it broke without sending anything off this machine. That's not a feature I'm performing — that's a property of how Signal is built. The cable's still out. (lifts cable) Always was."*

Then: *"Let me show you a recorded run of the publish gate I would have just shown you live."* Cut to a 35-second pre-recorded segment of beats 3–7, screen-captured the morning of the demo. Bookmarked, ready to play with one keystroke.

**Pre-condition for demo readiness:** the recorded fallback is rehearsed and one keystroke away. If it isn't, the demo doesn't go live — per Sofia's S4.

---

## 5. What stays invisible (and is fine)

Honest list. Each load-bearing for the architecture, none demoed, **none of which the audience needs to see** to believe Signal is what it claims.

| Thing | Why it's load-bearing | Why it stays invisible | What protects it |
|---|---|---|---|
| **F2 zero-egress invariant** | The privacy claim is the whole §10 PRD posture. | The audit chip + the unplugged cable show it once, at t=8s and t=88s; the *test* itself runs in CI. The audience does not need to see CI run. | The unplugged cable is the strongest visible proof; the chip is the secondary visible proof; the F2 CI test is the mechanical proof. Three layers; only one needs to be visible. |
| **F8 nuance preservation** | One of two publish-gate fitness functions. | Beat 6 publishes a single claim, so F8 is trivially satisfied. F8 only "shows" on multi-claim narratives, which need 5+ minutes of session to accumulate. | F1 + F3 are demoed as the dual gate; the audience generalizes "two judges had to agree" to F8 by analogy. We do not need to demo all four publish-gate dimensions to communicate dual-gate. |
| **F4 compression efficiency** | Soft fitness function; not publish-gate. | Inferable from card 3's specificity vs card 2's slop, but not measured on stage. | Beat 4's "is a sentence anyone can say" *is* the human-legible compression argument. The 1.3× number is for nightly CI, not demo. |
| **F6 RAM ceiling** | Without F6 the system OOMs and there is no product. | "RAM" is a ceiling, not a thing the audience watches. | Pre-warmed models + green-room rehearsal verify it before the demo. |
| **F7 contradiction recall ≥80%** | The *quality* of Vey's contradiction-detection. | Beat 7 shows Vey finding ONE contradiction. Recall is a population statistic; one example is the demo's job. | Pre-seeded session guarantees a true positive; the audience sees one good catch and trusts the rest is calibrated offline. |
| **Multi-agent topology as N≥4 distinct roles** | Driver §1.2; the differentiator. | Audience sees three actors: Cassady's room (resident), the building voice (gate-narrator), Vey (contradiction-detector). They do *not* see Compressor or Genericness-judge as characters — those operate inside the building voice. | The audience does not need to count to four. They need to see "more than one." The demo shows three. |
| **Audit log capturing zero prose** | Privacy posture; verifiable. | The chip is the gesture; the schema is verifiable in code. | We don't open `~/.signal/audit.log` on stage. We say it exists; the unplugged cable is the demo. |
| **The four-room cut + each-NPC-owns-a-probe-class structure** | Vesper §3 / Kenji §1.5 — the topology of probes. | Demo only enters Foyer + Workshop. Library + Glasshouse never appear. | Cold-open establishes the *form* (rooms hold NPCs hold artifacts hold gates); the rest is implied. A 90-second demo cannot tour four rooms without becoming a tour. |

**Rule we held to.** If it cannot be made visible in 90 seconds without lying about it, **don't try.** The unplugged cable is the strongest cable-based privacy proof in the industry; the audit chip is enough; the rest is verified offline. Honesty about what's not on stage is the demo's credibility.

---

## 6. The "holy shit" moment — named, timestamped, self-assessed

### Holy-shit moment

**t=27s–43s.** *The card does not move.* The user clicks publish, and the system **physically refuses to ship the claim** while the building voice — in the room's own language, not a modal, not a toast, not "AI may make mistakes" boilerplate — explains *why* in two distinct sentences corresponding to two distinct fitness functions:

> *"This claim has no receipt."* (F1)
>
> *"And: 'drove transformation' is a sentence anyone can say."* (F3)

### Why this is the moment

1. **It is the only beat where the audience sees the system *do something they have never seen another product do.*** Every chat UI says yes. Every résumé builder says yes. Signal's first audible action in the Workshop is **no, with an architectural reason.** The thing the audience walks away with is "wait, that thing refused to publish — *what*?"

2. **It is invisible-by-design made visible.** The publish gate is the most architecturally-load-bearing component (F1 + F3 = two of the three hard gates) and the hardest to demo. We made it the demo by *staging the rejection*, not the success. A system saying *no* is more legible than a system saying *yes* — because *yes* is what every other product does.

3. **It is unforgeable by a chat wrapper.** A chat UI cannot reproduce this beat without re-architecting itself. There is no prompt-engineering trick that produces a card that won't move because two separate gates rejected it. The architecture is doing the demo.

4. **It is felt-experience-aligned (Dash §4 / project memory standing order #4).** "Generic is a bug." Beat 4 is the exact second the audience watches a bug get refused. The product's standing order shows up on screen as physics.

5. **Publish-gate-as-felt-experience also closes Mara M5** (the panel's "rejection UX is unspecified" nit). The voice samples in beat 4 are the publish-rejection voice samples Dash hadn't written yet. Two birds.

### Self-assessed strength: **8.5 / 10**

**Why not 10:**
- The audience has to *understand* what F1 and F3 are in real time. The `RejectionReport` panel (beat 5) does the explanation, but it's slightly too much text. A first-time viewer who doesn't catch the panel may experience beat 4 as "the AI refused me" rather than "two gates refused for different reasons." Mitigation: demonstrator's beat 5 line ("F1 is the receipt gate. F3 is the genericness gate. Two different judges had to agree.") is the load-bearing sentence of the entire 90 seconds. **If the demonstrator flubs that line, the moment drops to 6.**
- Beat 7 (Vey + contradiction) is also strong (~7) but is the *second* holy-shit moment. Two strong moments in 90 seconds is right; **beat 4 is the one that earns the audience.**

**Why not lower:**
- Compared to candidates considered (Vey-only, the audit chip alone, the provenance line-draw alone) this is the only beat that is *causally* unforgeable. Provenance line-draw can be faked by any product that draws lines. F2 / unplugged-cable is a property, not a moment. Vey's contradiction-surface is great but is dialogue, not a refusal-of-action. The card-doesn't-move is a *physical refusal in a fictional space* — the architecture's most legible self.

### If beat 4 turns out weaker than 8.5 in rehearsal

Backup holy-shit moment: **t=62s–68s** (the provenance line drawing live from card to `migration-rfc-007`). Strength self-assessed 7/10 — pretty, but not unforgeable. Demonstrator slows down at t=63s and lets the line *finish drawing* before speaking. If beats 4 and 6 both rehearse weak, **the demo cold-open is wrong and the cut needs revisiting** (not the script — the cut). See §7.

---

## 7. Cascade flags for synthesis (BP-014) and v0.1 cut

### 7.1 If R1 (signal-r1j) lands verdict B (F5 relaxed to p50≤7s, p99≤15s)

The cold-open's pacing absorbs this **as long as the publish-gate verification is <2s wall-clock** (beat 3→4 transition). F1 + F3 together are bounded by F3's 3B-model judge call (~1.5s + banned-words match ~50ms + provenance schema check <100ms = ~1.7s budget). That's the only F5-sensitive beat.

**Cascade flag:** if F5 relaxes such that **publish-gate verification itself exceeds 3s**, beat 4's "click → narration starts" gap becomes audible and the holy-shit moment loses its punch. The demonstrator's Failure-B pivot covers this, but at strength cost.

**Recommendation to Opus synthesis:** F1 + F3 publish-gate latency must be its own sub-budget, sized ≤2s p95 even if F5 overall is relaxed. This is a demo constraint that becomes a product constraint.

### 7.2 If M3 (signal-b5x) lands decision A or C (Marlow not the opener)

The cold-open's beat 1–2 (Marlow at the door, then pan to Workshop) is **deliberately shallow on Marlow** — he is *seen* but does not interrogate. The demonstrator walks past him into Workshop. This is consistent with M3 verdict A (different opener NPC) or C (no NPC opener) **as long as the Foyer remains a passable threshold scene**.

**Cascade flag — soft:** if M3 verdict B (keep Marlow + add orientation beat), the orientation beat must fit between t=10s (building voice) and t=15s (camera pan). That's 5s. If Dash's orientation beat needs more than 5s, **the demo cold-open's pan to Workshop slips later, and the holy-shit moment lands at t=32s+ instead of t=27s, compressing beats 5–8 dangerously.**

**Recommendation to Dash (M3 owner):** any orientation beat for first-time *session* users must be ≤5s wall-clock to stay compatible with this demo cold-open. If that's not feasible, the demo cold-open needs a different opening NPC choice (Marlow seen but not greeted) and the M3 resolution should call out demo-compatibility explicitly.

### 7.3 If both R1 and M3 close with conflicting requirements

Demo cold-open is the **junior partner** in the cascade. M3's session-opener and R1's latency budget are product-shape decisions; this script bends to them, not the reverse. **But:** if M3's session opener and the demo cold-open diverge to the point that someone watching the demo and someone using the product see *materially different first 90 seconds*, the demo is dishonest and Sofia's S1 blocker is not actually closed. **Hard line:** the demo's first 90 seconds must be *reachable* in the product within first 2 minutes of a session, not staged-only.

### 7.4 If the cold-open as drafted forces re-cutting v0.1

**No re-cut required as drafted.** Every beat uses features in Kenji §1 (1.2 provenance, 1.3 publish gate F1+F8, 1.4 F3 genericness, 1.5 four NPCs / Foyer + Workshop only, 1.6 memory-palace UI, 1.7 audit chip / unplugged cable). Beat 7 (Vey contradiction) uses §1.1 multi-agent topology with Vey as the visible probe.

**Single soft ask of v0.1 scope:** beat 4's `RejectionReport` panel needs Dash to write **publish-rejection voice samples** (Mara M5 nit). Three lines, ~15 words each. That's a copy task, not a feature. Adding to BP-019 product-bead spawn list as a copy item, not a scope change.

---

## 8. ADR-class statement (one sentence)

**Signal's v0.1 demo cold-open is built around the publish-gate refusal at t=27s–43s because the system saying *no* — with two architecturally-distinct reasons, in the room's own voice, on a card that physically does not move — is the only 16-second window where Signal's invisible-by-design differentiators become a thing a stranger can point at and remember.**

---

## 9. Done-when checklist (per bead spec)

- [x] 60–90 second demo cold-open, pasteable narration (§1) — replaces Sofia's panel-rejected attempt
- [x] Designated visible moments per minute for each load-bearing differentiator (§2)
- [x] Beat-by-beat storyboard, 8 beats over 90s (§3)
- [x] Demo failure-mode plan, top 3 break scenarios (§4)
- [x] What stays invisible — honest list (§5)
- [x] Holy-shit moment named, timestamped, self-assessed (§6)
- [x] Cascade flags for R1, M3, v0.1 cut (§7)
- [x] ADR-class statement (§8)
