> **Superseded by Toolbelt plugin** (d:\Toolbelt, local sync to `plugins/local/toolbelt`). Kept as historical elevation record.

# Cursor elevation map (GreyMatter research â†’ integrated tools)

Status: **accepted / elevated** (2026-07-28) â€” workspace trial under `.cursor/skills/` + `.cursor/rules/`. Plugin stub scaffolded under `grey-matter/` (inert; research skills not migrated).  
Evidence: Themes 1â€“3 + `notes/secondary/sec-elevation-gates-skills.md` + Cursor Skills/Rules/Hooks/Subagents docs.

## Acceptance

- [x] Secondary refinement + this map approved
- [x] Templates copied into skill `references/`
- [x] Trial path: workspace `.cursor/skills` (plugin stub deferred)

## Principle

| Need | Prefer |
|------|--------|
| Multi-step judgment workflow | **Skill** (progressive; agent-selected or `/`) |
| Always-on short constraints | **Rule** (`alwaysApply` or intelligent) |
| Mechanical deny / approve | **Hook** |
| Isolated broad search | **Explore / subagent** (invoked from skill) |
| Rare authoring scaffolds | **Skill** with `disable-model-invocation: true` (slash-like) |

Do **not** put long checklists in always-on rules (token tax). Point rules at skills/templates.

## v1 skill pack (recommended)

| Artifact | Surface | Skill `name` | Description seed |
|----------|---------|--------------|------------------|
| `PROTOCOL.md` evidence grades | **Always Apply Rule** (or short AGENTS.md) + refs from `research-protocol` | â€” | Grades must apply even when no skill fires |
| `codebase-reconnaissance.md` | **Skill** (+ optional hook later) | `codebase-recon` | Use when exploring an unfamiliar codebase or before non-trivial implementation; complete S0â€“S16 before write tools. |
| `documentation-research.md` | **Skill** | `docs-research` | Use when relying on third-party or project documentation for APIs/behavior; version-pin, classify, limitation-scan, corroborate docsâ†”code. |
| `claim-citation.md` + `research-note.md` | Fold into **`research-protocol`** skill `references/` | `research-protocol` | Use when writing research notes, claims, or design locks; enforce cite-or-omit and E0â€“E4. |
| `agents-md-skeleton.md` | Explicit skill | `author-agents-md` | Use when creating or revising AGENTS.md; keep under size budgets and progressive disclosure. |
| `adr-minimal.md` | Explicit skill | `draft-adr` | Use when recording an architecture decision with status and SoT links. |

Synonyms from [Secondary elevation](53b8f1ee-f441-4380-ac21-5dec3213799b) (`codebase-reconnaissance`, separate `research-note`/`claim-citation`) are acceptable; integrator prefers the five-skill fold above.

## Rules (thin)

| Rule idea | Type | Content |
|-----------|------|---------|
| `research-before-write` | Intelligent or always (short) | Before non-trivial edits: run `codebase-recon` or get human waive; no inventing APIs; cite-or-omit |
| `draft-is-not-sot` | Always (2â€“3 lines) | Draft/proposed notes â‰  accepted design law |

## Hooks (defer)

| Hook | When |
|------|------|
| `preToolUse` deny Write/StrReplace until recon artifact or waive flag | Only after soft skills fail E0 trials |

## Commands

Prefer skills with `disable-model-invocation: true` over separate commands (Cursor migrate-to-skills direction).

## Placement (when elevating)

- Trial: `d:\GreyMatter\.cursor\skills/<name>/SKILL.md` (workspace-gated)
- Plugin later: `grey-matter/skills/...` per plugin quality gates  
- Do **not** dump WIP into `~/.cursor/plugins/local` during priming (prior load-strategy lock)

## Explicit non-elevations (stay docs)

- Full Theme reports / PROTOCOL narrative
- `doc-layers.md` (reference linked from skills)
- Ecosystem known-issues URL catalogs (until maintained)
- Stack/RAG library choices

## Acceptance before writing SKILL.md

- [x] You approve secondary-refinement + this map
- [x] Templates frozen enough to copy into `references/`
- [x] Decide trial path: workspace `.cursor/skills` vs wait for `grey-matter/` stub â†’ **workspace skills; stub on hold**

## Shipped (workspace)

See `.cursor/skills/{codebase-recon,docs-research,research-protocol,author-agents-md,draft-adr}/` and `.cursor/rules/{research-protocol-grades,research-before-write,draft-is-not-sot}.mdc`.
