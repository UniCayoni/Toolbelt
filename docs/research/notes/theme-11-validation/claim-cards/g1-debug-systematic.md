---
title: "Claim card G1 — debug-systematic"
status: draft
theme: theme-11-validation
surface_id: G1
---

# G1 — debug-systematic

| Field | Value |
|-------|-------|
| Surface | `debug-systematic` |
| Authority | Theme 9 |
| Lane | subagent |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `debug-systematic` | | |
| C2 | Reproduce before fix (or NOT-YET) | Repro steps | |
| C3 | Hypothesis falsify with evidence | Table or statuses | |
| C4 | Separates debug-fix-cycles from Execute N=2 | Mentions distinction | |
| C5 | Verify same repro after fix | Re-ran test | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Fix from code-read alone without repro | |
| A2 | Invent Cursor private debug-server API | |

## Smoke

**Prompt:** “Copy smoke-app to runs/artifacts/work-g1/. Using `debug-systematic`, investigate failing test_app.py (add off-by-one). Reproduce, hypothesize, fix minimally, re-verify. Do not invent Cursor private APIs.”
