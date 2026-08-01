---
title: "Theme 12 smoke delta — research surfaces"
status: draft
theme: theme-11-validation
created: 2026-07-31
aligned_with:
  - docs/research/reports/theme-12-research-scoping.md
  - docs/research/notes/theme-11-validation/smoke-matrix.md
---

# Theme 12 smoke delta (2026-07-31)

## Compliance vs pre-Theme-12 cards

| Surface | Compliant before? | Fix |
|---------|-------------------|-----|
| R1–R3 | Mostly — still valid; R1 count stale at 19 | Re-ran; cards + C5 companion boundary |
| H1 | Mostly — missing optional `research-scope` | Added C6 + research-branch smoke; re-ran |
| `research-scope` | **Missing** from matrix | New **R7** card + PASS run |
| U2 / other P0 | Untouched by Theme 12 | Not re-run |

## Scoreboard (touched set)

| ID | Verdict |
|----|---------|
| R1 | **PASS** |
| R2 | **PASS** |
| R3 | **PASS** |
| R7 | **PASS** |
| H1 | **PASS** |

**5/5 PASS** on Theme-12-touched smokes. No NEEDS REVISION.

## Operator note

These are pocket/controller-style E0 claim-card smokes in-session (same method as Theme 11 Phase B), not a separate fresh-chat discovery lane for R7 description trigger.
