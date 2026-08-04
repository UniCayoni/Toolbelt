---
name: guide-standards
description: >-
  Resolve which host standards modules to load (formerly standards-router):
  classify by action, wording, skill, path, and intent, then emit
  standards_modules pointers without pasting full rule bodies. Use when
  guide-standards, standards-router, which standards apply, load coding
  standards modules, selective standards, or when the standards-resolve-gate
  finds an accepted catalog. Prefer over dumping an entire standards profile
  into context. Compose-only — not for authoring standards.
---

# Guide standards

Announce once: **Using `guide-standards`**.

Authority: Theme 19 accepted (`docs/research/reports/theme-19-standards-apply.md`);  
Theme 21 fan-out callers (`docs/research/reports/theme-21-standards-fanout.md`).  
Feedstock: Theme 16 (`author-standards` profiles).  
**Compose only** — pointers, not rule dumps. **Draft ≠ law** (`draft-is-not-sot`).  
**Selection ≠ authoring** — use `author-standards` to write/derive profiles.

## When to use

- Ambient **standards-resolve-gate** found an accepted host catalog (or user asks which standards apply)
- Pocket guides (`guide-research` / `guide-design` / `guide-implementation` / `guide-debug`) if-present resolve (Theme 21)
- Before Plan/Execute/Closeout work when modules are unclear
- Task/subagent needs a `standards_modules` handoff packet
- User asks to load relevant coding standards without the whole corpus

**Skip** (document): no catalog / no accepted modules → **no-op** (not an error).  
**Skip:** modules already pinned for this turn with clear paths.  
**Skip:** user only wants to *author* standards → `author-standards`.

**Out of scope:** Toolbelt-universal coding law; embedding full modules in this skill; PR/merge ceremony; global meta-router; auto-promote draft/proposed.

## Instructions

1. **Locate catalog** — prefer host `docs/standards/index.md` (or path from AGENTS / user). If absent or status not **accepted**, or zero accepted modules → **stop (no-op)**.
2. **Classify** using action, wording, skill id, **caller pocket guide**, path globs, perceived intent (see checklist). If ambiguous → ask once or emit **core-only** if catalog defines a core module.
3. **Select modules** — only `status: accepted` rows whose `applies_to_paths` / skills/pockets match the **caller pocket**. One-file Theme 16 profile listed in the catalog counts as a single module when its tags match.
4. **Emit handoff** — `standards_catalog` + `standards_modules[{id,path,reason}]`. **Do not paste** module rule tables into the router output.
5. **Load** — read the pointed module files (or pass paths into Task/subagent prompts). Prefer progressive disclosure; do not preload the entire catalog corpus.
6. **Hand off** — continue the caller’s pocket work with modules in context; if profiles need authoring → `author-standards`.

Read `references/guide-standards-checklist.md` **when** resolving a non-trivial ask.  
Catalog SoT templates: Toolbelt `docs/templates/standards-catalog.md`, `standards-module.md`.

## Classifier hints

| Signal | Lean |
|--------|------|
| Caller `guide-research` | research / principles / method-inclination modules — not Impl technical by default |
| Caller `guide-design` | design / principles / design-inclination modules — not Impl technical by default |
| Caller `guide-implementation` / `guide-debug` | technical modules (naming/layout/tests/safety) matching paths |
| Authoring skill / Cursor surface | modules tagged skills / authoring / markdown |
| Research note / protocol | research pocket modules |
| Implement code under `src/` etc. | impl / language modules matching globs |
| Closeout / ship-ready check | closeout + any required core |
| Secrets / safety wording | core-safety (if present) |
| No catalog / all draft | **no-op** |

## Anti-patterns

- Dumping full standards into the chat or always-on rule  
- Treating draft/proposed modules as law  
- Inventing Toolbelt-universal style when catalog absent  
- Becoming a global skill meta-router  
- Replacing `author-standards` authoring modes  
- Auto-applying Impl technical modules on research/design entry without catalog match  

## Handoffs

| Need | Use |
|------|-----|
| Author / derive / bind-check profiles | **`author-standards`** |
| Pocket guides (callers) | `guide-research`, `guide-design`, `guide-implementation`, `guide-debug` |
| Plan / Execute / Closeout | `implementation-plan`, `implementation-execute`, `implementation-closeout` |
| Full ladder | `implementation-happy-path` |
| Recon / brownfield derive feedstock | `research-codebase-recon` (S12b) → `author-standards` derive |
| Cursor packaging | `author-cursor-surfaces` |

## References

- Read `references/guide-standards-checklist.md` **when** resolving modules
- Read `references/standards-catalog.md` **when** creating/updating a host index (SoT: `docs/templates/standards-catalog.md`)
- Read `references/standards-module.md` **when** adding a module stub (SoT: `docs/templates/standards-module.md`)
- Theme 19: Toolbelt `docs/research/reports/theme-19-standards-apply.md` (accepted)
- Theme 21: Toolbelt `docs/research/reports/theme-21-standards-fanout.md` (accepted)
- Theme 16: Toolbelt `docs/research/reports/theme-16-host-standards.md` (accepted)
