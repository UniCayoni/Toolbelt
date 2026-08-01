---
title: "Theme 13 T13C — Contributor surfaces lean (compose)"
status: draft
theme: theme-13-contributor-workflow
track: T13C
created: 2026-07-31
updated: 2026-07-31
authors: [coordinator]
depth: normal
aligned_with:
  - docs/research/notes/theme-13-contributor-workflow/t13a-decision-culture.md
  - docs/research/notes/theme-13-contributor-workflow/t13b-contribution-ux.md
supersedes: null
---

# T13C — Phase 2 contributor surfaces (lean)

**Using `research-protocol`**; depth: **normal compose** (no new external gather).  
**Status:** `draft`. Not permission to elevate until human accepts Theme 13 report / this lean.  
**Decision lean:** quality over ease (human 2026-07-31) — thorough culture gates; still **docs-first** (no skill sprawl).

## Recommended MVP (docs-first, quality-complete)

| Surface | Action | Rationale |
|---------|--------|-----------|
| `CONTRIBUTING.md` (repo root) | **Elevate after accept** | Full culture + propose path (not a stub paragraph) |
| `.github/pull_request_template.md` | **Elevate after accept** | Complete checklist: AI disclosure, human review, research/accept for skills, sync/Reload |
| `README.md` | Link Contributing | Visible entry |
| Packs README | PR/workflow → **contributor docs shipped**; CI still Phase 2 | Honest status |
| New Toolbelt skill | **Defer** | Quality ≠ more skills; `author-cursor-surfaces` already exists |
| GitHub Discussions | **Lean enable** (proposal quality) | agentskills pattern; turn on in GitHub Settings |
| CLA / `dev` branch / fat CI | **Park** (T13B §9) | Not day-one theater |

## CONTRIBUTING outline (candidate sections)

1. Welcome + what this repo is (Cursor plugin, not app runtime)  
2. **Non-negotiables:** draft≠SoT; cite-or-omit; human accept before method/skill law  
3. Ways to contribute (docs typo vs method/skill vs bug)  
4. Propose large changes: issue/discussion → research-scope/theme → accept → `author-cursor-surfaces`  
5. Domain-first skill naming + sync/Reload  
6. AI/agent disclosure expectation  
7. What we usually won’t merge (drive-by skills, draft-as-law, Phase 2 CI religion)  
8. Pointers: PROTOCOL, packs, Theme reports, README install  

## PR template checklist (candidate)

- [ ] Summary / why  
- [ ] Change type: docs | research | skill/rule | other  
- [ ] Linked issue/discussion (required if method/skill)  
- [ ] AI assistance disclosed (or “hand-written”)  
- [ ] If skills/rules: followed `author-cursor-surfaces`; `name`==folder; sync script noted  
- [ ] Does **not** treat draft research as accepted SoT  
- [ ] Human reviewed the full diff  

## Next after human accept of Theme 13

1. Integrated draft report `docs/research/reports/theme-13-contributor-workflow.md`  
2. Human accept report  
3. Elevate CONTRIBUTING + PR template (+ README/packs pointer) — **no** new skill unless asked  
