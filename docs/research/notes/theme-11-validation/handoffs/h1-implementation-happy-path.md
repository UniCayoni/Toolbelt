# Handoff — H1 fresh chat (`implementation-happy-path`)

Copy everything below the line into a **new chat**. Prefer a cold context.  
Run **Part A** first. Optionally **Part B** and **Part C** in the **same** chat after Part A is scored (discovery suite).

---

**Workspace:** `D:\Toolbelt`  
**Theme 11 smoke H1** — skill `implementation-happy-path`.  
**Do not** implement the smoke-app fix. **Do not** edit `skills/`. Orchestration / routing output only.

## Task

1. Read `docs/research/notes/theme-11-validation/claim-cards/h1-implementation-happy-path.md`.
2. Run Part A (explicit). Score claims.
3. Optional Part B (implicit discovery) then Part C (negative control).
4. Write: `docs/research/notes/theme-11-validation/runs/H1-20260730.md` covering A (+ B/C if run).

### Part A — explicit (required)

> Using `implementation-happy-path`, classify and route: we need to fix smoke-app add() off-by-one end-to-end. Output classifier + checklist stages only; do not implement.

### Part B — implicit (optional discovery)

> What’s the Toolbelt order of skills for a small feature fix?

Expect: routes through happy-path or equivalent ladder; should not invent a foreign workflow.

### Part C — negative (optional)

> Only draft an ADR for logging.

Expect: `draft-adr` / authoring path — **not** forcing the full feature ladder as mandatory.
