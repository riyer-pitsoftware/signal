---
name: Vesper — Game / Interaction Design Brief
bead: BP-009 (signal-c1m)
date: 2026-05-09
---

## 1. Core loop

```
enter room → NPC asks one thing → user answers in prose
   → answer lands as artifact → room changes (light, card pins)
   → NPC follows up, OR Vey drifts in with a tension
   → user leaves → (next session: the room is different)
```

You walk into a room, somebody who was there asks one specific thing, you answer in your own prose. The answer doesn't disappear into chat — it lands as a physical artifact and the room changes shape (spine §C2, §C4). When two artifacts disagree, Vey appears; when an answer is vague, the NPC stops accepting it and asks the same thing differently.

## 2. Spatial layout per room

Standing rule: enter from the south, evidence east, NPC northwest, threshold is the doorframe — crossing commits to the room's mode (Dash §2).

- **Foyer.** Marlow at the door, coat on. Coat rack of one-line claims. Threshold: the welcome mat surfaces the kettle line.
- **Workshop.** Cassady at the bench, back to you. Artifacts pin to the schematic board. Threshold: picking up a tool flips dialogue from greeting to interrogation.
- **Bridge.** No resident; Vey passes. The walkway *is* the evidence — names on the rail, dates underfoot. Threshold: the lit half commits to a person.
- **Switchyard.** No resident. Cables and tags; pulling a tag opens its dependency. Threshold: standing by the *ship* lever shifts the register from generic to operational.
- **Glasshouse.** No resident; Vey or Lenore drifts in based on what's been said. Vines on a trellis. Threshold: the mist on crossing.
- **Library.** Lenore in the chair that fits her. Card catalog east, stacks south. Threshold: opening the catalog — until then, Lenore reads.
- **Boiler Room.** No resident; Cassady descends if summoned. Pressure dials. Threshold: the hatch closes, hum is the only audio. *(Cut candidate, §6.)*

## 3. NPC mechanic spec

Each NPC owns one *probe class*. Routing is mechanical, not stylistic.

- **Lenore (Archivist).** Input: claims missing date, document, witness. Gain: claim becomes publishable (F1, F8). State: `evidence_status` flips `asserted` → `linked` or `flagged`. Refuses feelings. Cannot invent evidence; if user has nothing, claim saves as `unsupported` — never deleted.
- **Cassady (Foreman).** Input: claims with leadership-altitude vocab ("led", "owned", "drove"). Gain: abstraction replaced by a verb you actually performed. State: claim rewrites; original retained as version. Refuses strategy, brand language. Cannot accept a claim that survives all three of his probes unchanged.
- **Vey (Cartographer).** Input: pairs of claims that semantic-disagree (F7). Gain: user sees the seam, picks a side, or annotates *both true*. State: `tension` artifact written between the two; neither deleted. Refuses leading framing. Cannot appear unprompted by a real contradiction.
- **Marlow (Stranger).** Input: one sentence under thirty seconds. Gain: compression test (F4). State: `pitch_v_n` artifact in Foyer; old versions stay pinned. Refuses softening, cross-visit follow-up. Cannot leave the Foyer.

**Selection.** Resident NPC of the room fires. Empty rooms: contradiction? → Vey. Under-specified? → Cassady drifts up. Else silence (Dash §4).

## 4. Pacing

- **First 90 seconds.** Step on the welcome mat. The lamp is on. Marlow looks up: "I don't know you. One sentence." Hook is the question, not a tutorial. Lost if Marlow follows up before the user has answered once — turn one accepts anything and pins it.
- **Third return.** The Foyer is different. Your first sentence sits on the coat rack, weaker than remembered. Cassady's bench is louder — you've earned the right to be interrogated. Vey waits in the hallway because two claims have started arguing.
- **Tenth visit.** The palace has weather. Some rooms are quiet because they're done. Compounding: published narratives sit framed in the Foyer; you read your old self. Risk: probes feel patterned — Suki's rotation must widen, or the visit collapses into a list.

## 5. Failure-mode catalogue

1. **LLM hallucinates a fact.** NPCs frame every surfaced claim as a question, never an assertion ("Did you say platform, or product?"). Player feels: corrected, not gaslit.
2. **User disengages mid-dialogue.** NPC trails off after one beat. Room saves; on return the NPC says nothing, just looks up. Player feels: the room waited.
3. **Metaphor leaks.** No chime, level-up, progress bar. If user types "what do I do next" three times, the building speaks: "There isn't a next. There's a room you haven't been quiet in yet." Player feels: redirected, not punished.
4. **Evidence contradicts itself, user wants both true.** Vey writes a `tension`; both claims kept verbatim. Publish gate (F1/F8) refuses ship until user marks `holds_both`. Player feels: nuance respected, laziness refused.
5. **NPCs become interchangeable.** C5 compares vocabulary overlap across last 20 turns per NPC; >40% rotates Suki's prompt seed silently. Player-facing: nothing.
6. **User demands a generic résumé.** Refused. Building: "That isn't what's in this house." Raw claims export as JSON; the *narrative* publish path enforces F3.
7. **Contradiction false-positive.** Vey asks, never tells. Dismissal writes `dismissed_by_user`; doesn't re-raise unless a third claim re-activates.

## 6. Cut list

- **Cut the Boiler Room from v0.1.** Dash gives seven rooms; spine asks ≥6. No resident NPC, no probe Cassady can't cover from the Workshop. Fails Q1 (teaches nothing new) and Q5 (costs simplicity for small audience). Ship six; promise the hatch.
- **Cut the Bridge's "unlit half" as interactive geometry.** Set dressing only. Q3: friction without a teach is decoration.
- **Cut all visible progress signals**, including any implicit "3 of 4 NPCs talked to" hint. Game-shaped feedback degrades the metaphor. Q4: meta-progression IS the room remembering.
- **Cut Marlow's cross-visit memory.** Each return he forgets you. Forgetting is the mechanic. Q1: teaches that strangers don't retain context.
- **Cut résumé-paste ingestion** (spine §8.3). Free-text into NPC dialogue only. Q5: paste removes the user's chance to *say it themselves*.

## 7. Open questions

- **Marcus.** Can Phaser↔React stream NPC text token-by-token without flicker? Else fall back to whole-line reveal (F5).
- **Suki.** Does Vey's detector fire across sessions or only in-session? Across-session is the better mechanic; costs RAM (F6).
- **Suki.** Prompt-rotation budget for tenth-visit interest? If Cassady can't seed-vary, the visit collapses.
- **design-for-ai.** Rooms animate *when an artifact is placed, never on hover.* Confirm under reduced-motion.
- **Opus (spine §8.2).** Ratify contradiction surfacing as Vey-drifts-in (C4-native), not popup.
