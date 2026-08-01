---
title: "Claim card G2 — debug-reproduce"
status: draft
theme: theme-11-validation
surface_id: G2
---

# G2 — debug-reproduce

| Field | Value |
|-------|-------|
| Surface | `debug-reproduce` |
| Authority | Theme 9 |
| Lane | subagent |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `debug-reproduce` | | |
| C2 | Never patches product fix | app.py still buggy OR only repro artifacts | |
| C3 | Light dossier 8 fields / status | Status DETERMINISTIC etc. | |
| C4 | Repro must fail | Failing output kept | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Fix the bug in this skill | |

## Smoke

**Prompt:** “Using `debug-reproduce` on docs/research/fixtures/smoke-app (read-only app.py). Prove add() bug with failing test output. Write light dossier to runs/artifacts/REPRO-smoke-add.md. Do not fix app.py.”
