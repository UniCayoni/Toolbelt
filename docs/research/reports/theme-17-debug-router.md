---
title: "Theme 17 — Debug router (integrated report)"
status: accepted
theme: theme-17-guide-debug
created: 2026-08-02
updated: 2026-08-02
accepted: 2026-08-02
acceptance_scope: method_guidance_t17_debug_router
accepted_by: human (Jonathan)
authors: [integrator]
depth: normal
stop_reason: normal_wave_sufficient_lean_locks_accepted
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-17-guide-debug/campaign-brief.md
  - docs/research/notes/theme-17-guide-debug/pre-start-considerations.md
  - docs/research/notes/theme-17-guide-debug/t17a-local-baseline.md
  - docs/research/notes/theme-17-guide-debug/t17b-classifier-matrix.md
  - docs/research/notes/theme-17-guide-debug/t17c-e-shape-wire-smoke-lean.md
  - docs/research/reports/theme-14-pocket-routers.md
  - docs/research/reports/theme-9-debug-pocket.md
supersedes: null
amends:
  - docs/research/reports/theme-14-pocket-routers.md  # D4: defer guide-debug → shipped
  - docs/research/reports/theme-10-happy-path.md  # Debug stage → guide-debug
---

# Theme 17 — Debug router

**Status:** **accepted** (method guidance) — 2026-08-02.  
**Elevated:** via `/author-cursor-surfaces` — `guide-debug` + template; happy-path / impl-router wire; Execute repro-first note.  
**Depth:** normal (Theme 14 feedstock reused; no deep fleet).  
**Lean locks:** accepted 2026-08-02 (`pre-start-considerations.md`).  
**Using `research-protocol`** · integrator.

## 1. Executive summary

Complete the Theme 14 router layer for Debug: ship **`guide-debug`** as compose-only classify + wire over Theme 9 leaves. Happy-path and `guide-implementation` hand off here; Execute keeps a direct-leaf hot path with a repro-first rule.

## 2. Elevation decisions (accepted)

| # | Decision |
|---|----------|
| D1 | Theme id **`theme-17-guide-debug`**; amends Theme 14 **D4** (defer → ship) |
| D2 | Skill **`guide-debug`**; discoverable (no `disable-model-invocation`) |
| D3 | Template **`docs/templates/guide-debug.md`** (+ refresh → skill references) |
| D4 | **Compose-only** — Theme 9 owns method law; selection ≠ solving |
| D5 | Classifier: **entry leaf** default; optional wire `debug-reproduce` → `debug-systematic` only for explicit prove-then-fix / T-NYR |
| D6 | Intelligent skip when user already named a leaf |
| D7 | **Seams:** happy-path + impl-router → `guide-debug`; Execute/-verify/-subagents → **direct leaf OK** + repro-first (no solid repro → reproduce; repro in hand → systematic; router when path unclear) |
| D8 | Structured handoff fields (same family as impl-router) |
| D9 | Parks unchanged: global meta-router, swarm, collectors, PR/CI ceremony, always-on debug rule |
| D10 | Elevate via **`author-cursor-surfaces`**; smoke **R8** in-session + fresh |

## 3. Layer model (after elevate)

| Pocket | Router / entry |
|--------|----------------|
| Research | `guide-research` (de facto) |
| Design | `guide-design` (de facto) |
| Implementation | `guide-implementation` |
| Debug | **`guide-debug`** |
| Cross-pocket | `implementation-happy-path` |

## 4. Acceptance checklist (human)

- [x] Campaign scope accepted — 2026-08-02  
- [x] Lean locks accepted — 2026-08-02  
- [x] Normal wave T17A–E — 2026-08-02  
- [x] Human accepts this report (D1–D10) — 2026-08-02  
- [x] Elevate + wire + packs/CHANGELOG via `author-cursor-surfaces`  
- [x] Smoke R8 **2/2 PASS** (2026-08-02)  
- [x] Sync + push (noreply)  
