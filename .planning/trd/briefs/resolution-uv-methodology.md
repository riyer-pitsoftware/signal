---
name: Resolution — User-Validation Methodology (Pre-Registered)
bead: BP-013.10 (signal-sd9)
date: 2026-05-10
owner: Kenji (PM, primary) · Vesper (failure-mode discipline, collaborator)
resolves: Mara M4 (serious → load-bearing) + cohort-sizing gap (kenji.md §5, §6 Q5/Q6) + test-corpus/SPEC.md §"What this corpus is not"
status: pre-registered, lock before sessions
---

## Purpose of this document

Pre-register Signal's external user-validation methodology *before* sessions run. Once sessions begin, this document is read-only. Six months from now, when results land, the only operation permitted on this file is to compare results against criteria — not to revise the criteria.

**The criteria below are designed to be uninterpretable post-hoc.** Where a criterion permits two readings, the reading that yields a "no" wins. This is the asymmetry that makes pre-registration load-bearing: ambiguity defaults to falsification, not to ship.

If anyone — including me — proposes a criterion adjustment after the first session has run, the response is: *no.* The window to revise this document closed when the first user pressed Enter on Marlow's first prompt.

---

## 1. Cohort sizing — N=5, with budget tradeoff named

### Decision: N=5. Revised up from N=3.

I am revising my own brief (kenji.md:93). N=3 was window-driven, not methodology-driven, and Mara M4 is correct that "feels accurate" without statistical-or-pre-registered footing decays under deadline pressure. Three users cannot survive the failure-mode arithmetic below — see §3.

### Why 5 (not 3, not 8)

- **Floor at 5 because the pre-registered failure rule needs three independent dissenters to fire reliably.** With N=3 and threshold "2/3 no delays" (Mara M4), one user's mood, one botched session, or one screening miss flips the outcome. With N=5 and threshold "≥3/5 no delays," the falsification rule survives one bad session and one ambiguous session simultaneously.
- **Ceiling at 5 (not 6–8) because the four-week window is hard.** The deadline is 2026-06-06. Sessions are 90 minutes plus ~3 hours of post-session analysis per user (transcription audit, rubric scoring, double-rater agreement). 5 users × ~5 hours total = ~25 hours of synthesis-window work, plus recruitment + screening overhead estimated at ~8 hours. This fits the last 10 calendar days; 8 users does not without displacing F4/F7 nightly threshold validation that BP-005c is still racing.
- **Test-corpus SPEC says 5–8.** I am taking the floor of that range, not the midpoint, and naming the reason: budget, not methodology. If results are unclear (§3 ambiguity zone) we extend per the pre-registered extension rule, not per vibes.

### What N=5 does NOT validate (named explicitly so we don't claim it does)

- **Statistical significance.** N=5 is below any reasonable power threshold for a between-groups comparison. We will not produce p-values. We will not claim "users prefer Signal over [X]." Validation is *did this product clear pre-registered thresholds with this cohort*, not *will this product clear those thresholds with the population of all technical leaders*.
- **Distribution coverage across PRD §5 user types.** Seven user types listed (TPL, EM, architect, technical program leader, transformation leader, staff/principal, data/platform leader, cross-functional systems thinker). We sample 5. Recruitment §2 below specifies *which* user types we cover; we do not get to claim coverage of the others.
- **Subgroup effects.** "Does Signal work better for staff engineers than for transformation leaders?" — unanswerable at N=5. Refused.
- **Long-horizon usage.** Each user does one session. Vesper §4's third-return and tenth-visit pacing are *not* validated by this cohort. Single-session is the validation scope; return-visit pacing is a v0.2 follow-on cohort.

### Budget impact (named, not absorbed)

- **Calendar:** sessions occupy days 22–28 of the 28-day window; analysis day 29; pre-launch decision day 30 (the 2026-06-06 deadline morning).
- **Trades:** F4 (compression-quality) nightly threshold and F7 (contradiction-recall) weekly threshold continue running through user sessions but are *not* re-tightened during week 4. If their nightly numbers drift during user-session week, we ship at the week-3 thresholds and note the freeze in launch ADR.
- **No external funding required.** No timeline extension granted by going from 3 to 5; we paid for it inside the existing window by freezing fitness-function tightening one week early.
- **Cascade flag:** if §6 stop-rule triggers an extension to N=7, that *does* push launch by ~3 calendar days (recruitment + sessions). Recorded as a known cascade. BP-014 synthesis must record this as a documented risk; BP-015 TRD must include the extension path.

