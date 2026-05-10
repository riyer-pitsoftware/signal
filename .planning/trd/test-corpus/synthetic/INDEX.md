# Synthetic personas — INDEX

**Bead:** BP-005c (signal-kv5)
**Author:** Suki
**Date:** 2026-05-10
**Total:** 30 personas

This index lets BP-014 synthesis sample by shape, seniority, and domain without opening every file. All personas are `fictional: true` and authored to spec (≥2 contradictions, ≥3 load-bearing details, ≥3 vague claims, ≥5 evidence anchors, persona-specific banned-phrase list).

## Shape distribution

| Shape | Count | IDs |
|---|---:|---|
| stated-identity-vs-admitted-self-knowledge | 4 | 001, 008, 016, 023 |
| title-vs-actual-work | 5 | 002, 009, 010, 017, 024 |
| evidence-light-influence-heavy (HARD) | 5 | 003, 011, 018, 025, 029 |
| sparse-narrative-rich-evidence (HARD) | 4 | 004, 012, 019, 026 |
| contradictory-praise (HARD) | 5 | 005, 013, 020, 027, 030 |
| domain-pivoter | 4 | 006, 021, 028 + 014 (double) |
| burnout-and-return | 4 | 007, 015, 022 + 014 (double) |

**Hard cases (combined):** 14 personas (target ≥12) — 003, 004, 005, 011, 012, 013, 018, 019, 020, 025, 026, 027, 029, 030.

**Double-shape personas:** synth-014 (domain-pivoter + burnout-and-return).

## Seniority distribution

| Seniority | Count | Target | IDs |
|---|---:|---:|---|
| staff | 6 | ~6 | 001 (no — principal), 004, 008, 012, 015 (no — principal), 019, 030 |
| principal | 10 | ~10 | 001, 003, 006, 011 (no — vp), 015, 017, 020, 023, 026, 028 |
| director | 7 | ~8 | 005, 009, 014, 018, 021, 024, 027 |
| vp | 7 | ~6 | 002, 010, 011, 016, 022, 025, 029 |

Final achieved: staff=5, principal=10, director=7, vp=7, total=29 + 1 = 30.

(Note: re-counting from files: 001=principal, 002=vp, 003=principal, 004=staff, 005=director, 006=principal, 007=principal, 008=staff, 009=director, 010=vp, 011=vp, 012=staff, 013=principal, 014=director, 015=principal, 016=vp, 017=principal, 018=director, 019=staff, 020=principal, 021=director, 022=vp, 023=principal, 024=director, 025=vp, 026=principal, 027=director, 028=principal, 029=vp, 030=staff.
**Final tally:** staff=5, principal=11, director=7, vp=7. Slight under-rotation on staff (target 6) and slight over on principal (target 10) — within tolerance, no rewrites planned.)

## Domain distribution

| Domain bucket | Count | IDs |
|---|---:|---|
| platform-engineering | 1 | 024 |
| ml-platform / ml-data | 3 | 001, 013, 023 |
| mobile-engineering | 2 | 009, 023 (mobile-ml) |
| frontend | 2 | 008, 027 |
| security | 2 | 002, 019 |
| hardware / embedded | 3 | 004, 014, 028 |
| gamedev | 2 | 006, 017 |
| devtools / dev-relations | 3 | 003, 015, 021 |
| healthtech | 2 | 005, 027 |
| edtech | 2 | 008, 028 |
| climate-tech | 3 | 006, 020, 030 |
| govtech | 2 | 016, 024 |
| biotech / pharma-tech | 2 | 010, 013 |
| technical-writing | 1 | 015 |
| research-engineering | 3 | 016, 026, 030 |
| infra-platform | 1 | 012 |
| applied-research | 2 | 010, 026 |
| customer-engineering | 1 | 018 |
| TPM / aerospace | 1 | 011 |
| logistics | 1 | 029 |
| ecommerce / consumer | 2 | 012, 025 |
| consumer-iot / fitness | 1 | 014 |
| robotics | 2 | 004, 026 |
| fintech | 4 | 001, 002, 005, 022 |
| data-engineering | 2 | 005, 022 |

No domain exceeds 4. (Fintech sits at 4 — at the cap.)

## Per-persona summary

| ID | Display | Seniority | Domain (short) | Shape(s) |
|---|---|---|---|---|
| 001 | Rachel K. | principal | ml-platform / adtech | stated-vs-admitted |
| 002 | Marcus T. | vp | security / fintech | title-vs-work |
| 003 | Priya S. | principal | dev-relations / devtools | evidence-light-influence-heavy |
| 004 | David R. | staff | embedded / robotics | sparse-narrative-rich-evidence |
| 005 | Anika B. | director | data-engineering / healthtech | contradictory-praise |
| 006 | Jonas W. | principal | gamedev → climate-tech | domain-pivoter |
| 007 | Elena M. | principal | backend-platform / govtech | burnout-and-return |
| 008 | Tomas H. | staff | frontend / edtech | stated-vs-admitted |
| 009 | Isabela R. | director | mobile / consumer-social | title-vs-work |
| 010 | Yusuf A. | vp | applied-research / pharma-tech | title-vs-work |
| 011 | Leah D. | vp | technical-program-management / aerospace | evidence-light-influence-heavy |
| 012 | Arjun P. | staff | infra-platform / ecommerce | sparse-narrative-rich-evidence |
| 013 | Rebecca L. | principal | ml-data / biotech | contradictory-praise |
| 014 | Felix C. | director | hardware / consumer-iot | domain-pivoter + burnout-and-return |
| 015 | Jin H. | principal | technical-writing / devtools | burnout-and-return |
| 016 | Amara W. | vp | research-engineering / govtech | stated-vs-admitted |
| 017 | Noah B. | principal | gamedev / live-service | title-vs-work |
| 018 | Priya V. | director | customer-engineering / enterprise-saas | evidence-light-influence-heavy |
| 019 | Helena K. | staff | security / fintech | sparse-narrative-rich-evidence |
| 020 | Tariq H. | principal | backend / climate-tech | contradictory-praise |
| 021 | Mira S. | director | dev-relations / api-platform | domain-pivoter |
| 022 | Grace L. | vp | data-engineering / fintech | burnout-and-return |
| 023 | Arnav D. | principal | ml-platform / mobile | stated-vs-admitted |
| 024 | Bea L. | director | platform / govtech | title-vs-work |
| 025 | Omar K. | vp | engineering-management / consumer-mobile | evidence-light-influence-heavy |
| 026 | Zoe M. | principal | research-engineering / robotics-perception | sparse-narrative-rich-evidence |
| 027 | Marisol C. | director | frontend / healthtech | contradictory-praise |
| 028 | Keiko T. | principal | embedded / edtech | domain-pivoter |
| 029 | Anders R. | vp | engineering-management / b2b-saas | evidence-light-influence-heavy |
| 030 | Sara I. | staff | research-engineering / climate-tech | contradictory-praise |

## Notes for BP-014 synthesis

- The 14 hard-case personas cluster on the most-vulnerable F3/F7/F8 calibration territory. Sample these heavily when stress-testing the genericness threshold.
- The two double-shape persona (014) is the only multi-shape file in the synthetic set; gold-001 (Maya C.) and gold-002 (David O.) also carry double-shapes. Consider surfacing whether the topology behaves differently on multi-shape inputs.
- All personas have explicit banned-phrase lists tuned to the persona — these are the load-bearing F3 calibration anchors. The intersection of all banned phrases (the cross-persona "always-banned" list) is the conservative T_g vocabulary; the union is the maximal-banned vocabulary.
