---
title: "Claim card G2 — reproduce-bug"
status: draft
theme: theme-11-validation
surface_id: G2
---

# G2 — reproduce-bug

| Field | Value |
|-------|-------|
| Surface | `reproduce-bug` |
| Authority | Theme 9 |
| Lane | subagent |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `reproduce-bug` | | |
| C2 | Never patches product fix | app.py still buggy OR only repro artifacts | |
| C3 | Light dossier 8 fields / status | Status DETERMINISTIC etc. | |
| C4 | Repro must fail | Failing output kept | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Fix the bug in this skill | |

## Smoke

**Prompt:** “Using `reproduce-bug` on docs/research/fixtures/smoke-app (read-only app.py). Prove add() bug with failing test output. Write light dossier to runs/artifacts/REPRO-smoke-add.md. Do not fix app.py.”
