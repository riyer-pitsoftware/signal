# tools/interview — Signal voice-interview workflow

Local voice-interview tool for collecting **gold personas** (BP-005d → BP-005b).
Asks structured questions via local TTS, records the interviewee, transcribes
locally, writes a per-interviewee directory you and your collaborator mark up
to compose the final gold-persona file.

**Everything runs locally. No remote API calls. No telemetry.**

---

## Prerequisites

- Apple Silicon Mac (M1 / M2 / M3 / M4)
- macOS 13+
- Python 3.11+
- `uv` ≥ 0.6 ([install](https://docs.astral.sh/uv/getting-started/installation/))
- A working microphone
- **Headphones strongly recommended** to avoid TTS bleed into recording
- Optional: `brew install espeak-ng` (Kokoro fallback for non-American English voices; not required for default `af_heart`)

## Install

The script uses [PEP 723 inline metadata](https://peps.python.org/pep-0723/), so `uv` resolves and installs deps automatically. No `pip install` step.

```bash
cd tools/interview
uv run run.py --help
```

**First run** will download:
- Whisper large-v3 MLX (~3 GB) → `~/.cache/huggingface/hub`
- Kokoro 82M (~330 MB) → `~/.cache/huggingface/hub`

After download, all subsequent runs are fully offline.

## Usage

```bash
uv run run.py --shape stated-vs-admitted --interviewee maya-r
```

List available shapes:
```bash
uv run run.py --list-shapes --shape any --interviewee any
```

Available shapes (defined in `questions.yaml`):

- `stated-vs-admitted` — stated identity vs admitted self-knowledge
- `title-vs-work` — org-chart role vs work product
- `evidence-light-influence-heavy` — invisible-leverage careers
- `sparse-narrative-rich-evidence` — anti-retrospective speakers
- `contradictory-praise` — competing readings of the same person
- `domain-pivoter` — careers across unrelated domains
- `burnout-and-return` — discontinuities the speaker explains away

### In-session controls

| Phase | Keys |
|---|---|
| Question presented | `[s]peak via TTS` · `[r]ead aloud yourself` · `[n]ext` · `[q]uit` |
| Recording | press `[enter]` to stop |
| After transcript | `[k]eep` · `[e]dit in $EDITOR` · `[r]edo` |

The interviewer chooses the next prompt; the script does not auto-advance through all questions. Skip whatever isn't earning, dwell where the speaker mines gold.

## Output

```
.planning/trd/test-corpus/gold/raw/<interviewee>/
  audio/
    Q01-stated-vs-admitted-opener.wav
    Q02-stated-vs-admitted-probe.wav
    ...
  transcript.md
```

`transcript.md` has one section per question with prompt, intent, audio path, and the auto-transcribed response.

## Next: ground-truth markup (BP-005b)

After the interview:

1. Read `../../.planning/trd/test-corpus/SPEC.md` (the corpus spec).
2. Sit with your collaborator. Read the transcript together.
3. Identify the ground truth: contradictions, load-bearing details, vague claims, evidence anchors.
4. Compose `gold-00X-<pseudo>.md` from the transcript using the template in SPEC.md.
5. The audio + transcript stay local (and may be deleted per consent preference). The fictionalised gold persona file gets committed.

## Privacy

- Audio recording: local file system only.
- Transcription: `mlx-whisper` runs entirely on-device.
- TTS: `kokoro` runs entirely on-device.
- No outbound network calls during a session (after first-time model download).
- Interviewee can request deletion at any time: `rm -rf .planning/trd/test-corpus/gold/raw/<interviewee>/`

## Consent

`CONSENT.md` is the consent form. The script asks for confirmation at session start. Read it with the interviewee before recording.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `No audio device` / silent recording | macOS Settings → Privacy & Security → Microphone → enable Terminal/iTerm |
| Whisper download fails | Briefly connect during first run; subsequent runs are offline |
| TTS sounds robotic / fails | Pass `--no-tts`; read questions yourself |
| Out-of-memory during transcription | Use a smaller model: `--whisper-model mlx-community/whisper-medium-mlx` |
| TTS bleeds into recording | Use headphones; or pass `--no-tts` |
| `RuntimeError: No audio captured` | You pressed enter before speaking; just try again |

## File map

```
tools/interview/
  run.py            # entry point (PEP 723 deps inline)
  questions.yaml    # 33 prompts across 7 shapes
  CONSENT.md        # consent form (sign before recording)
  README.md         # this file
```

No `pyproject.toml`, no `requirements.txt`. Deps live in `run.py`'s header. `uv run` handles the rest.
