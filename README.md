# Toolbelt

Reusable Cursor **agent utility** plugin: research method (PROTOCOL grades, codebase recon, documentation research, ADRs, `AGENTS.md` authoring, Cursor surface authoring), Design, Plan, Execute, **Verify gates** (plan-verify / execute-verify), and **Debug** (systematic-debug / reproduce-bug). Not a Brain/RAG product.

| Install this for… | Use instead for… |
|-------------------|------------------|
| **Toolbelt** — how agents research, design, plan, execute, verify, and debug | **grey-matter** — Brain / RAG MCP product |

## Install (local plugin)

```text
python d:\Toolbelt\scripts\sync-toolbelt-local-plugin.py
```

Then **Developer: Reload Window**. Confirm Customize → Plugins lists `toolbelt`.

Operational load uses `~/.cursor/plugins/local/toolbelt` (same pattern as grey-matter). Cursor `workspaceOpen`→`pluginPaths` auto-load remains a known limitation on some builds — prefer this sync script.

### Verify after sync

1. **Developer: Reload Window**
2. **Customize** → Plugins: `toolbelt` (display name **Toolbelt**) is listed
3. Skills: Research (6) + Design (5) + Plan + Plan-verify + Execute + Execute-subagents + Execute-verify + systematic-debug + reproduce-bug (**18** total)
4. Rules: grades + draft≠SoT always-on; explore-before-write + coexistence available
5. Smoke: `/implementation-plan`, `/implementation-execute`, `/design-process`, `/author-cursor-surfaces` (or Customize → Skills)

## After editing method SoT

Edit `docs/PROTOCOL.md` and `docs/templates/`, then refresh skill runtime copies:

```text
python d:\Toolbelt\scripts\refresh-skill-references.py
python d:\Toolbelt\scripts\sync-toolbelt-local-plugin.py
```

Reload Window after sync. **Elevating or revising skills/rules:** use `/author-cursor-surfaces` (Theme 4 reinforce) before treating as SoT.

## Layout

```text
skills/          Research + Design + Plan + Execute + Verify + Debug + authoring (18)
rules/           Grades + draft≠SoT (always); explore-before-write + Superpowers coexistence (intelligent)
docs/PROTOCOL.md Method law
docs/templates/  Checklist/template SoT (skills copy into references/)
docs/plans/      Durable implementation plans (non-trivial)
docs/design/     Design notes (when used)
docs/adr/        ADRs
docs/research/   Theme reports + gatherer notes (method history)
docs/archive/    Smoke, sources, elevation map, harness ADR (frozen)
docs/packs/      Pack index (Research / Design / Plan / Execute / Verify / Debug shipped; PR stub)
```

## Skills

### Research

| Skill | Use when |
|-------|----------|
| `codebase-recon` | Unfamiliar repo / before non-trivial implementation |
| `docs-research` | Third-party or product docs with version pin |
| `research-protocol` | Full Method-envelope research notes; **normal** (default) vs **deep** theme campaigns |
| `author-agents-md` | Create/revise `AGENTS.md` (`/` invoke) |
| `draft-adr` | Record an architecture/process decision (`/` invoke) |
| `author-cursor-surfaces` | Author/compose skills, rules, commands, hooks to Theme 4 standards (`/` invoke) |

### Design

| Skill | Use when |
|-------|----------|
| `design-process` | Shared design spine + human gate |
| `technical-design` | Code architecture / stack / services |
| `creative-systems-design` | Game/creative systems |
| `creative-narrative-design` | Story / quests / interactive narrative |
| `creative-world-character-design` | World bible / characters |

### Plan → Verify → Execute → Verify → Debug

| Skill | Use when |
|-------|----------|
| `implementation-plan` | Hybrid implementation plans for agents |
| `implementation-plan-verify` | Graded plan validate before Meta `ready` |
| `implementation-execute` | Execute approved plans (Done-when, N=2) |
| `implementation-execute-subagents` | Controller + fresh implementers |
| `implementation-execute-verify` | Post-green quality/readability + EOP converge |
| `systematic-debug` | Investigate / root-cause / fix with evidence (compose Cursor Debug Mode) |
| `reproduce-bug` | Never-fix: prove bug + light dossier before patch |

Announce **Using `<skill-name>`** once when a Toolbelt skill applies.

## Note output paths

Prefer the **host project’s** research notes directory:

1. `docs/research/notes/` if it exists in the workspace
2. Else a path the user specifies
3. Else ask before writing

Do not assume GreyMatter paths.

## Growth

Future packs (PR/workflow, UX/T5C, standards) land as additional flat `skills/<name>/` entries after accepted research + `/author-cursor-surfaces`. See [docs/packs/README.md](./docs/packs/README.md). Do not pile new always-apply rules without need.

Plugin packaging / skill-authoring policy: accepted Theme 4 report — [docs/research/reports/theme-4-cursor-plugin-components.md](./docs/research/reports/theme-4-cursor-plugin-components.md). Full surface audit: [docs/research/notes/theme-8-verify/author-surfaces-full-plugin-audit.md](./docs/research/notes/theme-8-verify/author-surfaces-full-plugin-audit.md).
