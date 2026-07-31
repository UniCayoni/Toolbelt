# smoke-app agent instructions

> Nested fixture `AGENTS.md` for Theme 11 smokes only.  
> Scope: this directory (`docs/research/fixtures/smoke-app/`). Do not treat as Toolbelt root guidance.  
> Prefer links over growth; keep under instruction size budgets.

## Dev environment / commands

- Install: none (stdlib + optional pytest)
- Build: n/a
- Test: `python -m pytest test_app.py -q` (or `python test_app.py` if pytest absent)
- Lint: n/a

## Layout / architecture pointers

- See [README.md](./README.md) for layout and intentional bug notes.
- `app.py` — `add(a, b)`
- `test_app.py` — expects `add(2, 3) == 5`

## Code conventions

- Keep the fixture minimal; do not expand into a product app.

## Testing / definition of done

- Tests green via the Test command above.
- Note: current `add` is intentionally off-by-one until a fix smoke corrects it (see README).

## Boundaries (do-not)

- Do not edit Toolbelt root `AGENTS.md` from this fixture.
- Do not redesign Toolbelt `skills/` or `rules/` from smoke runs.

## Security / secrets

- No secrets; fixture only.

## When you change this file

Update after repeated agent mistakes. Link to README for detail rather than duplicating it here.
