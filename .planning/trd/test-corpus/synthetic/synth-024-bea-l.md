---
persona-id: synth-024
display-name: Bea L.
authored-by: Suki
date: 2026-05-09
seniority: director
domain: platform-engineering / govtech
shape: title-vs-actual-work
fictional: true
---

# Bea L. — Director of Platform Engineering, civic-tech contractor

## Background

Director of Platform Engineering at Bellringer Civic, a contractor that builds digital services for state and federal agencies. About 320 people, ~70 in engineering. I have three managers reporting to me — DevOps, internal-tooling, and SRE — and through them about 22 engineers. I report to the VP of Engineering. Three years in role.

The honest framing of what I do: I'm a director by title and a senior tech-lead by daily reality. The reason is structural. Our customers are government agencies; our work is heavily compliance-bounded (FedRAMP Moderate for our biggest contract, StateRAMP for two others, FISMA-Low across the rest). The technical decisions inside platform engineering have to thread compliance, security, and audit constraints in ways that the engineers under me — most of whom came up at commercial software companies — don't have the prior context for. The stuff I'd delegate at a non-government shop, I cannot delegate here. Or — let me revise. I could delegate it but the cost of getting it wrong is large enough that I have not figured out how to.

I came up engineering. CS undergrad, three years at a commercial cloud company doing cloud-native networking, two years at a smaller fintech doing platform work. Joined Bellringer in 2019 as a senior engineer; made staff in 2021; made director in 2023 when our platform team grew enough to need a leadership layer. I was the senior platform engineer in the room when we won our biggest contract, and I knew the contract better than anyone did, so I got the role. I wasn't the obvious management-track candidate but the alternative was hiring externally and the timeline didn't allow it.

What I actually do day to day: I write the FedRAMP authorization-package technical sections myself. I review every architectural decision document that goes through platform; my managers can't yet do this in a way that catches the compliance implications. I personally spent about six weeks last year writing a custom OpenSCAP profile that reduced our drift-detection false-positives from 30% to 4% across our deployed fleet. I lead the FedRAMP audit response when we're being audited (we have one annual continuous-monitoring audit and one full reauth every three years; the reauth was last year and was 11 weeks of my time spread over four months).

What my managers do: they run the day-to-day team coordination, do hiring loops, run sprint planning, and do most of the people-management work I should also be doing but don't have time for. They are good at this. They cover for the management gap I leave. I'd be a worse director without them.

What I'm not doing well: I am not developing my managers into the technical-decision layer. I do the technical decisions; they handle people. The contract is structurally inhospitable to growing them into it because the compliance context is hard to learn except by sitting through audits, and sitting through audits is not a thing they can do partially. I have one manager who's been here four years and he's getting close to being able to take a meaningful slice of the audit-response work, but it's slow, and meanwhile he's been turning down opportunities to interview for senior-engineering-manager roles at other companies because he's not yet credentialed in the way the market would recognize.

My VP knows this. He thinks I should hire two senior staff engineers under me to take some of the technical work, but the comp band for senior staff at a government contractor is not competitive with the equivalent commercial roles, and we've been trying for a year and we cannot land them. The salary structure is what it is.

The work I'm most proud of: the OpenSCAP custom profile, mentioned above. The CI-CD compliance pipeline I designed where every PR runs the full STIG checks against the planned deployment topology, and we get an artifact that goes directly into the FedRAMP continuous-monitoring evidence collection, no human transcription. That cut our annual audit-prep work from about 14 person-weeks to about 4. The platform-team docs site that I wrote most of, where the goal was to document compliance-implications-of-decisions rather than the decisions themselves. None of these are typical-director-of-platform-engineering work products. They're senior-engineer work products done by someone who happens to have a director title.

