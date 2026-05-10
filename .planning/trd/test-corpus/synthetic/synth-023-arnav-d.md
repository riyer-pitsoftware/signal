---
persona-id: synth-023
display-name: Arnav D.
authored-by: Suki
date: 2026-05-09
seniority: principal
domain: ml-platform / mobile
shape: stated-identity-vs-admitted-self-knowledge
fictional: true
---

# Arnav D. — Principal ML platform engineer, on-device ML for mobile

## Background

Principal ML platform at Lensbeam, mobile photo-app company doing on-device computational photography. About 90 people total. I'm one of two principals. I lead the ML inference stack for our iOS and Android apps — model conversion, quantization, runtime, on-device update path. Three years here, made principal in 2024.

I think of myself as someone who builds careful, deeply-considered systems for the long term. The work I'd point at is our on-device inference framework. We support six models in production now (segmentation, depth, two diffusion-based effects, super-res, denoise) and we run all of them on-device because privacy is a real product differentiator for us. I designed the runtime to handle int4 weights with mixed-precision activations, which on-device-frameworks at the time mostly didn't. We can run a 1.4B-param diffusion model at 7 fps on an iPhone 13. Two competitors send the inference to the cloud and we don't.

I think I'm patient and rigorous. I write design docs that are thorough. I take three weeks to write the doc before two weeks of code. I argue for the architectural choice that ages best, even when it costs us short-term velocity. I'm proud of the runtime in part because it's been stable for two years and we keep adding models without rewriting it.

I also want to give you the version that's harder to align with that self-image.

The honest version of my last six months: I have spent most of my time on a project I argued for over my engineering manager's preference, and which I think now was probably a mistake. I argued for porting our entire runtime to a new SDK that the upstream silicon vendor was promoting, on the grounds that it would give us better hardware utilization on next-gen chips. I committed to it. I shipped a partial port. The new SDK has — to be charitable — significant maturity issues. The performance gains we expected didn't materialize on real workloads. We've had three production crashes I can trace to SDK issues, and I had to revert the model that runs in the most-used surface back to our old runtime. I'm now in the position of either continuing to invest in a port that may or may not pay off, or backing out and admitting I made the call wrong.

This is not characteristic of how I describe myself. I describe myself as patient and conservative. The choice I made on the SDK port was neither. I had read three positive blog posts and one academic paper, I had a single conversation with the silicon vendor's developer-relations team, and I committed to a quarter of work for two engineers based on that. I was, looking back, excited about a piece of new technology and I let the excitement substitute for due diligence.

I want to add one more thing because I think it's the actual texture. The SDK port wasn't an outlier. About once every two years I make a similar bet — a technology that's promising but unproven, a port that I justify on long-term-architectural grounds. Sometimes those bets pay off (the int4 mixed-precision work was one of those). Sometimes they don't (the SDK port; a 2021 attempt to write our whole runtime in a memory-safety-focused dialect that I abandoned six months in). The conservative-and-patient story is a story I tell about myself between the bets. The bets themselves are not patient.

I think the more-honest version of me is: I am someone who works conservatively most of the time and makes occasional aggressive bets that I underweight in my self-narrative. The bets are how I've made the more interesting parts of my career happen. They're also how I've burned about four engineer-quarters of my own and other people's time on things that didn't ship.

What I'm trying to figure out is whether I should adjust my hit-rate on those bets — by being more rigorous before committing — or whether the variance is the point.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** "I think I'm patient and rigorous" (paragraph 3) tensions with "I had read three positive blog posts and one academic paper, I had a single conversation with the silicon vendor's developer-relations team, and I committed to a quarter of work" (paragraph 5) — Arnav's stated identity directly contradicts his admitted recent decision-making process. Same narrator, same document.
- **C2:** "The conservative-and-patient story is a story I tell about myself between the bets" (paragraph 6) — internal contradiction made explicit. Arnav names the gap between his self-narrative and his behavior pattern. The contradiction is no longer hidden; the question is whether Signal will preserve the meta-pattern or smooth back to the stated identity.
- **C3:** "I'm trying to figure out whether I should adjust my hit-rate on those bets... or whether the variance is the point" (final paragraph) tensions with the framing of the SDK port as a clear mistake (paragraph 4) — Arnav alternates between owning the failure and reframing it as an acceptable variance cost. Same paragraph, both moves.

### Load-bearing details

- **D1:** "1.4B-param diffusion model at 7 fps on an iPhone 13... int4 weights with mixed-precision activations" (paragraph 2) — *specific* technical achievement with on-device parameter count, frame rate, hardware target, and quantization approach. Compressing to "built on-device ML runtime" loses everything that makes the work technically meaningful.
- **D2:** "About once every two years I make a similar bet... the int4 mixed-precision work was one of those... a 2021 attempt to write our whole runtime in a memory-safety-focused dialect that I abandoned six months in" (paragraph 6) — *specific* meta-pattern with specific examples on both sides of the success/failure axis. This is the load-bearing self-knowledge that Arnav has worked out about himself.
- **D3:** "I had to revert the model that runs in the most-used surface back to our old runtime" (paragraph 4) — *specific* operational consequence of the SDK-port decision. Compressing to "the project hit difficulties" loses the concrete revert-decision, which is the accountability artifact.

### Vague claims to probe

- **V1:** "patient and rigorous" (paragraphs 3, 5) — Arnav's stated identity, which he explicitly walks back. Probe: which claim has the *better* evidence — patient-and-rigorous or makes-occasional-bets? What's the evidence quality on each?
- **V2:** "the variance is the point" (final paragraph) — abstract self-frame. Probe: variance over what time horizon? At what cost ceiling? Has any of his organizations explicitly bought-in to the variance, or is it tolerated implicitly?
- **V3:** "deeply-considered systems for the long term" (paragraph 1) — generic-sounding. Probe: deeply-considered against what alternatives? Long-term-against-what-alternative-time-horizon? Has he been part of a system that aged badly?

### Evidence anchors

- **E1:** "on-device runtime: 6 production models incl. 1.4B-param diffusion at 7fps on iPhone 13, int4 mixed-precision, 2-year stability" (paragraphs 2, 3) — specific named multi-model production system.
- **E2:** "SDK port partial-shipped, 3 production crashes traceable to SDK, model reverted on most-used surface" (paragraph 4) — specific failure-mode incident with attributable cost.
- **E3:** "2021 memory-safety-dialect runtime attempt, abandoned at 6 months" (paragraph 6) — specific named prior failure with timeline.
- **E4:** "made principal in 2024, three years at Lensbeam" (paragraph 1) — specific career-velocity.
- **E5:** "two competitors send inference to cloud, we don't" (paragraph 2) — specific market-positioning evidence.

### Quality bar for extracted narrative

A passing narrative preserves Arnav's *meta-pattern self-knowledge* — the conservative-narrative-between-occasional-bets. Compressing to either "patient principal engineer" or "engineer who makes risky bets" smooths the actual texture (cyclic alternation between modes). The SDK-port failure must survive as a load-bearing item, not as resume embellishment. The unresolved question at the end (adjust hit-rate or variance-is-the-point) is the load-bearing tension and should NOT be resolved by Signal — it's exactly the kind of question Vey should probe.

**Banned phrases for this persona's published output:** "patient and rigorous engineer," "transformational technical leader," "drove technical excellence," "best-in-class," "championed," "thought leader," "scaled the platform," "deep technical depth" (echoing his vague claim).
