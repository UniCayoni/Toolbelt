# Documentation layers — when to use which

Authority: `docs/research/reports/theme-2-agent-usable-documentation.md` §2  
Status: reference cheat sheet (not a design lock)

| Need | Prefer | Do not confuse with |
|------|--------|---------------------|
| Public docs discovery under context limits | `llms.txt` + `.md` page mirrors | Repo agent config |
| Cross-tool repo coding instructions | `AGENTS.md` | Human README marketing |
| Cursor-only conditional/scoped rules | `.cursor/rules/*.mdc` | Portable AGENTS.md (keep both; ops in AGENTS.md) |
| Claude path-scoped / memory | `CLAUDE.md` + `.claude/rules/` importing `@AGENTS.md` | Replacing AGENTS.md |
| Human doc IA / writing quality | Diátaxis types (tutorial / how-to / reference / explanation) | Agent file convention |
| Decision rationale history | ADR / MADR (`templates/adr-minimal.md`) | Implementation notes |
| Tool/API I/O enforcement | JSON Schema / OpenAPI | Narrative onboarding |
| Large knowledge on demand | Retrieval / tools / MCP | Stuffing full wikis into always-on prompts |

## Nested instruction files

Local/closer guidance generally wins in spirit, but **merge algorithms differ by product** (Cursor / Claude / Codex / VS Code). Do not assume one merge model. [Theme 2 conflict C6]
