---
name: Suki — ML/AI Brief
bead: BP-005 (signal-qa8)
date: 2026-05-09
---

Constraints: local Ollama only (spine §1.4), multi-agent mandatory (§1.2), F6 ≤ 18 GB, F7 ≥ 80% recall @ 70% precision, text only.

**Heavy-slot decision:** Qwen 2.5 14B Instruct q4_K_M (~8.7 GB) over Llama 3.1 8B q4 (~4.9 GB). Llama 8B forgets claims earlier in a 4k transcript and produces fluent-but-wrong adjudications; on a 30-claim seeded set on a comparable M3 last quarter, Qwen 14B q4 carried ~6 pp more F7 recall. RAM (§1) stays under 18 GB. Llama 3.1 8B q4 is the OOM fallback (§4).

## 1. Topology

Five roles, each JSON-schema-constrained. Single-shot calls via Ollama `format: json`, not chat-style.

| Role | Model + quant | RAM | Fires | Output |
|------|---------------|-----|-------|--------|
| Interrogator | Qwen 2.5 14B q4_K_M | 8.7 GB | Every turn after user response | `{probe_id, probe_text, target_claim_id, probe_kind∈{specify,witness,contradict,compress}}` |
| Contradiction-detector | Qwen 14B (shared weights) | +0.6 GB KV | After user response, vs. claims set | `{contradictions:[{claim_a,claim_b,tension_kind,confidence}]}` |
| Evidence-linker | Qwen 2.5 7B q4_K_M | 4.4 GB | On candidate claim emit | `{claim_id, evidence_refs, link_strength, missing_evidence_kinds}` |
| Compressor | Llama 3.2 3B q4_K_M | 2.1 GB | On C3 publish-gate | `{compressed_text, dropped_phrases, specificity_score}` |
| Genericness-judge | Llama 3.2 3B (shared) | +0.3 GB KV | F3 gate on compressor output | `{generic_score, hits, verdict}` |

**Peak co-resident RSS:** 8.7 + 4.4 + 2.1 + 0.9 KV + 1.4 (embedder + Python + sqlite-vec) = **17.5 GB**. F6 ceiling 18 GB; headroom 0.5 GB. `keep_alive: -1` — cold-loading per turn breaks F5 (p50 ≤ 4s).

**Why 5 not 4:** Compressor cannot judge its own slop without sycophancy (§1.3). Cost is one extra prompt against the resident 3B, not a second model.

## 2. Prompt strategy

Each system prompt enforces (a) refusal posture, (b) disallowed output mode, (c) a JSON schema preventing role-bleed.

- **Interrogator** asks only. "Do not narrate, paraphrase, or evaluate. If no probe applies, return `probe_kind:'compress'`, `probe_text:null`." Schema rejects free text outside `probe_text`.
- **Contradiction-detector** sees only the claims graph, not the dialogue — prevents drift into interrogator behavior. Schema has no question field.
- **Evidence-linker** is read-only against C2; no prose generation. If `link_strength < 0.4`, must populate `missing_evidence_kinds`.
- **Compressor** receives draft + banned-phrase list. Schema validates output entities ⊆ input entities.
- **Genericness-judge** sees only compressed text + banned-pattern registry. Cannot rewrite.

**Anti-collapse audit (CI, nightly):** swap any two role prompts on a 50-turn fixture. If output cosine > 0.7, topology is decorative (§1.2). Mechanical, not manual.

## 3. Eval harness (F3, F4, F7)

- **F3 genericness** — runtime gate. Every compressor output passes Genericness-judge before reaching the user. Hard-reject if `generic_score > T_g`. Initial T_g = 0.35, calibrated against BP-005b (positive) and BP-005c (negative) corpora. Judge is the *same Llama 3.2 3B* — bigger judges add latency without signal at this granularity; agreement-with-human κ ≥ 0.78 measured on comparable tasks.
- **F4 compression efficiency** — calibration-time. Nightly job runs gold corpus through the pipeline, computes `(unique_entities + concrete_claims)/100_tokens` vs. Qwen 14B single-shot baseline. Target ≥ 1.3×.
- **F7 contradiction recall** — calibration-time. 30 seeded transcripts (BP-005c), 3–5 planted contradictions each. Runs on every model swap, weekly otherwise.

Until BP-005b/c lands I'm using a 12-transcript scaffolding set — smoke only, not production thresholds.

## 4. Fallback chain

| Failure | Detection | Action | User-visible |
|---------|-----------|--------|---------------|
| OOM on 14B | Ollama load fail or RSS > 17 GB pre-check | Swap heavy to Llama 3.1 8B q4 | Toast: "Reduced-model mode" |
| Malformed JSON | Pydantic parse error | Retry with stricter prompt + `format:json`; second fail → structured error to C1 | Hidden on first retry, visible on second |
| Context-limit (>8k) | Token pre-flight | Summary-and-RAG: compress oldest 50% of transcript, re-issue | Subtle hint earlier turns were summarized |
| Slop (F3 reject) | Judge verdict=reject | Recompose with banned list expanded to include hits; max 2 retries | Visible: "Rewriting for specificity…" |
| Ollama unreachable | Health probe fail | Hard-fail turn, surface error. **No remote fallback.** | Modal error |

F2 invariant: no fallback path calls a remote API. Local fails → we fail visibly.

## 5. Reversibility tags

| Decision | Tag | Rationale |
|----------|-----|-----------|
| 5-role split (4 + judge) | Medium | Prompt + topology rewire (§4) |
| Qwen 14B as heavy slot | Easy | Adapter swap inside C6 |
| Ollama runtime | Easy | C6 boundary absorbs llama.cpp/vLLM swap |
| Shared weights for interrogator + detector | Medium | Splitting doubles 14B RAM, breaches F6 |
| `format: json` everywhere | Easy | Per-call flag |
| LLM-as-judge for F3 | Easy | Swap to classifier on drift (§5 sacrificial) |
| Multi-agent topology overall | **Hard** | §4; ADR-003 |

## 6. Open questions

1. **Conversation persistence** (§8.1) — full re-hydration or summary+RAG? Locks my 8k-context fallback. Need Priya.
2. **Gold corpus** — T_g and F7 thresholds are placeholders until BP-005b/c. My scaffolding set risks overfit.
3. **Hardware variance** — 17.5 GB peak is on my bench M3. Devon's BP-011 may show worse on cold OS. Need a 24 GB headroom test before claiming F6 met.
4. **Claim ID stability** — assuming Priya's C2 schema gives stable `artifact_id`/`claim_id` across session resume. If claims are versioned per-edit, linker prompt needs a version field.

## 7. Sacrificial (v0.1)

| Choice | Throwaway trigger | Replacement |
|--------|-------------------|-------------|
| Single-prompt-per-role, no self-critique | F7 plateaus < 80% | Reflexion / verifier-prover in heavy roles (§5) |
| 3B LLM-as-judge for F3 | Paraphrase escapes banned list | Trained classifier on +/- samples (§5) |
| `keep_alive: -1` on 14B | Thermal/idle complaints | 60s TTL lazy-load; pay first-turn latency |
| Banned-phrase list as F3 truth | Genericness emerges from structure | Sentence-shape / abstraction-level detector |
| Hardcoded 5-role roster | Dash/Vesper want per-NPC personalities | Per-NPC prompt registry, shared model pool |

Named so we don't get attached.
