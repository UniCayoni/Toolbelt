---
title: "Claim card E2 — implementation-execute-subagents"
status: draft
theme: theme-11-validation
surface_id: E2
---

# E2 — implementation-execute-subagents

| Field | Value |
|-------|-------|
| Surface | `implementation-execute-subagents` |
| Authority | Theme 7 |
| Lane | subagent |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `implementation-execute-subagents` | | |
| C2 | Controller vs worker split described/followed | Worker one pocket | |
| C3 | Same spine as execute (verify evidence) | | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Give worker full happy-path | |

## Smoke

**Prompt:** “Using `implementation-execute-subagents`, act as controller only: write a worker brief for fixing smoke-app add() off-by-one (one task). Do not implement yourself. Show what the worker skill should be (`implementation-execute` only).”
