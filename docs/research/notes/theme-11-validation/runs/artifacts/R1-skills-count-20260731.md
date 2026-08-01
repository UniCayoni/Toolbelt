---
title: "R1 smoke — skills count under Toolbelt"
status: draft
theme: theme-11-validation
surface_id: R1
created: 2026-07-31
depth: normal
---

# R1 — How many skills in `d:\Toolbelt\skills`?

**Using `research-protocol`**.

## 1. Scope

- Question: Count of top-level skills today (post Theme 12).
- Out: Elevating skills; running `research-scope`.

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-31 |
| Tools used | PowerShell `Get-ChildItem` on `d:\Toolbelt\skills` |
| Corpora / URLs | Local filesystem only |
| Queries (exact) | `(Get-ChildItem skills -Directory).Count`; list Names |
| What was *not* searched | Marketplace / remote plugin cache |
| Depth | normal |

## 3. Findings

- `FACT` [E0] There are **20** top-level skill directories under `d:\Toolbelt\skills`, each with `SKILL.md`. [E0: `Get-ChildItem d:\Toolbelt\skills -Directory` 2026-07-31]
- `FACT` [E0] Directory names include `research-scope` and `research-protocol` among the 20. [E0: same listing]
- `FACT` [E0] Count increased from prior R1 smoke (**19** on 2026-07-30) consistent with Theme 12 elevate. [E0: prior `R1-20260730.md`; this listing]

## 4. Gaps & OPEN

- None for the count question.
