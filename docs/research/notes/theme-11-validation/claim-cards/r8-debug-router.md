---
title: "Claim card R8 — debug-router"
status: draft
theme: theme-11-validation
surface_id: R8
aligned_with:
  - docs/research/reports/theme-17-debug-router.md
---

# R8 — debug-router

| Field | Value |
|-------|-------|
| Surface | `debug-router` |
| Authority | Theme 17 |
| Lane | either |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `debug-router` | R8 + R8-fresh | **pass** |
| C2 | Classifies prove-only vs investigate-fix | R8 + R8-fresh | **pass** |
| C3 | Default one entry leaf; optional prove-then-fix wire | R8 + R8-fresh | **pass** |
| C4 | Invokes leaf via Using …; does not paste Theme 9 spine | R8 + R8-fresh | **pass** |
| C5 | Intelligent skip when leaf already named | R8 + R8-fresh | **pass** |
| C6 | Refuses PR/merge ceremony | R8 + R8-fresh | **pass** |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Default two-step wire always | **no** |
| A2 | Burn Execute verify-retry under Debug | **no** |
| A3 | Guess-fix / skip iron law | **no** |

## Verdict

**PASS** — in-session `R8-20260802.md` + fresh `R8-fresh-20260802.md` (2026-08-02)

## Smoke

**Part A — prove-only:** “Using `debug-router`: I only need a minimal failing repro dossier for a flaky test — do not fix yet. Classify and wire.”

**Part B — investigate-fix:** “Using `debug-router`: Execute verify-fail after N=2; repro command already known. Route for investigate/fix.”

**Part C — negative:** “Using `debug-router`: debug this and open/merge a PR.” Expect refuse ceremony.

**Part D — skip:** “Using `debug-router`: just run `debug-reproduce` — I already chose it.” Expect intelligent skip to leaf.
