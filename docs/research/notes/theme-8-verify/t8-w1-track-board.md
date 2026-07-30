---
title: "T8 Wave 1 track board — Verify gates"
status: draft
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: deep
campaign_phase: deep_wave2
aligned_with:
  - docs/research/notes/theme-8-verify/campaign-brief.md
  - docs/research/notes/theme-8-verify/t8a-w1-plan-verify.md
  - docs/research/notes/theme-8-verify/t8b-w1-execute-verify.md
  - docs/research/notes/theme-8-verify/t8c-w1-community-verify.md
  - docs/research/notes/theme-8-verify/t8d-w1-surface-elevation.md
supersedes: null
---

# T8 Wave 1 track board

**Using `research-protocol`** · depth: **deep**.  
**Identity:** Plan/Execute verification extensions — **not** Debug/PR.

## W1 status

| Track | Note | stop_reason |
|-------|------|-------------|
| T8A | [`t8a-w1-plan-verify.md`](./t8a-w1-plan-verify.md) | wave1_slice_coverage |
| T8B | [`t8b-w1-execute-verify.md`](./t8b-w1-execute-verify.md) | wave1_slice_coverage |
| T8C | [`t8c-w1-community-verify.md`](./t8c-w1-community-verify.md) | wave1_slice_coverage |
| T8D | [`t8d-w1-surface-elevation.md`](./t8d-w1-surface-elevation.md) | wave1_slice_coverage |

## Cross-track consensus (candidates — not elevated SoT)

| Topic | Consensus lean |
|-------|----------------|
| Surface | **C** — `implementation-plan-verify` + `implementation-execute-verify`; hybrid orchestration; skill-only |
| Plan-verify | Phase after write-plan / before Meta `ready`; Reality‖Drift‖Coverage/Actionability; verdicts + fix-plan; hard intent-gap; light taxonomy/DAG; verification table; Spec Kit grammar only; V1–V8 thin retain |
| Execute-verify | Iron law; post-green faithfulness+readability (fresh when required); EOP light converge (incl. unrequested); signal≠intent; N=2 + Theme 7 HITL frozen |
| Converge home | **`implementation-execute-verify`** (G12) |
| Layout | SKILL + checklist (+ refs for rubrics/converge) |
| Elevate order | Accept report → both companions → wire Plan → Execute → -subagents → packs |
| Parks | TDD auditor, council, CLI deps, Copilot PR, SHA-as-SoT, fat Quality, Debug pocket design |
| G9 | validating-plans `references/` **still 404** — Toolbelt writes native checklists |

## Residual → Wave 2

| ID | Item | W2 slice |
|----|------|----------|
| G1 | Rubric wording (readability/faithfulness) + severity unify Plan vs Execute | **W2-RUBRICS** |
| G2 | Non-trivial threshold (T8D lean T-D; T8B NT1–NT6) | **W2-THRESHOLDS** |
| G3 | Description triggers polish | W2-THRESHOLDS (light; T8D already has candidates) |
| OPEN-T8B-2 | Post-task converge? lean EOP-only | **W2-THRESHOLDS** |
| Append format | How converge appends tasks to `docs/plans/` | **W2-THRESHOLDS** |
| G4 | Exact orchestrator wiring prose | Defer to post-accept elevation (candidates exist in T8D) |
| G9 | Refs 404 | **Closed as confirmed GAP** — no more search |
| G10 | Debug leftovers | Closed as list in T8D — no design |
| G11 | Live E0 trial | Optional; skip unless human asks |

## Next

Launch W2: **W2-RUBRICS** ‖ **W2-THRESHOLDS** → then PLUS1 / integrate if diminishing returns.