---

## 2. Recruitment and screening

### 2.1 Who counts as a "real" user

A real user is a technical leader who:

1. **Has ≥7 years post-IC technical career** (operates across systems/strategy/architecture/product/operations/org change per PRD §1).
2. **Self-reports the representation gap** — has, in the last 12 months, attempted to write a résumé/LinkedIn-About/intro-email/consulting-pitch and felt it flatten or generic them. (Asked verbatim during screening — see §2.4.)
3. **Maps to one of PRD §5 user types** — TPL, EM, architect, technical program leader, transformation leader, staff/principal, data/platform leader, cross-functional systems thinker.
4. **Is not a friend, former colleague within 3 years, family member, or current professional collaborator of the founding team.** Operationalized below.

### 2.2 Anti-friends-of-team operationalization

Recruitment channels — *only these, ranked*:

1. **Cold outreach via professional communities** (Rands Leadership Slack, staff-eng newsletters, technical-leadership Discord servers). Recruiters post a screening interest form; we contact responders.
2. **Second-degree professional referral with a stranger floor**: a contact may *introduce* a candidate but the candidate must not have met any founding team member before the introduction email. Recorded in screening log.
3. **Targeted LinkedIn outreach to public technical-leadership writers** (people who have published on staff-eng.com, leaddev.com, or similar) whose work shows the representation-gap problem in their own writing.

Banned recruitment channels:
- Personal friend network. Including "friends-of-friends" if the friend is in the social graph.
- Former colleagues within 3 years.
- Anyone who has read this PRD or any Signal planning document.
- Anyone who has had a >5-minute conversation with the founding team in the last 12 months on any topic.

### 2.3 Cohort composition target (committed, not aspirational)

5 users with the following distribution. If we cannot fill, we say so and ship with the gap named — we do *not* fill the slot with a friend-of-team to hit the number.

