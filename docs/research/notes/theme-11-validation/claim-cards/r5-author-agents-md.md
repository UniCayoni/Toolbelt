---
title: "Claim card R5 — author-agents-md"
status: draft
theme: theme-11-validation
surface_id: R5
---

# R5 — author-agents-md

| Field | Value |
|-------|-------|
| Surface | `author-agents-md` |
| Authority | Theme 4-ish + skill |
| Lane | subagent |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `author-agents-md` | | |
| C2 | Produces AGENTS.md-shaped content | Sections present | |
| C3 | Prefer links over dumping everything | Thin pointers | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Overwrite host AGENTS without path clarity | |

## Smoke

**Prompt:** “Using `author-agents-md`, draft a minimal AGENTS.md for docs/research/fixtures/smoke-app/ only (do not touch Toolbelt root AGENTS.md). Include how to run tests.”
