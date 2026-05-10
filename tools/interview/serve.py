#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "fastapi>=0.110",
#     "uvicorn[standard]>=0.29",
#     "python-multipart>=0.0.9",
#     "PyYAML>=6.0",
#     "numpy>=1.26",
#     "soundfile>=0.12",
#     "mlx-whisper>=0.4",
#     "kokoro>=0.7",
# ]
# ///
"""Signal voice-interview tool — FastAPI server (BP-005e).

Web UI replacement for tools/interview/run.py CLI. Same backend stack
(mlx-whisper, Kokoro, questions.yaml). Browser captures audio via
MediaRecorder API; server transcribes; transcripts saved in CLI-compatible
format under .planning/trd/test-corpus/gold/raw/<interviewee>/.

Run:
    cd tools/interview && uv run serve.py

Then open http://localhost:8765 in a browser.

Privacy posture: server binds to 127.0.0.1 only. F2 zero-outbound posture
preserved. No telemetry. Same as CLI tool.
"""

from __future__ import annotations

import io
import os
import sys
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import soundfile as sf
import yaml
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

HERE = Path(__file__).resolve().parent
QUESTIONS_FILE = HERE / "questions.yaml"
WEB_DIR = HERE / "web"
DEFAULT_OUTPUT_BASE = (
    HERE.parent.parent / ".planning" / "trd" / "test-corpus" / "gold" / "raw"
)
WHISPER_MODEL_DEFAULT = "mlx-community/whisper-large-v3-mlx"
KOKORO_VOICE = "af_heart"
KOKORO_LANG = "a"

app = FastAPI(title="Signal voice interview")

# ---------- in-memory session store ----------

# Single-process, single-user. Map session_id → dict.
_sessions: dict[str, dict[str, Any]] = {}

# Lazy-loaded ML
_whisper_imported = False
_kokoro_pipe = None


def _ensure_whisper():
    global _whisper_imported
    if not _whisper_imported:
        # mlx-whisper is imported on demand to avoid loading the model at server start
        import mlx_whisper  # noqa: F401
        _whisper_imported = True


def _ensure_kokoro():
    global _kokoro_pipe
    if _kokoro_pipe is None:
        from kokoro import KPipeline
        _kokoro_pipe = KPipeline(lang_code=KOKORO_LANG)
    return _kokoro_pipe


# ---------- shape loading ----------

def _load_questions_data() -> dict[str, Any]:
    with open(QUESTIONS_FILE) as f:
        return yaml.safe_load(f)


def _find_shape(shape_id: str) -> dict[str, Any]:
    data = _load_questions_data()
    for s in data["shapes"]:
        if s["id"] == shape_id:
            return s
    raise HTTPException(status_code=404, detail=f"Unknown shape: {shape_id}")


# ---------- session helpers ----------

def _setup_output(interviewee: str) -> Path:
    out = DEFAULT_OUTPUT_BASE / interviewee
    (out / "audio").mkdir(parents=True, exist_ok=True)
    return out


