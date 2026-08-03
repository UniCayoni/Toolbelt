---
name: implementation-happy-path
description: >-
  Orchestrate Toolbelt’s end-to-end happy path: classify the ask, then chain
  pocket routers / entries (research-scope, design-process, implementation-router)
  plus optional ADR and debug leaves — without restating pocket law. Use when
  happy-path, toolbelt workflow, full feature pipeline, cold-start ladder, where
  do I start, or controller routing for subagent development. Prefer over
  inventing an ad-hoc multi-skill order.
---

# Implementation happy-path

Announce once: **Using `implementation-happy-path`**.

Authority: Theme 10 accepted (`docs/research/reports/theme-10-happy-path.md`);  
**composition amended** by Theme 14 (`docs/research/reports/theme-14-pocket-routers.md`).  
**Compose only** — pocket SoT stays in Themes 5–9 / 12 / 14 skills. **Draft ≠ law** (`draft-is-not-sot`).

**Identity:** Thin **cross-pocket caller** for cold agents and subagent **controllers**. Chains **pocket routers / entries**, not a dump of every leaf. Not a method pocket. Not an always-on rule. Not PR/CI packaging.

## When to use

- Starting non-trivial feature work and needing the Toolbelt ladder order
- Controller / parent agent routing stages across Research → Design → Implementation → Debug
- User asks for happy-path / full workflow / “which Toolbelt skills in what order”

**Do not use as the only skill inside a worker** implementing a single task — give workers one pocket skill (or one leaf).

## Classifier (step 0)

| Ask type | Entry |
|----------|--------|
| New / changed **feature** | Happy path below |
| **Bug** / verify-fail / unclear Critical | `debug-reproduce` and/or `debug-systematic` (return to design/plan if design wrong) |
| **Research** / theme campaign | Research pocket entry (`research-scope` if tracks unclear) → research leaves; continue to design only after accept |
| **Author** skill/rule/command | `author-cursor-surfaces` |
| **Host principles / standards** | **`author-standards`** |
| **Trivial** one-file tweak | Document skip of durable Design/Plan; implement carefully |
| **Implementation pocket only** | Prefer **`implementation-router`** (no full ladder) |
| **Closeout / ship-ready check** | **`implementation-closeout`** (readiness — not PR ceremony) |

## Happy path (feature)

Each stage: announce **Using `<skill>`** and follow that skill. Do **not** paste its spine here.

1. **Research (as needed)** — pocket entry: optional **`research-scope`** when expand-first / tracks unclear → then research leaves via that skill’s handoffs (`research-codebase-recon` / `research-docs` / `research-protocol`).  
   Skip research when code is familiar, no docs pin, and no deep campaign. Skip scope when the research question is already clear.
2. **Design** — pocket entry: **`design-process`** → domain design skills → **human accept**.  
   Skip for pure bug-fix with clear repro, research-only, or documented trivial exception.
3. **ADR (optional)** — `research-draft-adr` when architectural locks need recording (leaf; not a router).
4. **Implementation** — pocket router: **`implementation-router`** (wires plan → plan-verify → execute or -subagents → execute-verify with explicit skips).  
   Do not re-list those leaves here unless recovering without the router.
5. **Debug branch** — on T-VF / T-UB / T-MD / T-CR / T-NYR → `debug-reproduce` and/or `debug-systematic` (Debug router deferred).  
   Do not burn more Execute `verify-retry N=2` under Debug; Debug uses `debug-fix-cycles` (Theme 9).
6. **Closeout readiness (optional)** — **`implementation-closeout`** when a host profile exists or user asks ship-ready/closeout check. Skip by default for trivial work. Readiness only — not merge/push/PR create.
7. **Stop** — hand human for host ceremony; CI/Bugbot/**merge automation** = Phase 2 / host (not owned here).

Read `references/implementation-happy-path-checklist.md` **when** running a full session or recovering stage.  
Template SoT: Toolbelt `docs/templates/happy-path.md`.

## Subagent model

| Role | Holds |
|------|--------|
| **Controller** (parent / execute-subagents controller) | May run this skill for routing + stage gates |
| **Worker** | **One pocket leaf** — not happy-path, not the full router wire |

## Anti-patterns

- Re-teaching Plan/Execute/Verify/Debug law inside this skill  
- Skipping human design accept / Meta `ready` without documenting a valid skip  
- Giving a worker the full happy-path  
- Bypassing `implementation-router` by pasting the old leaf ladder here as duplicate SoT  
- Always-on rule or forcing Design on every bug  
- Conflating Execute `verify-retry N=2` with Debug `debug-fix-cycles`  
- Owning PR/merge ceremony here  
- Skipping optional closeout when user explicitly asked ship-ready check  

## Handoffs

| Need | Use |
|------|-----|
| Research pocket entry | `research-scope` |
| Design pocket entry | `design-process` |
| Implementation pocket router | **`implementation-router`** |
| Closeout readiness (define/check) | **`implementation-closeout`** |
| Bug / root cause | `debug-reproduce` / `debug-systematic` |
| Author Cursor surfaces | `author-cursor-surfaces` |
| PR / CI / merge ceremony | Host / human — Phase 2 automation still not this skill |

## References

- Read `references/implementation-happy-path-checklist.md` **when** tracking stages
- SoT template: Toolbelt `docs/templates/happy-path.md`
- Theme 10: Toolbelt `docs/research/reports/theme-10-happy-path.md` (accepted)
- Theme 14: Toolbelt `docs/research/reports/theme-14-pocket-routers.md` (accepted)
- Pocket law: Themes 5–9 / 12 skills (via routers and leaves)
