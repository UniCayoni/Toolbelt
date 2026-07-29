---
title: "Author Cursor surfaces checklist (skills / rules / commands / hooks)"
status: active
aligned_with: docs/research/reports/theme-4-cursor-plugin-components.md
created: 2026-07-29
---

# Author Cursor surfaces — checklist

Authority: Theme 4 **accepted** report (`docs/research/reports/theme-4-cursor-plugin-components.md`).  
Used by skill `author-cursor-surfaces`. Copy into a working note if tracking a multi-step authoring job; do not edit this SoT as the deliverable.

## 0 — Outcome & mode

| Field | Value |
|-------|-------|
| Outcome (one sentence) |  |
| Mode | author \| compose \| migrate |
| Target plugin / workspace | Toolbelt \| host path \| `~/.cursor/...` |
| Status until human accepts | `draft` |

- **author** — new skill / rule / command / hooks from requirements  
- **compose** — weave existing skills/rules into a new skill (or thin rule) for an outcome  
- **migrate** — turn sprawl (long always-on rules, slash commands) into skills with correct FM  

## 1 — Choose surface (Theme 4)

Pick **one primary** surface (compose may add a thin companion rule):

| Need | Prefer |
|------|--------|
| Always-on / short constraints | Rule (`.mdc`; `alwaysApply` or `globs` / intelligent `description`) |
| Multi-step judgment, progressive detail | Skill (`SKILL.md` + optional `references/`) |
| Explicit `/` only, no auto-apply | Skill with `disable-model-invocation: true` **or** Command |
| Isolated context / parallel search | **Runtime** Subagent (Task / `.cursor/agents/`) — **not** plugin `agents/` for Task isolation (GAP) |
| Mechanical allow/deny / observe | Hook (`hooks.json` + script) |
| External tools/data | MCP (`mcp.json`) — out of this skill’s primary scope unless user asks |

**Do not:** put long checklists in `alwaysApply: true` rules · invent undocumented Cursor APIs · treat draft outputs as SoT.

## 2 — Optional Cursor built-in scaffold

Use **when available**; never hard-depend. If missing/misfires → author from Theme 4 alone.

| Intent | Built-in (examples) | Notes |
|--------|---------------------|-------|
| New skill | `/create-skill` | Scaffold only — Toolbelt reinforce required |
| Rules/commands → skills | `/migrate-to-skills` | User/workspace scope per Cursor docs; plugin `commands/` migrate eligibility GAP |
| Runtime subagent | `/create-subagent` | Writes **runtime** agents (`.cursor/agents/`), **not** plugin packaging `agents/` |

Record: scaffold used? `yes (name)` / `no` / `GAP (unavailable)`.

## 3 — Toolbelt reinforce (required)

### Skills

- [ ] `name` == parent folder (kebab-case)
- [ ] Pushy `description` (what + when + keywords); cold-start discovery
- [ ] `disable-model-invocation: true` only when slash-like / explicit `/` intended
- [ ] Body lean; detail in `references/` with **“read X when Y”** gates
- [ ] Budgets: prefer &lt;500 lines / Spec guidance; progressive disclosure
- [ ] Announce **Using \`skill-name\`** once if Toolbelt-style auditability wanted
- [ ] Compose: point to existing Toolbelt/host skills instead of duplicating (e.g. run `codebase-recon` then …)

### Rules

- [ ] `.mdc` + YAML: `description`, `alwaysApply`, optional `globs`
- [ ] Always-on stays **short**; long workflows → skill
- [ ] Intelligent rules: pushy `description` (when/keywords)

### Commands

- [ ] `commands/` file + `name` / `description` frontmatter when shipping
- [ ] Prefer skill + `disable-model-invocation` for new Toolbelt slash workflows (Cursor migrate direction)

### Hooks

- [ ] `hooks/hooks.json` + scripts; known events only (no invented event names)
- [ ] Fail-open vs `failClosed` considered; debug via Hooks tab / output channel
- [ ] Do **not** add hard write-denies unless product opts in after soft-gate failure (Toolbelt ADR stance)

## 4 — Compose map (compose mode)

| Step in outcome | Existing skill / rule / command | Action |
|-----------------|----------------------------------|--------|
|  |  | invoke / thin-wrap / link |

Prefer **orchestration skill** (numbered steps + “Using X”) over copying other skills’ bodies.

## 5 — Verify (honest)

- [ ] Paths relative; under plugin/project layout
- [ ] Local: sync/reload or project discovery; Customize shows skill/rule
- [ ] Slash skills: `/name` searchable
- [ ] No secrets in repo; plugin `${VAR}` only if MCP/variables in scope
- [ ] Human accepts before treating as SoT

## 6 — Out of scope / defer

- Marketplace submission audit → create-plugin `review-plugin-submission` if available  
- Full plugin scaffold from zero → create-plugin scaffold / `plugin-template`  
- Deep research on unknown Cursor APIs → `docs-research` / `research-protocol` (depth as needed)  
