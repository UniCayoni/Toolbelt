---
title: "Docs research: Cursor plugins (D0 identity + campaign plan)"
status: draft
created: 2026-07-29
product: "Cursor IDE (hosted)"
installed_version: "3.13.25 (E0 from Local AppData package.json)"
docs_version_or_url: "https://cursor.com/docs/plugins + https://cursor.com/docs/reference/plugins (accessed 2026-07-29; live docs, no pinned tag)"
aligned_with: docs/research/reports/theme-3-researching-documentation.md
protocol_steps: D0-D14
campaign: theme-4-cursor-plugins
---

# Documentation research checklist — Cursor plugins campaign

**Rule:** Official docs are E1 hypotheses until corroborated. Forums/issues are E3 discovery only.

## D0 — Identity & version pin

| Field | Value |
|-------|-------|
| Product / package / homepage | Cursor IDE — https://cursor.com |
| Installed version (E0) | `3.13.25` from `C:\Users\Jonyc\AppData\Local\Programs\cursor\resources\app\package.json` [E0: path observed 2026-07-29] |
| Docs version / URL slug | Live docs at cursor.com/docs — **no release-tag pin found** → treat as current public docs; skew **unknown** vs build |
| Version skew? | unknown |

Session corroboration: Toolbelt workspace `d:\Toolbelt`; Cursor plugins in use (toolbelt, create-plugin cache, etc.). Status: `in_use`.

## D1 — Entry indexes

- [x] Official docs home — https://cursor.com/docs
- [x] Optional `/llms.txt` — `https://cursor.com/docs/llms.txt` **404** on 2026-07-29 (`GAP`); plugins reference sitemap still links `/llms.txt` [E0 WebFetch; E1 reference sitemap]
- Alexandria Wave 2: prefer `ai_llm_agents` (see `wave2-staging-alexandria-github.md` — Cursor-plugin-specific RAG coverage currently **weak**)
- Component docs (Wave 1 verify):
  - https://cursor.com/docs/plugins.md
  - https://cursor.com/docs/reference/plugins.md (coordinator fetch OK)
  - https://cursor.com/docs/rules.md / skills.md / hooks.md / mcp.md
  - https://cursor.com/docs/customize-cursor.md
  - https://cursor.com/docs/extension-api
  - Agents/subagents/commands — gatherers confirm exact URLs

## Campaign waves

| Wave | Focus | Evidence priority |
|------|-------|-------------------|
| 1 | Official Cursor docs per component | E1 primary |
| 2 | Alexandria RAG + web + high-signal GitHub skills/plugins | E2/E3 discovery → corroborate |
| 3 | Residual GAPs until diminishing returns | Fill or mark OPEN |
| Integrate | Graded report for Toolbelt skill authoring / re-eval | Merge only; no invention |

## Component inventory (docs claim — Wave 1 must verify)

From plugins overview (search snippet, uncorroborated until fetch): Rules, Skills, Agents, Commands, MCP Servers, Hooks + `.cursor-plugin/plugin.json` manifest / marketplace / local paths.

## Parallel gatherer assignments (Wave 1)

| ID | Scope | Output note |
|----|-------|-------------|
| T4A | Manifest, discovery, marketplace, local install, extension `registerPath` | `t4a-plugin-manifest-marketplace.md` |
| T4B | Rules + AGENTS.md | `t4b-rules-agentsmd.md` |
| T4C | Skills (SKILL.md, progressive disclosure, disable-model-invocation) | `t4c-skills.md` |
| T4D | Agents / subagents (plugin agents) | `t4d-agents-subagents.md` |
| T4E | Commands (+ migrate-to-skills if documented) | `t4e-commands.md` |
| T4F | Hooks (events, I/O, testing) | `t4f-hooks.md` |
| T4G | MCP servers in plugins | `t4g-mcp-in-plugins.md` |

Each gatherer: **Using `docs-research` + `research-protocol`**; cite-or-omit; prefer reference docs; mark GAP/OPEN; write full Method block.

## D2–D14

Deferred to per-component notes + integrator report.
