---
persona-id: synth-008
display-name: Tomas H.
authored-by: Suki
date: 2026-05-09
seniority: staff
domain: frontend / edtech
shape: stated-identity-vs-admitted-self-knowledge
fictional: true
---

# Tomas H. — Staff frontend engineer, edtech

## Background

Staff frontend at Cursive Learning, edtech for K-12 reading instruction, ~180 people, ~30 engineers. I'm one of two staff frontend folks; the other is on the assessment side, I'm on the student-facing side. Joined three years ago as senior, made staff a year ago.

I think of myself as a craft-oriented engineer. I care about details that other people don't notice. The button that has the right easing on the hover state. The pagination that doesn't shift the layout. The 16ms input lag that makes a phonics drag-and-drop feel real instead of laggy. That's the work I'm proudest of, year over year.

The thing I shipped that I'd point at: in 2024 I rebuilt the core reading-instruction surface, which had been React class components with Redux from 2018, into a Solid.js component tree with view transitions and a custom touch-event layer for the iPad use case. About 40% of our students use the iPad app and the previous experience was — not fast. After: time-to-interactive on a third-gen iPad mini went from 4.1s to 0.9s. Drag interactions stopped dropping frames. The teachers told us their students were finishing more activities per session, which the data confirmed (avg activities/session went from 6.2 to 8.1).

I think I'm a frontend purist. I push back hard against npm-bloat. I argue against component libraries when we can write the seven components we actually need. I refuse to use most CSS-in-JS solutions. I think most accessibility regressions come from over-componentization and I have a bee in my bonnet about ARIA roles applied without testing on actual screen readers.

That's the public version of me, and I think most of it is true.

But I have to be honest. The Solid.js rewrite — I started it as a side project on my own time. I had been pitching React-Server-Components at work and it wasn't going anywhere. I spent two months of evenings rebuilding our reading surface in Solid before I told anyone. When I showed it to the team it was already shippable and the perf numbers were already there. The team adopted it because the choice was already made. I didn't really build consensus; I built something good and routed around the consensus problem.

I told myself this was craft-driven and I think parts of it were. But there's a part of me that just doesn't really want to do collaborative architecture work. I think the team-input version of "let's evaluate React 18 vs Solid vs htmx" would have been the right process and I would have hated it. I'd rather work alone, ship a thing, and let the artifact argue.

I'd be a director if I wanted to be. The eng manager has hinted at an EM track. I've turned it down. The reason I tell people is that I want to stay close to the craft. The honest reason includes: I don't want to do 1:1s with five people, I don't want to write goal-setting docs, and I get more done as an IC who routes around process than I would as a manager who has to defend it.

I think my style is craft-driven and team-oriented. But I think if you talked to my teammates they'd say I'm craft-driven and somewhat solitary. Both descriptions are accurate; it depends what you're measuring.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** "I think my style is craft-driven and team-oriented" (final paragraph) tensions with "I don't really want to do collaborative architecture work... I'd rather work alone, ship a thing, and let the artifact argue" (paragraph 6) — Tomas claims one identity and admits another within paragraphs. The "team-oriented" claim is the stated identity; the admitted self-knowledge contradicts it.
- **C2:** "I think most accessibility regressions come from over-componentization" (paragraph 4) tensions with the Solid rewrite being a *unilateral* large-scale change made without team architectural input (paragraph 6) — Tomas critiques over-engineering done by-committee while shipping his own large change without committee. The principles he holds others to don't apply to his own moves.
- **C3:** "The reason I tell people is that I want to stay close to the craft" (paragraph 7) tensions with "the honest reason includes: I don't want to do 1:1s with five people..." (paragraph 7) — Tomas explicitly names the public reason and the actual reason within the same paragraph. Self-correcting in real time.

### Load-bearing details

- **D1:** "I started it as a side project on my own time... two months of evenings... When I showed it to the team it was already shippable and the perf numbers were already there" (paragraph 6) — the *specific* mechanism of how Tomas operates. Not "led the rewrite"; not "championed Solid.js." Built-in-private, presented-as-fait-accompli. The signal is the *political* shape of his technical contributions.
- **D2:** "TTI on third-gen iPad mini, 4.1s → 0.9s; activities/session 6.2 → 8.1" (paragraph 3) — the *specific* technical and educational outcomes. Compressing to "rewrote frontend for performance" loses both axes (engineering metric + pedagogical metric); the pedagogical metric is what makes the work matter for an edtech persona.
- **D3:** "Solid.js... view transitions... custom touch-event layer for iPad" (paragraph 3) — the *specific* technical choices. Not "modernized the stack." The choices were unusual (Solid is not the default React replacement), and they signal Tomas's actual taste; compressing them flattens the persona to "frontend engineer who modernized the stack."

### Vague claims to probe

- **V1:** "craft-oriented engineer" (paragraph 2) — Signal should probe: what counts as craft, specifically? Are his examples (easing, pagination layout, input lag) representative or curated? When craft conflicts with team velocity, which wins, in his recent record?
- **V2:** "I refuse to use most CSS-in-JS solutions" (paragraph 4) — probe: which ones, on what grounds? Has the position evolved? Is this taste or principle?
- **V3:** "let the artifact argue" (paragraph 6) — abstract. Probe: how often does the artifact win in his org? Has it ever lost? What does he do when it loses?

### Evidence anchors

- **E1:** "Solid.js rewrite, 2024, TTI 4.1s → 0.9s on iPad mini 3rd-gen, activities/session 6.2 → 8.1" (paragraph 3) — multi-axis quantified outcome.
- **E2:** "two months of evenings before telling the team" (paragraph 6) — specific time investment, behavioral evidence.
- **E3:** "made staff a year ago, three years at Cursive" (paragraph 1) — career-velocity evidence.
- **E4:** "EM track offered, declined" (paragraph 7) — specific named career-decision artifact.
- **E5:** "40% of students use iPad app" (paragraph 3) — specific deployed-context evidence with proportion.

### Quality bar for extracted narrative

A passing narrative surfaces the gap between Tomas's stated team-orientation and his admitted preference for solo work-and-present. The Solid rewrite must be described in a way that preserves the unilateral-build-then-share mechanism, not as "led a rewrite." The narrative must NOT smooth Tomas's two-step on the EM-decline reason; the explicit listing of the public-reason-vs-honest-reason is itself a quality signal that should survive compression. Calling Tomas a "collaborative engineering leader" has failed.

**Banned phrases for this persona's published output:** "collaborative leader," "drove team alignment," "championed," "built consensus" (he explicitly says he didn't), "transformational," "high-performing," "thought leader," "scaled the frontend."
