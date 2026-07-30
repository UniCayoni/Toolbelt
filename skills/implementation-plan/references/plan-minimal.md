---
title: "Implementation plan (minimal)"
status: active
aligned_with:
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/research/reports/theme-8-verify-gates.md
  - skills/implementation-plan/SKILL.md
  - skills/implementation-plan-verify/SKILL.md
note: "House template for durable plans. Skill copies via refresh-skill-references.py."
---

# Implementation plan — `<slug>`

| Meta | Value |
|------|-------|
| Status | `ready` \| `in_progress` \| `blocked` \| `done` |
| Blocked reason (if any) | `intent-gap` \| `verify-fail` \| `needs-human` \| — |
| Design / ADR | `docs/design/…` · `docs/adr/NNNN-….md` (Decision § …) |
| exec_default | `serial_implement_review` |
| Created | YYYY-MM-DD |

## Goal

<!-- T0: one clear outcome -->

## Global constraints

**Always:**
-

**Block if:**
-

**Never / do-not:**
-

## Out of scope

-

## Coverage map

| Design section / FR | Plan chapter / tasks |
|---------------------|----------------------|
| | |

## File / Code Map

| Path | Action | Notes (owner / exclusive-write?) |
|------|--------|----------------------------------|
| | create \| modify | |

## Paste / load guidance (T0–T3)

- **T0 (inline here):** Goal, constraints, interfaces, verify, this plan’s file map.
- **T1:** Path + section + what to extract (Decision, Interfaces).
- **T2:** Long rationale bodies — link; do not paste whole ADR options matrices.
- **T3:** Do not dump chat history or exploration traces into worker briefs.

## Tasks

### Task `<id>` — `<title>`

- [ ] Status: `ready`
- **Objective:**
- **Files:**
- **Interfaces (consumes / produces):**
- **Deps:** (none | task ids)
- **Done when:**
- **Verify:** `command` → expected signal
- **GWT (optional):** Given … / When … / Then …
- **Parallel-safe:** no *(only `yes` if independence + exclusive writes or worktree stated)*
- **Do-not (task-local):**

<!-- Repeat task blocks. Size = coherent reviewable unit. Optional story/phase labels if multi-slice. -->

## Pre-exec check (light — Plan pocket)

- [ ] V1 No unresolved intent gaps (else `blocked` + `intent-gap` — do not invent)
- [ ] V2 Files + interfaces + out-of-scope + verify present
- [ ] V3 Verify is runnable with expected pass/fail signal
- [ ] V4 Reality-check: cited paths / packages / APIs / commands exist
- [ ] V5 Drift: plan still matches tree if reused later
- [ ] V6 Design Open Questions that change build are closed
- [ ] V7 Binding constraints / Always·Block If·Never explicit
- [ ] V8 No reliance on mandatory full impl-code dumps (hybrid)

## Plan-verify (before Meta ready)

- [ ] Ran **`implementation-plan-verify`** (or documented trivial skip)
- [ ] Verdict: `PASS` \| `PASS WITH NOTES` \| `NEEDS REVISION` — Meta `ready` only on PASS*
- [ ] Optional task flag: mark `review-required` in Do-not / notes when post-green review must run even if otherwise “small”

## Execution notes

- After Meta `ready`: run Toolbelt **`implementation-execute`** (or **`implementation-execute-subagents`**).
- Default: **serial implement → verify** on shared checkout; continuous when green; HITL on blocked / major deviation.
- Parallel only when a task is marked parallel-safe with independence + exclusive file ownership or worktrees.
- Highly recommend fresh chat **or** fresh subagent at plan→execute (keeps parent context short).
- Verify: command → expected signal; up to **N=2** enhanced local fixes then `blocked`+`verify-fail`.
- Non-trivial / EOP: **`implementation-execute-verify`** (post-green quality+readability; EOP light converge may append `## Convergence` tasks — append-only, no Goal rewrite).
- Meta Status sync (S1): aggregate of tasks (`blocked` if any blocked; `done` iff all done).
- Trivial one-file tweaks may skip a durable plan file (intelligent exception); non-trivial work: save under `docs/plans/YYYY-MM-DD-<slug>-plan.md`.
- TDD ceremony is **optional**; verify is **required**.
