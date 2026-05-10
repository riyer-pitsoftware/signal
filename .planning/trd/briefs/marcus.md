---
name: Marcus — Frontend Brief
bead: BP-007 (signal-0t6)
date: 2026-05-09
---

Phaser 3 canvas hosts C4 (World & Spatial, spine §2); a React 18 overlay handles C1/C3 text-heavy surfaces. The layers never touch each other — they touch a Zustand store and an event bus. That isolation is the contract.

## 1. State bridge contract

`useSignalStore` is the only shared mutable surface. Slices, with write/read ownership:

| Slice | Shape | Phaser w/r | React w/r |
|---|---|---|---|
| `world.player` | `{ roomId, x, y, facing }` | w/r | -/r (minimap) |
| `world.activeRoom` | `roomId\|null` | w/r | -/r |
| `world.activeNPC` | `npcId\|null` | w/r (proximity) | w/r (close→null) |
| `dialogue.stream` | `{turnId, tokens[], status}` | -/r (typewriter) | w/r (net handler) |
| `dialogue.history` | `Turn[]` (cap 50, paged via Priya) | - | w/r |
| `evidence.items` | `Artifact[]` | -/r | w/r |
| `evidence.placements` | `Map<id,{roomId,x,y}>` | w/r (drag-in) | w/r (drag-out) |
| `narrative.draft` | `{claims, version, status}` | - | w/r |
| `session` | `{id, modelTier, latencyHint}` | -/r | -/r |

Phaser scenes subscribe via `useSignalStore.subscribe(selector, fn)` in `create()`, unsubscribe in `shutdown()`. React uses the hook. Mutations route through typed actions (`setActiveNPC`, `appendDialogueToken`, `placeArtifact`) — no direct `set()` from view code. Spine §1.4 forbids external sync; persistence is a one-way snapshot to Priya's `/session/save`.

## 2. Event protocol

Store holds *state*; a typed `mitt` bus (`gameEventBus`) carries *one-shot signals* the canvas reacts to without re-render dances.

```ts
type GameEvent =
  | { t:'dialogue.token';        turnId:string; text:string; idx:number }
  | { t:'dialogue.complete';     turnId:string; fullText:string }
  | { t:'dialogue.error';        turnId:string; reason:string }
  | { t:'contradiction.surfaced'; claimId:string; against:string; severity:'soft'|'hard' }
  | { t:'evidence.placed';       artifactId:string; roomId:string; x:number; y:number }
  | { t:'npc.gesture';           npcId:string; gesture:'lean'|'pause'|'frown'|'nod' }
  | { t:'camera.focus';          target:{kind:'npc'|'artifact'|'room';id:string}; ms:number };
```

Flow per interrogator turn (F5, spine §3):

1. React opens stream (§4). Within 200ms: NPC plays `pause` on optimistic dispatch. **Perceived latency starts here, not at first token** — how F5 p50 ≤ 4s is reachable when inference averages ~3s.
2. Tokens → `appendDialogueToken` → `dialogue.token` emit. Phaser typewriter at fixed 45 chars/sec; bursts buffer, never speed past readable. React DialoguePanel mirrors via store subscription.
3. Suki's tagged tokens (`<contradiction id=...>`) are stripped from the visible stream by the network handler and re-emitted as `contradiction.surfaced`. Phaser tints the artifact; React queues a margin annotation.
4. `dialogue.complete` commits to history; optional `camera.focus` if Suki returned a `focus_hint`.

