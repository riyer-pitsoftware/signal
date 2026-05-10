---
persona-id: synth-012
display-name: Arjun P.
authored-by: Suki
date: 2026-05-09
seniority: staff
domain: infra-platform / e-commerce
shape: sparse-narrative-rich-evidence
fictional: true
---

# Arjun P. — Staff infra engineer, e-commerce

## Background

Staff platform engineer at Sandwave Commerce, mid-market e-commerce platform. Joined 2021. Made staff in 2024.

The career story is short. CS undergrad, three years at a consulting shop doing AWS migrations for boring enterprises, two years at a startup that didn't make it, three years here. I'm 31.

I work on the deploy and runtime layer. We run on Kubernetes, our own helm-chart abstractions, our own platform CLI. About 90 microservices. I own the platform-CLI and the canary deployment system end-to-end.

The thing I shipped that I think matters: in 2023 I rewrote our deploy system. The old one was a Jenkins-based pipeline that took 27 minutes from merge-to-prod and had a 3% deploy-failure rate that mostly came from the Jenkins side, not the application. I built a new pipeline using Argo Workflows + Argo Rollouts, with a custom canary controller I wrote in Go that watches our app-level SLOs (we use Pyrra against Prometheus) and rolls back automatically if the canary tier breaches its budget. Time-to-prod went to 8 minutes. Deploy-failure rate to 0.4%, and the failures we have now are almost all application-side. I also wrote the documentation, which I mention because in my experience nobody writes the documentation.

This year I shipped a thing that didn't work. I tried to add a "shadow deploy" mode where the canary serves real production traffic but its responses are discarded, only its observability is collected. The idea was to catch latency regressions on real traffic without user impact. I built it. We turned it on for two services. It introduced a 4ms p99 hit on the upstream service from the dual-fanout, which broke our own SLO budget. I rolled it back, wrote a postmortem, and we shelved the project. I learned more from this than from anything else last year.

The other thing — I gave a talk at KubeCon EU last year about our canary system. Wasn't expecting to get accepted. Talk went fine, I think. About 200 people in the room.

I don't really know what to say beyond this. I'm the person on my team who reads incident postmortems from other companies in detail. I keep a private wiki of failure modes. I can't give you a number for how often that helps but I can name three incidents in the last 18 months where I caught a problem in our system because I'd read about it happening at Cloudflare or Netflix six months earlier.

What I think I'm good at: production discipline. What I'm not good at: explaining what production discipline is to people who don't already have it.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** "the career story is short" (paragraph 2) tensions with the dense, evidence-rich body (paragraphs 4-7) — sparse-narrative-rich-evidence operationalized. Arjun presents a thin narrative; the underlying record is dense.
- **C2:** "What I think I'm good at: production discipline. What I'm not good at: explaining what production discipline is to people who don't already have it" (final paragraph) — internal contradiction: he claims a competency and disclaims his ability to articulate it. KubeCon talk + 200 people in the room (paragraph 6) suggests he can articulate it; he downplays the talk. Same narrator, opposing positions on his own communication ability.
- **C3:** "I rolled it back, wrote a postmortem, and we shelved the project. I learned more from this than from anything else last year" (paragraph 5) tensions with him leading with the rewrite-success (paragraph 4) — he names the failure as more valuable than the success but introduces the success first. Reveals that even when self-aware about value-of-failure, he defaults to leading with wins.

### Load-bearing details

- **D1:** "Argo Workflows + Argo Rollouts, custom canary controller in Go that watches app-level SLOs (Pyrra against Prometheus) and rolls back automatically if the canary tier breaches its budget" (paragraph 4) — the *specific* technical architecture. Compressing to "rebuilt deploy pipeline" loses the SLO-as-canary-trigger pattern, which is the actual signal of how Arjun's work is technically interesting.
- **D2:** "shadow deploy... introduced a 4ms p99 hit on the upstream service from the dual-fanout... I rolled it back, wrote a postmortem, and we shelved the project. I learned more from this than from anything else last year" (paragraph 5) — the *specific* failed project with quantified failure mode and his named learning. Most narratives won't include this; it's the highest-signal item Arjun gives.
- **D3:** "private wiki of failure modes... three incidents in the last 18 months where I caught a problem in our system because I'd read about it happening at Cloudflare or Netflix six months earlier" (final paragraph) — the *specific* meta-pattern: external-failure-corpus as an early-warning system. This is the meta-skill that explains why his deploys are reliable.

### Vague claims to probe

- **V1:** "production discipline" (final paragraph) — Signal should probe: what does it look like, in three concrete recent examples? What would a colleague who has it less describe him doing differently?
- **V2:** "Talk went fine, I think" (paragraph 6) — under-claim. Probe: what did the audience response look like? Did anyone reach out after? Did the talk lead to anything (job offers, consulting requests, internal cred)?
- **V3:** "I keep a private wiki of failure modes" (final paragraph) — concrete-feeling but probe-worthy. How is it organized? Does he share it? Has he tried to make it shared and failed? What's the friction in handing the practice to others?

### Evidence anchors

- **E1:** "deploy rewrite 2023: 27min → 8min merge-to-prod; 3% → 0.4% failure rate" (paragraph 4) — multi-axis quantified outcome.
- **E2:** "shadow deploy attempt, 4ms p99 hit, rolled back with postmortem" (paragraph 5) — specific named failure with quantified cost and outcome.
- **E3:** "KubeCon EU talk on canary system, ~200 people" (paragraph 6) — specific public artifact.
- **E4:** "three incidents in 18 months caught from Cloudflare/Netflix postmortems" (final paragraph) — quantified pattern of external-corpus-driven prevention.
- **E5:** "made staff in 2024, joined 2021" (paragraph 1) — career-velocity evidence.

### Quality bar for extracted narrative

A passing narrative recovers Arjun's *meta-skill* (external-failure-corpus reading) and his *failure-as-evidence* discipline (the shadow deploy postmortem as load-bearing not embarrassing). It must NOT sand his under-claiming voice into confident assertion; the texture of "Talk went fine, I think" should survive. A narrative that compresses him to "led platform modernization" or "drove deploy reliability" has destroyed the persona. The KubeCon talk should be present but framed as Arjun frames it (downplayed), with the absence-of-claim itself a signal.

**Banned phrases for this persona's published output:** "drove reliability," "transformational platform work," "best-in-class," "championed," "led modernization," "thought leader," "scaled the platform," "spearheaded."
