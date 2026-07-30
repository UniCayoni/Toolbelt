---
title: Implementation execute checklist
status: active
aligned_with:
  - docs/research/reports/theme-7-execute-pocket.md
  - docs/research/reports/theme-8-verify-gates.md
---

# Implementation execute checklist

Use with skill `implementation-execute`.

## Preconditions

- [ ] Plan Meta `ready` (or human waive) — not draft-as-law
- [ ] Prefer prior **`implementation-plan-verify`** PASS* (warn/bounce if durable plan never verified)
- [ ] Fresh context highly recommended (new chat **or** fresh subagent)
- [ ] Critical review batched before first code (raise ≠ invent)

## Task loop

- [ ] Serial default; parallel-safe only if plan marks + ownership/worktrees
- [ ] Task Status: ready → in_progress → done | blocked(+reason)
- [ ] Meta sync S1 (aggregate of tasks)
- [ ] Ledger = plan file Status/checkboxes under `docs/plans/…`
- [ ] Stay inside Files / Interfaces / Do-not
- [ ] Verify command run + expected signal + evidence kept
- [ ] Verify-fail after at most **N=2** enhanced local fixes
- [ ] Non-trivial green → **`implementation-execute-verify`** post-green (fresh; quality/readability/faithfulness)
- [ ] Continue when green (no per-task HITL)

## Escalate

- [ ] intent-gap / verify-fail / needs-human set when stopping
- [ ] Major-deviation checklist checked before expanding scope
- [ ] No silent plan rewrite

## End

- [ ] All required tasks done or blocked with reasons
- [ ] Meta Status reflects S1
- [ ] Durable plan → required **`implementation-execute-verify`** EOP review + light converge
- [ ] Appended Convergence tasks re-entered in loop; Debug/PR deferred
