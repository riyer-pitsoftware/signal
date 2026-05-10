---
persona-id: synth-013
display-name: Rebecca L.
authored-by: Suki
date: 2026-05-09
seniority: principal
domain: ml-data / biotech
shape: contradictory-praise
fictional: true
---

# Rebecca L. — Principal data scientist, biotech

## Background

Principal data scientist at Cellatrix Therapeutics, a clinical-stage biotech (~340 people, ~12 in computational). I report into the SVP of Translational Sciences. Joined 2020 as senior, made principal in 2023.

The headline of my work: I built our patient-stratification analytics for the lead Phase 2 trial that read out positive in late 2024. The trial enrolled 320 patients with a hard-to-diagnose autoimmune condition. My team's biomarker-stratification model identified the responder subgroup that drove the trial's hazard-ratio significance. Without that subgroup analysis the trial was a wash. The CSO presented it at JP Morgan Healthcare in January and the company's market cap moved on it.

I want to give you the messy version because the headline isn't actually the story.

The CSO loves my work. He's mentioned me by name in two earnings calls. He has me in front of the board for any computational discussion. I got a meaningful equity refresh last year and I think I'm one of the most-protected people in the company in a layoff scenario.

The principal investigator on the trial does not love me. She thinks the stratification analysis was post-hoc cherry-picking and that the trial would have been called negative under the original analysis plan, which it would have been. She has said this in two different forums I was present for. She's correct that the analysis was post-hoc. I argued at the time, and still argue, that the post-hoc analysis was statistically defensible because we'd pre-registered the biomarker hypothesis even if not the cutoff value, and the FDA accepted it in our follow-up communication. But she has a real concern and I am not going to pretend it isn't real.

The clinical operations team — the people who actually run the trial — are split. Two of the senior CRAs trust me; one explicitly doesn't. The data manager has filed concerns about my team's data-handling practices twice. They were not, in my view, valid concerns; they reflect a different model of who has authority over what. But they're on the record.

So the contradictory-praise version is: my professional reputation in the company is a function of who you ask, and which version is "real" depends on whether the trial readout holds up in Phase 3. If it does, I'm the data scientist who saved the program. If it doesn't, I'm the data scientist who p-hacked our way into a press release.

The honest version of my career is I have made a series of bets on biomarker-driven trial design at three companies (this one, a previous biotech where the trial failed, and a CRO before that where I was a junior on someone else's trial). One trial failed. One trial (this one) is mid-readout. The CRO trial succeeded but I had a small role. I have a real win, a real loss, and an uncertain win. The way the industry works, the most-recent uncertain win is what people remember. I know that. I'm trying to use that visibility to push for better practices in our Phase 3 design.

What I think I'm best at: identifying which patient population a treatment will work for, given partial early-trial data. What I'm worried about: I think I'm above-average at this and I think the variance on biomarker-driven analysis is high enough that I can't tell if I'm above-average because I'm right or because I survived the variance.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** CSO's praise (mentions in earnings calls, equity refresh, board access) (paragraph 3) tensions sharply with the PI's documented concern that the stratification was post-hoc cherry-picking (paragraph 4) — same work, two senior named stakeholders, opposing readings. Both have power; both are correct from their vantage. Classic contradictory-praise.
- **C2:** "I argued at the time, and still argue, that the post-hoc analysis was statistically defensible" (paragraph 4) tensions with "I think the variance on biomarker-driven analysis is high enough that I can't tell if I'm above-average because I'm right or because I survived the variance" (final paragraph) — Rebecca defends her work publicly while privately holding deep uncertainty about whether her track record reflects skill or noise. Same narrator, two epistemic stances within the same document.
- **C3:** "the data manager has filed concerns about my team's data-handling practices twice. They were not, in my view, valid concerns" (paragraph 5) — Rebecca documents the concerns then dismisses them in adjacent sentences, then immediately concedes "they're on the record." Multiple pivots in three sentences; the contradiction is between her dismissal and her preservation of the adverse evidence.

### Load-bearing details

- **D1:** "the trial would have been called negative under the original analysis plan" (paragraph 4) — the *specific* technical core of the contradiction. If Signal compresses to "led successful biomarker analysis," the load-bearing fact (the analysis was post-hoc and the original plan would have failed) is destroyed. This is the actual signal of Rebecca's situation.
- **D2:** "we'd pre-registered the biomarker hypothesis even if not the cutoff value, and the FDA accepted it in our follow-up communication" (paragraph 4) — Rebecca's *specific* defense. Compressing to "the analysis was approved" loses the precise structure (hypothesis pre-registered, cutoff post-hoc, regulator accepted). The specifics are what differentiate defensible-from-indefensible in this domain.
- **D3:** "I have a real win, a real loss, and an uncertain win... the most-recent uncertain win is what people remember" (paragraph 6) — Rebecca's *own* most-honest meta-pattern. The career-shape, not the project-shape. Should survive into final narrative; it's the line that distinguishes her from the heroic-data-scientist version.

### Vague claims to probe

- **V1:** "saved the program" (paragraph 6, in the conditional) — buzzword that gets applied to her if the trial holds. Signal should probe: what does saving look like operationally? What would not-saving look like? Is the framing of saving even the right frame for what she did?
- **V2:** "biomarker-driven trial design" (paragraph 6) — domain-specific jargon. Probe: what are the alternatives to biomarker-driven? What's her track record in choosing whether to pursue a biomarker-driven approach in the first place (versus pre-specified, all-comers)?
- **V3:** "I think I'm above-average at this" (final paragraph) — vague self-claim, immediately self-undercut. Probe: above-average against what reference class? Has she ever bet on a biomarker hypothesis and been wrong about which subgroup would respond? When?

### Evidence anchors

- **E1:** "Phase 2 trial, 320 patients, autoimmune indication, late 2024 readout, hazard ratio significance from responder-subgroup analysis" (paragraph 2) — specific named outcome with patient count and analytical method.
- **E2:** "CSO mentioned by name in two earnings calls; equity refresh last year" (paragraph 3) — specific positive social/financial evidence.
- **E3:** "PI's stated concern about post-hoc cherry-picking, voiced in two forums" (paragraph 4) — specific adverse evidence with named stakeholder.
- **E4:** "data manager filed concerns twice; one CRA trusts me, two don't / two do, one doesn't" (paragraphs 4-5) — granular operational evidence with quantified positions.
- **E5:** "previous biotech trial failed; CRO trial succeeded with my small role" (paragraph 6) — full career track record with named outcomes.

### Quality bar for extracted narrative

A passing narrative does NOT resolve the contradictory-praise. The CSO's reading (Rebecca saved the program) and the PI's reading (Rebecca p-hacked the result) must both appear, and the narrative must surface that the resolution depends on Phase 3 readout — i.e., on the future, not on the present. Rebecca's own epistemic uncertainty about her track record (skill vs variance) is the load-bearing self-frame and should survive. A narrative that calls her an "expert biomarker analyst who drove trial success" has flattened exactly what makes the persona useful for calibrating contradictory-praise detection.

**Banned phrases for this persona's published output:** "drove trial success," "saved the program" (echoing without probing), "transformational analytics leader," "best-in-class," "championed," "thought leader," "trusted advisor," "scaled the analytics function."
