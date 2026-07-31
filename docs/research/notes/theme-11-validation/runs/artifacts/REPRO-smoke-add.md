---
title: "Light repro — smoke-app add() off-by-one"
status: draft
theme: theme-11-validation
surface_id: G2
created: 2026-07-30
aligned_with: docs/templates/repro-light.md
---

# REPRO — smoke-app `add()` off-by-one

Authority: Theme 9 light dossier (8 fields). Product code left read-only; no fix in this skill.

## 1. Status

`DETERMINISTIC`

## 2. Symptom

- **Expected:** `add(2, 3) == 5`
- **Actual:** `add(2, 3) == 6` (off-by-one: returns `a + b + 1`)
- **Frequency:** every run of `test_app.py` / direct call

## 3. Command / steps

```text
cd docs/research/fixtures/smoke-app
python test_app.py
```

Alternate direct check (not a green gate):

```text
python -c "from app import add; print(repr(add(2,3)))"
```

## 4. Failing output

```text
Traceback (most recent call last):
  File "D:\Toolbelt\docs\research\fixtures\smoke-app\test_app.py", line 11, in <module>
    test_add()
  File "D:\Toolbelt\docs\research\fixtures\smoke-app\test_app.py", line 7, in test_add
    assert add(2, 3) == 5
           ^^^^^^^^^^^^^^
AssertionError
```

Direct call observed: `add(2, 3)` → `6`.

## 5. Load-bearing triggers

- Inputs `(2, 3)` (any ints sufficient; fixture test is enough)
- Importing `add` from local `app.py` in `docs/research/fixtures/smoke-app`

## 6. Hypothesis ledger

| Hypothesis | State | Note |
|------------|-------|------|
| `add` returns `a + b + 1` instead of `a + b` | open | Matches docstring BUG comment and observed `6` vs expected `5` |
| Test expectation wrong | killed | Docstring and test both specify sum; fixture is intentional bug bench |

## 7. Attempt #0+

| # | Action | Result |
|---|--------|--------|
| 0 | `python -m pytest test_app.py -v` | env: `No module named pytest` — switched surface |
| 1 | `python test_app.py` | **fail** — `AssertionError` on `assert add(2, 3) == 5` |
| 2 | `python -c "from app import add; print(repr(add(2,3)))"` | prints `6` (confirms buggy product, read-only) |

## 8. Handoff acceptance

Fix done when this repro turns green:

```text
cd docs/research/fixtures/smoke-app
python test_app.py
```

→ exits 0 and prints `ok`. Hand off product fix to **`systematic-debug`** (do not patch in `reproduce-bug`).
