---
title: "Theme 13 — Contributor / GitHub change workflow (integrated report)"
status: accepted
theme: theme-13-contributor-workflow
created: 2026-07-31
updated: 2026-07-31
accepted: 2026-07-31
acceptance_scope: contributor_docs_t13
accepted_by: human (Jonathan)
authors: [integrator]
depth: normal
stop_reason: normal_compose_sufficient
protocol: docs/PROTOCOL.md
decision_lean: quality_over_ease
aligned_with:
  - docs/research/notes/theme-13-contributor-workflow/campaign-brief.md
  - docs/research/notes/theme-13-contributor-workflow/t13a-decision-culture.md
  - docs/research/notes/theme-13-contributor-workflow/t13b-contribution-ux.md
  - docs/research/notes/theme-13-contributor-workflow/t13c-surface-lean.md
supersedes: null
---

# Theme 13 — Contributor / GitHub change workflow

**Status:** **accepted** (contributor docs) — 2026-07-31.  
**Elevated:** `CONTRIBUTING.md` + `.github/pull_request_template.md` + README/packs pointers.  
**Depth:** normal (T13A E0 + T13B primary docs + T13C compose). No deep fleet.  
**Decision lean:** **quality over ease** (human 2026-07-31).

**Using `research-protocol`** · integrator.  
**Using `author-cursor-surfaces`** · elevate (docs surfaces).

### Elevation decisions (accepted — quality lean)

| # | Decision |
|---|----------|
| D1 | Theme id **`theme-13-contributor-workflow`** |
| D2 | Fill Phase 2 **contributor docs** first; **no** new contribution skill |
| D3 | Ship root **`CONTRIBUTING.md`** that front-loads Toolbelt culture (draft≠SoT, cite-or-omit, accept→elevate, domain-first names, AI disclosure) — thorough, not stubby |
| D4 | Ship **`.github/pull_request_template.md`** with complete checklist (change type, issue/discussion link for method/skills, AI disclosure, human reviewed diff, skill sync/Reload) |
| D5 | README + packs point to Contributing; packs status: contributor docs shipped, **CI/Bugbot still Phase 2** |
| D6 | Prefer **GitHub Discussions** for proposals (quality of intake) — operator enables in Settings |
| D7 | Park: CLA day-one, Superpowers `dev`/eval harness as law, fat CI as contribution blocker, Continue as live SoT |
| D8 | Large method/skill changes: issue or Discussion → research/accept path → `author-cursor-surfaces`; small docs/typos may PR directly |
| D9 | Deep T13B fleet **not required** for this elevate |

---

## 1. Executive summary

Toolbelt already has a strong internal change culture (T13A) but no discoverable GitHub contributor path (G1). External comparators (GitHub Docs, agentskills, Superpowers, Aider) show a consistent MVP: **CONTRIBUTING + PR template**, discuss-before-large-change, and **AI/agent disclosure** for agent-era repos. Quality lean means those docs should encode Toolbelt’s accept gates clearly — not the shortest possible boilerplate, and not a new skill or CI religion.

---

## 2. Sources

- [`campaign-brief.md`](../notes/theme-13-contributor-workflow/campaign-brief.md)  
- [`t13a-decision-culture.md`](../notes/theme-13-contributor-workflow/t13a-decision-culture.md)  
- [`t13b-contribution-ux.md`](../notes/theme-13-contributor-workflow/t13b-contribution-ux.md)  
- [`t13c-surface-lean.md`](../notes/theme-13-contributor-workflow/t13c-surface-lean.md)  
- Packs / Theme 9–10 Phase 2 parks (E0)

---

## 3. Culture to protect (from T13A)

```text
research (± guide-research) → draft notes → human accept → author-cursor-surfaces
  → refresh + sync + Reload → optional E0 smokes → hand human
PR/CI = Phase 2 (not happy-path owned)
draft/proposed ≠ law
```

---

## 4. External atoms kept (from T13B)

| Keep | Source class |
|------|----------------|
| CONTRIBUTING in root / `.github` / docs | GitHub E1 |
| PR template on default branch | GitHub E1 |
| Discuss/issue before large change | Aider / agentskills E1 |
| AI disclosure | agentskills / Superpowers E1 |
| Explicit non-acceptance of drive-by skills | Superpowers / agentskills E1 |

---

## 5. Elevation status

| Surface | Status |
|---------|--------|
| `CONTRIBUTING.md` | **Shipped** |
| `.github/pull_request_template.md` | **Shipped** |
| README / packs pointers | **Shipped** |
| New skill | **Rejected** |
| CLA / fat CI / `dev` branch | **Parked** |
| GitHub Discussions | **Operator** — required before marketplace; see marketplace prep checklist |

---

## 6. Acceptance checklist

- [x] Human accepted this report (quality decisions D1–D9) — 2026-07-31  
- [x] Elevate CONTRIBUTING + PR template + README/packs  
- [ ] Operator GitHub/marketplace items — tracked in marketplace prep **Pre-marketplace operator checklist** ([`docs/research/notes/marketplace-prep/review-plugin-submission-2026-07-30.md`](../notes/marketplace-prep/review-plugin-submission-2026-07-30.md)): push, public repo, Discussions, Contributing/PR UI verify  
