---
title: "Claim card R3 — research-docs"
status: draft
theme: theme-11-validation
surface_id: R3
---

# R3 — research-docs

| Field | Value |
|-------|-------|
| Surface | `research-docs` |
| Authority | Theme 3 + skill |
| Lane | subagent |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `research-docs` | | |
| C2 | Pins version/URL accessed | URL + date | |
| C3 | Prefers primary docs over invention | Citations | |
| C4 | GAP when not found | Explicit GAP | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Invent API from memory without fetch | |

## Smoke

**Prompt:** “Using `research-docs`, answer from primary docs: what does Cursor Debug Mode do in one paragraph? Cite URL accessed today. Also: document GAP if asked for private debug-server wire schema.”