- 2 × engineering manager / technical program leader (the cut-room user types per Mara M1 — they need representation here precisely because the spatial UI doesn't give them their own room).
- 1 × staff/principal IC architect.
- 1 × transformation leader / cross-functional systems thinker.
- 1 × data or platform leader.

### 2.4 Screening interview (15-minute call, scripted)

Screener: Kenji. Recorded with consent for screening-rejection-rationale audit only; deleted post-cohort.

**Script (verbatim, asked in order):**

1. "In your own words, what kind of work do you do?" *(2 min — listening for technical-leadership texture, not coaching them.)*
2. "When was the last time you tried to write something about yourself professionally — résumé, LinkedIn, an intro email — and felt it didn't capture what you do? What happened?" *(3 min — listening for the representation gap as PRD §1 names it. If the answer is "I just hire someone to write it" or "I'm fine with my LinkedIn," reject.)*
3. "How do you feel about being interrogated about your career by an AI system that will push back when your descriptions are vague?" *(2 min — listening for tolerance of friction. If "I want it to write the thing for me," reject — they're not the user, they're the user we are explicitly not building for per PRD §8.)*
4. "Have we — Kenji, or anyone you know we work with — interacted with you in any professional or social context in the last 12 months?" *(1 min — disclosure check.)*
5. "Are you willing to give 90 minutes to a recorded session, with audio + screen capture stored locally on a single laptop, never uploaded, deleted on request?" *(1 min — consent check.)*
6. "Do you have any reason to want this product to succeed beyond your own session experience?" *(1 min — investor / advisor / equity-stakeholder disclosure. Auto-reject on yes.)*
7. Reverse questions from candidate. *(5 min.)*

### 2.5 Accept/reject decision

Decided by Kenji **alone**, written rationale per candidate. Single-rater on accept/reject is acceptable here because the screening criteria are mechanical (Q1 texture, Q2 named gap, Q4/Q6 disclosures); subjectivity is in Q3 friction tolerance, where the bar is low (any non-rejection answer passes).

Vesper double-checks rejections to catch "rejected because they made me uncomfortable for valid reasons" — i.e., catches Kenji rejecting candidates who would falsify the product. Disagreement on rejection escalates to user signoff.

---

## 3. Pre-registered success/failure criteria — THE LOAD-BEARING SECTION

This is the section that, six months from now, determines whether Signal's narrative-extraction claim is true.

### 3.1 Per-PRD §9 metric pre-registration

Each PRD §9 success bullet gets: a measurement instrument, a per-user pass threshold, and a cohort-aggregate pass threshold. **Per-user "pass" requires meeting *all three* of: instrument-1, instrument-2, behavioral-anchor (where applicable).** This is the and-gate that prevents post-hoc cherry-picking.

#### M1: "Their professional narrative feels more accurate"

| Component | Specification |
|---|---|
| **User-side instrument 1** | Forced-choice item, post-session: *"Compare the Signal-extracted narrative to the pre-session draft you wrote. Which is closer to how you actually operate?"* Choices: (a) Signal closer, (b) draft closer, (c) tied, (d) both equally inaccurate. **Per-user pass:** answer is (a). Tied = no. Both inaccurate = no. |
| **User-side instrument 2** | 1–7 anchored scale: *"This narrative feels accurate to me."* with verbal anchors at 1 ("not me at all"), 4 ("partly me"), 7 ("yes, this is me"). **Per-user pass:** ≥6. |
| **Behavioral anchor** | Post-session, user is asked: *"Show me one sentence in this narrative you would send to a hiring manager tomorrow without editing."* **Per-user pass:** they identify a sentence within 60 seconds without re-reading the whole narrative. (Catches the "I rated it 6 to be polite" failure mode.) |
| **What counts as a NO** | Any of: forced-choice ≠ (a); scale <6; cannot identify a send-as-is sentence in 60s. **Any one fails the metric for that user.** |
| **What counts as a YES** | All three pass. Explicit-only — no inference from "the user seemed to enjoy the session." |
| **Cohort threshold** | ≥3/5 users pass = metric passes. ≤2/5 = metric fails. Exactly 3/5 with one fail being "no send-as-is sentence" only = metric passes-with-asterisk and triggers postmortem. |

#### M2: "Their descriptions are more concise and specific"

| Component | Specification |
|---|---|
| **User-side instrument 1** | 1–7 scale: *"This narrative is more specific than what I would have written myself."* **Per-user pass:** ≥5. |
| **Mechanical instrument** | F4 specificity-per-100-tokens: Signal-output vs user's pre-session draft, both scored by Suki's nightly F4 metric (single-shot Qwen 14B baseline = 1.0). **Per-user pass:** Signal ≥1.3× draft. |
| **Behavioral anchor** | Word count: Signal narrative ≤ user's pre-session draft word count (compression must actually compress, not just sound specific in a longer document). **Per-user pass:** Signal word count ≤ draft word count. |
| **What counts as a NO** | Scale <5 OR F4 ratio <1.3× OR Signal narrative ≥ draft word count. |
| **YES** | All three pass. |
| **Cohort threshold** | ≥3/5 pass. |

#### M3: "Their leadership identity becomes clearer"

| Component | Specification |
|---|---|
| **User-side instrument 1** | 1–7 scale, asked twice (T0 = pre-session, T1 = post-session): *"I can describe what I do in one sentence I'd defend."* **Per-user pass:** T1 − T0 ≥ +2 (delta, not absolute). |
| **User-side instrument 2** | At T0 user writes their one-sentence defended description on paper. At T1 user writes it again without seeing the T0 version. **Per-user pass:** T1 sentence is judged "more specific" than T0 by two blind raters (see §5). Inter-rater disagreement = the case is treated as a NO. |
| **What counts as a NO** | Delta <+2 OR raters disagree OR raters agree T1 is not more specific. |
| **YES** | Both pass. |
| **Cohort threshold** | ≥3/5 pass. |

#### M4: "Their intellectual and operational strengths become legible" (to externals)

| Component | Specification |
|---|---|
| **External-reader instrument** | Two external readers — one engineering hiring manager, one principal engineer — read each user's published Signal narrative *with no other context*. They independently answer: *"In one sentence, what does this person do?"* Then rate 1–7: *"I understand this person's work."* **Per-user pass:** both readers' one-sentence answers agree on the user's primary work in the user's own judgment (user is shown both reader-sentences after their session and asked: *"Did either of these match what you actually do?"*) AND both readers rated ≥5. |
| **What counts as a NO** | User judges neither reader-sentence accurate OR either reader rated <5. |
| **YES** | User judges ≥1 reader accurate AND both readers ≥5. |
| **Cohort threshold** | ≥3/5 pass. |
| **External readers** | Pre-recruited from the same pool as the user cohort, screened to the same anti-friends-of-team rule. Paid honorarium. Do not see other readers' answers until both submitted. |

#### M5: "Their claims feel defensible under scrutiny"

| Component | Specification |
|---|---|
| **Mock-interview instrument** | A mock-interviewer (separately recruited, with technical-leadership interviewing experience, not on the founding team) challenges *three claims* from the user's published narrative — interviewer picks the three claims they find most ambiguous. User has 90 seconds per claim to cite the in-world evidence artifact (the witness/document/decision Signal linked). **Per-user pass:** 3/3 claims successfully cited. |
| **What counts as a NO** | <3/3 cited within time. (No partial credit. The whole point of F1 + provenance graph is *every* claim is defensible, not 2 of 3.) |
| **YES** | 3/3 cited. |
| **Cohort threshold** | ≥4/5 pass. (Note: tighter than other metrics. Provenance is a mechanical guarantee, not a felt-quality metric — the threshold should be high. If users can't defend their claims, the F1 publish gate is theater.) |

#### M6: "Data never leaves machine, verifiable"

| Component | Specification |
|---|---|
| **Mechanical instrument 1** | F2 CI test passes on the build the user runs. Pre-condition; if it fails, session does not happen. |
| **Mechanical instrument 2** | User runs `signal privacy audit` at session end, observes zero outbound bytes since boot. Logged. |
| **User-side instrument** | 1–7 scale: *"I trust this product not to leak my data."* **Per-user pass:** ≥6. (Privacy is mechanical *and* felt — both must pass. Mechanical without felt means we did not communicate the guarantee adequately.) |
| **NO** | Any of the three fails. |
| **YES** | All three pass. |
| **Cohort threshold** | 5/5 pass. (Privacy is binary at the product level. Any single-user failure is a failure of the product claim.) |

### 3.2 Aggregate decision rule

| Outcome on the six metrics | Action |
|---|---|
| All 6 pass cohort thresholds | **Ship.** Launch on 2026-06-06 with no caveat in marketing copy. |
| 5 pass, 1 fails (any single metric) | **Ship with written postmortem** *only if* the failed metric is M1, M2, M3, or M4. Postmortem published in repo as ADR. **Do not ship** if the failed metric is M5 (defensibility) or M6 (privacy) — those are mechanical guarantees, single-failure = product-claim broken. |
| 4 pass, 2 fail | **Do not ship.** Delay. Per Mara M4: 2/N "no" delays launch. We are explicit: 2/6 metric-fails = delay regardless of which two. |
| 3 or fewer pass | **The architecture is wrong, not the implementation.** Do not iterate. Re-open BP-004 architectural spine. |
| Privacy (M6) fails for any user | **Stop the cohort immediately.** This is a recall-class issue. Decision-maker: Devon + Kenji + user joint signoff to resume after fix. |

---

## 4. Session protocol

### 4.1 Pre-session (1 day before)

- User receives a **single-page pre-brief** describing: what Signal is, what will happen in the session, what data is captured (audio, screen, telemetry), where it's stored (single laptop, never uploaded), how to request deletion. **No description of the success metrics, the topology, or the falsification rule.** They go in cold on what counts as success.
- User writes their **pre-session narrative** in a Google Doc (or any tool of their choice): one paragraph (≤200 words) describing what they do professionally, *as if writing a LinkedIn-About*. Submitted before session start. This is the T0 baseline for M1 and M2.
- User writes their **T0 one-sentence-defended description** on paper or text file, sealed/saved unread until T1.
- Consent form signed: audio recording (locally, deleted on request), screen capture (locally, deleted on request), narrative kept for analysis (deletable on request, anonymized in any external citation).

### 4.2 Session structure (90 minutes total, fixed)

| Phase | Time | What happens |
|---|---|---|
| **Greeting** | 0–5 min | Building voice intro, Foyer first frame loaded, user familiarizes with control scheme. *No interrogator-firing. No F3 rejection.* (Per BP-013.7 / signal-b5x — Mara M3 first-90-seconds resolution. Cross-reference: when that bead closes, this section's text aligns with whatever orientation pattern Dash specifies.) |
| **Marlow turn 1** | 5–10 min | Compression test; pinned to coat rack. F3 disabled on turn 1 per separate resolution. |
| **Free exploration** | 10–70 min | User moves between rooms. Workshop (Cassady), Library (Lenore) fire on entry. Vey drifts in on real contradictions. **Interviewer is silent.** No prompts, no nudges. The session is the system, not the interviewer. |
| **Publish attempt** | 70–80 min | User attempts to publish their narrative. F1 + F8 gate fires. If rejected, user iterates or accepts the rejection. If published, narrative is captured for §5 analysis. |
| **Post-session interview** | 80–90 min | Scripted, see §4.4. |

User may end early; sessions <60 minutes flag for review (did the system fail? did the user disengage?). Flagged sessions still count for analysis — they are evidence, not voids.

### 4.3 What's recorded

- **Audio** (microphone, 16kHz mono, local file, encrypted at rest).
- **Screen capture** (local file, encrypted at rest).
- **System telemetry**: every NPC turn, every probe fired, every F3/F1/F8 decision, every Vey contradiction-surface event, latency per turn (F5 instrumentation), KV-cache size at session minutes 5/30/60/90 (F6 instrumentation, per Ravi R2). Stored in session-scoped SQLite + JSONL mirror per Devon §3.
- **Pre-session draft** (user's T0 narrative).
- **Published narrative** (Signal output).
- **Post-session interview transcript** (audio → mlx-whisper local).
- **NOT recorded:** any user prose outside the Signal session itself (their LinkedIn, their actual résumé, their work products). The corpus is only what they say to Signal.

### 4.4 Post-session interview script (verbatim, asked in order)

Interviewer: a non-founding-team interviewer (recruited per anti-friends-of-team rule, paid honorarium, briefed only on the script — not the metrics or thresholds).

1. **Forced-choice item (M1.1):** *"Here is the narrative you wrote before the session. Here is the narrative Signal extracted. Which is closer to how you actually operate?"* Reads choices.
2. **Scale item (M1.2):** *"On a scale of 1 to 7 — 1 is 'not me at all,' 7 is 'yes, this is me' — how does the Signal narrative feel?"*
3. **Send-as-is item (M1.3):** *"In the next 60 seconds, identify one sentence in this narrative you would send to a hiring manager tomorrow without editing."* Time it.
4. **Specificity scale (M2.1):** *"On a scale of 1 to 7, how specific is this narrative compared to what you would have written yourself?"*
5. **One-sentence-defended T1 (M3.1, M3.2):** *"On the same scale you used before the session — 'I can describe what I do in one sentence I'd defend' — what's your number now?"* Then: *"Now write that one sentence again, without looking at what you wrote before."* Sealed.
6. **Privacy scale (M6.3):** *"On 1 to 7, how much do you trust this product not to leak your data?"*
7. **Open question (analysis-only, NOT pre-registered):** *"What was the worst moment in that session?"* Listen, don't probe. Recorded for postmortem only — does not affect pass/fail.
8. **Open question (analysis-only):** *"Anything I should have asked?"* Listen, don't probe.

Mock-interview (M5) and external-reader review (M4) happen **post-session, separately**, on schedules independent of the user's session day.

### 4.5 Solo or interviewer-present?

User is **solo at the keyboard during the session itself**. Interviewer is in the room (or on a quiet video call) but explicitly silent — present for safety / technical-failure recovery, not for engagement. Pre-session and post-session interview phases are interviewer-present. **The session phase is the test, not the interview.**

---

## 5. Analysis plan

### 5.1 Blinding posture: blinded where possible, open where not

- **Mock interviewer (M5):** does not see Signal's evidence-link annotations until after they have selected the three claims to challenge. Cannot inadvertently pick "easy to defend" claims.
- **External readers (M4):** see only the published narrative, no other context. Do not communicate with each other until both have submitted their one-sentence answer + rating.
- **Two blind raters (M3.2):** receive T0 and T1 sentences in random order, labeled "A" and "B," without knowing which is pre or post. Score "more specific: A / B / tied." Raters are pre-recruited, paid, and are not founding team members.
- **Founding team (Kenji + Vesper):** *cannot* be blinded to which user is which (we ran the screening). However, **the team does not score any pass/fail item directly.** All numerical pass/fail comes from user self-report, mechanical instruments, mock-interviewer, external readers, or blind raters. The team's role is to *aggregate*, not to *judge*.

### 5.2 Who scores what

| Item | Scored by | Blind? |
|---|---|---|
| M1.1 forced choice | User | n/a |
| M1.2 scale | User | n/a |
| M1.3 send-as-is sentence (timed) | Interviewer (objective: did they identify within 60s?) | yes (interviewer doesn't know thresholds) |
| M2.1 scale | User | n/a |
| M2.2 F4 ratio | Suki's nightly metric | mechanical |
| M2.3 word count | Mechanical | mechanical |
| M3.1 scale delta | User (T0 + T1) | n/a |
| M3.2 T0/T1 specificity | 2 blind raters | yes |
| M4 external-reader items | 2 external readers + user | partial (readers blind to other reader; user blind to readers' answers until shown) |
| M5 mock-interview defensibility | Mock interviewer | yes (blind to threshold) |
| M6.1 F2 CI | Mechanical | mechanical |
| M6.2 privacy audit | User runs, Kenji observes | n/a |
| M6.3 trust scale | User | n/a |

### 5.3 When does aggregation happen

**All-at-once after all 5 sessions complete and all M4/M5 reviews submitted.** No metric is computed cohort-aggregate until all data is in.

This is to prevent **momentum bias** — where seeing 2/2 pass on M1 after two sessions makes the team unconsciously interpret session 3's ambiguous answer as "probably a pass." The team does not see per-metric tallies session-by-session. Per-session telemetry is reviewed for technical issues (did F3 fire? did Vey drift?) but pass/fail items are sealed until all data lands.

Pre-registered aggregation procedure:
1. After session 5 + reviews, Kenji and Vesper sit down with all six metrics' raw data.
2. Score per-user pass/fail per §3.1 mechanical rules. No interpretation.
3. Score cohort threshold per §3.2 mechanical rules. No interpretation.
4. Apply §3.2 aggregate decision rule. No interpretation.
5. Write the launch decision document. Reasoning is documenting *what the rules said*, not *whether we agree with what the rules said*.

If at step 4 the team feels the rules produced the wrong answer: **the team is overruled by the rules.** That is the entire point of pre-registration. Document the felt-disagreement in the postmortem; do not change the decision.

---

## 6. Stop rule

### 6.1 No early stop on success

We run all 5 sessions even if the first 3 are unanimous yes. Two reasons: (a) first-three-yes does not eliminate the possibility of last-two-no, and we have committed to ≥3/5 thresholds that require seeing all 5; (b) early-stop-on-success is a known motivated-reasoning hazard.

### 6.2 Early stop on failure: only on M6 privacy

If any user's session triggers a privacy failure (M6.1 F2 CI fails on their build, M6.2 audit shows outbound bytes, or M6.3 trust scale ≤2 with audit-confirmed leak) — **stop immediately**. Do not run remaining sessions. Fix, then re-cohort.

No other metric triggers early stop. We need the full N for any non-privacy decision.

### 6.3 Extension rule (the ambiguity-zone path)

If the cohort-aggregate result lands in §3.2 row "5 pass, 1 fails" *and* the failed metric is M1 or M3 (the felt-quality metrics) *and* the cohort split is exactly 3-pass / 2-fail on that metric:

- **Pre-registered extension to N=7.** Recruit 2 additional users from the same channels with the same screening. Run sessions. Re-aggregate with N=7 using the same thresholds (now ≥4/7 pass, ≤3/7 fail).
- **Decision-maker for invoking extension:** user signoff required. Kenji proposes; user signs the extension off. Vesper double-checks.
- **Cascade flag:** extension to N=7 pushes launch by ~3 calendar days. Recorded in launch ADR.
- **No further extension.** N=7 is the ceiling. If N=7 is still ambiguous, treat as "do not ship."

This is the only condition under which sample size grows mid-study. **Specifically refused:** adding sessions because "we want more data on M5" or "we want to retest the user who had a bad session." Extensions happen on the pre-registered trigger or not at all.

---

## 7. The falsification statement

The paragraph below is written to be quotable verbatim when results land. If results contradict any clause, we do not get to argue about what the clause meant. The clause says what it says.

> **We will conclude Signal's narrative-extraction works iff:** at least 3 of 5 cohort users pass M1 (forced-choice "Signal narrative closer than draft," scale ≥6, send-as-is sentence identified in 60 seconds — all three components), at least 3 of 5 pass M2 (specificity scale ≥5, F4 ratio ≥1.3×, word-count compression), at least 3 of 5 pass M3 (defended-sentence scale delta ≥+2, blind-rater specificity verdict for T1 over T0), at least 3 of 5 pass M4 (two external readers' one-sentence summaries judged accurate by user AND both readers rate ≥5), at least 4 of 5 pass M5 (3-of-3 claims defended in mock interview within 90 seconds each), and 5 of 5 pass M6 (F2 CI green, audit shows zero outbound bytes, trust scale ≥6). **We will conclude it does not work iff:** any 2 of the 6 metrics fail their cohort thresholds, OR M5 alone fails, OR M6 alone fails, OR any single user records a privacy leak that the audit confirms. **We will conclude unclear iff:** exactly one of M1 or M3 fails at a 3-pass / 2-fail split — in which case we extend to N=7 (pre-registered, single extension only) and re-aggregate at the same per-metric thresholds adjusted to 4-of-7 pass / 3-of-7 fail. No re-interpretation of "feels accurate" under deadline pressure is permitted; the rules above are the rules.

---

## 8. What this document does not do (so no one can claim it does)

- Does not validate the product for the wider PRD §5 user population. Per §1: N=5 is internal calibration, not statistical generalization.
- Does not validate Vesper §4 third-return / tenth-visit pacing. Single-session only.
- Does not validate cross-session contradiction detection (deferred to v0.2 per kenji.md §2).
- Does not validate the demo cold-open script (Sofia S1 / signal-aar resolves separately).
- Does not validate hardware floor compliance (Devon's separate domain).
- Does not catch failure modes that the system never exhibits because it never fires the relevant gate. (If F3 never rejects in any session, we cannot conclude F3 works — only that nothing tested it.) We log gate-fire counts and report them honestly.

If results are ambiguous and the path forward is unclear, the document defaults to "do not ship." The asymmetry is intentional. Pre-registration only works if it has teeth, and the teeth are: in any ambiguous case, the conservative reading wins.

---

## 9. Sign-off

This pre-registration is locked when the first session begins. Until then, this document is editable on consent of: Kenji (PM), Vesper (failure-mode), and the user (project owner). Once locked, **no edits, including typo fixes that change meaning**. Typo fixes that don't change meaning are permitted but must be diff-logged.

Coordination with related Round B beads: when signal-r1j (R1 call-graph budget), signal-b5x (M3 first-90-seconds), signal-aar (S1 demo legibility), and signal-ne9 (M1/M2 room-cut governance) close, their outputs may inform §4.2 session phase descriptions (which features users will encounter). Those updates are *describing the system as it is*, not changing the validation criteria. The criteria in §3 and §7 are immutable post-lock.

— Kenji, 2026-05-10
