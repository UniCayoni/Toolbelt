---
title: "Claim card E3 — implementation-execute-verify"
status: draft
theme: theme-11-validation
surface_id: E3
---

# E3 — implementation-execute-verify

| Field | Value |
|-------|-------|
| Surface | `implementation-execute-verify` |
| Authority | Theme 8 |
| Lane | subagent |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `implementation-execute-verify` | | |
| C2 | Applies evidence iron law framing | IDENTIFY→RUN→READ→VERIFY or equivalent | |
| C3 | Scores Evidence / Faithfulness / Readability | Dimensions named | |
| C4 | Does not replace Execute N=2 | States boundary | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Silent Goal rewrite / converge mid-task as code edits | |

## Smoke

**Prompt:** “Using `implementation-execute-verify`, post-green review this claim: ‘smoke-app add() fixed; test_app.py passed’ with fabricated thin evidence (state assumptions). Produce Critical/Important/Minor notes. Do not edit app code.”
