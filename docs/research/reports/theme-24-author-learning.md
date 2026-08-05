---
title: "Theme 24 — Author-learning / quality-gated harvest (integrated report)"
status: accepted
theme: theme-24-author-learning
created: 2026-08-05
updated: 2026-08-05
accepted: 2026-08-05
acceptance_scope: method_and_elevate_t24_author_learning_v2
accepted_by: human (Jonathan)
authors: [integrator]
depth: deep
stop_reason: diminishing_returns_plus_2
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-24-author-learning/campaign-brief.md
  - docs/research/notes/theme-24-author-learning/w1-integrator-synthesis-v2.md
  - docs/templates/author-learning.md
  - skills/author-learning/SKILL.md
supersedes:
  - docs/research/notes/theme-24-learn-back/campaign-brief.md
amends: null
---

# Theme 24 — Author-learning

**Status:** **accepted** (method + elevate) — 2026-08-05.  
**Using `author-cursor-surfaces`**.  
**Elevate lean:** Wave 1 integrator **v2** (quality-first); v1 denied for elevate.

## 1. Executive summary

Ships **`author-learning`**: quality-gated harvest of **host/workspace** learnings into **proposed** feedstock, then compose into `author-standards` / `author-agents-md` / `author-cursor-surfaces` / `research-draft-adr` after human accept. Evidence + guideline-quality floors before propose; human accept is last gate. Not Toolbelt plugin skill self-modify; not auto-accept; not always-on.

## 2. Elevation decisions (accepted)

| # | Decision |
|---|----------|
| D1 | Theme id **`theme-24-author-learning`** (was learn-back) |
| D2 | Skill **`author-learning`** + `docs/templates/author-learning.md`; `disable-model-invocation: true` |
| D3 | Identity: **quality-gated harvest** (not convenience router) |
| D4 | Target: host workspace skills/standards/AGENTS/ADR only |
| D5 | Floor: evidence+locator; **U / no locator → do not propose** |
| D6 | Triggers: explicit `/`; optional closeout handoff **only if** citable friction |
| D7 | Never auto-accept; draft≠SoT |
| D8 | Compose into existing author-* after accept |
| D9 | Wires: closeout, guide-meta, packs, playbook/catalog, README |
| D10 | Parks: Memories-as-law; always-on; plugin self-modify; act-by-default |
| D11 | Smoke **L1** |

## 3. Surfaces

| Surface | Change |
|---------|--------|
| `skills/author-learning/` | New |
| `docs/templates/author-learning.md` | New + refresh mapping |
| `implementation-closeout` | Optional evidence-warranted handoff |
| guide-meta / author-* / packs / playbook | Pointers |
| Theme report / CHANGELOG / plugin keywords | Theme 24 |

## 4. Research trail

Deep W1 (T24C/D/F/G) → v1 integrator **denied for elevate** → v2 quality-first lean **accepted**.

## 5. Acceptance checklist

- [x] Scope + v2 lean accepted — 2026-08-05  
- [x] Elevate via `author-cursor-surfaces`  
- [x] Smoke L1 (see Theme 11 runs)  
- [x] Sync after refresh (Reload Window on your side)  
- [ ] Human review → commit/push when asked  
