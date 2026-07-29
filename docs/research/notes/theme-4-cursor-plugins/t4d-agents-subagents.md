---
title: "T4D: Cursor plugin Agents vs runtime Subagents / Explore / Task"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-T4D]
supersedes: null
campaign: theme-4-cursor-plugins
wave: 1
access_date: 2026-07-29
cursor_version: "3.13.25"
aligned_with: docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md
---

# T4D — Agents (plugin) and Subagents (runtime)

Using `docs-research` + `research-protocol`.

## 1. Scope

- Question / goal: Deep-dive official Cursor docs on **plugin Agents** (`agents/*.md`) and **runtime subagents** (Explore / Task / custom subagents); clarify terminology overlap; cover frontmatter, selection/invocation, composition with skills/rules, context isolation, testing.
- In scope: Official `cursor.com/docs` pages for plugins, plugins reference (Agents format), Customize, Subagents, Search (Explore), Hooks (Task/subagent lifecycle), Skills (subagent vs skill guidance only).
- Out of scope: Forums/E3; inventing mapping behavior; treating Cloud Agents product setup as plugin-agent SoT (cloud subagent section labeled carefully); SDK as primary SoT (noted only where it corroborates naming).
- Comprehension / research goal type: adaptive (authoring Toolbelt / plugin agent components correctly)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch; WebSearch (`site:cursor.com/docs`); Shell (read Cursor `package.json` version); Read (D0 campaign note; fetched doc dumps) |
| Corpora / URLs searched | https://cursor.com/docs/reference/plugins.md ; https://cursor.com/docs/plugins.md ; https://cursor.com/docs/customize-cursor.md ; https://cursor.com/docs/subagents.md ; https://cursor.com/docs/agent/tools/search ; https://cursor.com/docs/hooks.md ; https://cursor.com/docs/skills.md ; WebSearch queries below |
| Queries (exact) | `site:cursor.com/docs subagents Explore agent Task tool custom agents` ; `site:cursor.com/docs agents plugin agents/*.md` ; `site:cursor.com/docs plugin agents subagents "agents/" Task tool` |
| What was *not* searched | Alexandria RAG; GitHub issues/forums (E3); full Cloud Agent API/endpoints as design law; marketplace plugin source beyond incidental local create-plugin agent file; `llms.txt` (fetch timed out once) |
| Provenance (optional PROV) | Entity=Cursor public docs; Activity=Wave1 T4D fetch 2026-07-29; Agent=gatherer-T4D; wasDerivedFrom=D0 identity note + WebFetch bodies |

### D0 pin (from campaign + this session)

| Field | Value |
|-------|-------|
| Product | Cursor IDE (hosted) — status `in_use` |
| Installed version (E0) | `3.13.25` from `C:\Users\Jonyc\AppData\Local\Programs\cursor\resources\app\package.json` [E0: 2026-07-29] |
| Docs | Live cursor.com/docs — no release-tag pin → skew **unknown** vs build |

### Diátaxis (D2)

| URL | Type | Trust for behavioral truth |
|-----|------|----------------------------|
| `/docs/reference/plugins` | reference | high for plugin Agents **file format / discovery** |
| `/docs/plugins` | how-to + overview | medium (install/test local; component inventory) |
| `/docs/customize-cursor` | explanation / index | medium (terminology: Plugins package **subagents**) |
| `/docs/subagents` | how-to + reference-ish | high for **runtime** subagent behavior/frontmatter |
| `/docs/agent/tools/search` | how-to | high for Explore subagent mention |
| `/docs/hooks` | reference | high for Task tool ↔ subagent lifecycle hooks |
| `/docs/skills` | how-to + reference | medium for skills vs subagents decision table (via subagents page link) |

OpenAPI/contracts: **N/A** (prose product docs).

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | systematic (Wave 1 official docs only) |
| Why this mode | User mission: cite-or-omit; no invention; separate plugin-agents vs runtime-subagents |
| Scope boundary | Official docs URLs above; cloud product docs only when clearly about subagent customization |

---

## 4. Findings

### A. Terminology: two layers (explicit separation)

