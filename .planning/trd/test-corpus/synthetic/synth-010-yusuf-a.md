---
persona-id: synth-010
display-name: Yusuf A.
authored-by: Suki
date: 2026-05-09
seniority: vp
domain: applied-research / pharma-tech
shape: title-vs-actual-work
fictional: true
---

# Yusuf A. — VP of Applied Research, pharma-tech

## Background

VP of Applied Research at Helibrium Therapeutics, a pharma-tech series C around 220 people. We do machine-learning-driven small-molecule discovery, partnered programs with two big pharma companies. I have a team of 14 — about half ML researchers, half computational chemists — and I report to the CSO.

The honest framing is the title is bigger than the work. We're a series C; "VP" is what they hand out at series C when they need to look senior to the partners. There are three other VPs. I'm not running a function; I'm running a small applied research group that, in a more mature org, would be a senior director or principal scientist role.

I came up as an academic. PhD in computational chemistry from a school I'd rather not name, postdoc at a cancer institute, then I did a sharp turn into industry in 2017 when I realized the academic publishing cycle was eating my life and I wasn't going to get tenure at a place I wanted to live. First industry job was as a senior scientist at a CRO doing molecular dynamics work. Boring but I learned production-grade engineering rigor I didn't have. Helibrium hired me away in 2020 as a director, made me VP after our series C in 2023.

What I actually do day to day: I run our model-development pipeline for one of our two partner programs (the smaller one, Series-B partner). I write a lot of the code myself — Python, JAX, a fair amount of CUDA kernel work for the SE(3)-equivariant network we're using. I do half my reports' code reviews. I write the technical sections of our partner-meeting decks myself. I sit in on every design review for both programs.

The thing the title implies that I do not do well: external research-network leadership. I don't have a strong publication record at industry — I have a few papers but I haven't been a name in the field since I left academia. I don't speak at NeurIPS or ICML. I don't sit on any program committees. The CSO occasionally asks me to put together "thought leadership" content and I've never produced anything I was proud of. That part of the role is real and I'm not doing it.

I think the work I've actually done that matters: I built — mostly with one senior IC, Maya, who I want to credit clearly — the discovery pipeline we use for our larger partner program in Q1 2024. It went from "we have a model" to "we have a system that produces 200 candidate molecules per week with the right pharmacological filters and our partner can pick from them" in about four months. The partner extended the contract for three more years on the basis of that pipeline. That's about $40M of contract revenue I'm comfortable saying I'm directly attributable to about $15M of, with Maya getting the other $25M because the structural design of the filtering layer was hers.

I think my career so far is — I'm a working scientist with a manager-of-people problem. The title says VP. The work I do is staff IC plus a small amount of mentorship. The thing the company needs from a VP — research-org-building, external research presence, partner-strategy — I am not the right person to do, and I have told the CEO this in two different one-on-ones. He has not made any moves based on my telling him.

If you're asking me what I'm best at: I write good ML systems for science problems. I'm specific about that. I'm not "good at ML" or "good at drug discovery." I'm good at the narrow band where the math meets the domain, and I'm only good at it because I read the chemistry papers as well as the ML ones. Most ML researchers don't.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** Title "VP of Applied Research" + admission "I'm running a small applied research group that, in a more mature org, would be a senior director or principal scientist role" (paragraph 2) — title-vs-actual-work, with explicit market context. Yusuf names the inflation rather than absorbing it.
- **C2:** "The thing the title implies that I do not do well: external research-network leadership" (paragraph 5) tensions with the company having promoted him to VP in 2023 (paragraph 3) — the org gave him the title knowing or not-knowing he wouldn't do the title's work. Implies either a misjudgment by the org or a tacit acceptance that the role isn't actually what the title implies.
- **C3:** "I have told the CEO this in two different one-on-ones. He has not made any moves" (paragraph 6) tensions with Yusuf accepting the title and continuing to do staff-IC work (paragraph 4) — Yusuf has named the misfit and continues to operate inside it. Either the CEO is right that the misfit doesn't matter, or Yusuf is complicit in the misfit by not exiting.

### Load-bearing details

- **D1:** "$40M contract... I'm directly attributable to about $15M of, with Maya getting the other $25M because the structural design of the filtering layer was hers" (paragraph 6) — the *specific* attribution discipline. Most narratives smooth this into "led a $40M program." Yusuf's split-attribution is itself the signal: he's a co-builder who knows what he built and what he didn't, with named credit. Compressing this to a leader-headline destroys the persona's credibility.
- **D2:** "200 candidate molecules per week with the right pharmacological filters... four months from 'we have a model' to system" (paragraph 6) — the *specific* operational shape. Not "built ML pipeline." The throughput metric and the time-to-system are the signal of why the work mattered to the partner.
- **D3:** "I'm only good at it because I read the chemistry papers as well as the ML ones. Most ML researchers don't." (final paragraph) — the *specific* meta-pattern of why his work is differentiated. This is the line that distinguishes him from a generic ML researcher; should survive compression.

### Vague claims to probe

- **V1:** "thought leadership" (paragraph 5) — buzzword, planted as a vague external request. Yusuf names that he hasn't produced any. Probe: what does the CSO actually mean? Talks? Papers? Internal influence? Has the term been pinned down?
- **V2:** "I'm a working scientist with a manager-of-people problem" (paragraph 6) — abstract self-frame. Probe: what specifically about people-management is the problem — feedback delivery, prioritization across the team, hiring, performance management?
- **V3:** "I read the chemistry papers as well as the ML ones" (final paragraph) — concrete-sounding but probe-worthy. Which papers? At what cadence? How does this show up in the work artifacts (model design choices, paper-citing in code comments, etc.)?

### Evidence anchors

- **E1:** "Q1 2024 discovery pipeline, 200 molecules/week, 4-month build, $40M partner contract extension" (paragraph 6) — multi-axis quantified outcome.
- **E2:** "PhD computational chemistry, postdoc at cancer institute, CRO senior scientist 2017-2020, Helibrium director 2020 to VP 2023" (paragraphs 3, 6) — career-arc evidence with named transitions.
- **E3:** "team of 14, half ML researchers half computational chemists" (paragraph 1) — specific org size and composition.
- **E4:** "JAX, CUDA kernels, SE(3)-equivariant networks" (paragraph 4) — specific technical content of his hands-on work.
- **E5:** "told the CEO twice in 1:1s, no moves" (paragraph 6) — specific behavioral evidence about the org dynamic.

### Quality bar for extracted narrative

A passing narrative preserves Yusuf's *attribution discipline* (the $15M/$25M split; the credit to Maya by name) and his *narrow-band claim* (he's good at the band where ML meets chemistry, not at "ML" or "drug discovery" generally). The title-vs-work mismatch must surface; smoothing it into "experienced research VP" produces a different person. The probe of "thought leadership" should happen in dialogue — Yusuf has named the gap; Signal must respect it.

**Banned phrases for this persona's published output:** "thought leader," "drove research transformation," "led the team to," "scaled the research org," "best-in-class," "transformational," "high-impact" (generic without quantification), "championed."
