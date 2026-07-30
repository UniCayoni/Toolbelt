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

Authority: Theme 7 accepted. **Same spine as `implementation-execute`** — this skill is the **broad-use controller mode** (fresh implementer per task). Standalone Toolbelt; no Superpowers dependency.

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
   - On return: run or require **Verify evidence**; optional fresh **task reviewer** subagent for spec+quality when stakes are high
   - Mark task `done` or `blocked`(+reason); continue when green
4. Escalate to human on blocked / major deviation (same checklist as `implementation-execute`)
5. After all tasks: optional light end review (fresh context); fuller review later

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
| Spine without subagents | `implementation-execute` |
| Plan missing / wrong | `implementation-plan` / human |
| Checklist detail | `implementation-execute` → `references/implementation-execute-checklist.md` |

## References

- Theme 7: Toolbelt `docs/research/reports/theme-7-execute-pocket.md` (accepted)
- Companion spine: skill `implementation-execute`
