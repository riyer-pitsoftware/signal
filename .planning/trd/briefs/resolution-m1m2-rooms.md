---
name: Resolution — Mara M1 + M2 (room-cut governance + Glasshouse role)
bead: BP-013.11 (signal-ne9)
date: 2026-05-10
authors: Dash (primary, owns room-as-metaphor) — pending Kenji collaborator concurrence at BP-014
governance: Rule B (lesson #8) — Soft spine constraint at `spine.md:164`
---

## ADR-class statement (lead)

**Signal v0.1 ships with six rooms because the room IS the metaphor for the user type, and decapitating user-type spatial coverage to save tilemap cost trades a Hard product principle (memory-palace as primary UI, ADR-002) against a Medium one (4-week build window).**

---

## 1. Decision — room count: **C. Reinstate Bridge + Switchyard → 6 rooms (full spine compliance).**

Rejected: A (hold at 4), B (5 rooms — Bridge only), D (other).

### 1.1 The four-room cut was a non-decision

Kenji's brief §1.5 ships four rooms; §2 acknowledges *"Spine asks ≥6 rooms; we ship 4 and promise the rest"* in a defer-list footnote. That sentence is the failure: it concedes the spine constraint without authoring the override. Rule B requires either (a) an explicit override doc with spine line, original value, new value, cost, justification, and judge-panel re-acknowledgment hook, or (b) reversal. Kenji's defer note is neither — it is governance theater.

This bead is the Rule B fork. We are choosing reversal.

### 1.2 Why M1 is right on the substance

Dash §2 binds each room to a PRD §5 user type. The binding is not decoration — it is the *first felt experience* a user has of "this product saw me." A technical program leader walking into a room labeled *Library* is not a TPL being interrogated by an Archivist with a related probe class. It is a TPL being told, in the medium most upstream of any dialogue line, that the product does not have a room shaped like their work.

Kenji's defense — *"each NPC owns one probe class; Cassady/Lenore can cover the probe needs from their resident rooms"* — is correct about probe classes and wrong about the level at which the metaphor binds. The probe is the *second* mechanic. The room is the *first*. PRD §6.3 names "intellectual flattening" — broad thinkers reduced to standardized archetypes — as a primary user problem. Routing a TPL through a Library because the Switchyard was deferred is a concrete instance of that flattening, executed by us, in our own product.

This is what spine §4 means by *"Memory-palace metaphor as primary UI — Hard reversibility, ADR-002."* The four-room cut was a Hard-reversibility partial-revert dressed as a Medium-cost scope trim. M1 caught it.

### 1.3 Why C, not B

Mara recommends 5 rooms — Bridge only. The argument: Bridge is the cheapest reinstate (Vesper §2:24 already routes Vey through the Bridge; no resident NPC required), and EM is the larger underserved cohort. True. But:

- **B still requires an override doc** — 5 < spine's ≥6. We trade one defended override (M1's specific framing) for another (5 rooms ships, where is the EM but not TPL).
- **Switchyard's marginal cost is the same shape as Bridge's** — Vesper §2:25 already specifies the layout (cables, dependency tags, the *ship* lever, log book). Dash §2 already specifies the theme (TPL: *"you kept the trains from hitting each other and almost nobody noticed"*). Neither requires a new NPC, new probe class, new dialogue line, or new event-protocol entry. Both require a tilemap + room state + room-state save/load entry.
- **The TPL user type is not residual.** Switchyard is mapped to the *technical program leader* — listed in PRD §5 as a primary user type alongside engineering manager. Holding at 5 reproduces M1's failure mode for half the offended cohort.
- **Sofia S2's demo-art risk is bounded by the Foyer.** The demo's first frame is the Foyer, per Sofia S2 (*"spend ~3 days art budget on the Foyer only — bespoke. Other rooms can stay placeholder."*). Adding two no-resident placeholder rooms does not change the demo's art surface — the demo doesn't visit them in 90 seconds.

