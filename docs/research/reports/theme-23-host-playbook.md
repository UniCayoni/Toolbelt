---
title: "Theme 23 — Host adoption playbook (integrated report)"
status: accepted
theme: theme-23-host-playbook
created: 2026-08-04
updated: 2026-08-04
accepted: 2026-08-04
acceptance_scope: method_and_elevate_t23_host_playbook
accepted_by: human (Jonathan)
authors: [integrator]
depth: deep
stop_reason: diminishing_returns_plus_2
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-23-host-playbook/campaign-brief.md
  - docs/research/notes/theme-23-host-playbook/w1-integrator-synthesis.md
  - docs/host-playbook.md
  - docs/host-playbook-catalog.md
supersedes: null
amends: null
---

# Theme 23 — Host adoption playbook

**Status:** **accepted** (method + elevate) — 2026-08-04.  
**Using `author-cursor-surfaces`**.  
**Depth:** deep; Wave 2 skipped (`diminishing_returns_plus_2`).

## 1. Executive summary

Ships host-facing **setup + use** docs: cold path install → verify → **`guide-meta`** → pocket / happy-path flows; compact **catalog as reference** (not opening wall); maintenance contract so playbook does not drift from live skills. Explicitly **not** Theme 24 learn-back, Phase 2 CI doc-drift, or Superpowers always-bootstrap as Toolbelt law.

## 2. Elevation decisions (accepted)

| # | Decision |
|---|----------|
| D1 | Theme id **`theme-23-host-playbook`** (split from learn-back → Theme 24) |
| D2 | SoT path **`docs/host-playbook.md`** + companion **`docs/host-playbook-catalog.md`** |
| D3 | Genre: host setup/use (not ops incident playbook) |
| D4 | Start-here: **`guide-meta`** + smallest sufficient entry; happy-path when full ladder |
| D5 | Catalog is progressive disclosure / reference — not cold-start wall |
| D6 | Always-on rules called out (3) + empty standards shelf = normal no-op |
| D7 | Conflict: live **`SKILL.md` wins**; fix playbook |
| D8 | Maintenance: `author-cursor-surfaces` checklist §5 + CONTRIBUTING mirror |
| D9 | Wires: README, packs row, `guide-meta` handoff to playbook |
| D10 | Parks: Theme 24; Phase 2 CI drift automation; always-on meta |

## 3. Surfaces

| Surface | Change |
|---------|--------|
| `docs/host-playbook.md` | New (active) |
| `docs/host-playbook-catalog.md` | New (active) — from T23A |
| `docs/templates/author-cursor-surfaces.md` | §5 host-playbook drift |
| `skills/author-cursor-surfaces/SKILL.md` | Steps for playbook drift |
| `skills/guide-meta/` + template | Point hosts to playbook |
| README / CONTRIBUTING / packs / CHANGELOG | Pointers + maintenance line |

## 4. Research trail

| Artifact | Role |
|----------|------|
| `t23a-toolbox-inventory.md` | E0 surface matrix → catalog feedstock |
| `t23b-*` + `t23d-*` | Playbook craft / maintenance leans (Wave 1) |
| `w1-integrator-synthesis.md` | Human-accepted lean (2026-08-04) |
| Campaign board | Deep; stop after W1 |

## 5. Acceptance checklist

- [x] Wave 1 stop + TOC/maintenance lean accepted — 2026-08-04  
- [x] Elevate playbook + catalog + maintenance wires  
- [x] Smoke H1 **PASS** (`H1-theme23-20260804.md`)  
- [x] Sync after refresh (Reload Window on your side)  
- [ ] Human review → commit/push when asked  
