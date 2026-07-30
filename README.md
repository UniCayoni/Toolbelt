# Toolbelt

Reusable Cursor **agent utility** plugin: research method (PROTOCOL grades, codebase recon, documentation research, ADRs, `AGENTS.md` authoring, Cursor surface authoring), Design, Plan (`implementation-plan`), and Execute (`implementation-execute`).

| Install this for… | Use instead for… |
|-------------------|------------------|
| **Toolbelt** — how agents research and grade evidence | **grey-matter** — Brain / RAG MCP product |

## Install (local plugin)

```text
python d:\Toolbelt\scripts\sync-toolbelt-local-plugin.py
```

Then **Developer: Reload Window**. Confirm Customize → Plugins lists `toolbelt`.

Operational load uses `~/.cursor/plugins/local/toolbelt` (same pattern as grey-matter). Cursor `workspaceOpen`→`pluginPaths` auto-load remains a known limitation on some builds — prefer this sync script.

### Verify after sync

1. **Developer: Reload Window**
2. **Customize** → Plugins: `toolbelt` (display name **Toolbelt**) is listed
3. Skills: research + Design + Plan (`implementation-plan`) + Execute (`implementation-execute`, `implementation-execute-subagents`) + authoring
4. Rules: grades + draft≠SoT always-on; explore-before-write + coexistence available
5. Smoke: `/implementation-execute`, `/implementation-plan`, `/design-process` (or Customize → Skills)

## After editing method SoT

Edit `docs/PROTOCOL.md` and `docs/templates/`, then refresh skill runtime copies:

```text
python d:\Toolbelt\scripts\refresh-skill-references.py
python d:\Toolbelt\scripts\sync-toolbelt-local-plugin.py
```

Reload Window after sync.

## Layout

```text
skills/          Research + Design + Plan + Execute (`implementation-execute*`) + authoring
rules/           Grades + draft≠SoT (always); explore-before-write + Superpowers coexistence (intelligent)
docs/PROTOCOL.md Method law
docs/templates/  Checklist/template SoT (skills copy into references/)
docs/plans/      Durable implementation plans (non-trivial)
docs/design/     Design notes (when used)
docs/adr/        ADRs
docs/research/   Theme reports + gatherer notes (method history)
docs/archive/    Smoke, sources, elevation map, harness ADR (frozen)
docs/packs/      Pack index (Research / Design / Plan shipped; Quality stub)
```

## Skills (v1)

| Skill | Use when |
|-------|----------|
| `codebase-recon` | Unfamiliar repo / before non-trivial implementation |
| `docs-research` | Third-party or product docs with version pin |
| `research-protocol` | Full Method-envelope research notes; **normal** (default) vs **deep** theme campaigns |
| `author-agents-md` | Create/revise `AGENTS.md` (`/` invoke) |
| `draft-adr` | Record an architecture/process decision (`/` invoke) |
| `author-cursor-surfaces` | Author/compose skills, rules, commands, hooks to Theme 4 standards (`/` invoke); optional Cursor `/create-*` scaffold then Toolbelt reinforce |

Announce **Using `<skill-name>`** once when a research skill applies.

## Note output paths

Prefer the **host project’s** research notes directory:

1. `docs/research/notes/` if it exists in the workspace
2. Else a path the user specifies
3. Else ask before writing

Do not assume GreyMatter paths.

## Growth

Future packs (code quality, standards, parallel workflows) land as additional flat `skills/<name>/` entries. See [docs/packs/README.md](./docs/packs/README.md). Do not pile new always-apply rules without need.

Plugin packaging / skill-authoring policy: accepted Theme 4 report — [docs/research/reports/theme-4-cursor-plugin-components.md](./docs/research/reports/theme-4-cursor-plugin-components.md).