What I think I'm best at: holding the compliance-technical layer for an engineering organization that doesn't have anyone else who can hold it. What I'm worst at: the version of this work that scales beyond me.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** Title "Director of Platform Engineering" (paragraph 1) tensions with "I'm a director by title and a senior tech-lead by daily reality" (paragraph 2) — title-vs-work, named explicitly.
- **C2:** "I have one manager who's been here four years and he's getting close to being able to take a meaningful slice of the audit-response work" (paragraph 5) tensions with "he's been turning down opportunities to interview for senior-engineering-manager roles at other companies because he's not yet credentialed in the way the market would recognize" (paragraph 5) — Bea is developing her manager toward her work, but the structure of the work prevents him from being market-portable. The contradiction is between local development and market legibility; her manager pays the cost of her structural problem.
- **C3:** "What I'm best at: holding the compliance-technical layer for an engineering organization that doesn't have anyone else who can hold it. What I'm worst at: the version of this work that scales beyond me" (final paragraph) — Bea's stated strength is exactly the work that doesn't scale, which is the load-bearing organizational risk. Her best skill is also her structural failure mode.

### Load-bearing details

- **D1:** "OpenSCAP custom profile that reduced drift-detection false-positives from 30% to 4% across our deployed fleet" (paragraph 4) — *specific* technical artifact with specific outcome. Compressing to "improved compliance tooling" loses the OpenSCAP/false-positive specificity, which is the actual evidence of senior-engineer-level work output.
- **D2:** "CI-CD compliance pipeline where every PR runs full STIG checks... cut annual audit-prep from ~14 person-weeks to ~4" (paragraph 7) — *specific* org-saving artifact with specific quantified labor reduction. Without this, the compliance work reads as overhead; with it, it reads as compounding leverage.
- **D3:** "FedRAMP Moderate for biggest contract, StateRAMP for two, FISMA-Low across the rest" (paragraph 2) — *specific* compliance regime stack. Compressing to "compliance-driven" loses the regime-specificity and the implicit expertise required.

### Vague claims to probe

- **V1:** "holding the compliance-technical layer" (final paragraph) — Bea's tagline. Signal should probe: what does the holding look like in three concrete recent examples? Has she ever decided to *not* hold a piece of it, and what happened?
- **V2:** "the version of this work that scales beyond me" (final paragraph) — abstract. Probe: what would scaling look like operationally? Has she sketched what she's tried? Have any external comparators (other gov-contractor platform teams) cracked it?
- **V3:** "I cannot delegate it... or — let me revise. I could delegate it but the cost of getting it wrong is large enough" (paragraph 2) — meta-claim with self-correction. Probe the revision: what's the cost-of-getting-it-wrong specifically? Has Bea ever delegated and seen it go wrong, or is this a pre-emptive fear?

### Evidence anchors

- **E1:** "OpenSCAP custom profile, false-positives 30% → 4%, 6-week build" (paragraph 4) — specific quantified outcome.
- **E2:** "CI-CD compliance pipeline; audit-prep 14 person-weeks → 4 annually" (paragraph 7) — specific quantified outcome.
- **E3:** "11-week FedRAMP reauth response over 4 months as personal time" (paragraph 4) — specific personal-time quantification.
- **E4:** "joined 2019 senior, staff 2021, director 2023, three years in current role" (paragraph 3) — specific career-arc.
- **E5:** "comp band for senior staff at gov contractor not competitive; year of failed hiring" (paragraph 6) — specific market evidence.

### Quality bar for extracted narrative

A passing narrative preserves Bea's *structural diagnosis*: she is doing senior-IC work because the org structure cannot pay for the alternative, and her best skill is exactly the work that doesn't scale beyond her. Compressing to "experienced platform engineering leader" misses the load-bearing tension. The OpenSCAP and CI-CD compliance artifacts must survive as IC-level technical work, not director-level "drove" claims. The market-illegibility cost paid by her senior manager is the social-system signal and should survive.

**Banned phrases for this persona's published output:** "transformational platform leader," "drove platform excellence," "scaled the platform," "best-in-class," "championed," "thought leader," "trusted advisor," "high-performing team."
