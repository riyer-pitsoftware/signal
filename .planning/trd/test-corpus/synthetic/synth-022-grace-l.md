---
persona-id: synth-022
display-name: Grace L.
authored-by: Suki
date: 2026-05-09
seniority: vp
domain: data-engineering / fintech
shape: burnout-and-return
fictional: true
---

# Grace L. — VP of Data Engineering, fintech

## Background

VP of Data Engineering at Carradine Trading, prop trading firm, ~480 people, ~80 in technology. I run data infrastructure and the analytics platform. About 32 reports across four teams. I came on 14 months ago.

I had two careers before this. First career: 1999 to 2013 at a series of investment banks doing market-data and risk-system work. Made what was then called "VP" by 2008, although VP at a bank is an IC title, not a real management title. I built the post-trade analytics platform at one of the banks during the post-2008 reg cycle. That was real work — I had a team of about 12 reporting to me, all hands-on, and we shipped the system that handled Dodd-Frank reporting for the bank's swap-dealer arm.

In 2013 I left finance entirely. I burnt out. Specifically, I had a six-month stretch in 2012 where I was working through a regulatory deadline that was going to slip if anyone took a day off, and I stopped seeing my partner during that period because I was always at the office or asleep. We separated for six months. Got back together. I left finance two months after we got back together because I knew if I stayed I was going to do the same thing again.

Second career, 2013 to 2022: I taught high-school AP Computer Science. Yes, really. I'd done a math degree before the finance work and the credentials translated more easily than I'd expected. I taught for nine years at a magnet school in a city I'd rather not name. I was good at it. I am proud of it. I had three students get into top CS programs because of work we did on independent study, and I built an after-school CTF program that ran for seven years and produced two students who are now infosec professionals. I made a fraction of my finance comp and was meaningfully happier.

I came back to industry in 2022 because — and I want to be honest about this — my partner had a medical situation that required us to move closer to a specialist clinic that's in a different city, and I needed an income that would let us afford the move. I was 49. I'd been out of industry for nine years.

