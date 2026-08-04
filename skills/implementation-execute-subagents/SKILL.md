---
name: implementation-execute-subagents
description: >-
  Execute a Toolbelt implementation plan via a controller plus fresh subagent
  implementers per task (packets, task gates, end review). Broad-use across
  multi-task implementations. Use when running implementation-execute with
  subagents, Task/subagent implementers, or keeping the parent context short
  while workers code. Prefer with durable docs/plans and serial_implement_review.
---

# Implementation execute (subagents)

Announce once: **Using `implementation-execute-subagents`**.

Authority: Theme 7 accepted. **Same spine as `implementation-execute`** — this skill is the **broad-use controller mode** (fresh implementer per task). Standalone Toolbelt; no third-party workflow-pack dependency.

## When to use

- Multi-task plans where fresh implementer context improves quality / keeps the controller short
- User asks for subagent-driven / Task-based execution of a plan
- Alternative to a whole new chat: **fresh subagent ≈ fresh session** for the worker

**When not:** Single tiny task — use `implementation-execute` alone. No approved plan — write one with `implementation-plan` first.

## Controller responsibilities

1. Load plan + critical review (batch) — same as spine; do not invent
2. Own the **ledger** (plan file Status/checkboxes) and Meta S1 sync
3. For each task (serial default; Plan #2 parallel-safe only when marked):
   - Build a **handoff packet** (not a chat dump): Objective, Files, Interfaces, Deps, Done-when, Verify command+expected signal, Do-not, plan Global Constraints / Always·Block If·Never, path refs to design/ADR
   - Dispatch a **fresh** implementer subagent with that packet
   - On return: run or require **Verify evidence** (N=2 owned by Execute spine)
   - When non-trivial (incl. **SUB** this mode): invoke **`implementation-execute-verify`** post-green with a **fresh** reviewer context (Evidence + Faithfulness + Readability/coherence) — not optional self-review in the implementer
   - Mark task `done` or `blocked`(+reason); continue when green
4. Escalate to human on blocked / major deviation (same checklist as `implementation-execute`)
5. After all tasks on a durable plan: required **`implementation-execute-verify`** EOP review + light converge (append Convergence tasks; no silent Goal rewrite). Re-dispatch for appended tasks. On `verify-fail` / unclear Critical → **`debug-systematic`** (or **`debug-reproduce`**). PR later — not here.

## Implementer contract

Workers must:

- Stay inside packet Files / Interfaces / Do-not
- Run Verify and return evidence (command + output)
- Ask the controller (or halt) on ambiguity — **do not invent**
- Not update Meta unilaterally; controller adjudicates status

## Parallelism

Default serial implementers. Parallel only if plan marks parallel-safe **and** exclusive writes or worktrees — never invent parallel on overlapping files.

## Handoffs

| Need | Use |
|------|-----|
| Full Toolbelt ladder (controller routing) | **`implementation-happy-path`** (workers still one pocket) |
| Spine without subagents | `implementation-execute` |
| Post-green / EOP converge | **`implementation-execute-verify`** |
| Plan missing / wrong | `implementation-plan` / `implementation-plan-verify` / human |
| Verify-fail / user bug / unclear Critical | Direct leaf OK (repro-first) or **`guide-debug`** when path unclear |
| Checklist detail | Read Execute checklist (below) |

## References

- Via skill **`implementation-execute`**: read `references/implementation-execute-checklist.md` **when** running a full controller session or recovering a skipped spine step (shared checklist; no duplicate under this skill)
- Via skill **`implementation-execute-verify`**: read its checklist / `review-dimensions.md` / `converge-light.md` **when** running post-green or EOP converge
- Theme 7: Toolbelt `docs/research/reports/theme-7-execute-pocket.md` (accepted)
- Companion spine: skill `implementation-execute`
