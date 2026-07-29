---
title: "T4B: Cursor Rules and AGENTS.md (Wave 1 — official docs)"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-T4B]
supersedes: null
campaign: theme-4-cursor-plugins
wave: 1
product: "Cursor IDE"
product_version_in_use: "3.13.25"
aligned_with: docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md
---

# T4B — Rules and AGENTS.md (plugin / workspace components)

Using `docs-research` + `research-protocol`.

## 1. Scope

- **Question / goal:** Deep dive on **Rules** and **AGENTS.md** as Cursor plugin/workspace components: frontmatter (`description`, `alwaysApply`, `globs`), project/user/team rules, how rules attach vs skills, token/context implications if documented, testing/validation if documented, composition with plugins.
- **In scope:** Official Cursor docs (Wave 1); optional E0 path observations of local example rule files for *structure only*.
- **Out of scope:** Editing Toolbelt skills/rules product files; E2/E3 community rule packs; inventing token budgets or undocumented precedence; runtime E0 of Agent rule injection (not executed this pass).
- **Comprehension / research goal type:** adaptive (understand product contracts for later Toolbelt authoring).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch; WebSearch (`site:cursor.com/docs`); Read (local paths); Shell (path listing); prior D0 note |
| Corpora / URLs searched | See §9; `https://cursor.com/llms.txt` index |
| Queries (exact) | `site:cursor.com/docs AGENTS.md nested precedence`; follow links from rules / plugins / customize / skills / CLI / cloud-agent setup |
| What was *not* searched | Help Center deep pages beyond index awareness; forums; GitHub issues; Alexandria RAG; changelog archaeology; Extension API for rules; runtime Agent prompt dumps |
| Product pin | Cursor **3.13.25** in use (per campaign D0 / user); docs = live cursor.com (no tagged docs version found) → skew **unknown** |
| Provenance (PROV light) | Entity=Rules/AGENTS.md docs; Activity=T4B Wave 1 fetch+grade; Agent=gatherer-T4B; wasDerivedFrom=fetched URLs below |

**D0–D14 (docs-research) — condensed:**

| Step | Result |
|------|--------|
| D0 | Product Cursor IDE `in_use` 3.13.25; docs live URLs accessed 2026-07-29; version skew unknown |
| D1 | llms.txt lists `rules.md`, `plugins.md`, `customize-cursor.md`, `skills.md`, CLI/cloud pages |
| D2 | `rules.md` = how-to + explanation; `reference/plugins.md` = **reference** (higher for plugin rule format); `plugins.md` / `customize-cursor.md` = how-to/overview |
| D3 | No OpenAPI for rules; normative tables in rules + plugins reference treated as E1 contracts |
| D5 | Limitations: FAQ (when rules apply / Tab / Inline Edit); best-practice line limits — no dedicated “limitations” page |
| D7 | Waived (Wave 1 = official docs only) |
| D10–D13 | Docs as hypotheses; atoms extracted below; OpenAPI N/A; no executable rule-schema validator found in docs |
| D14 | Live docs, no pin — freshness risk noted as OPEN |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | systematic (Wave 1 URL list) + hybrid follow-links for AGENTS.md |
| Why this mode | Mission mandated official URLs + AGENTS.md semantics search |
| Scope boundary | Official docs + optional E0 structure of `d:\Toolbelt\rules\*.mdc` and create-plugin quality-gate rule text |

## 4. Findings

### 4.1 Four rule surfaces (workspace / account)

