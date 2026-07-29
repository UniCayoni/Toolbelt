---
title: "T4E — Cursor plugin Commands (slash commands)"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-T4E]
supersedes: null
access_date: 2026-07-29
cursor_version: "3.13.25"
aligned_with: docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md
---

# T4E — Commands (plugin `commands/*`, slash commands)

**Using `docs-research` + `research-protocol`.**

## 1. Scope

- Question / goal: Deep-dive Wave 1 (official Cursor docs only) on **Commands**: plugin format, frontmatter, `/` invocation, relationship to Skills (incl. migrate-to-skills), when to use commands vs skills vs agents/subagents, and whether testing is documented.
- In scope: Official `cursor.com/docs` and linked Help pages for Commands as a plugin/customize component; Skills migration guidance; Subagents anti-pattern guidance mentioning commands; Deeplinks for `.cursor/commands`; Enterprise LLM-steering mention of Commands.
- Out of scope: Wave 2 Alexandria/GitHub/community; E0 runtime verification of command loading; inventing missing schema fields; Cursor **CLI** built-in slash commands (`docs/cli/reference/slash-commands`) except as a named distinction.
- Research goal type: reuse (authoring Toolbelt / plugin command guidance later)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch; WebSearch (`site:cursor.com/docs`, `site:cursor.com/help`); llms.txt fetch; read D0 campaign note |
| Corpora / URLs searched | See §9 Source list |
| Queries (exact) | `site:cursor.com/docs commands slash commands migrate-to-skills`; `site:cursor.com/docs "slash command" OR "commands/" OR "Reusable prompts"`; `site:cursor.com/docs OR site:cursor.com/help ".cursor/commands" OR "commands directory" OR "slash commands"`; `site:cursor.com/help/customization commands markdown files invoke` |
| What was *not* searched | Alexandria RAG; GitHub issues/forums (E3); marketplace plugin source; local `~/.cursor/commands` filesystem (deferred E0); CLI slash-commands page contents beyond existence via llms.txt/search |
| Provenance (optional PROV) | Entity=Cursor public docs; Activity=T4E Wave 1 gather; Agent=gatherer-T4E + WebFetch |

**D0 pin (from campaign D0):** Cursor IDE `in_use`; installed `3.13.25` [E0 via D0 note]; live docs (no release-tag pin) → version skew **unknown**.

**D2 Diátaxis (this pass):**

| URL | Type | Trust for API truth |
|-----|------|---------------------|
| https://cursor.com/docs/reference/plugins.md | reference | high for plugin file format / discovery |
| https://cursor.com/docs/plugins.md | how-to + overview | medium |
| https://cursor.com/docs/customize-cursor.md | explanation / overview | medium (invocation wording) |
| https://cursor.com/docs/skills.md | reference + how-to | high for skills↔commands relationship |
| https://cursor.com/docs/subagents.md | how-to / explanation | medium (when-not-subagent) |
| https://cursor.com/docs/reference/deeplinks.md | reference | high for deeplink params; medium for `.cursor/commands` path claim |
| https://cursor.com/docs/enterprise/llm-safety-and-controls.md | explanation | medium (steering narrative) |
| https://cursor.com/help/customization/skills.md | how-to | medium (migrate section) |
| https://cursor.com/help/customization/plugins.md | how-to | low–medium (inventory only) |

**D7 E3:** Waived (Wave 1 official-only).

**D12 OpenAPI/contracts:** N/A (prose product docs).

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | systematic (assigned URLs) + as-needed follow links from llms.txt / in-page links |
| Why this mode | Campaign Wave 1: E1 primary only |
| Scope boundary | Commands component + documented skills/agents relationship; exclude unrelated plugin components except inventory context |

## 4. Findings

### 4.1 Plugin packaging & discovery

