---
status: proposed  # proposed | accepted | deprecated | superseded
date: 2026-07-30
---

# ADR SMOKE: Smoke fixture uses off-by-one for validation

> Toolbelt house ADR (Theme 2 + Theme 5): Nygard core + explicit options (Fowler/MADR).  
> Path (smoke override): `docs/research/notes/theme-11-validation/runs/artifacts/adr-smoke.md`.  
> Do not treat `proposed` as project law. Explicit skill invoke: `/draft-adr` (not always-on).

## Status

proposed

## Context

Theme 11 pocket smokes need a small, deliberate failure surface so execute/debug skills can demonstrate reproduce → fix → verify without touching production code. The fixture at `docs/research/fixtures/smoke-app/` documents an intentional off-by-one in `app.py` (`add` returns `a + b + 1`) with `test_app.py` expecting correct addition (`add(2,3)==5`) [E0: `docs/research/fixtures/smoke-app/README.md`].

Forces:

- Keep a stable failing target for G2/G1 and execute-lane smokes.
- Avoid “fixing” the fixture early and breaking later smoke prompts.
- Do not elevate this note to architecture SoT while status remains `proposed`.

## Considered Options

| Option | Pros | Cons |
|--------|------|------|
| A — Keep intentional off-by-one until execute/debug smokes fix it | Predictable fail signal; aligns fixture README; supports ordered G2→G1 / E* smokes | Tests stay red until those lanes run; easy to “helpfully” fix too early |
| B — Fix the bug in the fixture before execute/debug smokes | Clean green baseline | Removes the failure the later smokes are designed to exercise |
| C — Remove / rewrite smoke-app for a different bug shape | Fresh scenario | Extra scope; breaks existing Theme 11 claim cards that assume off-by-one |

## Decision

We will keep the intentional off-by-one bug in `docs/research/fixtures/smoke-app/` until it is fixed by the execute/debug smokes.

Because option A preserves the documented failure contract for Theme 11 validation; B and C would erase or reshape the signal those lanes need. This ADR remains **proposed** only — human acceptance required before treating it as project law.

## Consequences

- Positive: Execute/debug pocket smokes retain a reproducible failing target.
- Negative: Anyone running `pytest` against smoke-app will see a deliberate failure until those smokes complete.
- Neutral: Path is under Theme 11 `runs/artifacts/` for this smoke; house default `docs/adr/NNNN-…` unused by explicit prompt override.

## Confirmation (optional)

Later execute/debug smokes change `add` to correct `a + b` and make `python -m pytest test_app.py -q` pass (or equivalent), without this ADR being marked `accepted` by the agent alone.

## Notes / links

- Fixture: `docs/research/fixtures/smoke-app/README.md`
- Claim card: `docs/research/notes/theme-11-validation/claim-cards/r4-draft-adr.md`
- Related ADRs: none
- Skill: explicit `/draft-adr` (`disable-model-invocation: true`); not an always-on rule
