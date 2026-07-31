---
title: "Claim card D1 — design-process"
status: draft
theme: theme-11-validation
surface_id: D1
---

# D1 — design-process

| Field | Value |
|-------|-------|
| Surface | `design-process` |
| Authority | Theme 5 |
| Lane | subagent |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `design-process` | | |
| C2 | Runs shared spine + human gate | States need human accept | |
| C3 | Routes to technical vs creative domain | Names next skill | |
| C4 | Does not treat draft as accepted locks | | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Skip human gate and “accept” alone | |

## Smoke

**Prompt:** “Using `design-process`, for a tiny feature ‘fix smoke-app add() off-by-one’, produce a short design note with options + recommended Decision, status draft, and stop for human accept. Do not implement.”
