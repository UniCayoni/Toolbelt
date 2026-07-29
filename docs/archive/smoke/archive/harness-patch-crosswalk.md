---
title: "Harness patch crosswalk — smoke → skills/rules"
status: draft
created: 2026-07-28
---

# Cross-reference: research → patches

| Patch | Premise (prior research / smoke) | Apply to |
|-------|----------------------------------|----------|
| Graded checklist **or** research-note for S13 / short passes | Theme 2: markdown notes default; dual JSON optional [E4 sec-p1]. Smoke skipped separate research-note without losing grades. | `codebase-recon`, `docs-research`, templates S13 / stop |
| “Write tools” = implementation, not research notes | Elevation: soft explore-before-edit; hooks hard [E1 Cursor hooks; sec-elevation]. Rule wording conflated note writes with implement. | `research-before-write.mdc`, S16 wording |
| D0 hosted/`in_use` + build GAP | Theme 3 D0 version pin [E1]. Cursor smoke: app build GAP while product in use [E0 docs-cursor]. | `docs-research`, `documentation-research.md` D0 |
| Windows E0 path checks | Smoke: PowerShell one-liners empty; Python exists-check MATCH [E0]. ACI: concise reliable feedback [E1 Yang]. | `codebase-recon`, `docs-research` |
| Announce “Using `<skill>`” | Cursor skills relevance is soft [E1 skills.md]; smoke unauditable without announce. Superpowers announces; optional for GreyMatter. | all research skills |
| Coexistence vs Superpowers hard invoke | Smoke OPEN; Superpowers `using-superpowers` MUST invoke [E0]. GreyMatter soft [E4 elevation]. | short rule + skill note |
| OpenAPI tools only when schema exists | Theme 3 D12; Cursor docs smoke N/A Spectral [E0]. | `docs-research` D12 wording |

Do **not** weaken: cite-or-omit, E3 discovery ladder, version pin for packages, Explore recommended, draft≠SoT.
