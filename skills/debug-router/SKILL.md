---
name: debug-router
description: >-
  Pocket router for Toolbelt Debug: classify the ask, emit a wire plan over
  debug-reproduce and/or debug-systematic with explicit skips, then invoke those
  skills without restating Theme 9 law. Use when debug-router, which debug skill,
  prove vs fix, T-VF T-UB T-MD T-CR T-NYR routing, after Execute N=2, or choosing
  never-fix vs systematic investigate. Prefer over inventing ad-hoc Debug skill
  order. Not for running the Debug spine itself.
---

# Debug router

Announce once: **Using `debug-router`**.

Authority: Theme 17 accepted (`docs/research/reports/theme-17-debug-router.md`);  
amends Theme 14 D4. Leaf law: Theme 9 (`debug-systematic` / `debug-reproduce`).  
**Compose only.** **Draft ≠ law** (`draft-is-not-sot`).  
**Selection ≠ solving** — this skill routes; leaves do the work.

## When to use

- Choosing between prove-only and investigate/fix
- Happy-path Debug branch or `implementation-router` exit on verify-fail / unclear Critical
- User asks which Debug skill to run next
- Seam triggers T-VF / T-UB / T-MD / T-CR / T-NYR when path is unclear

**Skip** (document): user already named `debug-reproduce` or `debug-systematic` — invoke that leaf directly.  
**Execute hot path:** leaves may be invoked directly with **repro-first** (no solid repro → reproduce; repro in hand → systematic). Use this router when which path is unclear.

**Out of scope:** Restating Theme 9 spine; PR/CI/Bugbot; swarm; collectors; always-on debug rule; burning Execute `verify-retry N=2`.

## Instructions

1. **Classify** debug ask: `prove-only` | `investigate-fix` | `prove-then-fix` | `skip-to-named-leaf` | `exit-design`.
2. **Seam** — note T-VF / T-UB / T-MD / T-CR / T-NYR if inbound from Execute/Verify/happy-path.
3. **Structured handoff** — goal, prior, facts+source, open question, constraints (see template). Iron law constraint: no product fix without repro or `NOT-YET-REPRODUCED`.
4. **Wire plan** — **default one entry leaf**:
   - `prove-only` → `debug-reproduce`
   - `investigate-fix` → `debug-systematic` (leaf may prefer reproduce inside spine)
   - `prove-then-fix` or **T-NYR** → optional wire `debug-reproduce` → `debug-systematic`
   - Named leaf → skip router
   - Intent/design gap → exit to `design-process` / happy-path (not a Debug leaf)
5. **Invoke** each selected leaf: announce **Using `<skill>`** and follow that skill. Do **not** paste Theme 9 law here.
6. **Budgets** — Debug uses `debug-fix-cycles` (Theme 9); do **not** burn more Execute `verify-retry N=2`.
7. **Stop** — summarize for human, happy-path, or return to Implementation; refuse PR/merge ceremony.

Read `references/debug-router-checklist.md` **when** running a non-trivial wire or recovering mid-pocket.  
Template SoT: Toolbelt `docs/templates/debug-router.md`.

## Classifier hints

| Signal | Lean |
|--------|------|
| Prove / minimize / dossier only | `debug-reproduce` |
| Fix with evidence; repro exists or will be made in spine | `debug-systematic` |
| Explicit prove-then-fix / T-NYR | reproduce → systematic |
| T-VF / T-MD / T-CR typical | `debug-systematic` (prove-first → reproduce first) |
| User named one leaf | skip router |
| “Open a PR” / merge | refuse ceremony; Debug only if bug remains |

## Anti-patterns

- Restating Theme 9 method in this skill  
- Default two-step wire on every ask  
- Guess-fix / skipping iron law  
- Always-on / global meta-router behavior  
- Giving a worker this router **and** the fix — workers get **one leaf**  
- Conflating `debug-fix-cycles` with Execute `verify-retry N=2`  

## Handoffs

| Need | Use |
|------|-----|
| Full Toolbelt ladder | `implementation-happy-path` |
| Implementation pocket | `implementation-router` |
| Prove / dossier | **`debug-reproduce`** |
| Investigate / fix | **`debug-systematic`** |
| Design wrong | `design-process` |
| Closeout readiness | `implementation-closeout` |
| Author surfaces | `author-cursor-surfaces` |
| PR / CI / merge | **Host / human** — Phase 2 |

## References

- Read `references/debug-router-checklist.md` **when** wiring a session
- SoT template: Toolbelt `docs/templates/debug-router.md`
- Theme 17: Toolbelt `docs/research/reports/theme-17-debug-router.md` (accepted)
- Leaf law: Theme 9 accepted report (via `debug-systematic` / `debug-reproduce`)
