---
title: "T17B — Classifier matrix"
status: draft
theme: theme-17-debug-router
track: T17B
created: 2026-08-02
depth: normal
---

# T17B — Classifier matrix

**Using `research-protocol`**. Premises: accepted lean (`pre-start-considerations.md`) + Theme 9 F10.

## Classifier (accepted)

| Signal | Entry / wire |
|--------|----------------|
| Prove / minimize / dossier only | `debug-reproduce` |
| Investigate + fix; repro in hand or will be made in spine | `debug-systematic` |
| Explicit prove-then-fix or T-NYR | optional wire: `debug-reproduce` → `debug-systematic` |
| User named one leaf | skip router → that leaf |
| Design/intent wrong | exit → `design-process` / happy-path (not Debug leaf) |
| T-VF / T-MD / T-CR (typical) | `debug-systematic` (prove-first → reproduce first) |
| T-UB unclear repro | lean reproduce or systematic with iron law |
| PR/merge ask | refuse ceremony; Debug only if bug remains |

## Anti-patterns

- Default two-step wire every time  
- Router restates Theme 9 spine  
- Burning Execute `verify-retry N=2` under Debug  
- Guess-fix when `NOT-YET-REPRODUCED`
