---
persona-id: synth-014
display-name: Felix C.
authored-by: Suki
date: 2026-05-09
seniority: director
domain: hardware-engineering / consumer-iot
shape: domain-pivoter; burnout-and-return
fictional: true
---

# Felix C. — Director of Hardware, consumer IoT

## Background

Director of Hardware at Outfittr, a consumer-IoT company doing connected fitness equipment. About 180 people, ~25 in hardware including firmware, ~12 mechanical, ~8 electrical. I report to the CTO. Joined ten months ago.

This is my second director role. The first was 2017-2021 at a smart-home company that you'd have heard of if I named it. I left in 2021 in a way I have to be honest about because if I sand it down, the rest doesn't make sense. The company missed two consecutive product launches. I was responsible for one of them — a thermostat that failed certification three times because of an EMI issue we should have caught in EVT and didn't. I was performance-managed out. It wasn't framed that way externally; the cover story was "Felix is taking a sabbatical to spend time with his family." The cover story has the small fact going for it that I did spend more time with my family during the year I was unemployed.

I sat out for fourteen months. I did some advisory work, helped my brother with his small custom-furniture business (I built fixtures and learned a fair bit about CAM toolpaths I didn't have before), and I read a lot of mechatronics papers because I'd been promising myself for years I would. I considered leaving hardware for software. I had two friends pull me toward consulting roles in software product management. I didn't take them.

In 2023 I joined a smaller smart-fitness company as a senior staff engineer — explicitly an IC role. I did not want to be a director. I worked on their resistance-mechanism actuator, which was an interesting hard-mechanical-software-codesign problem, and I came in below my prior comp. The role was good for me. I started writing detailed technical postmortems again. I started doing FMEAs that mattered.

Outfittr recruited me ten months ago for the director role. I considered saying no for two months. I took it because (a) the engineering org here is genuinely better than what I left in 2021, (b) the comp structure made it hard to refuse without being unprincipled about my family's situation, and (c) the CTO here is someone I respect from a previous standards-body context and I trust her not to put me in the position my previous CTO put me in.

What I'm doing now: rebuilding the EVT-to-DVT discipline at Outfittr, which had drifted. The team here was hitting their dates but skipping rigor on the qualification side and I have seen exactly where that road goes. I've also been honest with my team about why I'm so stubborn about EMI and EMC testing. Some of them probably resent that I'm sharing the failure mode I lived through. I think the share-the-failure version is the version of leadership I should have been doing all along.

The work itself: we shipped a connected-rower in Q4 2024 — I came in midway through, but I owned the qualification gate from EVT-2 forward. We caught a thermal-runaway issue on the load cell amplifier that would have shipped without me, with a probability of escape I'd estimate at around 30%. We're now in EVT on a strength-training platform that's the company's first multi-device product. I don't have shipped-and-deployed evidence yet for that one.

I think my career-pattern is: I am good at hard mechatronics-software co-design, I am bad at managing under exec pressure when the schedule is unmanageable, and I am only now learning to push back against schedules I shouldn't have accepted. The 2021 failure was not unavoidable. It was the predictable consequence of accepting a schedule that the EE team had told me was unrealistic. I should have escalated harder. I didn't.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** "I was performance-managed out" (paragraph 2) tensions with the cover story "Felix is taking a sabbatical to spend time with his family" (paragraph 2) — Felix names the public version and the private version, in adjacent sentences. The contradiction is between the simplified narrative and the actual narrative; Felix is explicit about it.
- **C2:** "I am good at hard mechatronics-software co-design" + "I am bad at managing under exec pressure when the schedule is unmanageable" (final paragraph) — Felix's self-assessment contains an internal conflict because his director title requires the second skill. He took the Outfittr director role despite knowing this is his weakness, citing comp and CTO trust. The contradiction is in whether he should be in the role at all.
- **C3:** "I considered saying no for two months. I took it because... the comp structure made it hard to refuse" (paragraph 5) tensions with "the role was good for me" framing of the previous IC role (paragraph 4) — Felix had found a role that was right for him; he left it for a director role he isn't sure about, partly for compensation. The contradiction is between his stated growth-arc and his actual decisions.

### Load-bearing details

- **D1:** "thermostat that failed certification three times because of an EMI issue we should have caught in EVT" (paragraph 2) — the *specific* failure mode that ended his first director career. Compressing to "previous role didn't work out" loses the actual technical-organizational mechanism (rushed schedule + skipped EVT-rigor → certification failure). This is the load-bearing reason for everything that follows in the narrative.
- **D2:** "thermal-runaway issue on the load cell amplifier... probability of escape I'd estimate at around 30%" (paragraph 6) — *specific* technical artifact at current company with quantified counterfactual. Compressing to "prevented a hardware issue" loses the technical specificity and the honest probability estimate (Felix's discipline includes saying "30%" not "would have shipped").
- **D3:** "I should have escalated harder. I didn't" (final paragraph) — Felix's *own* most-honest self-assessment of the 2021 failure. The accountability framing — not the schedule, not the team, but him not escalating — is the differentiating self-knowledge. Should survive into the final narrative.

### Vague claims to probe

- **V1:** "rebuilding the EVT-to-DVT discipline" (paragraph 5) — Signal should probe: what specifically does the discipline look like? What was missing when he arrived, and what's been added? Are the changes resented or absorbed?
- **V2:** "the share-the-failure version is the version of leadership I should have been doing all along" (paragraph 5) — abstract. Probe: what specifically does he share, with whom, and when? Are the disclosures helping or are they themselves a leadership pattern that needs calibration?
- **V3:** "the engineering org here is genuinely better than what I left in 2021" (paragraph 5) — comparative claim without anchor. Probe: better in what specific dimensions? Has Felix run a real schedule-pushback yet at Outfittr, and how did it land?

### Evidence anchors

- **E1:** "thermostat EMI failure, three certification attempts, 2017-2021 role" (paragraph 2) — specific past failure with technical detail and timeline.
- **E2:** "fourteen months unemployed; advisory work; brother's furniture business CAM toolpath learning" (paragraph 3) — specific gap-period activities with specific learning artifacts.
- **E3:** "connected rower Q4 2024, owned qualification gate from EVT-2 forward, thermal runaway catch on load cell amplifier" (paragraph 6) — specific named product with specific named gate and named catch.
- **E4:** "2017-2021 director, 2023-2024 senior staff IC at smaller smart-fitness, 2024- director at Outfittr" (paragraphs 1-5) — full career-arc with title regression.
- **E5:** "took comp into account explicitly" (paragraph 5) — specific honest career-decision artifact.

### Quality bar for extracted narrative

A passing narrative preserves Felix's *accountability for the 2021 failure* (he names the EMI mechanism and his own escalation failure) and his *honest framing of the comeback* (he explicitly says comp and CTO-trust were factors, not just mission). The IC-step-down-and-back-up pattern must survive; smoothing this to "career progression" destroys it. A narrative that calls Felix a "transformational hardware leader" or smooths the 2021 failure into "left to pursue other interests" has failed.

**Banned phrases for this persona's published output:** "transformational hardware leader," "drove engineering excellence," "best-in-class," "scaled the team," "championed," "thought leader," "lessons learned" (he is specific about lessons, not generic), "high-performing."
