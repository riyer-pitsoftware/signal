---
name: Resolution — Mara M3 (first-90-seconds orientation)
bead: BP-013.7 (signal-b5x)
date: 2026-05-10
author: Dash (creative direction) — drafted under spine §F5 (p50 ≤ 4s, p99 ≤ 12s); flags cascade if signal-r1j relaxes thresholds
blocker_addressed: Mara M3 — "Marlow as the first-90-seconds NPC is a single point of failure; every first-time user lands on the hardest probe in the system with no orientation beat."
---

## Decision

**B. Keep Marlow as the opener. Insert a 35-second orientation beat — *the building speaks first* — before Marlow looks up. Make turn-1 a *collection* turn, not an *interrogation* turn: any answer is accepted and pins to the coat rack. The compression test does not begin until turn 2.**

This preserves Sofia's demo cold-open script (judges-pre-draft.md, lines 92–116) almost frame-for-frame — only the timing shifts and the system-voice prelude is specified. It directly addresses Mara M3's two failure modes ("user can't produce a one-sentence pitch in 30 seconds" and "user bounces believing Signal is an AI that won't accept my answer") by making the first-NPC turn *contractually* incapable of refusal.

Decision A (replace Marlow) was rejected: Marlow's outsider compression test is the single demo moment that distinguishes Signal from chat (PRD §7.5; Sofia S1). Replacing him moves the load-bearing demo asset out of frame one. Decision C (non-NPC opener — guided room tour) was rejected: it makes the *building* the first interlocutor, which leaks the metaphor (the building is third voice, not first voice; dash.md §5) and trains the user that Signal is a guided product rather than a quiet one.

---

## Literal narration: session seconds 0–90

This is what a first-time user sees and hears. No filling-in. The clock starts the instant the app window finishes its initial paint.

```
t=0s     [visual]   Window opens to flat oklch(15% 0.01 60) — near-black
                    with warm undertone. No logo. No spinner. No chrome.
t=1s     [visual]   Black holds. (Camera is closed-eye. The room is on the
                    other side of it.)
t=3s     [visual]   Cross-dissolve begins, 480ms, cubic-bezier(0.65,0,0.35,1).
                    Black → Foyer interior at oklch(94% 0.01 80) — paper
                    background, slight yellow cast. No motion in the room
                    yet. No NPC yet. A coat rack stands left of frame, empty
                    of pinned sentences. A lamp on the entry table is unlit.
t=4s     [visual]   The lamp glows on. 220ms fade-in, ease-out. --lamp
                    (oklch(78% 0.13 75)) catches the wood, throws warm cast
                    on coat rack. The first thing that *moves* in this app
                    is a lamp turning on.
t=6s     [audio]    Room tone fades up, -28dB: low building hum, distant
                    weather (rain on a roof, far). Held throughout.
                    No music. No sting. No chime.
t=8s     [text]     Building voice — Inter, 16px, --shadow on --paper —
                    fades in below the lamp, 220ms.
                    "The lamp is on. Take your time."
                    Held on screen 4s. No typewriter on system voice;
                    typewriter is reserved for NPCs (design-system §4).
t=14s    [text]     Line 1 fades. Line 2 fades in.
                    "There's a stranger by the door. He hasn't met you."
                    Held 4s.
t=20s    [text]     Line 2 fades. Line 3 fades in.
                    "Whatever you say first will pin to the coat rack.
                     You can change it later. You can change it always."
                    Held 5s. This is the trust contract, stated literally.
t=27s    [visual]   Pixel-art Marlow appears, fade-in 480ms, at the
                    door — coat on, hands at sides, looking at the floor.
                    Idle breath: 2px translateY, 5s loop, opacity 0.95↔1.0.
                    He is *not yet looking at the user*. This is deliberate.
                    The user has 8 seconds with him in the room before he
                    becomes an interlocutor.
t=32s    [text]     Building voice, line 4.
                    "He's getting on a plane. He has thirty seconds."
                    Held 4s. This frames Marlow's brevity as *his* limit,
                    not the system's standard.
t=36s    [visual]   Marlow lifts his head. 200ms ease-out. He looks at
                    the user. The lamp brightens 4% (oklch L: 78% → 81%).
                    The text input field fades in below the room, 320ms,
                    --paper surface, --ink caret. No placeholder text.
                    No "send" glyph. The lamp is the affordance.
t=40s    [text]     Marlow speaks. EB Garamond, 28ms typewriter, jittered
                    ±6ms (design-system §4).
                    "I don't know you. In one sentence — what should I
                     have hired you to do, last year?"
                    Typewriter completes at t≈44s.
t=44s    [state]    Cursor blinks in the input field. The room waits.
                    No timer. No "skip" button. No "I don't know what
                    to type" hint yet — the orientation said what the
                    user needs to know.
t=44–75s [input]    User types. The lamp glows 2% brighter while focus
                    is in the field. Marlow's idle continues. No
                    interruption from the system. No suggestion.
                    No autocomplete. (If the user has not begun typing
                    by t=75s, see Failure Modes §3 — confused user.)
t=~80s   [input]    User submits (Enter). Whatever they typed — one
                    word, three sentences, "I don't know," a single
                    period — is accepted. Turn-1 cannot reject.
                    The lamp dims 4% on submit (the room receives).
t=80s    [visual]   Submitted text animates from input field to coat
                    rack: 600ms, cubic-bezier(0.22,1,0.36,1). Lands as
                    a pinned card. Mono type (Berkeley Mono 14px), date
                    underneath in --shadow. The card is dated and
                    timestamped — visible provenance from turn one.
t=83s    [text]     Building voice, beneath the coat rack.
                    "Filed. The room remembers."
                    Held 3s. (This is the trust-calibration moment. See
                    §Trust Calibration.)
t=86s    [visual]   Marlow nods once — 180ms, single head-dip, no smile.
                    He does not yet probe. Turn-1 is collection, not
                    interrogation.
t=88s    [text]     Marlow's second line begins typewriter — but does
                    NOT challenge the first sentence. It opens the
                    space for the next one.
                    "Okay. Tell me one more thing about that — whatever
                     comes next."
                    (The compression test — "that sentence had three
                     jobs in it; pick the one that pays you" — fires on
                     turn 2, not turn 1. By then the user has experienced
                     the system *receiving* before the system *probing*.)
t=90s    [state]    Typewriter still running. User has answered once,
                    seen their sentence pin to a physical surface, heard
                    the building acknowledge receipt, and is now reading
                    the second prompt — which is *additive*, not corrective.
                    First-90-seconds gate cleared.
```