Frame budget: 60 fps on M3 24GB; 30 fps degraded below 16 GB (Devon's matrix, BP-011). Selectors scoped per-subscriber to avoid full-store thrash.

## 3. Asset pipeline

- **Tilemap source:** Tiled `.tmx` with embedded tileset, exported to JSON at build time. One map per room (≤6, BP-008). Object layer carries spawn points, NPC anchors, artifact slots — read by name, no magic numbers.
- **Sprite spec:** 32×32 base tile, 64×96 NPC sprites, 4-frame idle + 4-frame talk loop. Indexed PNG against BP-010's palette so recolors are cheap.
- **Build flow:** Vite bundles JS/CSS/fonts and copies `public/assets/**` verbatim. Phaser `preload()` loads from `/assets/` (relative — FastAPI serves the same static dir, spine constraint). **Budgets:** JS ≤ 500 KB gzip (Phaser ~280 KB), assets ≤ 4 MB v0.1. Fonts self-hosted woff2 — no Google Fonts (F2, spine §3).
- **Placeholder v0.1:** Kenney 1-bit / Mana Seed CC0 recolored to BP-010 palette; NPCs as silhouette + accent. Vesper signs off on legibility before bespoke art lands.

## 4. Transport choice — **SSE**, not WebSocket

Dialogue is server-push-dominant: user posts a turn, server streams tokens back. Bidirectional duplex buys nothing — Vesper's loop has the user *wait and read*, no useful mid-turn input. Picks:

- **SSE** at `/turn/stream`. Native `EventSource` reconnect, HTTP/1.1, debuggable in devtools, no framing layer. Backpressure is the kernel's problem.
- **REST** for everything else: `/session`, `/evidence`, `/narrative/draft`, `/narrative/publish`. Idempotent, cacheable, easy to test.
- **No WebSocket.** Adds framing, reconnect logic, and a second mental model for the same data. F5 p50 ≤ 4s is dominated by inference, not transport — SSE adds ≤ 5 ms over REST. If we ever need client→server mid-turn (e.g., "stop"), `POST /turn/{id}/cancel` is enough.

Reconnect: `EventSource` auto-reconnects; server replays from last `event-id` if the turn is live, else `204` and the client falls back to history fetch.

## 5. Component layer

**React (DOM):** `DialoguePanel` (active turn + history), `EvidenceDrawer` (artifact CRUD, drag source), `NarrativeEditor` (claim list, contradiction margin, publish button — F1/F8 gated by Priya), `MapMinimap` (read-only, derived from `world`), `SettingsSheet` (model tier, reduced-motion).

**Phaser (canvas):** room rendering, player + NPCs, artifact sprites, ambient motion, camera, drop-targets for artifacts dragged from the React drawer (HTML5 drag → canvas hit-test via shared coords). Text *inside* the world stays short (speech bubbles, room labels); anything ≥ 2 paragraphs lives in React.

## 6. Reversibility tags

| Decision | Tier |
|---|---|
| Zustand as bridge | Easy — swap behind action API |
| `mitt` event bus | Easy |
| SSE transport | Easy — WebSocket adapter is a day's work |
| Tiled `.tmx` source | Easy — LDtk swap later |
| Phaser 3 (spine §4) | Medium |
| Vite + FastAPI static colocate | Medium |
| Store schema shape | Medium — migrates with saved sessions |
| Memory-palace as canvas (vs DOM) | Hard — ratifies ADR-002 |

## 7. Open questions

- **Priya:** exact `POST /turn` shape, SSE `event-id` semantics, `/session/save` snapshot format, claim/artifact ID stability across versions.
- **Suki:** token framing — raw text vs JSON-per-event? How are `contradiction` / `focus_hint` tags emitted (inline sentinel vs separate event)? First-token latency target so I can size the optimistic-gesture window.
- **Vesper:** does mid-turn input exist? Does the player move during dialogue or freeze? Drives whether camera is store- or scene-driven.
- **design-for-ai (BP-010):** palette hex values, motion easing, reduced-motion fallbacks, focus-ring spec across the React/Phaser boundary.
- **Dash:** is `lean/pause/frown/nod` enough gesture vocabulary, or do specific NPCs need bespoke beats?

## 8. Sacrificial choices (v0.1)

| Choice | Trigger | Replacement |
|---|---|---|
| Single Zustand store, no slicing lib | >12 slices or perf regression | Zustand `slices` or split stores per context |
| `mitt` event bus | Need replay/inspector | xstate or typed broker with devtools |
| Placeholder CC0 tilesets | Commissioned art lands | Vesper-approved bespoke tiles |
| `dialogue.history` cap of 50 in memory | Sessions exceed cap | Paged fetch from Priya, virtualized list |
| HTML5 drag-to-canvas | Touch/tablet support | Pointer Events + Phaser `Input.dragstart` parity |
| Single-bundle Vite build | Initial load >2s on 16GB tier | Route-split + Phaser lazy `import()` |
