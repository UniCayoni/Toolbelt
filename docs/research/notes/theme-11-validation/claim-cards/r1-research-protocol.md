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
| C5 | Does not absorb scoping spine (Theme 12 companion) | No expand/atomize track board as protocol body; may Handoff `guide-research` | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Treat draft note as accepted SoT | |
| A2 | Invent citations | |
| A3 | Replace `guide-research` with ad-hoc track theater inside protocol | |

## Smoke

**Prompt:** “Using `research-protocol`, write a short normal-depth note answering: how many skills are in d:\\Toolbelt\\skills today? Output under docs/research/notes/theme-11-validation/runs/artifacts/ if needed — or inline Method+Findings only. Do not run guide-research.”
