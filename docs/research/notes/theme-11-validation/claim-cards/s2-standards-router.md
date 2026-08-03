---
title: "Claim card S2 — standards-router"
status: draft
theme: theme-11-validation
surface_id: S2
aligned_with:
  - docs/research/reports/theme-19-standards-apply.md
---

# S2 — standards-router (+ resolve gate)

| Field | Value |
|-------|-------|
| Surface | `standards-router` / `standards-resolve-gate` |
| Authority | Theme 19 |
| Lane | either |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `standards-router` when resolving | S2-20260803 | **pass** |
| C2 | Absent / unaccepted catalog → **no-op** (not invent law) | S2-20260803 | **pass** |
| C3 | Emits **module pointers** (`standards_modules`) not full rule dumps | S2-20260803 | **pass** |
| C4 | Classifier uses action/wording/skill/path (or documents lean) | S2-20260803 | **pass** |
| C5 | Refuses Toolbelt-universal coding law / pasting entire style guide | S2-20260803 | **pass** |
| C6 | Authoring still handed to `author-standards` | S2-20260803 | **pass** |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Dump full standards corpus into reply | **no** |
| A2 | Treat draft modules as accepted law | **no** |
| A3 | Act as global meta-router for all skills | **no** |

## Verdict

**PASS** (in-session) — fresh optional; await human review before commit.

## Smoke

**Part A — no-op:** “Using `standards-router`: which standards apply for editing `skills/debug-router/SKILL.md`?” (Toolbelt has no accepted host catalog.) Expect **no-op** / absent catalog.

**Part B — pointers (fixture):** Create ephemeral accepted catalog under `docs/research/notes/theme-11-validation/runs/artifacts/t19-catalog/` with one module; resolve for “author a Cursor skill”; expect pointers only.

**Part C — negative:** “Load every Toolbelt coding standard as always-on law into this chat.” Expect refuse / selective-load fence.
