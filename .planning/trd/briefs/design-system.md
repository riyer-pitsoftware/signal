---
name: Visual System Brief (design-for-ai lineage)
bead: BP-010 (signal-16f)
date: 2026-05-09
---

## 1. Mood anchor

Late-evening study: the room a careful person sits in to remember work, alone, with one warm lamp and weather outside. References: ochre-under-tungsten interiors of *In the Mood for Love* (Doyle/Wong, 2000); the archival paperwork texture of *The Conversation* (Murch, 1974); New Directions paperbacks in the Alvin Lustig era (1945–55); Hammett-era pulp on uncoated stock, sun-yellowed (dash.md §4); and the dusk palette of *Kentucky Route Zero* Act III interiors — desaturated teal shadow against a stove-warm key. Working synonyms (spine §9 bans the obvious): *quiet, lived-in, low-lit, paperish.* (PRD §4.4; dash.md §1.)

## 2. Type system

Three families, all self-hosted under `/public/fonts/` — no remote CDN (F2 hard, spine §3).

- **Narrative prose (NPC dialogue, room descriptions): EB Garamond 12 / fallback iA Writer Quattro.** Humanist serif cut for small body sizes; x-height ~0.52em, moderate stroke modulation. Reads as "private notebook in a public archive" (dash.md §4). Not Adobe Garamond — Kadavy ch. 3, humanist serifs render thin under 16px on 1× pixel grids; EB Garamond 12 survives the squint test where Adobe's cut does not.
- **System messages (the building): Inter v4 variable.** Realist sans, optical sizing on, Display ≥21px / Text ≤16px. Realist↔humanist is intentional contrast (Kadavy appendix): serif for *voiced characters,* sans for the *third-person narrator.* Helvetica rejected — collides at small UI sizes.
- **Evidence + metadata + claim refs: Berkeley Mono / fallback IBM Plex Mono.** Slab-tinted mono, generous counter, low contrast. Signals *artifact,* not chat. JetBrains Mono rejected — too geometric, reads IDE-chrome.

**Type scale (3:4, Kadavy ch. 7):** 12 / 14 / 16 / 18 / 21 / 28 / 37 px — seven sizes. Body 16px / line-height 1.45 (above 1.4 because serif body in a low-lit palette wants air). Hierarchy skips a rung — ≥25% jumps. Tailwind tokens `text-xs/sm/base/lg/xl/2xl/3xl` map to this scale, *not* defaults. Authentic weights only. Smart quotes + en/em dashes via remark plugin at build.

## 3. Color system

Five anchors, expressed in OKLCH (HSL lies about lightness; Kadavy ch. 8):

- `--ink` `oklch(22% 0.02 60)` ≈ `#2A241E` — warm dark, primary text. Not `#000`.
- `--paper` `oklch(96% 0.01 85)` ≈ `#F5F1E8` — uncoated-stock background, slight yellow cast.
- `--lamp` `oklch(78% 0.13 75)` ≈ `#D9A864` — tungsten ochre. Single accent. CTAs, focus rings, the lit lamp.
- `--shadow` `oklch(38% 0.03 240)` ≈ `#4A5568` — cool gray-blue, secondary text and recessed surface. Hue-shifted *cooler* than `--ink` so warm/cool depth holds (Kadavy ch. 9).
- `--ember` `oklch(52% 0.18 28)` ≈ `#B14A3D` — muted brick, reserved for contradiction surfacing (Vey; PRD §7.6). Not error-red — desaturated, no urgency theater.

Scheme: **analogous warm with cool secondary** — yellow-orange to red-orange wedge, plus one cool gray for hierarchy. Complementary at this saturation reads branded; analogous reads inhabited.

**Semantic mapping (Tailwind theme tokens):** `bg`→`--paper`, `fg`→`--ink`, `muted`→`--shadow`, `accent`→`--lamp`, `alert`→`--ember`, `surface`→`oklch(93% 0.012 80)`.

**Contrast (WCAG2):** ink/paper **12.4:1** (AAA). shadow/paper **6.1:1** (AA). lamp/ink button **8.2:1**. ember/paper **5.8:1**.

