---
name: Kenji — PM Brief (MVP cut, defer/kill, success-metric mapping)
bead: BP-012 (signal-trq)
date: 2026-05-09
deadline: 2026-06-06 (4 weeks)
---

## Executive summary

Signal v0.1 ships a **single-user, local-only memory palace with four NPCs across four rooms**, one heavy interrogator model (Qwen 14B q4) plus the supporting role pool, and a publish path that mechanically refuses any claim without an evidence link or a preserved load-bearing token (F1 + F8). Three of Dash's seven rooms (Bridge, Switchyard, Boiler Room) are deferred — they have no resident NPC and add map surface without adding probe types. The 8 GB tier is killed: Devon's matrix shows it forces single-LLM mode, which violates spine §1.2 and ships the slop F3 exists to refuse. We bet the product on the *interrogation topology and the provenance graph*, not on world surface area, art, or session-spanning continuity. If the topology produces "feels more accurate" narratives in three out-of-team user sessions before launch, we ship; if it doesn't, no amount of additional rooms saves it.

---

## 1. MVP cut (v0.1 walking skeleton)

Each item earns shelf space by moving a PRD §9 metric. If it doesn't, it's not here.

**1.1 Multi-agent topology — 5 roles (Suki §1).** Interrogator + contradiction-detector + evidence-linker + compressor + genericness-judge. *Justification:* this IS the differentiator (PRD §3, §4.2). Without it Signal is a chat wrapper. Drives §9 "accurate," "specific," "defensible." Anti-collapse audit (Suki §2) ships as CI gate so we know the topology isn't decorative.

**1.2 Provenance graph — full C2 schema (Priya §1–§2).** `source` → `evidence_artifact` → `claim` ↔ `claim_evidence_link` + `witness`. *Justification:* PRD §4.1 + §9 "defensible under scrutiny" is mechanically impossible without this. Schema-level CHECK + publish-gate function (defense in depth, Priya §5). Cuts the "evidence traceability" success metric (25% of weight) from felt-quality to mechanical guarantee.

**1.3 Publish gate enforcing F1 + F8 (Priya §5).** Hard-fail any narrative_version whose claims are missing `supports` links OR whose compression dropped >10% of load-bearing tokens. *Justification:* one of two places the architecture refuses to ship slop. F1 is 100% (binary) and F8 is 90% (graded) — both block publish. Every PRD §9 success bullet routes through this gate.

**1.4 Genericness-judge gate enforcing F3 (Suki §3).** Llama 3.2 3B judge runs on every compressor output before it reaches the user. Hard-reject above T_g=0.35; recompose with banned list expanded. *Justification:* "generic is a bug" (project memory standing order). Cuts the "compression quality" metric (20%) from prose-discipline aspiration to runtime gate.

**1.5 Four rooms, four NPCs (Dash §2–§3, Vesper §2).** Foyer (Marlow / outsider compression test), Workshop (Cassady / operational specificity), Library (Lenore / evidence retrieval), plus the **Glasshouse** as the empty-room default Vey drifts into. *Justification:* each NPC owns *one probe class* (Vesper §3), each probe class moves a different §9 metric. Four is the minimum where the topology is non-trivial and Vey's contradiction-surfacing (PRD §7.6) has somewhere to land.

**1.6 Memory-palace as primary UI (Marcus §1–§2, Dash §1).** Phaser canvas + React overlay + Zustand bridge + SSE token stream. *Justification:* spine §4 marks this Hard-reversibility (ADR-002). The metaphor is what makes Socratic friction *valued not avoided* (§9 "felt experience," 15%). Reverting to "list of probes" is a different product.

**1.7 Local-only by construction (Devon §1, §3, §6).** Native install primary, 16 GB floor, F2 zero-egress CI test + `pf`/`nftables` runtime guard. *Justification:* PRD's implicit NDA on career corpus + §9 privacy bullet (10%). Spine §1.4 marks this Hard-reversibility (ADR-004). No remote fallback — local fails visibly.

