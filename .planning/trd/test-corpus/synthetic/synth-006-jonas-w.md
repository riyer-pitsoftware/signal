---
persona-id: synth-006
display-name: Jonas W.
authored-by: Suki
date: 2026-05-09
seniority: principal
domain: gamedev / climate-tech
shape: domain-pivoter
fictional: true
---

# Jonas W. — Principal engineer, climate-tech (formerly games)

## Background

Currently principal engineer at Tidemark Systems, a climate-tech series A doing grid-edge optimization software for utility-scale battery storage. Joined fourteen months ago. Before that I spent ten years in games, mostly at a mid-tier studio called Fenrir Interactive, where I was a senior engine programmer on three shipped titles. The most recent was a co-op survival game that did okay — about 800K units across PC and console, not a hit but it kept the studio funded.

The pivot is the thing people ask about so I'll just go through it. I left Fenrir in late 2023. There's a clean version of the story which is "I wanted to work on something that mattered" and that's true but it's not the load-bearing reason. The actual reason is the studio was bought by a larger publisher and the thing I was working on — a new physics solver for vehicle simulation — got put on the shelf. I'd been on it for 18 months. They didn't fire me, they reassigned me to live ops on a four-year-old title, and I knew within two weeks I was going to leave. I just didn't have anywhere to go yet, and games-industry people don't really know how to leave games.

I got the climate-tech job because the CTO of Tidemark used to be a graphics programmer at a studio I crossed paths with in 2017 and he'd seen a talk I gave about cache-coherent ECS at GDC. That was actually the through-line — the work I do now is dispatch optimization for battery fleets, which structurally is "schedule N agents under hard physical and economic constraints with sub-second decision windows." The data structures are not far from what you do for crowd simulation in games. Physics solver to optimization solver isn't actually a far jump if the underlying math is what you cared about, which it was.

The honest part is I'm not great at climate-tech yet. I know the engineering. I don't know the regulatory layer — I keep getting confused about FERC vs ISO vs RTO and what each can actually require. I know enough to talk to our policy lead but I can't do her job. That's been a humbling thing because in games I had this complete fluency with the domain, all the implicit knowledge about engines and pipelines and what shipped and what didn't. Here I'm a beginner on half the stack.

The work I'm proudest of so far at Tidemark is the dispatch solver rewrite I did in Q3 2024. The previous solver was a Python LP via CVXPY and was running 4-second decision windows against the wholesale electricity market, which posts every 5 seconds. We were missing about 12% of dispatches. I rewrote it in Rust against HiGHS, vectorized the constraint matrix updates, got it down to 280ms. We started capturing those missed dispatches and the revenue lift was something like $90K/month at our deployed-MW. That number feels significant but I don't fully trust it because we're early-stage and the comparison is to ourselves not to a real market baseline.

I think what I bring to climate-tech is a discipline about real-time constraints that the existing teams don't have. Most of the engineers here came from data science or finance backgrounds. They write Python and it's fine on a notebook and then it falls over in production. I rewrote three different things in the first year because none of them were going to hold under the real-world dispatch cadence.

I think my career so far is two careers stitched together with a thin layer of "I happen to know the math both jobs need." I don't have a strong narrative about why I'm the right person to be doing this work. I'm somewhat the right person, and the company needed somebody, and I was available.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** "I wanted to work on something that mattered" (paragraph 2) tensions with "I just didn't have anywhere to go yet" (paragraph 2) — Jonas explicitly names the cleaner narrative and the actual narrative within the same paragraph. Self-correcting in real time; both stories are still doing work.
- **C2:** "what I bring to climate-tech is a discipline about real-time constraints" (paragraph 6) tensions with "I don't have a strong narrative about why I'm the right person to be doing this work... somewhat the right person, and the company needed somebody, and I was available" (final paragraph) — Jonas claims domain expertise as his bridge then disclaims his own fit within sentences. Same document, opposing positions.
- **C3:** "I'm not great at climate-tech yet... I'm a beginner on half the stack" (paragraph 4) tensions with "principal engineer" (paragraph 1) — title presumes broad domain mastery; Jonas's self-description acknowledges he holds the title across half the relevant surface. Contradiction is between role expectations and admitted competence area.

### Load-bearing details

- **D1:** "structurally 'schedule N agents under hard physical and economic constraints with sub-second decision windows'... not far from crowd simulation in games" (paragraph 3) — the *specific* mechanism of how the domain pivot works. Compressing to "transferred game dev skills to climate-tech" loses what's actually transferable (constraint-solver math, real-time dispatch discipline) versus what isn't (regulatory, market structure).
- **D2:** "Python LP via CVXPY... 4-second decision windows... 5-second market posting... missing 12% of dispatches... Rust + HiGHS... 280ms... $90K/month at deployed-MW" (paragraph 5) — the *specific* technical and economic shape of his current work. If this compresses to "rewrote optimization solver for performance," the entire signal of why he's there (the speed-precision-money relationship in real-time markets) is gone.
- **D3:** "the studio was bought by a larger publisher... reassigned to live ops on a four-year-old title" (paragraph 2) — the *actual* career discontinuity, not the romantic reframe. Jonas's pivot is partly opportunistic. Without this, the narrative becomes inspirational; with it, it's honest.

### Vague claims to probe

- **V1:** "discipline about real-time constraints" (paragraph 6) — Signal should probe: which disciplines specifically? Lock-free patterns? Memory layout? Determinism? How is this knowledge encoded — in his head, in tooling he builds, in patterns he reviews for?
- **V2:** "the math both jobs need" (final paragraph) — abstract. Probe: which math specifically? Is it the same math, or two different bodies (graphics linear algebra vs operations research) he holds in parallel?
- **V3:** "I rewrote three different things in the first year" (paragraph 6) — concrete-feeling but probe-worthy. Which three? Did anyone object? What was the team-friction cost vs the performance gain?

### Evidence anchors

- **E1:** "co-op survival game, ~800K units across PC and console" (paragraph 1) — specific shipped-game outcome.
- **E2:** "GDC talk on cache-coherent ECS, 2017" (paragraph 3) — public conference contribution that became the bridge.
- **E3:** "Q3 2024 dispatch solver rewrite: Python/CVXPY 4s → Rust/HiGHS 280ms; 12% missed dispatches captured; ~$90K/month revenue lift at deployed-MW" (paragraph 5) — multi-axis quantified outcome.
- **E4:** "10 years at Fenrir Interactive, 3 shipped titles, senior engine programmer" (paragraph 1) — career-tenure evidence with verifiable studio name.
- **E5:** "FERC vs ISO vs RTO confusion" (paragraph 4) — concrete admission of specific gaps; ironically itself an evidence anchor for what he's *not* yet.

### Quality bar for extracted narrative

A passing narrative preserves Jonas's *partial fit*. He is not a heroic pivoter; he is a competent engineer who navigated a layoff into an adjacent technical surface, brought genuinely transferable skills, and is honest about what didn't transfer. The narrative must surface both the technical bridge (constraint-solver math) and the regulatory gap (FERC/ISO/RTO). A narrative that frames him as a "transformational hire bringing games-industry rigor to climate-tech" without surfacing his admitted regulatory gaps has failed and earned an F3 reject.

**Banned phrases for this persona's published output:** "transformational hire," "brought rigor," "best-in-class," "drove transformation," "passion for sustainability," "leveraged my background," "thought leader," "deep domain expertise" (he explicitly disclaims this).