**Per-room shifts** (C4; dash.md §2). Base holds; rooms shift `--paper` ±4% L, ±10° H:
- Boiler Room `oklch(92% 0.02 65)` — warmer, pipe-lit.
- Library `oklch(96% 0.008 95)` — paler, greener-yellow, reading-lamp neutral.
- Glasshouse `oklch(94% 0.02 130)` — faint chlorophyll cast.
- Foyer base; Workshop / Bridge / Switchyard ±2% L, hue held.

Chroma capped at 0.13 anywhere text is read. The saturation pop a brand palette would reach for is foreclosed.

## 4. Motion principles

The world barely moves. Animates: typewriter, NPC idle, room transitions. Still: the room, the type, the cursor between turns.

- **Dialogue typewriter:** 28ms/glyph, jittered ±6ms (a hand chooses words, dash.md §4). Per-line fade-in `cubic-bezier(0.22, 1, 0.36, 1)`, 220ms. Not 16ms machine-gun — that reads as LLM streaming.
- **NPC idle:** 4–7s loop, 2px translateY breath, opacity 0.95↔1.0; `cubic-bezier(0.45, 0, 0.55, 1)`. Per-NPC amplitude (Vesper ratifies).
- **Room transitions:** 480ms cross-dissolve, 80ms hold on `oklch(15% 0.01 60)` mid-frame — a felt threshold. `cubic-bezier(0.65, 0, 0.35, 1)`.
- **Phaser camera pans:** 240 px/s linear, ≤1.2s. No spring overshoot — the building is heavy.
- **Reduced motion** (`prefers-reduced-motion: reduce`): typewriter→instant; idle→static; transitions→1-frame cut.

## 5. Accessibility floor (v0.1)

- Contrast: AAA body, AA secondary, AA accent (numbers §3).
- Keyboard: every NPC, evidence panel, claim-edit reachable via Tab; focus ring `--lamp` 2px outline + 2px offset, never removed. Phaser overlay traps focus until dismissed.
- Screen reader: dialogue → visually hidden `aria-live="polite"`; evidence panels `<article>` + `<header>` + linked claim IDs; canvas `aria-hidden="true"` — the world doesn't narrate, the dialogue does.
- Minimums: 14px metadata, 16px prose. User zoom respected.
- **Not in v0.1:** i18n (LTR only), dyslexia-friendly font toggle, high-contrast theme (palette too load-bearing — v0.2), full WCAG 2.2 audit. Named throwaways (spine §5).

## 6. The "not an AI app" tells

Five conventions avoided (Mara's mute test):

1. **Gradient hero buttons / blue-violet sparkles.** Instead: solid `--lamp` on `--paper`. No gradients except the 480ms cross-dissolve.
2. **Orb/avatar circles for the assistant.** Instead: NPCs are pixel-art figures placed *in the room,* not floating heads in a chat sidebar.
3. **"Send message" + paper-airplane glyph.** Instead: plain text field; the lamp glows when focus lands; submit is Enter; the glyph is a period.
4. **Markdown bullet lists, emoji glyphs in UI chrome.** Instead: dialogue is plain prose, one paragraph per turn, typewriter-served. Zero emoji in UI.
5. **"Powered by [model]" / "AI may make mistakes" boilerplate.** Instead: a single system-voice line — "The building is listening. It can be wrong." — only when relevant.

Bonus sixth: no dark-mode-with-neon toggle. The default *is* dim-warm; there is no "AI dashboard mode."

## 7. Open questions

- **Marcus:** Can shadcn's `<Dialog>` / `<Popover>` accept a non-default backdrop without fighting Radix z-index? Surface tokens need to inject into `theme.css`, not override per-component.
- **Vesper:** Idle amplitude per NPC — does Lenore breathe, or hold pure stillness with a 200ms blink every 8s? Mechanic question.
- **Dash:** Ratify §1 references and `--ember` for contradiction. If Vey reads "alarm" rather than "seam," chroma drops 10%.
