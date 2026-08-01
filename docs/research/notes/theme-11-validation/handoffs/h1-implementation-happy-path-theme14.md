# Handoff — H1 fresh chat (`implementation-happy-path`, Theme 14)

Copy everything below the line into a **new chat** (separate from I1). Prefer a cold context.  
Run **Part A** first. Then B–E in the **same** chat after scoring A.

---

**Workspace:** `D:\Toolbelt`  
**Theme 14 re-smoke H1** — skill `implementation-happy-path`.  
**Do not** implement. **Do not** edit `skills/`. Classifier + checklist stages only.

## Task

1. Read `docs/research/notes/theme-11-validation/claim-cards/h1-implementation-happy-path.md` (includes Theme 14 claims C7–C8).
2. Run Part A. Score claims.
3. Run Parts B–E in the same chat.
4. Write: `docs/research/notes/theme-11-validation/runs/H1-fresh-<YYYYMMDD>.md`.

### Part A — bug (required)

> Using `implementation-happy-path`, classify and route: we need to fix smoke-app `add()` off-by-one end-to-end. Output classifier + checklist stages only; do not implement.

Expect: **bug** → Debug leaves (`debug-reproduce` / `debug-systematic`); design/research skipped with reason; **not** forced through `implementation-router` first.

### Part B — feature / Implementation via router (required)

> Using `implementation-happy-path`, classify and route a non-trivial **feature** that still needs design then implementation. Checklist stages only; do not design or implement.

Expect: stage for Implementation is **`implementation-router`** (not a re-listed plan→execute leaf dump as SoT).

### Part C — research campaign (required)

> Using `implementation-happy-path`, classify and route: run a multi-surface theme campaign on “how agents should scope research tracks” — checklist stages only; do not gather.

Expect: optional **`research-scope`** then research leaves; design only after accept.

### Part D — negative ADR-only (required)

> Only draft an ADR for logging.

Expect: authoring / `research-draft-adr` path — **not** mandatory full feature ladder.

### Part E — implementation-only (required)

> Using `implementation-happy-path`: design is already accepted; wire **Implementation pocket only**.

Expect: prefer **`implementation-router`** over running the entire Research→Design ladder.

### Pass bar (quick)

- Announces **Using `implementation-happy-path`**
- Bug ≠ feature ≠ research ≠ authoring routing
- Feature path uses **`implementation-router`** at Implementation stage (Theme 14 C7)
- Implementation-only prefers router (C8)
- No Execute/Debug method spines pasted
- Workers = one pocket leaf called out
