# tools/interview — Signal voice-interview workflow

Local voice-interview tool for collecting **gold personas** (BP-005d → BP-005b → BP-005e).
Asks structured questions via local TTS, records the interviewee, transcribes
locally, writes a per-interviewee directory you and your collaborator mark up
to compose the final gold-persona file.

**Everything runs locally. No remote API calls. No telemetry.**

Two front-ends:
- **Web UI** (`serve.py` — preferred for non-CLI users; BP-005e). Browser at `http://localhost:8765`.
- **CLI** (`run.py` — original; useful for automation). Same backend, same output format.

Both use `questions.yaml`, `mlx-whisper`, Kokoro TTS, and write to `.planning/trd/test-corpus/gold/raw/<interviewee>/` with the same `transcript.md` format.

---

## Quickstart — Web UI (recommended; BP-005e)

```bash
cd /Users/riyer/code/signal/tools/interview
uv run serve.py
```

Then open `http://localhost:8765` in any browser.

The UI walks the operator + interviewee through:
1. Consent confirmation (must check box; links to `CONSENT.md`)
2. Shape picker (each shape shows description + which fitness function it primarily tests)
3. Interviewee pseudonym entry
4. Per-question loop: speak via TTS / read aloud yourself / record / review transcript / keep / redo / skip / quit
5. Done summary + reminder of the markup workflow

### One-time pre-flight

1. **Headphones on.** TTS bleed is the main reason for them. Or click "I'll read it aloud myself" instead of "Speak via TTS."
2. **Browser mic permission.** First time you click "Record," the browser asks. Allow.
3. **Sign `CONSENT.md` with the interviewee.** UI requires you to confirm this with a checkbox.
4. **First run downloads ~3.3 GB** (Whisper large-v3 + Kokoro). One-time. After that fully offline.

### Privacy posture (same as CLI)

- Server binds to `127.0.0.1` only — never `0.0.0.0`. Localhost-only by design.
- Browser audio capture (`MediaRecorder`) → uploaded to local FastAPI server → mlx-whisper transcribes locally → file written to disk.
- No network calls leave the machine after first-run model download.
- F2 zero-outbound posture preserved.

### Audio file format

Browser-captured audio is saved as `.webm/opus`. The CLI captures `.wav`. Whisper handles both via its underlying ffmpeg path. The `transcript.md` format is identical.

### Output

```
.planning/trd/test-corpus/gold/raw/<interviewee>/
  audio/
    Q01-<shape>-opener.webm    (UI captures) OR .wav (CLI captures)
    Q02-<shape>-probe.webm
    ...
  transcript.md                (same format both front-ends)
```

### Troubleshooting (UI)

| Symptom | Fix |
|---|---|
| "Mic permission denied" in browser | Browser settings → Site Settings → `localhost:8765` → Microphone: Allow |
| TTS doesn't play | Browser autoplay policy; click anywhere on the page first, then retry |
| Whisper takes 30+ seconds for short clips | First-time model load. Subsequent transcriptions are faster. |
| Server won't start (port in use) | `SIGNAL_INTERVIEW_PORT=8766 uv run serve.py` |

---

## Quickstart — CLI (BP-005d, original)

The CLI is preserved as fallback for automation or headless use. Same backend, same output format.

There is no GUI. The script uses your **system default microphone** (whatever macOS has selected in System Settings → Sound → Input). No in-script device picker.

### One-time pre-flight

1. **Headphones on.** TTS bleeds into the mic without them. Alternative: pass `--no-tts` and read questions yourself.
2. **Mic permission.** macOS Settings → Privacy & Security → Microphone → enable your terminal app (Terminal / iTerm / Ghostty / etc.).
3. **Pick the right input.** macOS Settings → Sound → Input → confirm the mic you want is selected (built-in vs USB vs AirPods). Script has no override.
4. **Sign CONSENT.md with the interviewee.** Script asks `[y/N]` at session start — `n` aborts.
5. **First run downloads ~3.3 GB** (Whisper large-v3 + Kokoro). One-time; subsequent runs are fully offline.

### Per-session command

```bash
cd /Users/riyer/code/signal/tools/interview
uv run run.py --shape stated-vs-admitted --interviewee gold-003
```

Replace the shape and the pseudonym. List shapes: `uv run run.py --list-shapes --shape any --interviewee any`. Seven shapes are defined — pick the one that matches the interviewee's career arc.

### In-session keys

| Phase | Keys |
|---|---|
| Question shown | `[s]peak via TTS` · `[r]ead aloud yourself` · `[n]ext` · `[q]uit` |
| Ready to record | `[r]ecord` · `[s]kip` · `[q]uit` |
| Recording (live) | press **`[enter]`** to stop |
| After transcript | `[k]eep` · `[e]dit in $EDITOR` · `[r]edo` |

Skip prompts that aren't earning. Dwell where the speaker mines gold. Script does NOT auto-advance through all 33 prompts — you steer.

### Output

```
.planning/trd/test-corpus/gold/raw/gold-003/
  audio/Q01-stated-vs-admitted-opener.wav
  audio/Q02-...
  transcript.md
```

### After the session (the actual BP-005b deliverable)

Recordings are inputs, not the deliverable. Read `../../.planning/trd/test-corpus/SPEC.md`, then sit with your collaborator and:
1. Read the transcript together.
2. Mark up ground truth: contradictions, load-bearing details, vague claims, evidence anchors.
3. Compose `gold-00X-<pseudo>.md` per the SPEC.md template.

Calibrate against the two samples already at `.planning/trd/test-corpus/gold/gold-001-maya-c.md` and `gold-002-david-o.md` — read those first.

Audio + raw transcript stay local and can be deleted per consent preference. **Only the fictionalised gold persona file gets committed.**

### If something goes wrong

| Symptom | Fix |
|---|---|
| Silent recording / `No audio device` | Mic permission for terminal (step 2 above) |
| `RuntimeError: No audio captured` | You hit enter before speaking — retry |
| TTS bleeds into recording | Headphones, or `--no-tts` |
| OOM during transcription | `--whisper-model mlx-community/whisper-medium-mlx` |
| TTS robotic / fails | `--no-tts`, read questions yourself |
| Wrong mic capturing audio | Change macOS Settings → Sound → Input |

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
