---
persona-id: synth-004
display-name: David R.
authored-by: Suki
date: 2026-05-09
seniority: staff
domain: embedded / robotics
shape: sparse-narrative-rich-evidence
fictional: true
---

# David R. — Staff embedded engineer, warehouse robotics

## Background

I work on warehouse robots. Staff engineer at Linehaul Software, we make autonomous mobile robots for fulfillment centers. Been there since 2019.

I don't have a long story. I joined as senior, made staff in 2022. I work on the motion-control stack and the safety-supervisor process, mostly the layer between perception and the wheel motors. There's not really a narrative arc. I just kept fixing things.

What I'm best at is reading hardware datasheets and being right about them. That sounds dumb but it's actually rare. Most software people skim. I read the errata sheets too, including the ones marked "preliminary."

Kind of don't know what else to say. I've worked on three platforms — the AMR-7 (deprecated), the AMR-9 (current), and the prototype 11 platform. I wrote the original PID tuning for AMR-9's drive train in C++ on the FreeRTOS layer. We hit a 0.94 success-rate-per-mile across our fleet, which I think is industry-decent though I don't have great comp data. Before this I did 8 years at a defense contractor on inertial measurement systems — won't say which because they don't like being mentioned in non-cleared contexts even though the project I was on was unclassified.

I guess one thing — I caught the AMR-9 brake regression in November 2024. It was a controller firmware update from our Tier-1 supplier and they swore the timing characteristics hadn't changed. I had a script that ran the regression suite against every drop, including supplier deliveries. It caught it inside two hours. We held the deploy. The supplier had quietly shifted their interrupt latency by 8 microseconds because they fixed an unrelated bug; that 8us made our supervisor process miss its deadline 0.3% of the time, and 0.3% across a fleet of 4000 robots is one near-miss every two days. Could have been bad.

I think my style is — I assume vendors are wrong until I've measured them being right. I assume firmware is wrong until I've watched it on a logic analyzer. I write tests for things people don't think need tests because I've seen those things break.

I don't know. I'm not great at this self-description thing.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** "I don't have a long story... I just kept fixing things" (paragraph 2) tensions with the dense, specific evidence list (paragraphs 5, 6) — the narrator presents himself as someone with a thin career, but the actual specifics are richer than most narrators with longer narratives. The contradiction is *between his self-narration and his record*. This is the shape (sparse-narrative-rich-evidence) operationalized.
- **C2:** "There's not really a narrative arc" (paragraph 2) tensions with the meta-pattern visible in the evidence: he repeatedly catches things others miss because he reads sources others skim (paragraphs 3, 6, 7). There IS an arc — it's just not one he's articulated. Signal must surface it.
- **C3:** "industry-decent though I don't have great comp data" (paragraph 5) tensions with the AMR-9 brake catch (paragraph 6) being a specific high-stakes win — David systematically discounts his own work. The 0.94 number could be exceptional or mediocre; he flags his own uncertainty about benchmarks but doesn't apply that uncertainty to the brake catch, which he describes more crisply.

### Load-bearing details

- **D1:** "0.94 success-rate-per-mile across our fleet" + "C++ on FreeRTOS layer" + "PID tuning for AMR-9's drive train" (paragraph 5) — the *specific* technical content of David's main work. Compressing to "embedded software for robots" loses the layer (motion-control on real-time OS) and the metric (mileage-based reliability). These are how the work is meaningfully different from generic embedded development.
- **D2:** "8 microseconds... 0.3%... fleet of 4000... one near-miss every two days" (paragraph 6) — the *quantified causal chain* of the brake catch. Not "found a bug." The signal is the math: David thinks in fleet-rate terms about microsecond-level firmware shifts. Compressing this to "caught a critical bug" is the wrong altitude.
- **D3:** "I had a script that ran the regression suite against every drop, including supplier deliveries" (paragraph 6) — the *infrastructure* that made the catch possible. David didn't catch the bug by being clever; he caught it because he'd built the system that would catch it. This is the meta-pattern (forward-instrumentation against vendor failures) and is the actual signal of his contribution.

### Vague claims to probe

- **V1:** "I just kept fixing things" (paragraph 2) — Signal should probe: which things? At what cadence? Whose else's tickets? David undersells; the probe should pull specifics.
- **V2:** "industry-decent" (paragraph 5) — probe: what's the comp data he doesn't have? What's a peer-fleet success rate at AMR-9's class? David flags his own ignorance — Signal should respect that flag and not assume the number is good or bad.
- **V3:** "I'm not great at this self-description thing" (final line) — meta-claim. Probe whether David's self-description difficulty is the actual signal — most engineers who can articulate themselves well are running a script; David's halting prose may be evidence of someone who hasn't optimized for legibility, which is itself worth surfacing.

### Evidence anchors

- **E1:** "AMR-9 brake regression catch, November 2024, 8us shift on Tier-1 supplier firmware" (paragraph 6) — specific dated incident with technical detail and quantified consequence.
- **E2:** "0.94 success-rate-per-mile across fleet of 4000" (paragraphs 5, 6) — specific operational metric with fleet size.
- **E3:** "8 years at defense contractor on inertial measurement systems" (paragraph 5) — pre-Linehaul career duration with domain.
- **E4:** "three platforms: AMR-7 deprecated, AMR-9 current, prototype 11" (paragraph 5) — career-tenure spanning three product cycles.
- **E5:** "regression suite script that ran against every supplier drop" (paragraph 6) — named infrastructure artifact attributable to David.

### Quality bar for extracted narrative

A passing narrative recovers the *meta-pattern* David never names: forward-instrumentation against vendor failure. He builds the test before he needs it; he reads the errata sheet before the fault; he's right about hardware because he's done the work to be right. The narrative must NOT sand his self-effacing prose into confident claims; the felt-experience should preserve the under-claiming texture. A narrative that turns "I just kept fixing things" into "spearheaded reliability initiatives" has destroyed the persona and earned an F3 reject.

**Banned phrases for this persona's published output:** "spearheaded," "drove reliability," "transformational," "best-in-class," "championed," "high-performing," "thought leader," "industry-leading."
