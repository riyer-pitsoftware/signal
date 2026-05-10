---
name: Devon — DevOps Brief
bead: BP-011 (signal-iep)
date: 2026-05-09
---

# Round A — local packaging, sizing, privacy verification

Constraints up front: local-only by construction (spine §1.4), F2 zero outbound bytes (§3, hard), F6 peak RSS ≤ 18 GB on 24 GB M3 (§3, hard), no Terraform, GitHub Actions lint+test only.

## 1. Packaging

Two paths. Native is primary; Docker is secondary.

- **Native install script** (`scripts/install.sh`, ~150 lines): detects macOS/Linux, installs Ollama via official installer, pulls Suki's model registry (Qwen 2.5 14B q4, 7B q4, Llama 3.2 3B q4, `nomic-embed-text`, plus Llama 3.1 8B q4 fallback), creates `~/.signal/`, runs `uv sync` for backend, `pnpm i && pnpm build` for frontend. ~22 GB models + ~400 MB code. Runs as user, no root, no daemon.
- **docker-compose.yml**: services `ollama` (image `ollama/ollama:0.4`), `backend` (FastAPI + sqlite-vec, mounts `./signal_data`), `frontend-dev` (Vite, profile `dev` only), named volume `signal-sqlite`. Image footprint ~3.1 GB plus models pulled into Ollama volume.

**Pros native:** Metal acceleration on M3 — Suki's 16.6 GB measurement assumed Metal; Docker on macOS loses Metal and breaches F6. **Pros Docker:** reproducible, single command, Linux GPU passthrough clean. **Primary v0.1: native.** Docker is for Linux contributors and CI.

## 2. Hardware sizing matrix

| Tier | Co-resident models | Behavior | p50 turn | Experience |
|------|--------------------|----------|---------|-----------|
| 8 GB | None (OS+browser+IDE leaves <1.5 GB) | Refuse to launch | n/a | Unsupported |
| 16 GB | Llama 3.1 8B (4.9) + 7B (4.4) + 3B (2.1) = 11.4 GB | Degraded; F7 recall −6 pts (Suki §0) | 6–8s | Works; recall warning shown |
| 24 GB (primary) | Qwen 14B (8.7) + 7B (4.4) + 3B (2.1) + embedder/runtime (1.4) = 16.6 GB | Full per Suki §1; F6 met, 1.4 GB headroom | ≤ 4s | Full |
| 32 GB | As 24 GB; surplus to KV cache (8k → 16k context) | Full + longer transcript before summary-and-RAG | ≤ 3s | Full + longer sessions |
| 64 GB | Co-load Qwen 14B and Llama 3.1 8B | Full + zero-cost fallback swap | ≤ 3s | Full + invisible degradation |

**8 GB resolution: NO.** Floor is 16 GB. At 8 GB the OS + browser + IDE leaves <1.5 GB; even the 3B fallback (2.1 GB) cannot co-reside with the 7B linker, and a single-model topology violates spine §1.2. Installer hard-checks `sysctl hw.memsize` / `/proc/meminfo` and refuses below 16 GB. No "lite mode" — degrading further yields a single-LLM chat product, the thing the spine says we are not building.

## 3. Privacy verification (F2)

CI test (`tests/privacy/test_f2_no_egress.py`, every PR, GitHub Actions Linux runner):

1. Compose stack on a Docker network with `--internal` (no NAT, no default gateway).
2. Observer container runs `tcpdump -i any -w capture.pcap` on the host bridge.
3. Harness drives a 90-turn scripted session: 30 probes, 20 evidence placements, 5 publishes. ~90s wallclock.
4. Assertion: capture filtered against an allowlist (127.0.0.0/8, ::1, Docker bridge, local DNS) yields **0 bytes** to any non-loopback peer. Bytes > 0 = PR blocked.
5. Backstop: `lsof -i -n -P` snapshots every 10s show no `ESTABLISHED` to non-loopback from `backend`/`ollama` PIDs.

**Runtime guard (production, native):** macOS `pf` rule installed at first run drops outbound TCP/UDP from the backend's UID to anything but loopback. Linux equivalent via `nftables` chain `signal_egress_drop` policy `drop` for the backend's UID. Defense-in-depth — primary mechanism is "no code path opens a non-loopback socket"; the guard makes that auditable.