**Total system-voice load before Marlow speaks: 4 lines, 35 seconds.** Slow enough to feel like a building, not a tutorial. Fast enough that a curious user does not bail.

**Total user-input affordance before any rejection is mechanically possible: 90 seconds + turn 2.** Mara's "user can't produce a one-sentence pitch in 30 seconds" failure is now structurally impossible — there is no sentence requirement on turn 1.

---

## First-NPC choice with rationale

**Marlow stays.** Two reasons:

1. **He is the only NPC whose probe is *one sentence under thirty seconds*.** Cassady's probe needs operational vocabulary in the answer to fire. Lenore's probe needs a claim missing date or document. Vey's probe needs *two* claims to detect contradiction. None of these fire usefully on turn one — there is no input yet. Marlow is the only NPC whose probe shape (compression test, PRD §7.5) makes sense as a *first* prompt.

2. **The demo cold-open (Sofia, judges-pre-draft.md §Demo) depends on Marlow at second 14.** Replacing Marlow forfeits the visible mechanic that distinguishes Signal from chat in frame one. Sofia's S1 already flagged the differentiator as "invisible-by-design"; removing Marlow makes it *additionally* invisible by removing the only visible early probe.

**The change is in Marlow's turn-1 mode, not his identity.** Per Vesper §4 ("turn one accepts anything and pins it"), turn-1 is now contractually a *collection* turn — Marlow's probe class fires on turn 2 onward. Vesper called this "aspirational"; this resolution promotes it to **contractual** and names the Suki-side gate (per Mara M3 fix line) that disables F3 rejection on turn 1. **Cascade for BP-014 / Suki:** F3 genericness gate runs in *audit-log mode only* on turn 1 of the first-ever session; first hard rejection happens at turn 2 earliest.

