---
name: implementation-happy-path
description: >-
  Orchestrate Toolbelt’s end-to-end happy path: classify the ask, then route
  through research (as needed), design gate, optional ADR, plan, plan-verify,
  execute or execute-subagents, execute-verify, and debug branch — invoking
  existing skills without restating pocket law. Use when happy-path,
  toolbelt workflow, full feature pipeline, cold-start ladder, where do I
  start, or controller routing for subagent development. Prefer over inventing
  an ad-hoc multi-skill order.
---

# Implementation happy-path

Announce once: **Using `implementation-happy-path`**.

Authority: Theme 10 accepted (`docs/research/reports/theme-10-happy-path.md`).  
**Compose only** — pocket SoT stays in Themes 5–9 skills. **Draft ≠ law** (`draft-is-not-sot`).

**Identity:** Thin **orchestration** for cold agents and subagent **controllers**. Not a new method pocket. Not an always-on rule. Not PR/CI packaging.

## When to use

- Starting non-trivial feature work and needing the Toolbelt ladder order
- Controller / parent agent routing stages across Design → Plan → Execute → Verify → Debug
- User asks for happy-path / full workflow / “which Toolbelt skills in what order”

**Do not use as the only skill inside a worker** implementing a single task — give workers one pocket skill.

## Classifier (step 0)

| Ask type | Entry |
|----------|--------|
| New / changed **feature** | Happy path below (research as needed → design → …) |
| **Bug** / verify-fail / unclear Critical | `reproduce-bug` and/or `systematic-debug` (return to plan if design wrong) |
| **Research** / theme campaign | `research-protocol` (+ recon/docs); continue to design only after accept |
| **Author** skill/rule/command | `author-cursor-surfaces` |
| **Trivial** one-file tweak | Document skip of durable Design/Plan; implement carefully (Plan/Design intelligent exception) |

## Happy path (feature)

Each step: announce **Using `<skill>`** and follow that skill. Do **not** paste its spine here.

1. **Research (as needed)** — `codebase-recon` / `docs-research` / `research-protocol`  
   Skip when code is familiar, no docs pin, and no deep campaign.
2. **Design** — `design-process` → domain skill (`technical-design` or creative-*) → **human accept**  
   Skip for pure bug-fix with clear repro, research-only, or documented trivial exception.
3. **ADR (optional)** — `draft-adr` when architectural locks need recording.
4. **Plan** — `implementation-plan` → durable `docs/plans/…` when non-trivial.
5. **Plan-verify** — `implementation-plan-verify` → Meta `ready` (PASS*).
6. **Execute** — `implementation-execute` **or** `implementation-execute-subagents`.
7. **Execute-verify** — `implementation-execute-verify` when non-trivial / required EOP.
8. **Debug branch** — on T-VF / T-UB / T-MD / T-CR / T-NYR → `reproduce-bug` (prove-first) and/or `systematic-debug`.  
   Do not burn more Execute `verify-retry N=2` under Debug; Debug uses `debug-fix-cycles` (Theme 9).
9. **Stop** — hand human; PR/CI/Bugbot = Phase 2 stub only (not owned here).

Read `references/implementation-happy-path-checklist.md` **when** running a full session or recovering stage.  
Template SoT: Toolbelt `docs/templates/happy-path.md`.

## Subagent model

| Role | Holds |
|------|--------|
| **Controller** (parent / execute-subagents controller) | May run this skill for routing + stage gates |
| **Worker** | **One pocket only** — plan task, execute task, debug session, etc. |

## Anti-patterns

- Re-teaching Plan/Execute/Verify/Debug law inside this skill  
- Skipping human design accept / Meta `ready` without documenting a valid skip  
- Giving a worker the full happy-path  
- Always-on rule or forcing Design on every bug  
- Conflating Execute `verify-retry N=2` with Debug `debug-fix-cycles`  
- Owning PR/merge ceremony here  

## Handoffs

| Need | Use |
|------|-----|
| Unfamiliar code | `codebase-recon` |
| Design spine | `design-process` |
| Plan / verify / execute | `implementation-plan` → `implementation-plan-verify` → `implementation-execute` (+ `-subagents`, `-verify`) |
| Bug / root cause | `reproduce-bug` / `systematic-debug` |
| Author Cursor surfaces | `author-cursor-surfaces` |
| PR / CI | Phase 2 — not this skill |

## References

- Read `references/implementation-happy-path-checklist.md` **when** tracking stages
- SoT template: Toolbelt `docs/templates/happy-path.md`
- Theme 10: Toolbelt `docs/research/reports/theme-10-happy-path.md` (accepted)
- Pocket law: Themes 5–9 accepted reports (via their skills)
