---
title: "T20A — Reference inventory / break-risk"
status: draft
theme: theme-20-guide-rename
created: 2026-08-04
depth: normal
authors: [research-gatherer]
aligned_with:
  - docs/research/notes/theme-20-guide-rename/campaign-brief.md
---

# T20A — Reference inventory / break-risk

**Using `research-protocol`.** Depth: **normal**. E0 grep 2026-08-04.

## 1. Scope

Exact hit footprint for five ids before scrub; classify **must-update (live)** vs **historical keep**.

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-08-04 |
| Tools | ripgrep `-l` / `-c` over repo (exclude node_modules) |
| Depth | normal |

## 3. Hit counts (files containing id)

| Current id | Proposed | Files (approx) | Notes |
|------------|----------|----------------|-------|
| `guide-research` | `guide-research` | **53** | Research pocket + Theme 12 |
| `guide-design` | `guide-design` | **74** | Highest; Design leaves + Theme 5 |
| `guide-implementation` | `guide-implementation` | **43** | Happy-path + Theme 14 |
| `guide-debug` | `guide-debug` | **48** | Theme 17 dense |
| `guide-standards` | `guide-standards` | **36** | Theme 19 + resolve gate |

Overlap: many files cite 2+ ids (happy-path, packs, README).

## 4. Must-update (live product) — break if missed

| Tier | Paths / surfaces |
|------|------------------|
| **P0 skill folders** | `skills/{guide-research,guide-design,guide-implementation,guide-debug,guide-standards}/` → rename folder + `name:` FM + announce string |
| **P0 templates + refresh** | `docs/templates/{research-campaign-brief→keep content, guide-design checklist, guide-implementation, guide-debug, guide-standards}.md`; `scripts/refresh-skill-references.py` mappings + dest paths under new skill folders |
| **P0 ambient** | `rules/standards-resolve-gate.mdc` → call **`guide-standards`** |
| **P0 orchestration** | `skills/implementation-happy-path/` (+ template `happy-path.md`); packs `docs/packs/README.md`; root `README.md`; `CONTRIBUTING.md`; `.cursor-plugin/plugin.json` keywords/description |
| **P0 cross-skill handoffs** | Leaves that name routers: `implementation-plan/execute/-verify/-subagents`, `debug-systematic/reproduce`, `design-*`, `research-*`, `author-standards`, `implementation-closeout`, etc. |
| **P0 authority reports** | Amend Theme 5/12/14/17/19 (and Theme 16 apply row) skill ids — do not leave accepted D-locks on old ids without amend note |
| **P0 smoke matrix / claim cards** | Update surface names for R7, D1, I1, R8, S2 (+ handoffs); keep old run logs as historical |

## 5. Historical — do not bulk-rewrite

| Class | Policy |
|-------|--------|
| Gatherer notes under `docs/research/notes/theme-*/` (pre-rename) | Keep old ids as **FACT** of past ship; optional one-line “now `guide-*`” only on theme index/report |
| Smoke **runs/** and exports | Keep verbatim evidence |
| CHANGELOG past bullets | Add new **Changed/Breaking** entry; leave old bullets |

## 6. Already-broken / skew risks (pre-scrub)

- `FACT` [E0] No dual-id aliases exist — cutover is hard for `/` invoke and Customize.  
- `FACT` [E0] Local plugin sync required after scrub or Customize shows stale ids.  
- `OPEN` Whether template filenames become `guide-*.md` or keep old filenames with new skill refs only — lean: **rename templates to match skill** for refresh clarity.  
- `GAP` No automated link checker in repo — scrub verify = targeted rg for old ids in live tiers after migrate.

## 7. Scrub order (proposed)

1. Add new `skills/guide-*` (+ templates) content from old (or git mv).  
2. Update refresh mappings; run refresh.  
3. Update rule + happy-path + packs + README + plugin.json + CONTRIBUTING.  
4. Update all **skills/** handoff strings (live).  
5. Amend Theme reports D-locks / packs.  
6. Update smoke matrix + claim cards (surface id).  
7. Delete old skill folders when empty.  
8. `rg` old ids under `skills/`, `rules/`, `docs/templates/`, `docs/packs/`, `README.md`, `CONTRIBUTING.md`, `plugin.json`, `scripts/` — expect **zero** (notes/ may remain).  
9. Sync local plugin; smoke; **human review before commit**.
