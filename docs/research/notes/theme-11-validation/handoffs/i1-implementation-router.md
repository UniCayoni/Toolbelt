# Handoff — I1 fresh chat (`guide-implementation`)

Copy everything below the line into a **new chat**. Prefer a cold context.  
Run **Part A** first. Then **Part B** and **Part C** in the **same** chat after Part A is scored.

---

**Workspace:** `D:\Toolbelt`  
**Theme 14 smoke I1** — skill `guide-implementation`.  
**Do not** write a real plan file. **Do not** implement code. **Do not** edit `skills/`. Routing / checklist / handoff output only.

## Task

1. Read `docs/research/notes/theme-11-validation/claim-cards/i1-implementation-router.md`.
2. Run Part A (explicit). Score claims C1–C7 + anti-patterns.
3. Run Part B then Part C in the same chat.
4. Write: `docs/research/notes/theme-11-validation/runs/I1-fresh-<YYYYMMDD>.md` with classifier, wire plans, claim scores, verdict (`PASS` | `PASS WITH NOTES` | `NEEDS REVISION`).

### Part A — full feature wire (required)

> Using `guide-implementation`: assume design for a smoke-app `add()` off-by-one fix is already human-accepted (treat as given; do not invent new product locks). Wire the Implementation pocket only. Output: announce, classifier, structured handoff block, wire plan with explicit N/A skips. Do not write plan body. Do not implement.

### Part B — verify-only (required)

> Using `guide-implementation`: Meta `ready` plan already exists and task greens are done. Need EOP `implementation-execute-verify` only. Wire with skips. Do not implement.

### Part C — single leaf / skip (required)

> Using `guide-implementation`: only run `implementation-plan-verify` on the existing plan. Either document router skip + leaf-direct, or emit a thin wire that is verify-only. Do not force plan→execute.

### Pass bar (quick)

- Announces **Using `guide-implementation`**
- Classifies differently across A/B/C (not the same wire every time)
- No pasted Plan/Execute method spines
- No WBS/task decomposition in the router output
- Part B does **not** force a full ladder
- Part C allows leaf-direct or verify-only wire
