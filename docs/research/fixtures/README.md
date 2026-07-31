---
title: "Theme 11 validation fixtures"
status: draft
theme: theme-11-validation
created: 2026-07-30
---

# Validation fixtures

In-repo smoke fixtures for Theme 11. **Not** method SoT. Agents under test should not edit claim cards or theme reports as “proof.”

| Path | Use |
|------|-----|
| `smoke-app/` | Tiny Python module + intentional bug for plan/execute/debug/repro smokes |
| (none) | Toolbelt repo itself for recon / docs-research / author-* / happy-path routing |

Copy `smoke-app/` to a temp workdir when a smoke must mutate files without touching Toolbelt SoT.
