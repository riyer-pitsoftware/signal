#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "click>=8.1",
#     "PyYAML>=6.0",
#     "sounddevice>=0.4",
#     "soundfile>=0.12",
#     "numpy>=1.26",
#     "mlx-whisper>=0.4",
#     "kokoro>=0.7",
# ]
# ///
"""Signal voice-interview tool — gold-persona collection (BP-005d → BP-005b).

Workflow per prompt:
  1. Display question (depth + intent)
  2. [s]peak via Kokoro TTS / [r]ead aloud yourself / [n]ext / [q]uit
  3. After question delivered: [r]ecord / [s]kip / [q]uit
  4. While recording: press [enter] to stop
  5. mlx-whisper transcribes locally; review
  6. [k]eep / [e]dit in $EDITOR / [r]edo

All processing local. See README.md and CONSENT.md.
"""

from __future__ import annotations

import os
import sys
import threading
import tempfile
import subprocess
from datetime import datetime
from pathlib import Path

import click
import numpy as np
import sounddevice as sd
import soundfile as sf
import yaml

QUESTIONS_FILE = Path(__file__).parent / "questions.yaml"
DEFAULT_OUTPUT_BASE = (
    Path(__file__).resolve().parent.parent.parent
    / ".planning" / "trd" / "test-corpus" / "gold" / "raw"
)
SAMPLE_RATE = 24000  # match Kokoro output for simplicity
WHISPER_MODEL_DEFAULT = "mlx-community/whisper-large-v3-mlx"
WHISPER_MODEL_FALLBACK = "mlx-community/whisper-medium-mlx"
KOKORO_VOICE = "af_heart"
KOKORO_LANG = "a"  # American English


# ---------- CLI ----------

@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--shape", required=True, help="Persona shape ID from questions.yaml")
@click.option("--interviewee", required=True, help="Pseudonym, e.g. 'gold-003' or 'maya-r'")
@click.option("--output-dir", default=None, help="Override default output dir")
@click.option("--no-tts", is_flag=True, help="Skip TTS — interviewer reads questions aloud")
@click.option("--whisper-model", default=WHISPER_MODEL_DEFAULT,
              help=f"HF model id (default: {WHISPER_MODEL_DEFAULT}; smaller: {WHISPER_MODEL_FALLBACK})")
@click.option("--list-shapes", is_flag=True, help="List available shapes and exit")
def main(shape, interviewee, output_dir, no_tts, whisper_model, list_shapes):
    questions_data = load_questions_or_die(shape, list_only=list_shapes)
    out = setup_output(interviewee, output_dir)
    print_banner(shape, questions_data, interviewee, out)

    confirm_consent_or_abort()

    print("\nLoading Whisper... (first run downloads ~3 GB)")
    from mlx_whisper import transcribe as whisper_transcribe

    tts_pipe = None
    if not no_tts:
        print("Loading Kokoro... (first run downloads ~330 MB)")
        from kokoro import KPipeline
        tts_pipe = KPipeline(lang_code=KOKORO_LANG)

    transcript_path = out / "transcript.md"
    write_transcript_header_if_new(transcript_path, shape, interviewee, questions_data["name"])

    questions = questions_data["questions"]
    idx = 0
    while idx < len(questions):
        q = questions[idx]
        idx_str = f"Q{idx + 1:02d}"

        action = prompt_present(q, idx_str, len(questions))
        if action == "quit":
            break
        if action == "next":
            idx += 1
            continue

        if action == "speak" and tts_pipe is not None:
            speak(tts_pipe, q["prompt"])
        elif action == "read":
            input(f"\n  Read aloud, then press enter:\n  > {q['prompt'].strip()}\n  ")

        rec_action = prompt_record()
        if rec_action == "skip":
            idx += 1
            continue
        if rec_action == "quit":
            break

        audio_path = out / "audio" / f"{idx_str}-{shape}-{q['depth']}.wav"
        try:
            record_audio(audio_path)
        except Exception as e:
            click.echo(f"  Recording error: {e}", err=True)
            continue

        click.echo("  Transcribing...")
        try:
            result = whisper_transcribe(str(audio_path), path_or_hf_repo=whisper_model)
            text = result["text"].strip()
        except Exception as e:
            click.echo(f"  Whisper error: {e}", err=True)
            click.echo("  Audio is saved; you can retry transcription later.", err=True)
            text = "[TRANSCRIPTION FAILED — see audio file]"

        click.echo(f"\n  --- transcript ---\n  {text}\n  --- /transcript ---\n")

        keep_action = prompt_keep()
        if keep_action == "redo":
            audio_path.unlink(missing_ok=True)
            continue  # don't increment
        if keep_action == "edit":
            text = edit_in_editor(text)

        append_to_transcript(transcript_path, idx_str, q, text, audio_path.relative_to(out))
        idx += 1

    click.echo(f"\nInterview saved to {out}")
    click.echo("Next: read transcript.md, mark up ground truth, compose gold-XXX.md per SPEC.md.")


# ---------- helpers ----------