- `CLAIM` [E1] Cursor documents **four** rule types: Project Rules (`.cursor/rules`), User Rules (global), Team Rules (dashboard; Team/Enterprise), and **AGENTS.md** (markdown alternative to `.cursor/rules`). [E1: Rules — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] Applied rule contents are included **at the start of the model context**; rules supply persistent prompt-level guidance because models do not retain memory between completions. [E1: Rules — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] Rules **do not** impact Cursor Tab or other AI features (FAQ). User Rules apply to Agent (Chat) only — **not** Inline Edit (Cmd/Ctrl+K). [E1: Rules FAQ — https://cursor.com/docs/rules.md — accessed 2026-07-29]

### 4.2 Project rules — path, extension, frontmatter

- `CLAIM` [E1] Project rules live in `.cursor/rules` as **`.mdc`** files (version-controlled); folders allowed; plain **`.md` in `.cursor/rules` is ignored** because it lacks frontmatter for `description`, `globs`, and `alwaysApply` — use AGENTS.md for plain markdown. [E1: Rules — Project rules — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] UI rule types map to frontmatter: Always Apply / Apply Intelligently / Apply to Specific Files / Apply Manually (`@`-mention). [E1: Rules — Rule anatomy — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] Under-the-hood frontmatter interaction table:

  | `alwaysApply` | `description` | `globs` | Behavior |
  |---------------|---------------|---------|----------|
  | `true` | — | — | Always included; globs and description ignored |
  | `false` | — | provided | Auto-attached when matching file in context |
  | `false` | provided | omitted | Agent may pull in when relevant from description |
  | `false` | omitted | omitted | Only via `@`-mention |

  [E1: Rules — Rule anatomy — https://cursor.com/docs/rules.md — accessed 2026-07-29]

- `CLAIM` [E1] `globs` may be comma-separated patterns (docs examples: `docs/**/*.md, docs/**/*.mdx`); table of glob examples includes `*`, `**`, `**/*.ts`, etc. [E1: Rules — Glob pattern examples — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] Creation paths: `/create-rule` in Agent; or Customize → Rules → Add Rule. [E1: Rules — Creating a rule — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] Best practices include keep rules under **500 lines**, split into composable rules, prefer `@` file references over copying code. [E1: Rules — Best practices — https://cursor.com/docs/rules.md — accessed 2026-07-29]

### 4.3 Team Rules and User Rules

- `CLAIM` [E1] Team Rules: free-form text (not Project Rules folder structure); optional **glob** for file-scoped application; without glob, apply to every conversation; managed in dashboard with draft vs enable, and **Enforce** (cannot be disabled in Customize). [E1: Rules — Team Rules — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] Precedence among layered rule sources: **Team Rules → Project Rules → User Rules**; all applicable rules merged; earlier sources win on conflict. [E1: Rules — Precedence — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] User Rules: global preferences in Customize → Rules; used by Agent (Chat). [E1: Rules — User Rules — https://cursor.com/docs/rules.md — accessed 2026-07-29]

### 4.4 AGENTS.md

- `CLAIM` [E1] `AGENTS.md` is plain markdown **without** metadata/complex configuration; place in project root as a simple alternative to `.cursor/rules`. [E1: Rules — AGENTS.md — https://cursor.com/docs/rules.md#agentsmd — accessed 2026-07-29]
- `CLAIM` [E1] Cursor supports `AGENTS.md` in the **project root and subdirectories**. Nested files apply when working with files in that directory or its children; instructions are **combined with parents**, with **more specific instructions taking precedence**. [E1: Rules — Nested AGENTS.md — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] Cloud agents read `AGENTS.md`; docs recommend a dedicated section (e.g. `Cursor Cloud specific instructions`) and link back to rules `#agentsmd`. [E1: Cloud agent setup — https://cursor.com/docs/cloud-agent/setup.md — accessed 2026-07-29]
- `CLAIM` [E1] CLI agent supports the same rules system; also reads **`AGENTS.md` and `CLAUDE.md` at the project root** (if present) and applies them as rules alongside `.cursor/rules`. [E1: CLI using — https://cursor.com/docs/cli/using.md — accessed 2026-07-29]
- `GAP` Precedence of `AGENTS.md` vs Team / Project / User Rules when guidance conflicts. Searched: rules.md precedence section, AGENTS.md section, customize-cursor.md, plugins.md, WebSearch `site:cursor.com/docs AGENTS.md nested precedence`. Result: nested AGENTS specificity documented; **cross-type merge order with Team/Project/User not stated**.
- `GAP` Whether nested `AGENTS.md` / `CLAUDE.md` apply in CLI the same as editor (CLI text only names root `AGENTS.md` and `CLAUDE.md`). Searched: cli/using.md. Result: root only mentioned for CLI; nested semantics only on rules.md.

### 4.5 Plugin composition — Rules as a plugin component

- `CLAIM` [E1] Plugins package **Rules** among Rules, Skills, Agents, Commands, MCP Servers, Hooks. [E1: Plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Default discovery: `rules/` — all **`.md`, `.mdc`, or `.markdown`** files; manifest optional field `rules` (string or array) **replaces** folder discovery when set. [E1: Plugins reference — Component discovery — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Plugin Rules format: `.mdc` with YAML frontmatter fields `description` (string), `alwaysApply` (boolean), `globs` (string **or array**); full behavior deferred to Rules docs. [E1: Plugins reference — Rules format — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Submission checklist requires rules (and skills/agents/commands) to have proper frontmatter metadata; local test via `~/.cursor/plugins/local/<plugin>` then restart/reload. [E1: Plugins reference — Submitting; Plugins — Test plugins locally — https://cursor.com/docs/reference/plugins.md , https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Customize: manage rules/skills; toggle rules between **Always**, **Agent Decides**, and **Manual**; skills appear under Agent Decides and can be invoked with `/skill-name`. [E1: Plugins — Rules and skills; Customize — https://cursor.com/docs/plugins.md , https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29]
- `GAP` Whether plugins may ship or discover `AGENTS.md` as a first-class plugin component. Searched: plugins.md, reference/plugins.md component tables. Result: **AGENTS.md not listed** as a plugin component (only Rules under `rules/`).

### 4.6 Rules vs Skills (attachment / context)

- `CLAIM` [E1] Skills are specialized capabilities in `SKILL.md`; agent sees available skills and decides relevance; also `/skill-name`; described as **progressive** (load resources on demand) for efficient context. [E1: Skills — https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `CLAIM` [E1] Skill frontmatter: required `name`, `description`; optional `paths` (globs; legacy `globs` accepted), `disable-model-invocation`, `metadata`. [E1: Skills — Frontmatter — https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `CLAIM` [E1] `/migrate-to-skills` converts **dynamic** rules (`alwaysApply: false`/undefined and **no** `globs`) to skills; rules with `alwaysApply: true` or specific `globs` are **not** migrated; User Rules not migrated. [E1: Skills — Migrating rules — https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `INFERENCE` [E4] Rules and skills are complementary attachment models: rules emphasize always/glob/manual injection into prompt start; skills emphasize agent-selected / progressive loading. Premises: (1) rules “included at the start of the model context” [E1 rules]; (2) skills “Progressive” / on-demand [E1 skills]; (3) migration excludes always/glob rules [E1 skills].

### 4.7 Token / context implications (documented only)

- `CLAIM` [E1] Applied rules consume prompt context by inclusion at context start; soft guidance: keep under 500 lines; prefer references over inlining. [E1: Rules — How rules work; Best practices — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] Skills docs claim progressive loading keeps context usage efficient. [E1: Skills — Progressive — https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `GAP` Numeric token budgets, truncation policy, or hard caps for rules / AGENTS.md / plugin rule bundles. Searched: rules.md, skills.md, plugins.md, reference/plugins.md, customize-cursor.md. Result: **not found**.

### 4.8 Testing / validation (documented only)

- `CLAIM` [E1] Local plugin validation path: copy/symlink to `~/.cursor/plugins/local`, reload, verify components (including rules) load; submission checklist includes “Plugin has been tested locally” and frontmatter/path checks. [E1: Plugins — Test plugins locally; reference submission checklist — accessed 2026-07-29]
- `CLAIM` [E1] FAQ troubleshooting: check rule type; Ensure description for Apply Intelligently; ensure glob matches for file-scoped rules. [E1: Rules FAQ — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `GAP` Automated schema validator, CLI lint, or CI checker for `.mdc` / AGENTS.md specifically. Searched: same official set. Result: **not found** (manual/local verify only).

### 4.9 Optional E0 — local structure (not product law)

- `FACT` [E0] `d:\Toolbelt\rules\` contains four `.mdc` files: `draft-is-not-sot.mdc`, `research-before-write.mdc`, `research-protocol-grades.mdc`, `research-skill-coexistence.mdc` (path listing 2026-07-29). [E0: path=`d:\Toolbelt\rules\` — 2026-07-29]
- `FACT` [E0] Example `draft-is-not-sot.mdc` uses YAML frontmatter `description` + `alwaysApply: true` then markdown body — consistent with documented Always Apply shape. [E0: path=`d:\Toolbelt\rules\draft-is-not-sot.mdc` — 2026-07-29]
- `FACT` [E0] create-plugin quality-gate rule at cache path uses `description` + `alwaysApply: true` and instructs YAML frontmatter for rules/skills/agents/commands. [E0: path=`C:\Users\Jonyc\.cursor\plugins\cache\cursor-public\create-plugin\45c66fde1f1681a902a30d1ae8bca1cc64465d6e\rules\plugin-quality-gates.mdc` — 2026-07-29]
- `INFERENCE` [E4] Local examples illustrate frontmatter shape only; they do **not** corroborate Cursor runtime attachment. Premises: E0 file reads; E1 docs remain authority for behavior.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Plugin `rules/` accepts `.md` while project `.cursor/rules` ignores `.md` | open (docs conflict / dual surface) | E1 both pages — see Conflicts |
| H2 | AGENTS.md sits outside Team→Project→User precedence or merges as Project-like | open | GAP — not documented |
| H3 | alwaysApply/glob rules remain preferred for “always on” guidance; intelligent rules trend toward skills | open / soft | E1 migrate-to-skills + progressive skills |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Rule file extensions | Project rules: plain `.md` in `.cursor/rules` **ignored**; need `.mdc` [E1 rules.md] | Plugin discovery: `rules/` includes `.md`, `.mdc`, `.markdown` [E1 reference/plugins.md] | **OPEN** — different surfaces; do not collapse. Prefer citing both. Possibly plugin parser ≠ project rules system. |
| `alwaysApply: false` wording | Project table: intelligent / glob / manual matrix [E1 rules.md] | Plugin field text: if false, rule “available on request” [E1 reference/plugins.md] | Prefer **rules.md** matrix as fuller contract; plugin blurb may be incomplete. Mark plugin wording **partial**. |
| CLI AGENTS nesting | Nested AGENTS in editor [E1 rules.md] | CLI: root `AGENTS.md` + `CLAUDE.md` only mentioned [E1 cli/using.md] | **OPEN** — whether CLI loads nested AGENTS.md |

## 7. Gaps & OPEN

1. **GAP:** AGENTS.md vs Team / Project / User conflict precedence.
2. **GAP:** Plugin packaging of AGENTS.md (not a listed component).
3. **GAP:** Token budgets / truncation for rules and AGENTS.md.
4. **GAP:** Automated validation tooling for rules/AGENTS.md beyond manual local plugin test + FAQ checks.
5. **GAP / OPEN:** Project `.md` ignored vs plugin `rules/` `.md` accepted — intentional dual behavior?
6. **OPEN:** Docs version skew vs Cursor 3.13.25 (live docs, no tag).
7. **OPEN:** CLI nested AGENTS.md / CLAUDE.md behavior.
8. **Not searched (Wave 1):** Help Center `help/customization/rules.md`; Extension API; changelogs for AGENTS nesting ship date.

## 8. Implications (INFERENCE only — not design locks)

- `INFERENCE` [E4] For Toolbelt plugin rules, ship `.mdc` under `rules/` with explicit frontmatter (`description` / `alwaysApply` / `globs`) matching plugins reference + rules matrix; do not rely on bare `.md` for **project** `.cursor/rules`. Premises: E1 project ignore `.md`; E1 plugin discovers `.md` but checklist stresses frontmatter.
- `INFERENCE` [E4] Use AGENTS.md for simple/nested directory guidance; use Project/Plugin `.mdc` when Always/Glob/Manual control or team distribution via plugins is required. Premises: E1 AGENTS.md “simple alternative”; E1 plugin component = Rules not AGENTS.md.
- `INFERENCE` [E4] Prefer skills for large/on-demand workflows; keep always/glob rules short to limit always-on context. Premises: E1 500-line guidance; E1 skills progressive; E1 migration excludes always/glob rules.

## 9. Source list (deduped)

1. https://cursor.com/docs/rules.md — accessed 2026-07-29
2. https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29
3. https://cursor.com/docs/plugins.md — accessed 2026-07-29
4. https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29
5. https://cursor.com/docs/skills.md — accessed 2026-07-29 (rules↔skills attachment)
6. https://cursor.com/docs/cli/using.md — accessed 2026-07-29 (AGENTS.md / CLAUDE.md)
7. https://cursor.com/docs/cloud-agent/setup.md — accessed 2026-07-29 (AGENTS.md cloud section)
8. https://cursor.com/llms.txt — accessed 2026-07-29 (index)
9. E0: `d:\Toolbelt\rules\*.mdc` — observed 2026-07-29
10. E0: create-plugin `rules/plugin-quality-gates.mdc` (cache path above) — observed 2026-07-29
11. Campaign D0: `docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md` (version pin 3.13.25)

## Self-check

- [x] Method block present
- [x] Every FACT/CLAIM has support
- [x] INFERENCEs list premises
- [x] No invented citations/APIs/token numbers
- [x] Conflicts logged
- [x] `status: draft` — not SoT
