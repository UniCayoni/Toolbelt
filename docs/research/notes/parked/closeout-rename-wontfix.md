---
title: "Park closed — closeout rename (wontfix)"
status: accepted
disposition: wontfix
created: 2026-08-03
accepted: 2026-08-03
accepted_by: human (Jonathan)
aligned_with:
  - docs/research/reports/theme-15-closeout-readiness.md
  - docs/research/reports/theme-16-host-standards.md
---

# Closeout rename — wontfix

**Disposition:** **wontfix** / not needed — 2026-08-03.

## Decision

Keep skill id **`implementation-closeout`**. Do not rename to `closeout-readiness` / `ship-readiness` (or similar).

## Why

- Skill was never an `author-*` closeout author; Theme 15 shipped domain-first **`implementation-closeout`** (define/update + check). Name OPEN vs `closeout-readiness` was optional cleanup, not a wrong identity.
- Theme 16 bind: host standards/principles are optional **criteria feedstock** for the closeout profile; that pairing fits the current id on the Implementation / happy-path ladder.
- No product pressure to migrate folder, plugin.json, handoffs, or C1 smoke surface.

## Was parked where

- Theme 16 D12 / §6 Parks; T16K lean  
- Theme 18 L9 parks (carry-forward)

## Still true

- Ceremony (PR/merge/CI) remains out of scope for this skill.  
- `author-standards` does not own closeout rename (anti-pattern unchanged).
