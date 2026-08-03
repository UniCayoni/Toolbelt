---
title: "Toolbelt debug-router checklist"
status: active
aligned_with: docs/research/reports/theme-17-debug-router.md
created: 2026-08-02
---

# Debug-router checklist

Authority: Theme 17 accepted. Used by skill `debug-router`.  
**Compose only** — invoke leaves via **Using `<skill>`**; do not paste Theme 9 Debug law here.

## Classifier

```text
Debug ask: prove-only | investigate-fix | prove-then-fix | skip-to-named-leaf | exit-design
Seam (if any): T-VF | T-UB | T-MD | T-CR | T-NYR | n/a
Named leaf already?: yes (which) | no
```

## Structured handoff (fill before first leaf)

```text
Goal (one sentence):
Prior actions / results (incl. Execute N=2 exhausted?):
Key facts + where from (error/stack/repro?):
Open question for next leaf:
Constraints (e.g. no product fix until repro / NOT-YET):
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
      | return Implementation / happy-path | design-process handoff
Do not: burn Execute verify-retry; open PR/merge; guess-fix
```
