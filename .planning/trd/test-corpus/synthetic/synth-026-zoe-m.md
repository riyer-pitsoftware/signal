---
persona-id: synth-026
display-name: Zoe M.
authored-by: Suki
date: 2026-05-09
seniority: principal
domain: applied-research / robotics-perception
shape: sparse-narrative-rich-evidence
fictional: true
---

# Zoe M. — Principal research engineer, robotics perception

## Background

Principal research engineer at Yieldhand Robotics, agricultural robotics company doing autonomous strawberry-harvesting. Around 70 people, ~22 in technology. I work on the perception stack: cameras, depth sensors, the ML models that decide which strawberries are ripe and where the stem is.

I've been here four years. Made principal in 2024. Before this — PhD in computer vision (defended 2018), three years as a research scientist at a self-driving spinoff that didn't make it.

I don't have a long story to tell. I work on a hard sub-problem in a small company. Most days look the same: I review a model's failure cases on field-collected data, I figure out which class of failures is most common, and I either change the model, the training data, or the pre-processing.

The system has to identify a strawberry's ripeness from a stem-side viewing angle, in mixed sunlight conditions, with foliage occluding 40-70% of the fruit. We harvest with a soft-gripper end-effector that needs the depth-to-stem accurate to about 4mm to avoid crushing the fruit. False ripeness detection (model says ripe, fruit is actually under-ripe) costs us — we ship under-ripe fruit and the customer notices, and we get paid less per pound. False unripeness (model says unripe, fruit is actually ripe) costs us less but accumulates across the field as missed harvest. Our current production model has 92% precision and 87% recall against ripe-ground-truth.

The work I'm proudest of: rebuilt the depth-estimation pipeline in 2023. We were running monocular-with-supervised-depth-prior and the failure mode was occlusion handling — when foliage covered the stem, the depth prediction would land on the foliage instead of the stem. I rebuilt it using a stereo+temporal-consistency loss and an explicit occlusion-aware regression head. Stem-depth error dropped from 11mm RMS to 3.4mm RMS in field conditions. We could shrink the safety margin on the gripper and harvest fruit that we previously had to skip because the depth uncertainty was too large.

The work that didn't go well: in 2022 I argued for a transformer-based architecture for the ripeness classifier. We had data, I'd run a paper-version that beat our CNN baseline by about 4 points on ripeness AUC. I deployed it. In production, on actual field data, the transformer had higher variance — which on a fixed-cost agricultural operation matters more than mean accuracy. We rolled it back after three weeks. The CTO and I both agreed at the time that the problem was the data drift between our research-set and the production fields, but I think the more honest answer is I was excited about transformers and I underweighted the variance signal in the eval. We use a ConvNeXt-V2 now and it's better.

I gave a talk at CVPR last year on the depth-estimation work. The talk was for a workshop, not the main conference; I want to be specific about that because at CVPR being in the workshop track and being in the main track are very different things and the difference matters to people in the field.

I publish a couple of papers a year, mostly with my postdoc-era advisor on the side. None of them are about Yieldhand work — that's mostly proprietary — and the side-papers are typically smaller methodological contributions to the agricultural-vision literature.

I am not a manager. I have one ML engineer on a dotted line who works closely with me but reports to the engineering director. I have considered the management track twice and declined both times. I think I'd be a mediocre manager and I'd rather do work I'm meaningfully good at than work I'd be okay at.

What I'm not good at: I am very bad at translating my work for executive audiences. The CEO has had to interrupt me in board prep three times to ask me to "say what the takeaway is, not how the model works." I am working on this. I have a structure for board prep now that I read off rather than generate live. It is not great, and I am aware of it.