The probe shape used at t=88s ("Tell me one more thing about that — whatever comes next") is gentler than Marlow's full interrogation because it is *additive* not *reductive*. Marlow at his hardest is "that sentence had three jobs; pick the one that pays you" — a cut. Marlow at turn-1.5 is "tell me one more thing" — an offering. Same character, different beat in the rhythm.

---

## Failure-mode coverage

Three modes Mara identified. Each has a specified system response, not an aspiration.

### 1. Confused user — doesn't understand what's being asked

**Trigger:** User has not begun typing by t=75s (i.e., no keystrokes in 31 seconds after Marlow's prompt completes), OR user types and deletes 3+ times within a 20-second window.

**Response:** At the trigger, Marlow does *not* repeat his question. The building voice fades in below the input field, --shadow color, 14px:

> "If nothing is coming — say what you wish he'd asked. He'll listen for it."

This is a graceful repeat that *reframes the question as the user's own*. It is also an "I don't know" affordance — the user can literally type "I don't know what you want me to say" and that sentence pins to the coat rack as a valid first claim. The system never says "try again" or "be more specific." The room waits.

If the user submits a non-attempt ("idk", "skip", "?"), turn-1 still pins it. Marlow then says: *"That's fine. Tell me what you did last week instead."* — sliding the question from career-altitude to operational. This is Cassady's probe shape borrowed for one beat, because Cassady can't drift into the Foyer (Vesper §3, NPC selection rules) but the *probe class* can be loaned for graceful degradation.

### 2. Skipping user — clicks through prompts without engaging

**Trigger:** User submits within 4 seconds of Marlow's prompt completing (i.e., before they could plausibly have read it), with content that is one of: empty, single character, copy-pasted text >200 chars, or matches a "skip pattern" (lorem ipsum, keyboard mash, "test" alone).

**Response:** The system does not accuse. It pins the input as it does for any answer. Then the building voice fades in:

> "Filed. If you weren't ready, that's fine. The lamp stays on."

The lamp *physically does not dim* on submit in this case — visual contradiction to the "received" state, signaling the system noticed. Marlow does not advance to his next line; he holds idle. The input field re-focuses with the user's submitted text *re-loaded as draft* — they can edit it without losing what they put in.

If the user submits a second skip-pattern, the system *disengages gracefully* rather than escalating: building voice, "Come back when there's something to say. The room will be here." The session saves and the user can close the window without penalty. **No "are you sure" modal. No retention nag.** Mara's "user bounces believing Signal is an AI that won't accept my answer" is foreclosed because Signal *did* accept. The user simply chose not to inhabit the room.

### 3. Leaving user — wants to abandon the session

**Trigger:** User closes the window, hits Cmd-Q, or clicks any "leave" affordance (the threshold-out arrow at the Foyer doorway, which fades in at t=60s if the user has not yet engaged with the input field).

**Response:** The building voice speaks once, before the window closes:

> "Saved. The room remembers. The kettle's still warm."

**No "are you sure?" No "before you go, please…". No exit survey.** The session writes to disk: any input the user typed (including unsent draft text) is saved as `unsent_draft` in the Foyer state. The lamp remains lit in the saved state — this is what the user sees if they relaunch.

On return (a separate session), the welcome line is different — pulled from the dash.md §5 register: *"You left a kettle in the Workshop. It's still warm."* If they had typed an unsent draft, the building says: *"Something you started is still on the table. No one read it."* The draft is in the input field, ready to edit or discard.

This honors PRD §4.5 (the user owns their narrative; the system does not retain emotional leverage) and Vesper §5 failure-mode 2 (NPC trails off, room saves, on return looks up).

---

## Trust calibration

**The trust-calibration moment is at t=83s: the building speaks "Filed. The room remembers." beneath the coat rack, after the user's first sentence pins as a physical artifact.**

Mara's deeper concern: *does the user trust Signal enough to keep going after 90s?* Trust is not established by the orientation beat (lines 1–4). Trust is not established by Marlow's first prompt. Trust is established by **the system demonstrating that it received the user's input before it judges it** — and that it received it as a *physical, dated, persistent thing* rather than as ephemeral chat history.

Three concrete signals at t=80–86s carry this moment:

1. **Visible artifact-creation (t=80s).** The submitted text *moves* from the input field to the coat rack — 600ms animation, with easing the user's eye can follow. Sentences in chat disappear up-screen and become history; sentences in Signal *go somewhere*. The user sees the spatial commitment.

2. **Provenance metadata is shown immediately (t=80s).** The pinned card carries a date and timestamp in --shadow Berkeley Mono. The user does not have to dig to see that the system has *recorded* their words with attribution to themselves. This previews the C2 provenance graph (spine §2) at the smallest possible scale — one claim, with metadata.

3. **The building speaks acknowledgement, not praise (t=83s).** "Filed. The room remembers." is third-voice, dry, present-tense (dash.md §5). It is *not* "Great answer!" or "Got it!" or any chat-derived affirmation. It tells the user the system noted what they said, and stopped. There is no dopamine, no streak, no encouragement — there is the bookkeeping of an archive. Mara's user-type (technical leaders, staff+ engineers) trusts a system that *files* what they say more than a system that *celebrates* it.

**If trust is not established at t=83s — what happens?** The system has no way to detect this directly (we cannot measure a feeling), but two downstream signals stand in: (a) user does not respond to Marlow's t=88s line within 60 seconds, OR (b) user closes the window during turn 2. In either case the *Leaving user* path (Failure Mode 3) handles it gracefully — saved draft, warm kettle on return, no retention nag. Trust failure is not catastrophic because the design assumes some users will not feel it on session 1, and *the system invites them back rather than insists they continue*. The kettle metaphor (dash.md §5) is the architectural translation of "trust is a return rate, not a session metric."

**Cascade flag for BP-014:** the trust moment depends on F5 holding for the artifact-pin animation latency (t=80s submit → t=80s pin). If signal-r1j (F5 verdict) relaxes p50 above 4s, the *artifact pin must remain immediate* even if Marlow's next-line LLM call is slower — i.e., the visible state-write from input → coat rack is decoupled from the LLM response. **This is a required ADR for BP-014: artifact pinning is a database-write event, not an LLM-completion event. It fires within 200ms of submit regardless of model state.** Without this, the trust moment slides past 90 seconds and the orientation design fails.

---

## ADR-class statement

**Signal's v0.1 opens with a 35-second building-voice orientation beat before Marlow speaks because every first-time user must experience the system *receiving* their input before the system *interrogating* it — turn one is contractually a collection turn, not a probe.**

---

## Cascade flags for BP-014 synthesis

Three places this design requires downstream specificity:

1. **Suki-side gate (Mara M3 fix).** F3 genericness rejection is disabled on turn 1 of the first-ever session. F3 runs in audit-log mode only for that turn. First hard rejection on turn 2 earliest. Required ADR.

2. **Artifact-pin decoupling (Trust calibration cascade).** The submit → coat-rack pin animation fires within 200ms of submit on a database-write trigger, *not* on LLM-completion. This is independent of F5 and must hold even if signal-r1j relaxes the latency budget. Required ADR — affects Priya's FSM (the `claim` write fires synchronously; the NPC reply streams independently).

3. **Marlow's turn-1.5 line ("Okay. Tell me one more thing about that — whatever comes next") is a *new* prompt seed.** Suki's prompt registry (§probe rotation, kenji.md §6 Q4) gains one mandatory turn-1 collection-mode seed for Marlow, distinct from his five interrogation seeds. Total Marlow seeds become 6, not 5. Cascade to Suki's prompt registry size budget.

If signal-r1j (currently OPEN) returns Verdict B (F5 relaxation), this design still holds — the orientation beat is system-voice text fade-in, not LLM-generated, so its 35-second budget is unaffected by model latency. Only Marlow's t=40s and t=88s lines depend on F5; both are short (<35 tokens) and even at relaxed thresholds (e.g., p50 ≤ 7s) they land inside the 90-second window. **This design is robust to F5 relaxation up to p50 ≤ 8s.** Above that, Marlow's t=40s prompt risks landing past t=50s and the orientation rhythm degrades — the user sits with an empty Foyer and a lit lamp for an uncomfortably long pause. If r1j returns Verdict B with p50 > 8s, this resolution requires a follow-up decision: pre-render Marlow's first prompt as static text (loses prompt-rotation across sessions for turn 1) OR shorten the orientation beat to compensate.
