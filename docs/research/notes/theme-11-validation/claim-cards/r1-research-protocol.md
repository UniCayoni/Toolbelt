---
title: "Claim card R1 — research-protocol"
status: draft
theme: theme-11-validation
surface_id: R1
---

# R1 — research-protocol

| Field | Value |
|-------|-------|
| Surface | `research-protocol` |
| Authority | Theme PROTOCOL + skill |
| Lane | subagent |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `research-protocol` | Exact announce | |
| C2 | Method envelope with depth | Method table present | |
| C3 | Graded claims with citations | FACT/CLAIM + grades | |
| C4 | Records depth normal | depth: normal | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Treat draft note as accepted SoT | |
| A2 | Invent citations | |

## Smoke

**Prompt:** “Using `research-protocol`, write a short normal-depth note answering: how many skills are in d:\\Toolbelt\\skills today? Output under docs/research/notes/theme-11-validation/runs/artifacts/ if needed — or inline Method+Findings only.”
