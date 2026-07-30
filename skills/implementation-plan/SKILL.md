---
name: implementation-plan
description: >-
  Write Toolbelt hybrid implementation plans for agents/subagents: consume
  approved design/ADR, decompose into checkable tasks (files, interfaces,
  Done-when + verify), serial_implement_review default, T0–T3 paste, light
  V1–V8 pre-exec checks. Use when writing a plan, task breakdown, write-plan,
  planning before implement, handoff packets for fresh agents, or after
  design-process gate. Prefer over jumping straight to multi-file coding.
---

# Implementation plan

Announce once: **Using `implementation-plan`**.

Authority: Theme 6 accepted (Plan method guidance). **Unapproved / draft plans ≠ accepted law** (`draft-is-not-sot`).

## When to use

- Non-trivial work after an approved design (or clear accepted Decision + constraints)
- Writing durable plans for fresh agents / subagents
- Decomposing design sections into ordered, verifiable tasks
- Before multi-file or multi-step implementation

**Intelligent exception:** trivial one-file tweaks may stay chat-ephemeral (same spirit as short Design). Prefer a durable plan when scope, risk, or handoff needs it.

**Out of scope:** Re-opening Design options; mandatory TDD/git/worktree/PR ceremony; UX planning (T5C); importing Superpowers execution skills as Toolbelt law.

## Preconditions

1. Design gate passed (`design-process` or equivalent human approval) — or work is trivial enough to skip durable design+plan
2. Consume **accepted** Decision / constraints / interfaces / success criteria / section IDs — cite paths; **do not** treat draft Design/ADR as locks
3. If intent is ambiguous with multiple defensible outcomes → status `blocked` + reason `intent-gap` (**do not invent**)

## Spine (do in order)

1. **Link inputs** — design note / ADR paths; restate binding Decision (or path+§); T0 constraints
2. **Coverage map** — approved design sections / FRs → plan chapters or task groups (100% of approved scope; no drive-by extras)
3. **File / Code Map** — create/modify paths; note exclusive-write ownership if any parallel-safe tasks
4. **Decompose** — WBS → vertical slices → SPIDR/Spike when oversized or unknown → SMART task units sized to a **coherent reviewable unit** (not a fixed minute budget). Optional story/phase labels when multi-slice
5. **Write tasks (hybrid density)** — each task: objective, files[], interfaces consumes/produces (or binding contracts), deps, **Done when**, **Verify** (`command` → expected signal), optional GWT when user/story-shaped, task-local do-not. **No TBD placeholders.** Binding signatures/interfaces OK; **no mandatory full impl-code dumps**
6. **Execution shape** — `exec_default: serial_implement_review` on shared checkout. Mark `parallel-safe` / `[P]` **only** when independence + exclusive file ownership **or** worktrees are stated
7. **Paste/load (T0–T3)** — T0 inline binding brief; T1 path+extract; T2 cold ADR/design bodies; T3 never dump chat/history. No invented numeric token budgets
8. **Durable path** — non-trivial: write `docs/plans/YYYY-MM-DD-<slug>-plan.md` (host path overrides OK) using the house template
9. **Pre-exec check (V1–V8)** — light Plan-pocket validation before handoff to implementers
10. **Handoff** — for subagents: controller spine + per-task packet (objective, I/O, boundaries, path refs) — not a chat dump. Status vocab: `ready` · `in_progress` · `blocked` (`intent-gap` / `verify-fail` / `needs-human`) · `done`. HALT ≡ `blocked`+`intent-gap`

## Status vocabulary

| Status | Meaning |
|--------|---------|
| `ready` | Plan/task cleared for work |
| `in_progress` | Being executed |
| `blocked` | Stop — set reason |
| `done` | Verify signal passed |

## Anti-patterns

- Planning from draft/proposed Design as if accepted
- Reopening ADR options inside the plan
- Thin tasks with no verify signal
- Mandatory code-in-plan dumps or mandatory TDD red/green/commit as Plan grammar
- Parallel implementers on overlapping files without ownership/worktrees
- Assuming subagents share prior chat context

## Handoffs

| Next | Skill / action |
|------|----------------|
| Need design first | `design-process` (then return here) |
| Significant locks missing | `draft-adr` |
| Unfamiliar codebase before planning | `codebase-recon` |
| Execute the plan | **`implementation-execute`** (or **`implementation-execute-subagents`** for controller + fresh implementers) |

## References

- Read `references/implementation-plan-checklist.md` **when** writing a full plan or recovering a skipped step
- Read `references/plan-minimal.md` **when** creating/updating a durable plan file (SoT: `docs/templates/plan-minimal.md`)
- Theme 6: Toolbelt `docs/research/reports/theme-6-plan-pocket.md` (accepted)
