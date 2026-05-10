---
persona-id: synth-021
display-name: Mira S.
authored-by: Suki
date: 2026-05-09
seniority: director
domain: dev-relations / api-platform
shape: domain-pivoter
fictional: true
---

# Mira S. — Director of Developer Relations, API platform

## Background

Director of DevRel at Sundial APIs, mid-market API gateway and management platform, ~250 people. I have seven reports — three developer advocates, two technical writers, two community engineers. I report to the CMO. I've been in this role two years.

The pivot story: I started as a backend engineer. Six years writing APIs at a large media company in the late-2010s, then a startup that went under, then I led a small platform team at a fintech for a year. I left the fintech in 2021 because I'd been in management for nine months and discovered I was very bad at it — specifically, I was bad at sustaining motivation through quarter-on-quarter operational work that wasn't technically interesting. I was either deeply engaged or invisible to my team and the variance was hurting everyone.

I took eight months off, which is also the cover story for "I had no plan and the SaaS market in 2021 made it possible to wait for a role I actually wanted." During those eight months I started writing a newsletter about API design (boring topic, surprisingly engaged readership, peaked at maybe 4,000 subscribers), and I gave two conference talks that landed well. A founder I'd known peripherally reached out about Sundial. The role was unusual: it was DevRel-flavored but reporting up the marketing tree, and the brief was "make our developer experience the reason people pick us over the bigger players." I joined as a senior DevRel hire, made director within ten months when they expanded the team.

What I do that I think genuinely transferred from engineering: I read every PR our SDK team merges. I write a fair amount of the SDK example code myself, especially in languages where my advocates are weaker (Rust, Go from-zero, occasional Java). I do code review on our reference implementations the way a senior engineer would, not the way a marketing leader would. The SDK team is technically not my team — they're under the VP of Engineering — but in practice we operate as a paired unit and have for 18 months.

What I had to learn that didn't transfer: I am still genuinely bad at the marketing-org operations layer. I miss budget reconciliation deadlines. I forget which content sequence is supposed to drop in coordination with the product launch. I have a marketing ops manager on my team specifically because the CMO recognized I needed one and I am very honest that I'd be ineffective without her. Her name is Renée, she has saved me four times this year, and I include this because part of being honest about a pivot is being honest about what I cannot do without help.

The work I'm proudest of: our SDKs in 2024 went from a Stack Overflow tag-watch report of (paraphrasing): "documentation is okay but the SDKs are uniformly buggy across languages" to "the SDKs are the reason teams pick Sundial over [larger competitor]." That's a real customer-research finding. We did this by not adding features and by aggressively rewriting the seven languages we supported into a consistent shape using a code-generation pipeline I'd argued for in my second month and that took fourteen months to fully ship. Our developer NPS moved from 32 to 64. Our tracked organic mentions in HN/Twitter/Bluesky moved from negative-skewed to positive-skewed.

The other thing — and this is where I'm somewhere between proud and aware-it-could-be-overclaimed — I think I shifted Sundial's product strategy on enterprise plans last year. Engineering had been building toward feature parity with the enterprise tier of our biggest competitor. I argued, with three months of customer-call notes from my team, that our enterprise customers wanted *operational* parity (incident response, SLA cadence, dedicated support) and didn't care about the feature-list parity. The CEO came around. We re-scoped Q3 and Q4 of 2024. Renewal rate among enterprise accounts moved from 87% to 96%. I'm somewhere-between-proud-and-not because the head of product had been thinking similar things in parallel and I don't want to take all the credit. I think I provided the customer-evidence layer that let her argument win.