C eliminates the override-doc burden, eliminates the spine violation, restores both underserved user types, and costs ~2 tilemaps + 2 room-state save/load slots. The cost rationale Kenji invoked was about *NPC headcount and dialogue lines* (Vesper §6 cuts the Boiler Room for that reason; we keep the Boiler Room cut). Tilemap-only rooms don't trip that budget.

### 1.4 Boiler Room stays cut

Vesper §6 is correct that the Boiler Room teaches nothing new and serves a small cohort (data/platform leaders) at the cost of simplicity. Six rooms — Foyer, Workshop, Bridge, Switchyard, Glasshouse, Library — meets spine §164's ≥6 threshold without absorbing Vesper's Q1/Q5 critique. Boiler Room remains a v0.2 named throwaway-extension, per Kenji §7.

---

## 2. Decision — Glasshouse role (M2): **A. Glasshouse stays a theme room (transformation lead). Vey drifts into ANY empty room equally.**

Rejected: B (Glasshouse becomes Vey's home), C (other).

### 2.1 The conflation Mara flagged is real

Kenji §1.5 frames Glasshouse as *"the empty-room default Vey drifts into."* Dash §2 binds it to *transformation lead*. These are two different UX contracts running through the same spatial slot.

When a transformation-lead user enters Glasshouse for the first time, the felt experience must be: *"this room was made for the work I do — slow change, organizational vines, dead-branches-labeled-departed-initiatives, rust on the watering can."* If Vey-as-default lives there, the felt experience is instead: *"this is where the contradiction-NPC waits for me."* The transformation lead's room becomes a tribunal.

That is exactly the failure mode PRD §6.3 names. We do not ship it.

### 2.2 Vey's drift is mechanically improved by 6 rooms, not damaged

Vesper §3 describes Vey's selection rule: *"Empty rooms: contradiction? → Vey."* The rule does not require Vey to have a fixed home. With six rooms, Vey now has *four* candidate drift targets — Bridge, Switchyard, Glasshouse (when its theme-resident-NPC isn't drifting in), and the unused-room-of-the-moment. More drift surface, not less. The "Vey drifts into any empty room equally" recommendation Mara made is *mechanically easier* under Option C than under the four-room cut.

### 2.3 Glasshouse's resident probe

Glasshouse has no resident NPC — it is a theme room, not a probe-class room. When a transformation-lead user is in the Glasshouse and a probe is needed, the selection rule (Vesper §3) governs: contradiction-shaped need → Vey drifts in; under-specified-claim need → Cassady drifts up from the Workshop; evidence-retrieval need → Lenore drifts up from the Library. This is the same routing that already governs Bridge and Switchyard. The Glasshouse is not special; it is one of three theme-only rooms.

The transformation-lead user's *primary* affordance in the Glasshouse is the room itself — the org-chart vines, the rust, the watering can. The artifact pinning, the room-remembers state. The probe is whichever NPC the routing calls in; the *room* is the felt-experience anchor.

---

## 3. Override doc — N/A

Option C is full spine compliance. No override required. The Rule B fork resolves cleanly toward reversal. This section exists to record that the choice was deliberate, not absent: holding at 4 was *available* and would have required the override doc per the bead spec. We chose not to author one because the cost-of-reinstatement (two tilemaps, two room-state slots, no new NPCs, no new probe classes, no new dialogue lines) was lower than the cost-of-defending the override against Mara M1's specific framing on the record.

For BP-014 audit: the spine line `spine.md:164` is *not* overridden. Original value (≥6 rooms aligned to PRD §5 user types) is preserved. The footnote at Kenji §2 (*"Spine asks ≥6 rooms; we ship 4 and promise the rest"*) is the historical artifact of the cut that was reversed by this bead; Kenji's brief needs revision per §5 below.

---

## 4. Cascade — Vesper / Marcus / budget

### 4.1 Vesper (`briefs/vesper.md`)

