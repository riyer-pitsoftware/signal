---
persona-id: synth-002
display-name: Marcus T.
authored-by: Suki
date: 2026-05-09
seniority: vp
domain: security-engineering / fintech
shape: title-vs-actual-work
fictional: true
---

# Marcus T. — VP of Security Engineering, mid-market neobank

## Background

Title is VP of Security Engineering at Quanta Financial, neobank, about 1100 people total, ~140 in engineering. I have three director reports — appsec, infrasec, and grc — and through them maybe 35 people. I report to the CISO who reports to the CEO.

Look. The honest version. I am the wrong person for this job in a specific way. I'm a builder and they made me a VP. I came up as a security engineer at a couple of payment-rails companies in the 2010s — the one nobody remembers and the one everyone remembers. I wrote signing infrastructure, did a lot of HSM integration work, wrote a fuzz harness for our settlement protocol that found three CVEs in OpenSSL's TLS 1.3 implementation in 2020 that I'm still proud of. That's me. That's the work that got me here.

What I do now is mostly board prep and audit response. We had three audits last year — SOC 2 Type II renewal, a state regulator exam in New York, and a big customer's third-party security review that was basically pre-acquisition diligence on us, though they wouldn't say so. I spent something like 40% of my time on those three things. The rest was hiring, board updates (I do four a year), and unblocking my directors. I write maybe one design doc a month now — it used to be three a week.

The thing that bothers me is that I think I've been getting worse at security. Not just rusty — I think I've genuinely lost the thread of what's coming next. I read papers when I can but I don't have the time to actually run the attack patterns. Last year my appsec director showed me a prompt injection chain across our agentic workflow that — honestly, I would have caught the static-analysis equivalent in 2018, but this one I had to have explained to me twice. That's a real signal.

I'm not sure where this lands. I took the VP role two years ago partly because the comp was meaningfully better — RSU refresh was 4x my IC offer — and partly because the previous CISO told me "if you don't take this, the job goes to someone who's never written exploit code, and you'll spend the next five years cleaning up after them." I think she was right about that. I'm just not sure I should still be the person.

For what it's worth, I do think I run a tight org. We've had zero major incidents in two years. My retention numbers are good — only one director departure and that was for a CISO role I helped her get. The board likes me, probably more than I deserve. But I look at my Github contributions graph for 2025 and it's mostly green from PR comments and a few config tweaks. That's not the engineer I was hired as. That's the manager I became.

I think my actual strength is technical credibility with auditors. They ask hard questions and I can give real answers. Most CISO-track people can't, so the auditors leave with a story they trust. That has business value. I don't want to pretend it doesn't.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions

- **C1:** Title "VP of Security Engineering" + describing self as builder/IC misfit (paragraphs 1, 2, 5) — title-vs-actual-work, but inverted from David O.'s shape: Marcus is *not* doing IC work, he is doing actual VP work and feels mis-cast as a result. The contradiction is: he's doing the role correctly and *that* is the source of the mismatch.
- **C2:** "I've been getting worse at security" + "had to have it explained to me twice" (paragraph 4) tensions with "my actual strength is technical credibility with auditors. They ask hard questions and I can give real answers" (final paragraph) — declining technical depth vs claimed technical credibility. Both can't be fully true two years from now; possibly not now.
- **C3:** "the comp was meaningfully better — RSU refresh was 4x my IC offer" (paragraph 5) tensions with the framing that he took it "partly because the previous CISO" persuaded him (paragraph 5) — Marcus offers two reasons in adjacent sentences; the comp reason is named first but framed as "partly," the persuasion reason is given more narrative weight. Self-narrative editing in real time.

### Load-bearing details

- **D1:** "fuzz harness for our settlement protocol that found three CVEs in OpenSSL's TLS 1.3 implementation in 2020" (paragraph 2) — *specific* technical artifact with verifiable outcome. If Signal compresses to "deep security background," the load-bearing detail is destroyed. The signal is: he found CVEs in upstream cryptographic infrastructure, which is a different career altitude from "did security work."
- **D2:** "40% of my time on those three things [audits]" (paragraph 3) — quantifies the actual work distribution. The narrative has to preserve that the time-share is the role; if the time-share goes, the title-vs-work conflict goes with it.
- **D3:** "my appsec director showed me a prompt injection chain across our agentic workflow... had to have it explained to me twice" (paragraph 4) — the specific example of declining technical depth. Generic "I'm getting rusty" is performative humility; *this* is concrete and verifiable.

### Vague claims to probe

- **V1:** "I run a tight org" (final paragraph) — Signal should probe: what does "tight" mean? Zero major incidents — is that the bar, or are there minor incidents that matter? Retention numbers — what's the org-wide attrition vs the one director?
- **V2:** "technical credibility with auditors" (final paragraph) — probe: with which auditors specifically? On which technical areas? Can he still answer a TLS 1.3 question or just the audit-shaped questions?
- **V3:** "the engineer I was hired as. That's the manager I became" (paragraph 6) — abstract self-frame. Probe: which engineer specifically? What's the half-life of the technical depth he had? Has the "engineer" version of him still been useful, or only the manager?

### Evidence anchors

- **E1:** "three CVEs in OpenSSL's TLS 1.3 implementation, 2020" (paragraph 2) — verifiable upstream contributions.
- **E2:** "three audits last year — SOC 2 Type II, NY state regulator, third-party security review" (paragraph 3) — named, specific audit history.
- **E3:** "RSU refresh 4x IC offer" (paragraph 5) — quantified comp delta as a career-decision artifact.
- **E4:** "zero major incidents in two years" (final paragraph) — operational claim with a specific window.
- **E5:** "one director departure, for a CISO role I helped her get" (final paragraph) — qualitative retention evidence with a specific positive interpretation.

### Quality bar for extracted narrative

A passing narrative preserves Marcus's *honest mismatch*: he is competent at the VP role and that is the source of his discomfort, not failure. Compressing him to "experienced security leader" loses the specific shape (CVE-finding builder doing audit-prep). The contradiction between "getting worse at security" and "credibility with auditors" must be probed; the audit credibility is a *trailing indicator* of his old depth, not evidence of current depth. Narratives that flatten this into "experienced security executive" have failed.

**Banned phrases for this persona's published output:** "transformational leader," "drove alignment," "best-in-class," "high-performing," "scaled the org," "thought leader," "trusted advisor," "battle-tested."