## 4. Audit log schema

Two stores, one schema. **No event captures user prose.** Probe text, response text, narrative text never enter the audit log.

SQLite table `audit_events` in `signal.db`: `id INTEGER PK`, `ts TEXT ISO8601`, `session_id TEXT`, `event TEXT`, `actor TEXT` (`user|interrogator|linker|compressor|judge|system`), `payload_json TEXT` (counts, IDs, scores — no prose), `model_id TEXT NULL`, `latency_ms INTEGER NULL`. JSONL mirror at `~/.signal/audit/YYYY-MM-DD.jsonl`, append-only, identical fields. Mirror exists so DB corruption doesn't lose history.

Events: `session.start`, `session.end`, `probe.asked`, `response.received`, `evidence.placed`, `claim.published`, `contradiction.surfaced`, `model.oom`, `model.fallback`, `f2.guard.tripped`, `f3.reject`. Payload is metadata only — `{probe_id, probe_kind, target_claim_id}` not the probe text; `{token_count, response_id}` not the response.

Retention: 90-day rolling, user-controlled (`signal audit purge`). Reader: local user only; file mode 0600, DB file 0600. No external reader, no telemetry export.

## 5. Secrets

**No secrets in v0.1.** Affirmative inventory: no API keys (no remote LLM), no DB password (SQLite + OS file perms), no third-party tokens, no signing keys, no OAuth. Threat model is the user's own machine; defense is file permissions and the F2 invariant. No `.env` ships; `.gitignore` blocks commit; pre-commit `detect-secrets` blocks accidental check-in.

**v0.2 cloud sync would change this:** introduces sync token, server URL, end-to-end encryption keys. That re-opens spine §1.4 and is a separate ADR — not a config toggle.

## 6. Degradation below floor

Installer refuses below 16 GB. No lite mode, no offline-corpus-only, no single-LLM mode. Rationale: a single-agent product violates spine §1.2 and ships the slop the spine exists to prevent. Better to refuse than ship a degraded product the user blames for being bad.

## 7. CI/CD

`.github/workflows/ci.yml`, Linux runners, three parallel jobs: `lint` (ruff + pyright + eslint + tsc), `test` (pytest + vitest), `f2_privacy` (§3). On `main`, fourth job `build_artifact` produces `signal-vX.Y.Z.tgz` (backend wheel, frontend `dist/`, install script, model manifest), attached to the GitHub Release. **No deploy step. No registry push.**

## 8. Reversibility tags

| Decision | Tag | Rationale |
|----------|-----|-----------|
| Native install primary | Easy | Flip if Metal-in-Docker lands |
| 16 GB floor | Medium | Installer + addressable-user math (spine §4) |
| SQLite + JSONL dual audit | Easy | Drop JSONL on disk pressure |
| `pf`/`nftables` runtime guard | Easy | Remove if F2 CI proves sufficient |
| GH Actions lint+test only | Easy | Add deploy if v0.2 ships a server |
| Local-only posture | Hard | Spine §1.4; ADR-004 |

## 9. Open questions

- **Priya:** SQLite volume sizing — per-session row count and bytes-per-row for `claims`, `artifacts`, `links`, `narrative_versions`? Placeholder is 200 MB/year/user; need this to size the volume and set audit retention defensibly.
- **Suki:** confirm 16.6 GB peak holds with `keep_alive: -1` after a 4-hour session (KV cache growth). If it climbs past 17.5 GB the OOM trigger fires earlier.
- **Spine §8.1:** if persistence is summary+RAG not full re-hydration, the 32 GB tier value drops — call out in ADR.

## 10. Sacrificial choices

| Choice | Trigger | Replacement |
|--------|---------|-------------|
| Native script as primary | Docker on macOS gains Metal | Flip primary to compose |
| 16 GB floor | 8 GB M-series remains majority by v0.2 | Per-NPC model selection, runtime topology shrink |
| 90-day audit retention | Users want longer self-review history | User-set retention + encrypted export |
| UID-scoped `pf`/`nftables` drop | Windows support added | Per-process namespace + WFP rule |

Named so we don't get attached.
