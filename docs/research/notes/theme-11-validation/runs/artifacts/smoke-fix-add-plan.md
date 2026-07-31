---
title: "Implementation plan — smoke-fix-add"
status: draft
theme: theme-11-validation
surface_id: P1
note: >-
  Theme 11 pocket-smoke artifact. Meta Status is not `ready` until
  implementation-plan-verify passes (or documented trivial skip).
---

# Implementation plan — smoke-fix-add

| Meta | Value |
|------|-------|
| Status | — *(unset; not `ready`)* — awaiting **`implementation-plan-verify`**. When set, use vocab: `ready` · `in_progress` · `blocked` · `done`. |
| Blocked reason (if any) | — |
| Design / ADR | **Assumed human-accepted** Decision for this smoke: fix `add` to **return `a + b`** (fixture intent; no separate ADR path). Not treating unapproved/draft design as law without this note. |
| exec_default | `serial_implement_review` |
| Created | 2026-07-30 |

## Goal

Make `docs/research/fixtures/smoke-app/app.py` `add(a, b)` return the arithmetic sum `a + b` (remove off-by-one), so fixture tests pass.

## Global constraints

**Always:**
- Change only the smoke-app `add` implementation behavior to match Decision: return `a + b`.
- Keep the public signature `add(a: int, b: int) -> int`.
- Verify with a runnable Python test command → clear pass/fail signal.

**Block if:**
- Design Decision is revoked or ambiguous (intent-gap).
- Verify fails after N=2 enhanced local fixes → `blocked` + `verify-fail`.

**Never / do-not:**
- Redesign or edit Toolbelt `skills/` or `rules/`.
- Expand scope beyond the off-by-one fix.
- Invent Cursor private APIs.

## Out of scope

- Refactors, new APIs, packaging, CI wiring.
- Elevating or rewriting Toolbelt skills.
- Any work outside `docs/research/fixtures/smoke-app/`.

## Coverage map

| Design section / FR | Plan chapter / tasks |
|---------------------|----------------------|
| Decision: `add` returns `a + b` | Task T1 — fix off-by-one |

## File / Code Map

| Path | Action | Notes (owner / exclusive-write?) |
|------|--------|----------------------------------|
| `docs/research/fixtures/smoke-app/app.py` | modify | exclusive-write for T1 |
| `docs/research/fixtures/smoke-app/test_app.py` | (read / run only) | verify harness; no change expected |

## Paste / load guidance (T0–T3)

- **T0 (inline here):** Goal, constraints, Decision (`return a + b`), file map, T1 verify.
- **T1:** `docs/research/fixtures/smoke-app/app.py` — current buggy body `return a + b + 1`; docstring already states sum.
- **T2:** Fixture README bug note if needed: `docs/research/fixtures/smoke-app/README.md`.
- **T3:** Do not dump chat history into worker briefs.

## Tasks

### Task T1 — Fix `add` off-by-one

- [ ] Status: `ready` *(task-level; Meta plan status remains awaiting plan-verify)*
- **Objective:** Change `add` so it returns `a + b` instead of `a + b + 1`.
- **Files:** `docs/research/fixtures/smoke-app/app.py`
- **Interfaces (consumes / produces):** Consumes binding Decision `add(a,b) -> a+b`. Produces corrected `add` with unchanged signature.
- **Deps:** none
- **Done when:** `add(2, 3) == 5` and `test_add` passes with no assertion failure.
- **Verify:** `python test_app.py` (cwd: `docs/research/fixtures/smoke-app`) → expected signal: prints `ok` and exit code 0 (no AssertionError).
- **GWT (optional):** Given buggy `return a + b + 1` / When implementer applies Decision / Then `python test_app.py` exits 0 and prints `ok`.
- **Parallel-safe:** no
- **Do-not (task-local):** Do not edit `test_app.py` to match the bug; do not change signature or add features.

## Pre-exec check (light — Plan pocket)

- [x] V1 No unresolved intent gaps (else `blocked` + `intent-gap` — do not invent)
- [x] V2 Files + interfaces + out-of-scope + verify present
- [x] V3 Verify is runnable with expected pass/fail signal
- [x] V4 Reality-check: cited paths / packages / APIs / commands exist (`app.py`, `test_app.py`, `python test_app.py`)
- [x] V5 Drift: plan still matches tree if reused later
- [x] V6 Design Open Questions that change build are closed (smoke assumes accepted Decision)
- [x] V7 Binding constraints / Always·Block If·Never explicit
- [x] V8 No reliance on mandatory full impl-code dumps (hybrid)

## Plan-verify (before Meta ready)

- [ ] Ran **`implementation-plan-verify`** (or documented trivial skip)
- [ ] Verdict: `PASS` \| `PASS WITH NOTES` \| `NEEDS REVISION` — Meta `ready` **only** on PASS*
- **Note:** Meta Status above is intentionally **not** `ready`. Next step for this plan: run skill **`implementation-plan-verify`**; set Meta to `ready` only after PASS / PASS WITH NOTES.

## Execution notes

- After Meta `ready`: run Toolbelt **`implementation-execute`** (or **`implementation-execute-subagents`**).
- Default: **serial implement → verify** on shared checkout.
- Verify: command → expected signal; up to **N=2** enhanced local fixes then `blocked`+`verify-fail`.
- This smoke authored the plan only; did **not** implement the fix in `app.py`.
