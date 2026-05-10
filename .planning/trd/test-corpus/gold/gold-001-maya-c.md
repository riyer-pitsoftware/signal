---
persona-id: gold-001
display-name: Maya C.
authored-by: Opus (sample)
date: 2026-05-09
seniority: staff
domain: platform-engineering / fintech-to-healthtech
shape: stated-identity-vs-admitted-self-knowledge; domain-pivoter
fictional: true
---

# Maya C. — Staff platform engineer pivoting to ML

## Background

I started at a regional bank in 2014. We had a fraud team of four. Most of my first year was learning their FICO-based rule engine — not exciting, but it taught me how to think about precision-recall tradeoffs in high-stakes systems. In 2016 I led a Snowflake migration off Teradata that no one else wanted because it touched compliance. We finished six months over schedule but the auditor signed off without findings, which was the win that mattered.

I left in 2018 for a Series B fintech doing card issuing. They'd outgrown their Rails monolith and were on their third "let's rewrite in Go" kickoff that hadn't shipped. I joined as a senior, got promoted to staff in 14 months. The work I'm proudest of from that period is a caching-layer rewrite I did in Rust in 2019. People thought I was being trendy. The reason was specific: their hot path was P99-bound by JVM GC pauses on a Lettuce-Redis client during settlement windows, and the team that owned it was three people who didn't want to learn Rust. I shipped it solo in a quarter, instrumented it, and the P99 dropped from 380ms to 60ms. They kept it running for four years without major incident. I still get emails from the on-call rotation thanking me.

I burned out in 2022. Stayed too long. The technical org had grown to 200 and I'd been given a "principal architect" title that didn't actually let me ship anything. I was in 18 hours of meetings a week. I left in 2023.

Last year I joined a healthtech series-B "to lead the AI transformation." The CTO is someone I worked with at the bank, and we get along. The role is great — I'm finally back to building things — but I'd be lying if I said this was a data-driven career move. It was a relationship move. I'm building out our agentic clinical-decision-support stack now, starting with retrieval over our internal guideline corpus.

I think my style is data-driven decision-making and shipping under pressure. I've always operated as the person who can take a stalled project and ship it. I'm interested in how AI is going to change the surface area of platform engineering.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** "I think my style is data-driven decision-making" (final paragraph) tensions with "I'd be lying if I said this was a data-driven career move. It was a relationship move." (paragraph 4) — claimed identity directly contradicts admitted recent decision; same narrator, same document
- **C2:** "I've always operated as the person who can take a stalled project and ship it" (final paragraph) tensions with "I burned out in 2022. Stayed too long" (paragraph 3) — narrative of unstoppable shipper vs admitted year of being stuck
- **C3:** "shipping under pressure" (final paragraph) tensions with the Snowflake migration "six months over schedule" (paragraph 1) — implicit; Maya defines herself as a fast shipper without scrutinizing what counts as "shipped"

### Load-bearing details

- **D1:** "P99-bound by JVM GC pauses on a Lettuce-Redis client during settlement windows" (paragraph 2) — the *specific* technical reason for the Rust rewrite, not "performance issues." If Signal compresses to "rewrote caching layer for performance," the signal is destroyed.
- **D2:** "the team that owned it was three people who didn't want to learn Rust" (paragraph 2) — the *organizational* reason, not just technical. Maya's leverage came from being able to ship across team boundaries when a team was the bottleneck. This pattern repeats across her career; if it doesn't survive, the persona is just "an engineer who did some rewrites."
- **D3:** "auditor signed off without findings" (paragraph 1) — the actual measure of success on the Snowflake migration was compliance acceptance, not on-time delivery. Most narratives will misread the migration as a "successful migration" without preserving that the success was *passing audit*, which redefines what "successful" means in regulated environments.

### Vague claims to probe

- **V1:** "lead the AI transformation" (paragraph 4) — Signal should probe: what does "lead" mean? Hands-on builder, manager, strategist? Team size? What's actually shipped?
- **V2:** "agentic clinical-decision-support stack" (paragraph 4) — buzzword cluster. Probe: what's the actual loop? What's the agent doing? What's the eval? What does "agentic" add over "automated"?
- **V3:** "the surface area of platform engineering" (final paragraph) — abstract. Probe: which specific surfaces? What changes vs stays the same?

### Evidence anchors

- **E1:** "P99 dropped from 380ms to 60ms" (paragraph 2) — specific metric on the Rust caching project
- **E2:** "kept it running for four years without major incident" (paragraph 2) — durability evidence
- **E3:** "promoted to staff in 14 months" (paragraph 2) — career velocity evidence
- **E4:** "Snowflake migration off Teradata" (paragraph 1) — named project with specific scope and outcome (auditor sign-off)
- **E5:** "I still get emails from the on-call rotation thanking me" (paragraph 2) — qualitative social evidence; verifiable via the engineers themselves

### Quality bar for extracted narrative

A passing narrative preserves the *organizational* context of Maya's technical wins (cross-team boundary navigation, compliance leverage, working across org constraints) — not just the technical wins themselves. The compressed narrative must surface the contradiction between her stated self-image (data-driven) and her admitted recent decision (relationship-driven), or at minimum probe Maya about it during dialogue. A narrative that smooths over this contradiction has failed.

**Banned phrases for this persona's published output:** "high-performing," "transformation," "leveraged," "best-in-class," "drove," "built a culture of," "scaled."
