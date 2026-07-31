# smoke-app

Minimal fixture for Theme 11 smokes.

```text
smoke-app/
  README.md
  app.py          # add(a,b) — intentional off-by-one bug
  test_app.py     # expects add(2,3)==5 (fails until fixed)
```

**Bug:** `add` returns `a + b + 1` instead of `a + b`.  
**Verify:** `python -m pytest test_app.py -q` (or `python test_app.py` if pytest absent).
