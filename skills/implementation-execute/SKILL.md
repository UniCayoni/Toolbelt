---
name: implementation-execute
description: >-
  Execute an approved Toolbelt implementation plan: load plan, critical review,
  statused task loop, Done-when verify with evidence (N=2 retries), escalate on
  blocked or major deviation, continuous when green; invoke
  implementation-execute-verify for post-green quality/readability and EOP
  converge. Use when implementing from docs/plans, running a plan, execute-plan,
  after implementation-plan handoff, or cold/fresh agents implementing checkable
  tasks. Prefer over inventing work outside the plan.
---

# Implementation execute

Announce once: **Using `implementation-execute`**.

Authority: Theme 7 accepted (Execution method guidance). Consumes Theme 6 Plan law. **Draft / non-ready plans ≠ law** (`draft-is-not-sot`). Standalone Toolbelt — inspire from other projects; **do not depend** on Superpowers or foreign CLIs.

## When to use

- An approved durable plan exists (`docs/plans/…` or equivalent) and work should follow it
- After `implementation-plan` + human ready
- Multi-task / multi-file implementation from a written plan

**Intelligent exception:** trivial one-file tweaks with no durable plan may skip this skill (same spirit as Plan/Design).

**Out of scope:** Writing/revising the plan (→ `implementation-plan`); graded plan-validate (→ `implementation-plan-verify`); Design options; Build-domain cookbooks; mandatory git/worktree/TDD/PR packaging; Debug method (→ `systematic-debug` / `reproduce-bug`); PR/CI packaging.

**Multi-task with subagents:** Prefer supplementary skill **`implementation-execute-subagents`** (same spine; controller + fresh implementers).

## Preconditions

1. Plan Meta status is `ready` (or human explicitly waives) — if draft/non-ready → `blocked` + `needs-human` (do not invent)
2. Prefer plan already passed **`implementation-plan-verify`** (PASS*). If durable plan was never plan-verified → warn or bounce to that skill before coding
3. Run Plan V1–V8 lightly if not already done — unresolved intent gaps → `blocked` + `intent-gap`
4. **Highly recommend** a **fresh context** at plan→execute: new chat **or** fresh subagent (same idea — keeps the parent/main window short). Same-session OK for tiny continue-in-chat; do not dump prior exploration into workers

## Spine (do in order)

1. **Load** the durable plan (`docs/plans/YYYY-MM-DD-<slug>-plan.md` or user path)
2. **Critical review** (batch) before first code — Goal, Always/Block if/Never, Out of scope, File map, Done-when+Verify. Raise concerns with human or `blocked`+`intent-gap`. **Do not invent** missing intent
3. **Task loop** (`exec_default: serial_implement_review` unless plan marks parallel-safe)
   - Pick next `ready` task (respect deps)
   - Set task `in_progress`; update plan ledger (Status + checkboxes)
   - Sync **Meta** (S1): `blocked` if any task blocked; `done` iff all required tasks done; else `in_progress` if any in_progress or mix of done+ready; `ready` only if all ready
   - Implement only within task Files / Interfaces / Do-not + plan constraints
   - **Verify:** run listed command → expected signal; keep evidence (output). No bare “done” claims (**evidence-before-completion**)
   - On mismatch → local fix inside Files/Interfaces (enhanced, not blind retry), up to **N=2** attempts (**verify-retry**); then `blocked`+`verify-fail` → hand off **`systematic-debug`** (or **`reproduce-bug`** if prove-first). Do **not** burn more verify-retries under Debug.
   - On match → run **`implementation-execute-verify`** post-green when **non-trivial** (DUR/MF/IF/DEP/FLAG/SUB) — fresh context; Evidence + Faithfulness + Readability/coherence. Trivial → optional. Then task `done`; **continue** (no HITL pause when green)
4. **Escalate / HITL** (do not guess) when:
   - `intent-gap` — ambiguous intent, multiple defensible outcomes
   - `verify-fail` — verify exhausted
   - `needs-human` — irreversible/prod/credentials, or plan amend required
   - **Major deviation** (stop/ask) if work would: edit outside File/Code Map or task Files; change Interfaces/public shape; add unlisted dependency/toolchain; violate Never/Do-not/Out of scope/Block if; redefine Goal/Done-when to force a pass; unauthorized irreversible ops; drive-by refactors that are not required for the task’s Done-when
5. **End of durable plan:** required **`implementation-execute-verify`** EOP review + light converge (append Convergence tasks only; no silent Goal rewrite). Re-enter loop for appended tasks. PR/CI packaging stays later — not this skill

## Status vocabulary

| Status | Meaning |
|--------|---------|
| `ready` | Cleared for work |
| `in_progress` | Being executed |
| `blocked` | Stop — set reason: `intent-gap` \| `verify-fail` \| `needs-human` |
| `done` | Verify signal passed |

HALT ≡ `blocked` + `intent-gap`.

## Parallelism

Default **serial**. Parallel writers only when the plan marks the task parallel-safe **and** independence + exclusive file ownership or worktrees are stated (Theme 6 Plan #2).

## Anti-patterns

- Implementing from draft/unapproved plans as law
- Inventing requirements or silently rewriting the plan
- Claiming done without running Verify / reading evidence
- Pausing for human approval on every green task
- Mandatory Superpowers/OpenSpec/BMAD packaging as Toolbelt law
- Drive-by refactors and scope creep outside Done-when

## Handoffs

| Need | Use |
|------|-----|
| No plan yet | `implementation-plan` (after `design-process` as needed) |
| Multi-task / fresh implementers | `implementation-execute-subagents` |
| Post-green / EOP converge | **`implementation-execute-verify`** |
| Plan never validated | `implementation-plan-verify` |
| Unfamiliar codebase before a task | `codebase-recon` (as-needed) |
| Verify fails after N=2 / unclear root cause | **`systematic-debug`** (or **`reproduce-bug`** prove-first); escalate human if architecture |
| User bug / major-deviation runtime | **`systematic-debug`** |
| Unclear Critical from execute-verify | **`systematic-debug`** before more patches |
| PR / CI / Bugbot | Phase 2 — not Execute |

## References

- Read `references/implementation-execute-checklist.md` **when** running a full execute session or recovering a skipped step
- Plan template: Toolbelt `docs/templates/plan-minimal.md` / skill `implementation-plan`
- Theme 7: Toolbelt `docs/research/reports/theme-7-execute-pocket.md` (accepted)
- Theme 6: Toolbelt `docs/research/reports/theme-6-plan-pocket.md` (accepted)
