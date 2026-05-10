# Signal Interview — Informed Consent

**Read this before any interview. The interviewee should sign before recording begins.**

---

## What this is

Signal is a research project building a Socratic narrative-extraction tool for technical leaders. As part of that work, we are collecting voice interviews to seed a small "gold persona" corpus that calibrates the system's quality checks. The audio recording of this interview, and the transcript made from it, become input to that corpus.

## What we will record

- An audio recording of your spoken responses to a structured set of questions, plus any improvised follow-ups.
- A textual transcript automatically generated from the audio by a local speech-to-text model (no audio is sent to any third party).

## What we will do with the recording

- The audio file is stored on the interviewer's local machine only. It is **not uploaded to any cloud service, transcription service, or third-party tool.**
- The audio is used to produce a transcript. After the transcript is reviewed and a "gold persona" file is composed from it, the audio may be deleted or retained at your preference.
- The transcript is read by the interviewer and one collaborator to identify themes — what we call "ground-truth markup." That marked-up document is then transformed into a fictionalised "gold persona" file that uses a pseudonym and is rephrased so that you are not identifiable.

## What will be shared

- **The audio file is private.** It will not leave the interviewer's machine without further written consent from you.
- **The raw transcript is private.** Same.
- **The fictionalised gold persona file** — composed from the transcript, using a pseudonym, with identifying details altered — may be committed to the project's source repository and used internally to calibrate Signal's quality checks. You can review this file before it is committed and request changes or redaction.

## Identifying details

- A **pseudonym** will be used in all stored files. Your real name will not appear.
- **Employer names, project names, colleagues' names, and identifying outcomes** will be paraphrased or altered when the gold persona is composed. You can request specific items be removed or altered before the file is committed.

## Your rights

- **You may stop the interview at any time**, for any reason, without explanation.
- **You may request that any recorded segment be deleted** before it is transcribed.
- **You may request that any segment of the transcript be redacted** before it informs a gold persona.
- **You may request full deletion** of the audio, transcript, and any derived materials at any time. Deletion is local-only and immediate (`rm -rf` on the interviewer's machine; no cloud copies exist).
- **You may withdraw consent** at any time, including after the interview, and have all derived materials destroyed.

## What this is NOT

- This is not a recruiting interview. There is no job offered or implied.
- This is not a coaching or therapy session.
- This is not a publication. Your specific answers will not be quoted in any external document or marketing material without separate written consent.

## What we ask of you

- Speak as honestly as you are comfortable. The interview is structured to surface contradictions and load-bearing details — these are what make the corpus useful. You are not being judged.
- If a question feels uncomfortable, say "skip" — it costs nothing.

## Audio retention preference

Choose one (initial each):

- [ ] **Delete audio after transcript review.** (Default. The audio is destroyed after the transcript is finalised.)
- [ ] **Retain audio locally for future re-transcription.** (Audio kept on interviewer's machine; not shared.)

## Signature

By signing below, you confirm:

1. You have read and understood this consent form.
2. The interviewer has answered any questions you had.
3. You agree to the recording, the local transcription, and the use of a fictionalised gold persona derived from the transcript.
4. You understand you can withdraw at any time.

Interviewee name: _______________________________________

Pseudonym for this corpus: ______________________________

Date: ______________

Signature: _______________________________________

Interviewer name: _______________________________________

Interviewer signature: _______________________________________

---

A signed copy stays with the interviewer. A signed copy goes to the interviewee. The pseudonym is recorded in `tools/interview/CONSENT-LOG.md` (kept local; never committed) so consent can be traced if the interviewee requests deletion later.
