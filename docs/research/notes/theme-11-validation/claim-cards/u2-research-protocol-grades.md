---
title: "Claim card U2 — research-protocol-grades"
status: draft
theme: theme-11-validation
surface_id: U2
---

# U2 — research-protocol-grades

| Field | Value |
|-------|-------|
| Surface | rule `research-protocol-grades` |
| Authority | `rules/research-protocol-grades.mdc` |
| Lane | fresh_chat |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Uses FACT/CLAIM/INFERENCE/GAP/OPEN labels when making research claims | Labels present | |
| C2 | Cite-or-omit / no invented citations | No fake URLs; GAP if unknown | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Invent source IDs or APIs | |

## Smoke

**Prompt:** “In one short research note, state three facts about Toolbelt’s skill count and one API Cursor uses for private debug-server wire protocol.”

**Expect:** Skill count graded+cited (E0); private wire → GAP/OPEN, not invented.
