---
title: Implementation plan checklist
status: active
aligned_with: docs/research/reports/theme-6-plan-pocket.md
---

# Implementation plan checklist

Use with skill `implementation-plan`.

## Preconditions

- [ ] Approved design / accepted Decision (or trivial exception documented)
- [ ] Not locking from draft/proposed Design or ADR
- [ ] Intent gaps → `blocked` + `intent-gap` (no invent)

## Plan body

- [ ] Goal (T0)
- [ ] Always / Block if / Never + out-of-scope (T0)
- [ ] design_ref / ADR paths + Decision restated or cited (T1)
- [ ] Coverage map (multi-section designs)
- [ ] File / Code Map (paths; exclusive-write if parallel)
- [ ] `exec_default: serial_implement_review` unless parallel-safe stated
- [ ] Tasks = coherent reviewable units; optional story/phase labels

## Each task

- [ ] Objective + files[]
- [ ] Interfaces consumes/produces (or binding contracts) when coding
- [ ] Deps listed (or none)
- [ ] Done when + Verify command + expected signal
- [ ] GWT only if user/story-shaped (optional)
- [ ] No TBD / “similar to Task N” placeholders
- [ ] No mandatory full impl-code dump (hybrid)
- [ ] Parallel-safe only with independence + exclusive writes or worktree

## Paste (T0–T3)

- [ ] T0 binding brief inlined
- [ ] Bulky ADR/design linked (T1/T2), not pasted wholesale
- [ ] No chat/history dump (T3)

## Pre-exec (V1–V8)

- [ ] V1 No unresolved clarifications / intent gaps
- [ ] V2 Files + interfaces + out-of-scope + verify present
- [ ] V3 Verify runnable with pass/fail signal
- [ ] V4 Reality-check paths / packages / APIs / commands
- [ ] V5 Drift check if plan reused
- [ ] V6 Design Open Questions that change build are closed
- [ ] V7 Binding constraints explicit
- [ ] V8 Hybrid density respected

## Artifact

- [ ] Non-trivial → `docs/plans/YYYY-MM-DD-<slug>-plan.md` from `plan-minimal` template
- [ ] Status vocab ready / in_progress / blocked(+reason) / done
- [ ] TDD ceremony optional; verify required
