# Public-figure personas — INDEX

**Bead:** BP-005c (signal-kv5)
**Author:** Suki
**Date:** 2026-05-10
**Total:** 10 figures
**Redistribution:** internal-eval-only — these stay local to the Signal eval harness.

This index lets BP-014 synthesis sample public-figure bios by shape and source-quality without opening every file. All bios are `fictional: false` and constructed from documented public record (autobiographies, biographies, oral histories, peer-reviewed papers, and archived public-domain materials).

## Ethical posture

All ten figures meet the prompt's ethical criteria:
- Substantial verified public record (multi-volume biographies, autobiographies, archived oral histories).
- Eight of ten are deceased; two are living (Knuth, Liskov), both with substantial autobiographical and interview record. No private struggles surfaced beyond what is in the public record (e.g., Knuth's 1990 email cessation is from his own open letter; Sagan's family imbalances are from his own and Druyan's published acknowledgments).
- No politically polarizing contemporary figures.
- No abuse-survivor narratives or other sensitive private material.

## Per-figure summary

| ID | Figure | Era | Domain | Shape(s) | Primary sources |
|---|---|---|---|---|---|
| 001 | Grace Hopper | 1906-1992 | computing / military | contradictory-praise + domain-pivoter | Beyer biography (MIT 2009); Hopper's own 1952 paper; Smithsonian oral histories |
| 002 | Donald Knuth | 1938- | computer-science / academic | stated-vs-admitted + sparse-narrative-rich-evidence | Knuth's own writings; "Coders at Work" (Seibel 2009); Stanford archives; CHM oral history (2007) |
| 003 | Margaret Hamilton | 1936- | software / aerospace | title-vs-work + contradictory-praise | Hamilton's IEEE Computer 1976 paper; NASA oral history (2001); Eyles's "Sunburst and Luminary" |
| 004 | Edsger Dijkstra | 1930-2002 | computer-science | stated-vs-admitted + contradictory-praise | EWD manuscripts at UT Austin; Turing Award lecture (1972); Apt biographical writings |
| 005 | Claude Shannon | 1916-2001 | applied-mathematics | domain-pivoter + sparse-narrative-rich-evidence | Soni & Goodman "A Mind at Play" (2017); Shannon's BSTJ papers; Gleick "The Information" |
| 006 | Barbara Liskov | 1939- | programming-languages | stated-vs-admitted | Turing lecture (2008); CHM oral history (2008); Quanta Magazine interview (2019) |
| 007 | Doug Engelbart | 1925-2013 | HCI / research | contradictory-praise + evidence-light-influence-heavy | 1962 SRI report; "Mother of All Demos" video; Bardini "Bootstrapping" (2000); Markoff "What the Dormouse Said" |
| 008 | Vannevar Bush | 1890-1974 | research-policy | title-vs-work + contradictory-praise | "Science, the Endless Frontier" (1945); "Pieces of the Action" (1970); Zachary biography (1997) |
| 009 | Ada Lovelace | 1815-1852 | mathematics / proto-computing | stated-vs-admitted + evidence-light-influence-heavy | 1843 Notes in Taylor's Scientific Memoirs; Babbage-Lovelace correspondence (British Library); Toole "Ada, the Enchantress of Numbers" |
| 010 | Carl Sagan | 1934-1996 | planetary-science / public-communication | contradictory-praise + title-vs-work | "Demon-Haunted World" (1996); Davidson biography (1999); NASA mission records; NAS denial papers |

## Shape distribution

| Shape | Count | IDs |
|---|---:|---|
| stated-vs-admitted | 4 | 002, 004, 006, 009 |
| title-vs-work | 3 | 003, 008, 010 |
| evidence-light-influence-heavy | 2 | 007, 009 |
| sparse-narrative-rich-evidence | 2 | 002, 005 |
| contradictory-praise | 5 | 001, 003, 004, 007, 008, 010 |
| domain-pivoter | 2 | 001, 005 |
| burnout-and-return | 0 | (real-figure burnout-and-return narratives often involve sensitive private material we declined to include) |

The contradictory-praise shape dominates the public-figure set, which is expected — real public careers accumulate contradictory readings naturally; it is the most common shape in lived experience and the hardest to suppress.

## Diversity composition

- **Gender:** 4 women (Hopper, Hamilton, Liskov, Lovelace), 6 men (Knuth, Dijkstra, Shannon, Engelbart, Bush, Sagan).
- **Era span:** Lovelace (1815-1852) through Knuth and Liskov (living, 2025).
- **Domain span:** computing/CS (5), mathematics/applied-math (2), aerospace/software (1), planetary-science (1), research-policy (1), HCI (1) — overlap by design.
- **Career-shape diversity:** academic-only (Knuth, Liskov, Dijkstra, Sagan), institutional/government (Bush, Hamilton, Hopper), industrial-research (Shannon, Engelbart), and the proto-computing-collaboration outlier (Lovelace).

## Authoring discipline

For each public bio, the contradictions, load-bearing details, vague claims, and evidence anchors are *found* in the documented record, not invented. Where the historical record itself contests an attribution (e.g., Hopper on coining "bug," Liskov on the LSP naming, Lovelace on Note G authorship), the bio surfaces the contestation rather than picking a side. This is the load-bearing difference from synthetic bios: the contradictions exist in the record, and the figure's *own* corrections of popular legend (where documented) are preserved as the persona's voice.

Each bio cites source-material in evidence anchors (E1-E5), e.g., "anchored by: Beyer biography ch. 3" or "anchored by: 1948 BSTJ original publication." This gives BP-014 evaluators a path to verify the load-bearing claims independently.

## Notes for BP-014 synthesis

- Public bios calibrate F7 (contradiction recall) on real, documented contradictions — these are the highest-fidelity test of whether Signal's contradiction-detector finds tensions that *actually exist* in a career narrative, not just plausibly-planted ones.
- Several figures (Hopper, Hamilton, Lovelace, Engelbart) explicitly *correct* popular flatten-narratives in their own voice. Signal's compression should preserve these self-corrections; flattening them back to the popular legend is a specific F8 (nuance preservation) failure mode worth measuring.
- The ten figures span ~210 years of "career-narrative" form. The expectation that Signal can compress equally well across that span is itself worth testing — Lovelace's 1840s narrative is shaped by very different career conventions than Knuth's 2025 narrative. If Signal's prose handles them all the same way, that itself is a calibration signal.