- **§2 spatial layout per room:** No edits required for Bridge or Switchyard — both already have explicit spatial layouts written. Boiler Room entry stays as-is (still cut per §6).
- **§3 NPC mechanic spec / selection:** Confirm Vey's drift now spans four candidate rooms (Bridge, Switchyard, Glasshouse, plus current-empty). No prose edit required if §3's selection rule is read as written.
- **§6 cut list:** Remove "Cut the Bridge's 'unlit half' as interactive geometry" — actually, leave this line as-is; it cuts the *unlit half as interactive geometry*, not the Bridge itself. The Bridge ships as a room; only the unlit-half interactivity remains cut. Confirm in BP-014.
- Minor edit may be required to §6 to remove the implicit "ship six; promise the hatch" framing if Vesper drafted it under the four-room assumption. Read: Vesper §6 already says "Ship six; promise the hatch" — meaning Vesper *originally* shipped six (Boiler cut). The four-room cut came from Kenji, not Vesper. So Vesper §2 + §6 are consistent with this resolution and need no edits. **Cascade flag for Kenji, not Vesper.**

### 4.2 Marcus (`briefs/marcus.md`)

- **§3 asset pipeline:** Tilemap count moves from "≤6" (current text reads "One map per room (≤6, BP-008)") to "= 6" — minor edit, no contract change. Asset budget headroom: 2 additional placeholder tilemaps recolored from Kenney/Mana Seed CC0. JS bundle budget (≤500 KB gzip) and asset budget (≤4 MB v0.1) absorb this without revision.
- **§1 state bridge contract:** No changes. `world.activeRoom` is `roomId|null`; the room set grows from 4 to 6 IDs. Zustand is content-agnostic.
- **§2 event protocol:** No changes. Event types are room-agnostic.
- **Cascade flag:** Marcus §3 line "One map per room (≤6, BP-008)" should be tightened to "One map per room, 6 rooms" at BP-014 synthesis. No urgent rewrite.

### 4.3 Budget impact (4-week window)

- **NPCs:** No change. Four NPCs (Marlow, Cassady, Lenore, Vey). Bridge and Switchyard are no-resident.
- **Dialogue lines:** No change. Bridge/Switchyard fire whichever NPC the routing rule calls in; that NPC's existing prompt-seed pool (5 per NPC, per Kenji §6 Q4) covers it.
- **Probe classes:** No change. Four probe classes; routing covers theme rooms.
- **Tilemaps:** +2 placeholder tilemaps (Bridge, Switchyard). Estimated ~1 day total at the placeholder fidelity Marcus §3 specifies (Kenney/Mana Seed CC0 recolor + Tiled object layer for spawn/anchor/slot points).
- **Room-state save/load:** +2 entries in Priya's `state_blob` per session (Bridge state, Switchyard state). Schema-trivial; no migration path needed (v0.1 hasn't shipped).
- **Event-protocol entries:** None. Existing events (`evidence.placed`, `npc.gesture`, `contradiction.surfaced`, `camera.focus`) are room-agnostic.

**Total estimated budget impact: ≤1.5 day Marcus + ≤0.25 day Priya. Absorbed inside the 4-week window without cutting any other §1 feature from Kenji's MVP.**

### 4.4 Glasshouse decision cascade

- **Dash NPC roster:** No change. Vey already drifts; Vesper §3 already covers selection. Dash §3 line *"Vey — the Cartographer. Drifts between rooms."* is consistent.
- **Vesper Vey mechanic:** No change. Vey's spec at §3 (`Refuses leading framing. Cannot appear unprompted by a real contradiction.`) is consistent.
- **Cascade flag for Kenji:** §1.5 frames Glasshouse as "empty-room default Vey drifts into." That framing was M2's specific objection. Kenji §1.5 needs revision per §5 below.

---

## 5. Cascade — Kenji's MVP cut (`briefs/kenji.md`)

The four-room cut was the load-bearing claim of Kenji §1.5 and §2. Reverting to six requires inline revision:

