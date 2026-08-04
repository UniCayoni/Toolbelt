---
title: "Theme 19 — Standards application (integrated report)"
status: accepted
theme: theme-19-standards-apply
created: 2026-08-03
updated: 2026-08-03
accepted: 2026-08-03
acceptance_scope: method_and_elevate_t19_standards_apply
accepted_by: human (Jonathan)
authors: [integrator]
depth: deep
stop_reason: diminishing_returns_plus_2_w3p2_diminishing
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-19-standards-apply/campaign-brief.md
  - docs/research/notes/theme-19-standards-apply/t19i-shape-options-lean.md
  - docs/research/notes/theme-19-standards-apply/deep-campaign-board.md
  - docs/research/reports/theme-16-host-standards.md
  - docs/research/reports/theme-14-pocket-routers.md
supersedes: null
amends:
  - docs/research/reports/theme-16-host-standards.md  # D10/D12 apply layer — pending elevate
---

# Theme 19 — Standards application

**Status:** **accepted** (method + elevate) — 2026-08-03.  
**Scope** + **O1 lean** + **D1–D11** accepted 2026-08-03.  
**Depth:** deep (`diminishing_returns_plus_2`).  
**Using `author-cursor-surfaces`** for surface edits.

## 1. Executive summary

Theme 16 shipped **host standards feedstock** and soft Plan/Execute/Closeout bind. Theme 19 adds an **application process**: thin ambient **resolve gate** → small **`guide-standards`** → **catalog/module pointers** → selective load — so agents do **not** stuff full standards into every context. Not writing Toolbelt coding-style content. Pocket-router fan-out of the same gate is **later** (T19J).

## 2. Elevation decisions (accepted)

| # | Decision |
|---|----------|
| D1 | Theme id **`theme-19-standards-apply`** |
| D2 | Shape **O1** (accepted lean): skill **`guide-standards`** + catalog template + thin ambient rule |
| D3 | **Compose-only** router: classify → `standards_modules[{id,path,reason}]`; do not paste module bodies; selection ≠ authoring |
| D4 | **Catalog template** under `docs/templates/` (e.g. standards-catalog + module stub); one-file Theme 16 profile remains valid as a **single module** |
| D5 | **Ambient gate** rule `alwaysApply: true`, body thin: if no accepted catalog/modules → **no-op**; else resolve via `guide-standards` (or equivalent invoke). Never embed full standards in the rule |
| D6 | **Amend Theme 16 D12:** forbid always-on *standards bodies*; allow always-on *resolve gate* |
| D7 | Keep **`author-standards`** for principles / standards / derive / bind-check; D10 Plan/Execute/Closeout bind remains |
| D8 | Classifier dimensions: action, wording, skill id, path globs, perceived intent (ask or core-only when ambiguous) |
| D9 | Subagent/Task: pass `standards_modules` in handoff; child loads paths; re-resolve if missing |
| D10 | Smoke **S2** (or next free id): classify→pointers; absent no-op; refuse Toolbelt-universal law / full dump |
| D11 | Parks: writing host style content; global meta-router; dual-era schema v2; expanding apply into other pocket routers (**T19J later**) |

## 3. Evidence summary (cite-or-omit)

| Channel | Support for O1 | Key locators |
|---------|----------------|--------------|
| Local E0 | Soft bind only today; no router/catalog/ambient standards rule | T19A; Theme 16 D10/D12 |
| Cursor / peers primary | Thin rules; don’t copy entire style guides; skills `references/` progressive; Claude/Codex keep AGENTS small | T19E |
| RAG | Context engineering: select relevant context; Librarian/style-guide lookup; registry/catalog | T19F (`6daf3081…`, `4b9a08fc…`, `d51865d1…`) |
| GitHub | Catalog indexes; thin AGENTS pointers; path globs; “read X when Y”; **agentops `skills/standards`** selective load (“do not preload entire corpus”) | T19G S1–S10 |
| GAP | No widespread public skill id `guide-standards`; empty-catalog no-op is Toolbelt design | T19G / T19E |

## 4. Deep method

| Field | Value |
|-------|-------|
| stop_rule | `diminishing_returns_plus_2` |
| stop_reason | W3+2 diminishing — residuals are design locks, not missing primary evidence |
| Notes | Normal T19A–D, T19I; deep T19E–H; `deep-w3p1` / `deep-w3p2`; board |

## 5. Acceptance checklist (human)

- [x] Campaign scope accepted — 2026-08-03  
- [x] O1 lean accepted — 2026-08-03  
- [x] Deep gather stopped under `diminishing_returns_plus_2` — 2026-08-03  
- [x] Human accepts this report (D1–D11) — 2026-08-03  
- [x] Elevate via `/author-cursor-surfaces` (apply surfaces only)  
- [x] Smoke S2 in-session **PASS** (`S2-20260803.md`); fresh optional  
- [x] Sync + push — after human review 2026-08-03  
