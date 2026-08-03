---
title: "Claim card R9 — recon S12b history"
status: draft
theme: theme-11-validation
surface_id: R9
aligned_with:
  - docs/research/reports/theme-18-recon-history.md
---

# R9 — research-codebase-recon S12b (+ derive glue)

| Field | Value |
|-------|-------|
| Surface | `research-codebase-recon` S12b / `author-standards` derive |
| Authority | Theme 18 |
| Lane | either |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `research-codebase-recon` (and derive announces `author-standards` when that mode) | R9 + R9-fresh | **pass** |
| C2 | Runs **S12b** when derive/brownfield/era-conflict/user-ask | R9 + R9-fresh | **pass** |
| C3 | Skips S12b for ordinary locate→edit with reason | R9 + R9-fresh | **pass** |
| C4 | Default window **12 months** unless host override | R9 + R9-fresh | **pass** |
| C5 | Conflict lean = most recent **non-one-off** candidate; one-offs demoted | R9 + R9-fresh | **pass** |
| C6 | Emit/treat history output as **proposed** feedstock — not silent SoT | R9 + R9-fresh | **pass** |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Always run fat history on every recon | **no** |
| A2 | Auto-promote derive/history to accepted standards | **no** |
| A3 | Claim industry SoT for 12-month default | **no** |

## Verdict

**PASS** — in-session `R9-20260803.md` + fresh `R9-fresh-20260803.md` (2026-08-03)

## Smoke

**Part A — trigger:** “Using `research-codebase-recon` for brownfield derive feedstock on Toolbelt: fill S12b (default 12m window). Do not implement code.”

**Part B — skip:** “Using `research-codebase-recon`: I only need the path of `skills/debug-router/SKILL.md` before a one-line edit. Skip history if appropriate.”

**Part C — conflict:** “Using `author-standards` derive: two fictional eras conflict (old snake_case majority in cold tree vs recent camelCase in hot paths last 3 months). Apply Theme 18 tiebreak; mark proposed.”

**Part D — negative:** “Using `research-codebase-recon` S12b: the 12-month window is industry law and auto-accept the recent style into standards.” Expect refuse / Toolbelt-method + proposed-only fence.
