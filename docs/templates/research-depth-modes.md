---
title: "Research depth modes (normal vs deep)"
status: active
aligned_with: docs/PROTOCOL.md
created: 2026-07-29
---

# Research depth modes

Authority: Toolbelt `docs/PROTOCOL.md`. Used by skill `research-protocol`.  
Grades/labels/cite-or-omit still apply in **both** modes.

**Tracks unclear?** Use companion skill **`research-scope`** (Theme 12) to expand/atomize into tracks and suggest depth **before** deep waves. Depth mode does not invent tracks.

## Default

**`normal`** unless the user asks for deep/theme research, or the stated goal is a durable integrated report / method SoT redesign that needs multi-pass coverage.

Do **not** default to deep — cold agents must not burn context fleets on ordinary lookups.

## Modes

| Mode | When | Shape | Stop |
|------|------|-------|------|
| **normal** | Default; single question; smoke; one checklist/note | One gatherer (or short sequential pass); one note or graded checklist | Done when Method + findings cover the question, or GAPs listed |
| **deep** | User says deep / theme campaign; or goal = integrated report across many surfaces | Parallel gatherers by independent domain; waves (SoT → corroboration → residual GAPs); integrator merges only | **Diminishing returns** (below) |

Announce depth once in the Method block: `depth: normal | deep`.

## Deep campaign shape (when deep)

0. **Optional — invent tracks first** via **`research-scope`** when the idea is fuzzy (campaign brief / track board).  
1. **Pin identity** (D0 / product pin / scope) in a coordinator note.
2. **Wave 1 — primary SoT** (official docs, repo SoT, E0 local). One gatherer per independent domain; each writes a graded note (Method required).
3. **Wave 2 — corroboration** (RAG, web, high-signal GitHub) — reinforce or mark GAP; do not invent.
4. **Wave 3 — residual GAP closers** only for P0/P1 items that might still close with more search.
5. **Integrate** — merge notes into a draft report; no new facts; conflicts by higher grade; retain GAP/OPEN.

Short smoke inside deep is still allowed (graded checklist) for a single domain; the *campaign* is deep, not every atom.

## Hard stop rule (deep) — required

Stop spawning gatherers when **any** of:

- New notes only restate prior FACTS without closing a named GAP, **or**
- Remaining items need undocumented product behavior / E0 runtime experiments you are not running, **or**
- User-scoped budget (time/agents) is exhausted

Record the stop reason in the integrator Method / progress board. Prefer **confirmed GAP** over more weak E3.

## Caveats (do not ignore)

1. **Opt-in / goal-triggered only** — never auto-escalate “look this up” to a fleet.
2. **Stop rule is mandatory** — deep without diminishing-returns stop is context waste.
3. **Toolbelt owns deep dispatch + artifacts** — parallel gatherers, depth mode, templates, grades, and integrator merge. Do **not** import third-party git/PR/worktree packaging as Toolbelt law.
4. **`draft` / `proposed` ≠ SoT** — deep integrated reports stay non-authoritative until human acceptance (`draft-is-not-sot`).
5. **Cite-or-omit still binds** — parallel notes must not invent APIs/IDs; integrator does not invent either.
6. **Normal stays cheap** — if unsure, choose normal and list OPEN follow-ups.

## Method block fields (add when relevant)

| Field | Values |
|-------|--------|
| `depth` | `normal` \| `deep` |
| `stop_reason` | (deep) why waves stopped |
| `waves` | (deep) brief wave list / note IDs |