def load_questions_or_die(shape_id: str, list_only: bool):
    with open(QUESTIONS_FILE) as f:
        data = yaml.safe_load(f)
    if list_only:
        click.echo("Available shapes:")
        for s in data["shapes"]:
            click.echo(f"  {s['id']:32s} {s['name']}")
        sys.exit(0)
    for shape in data["shapes"]:
        if shape["id"] == shape_id:
            return shape
    available = [s["id"] for s in data["shapes"]]
    raise click.BadParameter(f"Unknown shape '{shape_id}'. Available: {available}")


def setup_output(interviewee: str, override: str | None) -> Path:
    base = Path(override) if override else DEFAULT_OUTPUT_BASE
    out = base / interviewee
    (out / "audio").mkdir(parents=True, exist_ok=True)
    return out


def print_banner(shape: str, qdata: dict, interviewee: str, out: Path):
    click.echo("\n=== Signal voice interview ===")
    click.echo(f"Shape:        {shape}  ({qdata['name']})")
    click.echo(f"Interviewee:  {interviewee}")
    click.echo(f"Questions:    {len(qdata['questions'])}")
    click.echo(f"Output:       {out}")
    click.echo(f"\nFor each prompt: [s]peak via TTS / [r]ead aloud yourself / [n]ext / [q]uit")
    click.echo("While recording: press [enter] to stop")
    click.echo("After transcript: [k]eep / [e]dit in $EDITOR / [r]edo\n")


def confirm_consent_or_abort():
    answer = input("Has the interviewee read and signed CONSENT.md? [y/N]: ").strip().lower()
    if answer != "y":
        click.echo("Aborting. See tools/interview/CONSENT.md.")
        sys.exit(1)


def prompt_present(q: dict, idx_str: str, total: int) -> str:
    click.echo(f"\n[{idx_str}/{total:02d}] depth={q['depth']}  intent={q['intent'][:80]}")
    click.echo(f"  > {q['prompt'].strip()}")
    while True:
        choice = input("  [s]peak / [r]ead / [n]ext / [q]uit: ").strip().lower()
        if choice in ("s", "speak"): return "speak"
        if choice in ("r", "read"):  return "read"
        if choice in ("n", "next"):  return "next"
        if choice in ("q", "quit"):  return "quit"


def prompt_record() -> str:
    while True:
        choice = input("  [r]ecord / [s]kip / [q]uit: ").strip().lower()
        if choice in ("r", "record"): return "record"
        if choice in ("s", "skip"):   return "skip"
        if choice in ("q", "quit"):   return "quit"


def prompt_keep() -> str:
    while True:
        choice = input("  [k]eep / [e]dit / [r]edo: ").strip().lower()
        if choice in ("k", "keep"): return "keep"
        if choice in ("e", "edit"): return "edit"
        if choice in ("r", "redo"): return "redo"


def edit_in_editor(text: str) -> str:
    editor = os.environ.get("EDITOR", "nano")
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(text)
        path = f.name
    subprocess.call([editor, path])
    with open(path) as f:
        edited = f.read().strip()
    os.unlink(path)
    return edited


def speak(pipe, text: str):
    click.echo("  (speaking...)")
    generator = pipe(text, voice=KOKORO_VOICE)
    for _, _, audio in generator:
        sd.play(np.asarray(audio), samplerate=24000, blocking=True)


def record_audio(path: Path):
    click.echo("  Recording — press [enter] to stop")
    chunks: list[np.ndarray] = []

    def callback(indata, frames, time_info, status):
        if status:
            click.echo(f"  ({status})", err=True)
        chunks.append(indata.copy())

    stream = sd.InputStream(
        samplerate=SAMPLE_RATE, channels=1, callback=callback, dtype="float32"
    )
    with stream:
        input()  # block until enter

    if not chunks:
        raise RuntimeError("No audio captured")
    audio = np.concatenate(chunks, axis=0)
    sf.write(str(path), audio, SAMPLE_RATE)
    duration = len(audio) / SAMPLE_RATE
    click.echo(f"  Saved {duration:.1f}s → {path.name}")


def write_transcript_header_if_new(path: Path, shape: str, interviewee: str, shape_name: str):
    if path.exists():
        return
    with open(path, "w") as f:
        f.write(f"# Interview transcript — {interviewee}\n\n")
        f.write(f"- shape: {shape} ({shape_name})\n")
        f.write(f"- date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"- audio: ./audio/\n\n")
        f.write("---\n\n")


def append_to_transcript(path: Path, idx_str: str, q: dict, text: str, audio_rel: Path):
    with open(path, "a") as f:
        f.write(f"## {idx_str} — {q['depth']}\n\n")
        f.write(f"**Prompt:** {q['prompt'].strip()}\n\n")
        f.write(f"**Intent:** {q['intent']}\n\n")
        f.write(f"**Audio:** `{audio_rel}`\n\n")
        f.write(f"**Response:**\n\n")
        f.write(f"{text}\n\n")
        f.write("---\n\n")


if __name__ == "__main__":
    main()