What I think I'm best at: being a senior engineer who chose to be in a non-engineering function, which lets me see things on the developer side that pure marketing folks miss and on the customer side that pure engineering folks miss. What I'm worst at: doing the things a marketing director is supposed to do that aren't engineering-adjacent.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** "I left the fintech in 2021 because I'd been in management for nine months and discovered I was very bad at it" (paragraph 2) tensions with "Director of DevRel" current title and successful 2-year tenure (paragraph 1) — Mira had a self-described management failure, then accepted another management role and is succeeding. The contradiction is about what kind of manager she is now and whether she fixed the problem or moved into a different management surface.
- **C2:** "I am still genuinely bad at the marketing-org operations layer" (paragraph 4) tensions with the work she points at as proudest (paragraph 5, $32 → $64 NPS, SDK rewrite, etc.) — large-scale operational successes coexist with admitted operational weaknesses. Not actually a contradiction; the resolution is that she has Renée. The contradiction is in whether "I have a co-pilot who handles half the job" is success or workaround.
- **C3:** "I think I shifted Sundial's product strategy on enterprise plans last year" (paragraph 6) tensions with "I don't want to take all the credit. I think I provided the customer-evidence layer that let her argument win" (paragraph 6) — Mira makes a strong claim and immediately partially-disclaims it within the same paragraph. The disclaim is itself the signal of how she operates (evidence-anchored to other people's arguments).

### Load-bearing details

- **D1:** "code-generation pipeline I'd argued for in my second month and that took fourteen months to fully ship" (paragraph 5) — *specific* timeline and ownership claim. Compressing to "led SDK consolidation" loses that the move was argued-for-early and shipped-late, which is the political pattern (long-game advocacy with eventual delivery).
- **D2:** "Renée, marketing ops manager... has saved me four times this year, and I include this because part of being honest about a pivot is being honest about what I cannot do without help" (paragraph 4) — *specific* named co-worker with attributed credit. This is the load-bearing humility detail; compressing it destroys Mira's voice and her honest-about-pivot frame.
- **D3:** "I read every PR our SDK team merges. I write a fair amount of the SDK example code myself, especially in languages where my advocates are weaker (Rust, Go from-zero, occasional Java)" (paragraph 3) — *specific* engineering-fluency-in-DevRel-role pattern. Compressing to "stays technical" loses the named-language specificity, which makes the claim probe-able.

### Vague claims to probe

- **V1:** "make our developer experience the reason people pick us over the bigger players" (paragraph 2, recruiter-pitch language) — buzzword-shaped. Signal should probe: did she end up taking that brief literally, or what was the modified version that actually drove her work?
- **V2:** "I shifted Sundial's product strategy" (paragraph 6) — strong claim, partially disclaimed. Probe the disclaim: what's her actual estimate of the counterfactual ("would have happened without me, six months later" vs "would not have happened")?
- **V3:** "being a senior engineer who chose to be in a non-engineering function" (final paragraph) — abstract self-frame. Probe: what's the choosing pattern? Has she considered going back to engineering? What would trigger a return?

### Evidence anchors

- **E1:** "developer NPS 32 → 64, organic-mention sentiment shift, 14-month SDK rewrite via codegen pipeline" (paragraph 5) — multi-axis quantified outcome.
- **E2:** "newsletter ~4,000 subscribers, two conference talks during 2021 gap" (paragraph 2) — specific gap-period production with reach.
- **E3:** "enterprise renewal rate 87% → 96% post-strategy-shift" (paragraph 6) — specific business outcome, partially attributed.
- **E4:** "joined Sundial as senior DevRel, made director in 10 months" (paragraph 2) — specific career-velocity within current company.
- **E5:** "I read every PR the SDK team merges; I write SDK example code in Rust, Go, Java" (paragraph 3) — specific behavioral evidence of engineering-fluency-in-DevRel.

### Quality bar for extracted narrative

A passing narrative preserves Mira's *honest pivot framing*: she had a management failure, took an unstructured break, found a role that lets her use her engineering past in a non-engineering function, and is candid about what she cannot do without organizational scaffolding (Renée). Compressing to "transitioned from engineering to developer relations leadership" smooths the failure and the scaffolding both. The Renée credit must survive — it's the load-bearing humility detail. A narrative that calls Mira a "transformational DevRel leader" has failed.

**Banned phrases for this persona's published output:** "transformational DevRel leader," "drove developer experience," "thought leader," "best-in-class," "championed the developer community," "transitioned to a customer-facing role," "scaled DevRel operations," "evangelized."
