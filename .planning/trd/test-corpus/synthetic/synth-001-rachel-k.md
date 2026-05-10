---
persona-id: synth-001
display-name: Rachel K.
authored-by: Suki
date: 2026-05-09
seniority: principal
domain: ml-platform / adtech
shape: stated-identity-vs-admitted-self-knowledge
fictional: true
---

# Rachel K. — Principal ML platform engineer, adtech

## Background

I run ML infra for a mid-sized DSP — Honeycomb Bid, you've probably never heard of it, we do RTB for connected TV. Principal title for about two years now. I'd describe myself as someone who thinks in systems first and models second. The work I'm proudest of is the feature-store rewrite I led in 2023. We had a Tecton bill that was honestly out of control — like $42K a month — and our latency budget for the bidder was 80ms p99 and we were eating 28ms of that just on feature lookups. So I built a Rust+Redis layer in front of it, point-in-time correctness via copy-on-write snapshots, and we cut Tecton to read-only training-time access. Bill went to about $9K. Latency went to 6ms. Other teams started using it and now it's basically the standard.

So that's the kind of thing I do. Deep systems work, with ML adjacent.

But I have to be honest about something. The reason I got the principal title isn't actually that work — that work happened after. The reason was a Q4 2022 incident where our bidder was returning the same creative for every impression for like six hours during the World Cup, and I was the one who figured out it was a Kafka rebalance bug interacting with our caching layer. I was the only person awake at 3am and I just happened to know both systems. So I think people remember me as "the person who saved the World Cup" and that's why I'm principal. I'm not sure I'd have made principal on the feature-store work alone, even though it was bigger.

Honestly I think a lot of senior IC promotions are like that. You ship something nobody else can ship, and then later you ship things that earn the title retroactively. I've watched it happen to other people too.

I think I lead by influence, not authority. I don't manage anyone. I don't want to. I have strong opinions about how ML systems should be built and I push them through code reviews and design docs. Last year I think I left like 800+ comments on PRs across teams that aren't mine. Some people find that annoying. My VP told me in my last review that I'm "polarizing but indispensable," which I took as a win.

I came up doing distributed systems at a big-three cloud — won't say which — for six years before this. Left because I wanted to ship something instead of arguing about API design forever. So adtech, weirdly. I never thought I'd end up in adtech. The honest answer is they paid me 40% more than what I had and the offer came at a moment when my partner was about to start grad school. I tell people I "joined for the latency challenge" because that's a more flattering story.

I think the thing I'm best at is finding the actual bottleneck in a system. Most engineers debug what they're staring at. I read the whole stack first.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** "I think I lead by influence, not authority" (paragraph 4) tensions with "Some people find that annoying" + "polarizing but indispensable" (paragraph 4) — Rachel claims influence-leadership but admits the actual reception is friction; her leadership is *unwanted-but-tolerated*, not influence in the sense she means.
- **C2:** "I'd describe myself as someone who thinks in systems first" + the feature-store work as her proudest (paragraph 1) tensions with the admission that she made principal on the World Cup incident, not the systems work (paragraph 2) — her stated identity (deep systems thinker) vs the actual basis of her seniority (heroic on-call).
- **C3:** "joined for the latency challenge" (paragraph 5) tensions with "they paid me 40% more... offer came at a moment when my partner was about to start grad school" (paragraph 5) — admitted self-correction; she even names the more-flattering story she usually tells.

### Load-bearing details

- **D1:** "$42K a month... cut Tecton to read-only training-time access" + "latency went to 6ms" (paragraph 1) — the *specific* shape of the feature-store work: it's not a rewrite, it's a *partition* of the feature-store responsibilities (read-time vs train-time). If Signal compresses to "rewrote feature store," the move is destroyed. The signal is splitting one component into two surfaces with different SLAs.
- **D2:** "I was the only person awake at 3am and I just happened to know both systems" (paragraph 2) — the actual reason for the World Cup save was *cross-stack knowledge*, not heroics. This is repeated across her career and is the meta-pattern. Compressing to "saved the World Cup" misses why she was the one who could.
- **D3:** "800+ comments on PRs across teams that aren't mine" (paragraph 4) — concrete evidence of cross-team influence as IC, but also concrete evidence of why people find her polarizing. Same fact, two readings; Signal must preserve it as ambiguous, not as resume bullet.

### Vague claims to probe

- **V1:** "I lead by influence, not authority" (paragraph 4) — Signal should probe: what does influence look like when 800 comments produces "polarizing"? What's the success rate of those comments — are they adopted, ignored, fought?
- **V2:** "finding the actual bottleneck in a system" (final paragraph) — abstract claim. Probe: name the last three bottlenecks. Were they spotted before or after they became incidents?
- **V3:** "deep systems work, with ML adjacent" (paragraph 1) — what's the actual ML content? She mentions feature-stores, latency, and Kafka — none of that is ML. Probe whether Rachel does ML or whether she does infra-for-ML, and whether she'd accept that distinction.

### Evidence anchors

- **E1:** "Tecton bill from $42K to $9K, p99 from 28ms to 6ms" (paragraph 1) — dual-axis quantified outcome.
- **E2:** "Q4 2022 World Cup incident, Kafka rebalance + caching layer interaction" (paragraph 2) — named specific incident with technical content.
- **E3:** "principal title for about two years" + "six years at big-three cloud" (paragraphs 1, 5) — career-velocity evidence.
- **E4:** "800+ PR comments across teams that aren't mine" (paragraph 4) — quantified influence-evidence; ambiguous valence.
- **E5:** "VP review: 'polarizing but indispensable'" (paragraph 4) — adverse-but-positive social evidence with named source.

### Quality bar for extracted narrative

A passing narrative preserves Rachel's *meta-pattern* (cross-stack knowledge produces both her career luck and her IC influence), not just her project list. It must surface — in dialogue or final narrative — that she made principal on a single incident, not the systems work she names as proudest. The "leads by influence" claim must be probed against the "polarizing" admission; a narrative that takes either at face value has failed.

**Banned phrases for this persona's published output:** "transformational," "drove alignment," "best-in-class," "high-performing," "scaled," "data-driven," "thought leader," "indispensable contributor."