### 5.1 §1.5 revision (rooms + NPCs)
- **Current text:** *"Four rooms, four NPCs (Dash §2–§3, Vesper §2). Foyer (Marlow / outsider compression test), Workshop (Cassady / operational specificity), Library (Lenore / evidence retrieval), plus the **Glasshouse** as the empty-room default Vey drifts into."*
- **Revised text:** *"Six rooms, four NPCs (Dash §2–§3, Vesper §2). Foyer (Marlow / outsider compression test), Workshop (Cassady / operational specificity), Library (Lenore / evidence retrieval), plus three theme-only rooms — Bridge (engineering manager), Switchyard (technical program leader), Glasshouse (transformation lead) — into which Vey drifts on contradiction, Cassady drifts on under-specification, Lenore drifts on evidence need, per Vesper §3 selection. Boiler Room remains v0.2 (Vesper §6)."*

### 5.2 §2 defer-list revision
- **Remove:** *"Bridge, Switchyard, Boiler Room (Dash §2; Vesper §6 already cuts Boiler). No resident NPC, no probe type Cassady/Lenore can't cover from their resident rooms. Spine asks ≥6 rooms; we ship 4 and promise the rest."*
- **Replace with:** *"Boiler Room (Vesper §6). Data/platform leader spatial coverage deferred to v0.2. Cassady can be summoned via the hatch but does not have a resident bench in the Boiler Room. Bridge and Switchyard ship in v0.1 per BP-013.11 resolution."*

### 5.3 §4 scorecard adjustment
- The "Felt experience" row (15% weight, scored 7) should bump to **8** — the room-as-metaphor argument that was load-bearing in M1's objection now resolves cleanly. Notable risk note (third-return / tenth-visit pacing) remains.
- Weighted total moves from 8.5 to ~8.6. Above ship threshold, materially the same.

### 5.4 §7 sacrificial choices revision
- **Remove the row:** *"4 rooms instead of 6–7 | User-type addressable-base feedback shows TPL/transformation-lead under-served | Add Bridge + Switchyard + Glasshouse-as-distinct-room in v0.2"*
- This row is no longer a sacrificial choice — it is reversed. Replace with: *"Boiler Room (data/platform leader spatial theme) deferred to v0.2 | User-type addressable-base feedback shows data/platform leader under-served | Add Boiler Room with Cassady-resident-via-hatch mechanic"*

### 5.5 Disposition

Kenji to execute these inline revisions, OR flag them for BP-014 synthesis to absorb. Either path is acceptable; what is not acceptable is a silent contradiction between this resolution and `briefs/kenji.md` at the moment Haiku drafts the TRD (BP-015). **Recommend inline revision for clarity.** I do not own Kenji's brief and will not edit it from this bead — collaborator-side cascade only.

---

## 6. Coordination with adjacent open beads

- **signal-r1j (Ravi R1, F5 latency).** If F5 relaxes (Verdict B), per-room dwell time increases — this argues *for* more rooms, not fewer, since a longer turn budget makes the spatial palette feel less hurried. Six rooms is robust to the F5 outcome in either direction.
- **signal-b5x (Mara M3, first-90-seconds orientation).** The first room is the Foyer regardless of room count. This resolution does not alter the opener; it expands the palette beyond the opener. The first 90 seconds remain a Foyer-bounded design problem.

---

## 7. Judge-panel re-acknowledgment hook

Since Option C is full spine compliance, the panel re-ack burden is light:

- **Mara (UX):** M1 resolves at 6 rooms. M2 resolves at "Glasshouse stays thematic." Both serious objections accepted on the record.
- **Ravi (Tech):** No new model-call surface, no new RAM consumers, no new event-protocol entries. F5/F6 envelope unchanged.
- **Sofia (Demo):** Demo art surface unchanged (Foyer-bounded per S2). Two additional placeholder rooms exist outside the demo path.

Synthesis (BP-014) records this resolution as ADR-class:

> *"Signal v0.1 ships with six rooms (Foyer, Workshop, Bridge, Switchyard, Glasshouse, Library) because the room IS the metaphor for the user type, and the four-room cut substituted spatial coverage of two primary user types (engineering manager, technical program leader) for a tilemap-cost saving that was misclassified as a Medium-reversibility scope trim against the Hard-reversibility memory-palace metaphor (ADR-002). Vey drifts into any empty room equally; the Glasshouse remains a theme room for transformation-lead users."*

This is what BP-014 records. The ADR-class statement at the head of this document is the one-sentence form.
