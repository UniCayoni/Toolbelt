---
title: "Theme 25 — Docs hygiene (wording + markdownlint)"
status: accepted
theme: theme-25-docs-hygiene
created: 2026-08-05
updated: 2026-08-05
accepted: 2026-08-05
accepted_by: human (Jonathan)
authors: [hygiene]
depth: normal
aligned_with:
  - docs/research/notes/theme-25-docs-hygiene/campaign-brief.md
  - .markdownlint-cli2.jsonc
---

# Theme 25 — Docs hygiene

**Status:** **accepted** (hygiene elevate) — 2026-08-05.  
Tier A wording + project-wide lint green under house config. Tier B/C historical note wording deferred (intentional).

## Decisions

| # | Decision |
|---|----------|
| D1 | Theme id **`theme-25-docs-hygiene`** |
| D2 | Ship `.markdownlint-cli2.jsonc` tuned for Toolbelt (no MD013/MD060 war) |
| D3 | Ignore `docs/archive/**` for lint |
| D4 | Tier A wording: playbook Theme 24 name → `author-learning`; Theme 23 report parks updated |
| D5 | Autofix + manual fix → **0** markdownlint errors on active tree |
| D6 | Historical “learn-back” in draft gatherer notes = history, not live voice |

## Verify

```text
npx markdownlint-cli2   # expect Summary: 0
```

Reload after sync if skill references changed (`plan-minimal`, campaign brief).
