---
title: "Light repro dossier (Toolbelt)"
status: active
aligned_with: docs/research/reports/theme-9-debug-pocket.md
created: 2026-07-30
---

# Light repro dossier

Authority: Theme 9 accepted. Used by skill `debug-reproduce`. Prefer host path `docs/repro/<slug>.md` or `REPRO.md` at repo root when writing artifacts.

**Status line (required):** `DETERMINISTIC` | `RATE-BASED (n/N)` | `NOT-YET-REPRODUCED`

| # | Field | Notes |
|---|-------|-------|
| 1 | **Status** | Never oversell |
| 2 | **Symptom** | Expected vs actual (+ frequency if known) |
| 3 | **Command / steps** | Exact repro the fixer can run |
| 4 | **Failing output** | Verbatim excerpt |
| 5 | **Load-bearing triggers** | Short list or `unknown` |
| 6 | **Hypothesis ledger** | Append-only: open / killed (+ killer observation) |
| 7 | **Attempt #0+** | At least runnability / first repro attempt |
| 8 | **Handoff acceptance** | “Fix done when this repro turns green” (or monitoring if NOT-YET) |

**Park (not required):** long evidence timeline tables; environment encyclopedia; deep-plan coupling.
