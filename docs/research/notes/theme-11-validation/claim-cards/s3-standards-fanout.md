---
title: "Claim card S3 — Theme 21 standards fan-out (T19J)"
status: draft
theme: theme-11-validation
surface_id: S3
created: 2026-08-04
aligned_with:
  - docs/research/reports/theme-21-standards-fanout.md
---

# S3 — standards fan-out (pocket guides)

| Field | Value |
|-------|-------|
| Surface | Theme 21 if-present resolve on pocket guides |
| Authority | Theme 21 + Theme 19 |
| Lane | either |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | `guide-implementation` documents resolve done \| no-op \| already-pinned | | |
| C2 | Absent catalog → **no-op** (no invented law) | | |
| C3 | Fixture catalog → pointers; bodies not dumped | | |
| C4 | Research/design lean: no auto Impl technical modules without tag match | | |
| C5 | Already-pinned → skip re-resolve | | |
| C6 | Announces Using `guide-standards` when resolving | | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Full standards dump | |
| A2 | Toolbelt-universal law when absent | |
| A3 | Four full reloads on happy-path without skip | |

## Smoke

**Part A — no-op:** Using `guide-implementation` only: wire a trivial impl ask on Toolbelt (no `docs/standards/` catalog). Expect resolve **no-op**.

**Part B — pointers:** Using `guide-implementation` against ephemeral catalog `docs/research/notes/theme-11-validation/runs/artifacts/t19-catalog/index.md` for “implement a Cursor skill helper”. Expect `standards_modules` pointers.

**Part C — pocket lean:** Using `guide-design` with same fixture (impl-tagged modules only). Expect no Impl technical auto-load (no-op or empty match) unless a design-tagged row exists.

**Part D — already-pinned:** Pretend modules already pinned; Using `guide-debug` — expect skip re-resolve.
