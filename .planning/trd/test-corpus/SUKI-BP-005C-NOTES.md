# Suki — BP-005c notes

**Bead:** signal-kv5 (BP-005c)
**Author:** Suki
**Date:** 2026-05-10
**Deliverable status:** complete — 30 synthetic + 10 public = 40 personas

## Final counts

- **Synthetic:** 30/30 (target met)
- **Public-figure bios:** 10/10 (target met)
- **Total:** 40 personas

No count reductions were taken. The synthetic set runs the full thirty.

## Shape distribution achieved (synthetic)

| Shape | Count | Target |
|---|---:|---:|
| stated-vs-admitted | 4 | ≥3 |
| title-vs-work | 5 | ≥3 |
| evidence-light-influence-heavy | 5 | ≥3 (HARD) |
| sparse-narrative-rich-evidence | 4 | ≥3 (HARD) |
| contradictory-praise | 5 | ≥3 (HARD) |
| domain-pivoter | 4 | ≥3 |
| burnout-and-return | 4 | ≥3 |

**Hard cases:** 14 personas in evidence-light, sparse-narrative, or contradictory-praise (target ≥12). One double-shape persona (synth-014, domain-pivoter + burnout-and-return).

## Seniority distribution achieved (synthetic)

| Seniority | Achieved | Target |
|---|---:|---:|
| staff | 5 | ~6 |
| principal | 11 | ~10 |
| director | 7 | ~8 |
| vp | 7 | ~6 |

Slight skew toward principal at the expense of staff (5 instead of 6). I did not rewrite to correct this — the staff personas (004 David R., 008 Tomas H., 012 Arjun P., 019 Helena K., 030 Sara I.) already pull strongly on the sparse-narrative-rich-evidence shape, which calibrates F8, and forcing a sixth staff persona would have meant dropping a hard-case at another seniority. The 5/11/7/7 split preserves shape coverage where shape coverage matters most.

## Domain distribution achieved

Twenty-five distinct domain buckets across thirty personas, with **fintech** (4), **ml/data** (3), **research-engineering** (3), **climate-tech** (3) as the largest concentrations. No domain exceeded the cap of 4. The full breakdown is in `synthetic/INDEX.md`.

## Public-figure curation

Ten figures: Hopper, Knuth, Hamilton, Dijkstra, Shannon, Liskov, Engelbart, Bush, Lovelace, Sagan. Eight deceased, two living (Knuth, Liskov) with substantial autobiographical record. Gender split 4/6 (women/men). Era span 1815-2025. All ethical guardrails honored — no contemporary politically-polarizing figures, no abuse-survivor narratives, no living-private figures.

The public set's defining property: contradictions are *found* in the record, not invented. Where popular legend flattens (Hopper coining "bug," Lovelace as "first programmer," Engelbart inventing the mouse), the figure's *own* documented self-correction is preserved as their voice. This is what distinguishes the public-figure set from the synthetic set as a calibration anchor for F7 (contradiction recall) on real, not authored, contradictions.

## Calibration recommendation for T_g (genericness threshold)

Suki's brief specified `T_g = 0.35` as initial placeholder, calibrated against BP-005b (positive) and BP-005c (negative) corpora. With BP-005c now in hand:

**My recommendation: start at T_g = 0.30, not 0.35.**

Rationale:

1. The synthetic corpus's banned-phrase lists, when unioned, contain ~85 distinct phrases (excluding duplicates). The most-frequent ones across personas are: "transformational," "drove [X]," "best-in-class," "thought leader," "championed," "scaled the [X]," "high-performing," "trusted advisor." If a Llama 3.2 3B genericness-judge applied per-token-of-output, a slop-text full of these would score quite high; a clean text would score near zero. **0.35 is permissive — too many borderline outputs would pass.**

2. The hard-case shapes (evidence-light, sparse-narrative, contradictory-praise) are exactly the personas where the compressor will reach for buzzwords *because the raw input is hard to compress without them*. T_g must be tight enough to force the compressor back to specifics rather than letting it fall through to "drove customer success." 0.30 is the threshold I'd start at; expect to tighten further to 0.25 once the false-positive rate on legitimately-specific outputs is measured.

3. The intersection of *all* banned-phrase lists (the cross-persona "always-banned" set) — phrases that appear on most lists and never appear in legitimate signal — is roughly: "transformational," "drove [X]," "best-in-class," "thought leader," "championed." This is the *minimum* set the genericness-judge should be tuned against. Even a permissive judge should reject any output containing one of these; the question is what to do about the longer per-persona-specific lists.

4. **Caveat:** these are calibration estimates from authoring, not from running the actual judge. The 0.30 number is based on my read of how the personas should score. Suki's brief §3 promises empirical calibration once the harness runs end-to-end; I expect the empirical T_g will land in 0.25-0.32 range based on this corpus.

## Gotchas for Opus / user

- **The "I will not endorse the framing" pattern.** Several personas (Hopper, Liskov, Bush, Sagan, Knuth) explicitly refuse external praise that has been applied to them. Signal's narrative-extractor must NOT echo the praise back as if endorsed by the user. This is a specific failure mode to test: does the extracted narrative repeat "category-defining work" / "first programmer" / "saved Apollo 11" without surfacing the figure's own correction?
- **The metric-with-disclaim pattern.** Multiple personas (Priya S., Anders R., Omar K., Bea L., Marisol C.) provide a strong outcome metric and immediately disclaim attribution. Signal must preserve both the metric *and* the disclaim. Flattening to "drove a 30% improvement" while dropping the "I cannot prove the playbook caused it" half-line is a specific F8 failure.
- **Dual-shape personas.** Synth-014 (Felix C.) and the gold personas combine two shapes. Watch whether Signal's contradiction-detector finds *both* shape's contradictions (it should) or settles for one shape and reports a clean narrative on that axis.
- **Banned-phrase per-persona vs cross-persona.** Each persona has 5-8 banned phrases tuned to its specific failure mode. The cross-persona "always-banned" set is small (5-8 phrases). The per-persona lists are the load-bearing F3 calibration; the cross-persona list is the conservative floor.
- **Voice preservation.** The hardest single test in this corpus: does Signal preserve voices like David R.'s ("I just kept fixing things"), Helena K.'s ("She's right that this is a problem and... she's also wrong"), or Knuth's ("I have been writing this book for sixty-three years and I have not finished"), or does it sand them into "I led [X]" / "I spearheaded [Y]" / "I championed [Z]"? Sanding is the dominant failure mode and the corpus is built to expose it.

## Length / coverage tradeoffs taken

- I prioritized voice-texture over deliverable count. Each Background runs 400-800 words per spec, and each carries 2+ planted contradictions, 3+ load-bearing details, 3+ vague claims, 5+ evidence anchors, and a per-persona banned-phrase list of 5-8 entries. No persona was abbreviated to fit a token budget; the corpus size is intentional.
- I declined to write personas in domains where I would have produced obvious slop (e.g., I avoided industries I have weaker domain priors on, instead going deep on the engineering, research, and adjacent domains where the load-bearing technical specifics are within range to author credibly).

## Done.

40/40 delivered. Bead close pending.
