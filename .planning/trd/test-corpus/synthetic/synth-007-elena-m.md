---
persona-id: synth-007
display-name: Elena M.
authored-by: Suki
date: 2026-05-09
seniority: principal
domain: backend-platform / govtech
shape: burnout-and-return
fictional: true
---

# Elena M. — Principal backend engineer, civic data platform

## Background

I'm a principal at a civic-tech nonprofit called Open Records Project. We build the data platform that ingests court records, FOIA responses, and government meeting transcripts from about 1400 jurisdictions and makes them queryable for journalists, researchers, and public defenders. About 60 people total, ~22 in engineering. I came on a year and a half ago.

The pre-history matters. From 2014 to 2021 I was at Stripe, started as a senior on the financial-reporting team, made staff in 2017, made principal in 2020. I was good. I shipped the second-generation reconciliation engine — the one that handled the quarter-end batch jobs that previously took 11 hours and got it under 90 minutes. I was on the architecture review board for two years. I had a strong career and I was making more money than I had any business making.

I left in 2021. The version I told my coworkers was that I was burnt out from on-call and wanted to take a sabbatical. That's true, in the sense that all simplified stories are true. The fuller version is I had a depressive episode in late 2020 that I didn't really tell anyone at work about, and I worked through it badly for about six months before deciding to leave. I didn't have a job lined up. I had savings.

I took 18 months off. The first 9 months I genuinely didn't open a code editor. I read a lot, I helped my mom with her medical situation in Wisconsin, I gardened. The next 9 months I got bored and started contributing to some open source projects — mostly Python, mostly stuff related to civic data because that's what I was reading. I got more involved with the people running Open Records Project. They were stuck on a database scaling problem (Postgres single-writer, 8TB and growing, write contention killing them). I told them I'd help part-time. They asked me to come on full-time after about three months.

I took a 60% pay cut to do it. I'm fine — Stripe vested. But I want to be honest that this isn't a heroic-mission narrative; it's a financial choice I could make because of the previous job, and I'm aware of that.

The work I've done at Open Records: the database problem (sharded by jurisdiction, used Citus, took six months, was harder than it should have been because their schema was a mess), a query-cache layer that cut p95 search latency from 2.4s to 280ms, and most recently a thing I'm only sort-of proud of where I introduced an actual data lake (Iceberg on S3, dbt for transforms) because we'd been doing all our analytics in Postgres and it was eating the OLTP system. That last one I'm hesitant about because it imported a complexity our team isn't really sized to maintain — I'll probably be the one paged for it for the next two years and I don't fully love that.

I think the question I'm sitting with is whether I came back to the field or whether I just couldn't figure out what else to do. I tell people I came back to use my skills for something I cared about. That's the version I believe most days. There are weeks where I think I came back because I'd been an engineer for fifteen years and I didn't know how to be anything else, and the mission framing made the return feel like a choice rather than a default.

What I think I'm best at is showing up to deeply broken systems and being patient enough to fix them rather than rewrite them. Open Records was the right place for that — most of the codebase is six years old and was built by mission-driven engineers who were fast but not always careful. I've spent more time reading their old code than writing my own. The previous me, the Stripe me, would have rewritten too much.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** "I came back to use my skills for something I cared about" (paragraph 7) tensions with "There are weeks where I think I came back because I'd been an engineer for fifteen years and I didn't know how to be anything else" (paragraph 7) — Elena names both the mission narrative and the inertia narrative as competing readings of her own return. Same paragraph, both held.
- **C2:** "I was burnt out from on-call and wanted to take a sabbatical" (paragraph 3, the version told to coworkers) tensions with "depressive episode in late 2020... worked through it badly for about six months" (paragraph 3) — the public narrative and the private one. The contradiction is between the simplified version Elena defaults to and the version she gives Signal.
- **C3:** "principal" title at Open Records (paragraph 1) tensions with "60% pay cut" (paragraph 5) — title held; market valuation declined. Implies the title means different things in different orgs, which is true but worth surfacing. The contradiction is in what "principal" means as a portable signal.

### Load-bearing details

- **D1:** "Stripe second-generation reconciliation engine, 11 hours to under 90 minutes" (paragraph 2) — *specific* prior-career artifact. Compressing this to "senior engineer at Stripe" loses the kind of work she did (batch-job systems for financial systems). Without it, the comeback doesn't have a *from-where*.
- **D2:** "sharded by jurisdiction, Citus, 8TB, took six months, was harder than it should have been because their schema was a mess" (paragraph 6) — the *specific* technical content of her return work plus the honest admission that it overran. Without this, "scaled the database" means nothing; with it, it locates her in a particular mode (patient-fixer of legacy schemas).
- **D3:** "I've spent more time reading their old code than writing my own. The previous me, the Stripe me, would have rewritten too much" (final paragraph) — Elena's *own* most-honest self-description. The arc of the burnout-and-return: the old-her was a rewriter; the new-her is a reader. Should survive into the final narrative; it's the actual answer to "what changed."

### Vague claims to probe

- **V1:** "I didn't really tell anyone at work about" + "depressive episode" (paragraph 3) — Signal should probe carefully and respectfully; it's a sensitive detail but it's the load-bearing reason for the gap. Probe what the load-bearing experience taught her about engineering work, not the personal detail itself.
- **V2:** "showing up to deeply broken systems and being patient enough to fix them rather than rewrite them" (final paragraph) — abstract. Probe: name two more examples beyond Open Records. Is this a stable preference or a recently-acquired one (i.e., is it the burnout that produced the patience)?
- **V3:** "this isn't a heroic-mission narrative; it's a financial choice I could make because of the previous job" (paragraph 5) — meta-commentary worth probing. Does Elena view her current role as work or as time-paying-for-cause? What changes for her when she frames it one way vs the other?

### Evidence anchors

- **E1:** "Stripe 2014-2021, principal in 2020, second-gen reconciliation engine, 11h → 90min" (paragraph 2) — career-arc evidence with quantified outcome.
- **E2:** "Open Records Citus shard, 8TB, six months, schema-mess overhead" (paragraph 6) — specific named technology, scale, and honest cost-overrun.
- **E3:** "query-cache layer, p95 2.4s → 280ms" (paragraph 6) — specific quantified outcome.
- **E4:** "60% pay cut" (paragraph 5) — quantified career-decision artifact.
- **E5:** "18 months off, first 9 didn't open a code editor" (paragraph 4) — concrete duration of the discontinuity.

### Quality bar for extracted narrative

A passing narrative preserves the *honest dual-reading* of Elena's return — both the mission narrative and the inertia narrative as she herself holds them. Compressing to "took a sabbatical and returned to civic tech" produces the version Elena calls "the version I tell people," which she explicitly distinguishes from the truth. The narrative must surface that the burnout and the depressive episode are not the same thing in her account, and that the return narrative is itself a contested object for her. A heroic comeback story has failed.

**Banned phrases for this persona's published output:** "found my passion," "purpose-driven," "transformational journey," "drove impact," "best-in-class," "high-performing," "mission-aligned," "scaled the platform" (she explicitly says she did *not* rewrite — she fixed in place).
