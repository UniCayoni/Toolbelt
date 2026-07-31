---
title: "Claim card P1 — implementation-plan"
status: draft
theme: theme-11-validation
surface_id: P1
---

# P1 — implementation-plan

| Field | Value |
|-------|-------|
| Surface | `implementation-plan` |
| Authority | Theme 6 |
| Lane | subagent |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `implementation-plan` | | |
| C2 | Tasks have Done-when + Verify command→signal | | |
| C3 | Meta status vocab ready/in_progress/blocked/done | | |
| C4 | Points to plan-verify before ready | | |
| C5 | No TBD placeholders in tasks | | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Implement the fix in this smoke | |
| A2 | Treat unapproved design as law without noting | |

## Smoke

**Prompt:** “Using `implementation-plan`, write a durable mini-plan to fix smoke-app add() off-by-one. Path: docs/research/notes/theme-11-validation/runs/artifacts/smoke-fix-add-plan.md. Assume human accepted design ‘fix return a+b’. Include one task with Verify: python test. Meta status draft/ready per skill — leave ready only after noting plan-verify needed.”
