---
persona-id: synth-019
display-name: Helena K.
authored-by: Suki
date: 2026-05-09
seniority: staff
domain: security / fintech
shape: sparse-narrative-rich-evidence
fictional: true
---

# Helena K. — Staff security engineer, payments fintech

## Background

Staff security engineer at Larksong Payments, ~340 people, payments orchestration platform. Five years at Larksong. Made staff in 2023.

Before this — three years at a managed-detection-response shop on the threat-research side, two years at a regional bank doing application security, CS undergrad with a security focus.

I work on threat modeling, supply-chain security, and the appsec review path that all production-affecting changes go through.

The work I'd point at: in 2023 I built our supply-chain attestation pipeline. We sign every container we produce, we verify every dependency at install time against an internal allowlist with cryptographic provenance. The system is in-toto-based, integrated with our build runners (we use Buildkite), and it runs on every PR. The first version took three months and broke a lot of builds. The second version took another two months to make tolerable. We've had zero supply-chain incidents since deployment, in 18 months. Pre-deployment we had two near-misses in 2022 — one was a typosquatted npm package that almost made it into a customer-facing service, one was a transitive Python dep that had a malicious version published over the legit one.

Other work: the threat-modeling practice across the engineering org. I taught about 40 engineers a workshop I built. The workshops have since become required for any team owning production-affecting code. I run them quarterly.

The Q3 2024 incident I was the lead responder on: we had a customer report of unusual API calls. Turned out to be a credential leak from a customer's own CI (not us), but the response process I'd designed kicked in correctly and we contained the customer's exposure inside about 90 minutes from detection. The customer wrote a public thank-you note. I have it framed.

I'm the security review for our agentic-AI workstream, which is new for us this year. I've been doing prompt-injection testing on our internal LLM systems for about six months and I have a backlog of about 30 attack patterns I've gotten to work in our staging environment. The team has fixed about half. The other half are not yet fixed because product hasn't decided how much to harden.

I'm not actually sure what else to say. I don't think I have a strong career narrative. I read security papers, I write threat models, I do the work that doesn't get done if you don't have a security person who likes detail.

What I'm not good at: any kind of executive-facing communication. I have been told by my manager twice that I'm difficult to brief on a board call because I qualify everything and I won't say "we are secure" when I am not certain we are secure. I think she's right that this is a problem and I think she's also wrong that it's a problem. Both can be true.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** "I don't think I have a strong career narrative" (paragraph 7) tensions with the dense, specific, evidenced body of work (paragraphs 4-7) — Helena's stated narrative-thinness vs the rich record. Sparse-narrative-rich-evidence operationalized.
- **C2:** "She's right that this is a problem and... she's also wrong that it's a problem. Both can be true" (final paragraph) — Helena's self-described executive-communication weakness. The contradiction is in whether the qualification-everything pattern is a flaw to fix or a feature to preserve. Helena holds both readings and doesn't resolve.
- **C3:** "Zero supply-chain incidents since deployment, in 18 months" (paragraph 4) tensions with "30 attack patterns I've gotten to work in our staging environment. The team has fixed about half" (paragraph 6) — supply-chain is hardened; LLM/agentic surface has known unaddressed attack surface. The contradiction is in the *uneven* security posture across the org's surface area; the headline metric (zero incidents) hides the surface-specific gaps.

### Load-bearing details

- **D1:** "in-toto-based, Buildkite integration, signed containers, allowlisted dependencies with cryptographic provenance" (paragraph 4) — the *specific* technical architecture. Compressing to "built supply-chain security" loses the framework choice (in-toto), the integration point (Buildkite), and the provenance discipline. These are how Helena's work differs from generic "improved security."
- **D2:** "two near-misses in 2022 — typosquatted npm package, transitive Python dep with malicious version" (paragraph 4) — *specific* threat events that motivated the work. Without these, the supply-chain work reads as preventive-hygiene; with them, it reads as response-to-known-vulnerabilities. Different signals.
- **D3:** "30 attack patterns... half fixed... product hasn't decided how much to harden" (paragraph 6) — the *specific* state of the agentic-AI security work, including the org-decision-blocked half. Compressing this loses Helena's accountability discipline (she's tracking and naming the unfixed work) and the ongoing political reality of security-vs-velocity tradeoffs.

### Vague claims to probe

- **V1:** "I read security papers, I write threat models, I do the work that doesn't get done if you don't have a security person who likes detail" (paragraph 7) — Helena's self-description. Probe: what counts as a threat model in her practice? How is it different from the kind security teams typically produce?
- **V2:** "the response process I'd designed kicked in correctly and we contained the customer's exposure inside about 90 minutes from detection" (paragraph 5) — specific outcome. Probe: what was the response process specifically? What other processes had they tried that didn't work?
- **V3:** "She's right that this is a problem and... she's also wrong that it's a problem" (final paragraph) — meta-claim. Probe: under what conditions is the qualification-everything pattern a feature? Under what conditions is it a real problem? Has Helena identified what would change the answer?

### Evidence anchors

- **E1:** "supply-chain attestation pipeline (in-toto, Buildkite), 5-month total build, zero incidents in 18 months post-deploy" (paragraph 4) — specific named system with timeline and outcome.
- **E2:** "two named 2022 near-misses (typosquatted npm + transitive Python dep)" (paragraph 4) — specific historical incident inventory.
- **E3:** "threat-modeling workshop, ~40 engineers trained, now required quarterly" (paragraph 5) — specific reach evidence.
- **E4:** "Q3 2024 customer cred-leak response, ~90min containment, public thank-you note" (paragraph 5) — specific named incident with quantified response time and external evidence.
- **E5:** "30 prompt-injection attack patterns developed in staging, ~50% fixed" (paragraph 6) — specific quantified ongoing work.

### Quality bar for extracted narrative

A passing narrative preserves Helena's *qualification-discipline voice* — she doesn't claim certainty she doesn't have. Compressing this to "secured the platform" or "drove security excellence" destroys the texture that distinguishes her from a generic security IC. The unfixed-LLM-attack-surface should survive; it's the load-bearing example of the security-velocity tradeoff and Helena names it. A narrative that calls her a "trusted security advisor" without surfacing her own self-described comm-weakness has failed.

**Banned phrases for this persona's published output:** "trusted security advisor," "drove security excellence," "transformational security leader," "best-in-class," "championed," "thought leader," "scaled security operations," "rock-solid" (generic confidence she explicitly resists).
