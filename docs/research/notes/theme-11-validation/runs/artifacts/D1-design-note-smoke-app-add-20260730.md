---
title: "Design note — fix smoke-app add() off-by-one"
status: draft
theme: theme-11-validation
surface_id: D1
created: 2026-07-30
feature: fix smoke-app add() off-by-one
---

# Design note — fix smoke-app `add()` off-by-one

**Status: draft.** Not accepted design law. **Stop for human accept** before any implementation plan or code change.

## 1. Context (explore)

| Fact | Citation |
|------|----------|
| `add(a, b)` returns `a + b + 1` with an inline BUG comment | E0 `docs/research/fixtures/smoke-app/app.py` |
| Fixture test expects `add(2, 3) == 5` | E0 `docs/research/fixtures/smoke-app/test_app.py` |

Scope: single function in a fixture module. No multi-subsystem split needed.

## 2. Criteria (before solutions)

1. `add(a, b)` returns the arithmetic sum `a + b` (no off-by-one).
2. Existing fixture test `test_add` passes without changing the expected value.
3. Minimal diff — no unrelated refactors or API surface changes.
4. Keep the fixture’s intentional-bug role clear for other smokes (fix only this path when accepted).

## 3. Options

| Option | Approach | Pros | Cons |
|--------|----------|------|------|
| **A (recommended)** | Change `return a + b + 1` → `return a + b`; drop or reword the BUG comment | Smallest faithful fix; matches docstring and test | Removes intentional bug until fixture is restored for other runs |
| **B** | Keep buggy `add`; add `add_correct` / alias and point tests at it | Preserves buggy path for other validation smokes | Wider API; drifts from “fix `add()`” intent |
| **C** | Change test expectation to `6` to match current bug | Zero production-line change | Violates purpose (fix off-by-one); fails criteria 1–2 |

## 4. Recommended Decision (draft — human decides)

**Recommend Option A:** edit `app.py` so `add` returns `a + b`, align comment with correct behavior. Rationale: quality + faithfulness to “fix off-by-one,” readability (one-line change), matches existing test contract.

**This recommendation is not an accepted lock.** Human must accept (or choose B/C / amend) before proceeding.

## 5. Critique (self-review)

- No placeholders/TODOs left open for this tiny scope.
- Option C is a non-fix anti-pattern; retained only as a rejectable contrast.
- Draft ≠ SoT: do not treat this note as architecture or implementation law.
- No Cursor private APIs invented or required.

## 6. Domain handoff (after human accept)

Next skill for code-level shape / boundaries if needed: **`technical-design`** (trivial one-file fix may then skip durable plan per design-process intelligent exception — still **human gate first**).

After accept, implementation ladder only if human directs: `implementation-plan` → … (or trivial exception). **Do not implement in this pass.**

## 7. Gate

**WAITING ON HUMAN ACCEPT** of Decision (A / B / C / other). No code changes. No ADR required for this trivial fixture fix unless human requests one.
