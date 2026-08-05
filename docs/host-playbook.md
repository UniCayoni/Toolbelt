---
title: "Toolbelt host playbook"
status: active
aligned_with: docs/research/reports/theme-23-host-playbook.md
created: 2026-08-04
updated: 2026-08-04
owner: Toolbelt maintainers
---

# Toolbelt host playbook

**Audience:** you installed Toolbelt in Cursor and want to **set up and use** it on a **host** project.  
**Not:** contributor CI/merge ceremony ([CONTRIBUTING.md](../CONTRIBUTING.md)); learn-back after ship (Theme 24 — separate).  
**Catalog:** compact surface reference → [host-playbook-catalog.md](./host-playbook-catalog.md).  
**Conflict rule:** if this playbook and a live `skills/*/SKILL.md` disagree, the **skill wins** — then fix this playbook.

## 1. What Toolbelt is / is not

| Is | Is not |
|----|--------|
| Agent **method** utility: research → design → plan → execute → verify → debug | A Brain / RAG product |
| Pocket `guide-*` entries + optional feature ladder | Always-on mega skill router |
| Host-owned standards **when you author them** | Toolbelt-universal coding style as law |
| Draft/proposed notes ≠ accepted law | Auto-accept of derive or design |

## 2. Install → verify

1. Install / sync per [README.md](../README.md) (`python scripts/sync-toolbelt-local-plugin.py` or marketplace).  
2. **Developer: Reload Window**.  
3. **Customize → Plugins:** Toolbelt listed; skills visible (~26).  
4. Optional smoke: `/guide-meta`, `/guide-design`.

## 3. Start here

| Ask | Prefer |
|-----|--------|
| “Which Toolbelt skill?” / fuzzy / mixed | **`guide-meta`** → exactly one next surface |
| Full new feature end-to-end | **`implementation-happy-path`** |
| One pocket only (plan/execute wire, debug, research scope…) | Matching **`guide-*`** |
| One-file obvious tweak | Document **trivial**; edit carefully — skip the ladder |

Smallest sufficient entry beats ceremony. See `guide-meta` anti-ceremony table.

## 4. Feature ladder (when)

`implementation-happy-path` chains: optional `guide-research` → `guide-design` (human accept) → optional ADR → `guide-implementation` → debug branch if needed → optional `implementation-closeout` → **human** for host git/PR ceremony.

Skip Research/Design when documented (familiar code, clear bug, trivial). Do not invent stages for show.

## 5. Host setup (copy-out)

Prefer host paths (override OK if you document them):

| Concern | Lean host path | Copy from Toolbelt template |
|---------|----------------|-----------------------------|
| Agent house ops | `AGENTS.md` | `docs/templates/agents-md-skeleton.md` |
| Research notes | `docs/research/notes/` | `research-note.md`, campaign brief, etc. |
| Design notes | `docs/design/` | (free-form; design skills) |
| ADRs | `docs/adr/` | `adr-minimal.md` |
| Plans | `docs/plans/` | `plan-minimal.md` |
| Standards catalog | `docs/standards/index.md` | `standards-catalog.md` + `standards-module.md` |
| Closeout profile | e.g. `docs/closeout/closeout-profile.md` | `closeout-profile.md` |
| Repro dossier | host choice / `REPRO.md` | `repro-light.md` |

**Rule:** copy templates into the host; do not treat Toolbelt template files as your working notes.

### Optional first standards catalog

Empty / missing accepted catalog → standards resolve **no-ops**. That is **normal**, not a failure. When ready: `/author-standards` → catalog + modules → human **accept** → selective load via `guide-standards`.

## 6. Always-on rules (3)

| Rule | Behavior |
|------|----------|
| `draft-is-not-sot` | Draft/proposed research, design, plans, ADRs ≠ accepted law |
| `research-protocol-grades` | Cite-or-omit + evidence grades on claim-bearing work |
| `standards-resolve-gate` | If accepted host catalog → `guide-standards`; else **no-op** |

Intelligent (not always-on): `research-before-write` — soft explore-before-edit on non-trivial code.

## 7. Task how-tos (goal-titled)

| Goal | Path |
|------|------|
| Scope a fuzzy research theme | `guide-research` → gather skills → human enough-to-start |
| Design before build | `guide-design` → domain `design-*` → human accept → plan |
| Wire plan → execute | `guide-implementation` (or happy-path after design) |
| Prove or fix a bug | `guide-debug` → `debug-reproduce` / `debug-systematic` |
| Which host standards apply | `guide-standards` (no-op if no catalog) |
| Write host standards | `author-standards` (proposed until accept) |
| Author a Cursor skill/rule | `author-cursor-surfaces` |
| Ship-ready check (not merge) | `implementation-closeout` |

Leaf intent / limits / handoffs: [catalog](./host-playbook-catalog.md).

## 8. When not / anti-ceremony

- Do **not** run happy-path for a typo or single known leaf.  
- Do **not** invent Toolbelt coding standards when the shelf is empty.  
- Do **not** treat chat plans as ADRs when significance triggers fire.  
- Do **not** expect Toolbelt to open/merge PRs (Phase 2 / host).  
- UX/UI product design skills: **deferred** (T5C).  
- Creative deep smokes optional; use `design-*` when the domain fits.

## 9. Maintenance (plugin authors)

When Toolbelt **skills, rules, or host-facing templates** change:

1. Update this playbook and/or [catalog](./host-playbook-catalog.md).  
2. Follow `author-cursor-surfaces` checklist (host-playbook item).  
3. Update packs/README + README skill tables ([CONTRIBUTING.md](../CONTRIBUTING.md)).  

**Owner:** Toolbelt maintainers · **Updated:** 2026-08-04 (Theme 23).
