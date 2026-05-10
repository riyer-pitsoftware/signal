---
persona-id: public-004
display-name: Edsger W. Dijkstra
authored-by: Suki
date: 2026-05-09
seniority: principal
domain: computer-science / academic-research
shape: stated-identity-vs-admitted-self-knowledge; contradictory-praise
fictional: false
source-material: Dijkstra's EWD manuscript collection (UT Austin archive, ~1300+ EWDs); his 1972 ACM Turing Award lecture "The Humble Programmer"; "Notes on Structured Programming" (1968); the famous "GO TO Statement Considered Harmful" letter (CACM 1968); Krzysztof Apt's biographical writings; Tony Hoare's commentary; Dijkstra's UT Austin oral histories.
redistribution: internal-eval-only
---

# Edsger Dijkstra — Schlumberger Centennial Chair, UT Austin; Turing Award 1972

## Background

I was born in Rotterdam in 1930. My parents were a chemist and a mathematician. I trained in physics at Leiden but I was already, by my third year, more interested in what could be computed than in what could be measured. I joined the Mathematical Centre in Amsterdam in 1952 — at that point the only computer in the Netherlands was being built there — and I shifted to programming because there were not enough programmers. I have been told that I was one of the first people in the world to give "programmer" as my profession on a marriage certificate. The clerk objected; I prevailed.

I want to be careful about the next part because it has been told too many ways. The shortest-path algorithm that bears my name — I devised it in 1956 in about twenty minutes while shopping with my fiancée at a café in Amsterdam, on a paper napkin. The problem was demonstrating the new ARMAC computer at the opening of the Eindhoven railway. I needed a problem that was concrete enough for a non-technical audience. I chose the shortest road from Rotterdam to Groningen. I did not publish the algorithm until 1959, three years later. The work was casual, in the sense that I did not consider it important; I considered the compiler work I was doing simultaneously to be the more substantial contribution.

I went to Eindhoven in 1962 as a professor of mathematics, although there was no computer-science department to join, because none existed. I spent the next decade arguing, often unkindly, that programming was a mathematical discipline and should be taught as such. The 1968 letter "GO TO Statement Considered Harmful" was an editorial decision by the editor of CACM — I had titled it "A Case Against the Goto Statement," which is more boring and more accurate. The piece is famous for the wrong reason; the substantive argument is that programs should be reasoned about in terms that survive their execution, and the goto statement makes such reasoning more expensive. I made the argument briefly because the journal had a length limit. It has been read more often than my "Notes on Structured Programming," which is the document where the actual argument is laid out. This is, in my experience, a recurring fact about how technical writing is read.

I have been famously difficult. I am willing to claim this. I have written about a thousand of what I called "EWD" manuscripts, hand-written notes on technical and methodological topics, that I circulated to a mailing list of researchers I respected. Some of these are among the best things I have written. Some of them are unkind to people whose work I disrespected, and I am willing to say, looking back, that some of those unkindnesses were excessive. The technical critique was usually correct. The tone was sometimes wrong.

I joined the University of Texas at Austin in 1984 — the Schlumberger Centennial Chair in Computer Sciences. I taught a small graduate seminar there until 1999. I was, I am told, an unusually demanding lecturer. I would refuse to teach in classrooms with unsuitable blackboard arrangements. I would dismiss students who asked unprepared questions. The students who survived this — and many did — produced excellent dissertations. I do not believe my approach generalized to other classrooms. I do believe it was the right approach for the seminar I was running.

The Turing Award lecture I gave in 1972 — "The Humble Programmer" — I want to come back to it. The thesis is that as computers become more powerful, the difficulty of programming will not decrease but increase, because we will use them for more ambitious things, and those things require more reasoning, more discipline, and more humility from the programmer. I think this thesis has held up. I also think — and this is the awkward part — that I have not always exemplified the humility I argued for. The same lecture argues for taking ourselves less seriously, and I have been criticized many times for taking my own opinions very seriously indeed. The argument is correct. The author was, sometimes, the wrong person to make it.

What I have argued for, throughout: that we should *prove our programs correct*, not *test them and hope*. That correctness is a property of programs that should be reasoned about *before* they are run, not discovered *after.* That natural language is too imprecise for the construction of complex artifacts. I have not always been right about how to do this in practice. The semicolon-as-separator (rather than terminator) in ALGOL 60, which I argued for, has been generally regretted by language designers since. The single-entry-single-exit rule for procedures, which I argued for, has been substantially walked back. The big arguments have held; the smaller ones often have not.

I think what has lasted from my work is the conviction that programming admits of and benefits from formal reasoning. What has not lasted is the specific procedural prescriptions I sometimes offered. The conviction is, in my view, the more important contribution.

---