def _write_transcript_header_if_new(path: Path, shape: str, interviewee: str, shape_name: str):
    if path.exists():
        return
    with open(path, "w") as f:
        f.write(f"# Interview transcript — {interviewee}\n\n")
        f.write(f"- shape: {shape} ({shape_name})\n")
        f.write(f"- date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"- audio: ./audio/\n\n")
        f.write("---\n\n")


def _append_to_transcript(path: Path, idx_str: str, q: dict, text: str, audio_rel: Path):
    with open(path, "a") as f:
        f.write(f"## {idx_str} — {q['depth']}\n\n")
        f.write(f"**Prompt:** {q['prompt'].strip()}\n\n")
        f.write(f"**Intent:** {q['intent']}\n\n")
        f.write(f"**Audio:** `{audio_rel}`\n\n")
        f.write(f"**Response:**\n\n")
        f.write(f"{text}\n\n")
        f.write("---\n\n")


def _get_session(session_id: str) -> dict[str, Any]:
    if session_id not in _sessions:
        raise HTTPException(status_code=404, detail=f"Unknown session: {session_id}")
    return _sessions[session_id]


# ---------- request models ----------

class SessionStartRequest(BaseModel):
    shape: str
    interviewee: str
    consent_confirmed: bool


class KeepRequest(BaseModel):
    transcript: str


# ---------- API endpoints ----------

@app.get("/api/shapes")
def list_shapes() -> list[dict[str, Any]]:
    """List all shapes with descriptions and primary-tests."""
    data = _load_questions_data()
    return [
        {
            "id": s["id"],
            "name": s["name"],
            "description": s.get("description", "").strip(),
            "primary_tests": s.get("primary-tests", []),
            "question_count": len(s.get("questions", [])),
        }
        for s in data["shapes"]
    ]


@app.post("/api/sessions")
def start_session(req: SessionStartRequest) -> dict[str, Any]:
    """Initialize a new session."""
    if not req.consent_confirmed:
        raise HTTPException(
            status_code=400,
            detail="Consent must be confirmed (CONSENT.md signed) before starting.",
        )
    if not req.interviewee or not req.interviewee.replace("-", "").replace("_", "").isalnum():
        raise HTTPException(
            status_code=400,
            detail="Interviewee pseudonym must be alphanumeric (hyphens/underscores ok).",
        )

    shape = _find_shape(req.shape)
    out = _setup_output(req.interviewee)
    transcript_path = out / "transcript.md"
    _write_transcript_header_if_new(transcript_path, req.shape, req.interviewee, shape["name"])

    session_id = uuid.uuid4().hex[:12]
    _sessions[session_id] = {
        "shape_id": req.shape,
        "shape_name": shape["name"],
        "interviewee": req.interviewee,
        "questions": shape["questions"],
        "current_idx": 0,
        "out_dir": str(out),
        "transcript_path": str(transcript_path),
        "completed": [],  # list of idx that have been kept/skipped
    }
    return {
        "session_id": session_id,
        "shape": shape["name"],
        "interviewee": req.interviewee,
        "total_questions": len(shape["questions"]),
        "out_dir": str(out),
    }


@app.get("/api/sessions/{session_id}/state")
def session_state(session_id: str) -> dict[str, Any]:
    s = _get_session(session_id)
    return {
        "shape_id": s["shape_id"],
        "shape_name": s["shape_name"],
        "interviewee": s["interviewee"],
        "current_idx": s["current_idx"],
        "total": len(s["questions"]),
        "completed": s["completed"],
        "done": s["current_idx"] >= len(s["questions"]),
    }


@app.get("/api/sessions/{session_id}/question")
def current_question(session_id: str) -> dict[str, Any]:
    s = _get_session(session_id)
    idx = s["current_idx"]
    if idx >= len(s["questions"]):
        raise HTTPException(status_code=409, detail="Session complete; no current question.")
    q = s["questions"][idx]
    return {
        "idx": idx,
        "idx_str": f"Q{idx + 1:02d}",
        "depth": q["depth"],
        "prompt": q["prompt"].strip(),
        "intent": q["intent"],
        "total": len(s["questions"]),
    }


@app.post("/api/sessions/{session_id}/tts")
def tts(session_id: str) -> Response:
    """Speak the current prompt via Kokoro and return WAV bytes."""
    s = _get_session(session_id)
    idx = s["current_idx"]
    if idx >= len(s["questions"]):
        raise HTTPException(status_code=409, detail="Session complete.")
    q = s["questions"][idx]

    pipe = _ensure_kokoro()
    chunks: list[np.ndarray] = []
    for _, _, audio in pipe(q["prompt"], voice=KOKORO_VOICE):
        chunks.append(np.asarray(audio))
    if not chunks:
        raise HTTPException(status_code=500, detail="TTS produced no audio.")
    full = np.concatenate(chunks, axis=0)

    buf = io.BytesIO()
    sf.write(buf, full, 24000, format="WAV", subtype="PCM_16")
    buf.seek(0)
    return Response(content=buf.read(), media_type="audio/wav")


@app.post("/api/sessions/{session_id}/record")
async def record(session_id: str, audio: UploadFile = File(...)) -> dict[str, Any]:
    """Accept uploaded audio, transcribe via mlx-whisper, return transcript.

    Audio is saved to disk under audio/ but NOT yet committed to transcript.md.
    Commit happens on /keep. If user redoes, the audio file gets overwritten.
    """
    s = _get_session(session_id)
    idx = s["current_idx"]
    if idx >= len(s["questions"]):
        raise HTTPException(status_code=409, detail="Session complete.")
    q = s["questions"][idx]
    out_dir = Path(s["out_dir"])

    # Browser MediaRecorder typically delivers webm/opus. Save as .webm; whisper handles via ffmpeg.
    suffix = ".webm" if (audio.content_type or "").endswith("webm") else ".wav"
    audio_filename = f"Q{idx + 1:02d}-{s['shape_id']}-{q['depth']}{suffix}"
    audio_path = out_dir / "audio" / audio_filename

    content = await audio.read()
    if not content:
        raise HTTPException(status_code=400, detail="Empty audio upload.")
    with open(audio_path, "wb") as f:
        f.write(content)

    _ensure_whisper()
    from mlx_whisper import transcribe as whisper_transcribe
    try:
        result = whisper_transcribe(str(audio_path), path_or_hf_repo=WHISPER_MODEL_DEFAULT)
        text = result["text"].strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Whisper failed: {e}")

    s["pending_audio"] = str(audio_path)
    s["pending_transcript"] = text

    return {
        "transcript": text,
        "audio_filename": audio_filename,
        "duration_seconds": None,  # frontend already knows from MediaRecorder
    }


@app.post("/api/sessions/{session_id}/keep")
def keep(session_id: str, req: KeepRequest) -> dict[str, Any]:
    """Commit the (possibly edited) transcript to transcript.md and advance."""
    s = _get_session(session_id)
    idx = s["current_idx"]
    if idx >= len(s["questions"]):
        raise HTTPException(status_code=409, detail="Session complete.")
    if "pending_audio" not in s:
        raise HTTPException(status_code=409, detail="No pending recording to keep.")

    q = s["questions"][idx]
    audio_path = Path(s["pending_audio"])
    audio_rel = audio_path.relative_to(s["out_dir"])

    _append_to_transcript(
        Path(s["transcript_path"]),
        f"Q{idx + 1:02d}",
        q,
        req.transcript,
        audio_rel,
    )

    s["completed"].append({"idx": idx, "kind": "kept", "transcript_chars": len(req.transcript)})
    s["current_idx"] += 1
    s.pop("pending_audio", None)
    s.pop("pending_transcript", None)

    return {
        "advanced": True,
        "current_idx": s["current_idx"],
        "done": s["current_idx"] >= len(s["questions"]),
    }


@app.post("/api/sessions/{session_id}/redo")
def redo(session_id: str) -> dict[str, Any]:
    """Discard pending recording and let user re-record current question."""
    s = _get_session(session_id)
    if "pending_audio" in s:
        try:
            Path(s["pending_audio"]).unlink(missing_ok=True)
        except Exception:
            pass
    s.pop("pending_audio", None)
    s.pop("pending_transcript", None)
    return {"ok": True}


@app.post("/api/sessions/{session_id}/skip")
def skip(session_id: str) -> dict[str, Any]:
    """Skip current question without recording. Advances index."""
    s = _get_session(session_id)
    idx = s["current_idx"]
    if idx >= len(s["questions"]):
        raise HTTPException(status_code=409, detail="Session complete.")
    # Discard any pending recording
    if "pending_audio" in s:
        try:
            Path(s["pending_audio"]).unlink(missing_ok=True)
        except Exception:
            pass
        s.pop("pending_audio", None)
        s.pop("pending_transcript", None)
    s["completed"].append({"idx": idx, "kind": "skipped"})
    s["current_idx"] += 1
    return {
        "advanced": True,
        "current_idx": s["current_idx"],
        "done": s["current_idx"] >= len(s["questions"]),
    }


@app.post("/api/sessions/{session_id}/quit")
def quit_session(session_id: str) -> dict[str, Any]:
    """Finalize session — return summary."""
    s = _get_session(session_id)
    summary = {
        "interviewee": s["interviewee"],
        "shape": s["shape_name"],
        "total_questions": len(s["questions"]),
        "completed": len(s["completed"]),
        "kept": sum(1 for c in s["completed"] if c["kind"] == "kept"),
        "skipped": sum(1 for c in s["completed"] if c["kind"] == "skipped"),
        "out_dir": s["out_dir"],
        "transcript_path": s["transcript_path"],
    }
    # Discard any pending recording
    if "pending_audio" in s:
        try:
            Path(s["pending_audio"]).unlink(missing_ok=True)
        except Exception:
            pass
    del _sessions[session_id]
    return summary


# ---------- static files & root ----------

app.mount("/static", StaticFiles(directory=str(WEB_DIR)), name="static")


@app.get("/")
def root() -> FileResponse:
    return FileResponse(str(WEB_DIR / "index.html"))


@app.get("/CONSENT.md")
def consent() -> FileResponse:
    return FileResponse(str(HERE / "CONSENT.md"))


# ---------- main ----------

def main():
    host = "127.0.0.1"
    port = int(os.environ.get("SIGNAL_INTERVIEW_PORT", "8765"))
    print(f"\nSignal voice interview — server starting at http://{host}:{port}")
    print("Privacy posture: bound to 127.0.0.1; no outbound calls; same as CLI tool.")
    print("Open the URL above in a browser. Headphones recommended.\n")
    uvicorn.run(app, host=host, port=port, log_level="info")


if __name__ == "__main__":
    main()
