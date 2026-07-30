---
title: "Implementation plan (minimal)"
status: active
aligned_with:
  - docs/research/reports/theme-6-plan-pocket.md
  - skills/implementation-plan/SKILL.md
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

## Execution notes

- Default: **serial implement → review/verify** on shared checkout.
- Parallel only when a task is marked parallel-safe with independence + exclusive file ownership or worktrees.
- Trivial one-file tweaks may skip a durable plan file (intelligent exception); non-trivial work: save under `docs/plans/YYYY-MM-DD-<slug>-plan.md`.
- TDD ceremony is **optional**; verify is **required**.