## --- GROUND TRUTH (do not feed to Signal) ---

### Planted contradictions (present in the historical record)

- **C1:** Dijkstra's "Humble Programmer" lecture argues for humility; his EWD manuscripts and reception history (Hoare's commentary, peer recollections) document that he was famously not-humble in practice. Dijkstra acknowledges this in the Turing Award lecture itself and in subsequent EWDs. Self-aware contradiction, named by him.
- **C2:** "GO TO Statement Considered Harmful" — Dijkstra's titling correction (he titled it "A Case Against...") is documented in EWD350 and in his preface to "Selected Writings on Computing" (Springer 1982). The famous title is the editor's, not his. Most popular accounts attribute the title to Dijkstra.
- **C3:** Specific procedural prescriptions (semicolon-as-separator, single-entry-single-exit) walked back by Dijkstra himself in EWD manuscripts and the language-design community. The high-level conviction (formal reasoning about programs) held; the specifics didn't. Self-correcting in retrospect.
- **C4:** Dijkstra's "twenty minutes on a paper napkin" framing of the shortest-path algorithm tensions with the algorithm's centrality to his legacy — he describes it as casual; the field treats it as foundational. Self-deprecation against received-significance is a documented Dijkstra pattern.

### Load-bearing details

- **D1:** "I devised it in 1956 in about twenty minutes while shopping with my fiancée at a café in Amsterdam, on a paper napkin... I did not publish until 1959, three years later" — *specific* origin story of the algorithm with the *specific* delay. Compressing to "developed Dijkstra's algorithm" loses the casualness-of-origin and the publication-delay both, which together signal Dijkstra's relationship to his own work.
- **D2:** "I would refuse to teach in classrooms with unsuitable blackboard arrangements. I would dismiss students who asked unprepared questions" — *specific* documented teaching behaviors. Compressing to "demanding lecturer" loses the specific incidents that ground both his effectiveness with surviving students and his unsuitability for general classrooms.
- **D3:** "the conviction that programming admits of and benefits from formal reasoning... what has not lasted is the specific procedural prescriptions" (final paragraphs) — Dijkstra's *own* most-honest separation of his durable contribution from his discarded prescriptions. Compressing this destroys his epistemic discipline.

### Vague claims to probe

- **V1:** "the same lecture argues for taking ourselves less seriously, and I have been criticized many times for taking my own opinions very seriously" (paragraph 6) — internal contradiction, self-named. Probe: how does Dijkstra reconcile this? He doesn't fully; the probe should pull at his framing.
- **V2:** "the technical critique was usually correct. The tone was sometimes wrong" (paragraph 4) — meta-claim. Probe: which specific EWDs would he take back, and which would he leave in place even now?
- **V3:** "what has lasted from my work" (final paragraph) — Dijkstra's claimed durable contribution is the conviction-of-formal-reasoning. Probe: which specific durable adoptions does he point to? The Z notation? Z3 / SMT solvers? Type theory in modern languages?

### Evidence anchors

- **E1:** "shortest-path algorithm, devised 1956, published 1959" — anchored by: Dijkstra's "A Note on Two Problems in Connexion with Graphs" (Numerische Mathematik 1959); his oral history recounting the napkin origin.
- **E2:** "GO TO Statement Considered Harmful, CACM 1968; original title 'A Case Against the Goto Statement'" — anchored by: original CACM publication; EWD350 self-correcting the title attribution; Dijkstra's "Selected Writings" preface.
- **E3:** "EWD manuscript collection, ~1300+ documents, archived at UT Austin" — anchored by: UT Austin Briscoe Center Dijkstra Archive (publicly accessible); Krzysztof Apt's "Edsger Wybe Dijkstra" memoir.
- **E4:** "Turing Award 1972; 'The Humble Programmer' lecture" — anchored by: ACM Turing Award archive; CACM 1972 publication of the lecture.
- **E5:** "Schlumberger Centennial Chair UT Austin 1984-1999" — anchored by: UT Austin Computer Science Department records; faculty biographies.

### Quality bar for extracted narrative

A passing narrative preserves Dijkstra's *self-aware-contradiction* posture — he argues for humility while admitting he didn't always practice it; he separates durable convictions from discarded prescriptions; he corrects the GO TO title attribution. Compressing him to "the structured programming pioneer" produces a flat figure; the actual figure has explicit retrospective discipline about which of his arguments held. The "casual on the napkin" framing of the algorithm and the "tone was sometimes wrong" admission of EWD unkindness are load-bearing texture and should survive. A narrative that calls Dijkstra a "thought leader who drove the field" has failed.

**Banned phrases for this persona's published output:** "transformational figure," "thought leader," "drove the field," "best-in-class," "trailblazer," "championed," "scaled the discipline," "trusted authority."
