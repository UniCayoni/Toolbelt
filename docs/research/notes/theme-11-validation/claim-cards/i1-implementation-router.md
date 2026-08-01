---
title: "Claim card I1 — implementation-router"
status: draft
theme: theme-11-validation
surface_id: I1
aligned_with:
  - docs/research/reports/theme-14-pocket-routers.md
---

# I1 — implementation-router

| Field | Value |
|-------|-------|
| Surface | `implementation-router` |
| Authority | Theme 14 |
| Lane | either (controller / pocket) |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `implementation-router` | I1-20260731 | **pass** |
| C2 | Classifies impl ask (full-ladder / plan-only / execute / …) | I1-20260731 | **pass** |
| C3 | Emits wire plan with explicit skips (N/A) | I1-20260731 | **pass** |
| C4 | Structured handoff fields present | goal/prior/facts/open/constraints | **pass** |
| C5 | Compose only — links leaves, does not paste Plan/Execute spines | I1-20260731 | **pass** |
| C6 | Selection ≠ solving — does not write plan tasks or implement | I1-20260731 | **pass** |
| C7 | On clear single-leaf ask, documents skip of router (or notes leaf-direct OK) | Part C | **pass** |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Restate Theme 6–8 pocket law inline | **no** |
| A2 | Become a second `implementation-plan` (decompose WBS here) | **no** |
| A3 | Force full ladder when ask is verify-only / execute-only | **no** |
| A4 | Treat draft design as accepted law | **no** |

## Verdict

**PASS** (2026-07-31 Theme 14 delta)

## Smoke

**Part A — full feature wire:** “Using `implementation-router`: design for smoke-app add() fix is accepted at `docs/design/smoke-add-design.md` (hypothetical). Wire Implementation pocket only; checklist + handoff; do not plan or code.”

**Part B — verify-only:** “Using `implementation-router`: Meta ready plan exists; greens done; need EOP execute-verify only. Wire; do not implement.”

**Part C — negative / skip:** “Using `implementation-router`: only run `implementation-plan-verify` on the existing plan. Wire or document leaf-direct.”
