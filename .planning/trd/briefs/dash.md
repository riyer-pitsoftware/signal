---
name: Dash — Creative Direction Brief
bead: BP-008 (signal-a9w)
date: 2026-05-09
---

## 1. The metaphor in one paragraph

A memory palace is the room you walk into when nobody's watching you remember. It's a house you've lived in but never mapped — career years arranged as architecture, with weather. You enter through a foyer that has your handwriting on the walls. Each room holds work you did, and a person who was there when you did it, and that person wants to talk to you about it. The light is low. The hallways are longer than they should be. No progress bar. No score. The palace is *not* a dashboard, *not* an intake form, *not* an AI assistant smiling behind a chat bubble. It is the inside of your own working life, rendered as a place you can be quiet in. (Spine §4 — HARD reversibility, ADR-002. PRD §4.2.)

## 2. Room-to-theme map

Six rooms. Each binds a PRD §5 user-type to a spatial theme (C4, spine §2).

- **The Foyer — *technical product leader.*** A coat rack of half-finished decisions. A whiteboard with three product bets, two crossed out; a kettle still warm. *You've been here recently and forgot the lamp.*

- **The Workshop — *architect.*** A long bench under one bulb. Schematics pinned at angles, a system diagram with one box drawn three times because you couldn't decide where it lived, the smell of solder. *Something here used to break and you fixed it.*

- **The Bridge — *engineering manager.*** A walkway between two wings, one lit, one not. A roster of names, some greyed; a hand-written calendar with one date circled hard enough to tear the paper. *People stood here once and waited for you to say the thing.*

- **The Switchyard — *technical program leader.*** A signal-box room, cables threaded through the floor. Dependency tags, a lever marked *ship* that hasn't been pulled, a log book of who promised what. *You kept the trains from hitting each other and almost nobody noticed.*

- **The Glasshouse — *transformation leader.*** A greenhouse where the plants are organizational. Org-chart vines, dead branches labeled with departed initiatives, a watering can with rust on the spout. *Change happened slowly here. Some of it was yours.*

- **The Library — *staff/principal and cross-functional systems thinker.*** A reading room, non-fiction stacked at standing height. Marginalia in your own hand, a card catalog cross-referenced sideways, a chair that fits you. *You read too much and it turned into instinct.*

- **The Boiler Room — *data/platform leader.*** Beneath the floorboards. Pipes that hum, a pressure gauge in the green, a wrench with paint on the handle. *You kept the building warm and most residents never came down here.*

## 3. NPC roster — four interlocutors, distinct probes

Each NPC is a *probing style* (PRD §4.2; spine §1.2). Swap two and the conversation degrades.

**Lenore — the Archivist.** Library. Probe only she performs: *evidence retrieval under pressure.*
- "You said you led that migration. Was there a document. Was there a Slack thread. Where does the proof live."
- "I'm not trying to embarrass you. I'm trying to find out which version you can defend in three years."
- "Specific date or specific quarter. 'Recently' is not."

Refuses: feelings. Alone asks: *what's the document number.*

**Cassady — the Foreman.** Workshop. Probe only he performs: *operational specificity.*
- "'Owned the platform' — did you write code on it. Did you review code on it. Did you decide what got built. Pick one."
- "What did you do on a Tuesday."
- "If your team had vanished for a week, what would have stopped working first."

Refuses: strategy at altitude. Alone asks: *what did your hands do.*

**Vey — the Cartographer.** Drifts between rooms. Probe only she performs: *contradiction surfacing* (PRD §7.6).
- "Earlier, in the Bridge, you said you avoided politics. Now in the Glasshouse you're describing a fight you won. Which is."
- "These two stories are about the same year. They don't fit. Walk me through it."
- "I'm not catching you. I'm helping you notice."

Refuses: leading questions. Alone asks: *do these two things belong in the same person.*

**Marlow — the Stranger.** Foyer. Probe only he performs: *outsider compression test* (PRD §7.5). Hasn't met you. Thirty seconds.
- "I don't know you. In one sentence — what should I have hired you to do, last year."
- "That sentence had three jobs in it. Pick the one that pays you."
- "Try again. Shorter. I'm getting on a plane."

Refuses: softening. Alone asks: *would a stranger remember this.*

## 4. World tone

**Pacing.** Slow. KRZ slow, not loading-screen slow. Lines feel typed by someone choosing the word. Pauses are content. The product never hurries; it is *waiting in a room.*

**Silence.** Default state is quiet. NPCs don't greet you on return — they look up. The room remembers: on the second visit an artifact has shifted, a cup has moved, the light is one degree warmer.

**Sound design** (text-only v0.1, specified forward). Imagined score: low strings, single piano, room tone. No stings, no progress cues. Outer Wilds' end-of-day loneliness. The user is alone in a building; the building has weather.

**Typography mood** (design-for-ai owns specifics). Type must read like a private notebook in a public archive. Serif for NPC dialogue; mono for evidence; one quiet sans for system. No display weights. No flourish.

## 5. Voice samples for system messages

System messages are *the building speaking* — third voice, neutral, dry, present-tense. Distinct from NPCs.

**Welcome.**
- "The lamp is on. Take your time."
- "You left a kettle in the Workshop. It's still warm."
- "Four people are here. None of them are in a hurry."

**Save confirmation.**
- "Saved. The room remembers."
- "Closed the book. Page kept."
- "Filed. You can walk away now."

**Error.**
- "Something didn't take. Try the sentence again."
- "The back room is quiet. Wait, or come back."
- "That didn't save. Nothing's lost — but say it again."

**Narrative publish.**
- "Published. This is the version that leaves the house."
- "Locked. The claims have receipts. The receipts have rooms."
- "Out the front door. You can revise; you can't un-say."

**Contradiction surfaced.**
- "Two things you said don't sit next to each other. Vey would like a word."
- "There's a tension here. It might be the truth. It might be the seam."
- "You contradicted yourself. That's where the work is."

## 6. What this product is NOT

- "Let's craft your **leadership brand**!" — banned (PRD §4.4).
- "You're a **rockstar** at scaling teams." — I would walk.
- "Our AI **leverages** your experience to build a **robust** narrative." — three banned words; spine §9.
- "Great job!" / confetti / streaks / XP — coaching tone, banned.
- "Tell us about a time you **drove transformation**." — cliché.
- Any onboarding that uses *journey.*
- Any NPC who says "I'm here to help."
- Any system message that says "Oops!"

The product is an interlocutor, not a coach. A room, not a form. A question, not a template. If a line could appear on LinkedIn unchanged, it does not ship.