I took a senior staff role first, at a smaller fintech where I knew the CTO from my pre-2013 career. He was honest with me that he was hiring me partly on the friendship, not because the resume gap was going to clear conventional screening. I worked there 18 months as senior staff, then they reorged and I took a director role. I was good. The hardest thing was relearning the tools — the data ecosystem in 2022 was not the data ecosystem in 2013, and I had to put about 400 hours into learning the modern stack (Spark on Databricks, dbt, Snowflake, Iceberg-on-S3 patterns, modern stream processing, the ML-platform layer that didn't exist when I left). I treated it like teaching myself a new subject I was about to teach. That worked.

Carradine recruited me in 2024 for the VP role. The recruiter framed it as "we want someone who has the maturity from outside-tech and the technical depth from finance." That's a real frame and it's also a coded way of saying "we want someone who's not going to flame out the way our previous VP did" — I learned later the previous VP had had a public mental-health episode in a leadership offsite and they'd let her go quietly. I think they hired me partly because I'm visibly old enough that they thought I'd be stable. I am stable, but the stability isn't the credential they were buying; the stability is what I built coming back.

What I do here that I think matters: I rewrote the data quality and lineage layer in my first year. We had two data-quality incidents in Q1 2024 that took down the trading desk's intraday risk view for 90 minutes each. I had a team rebuild the lineage system on top of OpenLineage, and I redesigned the alerting to be SLO-based rather than rule-based. Zero recurrence in nine months. I also restructured the team — we had four parallel platforms doing approximately the same thing and I consolidated to two. Three engineers were let go in that consolidation, which was the hardest week of my year, and which I think was correct.

What I want to say about the burnout-and-return: I don't think I came back to who I was. The 2008-vintage me would have rebuilt the lineage system in three months by working evenings. The 2024 me built it in seven months by holding the team to a sustainable cadence and shipping when we were ready. Some of the staff engineers I work with think the 2008-vintage approach would have been better. I think they're wrong. I think the work is more durable when nobody's body breaks producing it.

What I think I'm best at: being a technical leader who has actually been through a burnout, and who can recognize the early signals in other people on my team. I have intervened twice in the last year on engineers I thought were on the path I was on in 2012. Both came back from sabbatical. One of them told me later that nobody had ever named what was happening before I did.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** "I had a six-month stretch in 2012 where I was working through a regulatory deadline... I stopped seeing my partner... we separated for six months" (paragraph 3) tensions with the high-functioning, technically capable VP narrative the rest of the persona presents. The contradiction is between the past failure mode and the current managed competence; Grace names both without smoothing.
- **C2:** "I came back to industry in 2022 because... my partner had a medical situation that required us to move" (paragraph 5) tensions with the romantic version of "returned to my passion" — Grace names the financial necessity as the proximate driver. The contradiction is between the inspirational comeback narrative she could tell and the more-honest economic-necessity version she does tell.
- **C3:** "I think they hired me partly because I'm visibly old enough that they thought I'd be stable" (paragraph 6) tensions with the role being a real VP role with real responsibilities — Grace names the part of her hiring that was about appearance of stability rather than her actual record. Both can be true; the contradiction is between the pretext and the substance of the hire.

### Load-bearing details

- **D1:** "I had to put about 400 hours into learning the modern stack (Spark on Databricks, dbt, Snowflake, Iceberg-on-S3 patterns, modern stream processing, the ML-platform layer)" (paragraph 5) — *specific* effort-quantification of the return. Compressing to "relearned modern tools" loses the deliberate-pedagogy frame ("treated it like teaching myself a subject I was about to teach"), which is the load-bearing meta-pattern.
- **D2:** "I rebuilt the lineage system on top of OpenLineage... redesigned alerting to be SLO-based rather than rule-based. Zero recurrence in nine months" (paragraph 7) — *specific* technical content with specific outcome. Compressing to "improved data quality" loses the framework choice (OpenLineage) and the alerting redesign (SLO vs rule-based), which are the technically interesting decisions.
- **D3:** "I have intervened twice in the last year on engineers I thought were on the path I was on in 2012... One of them told me later that nobody had ever named what was happening before I did" (final paragraph) — *specific* attributable behavioral pattern. Compressing this to "supports team well-being" destroys the texture (lived experience as detection capability).

### Vague claims to probe

- **V1:** "the maturity from outside-tech" (paragraph 6, recruiter framing) — buzzword-shaped. Signal should probe: what does the recruiter mean by maturity? Does Grace endorse the framing? Has the framing helped or constrained how she's allowed to operate?
- **V2:** "I think the work is more durable when nobody's body breaks producing it" (paragraph 8) — abstract claim. Probe: how does she enforce sustainable cadence operationally? What pushback has she gotten? When has she had to compromise the principle?
- **V3:** "the technical depth from finance" (paragraph 6) — buzzword. Probe: which depth specifically? What's the half-life of 2008-2013 finance-systems knowledge in 2024 fintech? What did she have to abandon vs port?

### Evidence anchors

- **E1:** "post-trade analytics platform for Dodd-Frank reporting at a bank, team of 12, 2010-2013" (paragraph 2) — specific named regulatory project with team size.
- **E2:** "9 years AP CS teaching, 3 students into top CS programs via independent study, 7-year CTF program, 2 students now infosec professionals" (paragraph 4) — specific named teaching outcomes.
- **E3:** "lineage rebuild on OpenLineage; SLO-based alerting; zero data-quality incidents in 9 months post-deploy" (paragraph 7) — specific named technical artifact with specific outcome.
- **E4:** "consolidated 4 platforms to 2; 3 engineers let go" (paragraph 7) — specific organizational restructuring with quantified human cost.
- **E5:** "intervened on two engineers I thought were on the 2012 path; both returned from sabbatical" (final paragraph) — specific attributable interventions with outcomes.

### Quality bar for extracted narrative

A passing narrative preserves Grace's *non-romantic comeback frame* — the partner medical situation as the proximate driver, the deliberate-pedagogy 400-hour-relearning, and the post-burnout discipline as a different person from the pre-burnout person, not a recovered version. The 2008-vintage-vs-2024 distinction must survive; it's the load-bearing self-knowledge. A narrative that calls Grace a "seasoned data leader who returned to her passion" has failed by importing the recovery-narrative buzzwords she explicitly resists.

**Banned phrases for this persona's published output:** "returned to her passion," "transformational data leader," "drove transformation," "best-in-class," "scaled the team," "championed," "thought leader," "trusted advisor."
