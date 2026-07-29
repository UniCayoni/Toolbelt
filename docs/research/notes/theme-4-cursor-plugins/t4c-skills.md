---
title: "T4C — Cursor Agent Skills (Wave 1 official docs)"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-T4C]
supersedes: null
product: Cursor IDE
cursor_version: "3.13.25"
access_date: 2026-07-29
aligned_with: docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md
---

# T4C — Agent Skills deep dive (Wave 1)

**Using `docs-research` + `research-protocol`.**

## 1. Scope

- **Question / goal:** Document Cursor Agent Skills: `SKILL.md` structure, frontmatter, progressive disclosure / `references/`, load & `/` invocation, skill vs command vs rule vs agent, writing guidance, testing, plugin packaging — from **official Cursor docs** (+ official Agent Skills spec only where Cursor links it).
- **In scope:** Cursor docs skills/plugins/customize; agentskills.io overview + specification (via Cursor “Learn more”); `cursor/plugin-template` skill examples; optional E0 compare to Toolbelt `skills/*/SKILL.md`.
- **Out of scope:** Wave 2 Alexandria/community; inventing undocumented frontmatter; design locks; Anthropic blog/marketing unless linked as official Agent Skills material.
- **Comprehension type:** reuse / adaptive (author Toolbelt skills correctly).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch; WebSearch (`site:cursor.com/docs skills…`); GitHub MCP `get_file_contents` (`cursor/plugin-template`); Python frontmatter scan of `d:\Toolbelt\skills` |
| Corpora / URLs searched | https://cursor.com/docs/skills.md ; https://cursor.com/docs/reference/plugins.md ; https://cursor.com/docs/plugins.md ; https://cursor.com/docs/customize-cursor.md ; https://agentskills.io ; https://agentskills.io/specification ; https://github.com/cursor/plugin-template |
| Queries (exact) | `site:cursor.com/docs skills license compatibility allowed-tools frontmatter` |
| What was *not* searched | Alexandria RAG; forums/SO; Claude Code Anthropic docs beyond agentskills.io; Cursor changelog body beyond Customize link; `/llms.txt` full crawl |
| Provenance | Entity←Cursor docs + Agent Skills spec + plugin-template + local Toolbelt skills; Activity=T4C Wave 1 fetch 2026-07-29; Agent=gatherer-T4C |

**D0 pin (from campaign D0 note):** Cursor `in_use` build **3.13.25** [E0: `d0-cursor-plugins-identity.md`]. Docs = live cursor.com/docs (no release-tag pin) → version skew **unknown**.

**D2 Diátaxis:**

| URL | Type | Trust for API truth |
|-----|------|---------------------|
| cursor.com/docs/skills.md | how-to + reference (frontmatter table) | high for Cursor skill behavior |
| cursor.com/docs/reference/plugins.md § Skills format | reference (subset) | high for packaging; incomplete vs skills.md |
| cursor.com/docs/plugins.md | how-to / product | medium (install/UI) |
| cursor.com/docs/customize-cursor.md | explanation / how-to | medium (component distinctions) |
| agentskills.io/specification | reference (open standard) | high for *portable* fields; not Cursor-specific |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | systematic (URL list) + hybrid (E0 frontmatter sample) |
| Why | Mission fixed URLs; optional local corroboration |
| Scope boundary | Official Cursor docs + Agent Skills spec pages Cursor links; plugin-template; `d:\Toolbelt\skills` |

## 4. Findings

### 4.1 What a skill is / discovery & load

