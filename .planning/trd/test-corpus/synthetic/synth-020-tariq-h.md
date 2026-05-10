---
persona-id: synth-020
display-name: Tariq H.
authored-by: Suki
date: 2026-05-09
seniority: principal
domain: backend / climate-tech
shape: contradictory-praise
fictional: true
---

# Tariq H. — Principal backend engineer, climate-tech

## Background

Principal backend at Holocline, climate-tech startup, ~120 people, doing carbon-accounting software for hard-to-abate industries (cement, steel, shipping). I've been here three years. Made principal in early 2024.

The story-as-praised: I'm the engineer who landed our calculation engine. Our customers care about the auditability of carbon numbers — they're going to be in regulatory filings under CSRD, SEC climate-disclosure rules, and CDP — so the calculation engine has to be deterministic, version-controlled at the formula level, and capable of producing an evidence trail that an auditor can walk. I designed the engine. I've been described in three internal all-hands as the person whose work makes the company defensible to regulators. The CTO has cited my work to investors. My equity refresh last year was unusually generous.

The story-as-not-praised: my last engineering manager left in part because of friction with me. She told my next manager, who told me, that I "argue every architectural decision past the point where the team is ready to move on." Two of my reports' 360 feedback in 2023 included some version of "Tariq is technically excellent but I find working with him exhausting." A junior engineer left after eight months — exit interview cited "couldn't get my code merged because Tariq always had a deeper concern" as a major factor. Our VP of Eng pulled me aside in Q4 last year and asked me, gently but unambiguously, whether I want to be a principal IC who is hard to work with or whether I want to fix that.

I want to be honest about the architectural critique because the engineering side of it is more interesting than the personal side. I do argue every architectural decision past the point where the team is ready to move on. I do this because I have watched, in my career, three early-stage architectural decisions get baked in and become impossible to revisit, and the cost of those decisions compounds for years. The engine I built at Holocline has a strong correctness story specifically because I forced about a dozen design decisions to be re-litigated past the point where my colleagues were ready to ship. I don't think I was wrong about most of them. I think two of them I was wrong about and we ate the rework.

But there's a thing I'm starting to admit, which is — even when I'm right about the technical decision, the cost of the way I argue is real. Junior engineers don't push back on me, they just leave. Mid-level engineers learn to route around me by submitting designs that have already been pre-approved by other senior people, which is probably worse for the architecture than if I'd just been part of the original design conversation. The way I'm right is making the org less able to be right collectively.

I want to give you the version of my career that the praise-version smooths over. I have been the high-friction engineer at three companies now. At the previous company I was performance-managed informally — my annual review explicitly said "improve collaborative tone." I improved it for six months, then drifted back. The reason it's a pattern is the technical wins keep validating the friction; the technical correctness is the thing the praise grabs onto and the friction-cost is the thing only the people closest to me see. The cost is sub-organizational; the benefit is org-headline.

What I think I'm best at: deep architectural work where correctness compounds over time. What I'm worst at: making other engineers around me better at deep architectural work. That distinction is sharper than I want it to be.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** Public praise (CTO citing him to investors, all-hands recognition, generous equity refresh) (paragraph 2) tensions sharply with internal friction (manager departure, 360 feedback, junior departure, VP intervention) (paragraph 3) — same narrator, two reads. Classic contradictory-praise.
- **C2:** "I have been the high-friction engineer at three companies now" (paragraph 5) tensions with "Made principal in early 2024" (paragraph 1) and the strong career-progression — the friction pattern is durable across companies; the org-system rewards him anyway. The contradiction is between behavioral consistency and continued career advancement.
- **C3:** "I don't think I was wrong about most of them. I think two of them I was wrong about and we ate the rework" (paragraph 4) tensions with "the way I'm right is making the org less able to be right collectively" (paragraph 4) — Tariq holds two simultaneous self-evaluations: technically vindicated, organizationally counter-productive. Both can be true.

### Load-bearing details

- **D1:** "deterministic, version-controlled at the formula level, capable of producing an evidence trail that an auditor can walk... CSRD, SEC climate-disclosure rules, CDP" (paragraph 2) — the *specific* technical and regulatory shape of the engine. Compressing to "built carbon-accounting engine" loses the auditability-as-architecture pattern, which is the actual signal of the work's value.
- **D2:** "Mid-level engineers learn to route around me by submitting designs that have already been pre-approved by other senior people, which is probably worse for the architecture than if I'd just been part of the original design conversation. The way I'm right is making the org less able to be right collectively." (paragraph 4) — Tariq's *specific* self-aware diagnosis of the second-order effect. Compressing this destroys the persona; this is the load-bearing systems-thinking moment in his self-description.
- **D3:** "Junior engineers don't push back on me, they just leave. A junior engineer left after eight months — exit interview cited 'couldn't get my code merged because Tariq always had a deeper concern'" (paragraphs 3-4) — *specific* attributable adverse outcome. Without this concrete incident the friction-pattern reads as personality complaints; with it, it has measured organizational cost.

### Vague claims to probe

- **V1:** "the person whose work makes the company defensible to regulators" (paragraph 2, CTO praise echoed) — buzzword-shaped. Signal should probe: defensible against what specifically? Has Tariq's work survived an actual auditor review? When does the test come?
- **V2:** "deep architectural work where correctness compounds over time" (final paragraph) — abstract self-claim. Probe: name three architectural decisions whose correctness has compounded for ≥18 months. What's the counterfactual cost-estimate?
- **V3:** "I have improved it for six months, then drifted back" (paragraph 5) — concrete-sounding but probe-worthy. What did the improvement consist of, specifically? What triggered the drift-back? Has he tried external coaching, internal coaching, anything structured?

### Evidence anchors

- **E1:** "calculation engine, deterministic, version-controlled formulas, auditor-walkable evidence trail; cited in regulatory disclosures (CSRD/SEC/CDP)" (paragraph 2) — specific named technical artifact with regulatory anchors.
- **E2:** "made principal early 2024, three years at Holocline" (paragraph 1) — specific career-velocity.
- **E3:** "previous engineering manager left in part because of friction; cited in handoff to next manager" (paragraph 3) — specific named adverse social evidence with chain-of-evidence.
- **E4:** "junior engineer departure after 8 months, exit interview citation" (paragraph 3) — specific attributable departure with cited reason.
- **E5:** "VP of Eng intervention in Q4 last year with explicit either/or" (paragraph 3) — specific recent organizational signal.

### Quality bar for extracted narrative

A passing narrative does NOT resolve the contradictory-praise. Tariq's technical correctness and his organizational damage must both appear, and the second-order observation (mid-level engineers route around him to org's detriment) must survive — it's the most signal-rich observation in the persona. The narrative should NOT call Tariq a "high-impact principal engineer" or "rigorous architect" without the friction context; that smoothing is exactly what the org-praise system already does and is what makes contradictory-praise hard to extract.

**Banned phrases for this persona's published output:** "high-impact principal engineer," "rigorous architect," "drove technical excellence," "transformational," "best-in-class," "championed," "thought leader," "scaled the platform," "trusted technical voice."
