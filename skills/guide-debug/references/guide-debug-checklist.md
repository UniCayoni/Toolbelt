---
title: "Toolbelt guide-debug checklist"
status: active
aligned_with:
  - docs/research/reports/theme-17-debug-router.md
  - docs/research/reports/theme-21-standards-fanout.md
created: 2026-08-02
updated: 2026-08-04
---

# Guide-debug checklist

Authority: Theme 17 accepted; Theme 21 fan-out. Used by skill `guide-debug`.  
**Compose only** — invoke leaves via **Using `<skill>`**; do not paste Theme 9 Debug law here.

## Classifier

```text
Debug ask: prove-only | investigate-fix | prove-then-fix | skip-to-named-leaf | exit-design
Seam (if any): T-VF | T-UB | T-MD | T-CR | T-NYR | n/a
Named leaf already?: yes (which) | no
```

## Standards resolve (if-present) — Theme 21

```text
Resolve: done (pointers) | no-op (no accepted catalog) | already-pinned (skip) | n/a
standards_catalog:
standards_modules: (id / path / reason) or none
Pocket lean: technical / safety modules matching debug ask — skip if already pinned from Implementation
```

## Structured handoff (fill before first leaf)

```text
Goal (one sentence):
Prior actions / results (incl. Execute N=2 exhausted?):
Key facts + where from (error/stack/repro?):
Open question for next leaf:
Constraints (e.g. no product fix until repro / NOT-YET):
standards_catalog / standards_modules: (from resolve, or none)
```

## Wire plan

```text
Default = one entry leaf. Optional two-step only for explicit prove-then-fix / T-NYR.

- [ ] debug-reproduce — or N/A
- [ ] debug-systematic — or N/A
- [ ] (optional) debug-reproduce → debug-systematic — only prove-then-fix / T-NYR
- [ ] Exit design/plan — if intent gap (not a Debug leaf)
```

## Stop

```text
Exit: fixed+same-repro | NOT-YET-REPRODUCED | debug-fix-cycles exhausted → human
      | return Implementation / happy-path | guide-design handoff
Do not: burn Execute verify-retry; open PR/merge; guess-fix
```