- `CLAIM` [E1] Plugins can bundle **Commands** alongside rules, skills, agents, MCP servers, and hooks. Quote: "Agent-executable command files." [E1: Plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Default discovery: `commands/` contains all `.md`, `.mdc`, `.markdown`, or `.txt` files. [E1: Plugins reference — Component discovery — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Manifest optional field `commands` (string or array) specifies path(s) to command files or directories; if specified, it **replaces** folder discovery for that component (default folder not also scanned). [E1: Plugins reference — Optional fields / Component discovery — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Marketplace plugin entries may also declare `commands` path(s). [E1: Plugins reference — Plugin entry fields — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]

### 4.2 Format & frontmatter

- `CLAIM` [E1] Commands are "markdown or text files defining agent-executable actions" placed in `commands/`. [E1: Plugins reference — Commands format — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Supported extensions: `.md`, `.mdc`, `.markdown`, `.txt`. [E1: same]
- `CLAIM` [E1] Commands **can** include YAML frontmatter with fields:

  | Field | Type | Description (docs) |
  |-------|------|--------------------|
  | `name` | string | Command identifier (lowercase, kebab-case) |
  | `description` | string | Brief description of what the command does |

  Example filename in docs: `commands/deploy-staging.md` with body steps. [E1: Plugins reference — Commands format — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Wording is "can include YAML frontmatter" (not stated as required in the Commands format section). Separately, submission checklist says: "All rules, skills, agents, and commands have proper frontmatter metadata." [E1: Plugins reference — Commands format + Submission checklist — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `INFERENCE` [E4] For marketplace submission, frontmatter is treated as expected even though the format section uses soft "can include." Premises: (1) soft language in Commands format; (2) checklist requires proper frontmatter. Status: partial — do not lock "required vs optional" without E0 or sharper docs.
- `GAP` Additional command frontmatter fields (beyond `name` / `description`), argument placeholders, auto-run flags, or required body structure: **not found** in official Commands format section. Searched: reference/plugins Commands format; customize-cursor Commands row; skills migrate sections. Result: only `name` + `description` documented.

### 4.3 Invocation with `/`

- `CLAIM` [E1] Customize docs define **Commands** as: "Reusable prompts you invoke with `/` in Agent chat. Commands are markdown files that define a focused workflow or action." [E1: Customize Cursor — Extension components — https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29]
- `CLAIM` [E1] Customize page states you can add/manage **commands** (among other components) and control which are active per scope; filter by user / workspace / team. [E1: Customize Cursor — https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29]
- `CLAIM` [E1] Skills are also manually invocable by typing `/` in Agent chat and searching for the skill name; built-in skills listed with `/name` (e.g. `/migrate-to-skills`). [E1: Agent Skills — https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `CLAIM` [E1] Plugin overview: skills "can be invoked manually with `/skill-name` in chat" (under Rules and skills management). [E1: Plugins — Managing installed plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `GAP` Exact `/` picker UX for **plugin** commands (namespace, collision with skills, whether `name` frontmatter vs filename becomes the slash token): **not specified** in fetched docs.
- `CLAIM` [E1] Deeplinks document custom commands living under `.cursor/commands`; command deeplink params `name` + `text`; user must review/confirm before execution; deeplinks never auto-execute. [E1: Deeplinks — Commands — https://cursor.com/docs/reference/deeplinks.md — accessed 2026-07-29]
- `GAP` Dedicated how-to for authoring user/workspace `.cursor/commands` files (file naming, frontmatter parity with plugin `commands/`, user vs workspace paths beyond deeplink mention): **no dedicated page** in llms.txt customizing section; Help Customization lists rules/skills/plugins/mcp but **no** `commands.md`. Enterprise page links "See [Commands](https://cursor.com/help/customization/rules.md)" which is the **Rules** help page (no Commands section observed). [E1: LLM Safety — Commands and workflows — https://cursor.com/docs/enterprise/llm-safety-and-controls.md — accessed 2026-07-29]; [E1: Help Rules — https://cursor.com/help/customization/rules.md — accessed 2026-07-29]; [E1: llms.txt Help Customization index — https://cursor.com/llms.txt — accessed 2026-07-29]

### 4.4 Relationship to Skills (`/migrate-to-skills`)

- `CLAIM` [E1] Built-in skill `/migrate-to-skills`: "Converts eligible dynamic rules and slash commands into Agent Skills." Listed among built-in Cursor skills. [E1: Agent Skills — Built-in Cursor skills — https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `CLAIM` [E1] Docs state migration skill is included "in 2.4". [E1: Agent Skills — Migrating rules and commands to skills — https://cursor.com/docs/skills.md — accessed 2026-07-29]; corroborated Help: "available in Cursor 2.4+". [E1: Help Skills — How do I migrate commands to skills? — https://cursor.com/help/customization/skills.md — accessed 2026-07-29]
- `CLAIM` [E1] Migrated **slash commands**: "Both user-level and workspace-level commands are converted to skills with `disable-model-invocation: true`, preserving their explicit invocation behavior." [E1: Agent Skills — Migrating… — https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `CLAIM` [E1] Steps: type `/migrate-to-skills` → agent identifies eligible rules/commands → review generated skills in `.cursor/skills/`. [E1: same]; [E1: Help Skills — https://cursor.com/help/customization/skills.md — accessed 2026-07-29]
- `CLAIM` [E1] `disable-model-invocation: true` makes a skill "behave like a traditional slash command" — only included when explicitly invoked via `/skill-name`. [E1: Agent Skills — Disabling automatic invocation — https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `GAP` Whether **plugin-bundled** `commands/` entries are in scope for `/migrate-to-skills`: docs only say user-level and workspace-level commands. Plugin commands migration: **not stated**.
- `GAP` Whether remaining first-class Commands are deprecated vs still recommended for new plugins: migrate guidance exists; plugins reference still documents Commands format; no explicit deprecation notice found in Wave 1 sources.

### 4.5 Commands vs Skills vs Agents / Subagents

- `CLAIM` [E1] Customize inventory distinguishes: Skills = specialized capabilities Agent loads when relevant (`SKILL.md`); Subagents = specialized assistants with own context; Commands = reusable `/` prompts (markdown). [E1: Customize Cursor — Extension components — https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29]
- `CLAIM` [E1] Plugins reference: Agents = custom agent configurations/prompts (`agents/`); Commands = agent-executable actions (`commands/`); Skills = specialized capabilities (`skills/*/SKILL.md`). [E1: Plugins reference — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Subagents docs anti-pattern: "**Duplicating slash commands** — If a task is single-purpose and doesn't need context isolation, use a skill or command instead" (links skills + customize-cursor `#extension-components`). [E1: Subagents — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `CLAIM` [E1] Subagents vs skills table: use skills for single-purpose / quick repeatable / one-shot / no separate context window; use subagents for isolation, parallelism, multi-step specialized expertise, independent verification. [E1: Subagents — When to use subagents — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `CLAIM` [E1] Help Skills compares **Rules vs Skills** (not Commands vs Skills): skills for multi-step workflows; rules for short guidelines. [E1: Help Skills — When should I use skills instead of rules? — https://cursor.com/help/customization/skills.md — accessed 2026-07-29]
- `CLAIM` [E1] Enterprise steering: Commands package reusable prompts invoked as slash commands (e.g. `/test`, `/deploy`); scoped to teams, projects, or users; team admins can create org-wide commands. [E1: LLM Safety — Commands and workflows — https://cursor.com/docs/enterprise/llm-safety-and-controls.md — accessed 2026-07-29]
- `GAP` Official decision matrix **Commands vs Skills** (when to keep a command vs author a skill with/without `disable-model-invocation`): not found as a dedicated table; only migrate + "skills behave like slash commands" + subagents "use skill or command."
- `CLAIM` [E1] Help Plugins component list includes Commands but **omits Agents** (unlike docs/plugins and reference). [E1: Help Plugins — https://cursor.com/help/customization/plugins.md — accessed 2026-07-29] vs [E1: Plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]

### 4.6 Testing

- `CLAIM` [E1] Local plugin test path: load from `~/.cursor/plugins/local`, restart/reload, "Verify your plugin components load in Cursor, such as rules, skills, or MCP servers." [E1: Plugins — Test plugins locally — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Submission checklist includes "Plugin has been tested locally" (generic). [E1: Plugins reference — Submission checklist — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `GAP` Dedicated testing steps for Commands (how to confirm a plugin/user command appears under `/`, invoke smoke test, CI): **not documented** beyond generic local load verification. Example list in local-test section does not mention commands explicitly.

### 4.7 Distinction: CLI slash commands

- `CLAIM` [E1] llms.txt indexes `https://cursor.com/docs/cli/reference/slash-commands.md` under CLI Reference — separate from Customize/Plugins Commands. [E1: llms.txt — https://cursor.com/llms.txt — accessed 2026-07-29]
- `INFERENCE` [E4] CLI slash-commands page is a different surface (CLI agent built-ins such as `/model`, `/mcp`, … per search snippets) and should not be conflated with plugin/`commands/*` reusable prompts without corroborating that page for Theme 4. Premises: (1) separate llms.txt section; (2) search titles describe CLI toggles. Wave 1: page not fully fetched for claim inventory → treat as OPEN if Theme 4 needs CLI parity.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Plugin Commands remain first-class distributable components | open / leaning confirmed | Still in reference format + plugins inventory; migrate targets user/workspace slash commands, not stated for plugins |
| H2 | Skills with `disable-model-invocation: true` are the preferred successor to slash-command UX | open | Documented migrate + behavioral equivalence; no deprecation of Commands |
| H3 | Enterprise "See Commands → rules.md" is a broken/mis-aimed docs link | open | Link target is Rules help; no Commands body there |
| H4 | `.cursor/commands` is the filesystem home for non-plugin slash commands | partial | Deeplinks assert directory; full authoring how-to missing |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Frontmatter required? | Commands format: "can include" [E1 reference] | Submission checklist: commands must have "proper frontmatter" [E1 reference] | Leave OPEN; recommend frontmatter for publish; soft for local until E0 |
| Plugin component inventory | docs/plugins lists Agents + Commands [E1] | help/plugins lists Commands, omits Agents [E1] | Prefer docs/plugins + reference for authoring truth; note Help incompleteness |
| "Commands" docs link | Enterprise LLM safety → help/customization/rules.md labeled Commands [E1] | That page documents Rules only [E1] | Unresolved docs drift; mark GAP for Commands how-to |

## 7. Gaps & OPEN

- `GAP` No dedicated official **Commands** how-to page (Help or Docs) for `.cursor/commands` authoring; broken/mislinked "Commands" pointer from enterprise docs.
- `GAP` Slash-token resolution rules (filename vs `name` frontmatter; plugin namespace; collisions with skills).
- `GAP` Plugin `commands/` vs user/workspace commands: behavioral parity, Customize toggles, migrate eligibility.
- `GAP` Command-specific testing / verification procedure.
- `GAP` Extra frontmatter / args / parameter UI for commands.
- `GAP` Explicit deprecation or "prefer skills" normative guidance for **new** plugin commands.
- `OPEN` Fetch/full inventory of CLI `slash-commands.md` if Theme 4 needs CLI vs IDE command taxonomy.
- `OPEN` E0: place a sample command under local plugin `commands/` and observe `/` listing (Wave 2/3 or corroboration pass).
- `OPEN` Confirm whether Help plugins omitting Agents is intentional or docs drift.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] For Toolbelt plugin authoring SoT: use **Plugins reference → Commands format** for file layout/frontmatter atoms; use **Skills** docs for `/` + migrate + `disable-model-invocation` semantics; do not invent a Commands how-to from training data. Premises: §4.2–4.4 citations; §7 GAPs.
- `INFERENCE` [E4] Prefer documenting both still-supported `commands/` and skill-with-`disable-model-invocation` patterns until Cursor publishes a clear prefer/deprecate statement. Premises: H1/H2 open; both documented.
- Do **not** promote these inferences to design locks while note `status: draft`.

## 9. Source list (deduped)

1. https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29
2. https://cursor.com/docs/plugins.md — accessed 2026-07-29
3. https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29
4. https://cursor.com/docs/skills.md — accessed 2026-07-29
5. https://cursor.com/docs/subagents.md — accessed 2026-07-29
6. https://cursor.com/docs/reference/deeplinks.md — accessed 2026-07-29
7. https://cursor.com/docs/enterprise/llm-safety-and-controls.md — accessed 2026-07-29
8. https://cursor.com/help/customization/skills.md — accessed 2026-07-29
9. https://cursor.com/help/customization/plugins.md — accessed 2026-07-29
10. https://cursor.com/help/customization/rules.md — accessed 2026-07-29 (via enterprise "Commands" link; no Commands content)
11. https://cursor.com/llms.txt — accessed 2026-07-29
12. https://cursor.com/docs/agent/prompting.md — accessed 2026-07-29 (no Commands how-to; `/` not covered beyond @-mentions)
13. Campaign D0: `docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md` — Cursor 3.13.25 E0 pin
14. Indexed but not fully claimed: https://cursor.com/docs/cli/reference/slash-commands.md (CLI surface distinction)

## Stop conditions (docs-research)

- [x] D0 version pin recorded (via D0 + this Method)
- [x] Reference used for Commands format claims
- [x] Limitation / migrate path covered (D5-ish); E3 waived
- [x] Conflicts recorded
- [x] No design lock on uncorroborated E3
- [x] Durable findings in this `research-protocol` note