Docs use overlapping words (**Agents**, **Subagents**, **Task**, **Explore**) for related but differently documented surfaces. Below: **plugin-agents** vs **runtime-subagents**.

#### A1 — Plugin Agents (distributable component)

- `FACT` [E1] Plugins can bundle an **Agents** component described as “Custom agent configurations and prompts.” [E1: Plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Plugin Agents are markdown files under `agents/` (default discovery: all `.md`, `.mdc`, or `.markdown` files). Manifest optional field `agents` (string or array) overrides folder discovery when set. [E1: Plugins reference — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Plugin Agent frontmatter fields documented: `name` (string, lowercase kebab-case identifier), `description` (string, purpose). Body = agent prompt/behavior markdown. Example file `agents/security-reviewer.md`. [E1: Plugins reference § Agents format — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Submission checklist requires rules, skills, **agents**, and commands to have “proper frontmatter metadata.” [E1: Plugins reference § Submitting — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Local plugin test path: copy/symlink under `~/.cursor/plugins/local/<plugin>`, reload window, “Verify your plugin components load … such as rules, skills, or MCP servers.” Agents not named in that verification sentence. [E1: Plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]

#### A2 — Runtime Subagents (delegation / Task)

- `FACT` [E1] **Subagents** are “specialized AI assistants that Cursor's agent can delegate tasks to,” each in its **own context window**, returning a result to the parent. Usable in editor, CLI, and Cloud Agents. [E1: Subagents — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] Customize extension table lists **Subagents** separately from Plugins/Rules/Skills/Hooks/Commands, linking to `/docs/subagents`, and states Plugins package “rules, skills, **subagents**, commands, MCP servers, and hooks.” [E1: Customize Cursor — https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29]
- `FACT` [E1] Parallel: Plugins overview table names the component **Agents**; Customize names the packaged piece **subagents**. Same campaign surface, different labels across pages. [E1: https://cursor.com/docs/plugins.md + https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29]
- `FACT` [E1] Custom runtime subagents live as markdown under project `.cursor/agents/` (also `.claude/agents/`, `.codex/agents/`) or user `~/.cursor/agents/` (and Claude/Codex user paths). Precedence: project over user; among same name, `.cursor/` over `.claude/`/`.codex/`. [E1: Subagents § File locations — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] Runtime subagent frontmatter fields: `name`, `description`, `model` (default `inherit`), `readonly` (default `false`), `is_background` (default `false`). `description` is “shown in **Task tool** hints” and used for delegation. [E1: Subagents § Configuration fields — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] Built-in subagents: **Explore**, **Bash**, **Browser** — used automatically for context-heavy ops; no user configuration required. [E1: Subagents § Built-in — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] Explore: own context window, faster model, parallel searches; also documented under Search tool page. Parent may request via natural language (“use a subagent to find…”). [E1: Search § Explore subagent — https://cursor.com/docs/agent/tools/search — accessed 2026-07-29] [E1: Subagents — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] Invocation: automatic delegation (complexity, custom descriptions, context/tools); explicit `/name` in prompt; natural-language mention; parallel via “multiple **Task tool** calls in a single message.” [E1: Subagents § Using subagents — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] Hooks equate subagent lifecycle to the **Task tool**: `subagentStart` / `subagentStop` “Subagent (Task tool) lifecycle”; `subagentStart` “Called before spawning a subagent (Task tool).” Matchers filter types e.g. `generalPurpose`, `explore`, `shell`. [E1: Hooks — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] Context isolation (documented): subagents start with **clean context**; parent must put needed info in the prompt; “don't have access to prior conversation history.” Foreground blocks; background returns immediately. Resume via agent ID; background state under `~/.cursor/subagents/`. [E1: Subagents — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] Nesting: since Cursor 2.5, subagents can launch child subagents within a limit; “subagent launched by another subagent can't launch further ones”; needs Task tool access; hooks/policies can block. [E1: Subagents FAQ — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] MCP: local subagents inherit parent tools including MCP; **cloud subagents** use team MCP at cursor.com/agents, not local session MCP. [E1: Subagents FAQ / Cloud subagents — https://cursor.com/docs/subagents.md — accessed 2026-07-29]

#### A3 — Mapping plugin-agents ↔ runtime-subagents

- `INFERENCE` [E4] Customize’s “Plugins … package … **subagents**” + plugins’ `agents/` component are intended as the same distributable unit as custom subagents. Premises: (1) Customize packages “subagents” in plugins [E1 customize]; (2) Plugins reference only documents an `agents/` markdown component [E1 plugins reference]; (3) no third component name for subagents in plugin structure tree.
- `GAP` Official docs do **not** state explicitly that plugin `agents/*.md` are loaded into the Task/subagent registry the same way as `.cursor/agents/*.md`, nor how install merges plugin agents into Customize “subagents.” Searched: plugins.md, reference/plugins.md, subagents.md, customize-cursor.md. Result: terminology alignment implied, wire-up unstated.
- `GAP` Plugins Agents format documents only `name` + `description`; Subagents docs add `model`, `readonly`, `is_background`. Whether plugin agents may use the richer frontmatter is **not stated** in plugins reference.
- `CLAIM` [E0] Local Cursor-published create-plugin agent file includes `model: inherit` and `readonly: true` in frontmatter (path under plugins cache). This is **not** official product docs; does not close the GAP alone. [E0: `...\create-plugin\...\agents\plugin-architect.md` observed 2026-07-29]

### B. Composition with skills / rules

- `FACT` [E1] Subagents vs skills decision table: use subagents for context isolation, parallel workstreams, multi-step specialized expertise, independent verification; use skills for single-purpose / one-shot / no separate context. Points to Skills docs. [E1: Subagents § When to use — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] Anti-pattern: “Duplicating slash commands” — prefer skill or command if no isolation needed. [E1: Subagents § Anti-patterns — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] Built-in skill `/create-subagent` “Creates custom subagents with focused roles and delegation instructions.” [E1: Skills — https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] Best practice: “Use hooks for file output” when subagents should produce structured output files consistently (links Hooks). [E1: Subagents § Best practices — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `GAP` No official Wave-1 page found that specifies how **plugin Rules** or **plugin Skills** automatically attach inside a plugin Agent / subagent run (beyond general plugin bundling and subagent tool inheritance). Searched: plugins, reference/plugins, subagents, skills, customize. Result: composition rules not spelled out for agent↔skill↔rule.

### C. Selection / invocation (runtime)

- `FACT` [E1] Automatic: task complexity/scope; custom descriptions; current context and tools; phrase hints like “use proactively” / “always use for” in `description`. [E1: Subagents § Automatic delegation — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] Explicit: `/verifier …`, natural language “Use the verifier subagent…”. Viewing: check `.cursor/agents/`; “Agent includes all custom subagents in its available tools.” [E1: Subagents — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `GAP` No docs found describing how **plugin** agent names appear in `/` picker vs project `.cursor/agents/` after marketplace/local install (only Customize manages “subagents” at a high level).

### D. Testing (as documented)

- `FACT` [E1] Plugin testing: local load from `~/.cursor/plugins/local`, reload, verify components load; checklist item “Plugin has been tested locally.” [E1: Plugins + Plugins reference — accessed 2026-07-29]
- `FACT` [E1] Subagent testing guidance: “Invest in descriptions… Test by making prompts and checking if the right subagent gets triggered.” Debug: check description/prompt; invoke explicitly with a simple task. [E1: Subagents § Best practices / FAQ — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `GAP` No automated test harness, schema validator, or unit-test API for agent/subagent markdown documented on these pages.

### E. Cloud scope (careful labeling — not plugin-format SoT)

- `FACT` [E1] **Cloud subagents** (from local session via `/in-cloud`, `/babysit`, Agents Window): VM + branch isolation; environment/MCP from cloud/team config — documented under Subagents, not under Plugins Agents format. [E1: Subagents § Cloud subagents — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `GAP` / scope: Cloud Agent API `customSubagents` and SDK `agents` / `Agent` tool naming were hit by search but **not** treated as plugin-component reference for Wave 1. Follow-up OPEN if integrator needs API/SDK parity.

### F. Naming conflicts inside runtime docs

- `CLAIM` [E1] Built-in UI names: Explore / Bash / Browser; hooks matchers cite `explore`, `shell`, `generalPurpose` (and “etc.”). Exact enum of Task `subagent_type` values not fully enumerated on Subagents page. [E1: Subagents + Hooks — accessed 2026-07-29]
- `OPEN` Confirm whether hooks’ `shell` ≡ docs’ **Bash**, and full type list vs built-ins only.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Plugin `agents/*.md` are the distributable form of custom Subagents (Task-delegable) | open / plausible | Customize “package … subagents” + plugins `agents/` only; **GAP** on load path |
| H2 | Richer frontmatter (`model`, `readonly`, `is_background`) applies to plugin agents too | open | Present in subagents.md + E0 create-plugin file; **absent** from plugins Agents format table |
| H3 | “Task tool” is the IDE spawn mechanism for all custom + built-in subagents | confirmed (docs) | Subagents parallel section + Hooks subagentStart wording [E1] |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Component name in plugins | Plugins: **Agents** [E1 plugins.md] | Customize: plugins package **subagents** [E1 customize] | Retain both; treat as synonym **OPEN** until product confirms; do not invent merge semantics |
| Built-in names | Explore / Bash / Browser [E1 subagents] | Hook types `explore`, `shell`, `generalPurpose` [E1 hooks] | Leave **OPEN**; cite both |
| Frontmatter richness | Plugins Agents: `name`, `description` only [E1] | Subagents: + `model`, `readonly`, `is_background` [E1] | Prefer documenting both surfaces; GAP on plugin support for extra fields |

## 7. Gaps & OPEN

1. **GAP** — Explicit docs statement that plugin `agents/` ≡ project/user `.cursor/agents/` subagents (install/discovery/precedence with marketplace plugins).
2. **GAP** — Whether plugin Agents may declare `model` / `readonly` / `is_background`.
3. **GAP** — How plugin Agents compose with co-bundled rules/skills (auto-apply? inherit? none?).
4. **GAP** — Dedicated testing/validation for agents beyond local plugin load + prompt-trigger checks.
5. **GAP** — Full `subagent_type` enum for Task/hooks vs marketing built-in names.
6. **OPEN** — SDK/Cloud API `Agent` tool vs IDE **Task** tool naming (out of Wave-1 plugin SoT; needed for cross-surface authoring).
7. **OPEN** — `llms.txt` index fetch timed out; may list additional agent pages.

## 8. Implications (INFERENCE only — not design locks)

- `INFERENCE` [E4] For Toolbelt/theme authoring: treat **two doc surfaces** — (1) plugin packaging under `agents/` with minimal frontmatter per plugins reference; (2) runtime behavior/isolation/Task invocation per subagents.md — until H1 confirmed. Premises: H1 open; conflicts table.
- `INFERENCE` [E4] Prefer skills for one-shot workflows and subagents when isolation/parallelism matters — locked only as **doc guidance**, not product architecture. Premise: subagents vs skills table [E1].

## 9. Source list (deduped)

1. https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29
2. https://cursor.com/docs/plugins.md — accessed 2026-07-29
3. https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29
4. https://cursor.com/docs/subagents.md — accessed 2026-07-29
5. https://cursor.com/docs/agent/tools/search — accessed 2026-07-29
6. https://cursor.com/docs/hooks.md — accessed 2026-07-29
7. https://cursor.com/docs/skills.md — accessed 2026-07-29
8. E0: Cursor `package.json` version `3.13.25` — 2026-07-29
9. E0 (incidental, non-SoT): create-plugin `agents/plugin-architect.md` — 2026-07-29
10. Campaign D0: `docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md`

## Stop conditions (docs-research)

- [x] D0 version pin recorded (`3.13.25` E0; docs live/unpinned)
- [x] Reference used for plugin Agents format; subagents page for runtime
- [x] Limitation/GAP path recorded (D5-style absences → GAP)
- [x] Conflicts logged
- [x] No design lock on uncorroborated mapping
- [x] Durable findings in this research-protocol note
