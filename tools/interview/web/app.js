// Signal voice interview — frontend.
// Vanilla JS, no framework, no build step.
// State machine: SETUP → PRESENT → READY → RECORDING → TRANSCRIBING → REVIEW → (loop) → DONE.

(() => {
  "use strict";

  // ============================================================
  // App state
  // ============================================================

  const state = {
    view: "setup",
    shapes: [],
    selectedShape: null,
    consentChecked: false,
    interviewee: "",
    sessionId: null,
    sessionMeta: null,
    currentQuestion: null,
    sessionState: "present", // present | ready | recording | transcribing | review
    pendingTranscript: "",
    mediaRecorder: null,
    audioChunks: [],
    audioStream: null,
    recordStartTime: null,
    recordTimerInterval: null,
    vuInterval: null,
    audioContext: null,
    analyser: null,
    currentTtsAudio: null,
  };

  const root = document.getElementById("app");

  // ============================================================
  // Render: renders one of three top-level views
  // ============================================================

  function render() {
    if (state.view === "setup") renderSetup();
    else if (state.view === "session") renderSession();
    else if (state.view === "done") renderDone();
  }

  function mountTemplate(templateId) {
    const tpl = document.getElementById(templateId);
    root.innerHTML = "";
    root.appendChild(tpl.content.cloneNode(true));
  }

  // ------------------------------------------------------------
  // Setup view
  // ------------------------------------------------------------

  function renderSetup() {
    mountTemplate("tpl-setup");

    const consentCb = document.getElementById("consent-checkbox");
    const intervieweeInput = document.getElementById("interviewee-input");
    const startBtn = document.getElementById("start-button");
    const grid = document.getElementById("shapes-grid");

    consentCb.checked = state.consentChecked;
    intervieweeInput.value = state.interviewee;

    consentCb.addEventListener("change", () => {
      state.consentChecked = consentCb.checked;
      updateStartButton();
    });
    intervieweeInput.addEventListener("input", () => {
      state.interviewee = intervieweeInput.value.trim();
      updateStartButton();
    });
    startBtn.addEventListener("click", startSession);

    // Render shapes (already loaded or fetch fresh)
    if (state.shapes.length === 0) {
      fetch("/api/shapes")
        .then((r) => r.json())
        .then((shapes) => {
          state.shapes = shapes;
          renderShapesGrid(grid);
        })
        .catch((e) => {
          grid.innerHTML = `<div class="muted">Failed to load shapes: ${e.message}</div>`;
        });
    } else {
      renderShapesGrid(grid);
    }

    updateStartButton();
  }

  function renderShapesGrid(grid) {
    grid.innerHTML = "";
    state.shapes.forEach((shape) => {
      const card = document.createElement("div");
      card.className = "shape-card";
      if (state.selectedShape === shape.id) card.classList.add("selected");
      card.innerHTML = `
        <div class="shape-card-header">
          <span class="shape-card-name">${escapeHtml(shape.name)}</span>
          <span class="shape-card-meta">${shape.question_count} prompts · tests ${shape.primary_tests.join(", ")}</span>
        </div>
        <p class="shape-card-desc">${escapeHtml(shape.description)}</p>
      `;
      card.addEventListener("click", () => {
        state.selectedShape = shape.id;
        renderShapesGrid(grid);
        updateStartButton();
      });
      grid.appendChild(card);
    });
  }

  function updateStartButton() {
    const btn = document.getElementById("start-button");
    if (!btn) return;
    btn.disabled = !(
      state.consentChecked &&
      state.selectedShape &&
      state.interviewee.length > 0
    );
  }

  async function startSession() {
    const startBtn = document.getElementById("start-button");
    startBtn.disabled = true;
    startBtn.textContent = "Starting…";
    try {
      const res = await fetch("/api/sessions", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          shape: state.selectedShape,
          interviewee: state.interviewee,
          consent_confirmed: state.consentChecked,
        }),
      });
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        alert(`Failed to start: ${err.detail || res.statusText}`);
        startBtn.disabled = false;
        startBtn.textContent = "Start session";
        return;
      }
      const data = await res.json();
      state.sessionId = data.session_id;
      state.sessionMeta = data;
      state.sessionState = "present";
      state.view = "session";
      await loadCurrentQuestion();
      render();
    } catch (e) {
      alert(`Network error: ${e.message}`);
      startBtn.disabled = false;
      startBtn.textContent = "Start session";
    }
  }

  // ------------------------------------------------------------
  // Session view
  // ------------------------------------------------------------

  async function loadCurrentQuestion() {
    const res = await fetch(`/api/sessions/${state.sessionId}/question`);
    if (res.status === 409) {
      // Session done
      await finishSession();
      return;
    }
    if (!res.ok) {
      alert(`Failed to load question: ${res.statusText}`);
      return;
    }
    state.currentQuestion = await res.json();
  }

  function renderSession() {
    mountTemplate("tpl-session");

    document.getElementById("session-shape-name").textContent = state.sessionMeta.shape;
    document.getElementById("session-interviewee").textContent = state.sessionMeta.interviewee;
    if (state.currentQuestion) {
      document.getElementById("session-progress").textContent =
        `${state.currentQuestion.idx_str} / ${state.currentQuestion.total}`;
      document.getElementById("q-depth").textContent = state.currentQuestion.depth;
      document.getElementById("q-idx").textContent = state.currentQuestion.idx_str;
      document.getElementById("q-prompt").textContent = state.currentQuestion.prompt;
      document.getElementById("q-intent").textContent = "Intent: " + state.currentQuestion.intent;
    }

    document.getElementById("quit-button").addEventListener("click", quitSession);
    document.getElementById("speak-button").addEventListener("click", speakViaTts);
    document.getElementById("read-button").addEventListener("click", () => {
      showSection("record-actions");
    });
    document.getElementById("skip-button").addEventListener("click", skipQuestion);
    document.getElementById("record-button").addEventListener("click", startRecording);
    document.getElementById("back-to-present").addEventListener("click", () => {
      showSection("present-actions");
    });
    document.getElementById("stop-button").addEventListener("click", stopRecording);
    document.getElementById("keep-button").addEventListener("click", keepTranscript);
    document.getElementById("redo-button").addEventListener("click", redoTranscript);

    // Show the right section based on state.sessionState
    showSection(stateToSectionId(state.sessionState));
  }

  function stateToSectionId(s) {
    switch (s) {
      case "present": return "present-actions";
      case "ready": return "record-actions";
      case "recording": return "recording-actions";
      case "transcribing": return "transcribing-actions";
      case "review": return "review-actions";
      default: return "present-actions";
    }
  }

  function showSection(id) {
    ["present-actions", "record-actions", "recording-actions", "transcribing-actions", "review-actions"]
      .forEach((sid) => {
        const el = document.getElementById(sid);
        if (el) el.classList.toggle("hidden", sid !== id);
      });
  }

  // ------------------------------------------------------------
  // TTS
  // ------------------------------------------------------------

  async function speakViaTts() {
    const btn = document.getElementById("speak-button");
    const original = btn.textContent;
    btn.disabled = true;
    btn.textContent = "Synthesizing…";
    try {
      const res = await fetch(`/api/sessions/${state.sessionId}/tts`, { method: "POST" });
      if (!res.ok) throw new Error(`TTS failed: ${res.statusText}`);
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      const audio = new Audio(url);
      state.currentTtsAudio = audio;
      btn.textContent = "Speaking…";
      audio.addEventListener("ended", () => {
        URL.revokeObjectURL(url);
        btn.disabled = false;
        btn.textContent = original;
        showSection("record-actions");
      });
      audio.addEventListener("error", () => {
        btn.disabled = false;
        btn.textContent = original;
      });
      await audio.play();
    } catch (e) {
      alert(`TTS error: ${e.message}\nFall back to "Read aloud myself".`);
      btn.disabled = false;
      btn.textContent = original;
    }
  }

  // ------------------------------------------------------------
  // Recording
  // ------------------------------------------------------------

  async function startRecording() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      state.audioStream = stream;
      state.audioChunks = [];

      // VU meter setup
      state.audioContext = new (window.AudioContext || window.webkitAudioContext)();
      const source = state.audioContext.createMediaStreamSource(stream);
      state.analyser = state.audioContext.createAnalyser();
      state.analyser.fftSize = 256;
      source.connect(state.analyser);

      const mr = new MediaRecorder(stream);
      state.mediaRecorder = mr;
      mr.addEventListener("dataavailable", (e) => {
        if (e.data && e.data.size > 0) state.audioChunks.push(e.data);
      });
      mr.addEventListener("stop", handleRecordingStopped);
      mr.start();

      state.sessionState = "recording";
      state.recordStartTime = Date.now();
      showSection("recording-actions");
      startVuLoop();
      startTimerLoop();
    } catch (e) {
      alert(`Mic permission denied or unavailable: ${e.message}`);
    }
  }

  function startVuLoop() {
    const vuBar = document.getElementById("vu-bar");
    const data = new Uint8Array(state.analyser.frequencyBinCount);
    state.vuInterval = setInterval(() => {
      if (!state.analyser) return;
      state.analyser.getByteTimeDomainData(data);
      // RMS
      let sum = 0;
      for (let i = 0; i < data.length; i++) {
        const v = (data[i] - 128) / 128;
        sum += v * v;
      }
      const rms = Math.sqrt(sum / data.length);
      const pct = Math.min(100, Math.max(2, rms * 200));
      vuBar.style.width = `${pct}%`;
    }, 80);
  }

  function startTimerLoop() {
    const timer = document.getElementById("rec-timer");
    state.recordTimerInterval = setInterval(() => {
      const elapsed = Math.floor((Date.now() - state.recordStartTime) / 1000);
      const mins = Math.floor(elapsed / 60);
      const secs = elapsed % 60;
      timer.textContent = `${mins}:${secs.toString().padStart(2, "0")}`;
    }, 250);
  }

  function stopRecording() {
    if (state.mediaRecorder && state.mediaRecorder.state !== "inactive") {
      state.mediaRecorder.stop();
    }
  }

  function teardownRecording() {
    if (state.audioStream) {
      state.audioStream.getTracks().forEach((t) => t.stop());
      state.audioStream = null;
    }
    if (state.audioContext) {
      state.audioContext.close().catch(() => {});
      state.audioContext = null;
    }
    state.analyser = null;
    if (state.vuInterval) { clearInterval(state.vuInterval); state.vuInterval = null; }
    if (state.recordTimerInterval) { clearInterval(state.recordTimerInterval); state.recordTimerInterval = null; }
  }

  async function handleRecordingStopped() {
    teardownRecording();
    if (state.audioChunks.length === 0) {
      alert("No audio captured.");
      state.sessionState = "ready";
      showSection("record-actions");
      return;
    }

    const blob = new Blob(state.audioChunks, { type: state.mediaRecorder.mimeType || "audio/webm" });
    state.sessionState = "transcribing";
    showSection("transcribing-actions");

    const fd = new FormData();
    fd.append("audio", blob, "recording.webm");
    try {
      const res = await fetch(`/api/sessions/${state.sessionId}/record`, {
        method: "POST",
        body: fd,
      });
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || res.statusText);
      }
      const data = await res.json();
      state.pendingTranscript = data.transcript;
      state.sessionState = "review";
      showSection("review-actions");
      const ta = document.getElementById("transcript-textarea");
      ta.value = data.transcript;
      ta.focus();
    } catch (e) {
      alert(`Transcription failed: ${e.message}`);
      state.sessionState = "ready";
      showSection("record-actions");
    }
  }

  async function keepTranscript() {
    const ta = document.getElementById("transcript-textarea");
    const text = ta.value.trim();
    if (!text) {
      alert("Transcript is empty. Edit or redo.");
      return;
    }
    const btn = document.getElementById("keep-button");
    btn.disabled = true;
    try {
      const res = await fetch(`/api/sessions/${state.sessionId}/keep`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ transcript: text }),
      });
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || res.statusText);
      }
      const data = await res.json();
      if (data.done) {
        await finishSession();
      } else {
        state.sessionState = "present";
        await loadCurrentQuestion();
        render();
      }
    } catch (e) {
      alert(`Save failed: ${e.message}`);
      btn.disabled = false;
    }
  }

  async function redoTranscript() {
    try {
      await fetch(`/api/sessions/${state.sessionId}/redo`, { method: "POST" });
    } catch (e) { /* ignore */ }
    state.sessionState = "ready";
    showSection("record-actions");
  }

  async function skipQuestion() {
    const btn = document.getElementById("skip-button");
    btn.disabled = true;
    try {
      const res = await fetch(`/api/sessions/${state.sessionId}/skip`, { method: "POST" });
      if (!res.ok) throw new Error(res.statusText);
      const data = await res.json();
      if (data.done) {
        await finishSession();
      } else {
        state.sessionState = "present";
        await loadCurrentQuestion();
        render();
      }
    } catch (e) {
      alert(`Skip failed: ${e.message}`);
      btn.disabled = false;
    }
  }

  async function quitSession() {
    if (!confirm("Quit this session? Any unsaved recording is discarded; saved transcripts are kept.")) return;
    await finishSession();
  }

  async function finishSession() {
    teardownRecording();
    try {
      const res = await fetch(`/api/sessions/${state.sessionId}/quit`, { method: "POST" });
      if (res.ok) {
        const summary = await res.json();
        state.summary = summary;
      }
    } catch (e) { /* swallow */ }
    state.view = "done";
    render();
  }

  // ------------------------------------------------------------
  // Done view
  // ------------------------------------------------------------

  function renderDone() {
    mountTemplate("tpl-done");
    const s = state.summary || {};
    document.getElementById("done-interviewee").textContent = s.interviewee || state.sessionMeta?.interviewee || "—";
    document.getElementById("done-shape").textContent = s.shape || state.sessionMeta?.shape || "—";
    document.getElementById("done-kept").textContent = s.kept ?? "—";
    document.getElementById("done-total").textContent = s.total_questions ?? "—";
    document.getElementById("done-skipped").textContent = s.skipped ?? "—";
    document.getElementById("done-path").textContent = s.transcript_path || "—";
    document.getElementById("new-session-button").addEventListener("click", () => {
      // Reset relevant state for a fresh setup
      state.view = "setup";
      state.sessionId = null;
      state.sessionMeta = null;
      state.currentQuestion = null;
      state.sessionState = "present";
      state.pendingTranscript = "";
      state.summary = null;
      // Keep selectedShape and interviewee for convenience? Clear interviewee; keep nothing.
      state.interviewee = "";
      state.selectedShape = null;
      state.consentChecked = false;
      render();
    });
  }

  // ============================================================
  // Utilities
  // ============================================================

  function escapeHtml(s) {
    return String(s)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  }

  // ============================================================
  // Boot
  // ============================================================

  render();
})();