**1.8 Single-session conversation (no cross-session contradiction detection).** Within-session contradiction detection only (Suki §1; defer Vesper §7's cross-session ask). *Justification:* keeps F6 RAM ceiling reachable, and within-session is sufficient to demonstrate Vey's mechanic on the metric that matters ("felt more accurate"). Cross-session is a v0.2 RAM-budget conversation.

**1.9 Free-text-only evidence ingestion (Vesper §6 cut, spine §8.3).** No résumé paste, no GitHub link, no document upload in v0.1. *Justification:* the user *saying it themselves* IS the mechanism — paste removes the Socratic step. Saves parsing/provenance complexity.

**1.10 Audit log + privacy verification (Devon §3–§4).** SQLite + JSONL mirror, no prose captured, F2 CI test on every PR. *Justification:* the privacy claim is *verifiable* not just asserted. §9 privacy metric is binary — either the test passes or it doesn't.

---

## 2. Defer list (v0.2+)

Valuable, but not load-bearing for the v0.1 thesis. Each gets one rationale.

- **Bridge, Switchyard, Boiler Room (Dash §2; Vesper §6 already cuts Boiler).** No resident NPC, no probe type Cassady/Lenore can't cover from their resident rooms. Spine asks ≥6 rooms; we ship 4 and promise the rest. Cost of skipping: addressable user-type breadth (TPL, transformation lead) underserved by *spatial theme* — but their *probe needs* are still met by the four NPCs.
- **Cross-session contradiction detection (Vesper §7).** Better mechanic, costs ~3 GB additional KV cache, breaches F6 on M3 24GB. Defer until 32GB tier is the reference target or until summary+RAG persistence (spine §8.1) lands.
- **Bespoke NPC art and pixel-art animation polish (Marcus §3).** v0.1 ships Kenney/Mana Seed CC0 recolored to BP-010 palette + silhouette NPCs. Vesper signs off on legibility. Bespoke art does not move §9 — felt experience comes from *pacing and silence* (Dash §4), not sprite fidelity.
- **Résumé/GitHub/document ingestion (spine §8.3, Vesper §6 cut).** Material v0.2 feature once core loop validated; until then it competes with the *mechanism*.
- **Trained genericness classifier (Suki §7 sacrificial).** Banned-words + LLM-judge holds T_g for v0.1; trained classifier replaces it when adversarial paraphrase escapes the list. This is the biggest known throwaway and we should not amortize it before validating the loop.
- **Hybrid retrieval (BM25 + reranker; spine §5, Priya §8).** Top-K cosine on `artifact_vec` is fine for the v0.1 corpus size (~hundreds of artifacts/user). Ship when narrative-quality regression appears.
- **Phaser typewriter token-by-token streaming (Vesper §7, Marcus §7).** v0.1 may fall back to whole-line reveal under reduced-motion or Phaser/Zustand back-pressure. Token-stream is nicer; line-reveal still satisfies F5.
- **High-contrast theme + dyslexia font + i18n (design-system §5).** v0.1 named throwaway. The palette is load-bearing on §9 "felt experience" — splitting it before it's proven is premature.
- **Versioning granularity (spine §8.4).** v0.1 stores narrative_version as full snapshot per Priya §2. Fine-grained diffs are a v0.2 storage-cost optimization.
- **8 GB tier "lite mode" (Devon §6).** Not deferred — see kill list. Documented here because users *will* ask.
- **Multi-user, auth, cloud sync (Priya §8 sacrificial).** The single-user, no-auth, file-perms posture is correct for v0.1 — multi-user is a privacy-posture re-negotiation (spine §1.4 reversal), not a config toggle.

---

## 3. Kill list (do not ship, ever or only as throwaway)

- **Single-LLM "lite mode" for 8 GB hardware (Devon §6 — confirmed kill).** Violates spine §1.2 and ships the product F3 exists to refuse. The user blames Signal for being a bad chat product. Refusing-to-launch is a better failure mode than degrading-into-slop. Hard floor 16 GB, installer-enforced.
- **Cross-visit memory for Marlow (Vesper §6).** Marlow forgetting you is *the mechanic* — the outsider compression test only works if the outsider is a stranger. Implementing memory here doesn't extend the system, it breaks the metaphor.
- **Visible progress signals — XP, streaks, "3 of 4 NPCs talked to" (Vesper §6, Dash §6).** Coaching/gamification tone is exactly what PRD §4.4 and §8 say we are not. Banned at the design level, not the visual level.
- **Generic résumé export path with the same prose treatment as the narrative (Vesper §5 failure-mode 6).** Raw claims may export as JSON; the *narrative* publish path is gated by F1/F3/F8. We do not ship a "click here for a generic résumé" affordance — it would invalidate the whole topology.
- **Remote LLM fallback when Ollama is unreachable (Suki §4).** Local fails visibly; no path silently uses a cloud model. F2 invariant. This is the single most important kill: every "but what if the local model fails" suggestion in v0.2+ planning routes through *this* line.
- **WebSocket transport (Marcus §4).** Adds framing + reconnect + a second mental model. Kill in favor of SSE — even if streaming gets fancier in v0.2.
- **AI-design tells: gradient buttons, orb avatars, "send" airplane glyph, "AI may make mistakes" boilerplate, dark-mode-neon toggle (design-system §6).** Each one separately would re-classify Signal as "an AI app" instead of a memory palace. Killed at the visual-system level, not negotiable per-component.
- **Markdown bullets / emoji in NPC dialogue or system messages (design-system §6, Dash §6).** NPCs are people, not slack-bots. Banned in copy.
- **"Journey," "leverages," "robust," "rockstar," "best-in-class" and the rest of the banned-vocabulary list (Dash §6).** F3 enforces this. Kenji enforces it again at copy review. If a line could appear on LinkedIn unchanged, it does not ship.

---

## 4. Scorecard application

Project-memory rubric applied to the v0.1 cut. Differentiator weight is heaviest.

| Dimension | Weight | Score (0-10) | Reasoning |
|---|---|---|---|
| **Differentiator signal** — Socratic interrogation that surfaces contradictions and links claims to evidence | 30% | **9** | Multi-agent topology, anti-collapse CI audit, Vey's contradiction-surfacing mechanic, F7 recall ≥80%. Risk: T_g calibration (Suki §6 open question) — until BP-005c lands, the genericness threshold is empirical guesswork. |
| **Evidence traceability** — 100% of published claims linked to in-world artifacts | 25% | **10** | F1 enforced in two places (CHECK constraint + gate function, Priya §5). Mechanical, not stylistic. The schema makes the failure-mode unrepresentable. |
| **Compression quality** — specificity-per-token improves vs single-shot baseline | 20% | **7** | F4 ≥1.3× soft target. Ship-blocker risk: until the gold corpus is built (Suki §6), F4 is a nightly metric not a publish-gate, so a regression could land in a release. Mitigated by F3 publish-gate which catches the worst slop. |
| **Felt experience** — Socratic friction valued, not avoided | 15% | **7** | Dash + Vesper deliver the metaphor; design-system §4 motion principles support it. Risk: third-return / tenth-visit pacing (Vesper §4) untested in v0.1; if probe rotation is too narrow the visit collapses into a list. |
| **Privacy** — data never leaves machine, verifiable | 10% | **10** | F2 CI test + `pf`/`nftables` runtime guard + no-remote-fallback policy + audit-log captures no prose. Defense in depth. Devon §3. |
| **Total weighted** | | **8.5 / 10** | Above the 7.0 ship threshold. Two notable risks: T_g calibration (Suki §6) and pacing on return visits (Vesper §4). Both are *measurable*, not subjective. |

**Decision:** ship the cut. Both risks are gated on artifacts (BP-005c gold corpus, pre-launch user sessions on returns 3+) that are budget-affordable inside the four-week window.

---

## 5. Success-metrics mapping (PRD §9 → v0.1 features → fitness functions → measurement)

| PRD §9 metric | v0.1 features that move it | Fitness functions that gate it | Pre-launch measurement |
|---|---|---|---|
| "Narrative feels more accurate" | 1.1 multi-agent topology, 1.5 four NPCs (each owns one probe class), 1.4 F3 genericness gate | F3 (hard, publish-gate), F4 (soft, nightly), F7 (soft, weekly) | Three out-of-team users run a 90-min session each; structured post-interview ("does this feel like you?"). N=3 not because that's enough, but because that's affordable in 4 weeks. |
| "Descriptions more concise and specific" | 1.4 F3 genericness gate, 1.3 F8 nuance preservation, 1.5 Marlow's compression test | F3 (hard), F4 (soft, ≥1.3× single-shot baseline), F8 (hard, ≥90% load-bearing tokens kept) | Specificity-per-100-tokens on the same user's narrative vs single-shot Qwen 14B baseline (Suki's nightly job). Target ≥1.3×. |
| "Leadership identity becomes clearer" | 1.5 four NPCs (probe diversity), 1.6 memory-palace UI (room-to-theme binding) | F3 (rejects generic), F7 (Vey surfaces contradictions ≥80% recall) | User self-rating on "I can describe what I do in one sentence I'd defend" pre-session vs post-session, on a 1-7 anchor scale. |
| "Intellectual and operational strengths legible" | 1.2 provenance graph, 1.3 publish gate, 1.5 Cassady's operational-specificity probe | F1 (hard, 100%), F8 (hard, ≥90%) | External reader (one engineering hiring manager, one principal engineer) reads narrative + clicks through to evidence; reports back on "do you understand what this person does?" |
| "Claims feel defensible under scrutiny" | 1.2 provenance graph (witness + evidence_link), 1.3 F1 publish gate | F1 (hard, blocking), F7 (catches the contradictions before publish) | User-led mock interview: external interviewer challenges three published claims; user successfully cites the in-world artifact for each. Pass = 3/3. |
| "Data never leaves machine, verifiable" | 1.7 local-only, 1.10 F2 CI test + runtime guard | F2 (hard, CI gate, runtime drop) | F2 CI test runs on every PR; user runs `signal privacy audit` and sees zero outbound bytes since boot. Both are mechanical, not narrative. |

**F5 (latency) and F6 (memory)** don't map to a §9 metric directly but gate the others — if F5 misses p99 ≤12s the felt experience collapses; if F6 breaches 18 GB on M3 24GB the system OOMs and there is no product. Both are hard CI gates.

---

## 6. Open questions for Opus synthesis (BP-014)

Decisions I cannot make alone — each requires cross-role tradeoff Opus is positioned to settle.

1. **Conversation persistence: full re-hydration vs summary+RAG (spine §8.1).** Locks Suki's 8k-context fallback (Suki §6 Q1), changes Devon's 32 GB tier value (Devon §9), affects Priya's `state_blob` schema (Priya §4). Three roles want it decided before they freeze contracts. **My PM lean:** summary+RAG, because re-hydration breaks F6 on the third return visit and the cost (occasional summary artifacts) is tolerable.
2. **Contradiction surfacing UX (spine §8.2).** Vey-drifts-in (C4-native, Vesper §7) vs popup vs margin annotation. Affects Marcus's event protocol (`contradiction.surfaced`), Vesper's mechanic spec, Dash's tone constraints. **My PM lean:** Vey-drifts-in for the visible canvas, margin-annotation in React for the narrative editor — both, not one. Two surfaces because contradictions live in two contexts.
3. **T_g calibration corpus and timeline (Suki §6).** Until BP-005c gold corpus exists, F3 threshold is a guess. If we ship before T_g is calibrated, the genericness judge is performance theater. **PM ask of Opus:** should we delay v0.1 launch until BP-005c lands, or ship with T_g=0.35 as documented placeholder and a v0.1.1 hot-patch path? Recommendation: ship with placeholder + visible "calibration in progress" banner in audit log; the *worse* failure mode is delaying past the four-week window.
4. **Probe rotation budget for tenth-visit interest (Vesper §7 Q3).** If Cassady/Lenore can't seed-vary across visits, the late-visit experience collapses. Affects Suki's prompt registry size, Marcus's session-state. **PM ask of Opus:** is per-NPC prompt registry a v0.1 feature or a v0.2 throwaway-replacement? Recommendation: ship 5 prompt seeds per NPC for v0.1; per-user prompt-registry is v0.2.
5. **Out-of-team user-test logistics inside the four-week window.** Need three users, 90 min each, with consent for narrative review. Not a tech question — a calendar question. **PM ask of Opus:** ratify that I can spend the last week of the four on user-tests, even if that means f4/f7 nightly thresholds aren't fully validated until v0.1.1.
6. **What if all five hard fitness functions pass but the felt-experience metric is "no" from all three users?** This is the unfalsifiable-failure scenario. Need agreed escalation path before launch — not after. My instinct: we delay, we don't ship a product the users say doesn't feel accurate even if all the gates pass. The whole point of the architecture is to *enforce* the felt experience, not to validate against gates that turn out not to predict it.

---

## 7. Sacrificial choices (v0.1 throwaways I'm endorsing)

Adding to spine §5:

| Choice | Throwaway trigger | Replacement direction |
|---|---|---|
| 4 rooms instead of 6–7 | User-type addressable-base feedback shows TPL/transformation-lead under-served | Add Bridge + Switchyard + Glasshouse-as-distinct-room in v0.2 |
| In-session contradiction only | F7 recall plateau or "I forgot what I said last time" complaint cluster | Cross-session detection backed by summary+RAG persistence |
| Five fixed NPCs | User wants their own interlocutor (manager, mentor, peer reviewer) | NPC marketplace per spine §5 sacrificial |
| T_g placeholder = 0.35 | Calibration corpus drifts as banned-vocabulary evolves | Trained classifier (Suki §7) |
| Three-user pre-launch validation | We claim "feels more accurate" without N to back it | Cohort study at v0.2 with 15+ users |

Named so we don't mistake them for technical debt. They are intentional, budgeted, and timed.

---

## 8. Sign-off posture

I sign off on the cut above conditional on:

- BP-013 (Judge Panel adversarial review) flags no kill-list violations in any role's brief.
- Opus's BP-014 synthesis closes the six open questions in §6 with documented decisions, not punts.
- The first integration test that exercises 1.1 + 1.2 + 1.3 + 1.4 end-to-end (a single user prompt → claim → link → publish-or-reject) lands by week 2 of the build window, not week 3. If it slips, we cut a feature from §1, not extend the deadline.

If the topology+graph thesis is wrong, four extra rooms won't save it. If the topology+graph thesis is right, four rooms is enough to prove it.
