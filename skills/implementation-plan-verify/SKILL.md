---
name: implementation-plan-verify
description: >-
  Validate a Toolbelt implementation plan before execute: Reality + Drift +
  coverage/actionability; verdicts PASS / PASS WITH NOTES / NEEDS REVISION;
  hard ambiguity → intent-gap; light FR→task coverage and acyclic deps;
  codebase verification table when non-trivial (durable docs/plans/ or risk
  escalate). Use when plan-validate, validate-plan, review-plan before
  implement, pre-exec validate, after implementation-plan write, before Meta
  ready, or before implementation-execute. Prefer over jumping from draft plan
  to code. Not for execute-verify, converge, debug-systematic, or PR packaging.
---

# Implementation plan-verify

Announce once: **Using `implementation-plan-verify`**.

Authority: Theme 8 accepted (Verify gates — Plan extension). Theme 6 Plan law still owns authoring + light V1–V8. **Draft plans ≠ law** (`draft-is-not-sot`).

**Identity:** Verification **extension of Plan** — not the Debug method pocket or PR pack. Quality + readability of the *plan as an agent contract* first; ease is a side effect.

## When to use

- After writing/updating a durable plan, **before** Meta `ready` / `implementation-execute`
- When asked to validate-plan / review-plan / pre-exec validate
- Non-trivial work under `docs/plans/` (or risk escalate — see thresholds)

**Skip (document “trivial skip”):** chat-ephemeral single-file one-task tweak with no durable plan and no risk signals (Interfaces, deps, multi-file, subagent mode).

**Out of scope:** Execute evidence/converge (`implementation-execute-verify`); Debug method (`debug-systematic`); PR; mandatory TDD auditor; foreign CLI deps; inventing missing design intent.

## Preconditions

1. Plan artifact exists (durable path preferred)
2. Consume **accepted** design/ADR Decision — do not lock from draft Design
3. Plan skill / human remains orchestrator; this companion returns a **verdict** and fix guidance — fix the **plan**, not code

## Spine (do in order)

1. **Announce + load** plan (+ cited design/ADR paths)
2. **Trivial?** If skip path applies → document skip; stop. Else continue
3. **Codebase verification table** (when non-trivial) — Claim · Method · Result · Severity for cited paths/APIs/packages/commands
4. **Parallel lanes** (may run together):
   - **Reality** — paths/APIs/commands/packages exist; no hallucinated givens
   - **Drift** — plan still matches tree/deps if reused
   - **Coverage / actionability** — FR→task coverage; acyclic deps; light task taxonomy (composite / ambiguous / coverage_gap / misordered); falsifiable Verify steps
5. **Aggregate** severities → verdict (below)
6. **Handoff** — on PASS / PASS WITH NOTES → Meta may go `ready`. On NEEDS REVISION → fix plan, re-run this skill; if invent required → Meta `blocked`+`intent-gap`

## Verdicts & severity (Plan lane)

| Severity | Typical effect |
|----------|----------------|
| **BLOCKER** | → **NEEDS REVISION**; often `intent-gap` if invent required |
| **CRITICAL** | → **NEEDS REVISION** unless human risk-accept recorded |
| **WARNING** | → **PASS WITH NOTES** allowed |
| **NIT** | → PASS or PASS WITH NOTES |

Verdicts: **PASS** · **PASS WITH NOTES** · **NEEDS REVISION**.  
**Fix the plan, not code.** Re-validate after plan edits. Hard vs soft ambiguity gates: checklist.

## Non-trivial (shared with execute-verify)

True if any: **DUR** (durable `docs/plans/…`) · **MF** (≥2 files/paths/tasks) · **IF** (Interfaces/public) · **DEP** (new dep/toolchain/auth/migration) · **FLAG** (`review-required` / equivalent) · **SUB** (subagent execute mode).

## Gotchas

- V1–V8 on Plan is a **light** authoring check — this skill is the graded gate; do not skip it on durable plans
- Soft ambiguity ≠ inventable gap; only inventable gaps get `intent-gap`
- Do not “validate” by writing application code

## Anti-patterns

- Treating draft Design as accepted locks
- Jumping to code to “validate” the plan
- Importing TDD auditor / council consultants / Spec Kit CLI as law
- Silencing inventable gaps instead of `intent-gap`
- Fat Quality / Debug ceremony inside plan-verify

## Handoffs

| Next | Skill / action |
|------|----------------|
| Plan needs rewrite | `implementation-plan` (then re-run this skill) |
| Verdict PASS* | Meta `ready` → **`implementation-execute`** (or `-subagents`) |
| Intent cannot be chosen | Meta `blocked`+`intent-gap` — human / design |
| Post-code verify | `implementation-execute-verify` |

## References

- Read `references/implementation-plan-verify-checklist.md` **when** running a full plan-verify or scoring hard/soft ambiguity
- Theme 8: Toolbelt `docs/research/reports/theme-8-verify-gates.md` (accepted)
- Theme 6: `docs/research/reports/theme-6-plan-pocket.md` (accepted)
