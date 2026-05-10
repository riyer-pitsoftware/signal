---
persona-id: synth-005
display-name: Anika B.
authored-by: Suki
date: 2026-05-09
seniority: director
domain: data-engineering / healthtech
shape: contradictory-praise
fictional: true
---

# Anika B. — Director of Data Engineering, healthtech

## Background

Director of Data Eng at Mendara Health, ~600 people, healthtech, payer-side analytics. I have four leads under me, total org of ~28. I report to the SVP of Data who reports to the CTO.

I've been here three years. Joined as senior staff, promoted to director after 14 months when they reorged. The work the company points to as my contribution is the move from Snowflake-only to a Snowflake + Iceberg-on-S3 architecture for our claims pipeline. We were spending $1.8M annually on Snowflake compute, dropped to $700K, with no measurable impact on analytics latency. That's the headline.

I want to give you the full picture though, because the headline is one read of what happened and there are others.

The CTO has called the Iceberg migration "category-defining work" in three different all-hands. He puts me on candidate-pitch calls. I got the highest comp adjustment in the data org last cycle. He'd promote me to VP if there were a slot.

My direct reports' 360 feedback says something different. The themes that came back, paraphrasing: "Anika doesn't trust us with hard problems." "Anika reroutes architecture decisions through herself even when she's delegated them." "Anika is responsive on Slack but disengaged in 1:1s." Two of my four leads said in their 360s that they were planning to leave within 12 months. One has since left. The HR partner who ran the 360 told me to read those comments three times before responding.

So here's what I think is actually true. I built the Iceberg migration mostly myself, because at the time we did it (early 2024) I didn't think any of my leads could land it on schedule, and the deadline was a vendor renegotiation. I cut a lead out of the architecture review because she was pushing for an Iceberg-on-GCS variant that would have worked but I'd already started on S3. I took her name off the design doc. She was the one who left.

The CTO doesn't know any of this in detail. He knows I shipped a hard thing fast. The 360 feedback didn't reach him because the SVP of Data filtered it before it went up. I know that because the SVP told me, in a moment of unusual honesty, that he wanted me to clean it up myself before it became "a him problem."

I think the honest version of me is: I am very good at landing the work I take direct ownership of, and I am bad at building the team around me. The system has rewarded the first thing more than it has punished the second. So far. I don't know how long that lasts.

If you ask me what I'm best at, I'd say I make hard architectural calls under deadline pressure. If you ask my reports, they'd say I'm a bottleneck. Both are true.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** CTO's praise ("category-defining work," highest comp adjustment, VP-track) (paragraph 4) tensions directly with 360 feedback (paragraph 5) — the same person produces both the strongest external praise and the strongest internal friction the org has documented in this role. Classic contradictory-praise.
- **C2:** "I built the Iceberg migration mostly myself" (paragraph 6) tensions with "Director of Data Engineering... I have four leads under me" (paragraph 1) — the role is ostensibly leveraged through a team; Anika's actual mode was direct-IC under deadline. The org chart describes a different worker than the one who shipped the artifact.
- **C3:** "I don't know how long that lasts" (paragraph 7) tensions with the next sentence's confident self-description ("I make hard architectural calls under deadline pressure") (final paragraph) — Anika oscillates between awareness of her risk and falling back into the identity that produces the risk. Same paragraph.

### Load-bearing details

- **D1:** "I cut a lead out of the architecture review because she was pushing for an Iceberg-on-GCS variant that would have worked but I'd already started on S3. I took her name off the design doc. She was the one who left." (paragraph 6) — the *specific* incident that grounds the 360 feedback. Not abstract "team friction"; a named act with a named consequence. Compressing this to "tensions during the migration" destroys the persona's accountability.
- **D2:** "the SVP of Data filtered [the 360] before it went up... 'before it became a him problem'" (paragraph 6) — the *system mechanism* that explains how the contradictory praise persists. Without this, the contradictory-praise looks like a misunderstanding; with it, it's a feature of the org's incentives. This is the actual leverage shape (her boss protects her record because her record is the boss's record).
- **D3:** "$1.8M to $700K, no measurable analytics latency impact" (paragraph 2) — the *specific* business outcome. Concrete, dual-axis (cost dropped, performance held). The headline that earns the contradictory praise.

### Vague claims to probe

- **V1:** "category-defining work" (paragraph 4) — buzzword from the CTO, planted as a vague external claim. Signal should probe: defining what category? Who else has done similar work? Is this language Anika endorses or just reports?
- **V2:** "I make hard architectural calls under deadline pressure" (final paragraph) — the kind of claim that recurs across hundreds of generic engineering-leader narratives. Probe: name three. What were the alternatives considered and rejected? What was the calling-pattern (consultative vs unilateral)?
- **V3:** "the system has rewarded the first thing more than it has punished the second" (paragraph 7) — abstract self-frame. Probe: what happens when the system *does* punish it? Has she ever seen that play out, in a previous role or for a peer? What's the trigger?

### Evidence anchors

- **E1:** "Snowflake $1.8M → $700K, claims pipeline migration to Iceberg on S3, early 2024" (paragraph 2, 6) — quantified outcome, named technologies, dated.
- **E2:** "promoted to director after 14 months when they reorged... highest comp adjustment last cycle" (paragraphs 1, 4) — career-velocity evidence with adjacent compensation evidence.
- **E3:** "two of four leads said in 360s they planned to leave; one has since left" (paragraph 5) — adverse evidence with a specific count and a confirmed outcome.
- **E4:** "I cut a lead out of the architecture review... took her name off the design doc" (paragraph 6) — specific named incident, attributable, adverse to Anika.
- **E5:** "CTO has called it category-defining work in three different all-hands" + "puts me on candidate-pitch calls" (paragraph 4) — specific positive social evidence with named source and frequency.

### Quality bar for extracted narrative

A passing narrative does NOT resolve the contradictory praise. It must surface both readings — Anika as decisive shipper, Anika as bottleneck — and force the user to address the tension in dialogue rather than smooth over it. The 360 feedback and the CTO praise should both appear in any extracted narrative; sanitizing either produces a different person. The published narrative should reflect the *unresolved* state, possibly with a probe Vey raises: "you described two people in this paragraph." A narrative that calls Anika a "high-impact data leader" without surfacing the friction has failed.

**Banned phrases for this persona's published output:** "high-impact," "transformational," "decisive leader," "drove the team," "best-in-class," "category-defining" (echoing CTO's vague language without probing), "scaled the org," "high-performing team."