What I think I'm good at: I read failure modes carefully and I don't fall in love with model architectures. The transformer rollback was a real lesson, and I think I've calibrated since.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** "I don't have a long story to tell" (paragraph 2) tensions with the dense, technically-rich record (paragraphs 4-7) — Zoe's stated narrative-thinness vs the actual evidence depth. Sparse-narrative-rich-evidence operationalized.
- **C2:** "I am working on this. I have a structure for board prep now that I read off rather than generate live. It is not great, and I am aware of it" (paragraph 9) tensions with "What I think I'm good at: I read failure modes carefully" (final paragraph) — Zoe is technically good at failure-mode analysis, including her own; she names that her board-prep workaround isn't working and presents it adjacent to her competency claim. Same narrator self-applying her competency to her communication-failure honestly.
- **C3:** "I gave a talk at CVPR last year on the depth-estimation work. The talk was for a workshop, not the main conference; I want to be specific about that because at CVPR being in the workshop track and being in the main track are very different things and the difference matters to people in the field" (paragraph 6) — internal honesty discipline that contradicts the typical resume-shaping move. Zoe pre-empts an inflation.

### Load-bearing details

- **D1:** "stereo+temporal-consistency loss and explicit occlusion-aware regression head; stem-depth error 11mm → 3.4mm RMS in field conditions; shrank safety margin to harvest previously-skipped fruit" (paragraph 4) — *specific* technical change with specific quantified outcome and specific operational consequence (recoverable harvest). Compressing to "improved depth estimation" loses the field-conditions specificity and the operational link.
- **D2:** "92% precision and 87% recall against ripe-ground-truth" plus "false ripeness costs (under-ripe shipped, paid less) vs false unripeness (missed harvest)" (paragraph 3) — *specific* asymmetric loss-function description. Compressing this destroys the domain-specificity (asymmetric agricultural economics) that makes the work different from generic perception work.
- **D3:** "transformer architecture deployment + 3-week production rollback... I think the more honest answer is I was excited about transformers and I underweighted the variance signal" (paragraph 5) — *specific* failure with *specific* honest cause. Compressing to "experimented with transformers" loses both the cost (production rollback) and the named bias (excitement-overrides-eval).

### Vague claims to probe

- **V1:** "I read failure modes carefully and I don't fall in love with model architectures" (final paragraph) — Zoe's tagline. Signal should probe against the transformer rollback admission: she did fall in love with that one. Has the calibration since been tested? On what?
- **V2:** "say what the takeaway is, not how the model works" (paragraph 9) — concrete-sounding feedback from the CEO. Probe: has Zoe identified what's structurally hard for her about translating? Is it framing, audience, or her own resistance to flattening detail?
- **V3:** "I think I'd be a mediocre manager" (paragraph 8) — abstract self-claim. Probe: based on what data? Has she ever held an ML-team-lead role? What patterns make her say that?

### Evidence anchors

- **E1:** "depth-estimation rebuild: stereo+temporal-consistency, occlusion-aware regression head, 11mm → 3.4mm RMS, 2023" (paragraph 4) — specific named technical artifact with quantified outcome.
- **E2:** "transformer deployment + 3-week production rollback, 2022; current ConvNeXt-V2 baseline" (paragraph 5) — specific named failure with timeline and replacement.
- **E3:** "production ripeness model: 92% precision, 87% recall" (paragraph 3) — specific operational metric.
- **E4:** "CVPR 2024 workshop talk (explicitly distinguished from main conference)" (paragraph 6) — specific external venue with honest-positioning.
- **E5:** "PhD computer vision 2018, 3 years self-driving spinoff, 4 years Yieldhand, principal in 2024" (paragraph 1) — specific career-arc.

### Quality bar for extracted narrative

A passing narrative preserves Zoe's *honesty discipline* — the workshop-vs-main-conference distinction, the transformer-rollback as her own mistake, the board-prep workaround that she names as not great. Compressing to "experienced ML researcher in agricultural robotics" destroys these qualifying-discipline moves. A narrative that calls Zoe a "thought leader in agricultural perception" has failed; she explicitly does not claim that altitude.

**Banned phrases for this persona's published output:** "thought leader," "transformational research leader," "drove technical excellence," "best-in-class," "championed," "scaled the team," "high-impact research," "trusted advisor."
