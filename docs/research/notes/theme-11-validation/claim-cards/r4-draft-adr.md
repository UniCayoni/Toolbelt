---
title: "Claim card R4 — draft-adr"
status: draft
theme: theme-11-validation
surface_id: R4
---

# R4 — draft-adr

| Field | Value |
|-------|-------|
| Surface | `draft-adr` |
| Authority | Theme 2/5 + skill |
| Lane | subagent |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `draft-adr` | | |
| C2 | Uses status enum proposed/accepted/… | Status field | |
| C3 | Writes ADR-shaped sections | Context/Decision/… | |
| C4 | Slash-like / explicit skill | Does not claim always-on | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Mark accepted without human | |

## Smoke

**Prompt:** “Using `draft-adr`, draft a **proposed** ADR (do not accept) titled ‘Smoke fixture uses off-by-one for validation’ under docs/research/notes/theme-11-validation/runs/artifacts/adr-smoke.md — Decision: keep intentional bug in smoke-app until fixed by execute/debug smokes.”
