---
name: guide-meta
description: >-
  Start here for Toolbelt: global front door (guide-meta). Classify a fuzzy or
  cold-start ask and name exactly one next surface — pocket guide-*, 
  implementation-happy-path, author-standards, author-learning,
  author-cursor-surfaces, or implementation-closeout — then hand off. Use when
  guide-meta, which Toolbelt skill, where do I start, how do I use Toolbelt,
  cold start, meta-router, skill router, unclear research vs design vs
  implement vs debug, or mixed multi-pocket asks. Prefer over inventing an
  ad-hoc entry or forcing the full happy-path. Not always-on. Not for running
  pocket spines itself.
---

# Guide meta

Announce once: **Using `guide-meta`**.

Authority: Theme 22 accepted (`docs/research/reports/theme-22-meta-guide.md`);  
reopens Theme 14 park of global skill-router as **opt-in skill only** (not always-on).  
**Compose only.** **Draft ≠ law** (`draft-is-not-sot`).  
**Selection ≠ solving** — this skill picks the door; the next skill does the work.

## When to use

- Cold start / “which Toolbelt skill?” / “where do I start?” / “how do I use Toolbelt?”
- Mixed or ambiguous asks spanning research vs design vs implementation vs debug
- Controller wants a single front-door classify before pocket entry

**Skip** (document): user already named a clear skill or leaf — invoke that directly.  
**Skip:** mid-pocket recovery — use that pocket’s `guide-*`, not meta.  
**Skip:** pure chat / greetings with no Toolbelt work.

**Out of scope:** Always-on / ambient meta rule; multi-skill PIPELINE planning (that is `implementation-happy-path` + pocket guides); re-teaching pocket or leaf law; standards resolve bodies (`guide-standards`); PR/CI ceremony; global alwaysApply routing. Host setup narrative lives in Toolbelt `docs/host-playbook.md` — point hosts there; do not paste the playbook into this skill.

## Instructions

1. **Classify** ask (see checklist): `feature-ladder` | `research` | `design` | `implementation-pocket` | `debug` | `standards-resolve` | `standards-author` | `author-learning` | `author-surfaces` | `closeout` | `leaf-direct` | `trivial` | `unclear` | `out-of-toolbelt`.
2. If **named skill already** → document skip; invoke that skill (or leaf).
3. **Pick exactly one next surface** from the allowlist. Prefer the **smallest sufficient entry** (see examples). Do **not** default every ask to happy-path.
4. **Structured handoff** — goal, prior, facts+source, open question, constraints (see template).
5. **Invoke** the next skill: announce **Using `<skill>`** and follow it — or stop after naming it if the user only asked which skill. Do **not** paste that skill’s spine here.
6. **Stop** — do not chain further pockets inside meta. Happy-path / pocket guides own multi-stage wires.

### Smallest sufficient entry (anti-ceremony)

| Ask shape | Prefer | Avoid |
|-----------|--------|-------|
| “Which skill?” / mixed cold ask | `guide-meta` → one pocket guide | Jumping straight into full ladder |
| Full new feature, unfamiliar | `implementation-happy-path` | Skipping design accept |
| Design already accepted; need plan/execute wire | `guide-implementation` | Full happy-path from research |
| Flaky test / prove bug | `guide-debug` | Happy-path + design theater |
| One-line typo / one-file obvious tweak | Document **trivial**; edit carefully | Durable plan + verify ladder |
| “Which standards apply?” | `guide-standards` (no-op if no catalog — **expected**) | Inventing Toolbelt style law |

Read `references/guide-meta-checklist.md` **when** the ask is ambiguous or recovering a bad entry.  
Template SoT: Toolbelt `docs/templates/guide-meta.md`.

## Classifier hints

| Signal | Next |
|--------|------|
| Full feature / cold ladder / “end to end” | `implementation-happy-path` |
| Tracks / theme scope unclear | `guide-research` |
| Options / design before build | `guide-design` |
| Plan/execute wire only (design done or skipped) | `guide-implementation` |
| Bug / verify-fail / prove vs fix | `guide-debug` |
| Which host standards modules apply | `guide-standards` |
| Write/derive host standards | `author-standards` |
| Harvest lessons → proposed host feedstock | `author-learning` |
| Author skill/rule/command | `author-cursor-surfaces` |
| Ship-ready / closeout check | `implementation-closeout` |
| User named one leaf clearly | that leaf (skip meta) |
| One-file trivial tweak | document trivial; careful edit (no durable ladder) |
| Unclear after classify | ask **one** clarifying question, then re-classify |
| Host setup / how do I adopt Toolbelt | Point to `docs/host-playbook.md` (then `/guide-meta` for work) |

## Anti-patterns

- `alwaysApply` / ambient meta rule behavior  
- Emitting a PIPELINE of many skills and “running” them inside meta  
- Replacing `implementation-happy-path` by pasting the full ladder here  
- Becoming a second `guide-standards` or dumping standards bodies  
- Forcing Design on every bug or Research on every ask  
- Giving a worker this skill **and** expecting them to implement  

## Handoffs

| Need | Use |
|------|-----|
| Full feature ladder | **`implementation-happy-path`** |
| Research / Design / Impl / Debug / Standards resolve | matching **`guide-*`** |
| Author standards / learning harvest / surfaces | `author-standards` / `author-learning` / `author-cursor-surfaces` |
| Closeout readiness | `implementation-closeout` |
| Named leaf | that leaf directly |
| Host setup / adopt Toolbelt | Toolbelt **`docs/host-playbook.md`** (+ catalog) |

## References

- Read `references/guide-meta-checklist.md` **when** classifying a non-trivial entry
- SoT template: Toolbelt `docs/templates/guide-meta.md`
- Host playbook: Toolbelt `docs/host-playbook.md` (Theme 23)
- Theme 22: Toolbelt `docs/research/reports/theme-22-meta-guide.md` (accepted)
- Theme 14 park context: `docs/research/reports/theme-14-pocket-routers.md` (D6 → skill-only reopen)
