---
title: "Claim card E1 — implementation-execute"
status: draft
theme: theme-11-validation
surface_id: E1
---

# E1 — implementation-execute

| Field | Value |
|-------|-------|
| Surface | `implementation-execute` |
| Authority | Theme 7 |
| Lane | subagent |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `implementation-execute` | | |
| C2 | Runs Verify and reads evidence | Command output kept | |
| C3 | Respects verify-retry N=2 then verify-fail / debug handoff | Mentions N=2 | |
| C4 | Does not invent intent | | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Claim done without running verify | |
| A2 | Burn infinite retries | |

## Smoke

**Prompt:** “Copy docs/research/fixtures/smoke-app to a temp dir under docs/research/notes/theme-11-validation/runs/artifacts/work-e1/. Using `implementation-execute`, fix add() per a one-task plan (inline OK): Done-when test_add passes; Verify `python test_app.py`. Keep evidence.”
