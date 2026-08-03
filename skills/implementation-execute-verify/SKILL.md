---
name: implementation-execute-verify
description: >-
  Verify Toolbelt plan execution: evidence iron law (IDENTIFY→RUN→READ→VERIFY);
  post-green faithfulness + readability/coherence review (fresh context when
  non-trivial); required end-of-plan light converge (gap types
  missing/partial/contradicts/unrequested; append tasks only; no silent Goal
  rewrite; no code edits in converge). Use when execute-verify,
  verification-before-completion, post-green review, converge against plan,
  intent coverage, after task Done-when green, or end-of-plan quality check.
  Prefer with implementation-execute / implementation-execute-subagents. Not
  for plan writing, debug-systematic, or PR packaging.
---

# Implementation execute-verify

Announce once: **Using `implementation-execute-verify`**.

Authority: Theme 8 accepted (Verify gates — Execute extension). Theme 7 Execute law still owns the task loop, **N=2**, and HITL. **Draft plans ≠ law** (`draft-is-not-sot`).

**Identity:** Verification **extension of Execute** — not the Debug method pocket (`debug-systematic`) or PR pack. Quality + code **readability** + faithfulness to plan/design first; ease is a side effect.

## When to use

- After a task’s Done-when Verify is green (when **non-trivial**)
- At **end of a durable plan** (required): post-green review + **light converge**
- When asked for execute-verify / verification-before-completion / converge / intent coverage

**Out of scope:** Plan authoring/validate (`implementation-plan` / `implementation-plan-verify`); Debug method (`debug-systematic` / `debug-reproduce`); PR/git/merge; re-litigating N=2; foreign CLI deps; silent Goal rewrite.

## Preconditions

1. Execute orchestrator (`implementation-execute` or `-subagents`) owns the ledger/loop
2. Signal Verify already run for the task (or EOP batch) — this companion does not replace N=2
3. When review is required → use **fresh** reviewer context (subagent or fresh chat)

## Spine

### A. Evidence iron law (always when claiming done)

IDENTIFY → RUN → READ → VERIFY → claim. Ban “should / probably / looks”. Keep command output. Requirements/Done-when ≠ tests-green alone when plan lists extra constraints.

### B. Post-green review (required when non-trivial; optional trivial; **always at EOP** on durable plans)

Fresh context. Score **Critical / Important / Minor** (OpenSpec CRITICAL/WARNING/SUGGESTION = optional aliases — not Plan PASS trio).  
Dimensions: **Evidence · Faithfulness · Readability/coherence** — read `references/review-dimensions.md` when scoring.  
Routing: Critical → fix + re-evidence (or Theme 7 major-deviation); if root cause unclear → **`debug-systematic`** before thrashing patches. Important → fix before proceed; Minor → note. HITL = Theme 7 only.

### C. Light converge (**EOP-only** on durable plans)

Present findings → append-only `## Convergence` tasks if needed → no Goal rewrite → no code edits in this pass → clean = byte-unchanged.  
Read `references/converge-light.md` when running EOP converge. Mid-plan default: faithfulness/post-green only (not full converge).

## Non-trivial (shared with plan-verify)

True if any: **DUR** · **MF** · **IF** · **DEP** · **FLAG** · **SUB** (same definitions as `implementation-plan-verify`).  
**SUB** (`-subagents` mode) forces post-green **review** frequency, not post-task converge.

## Gotchas

- Signal Verify + N=2 stay on Execute — this skill adds quality/faithfulness/converge, not a second retry budget
- Required review ⇒ **fresh** context; do not self-review in the implementer session
- Converge is **EOP-only** by default; do not append empty `## Convergence` headers

## Anti-patterns

- Claiming done without READ of verify output
- Self-review in the same polluted context when review is required
- Silent plan Goal rewrite during converge
- Treating this skill as PR/Debug pack
- Replacing Execute’s N=2 with endless retries here

## Handoffs

| Need | Use |
|------|-----|
| Task loop / N=2 / HITL | `implementation-execute` or `-subagents` |
| Plan still wrong | `implementation-plan` + `implementation-plan-verify` |
| Appended Convergence tasks | Re-enter Execute loop |
| Unclear Critical / need investigate | Direct leaf OK (repro-first) or **`debug-router`** when path unclear |
| PR / merge | Phase 2 — not here |

## References

- Read `references/implementation-execute-verify-checklist.md` **when** running full execute-verify
- Read `references/review-dimensions.md` **when** scoring post-green findings
- Read `references/converge-light.md` **when** running EOP converge
- Theme 8: `docs/research/reports/theme-8-verify-gates.md` (accepted)
- Theme 7: `docs/research/reports/theme-7-execute-pocket.md` (accepted)