- `FACT` [E1] Agent Skills are an open standard; a skill is a portable, version-controlled package (files / GitHub) that teaches agents domain tasks; can include scripts, templates, and references; described as progressive (load resources on demand). [E1: Agent Skills — https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] “When Cursor starts, it automatically discovers skills from skill directories and makes them available to Agent. The agent is presented with available skills and decides when they are relevant based on context.” [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] Manual invoke: type `/` in Agent chat and search for the skill name. [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] Skill directories (auto-loaded):

  | Location | Scope |
  | ------------------- | ------------------- |
  | `.agents/skills/` | Project-level |
  | `.cursor/skills/` | Project-level |
  | `~/.agents/skills/` | User-level (global) |
  | `~/.cursor/skills/` | User-level (global) |

  Plus compatibility loads from `.claude/skills/`, `.codex/skills/`, `~/.claude/skills/`, `~/.codex/skills/`. [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] Each skill is a folder containing `SKILL.md`; optional `scripts/`, `references/`, `assets/`. Cursor walks skills roots recursively; category folders are organizational; identity = folder containing `SKILL.md`. Nested `.cursor/skills/` / `.agents/skills/` anywhere in a monorepo are discovered; nested project skills are auto-scoped to that directory (similar to `paths`). [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] View discovered skills: **Customize** → **Skills**; plugin/project skills appear alongside rules in **Agent Decides**. [E1: https://cursor.com/docs/skills.md ; https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Skills from GitHub: Customize → Rules → Add Rule → Remote Rule (Github) → repo URL. [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `CLAIM` [E1] Built-in Cursor skills (e.g. `/create-skill`, `/migrate-to-skills`, `/canvas`, …) appear in a table; “Agent may also use some built-in skills automatically when your request clearly matches their purpose.” [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29] (behavior not E0-tested this pass)

### 4.2 `SKILL.md` structure & Cursor frontmatter

- `FACT` [E1] YAML frontmatter + Markdown body. Minimal documented example uses `name` + `description`; body guidance includes When to Use / Instructions (example structure, not a schema). [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] **Cursor-documented frontmatter fields** (skills.md table):

  | Field | Required | Description (docs) |
  | -------------------------- | -------- | --- |
  | `name` | Yes | Skill identifier. Lowercase letters, numbers, and hyphens only. Must match the parent folder name. |
  | `description` | Yes | What the skill does and when to use it; used by agent for relevance. |
  | `paths` | No | Glob patterns scoping skill to matching files; comma-separated string or list; only surfaced when agent works with matching files. |
  | `disable-model-invocation` | No | When `true`, only included on explicit `/skill-name`; agent will not auto-apply from context. |
  | `metadata` | No | Arbitrary key-value mapping for additional metadata. |

  [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] Legacy `globs` still accepted as fallback; new skills should use `paths`. [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] Plugins reference **Skills format** table lists only `name` + `description`, and says “For full documentation, see Skills” linking skills.md. [E1: https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `GAP` Cursor skills.md / plugins Skills format tables do **not** document skill frontmatter fields `license`, `compatibility`, or `allowed-tools`. Searched: skills.md frontmatter table; plugins.md Skills format; WebSearch `site:cursor.com/docs skills license compatibility allowed-tools`. Result: not on Cursor pages (those fields appear on Agent Skills **specification** — §4.3).

### 4.3 Progressive disclosure / optional dirs / writing guidance

- `FACT` [E1] Optional dirs: `scripts/` (executable code agents can run), `references/` (additional documentation loaded on demand), `assets/` (static templates/images/data). “Keep your main `SKILL.md` focused and move detailed reference material to separate files… agents load resources progressively—only when needed.” [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] Scripts: reference with relative paths from skill root; any language supported by the agent implementation; should be self-contained, helpful errors, handle edge cases. [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] Official Agent Skills overview (linked from Cursor “Learn more” → agentskills.io): progressive disclosure in three stages — (1) Discovery: name+description at startup; (2) Activation: full `SKILL.md` when task matches; (3) Execution: follow instructions, optionally run bundled code / load referenced files. [E1: Agent Skills Overview — https://agentskills.io — accessed 2026-07-29; Cursor links this from skills.md]
- `FACT` [E1] Official Agent Skills **specification** progressive disclosure: Metadata (~100 tokens) name+description at startup; Instructions (<5000 tokens recommended) full body on activate; Resources as needed. Keep main `SKILL.md` under 500 lines; move detail to separate files; relative paths from skill root; keep references one level deep. [E1: Specification — https://agentskills.io/specification — accessed 2026-07-29]
- `FACT` [E1] Spec recommended body sections: step-by-step instructions, I/O examples, common edge cases; “no format restrictions” on body. [E1: https://agentskills.io/specification — accessed 2026-07-29]
- `CLAIM` [E1] Cursor example skill body suggests “Use the ask questions tool if you need to clarify requirements with the user” inside Instructions. [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]

### 4.4 Official Agent Skills spec frontmatter (portable) vs Cursor extensions

- `FACT` [E1] Spec frontmatter: required `name`, `description`; optional `license`, `compatibility`, `metadata`, `allowed-tools` (experimental, space-separated tool string). Name: max 64 chars; lowercase alnum+hyphens; no leading/trailing/consecutive hyphens; must match parent directory. Description: max 1024 chars. Compatibility: max 500 if set. [E1: https://agentskills.io/specification — accessed 2026-07-29]
- `INFERENCE` [E4] Cursor docs document **Cursor-specific** fields `paths` and `disable-model-invocation` not listed in the Agent Skills specification frontmatter table; conversely Cursor docs omit `license` / `compatibility` / `allowed-tools`. Premises: (1) skills.md frontmatter table [E1 Cursor]; (2) agentskills.io/specification frontmatter table [E1 spec]. → Treat as dual surface: portable subset + Cursor extensions; do not invent Cursor support for omitted fields without E0.
- `OPEN` Does Cursor runtime honor `license`, `compatibility`, `allowed-tools` from the portable spec? Not stated on Cursor skills.md. Follow-up: E0 experiment or Cursor engineering docs.

### 4.5 Skill vs command vs rule vs agent (docs distinctions)

- `FACT` [E1] Customize “Extension components”: **Rules** = persistent instructions shaping Agent; **Skills** = specialized capabilities Agent loads when relevant (`SKILL.md`); **Subagents** = specialized assistants with own context window; **Commands** = reusable prompts invoked with `/` in Agent chat (markdown files); **Hooks** = lifecycle scripts; **Plugins** = distributable bundles of the above (+ MCP). [E1: https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29]
- `FACT` [E1] Plugins overview component table: Rules (`.mdc`), Skills (specialized agent capabilities), Agents (custom agent configs/prompts), Commands, MCP, Hooks. [E1: https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Skills appear under **Agent Decides** and can be invoked with `/skill-name`; rules can toggle Always / Agent Decides / Manual. [E1: https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `FACT` [E1] `disable-model-invocation: true` makes a skill “behave like a traditional slash command” (explicit `/` only). [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] Migration `/migrate-to-skills` (Cursor 2.4+ per docs): converts **dynamic rules** (`alwaysApply: false`/undefined and no `globs`) → standard skills; converts **slash commands** → skills with `disable-model-invocation: true`. Does **not** migrate `alwaysApply: true`, rules with specific `globs`, or user rules (not on filesystem). Output reviewed under `.cursor/skills/`. [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `GAP` No single Cursor page with a normative matrix of mutual exclusivity / precedence when a plugin ships both a command and a skill with the same name. Searched skills.md + plugins.md + customize-cursor.md. Result: distinctions described; conflict resolution not found.

### 4.6 Plugin packaging of skills

- `FACT` [E1] Default discovery: `skills/` — each subdirectory containing `SKILL.md`. Manifest field `skills` (string or array) replaces folder discovery for that component when set. Root `SKILL.md` treated as single-skill plugin only if no `skills/` dir and no manifest `skills` field. [E1: https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Example tree includes `skills/code-reviewer/SKILL.md`. Marketplace plugin entries may also list `skills` paths. Submission checklist: all skills have proper frontmatter metadata; plugin tested locally. [E1: https://cursor.com/docs/reference/plugins.md ; https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Local test path: `~/.cursor/plugins/local/<plugin>` (or symlink), then Restart / Reload Window; verify components load. [E1: https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `FACT` [E1] `cursor/plugin-template` ships `plugins/starter-simple` and `plugins/starter-advanced`, each with `skills/code-reviewer/SKILL.md` using only `name` + `description` frontmatter; body When to use + Instructions. Commit observed: `46216072ac5750f782f95bb325b4d12b7c3ae9c9`. [E1: https://github.com/cursor/plugin-template — accessed 2026-07-29 via GitHub MCP]
- `FACT` [E1] Template README: validate with `node scripts/validate-template.mjs`; requires frontmatter on skill files. [E1: plugin-template README — accessed 2026-07-29]

### 4.7 Testing

- `FACT` [E1] Cursor plugins how-to: test by loading under `~/.cursor/plugins/local` and verifying components (including skills) load after reload. [E1: https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Agent Skills specification: validate with `skills-ref validate ./my-skill` (checks frontmatter/naming). [E1: https://agentskills.io/specification — accessed 2026-07-29]
- `GAP` No Cursor-docs-described automated skill unit-test harness, golden-prompt suite, or CI skill runner beyond local plugin load + (spec) `skills-ref` / (template) `validate-template.mjs`. Searched: skills.md, plugins.md, plugins reference submission checklist. Result: not found as a dedicated skill-testing product feature.

### 4.8 Optional E0 — Toolbelt skills vs Cursor docs

- `FACT` [E0] Under `d:\Toolbelt\skills/*/SKILL.md` (and mirrored `~\.cursor\plugins\local\toolbelt\skills`), observed frontmatter keys: all five skills have `name` + `description`; `author-agents-md` and `draft-adr` also set `disable-model-invocation: true`. No observed use of `paths`, `metadata`, `license`, `compatibility`, or `allowed-tools` in these files. Optional `references/` present on all five; no `scripts/` or `assets/`. [E0: path=`d:\Toolbelt\skills\*/SKILL.md` observed 2026-07-29]
- `FACT` [E0] `disable-model-invocation` **is** documented on Cursor skills.md (not an undocumented extra). [E0 observation of local use] + [E1: skills.md]
- `OPEN` Toolbelt does not currently exercise Cursor `paths` / `metadata` or portable-spec `license`/`compatibility`/`allowed-tools` — whether to adopt is product choice, not docs GAP for `disable-model-invocation`.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Cursor skill frontmatter = name, description, paths, disable-model-invocation, metadata (+ legacy globs) | confirmed (docs) | skills.md table |
| H2 | license / compatibility / allowed-tools are Cursor-documented skill fields | rejected | absent on Cursor pages; present on agentskills.io/specification |
| H3 | Plugin reference skills table is exhaustive | rejected | subset; points to skills.md |
| H4 | Progressive disclosure is three-stage (meta → body → resources) | confirmed for open standard; Cursor paraphrases “progressive / on demand” | agentskills.io + skills.md |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Skill frontmatter completeness | Cursor plugins reference: only `name`, `description` | Cursor skills.md: + `paths`, `disable-model-invocation`, `metadata` | Prefer skills.md for skill authoring; plugins ref = packaging subset + link-out |
| Portable vs Cursor fields | agentskills.io/spec: license, compatibility, allowed-tools | Cursor skills.md: paths, disable-model-invocation | Document both surfaces; OPEN on Cursor runtime for portable-only fields |
| Progressive disclosure detail | Cursor: brief “progressive / on demand” | agentskills.io: staged token budgets / 500-line guidance | Use Cursor for product behavior; use spec for portable authoring budgets (still E1 until E0) |

## 7. Gaps & OPEN

- `GAP` Cursor docs do not list skill fields `license`, `compatibility`, `allowed-tools` (portable spec only).
- `GAP` No dedicated Cursor skill automated testing story beyond local plugin load / Customize visibility.
- `GAP` No documented name-collision rules across skills vs commands vs agents in one plugin.
- `GAP` Installing skills via “Remote Rule (Github)” under Rules UI — naming suggests rules path; behavioral equivalence to skill dirs not E0-verified.
- `OPEN` Cursor runtime support for portable-only frontmatter (`license`, `compatibility`, `allowed-tools`).
- `OPEN` Exact token budgets / “5000 tokens recommended” / “500 lines” — stated on agentskills.io; not restated on Cursor skills.md (follow Cursor vs enforce portable guidance?).
- `OPEN` Whether nested monorepo auto-scoping and `paths` interact when both apply (docs say nested scoping is “similar to paths”).

## 8. Implications (INFERENCE only — not design locks)

- `INFERENCE` [E4] For Toolbelt skill authoring against Cursor 3.13.25 docs: require `name`+`description`; use `disable-model-invocation` when slash-command-like; use `paths` for file-scoped guidance; keep detail in `references/`. Premises: §4.2, §4.3, §4.8.
- `INFERENCE` [E4] Do not treat plugins-reference Skills frontmatter table as complete. Premise: conflict log row 1.
- `INFERENCE` [E4] Treat `license`/`compatibility`/`allowed-tools` as portable-spec fields until Cursor documents or E0 confirms. Premises: §4.2 GAP, §4.4.

## 9. Source list (deduped)

1. https://cursor.com/docs/skills.md — accessed 2026-07-29
2. https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29
3. https://cursor.com/docs/plugins.md — accessed 2026-07-29
4. https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29
5. https://agentskills.io — accessed 2026-07-29 (linked from Cursor skills.md “Learn more”)
6. https://agentskills.io/specification — accessed 2026-07-29
7. https://github.com/cursor/plugin-template (commit `46216072…`) — accessed 2026-07-29
8. E0: `d:\Toolbelt\skills\*/SKILL.md` — observed 2026-07-29
9. Campaign D0: `docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md` (Cursor 3.13.25)
