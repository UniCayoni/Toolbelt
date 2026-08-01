---
title: "R7 smoke — research-scope track board"
status: draft
theme: theme-11-validation
surface_id: R7
created: 2026-07-31
---

# R7 — Scope only (no gather)

**Using `research-scope`**.

## Header

```text
Title / idea: Improve how Toolbelt agents pick research tracks for a fuzzy multi-surface theme
Complexity: theme/campaign
Host note path: docs/research/notes/theme-11-validation/runs/artifacts/
Date: 2026-07-31
Scoped by: agent (smoke)
Enough-to-start (agent propose): yes — tracks named with in/out; gather not required for this smoke
Human accept scope: pending
```

## Expand

- What “pick research tracks” means for agents (when to invent tracks vs skip)
- How this relates to existing `research-protocol` depth modes vs companion `research-scope`
- What artifacts (brief/board) agents should produce
- Gaps vs Themes 1–3 / Theme 12 (already elevated — smoke only)

## Tracks

| ID | Track name | Question | In scope | Out of scope | Priority | Depth lean | Next skill(s) |
|----|------------|----------|----------|--------------|----------|------------|---------------|
| T1 | Companion identity | When must agents run `research-scope` vs skip? | Triggers, skips, composability | Rewriting PROTOCOL grades | P0 | normal | `research-protocol` (Handoff only) |
| T2 | Track artifact shape | What fields must a campaign brief have? | Template fields, enough-gate | Deep lit on question decomposition | P0 | normal | `research-scope` template; optional `author-cursor-surfaces` |
| T3 | Happy-path touch | How does expand-first appear on the ladder? | One Handoff / optional step | Forcing scope on every bug | P1 | normal | `implementation-happy-path` |

## Enough?

```text
Agent enough-to-start?: yes (for smoke / already-elevated Theme 12)
Open GAPs before gather: none required — Theme 12 already accepted; this smoke validates skill behavior
Human gate: pending (smoke scorer may treat as accepted for claim-card only)
```

## Handoffs (no gather this run)

- Do **not** write a `research-protocol` Method note for T1–T3 here.
- Concept atoms = tracks above — **not** T3 D11 checkable doc atoms.
