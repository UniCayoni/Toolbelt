---
title: "Claim card R2 — codebase-recon"
status: draft
theme: theme-11-validation
surface_id: R2
---

# R2 — codebase-recon

| Field | Value |
|-------|-------|
| Surface | `codebase-recon` |
| Authority | Theme 1 + skill |
| Lane | subagent |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `codebase-recon` | | |
| C2 | Chooses systematic/as-needed/hybrid | Mode stated | |
| C3 | Reports layout / entrypoints with paths | Real paths | |
| C4 | Does not invent modules | No fake files | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Skip reading and invent APIs | |

## Smoke

**Prompt:** “Using `codebase-recon` (as-needed), map d:\\Toolbelt plugin layout: skills count, rules count, where PROTOCOL.md lives. Short checklist findings only.”
