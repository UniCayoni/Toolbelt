---
title: "T4A — Cursor plugin manifest, marketplace, discovery, local install"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
authors: [t4a]
supersedes: null
---

# T4A — Cursor plugin packaging (manifest / marketplace / discovery)

**Using `docs-research` + `research-protocol`.**

Context pin: Cursor build **3.13.25** (E0 from Local AppData `package.json` per campaign D0 note). Live docs accessed 2026-07-29; docs↔build version skew **unknown**.

## 1. Scope

- **Question / goal:** Document how Cursor plugin packaging works — `.cursor-plugin/plugin.json`, `marketplace.json`, component discovery, variables, logos, submission/testing checklist, local install paths, and extension API `vscode.cursor.plugins.registerPath` — **only from official Cursor docs evidence** (plus light E0 local corroboration).
- **In scope:** Manifest schema fields as documented; multi-plugin marketplace manifest; automatic vs explicit component discovery; variables/logo rules; local `~/.cursor/plugins/local` test path; marketplace submit/security claims; Extension API plugin path registration; linked official hooks contract for `workspaceOpen` → `pluginPaths`.
- **Out of scope:** Redesigning Toolbelt skills; deep component formats for rules/skills/agents/commands/hooks/MCP (other Wave-1 gatherers); community/E3 guides; inventing undocumented fields.
- **Comprehension / research goal type:** reuse (packaging contract for later authoring) + adaptive (map docs to local Toolbelt layout).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch; WebSearch (site:cursor.com/docs); Shell/Python path-exists checks (E0); GitHub raw/API fetches for `cursor/plugin-template` |
| Corpora / URLs searched | See §9; primary: plugins overview, plugins reference, extension-api, customize-cursor, marketplace-security help, help/plugins, plugin-template repo, `https://cursor.com/llms.txt`, `https://cursor.com/docs/llms.txt`, `https://cursor.com/marketplace/publish` |
| Queries (exact) | WebFetch each primary URL listed in mission; WebSearch `site:cursor.com/docs plugins.registerPath workspaceOpen marketplace.json`; GitHub API `repos/cursor/plugin-template/contents/`; raw `README.md`, `marketplace.json`, `plugins/starter-simple/.cursor-plugin/plugin.json`, `docs/add-a-plugin.md` |
| What was *not* searched | Alexandria RAG; forums/Discord; non-Cursor blogs; VS Code Marketplace docs; Cursor source code / decompiled app; full hooks doc beyond `workspaceOpen`/`pluginPaths`; rules/skills/MCP deep pages (except as cited from plugins reference tables) |
| Provenance (optional PROV) | Entity=official Cursor docs + plugin-template + local Toolbelt plugin paths; Activity=T4A Wave-1 docs gather 2026-07-29; Agent=gatherer t4a / WebFetch+E0 |

**D0 (docs-research):** Product Cursor IDE `status: in_use`; build `3.13.25` [E0 via campaign D0]; docs = live untagged pages → treat as E1 hypotheses until E0.

**Diátaxis (light):** Plugins reference = **reference**; plugins.md / customize = **how-to + explanation**; extension-api = **reference**; marketplace-security = **explanation/FAQ**; plugin-template = **tutorial/starter** (official GitHub, not docs site).

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Docs-first Wave 1; optional E0 only to corroborate local install path + Toolbelt manifest shape |
| Scope boundary | Included: `d:\Toolbelt\.cursor-plugin\`, `~\.cursor\plugins\local\toolbelt\`; excluded: redesign of skills/rules content |

## 4. Findings

### 4.1 What a plugin is / contains

- `CLAIM` [E1] Plugins package rules, skills, agents, commands, MCP servers, and hooks into distributable bundles. [E1: Plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Customize page is the UI to install/manage plugins (and related components) at user / team / workspace scope. [E1: Customize Cursor — https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29]
- `CLAIM` [E1] Official marketplace plugins are Git repositories; community plugins also pointed to cursor.directory. [E1: Plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Help center: plugins work across Cursor desktop, web, and CLI. [E1: Help Plugins — https://cursor.com/help/customization/plugins.md — accessed 2026-07-29]

### 4.2 Plugin directory + `plugin.json`

- `CLAIM` [E1] A plugin directory has required `.cursor-plugin/plugin.json` plus optional component folders (`rules/`, `skills/`, `agents/`, `commands/`, `hooks/`, `mcp.json`, `assets/`, `scripts/`, `README.md`). [E1: Plugins reference — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] **Required** manifest field: `name` (string) — lowercase kebab-case (alphanumerics, hyphens, periods); must start and end alphanumeric. Examples: `my-plugin`, `prompts.chat`. [E1: Plugins reference — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] **Optional** manifest fields documented: `description`, `version`, `author` (`name` required, `email` optional), `homepage`, `repository`, `license`, `keywords`, `logo`, `rules`, `agents`, `skills`, `commands`, `hooks`, `mcpServers`, `variables`. [E1: Plugins reference — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Overview page: “The manifest only requires a `name` field. Components are discovered automatically from their default directories, or you can specify custom paths in the manifest.” [E1: Plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `FACT` [E0] Local Toolbelt plugin manifests exist at `d:\Toolbelt\.cursor-plugin\plugin.json` and `C:\Users\Jonyc\.cursor\plugins\local\toolbelt\.cursor-plugin\plugin.json` with `"name": "toolbelt"`, `version` `0.1.0`, author, license, keywords; no `marketplace.json` beside them. [E0: path exists + JSON read 2026-07-29]
- `FACT` [E0] Both Toolbelt plugin roots contain `rules/` and `skills/` (and `scripts/`); no `agents/`, `commands/`, `hooks/`, `assets/`, or root `mcp.json` observed. [E0: path-exists listing 2026-07-29]
- `GAP` Official plugins **reference** optional-field table does **not** list `displayName`, but official **plugin-template** `plugin.json` and docs use `"displayName"`. Searched: reference optional fields table; template README / starter-simple / add-a-plugin.md. Result: field present in template, absent from reference schema table. [E1 conflict — see §6]

### 4.3 Component discovery

- `CLAIM` [E1] When manifest does **not** specify explicit paths for a component type, parser uses automatic folder-based discovery: Skills=`skills/` (subdir + `SKILL.md`); Rules=`rules/` (`.md`/`.mdc`/`.markdown`); Agents=`agents/` (same); Commands=`commands/` (also `.txt`); Hooks=`hooks/hooks.json`; MCP=`mcp.json`; Root Skill=`SKILL.md` at plugin root only if no `skills/` dir and no manifest `skills` field. [E1: Plugins reference §Component discovery — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] If a manifest field **is** specified (e.g. `"skills": "./my-skills/"`), it **replaces** folder discovery for that component; default folder is not also scanned. [E1: Plugins reference — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Frontmatter requirements stated for rules (`description`, `alwaysApply`, `globs`), skills (`name`, `description`), agents (`name`, `description`), commands (`name`, `description`). [E1: Plugins reference — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `INFERENCE` [E4] Toolbelt’s `rules/` + `skills/` layout without explicit path fields in `plugin.json` is intended to rely on automatic discovery. Premises: (1) E1 discovery defaults above; (2) E0 Toolbelt manifest has no `rules`/`skills` path overrides.

### 4.4 Variables

- `CLAIM` [E1] `variables` is a JSON Schema declaring variable **names** (tokens, connection strings); plugin does **not** store secret values; users/admins set values in dashboard **Plugins → Configure**; substituted into `${VAR}` placeholders. [E1: Plugins reference §Variables — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Top level must be `{ "type": "object", "properties": { ... } }`. Accepted JSON Schema keywords limited to: `type`, `title`, `description`, `default`, `enum`, `const`, `properties`, `required`, `items`, and common length/numeric constraints. [E1: Plugins reference — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] In `mcp.json`, `${POSTGRES_URL}`-style placeholders are plugin variables (not shell `${env:...}`); plugin-managed MCP config is read-only in the dashboard. [E1: Plugins reference §MCP servers — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `GAP` Full enumeration of “common length/numeric constraints” not listed beyond that phrase. Searched: Variables section of plugins reference. Result: incomplete keyword list detail. [E1: Plugins reference — accessed 2026-07-29]

### 4.5 Logos

- `CLAIM` [E1] `logo` may be a relative path (e.g. `assets/logo.svg`) or absolute `http(s)://` URL; preferred: commit logo and use relative path. Relative paths resolve to `raw.githubusercontent.com` URLs based on repository and commit SHA. [E1: Plugins reference §Logos / optional fields — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Example resolution pattern: `assets/logo.svg` in repo `acme/plugins` at commit `abc123` → `https://raw.githubusercontent.com/acme/plugins/abc123/my-plugin/assets/logo.svg`. [E1: Plugins reference — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `GAP` Docs do not specify required image format/size beyond examples using SVG. Searched: Logos section. Result: format/size requirements not stated.

### 4.6 Multi-plugin `marketplace.json`

- `CLAIM` [E1] Multi-plugin repos use `.cursor-plugin/marketplace.json` at repository root. [E1: Plugins reference §Multi-plugin repositories; also Plugins overview — accessed 2026-07-29]
- `CLAIM` [E1] Marketplace required fields: `name` (kebab-case), `owner` (`name` required, `email` optional), `plugins` array (max 500). Optional `metadata`: `description`, `version`, `pluginRoot` (prefix for all plugin sources). [E1: Plugins reference — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Plugin entry fields include: required `name`; `source` (string path or object with `path` and options); plus description/version/author/homepage/repository/license/keywords/logo/category/tags; component path overrides; `hooks`; `mcpServers`; `variables` (prefer `plugin.json`; if both set, **manifest values take precedence**). [E1: Plugins reference — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Resolution: for `"source": "my-plugin"`, parser looks for `my-plugin/.cursor-plugin/plugin.json`; merges marketplace entry with per-plugin manifest (**marketplace/manifest entry values take precedence**); then component discovery inside that plugin directory. [E1: Plugins reference §How resolution works — accessed 2026-07-29]
- `FACT` [E1/E0-template] Official `cursor/plugin-template` ships multi-plugin layout: root `.cursor-plugin/marketplace.json` with `plugins` entries `source: "./plugins/starter-simple"` and `"./plugins/starter-advanced"`; no root single-plugin `plugin.json` (404 on that path). [E1: https://raw.githubusercontent.com/cursor/plugin-template/main/.cursor-plugin/marketplace.json — accessed 2026-07-29; GitHub API listing]
- `GAP` Docs say `source` may be “object with `path` and options” but do **not** enumerate those options. Searched: Plugin entry fields table. Result: options unspecified. [E1: Plugins reference — accessed 2026-07-29]

### 4.7 Local install / how to test

- `CLAIM` [E1] Before publish, load plugin from `~/.cursor/plugins/local`: create `~/.cursor/plugins/local/my-plugin`, copy files so `.cursor-plugin/plugin.json` is at plugin root, restart Cursor or **Developer: Reload Window**, verify components load. Symlink supported: `ln -s /path/to/my-plugin ~/.cursor/plugins/local/my-plugin`. [E1: Plugins — https://cursor.com/docs/plugins.md §Test plugins locally — accessed 2026-07-29]
- `FACT` [E0] On this machine, `C:\Users\Jonyc\.cursor\plugins\local` exists with directories `toolbelt` and `grey-matter` (not symlinks). [E0: path listing 2026-07-29]
- `CLAIM` [E1] Submission checklist (reference): valid `plugin.json`; unique kebab-case `name`; clear `description`; frontmatter on components; logo relative if provided; `README.md`; variables schema matches `${VAR}` usages; paths relative/valid (no `..`, no absolute paths); tested locally; multi-plugin needs root `marketplace.json` with unique names. [E1: Plugins reference §Submission checklist — accessed 2026-07-29]
- `CLAIM` [E1] Plugin-template adds validation step `node scripts/validate-template.mjs` and alternate contact note (Slack or `kniparko@anysphere.com`) in its README checklist. [E1: https://raw.githubusercontent.com/cursor/plugin-template/main/README.md — accessed 2026-07-29]
- `GAP` Official docs do not describe an automated IDE “plugin validator” UI beyond Reload Window + manual verify; template’s validate script is repo-local, not documented on cursor.com/docs. Searched: plugins.md Test section; reference checklist. Result: no docs-site validator command.

### 4.8 Marketplace publish + security

- `CLAIM` [E1] Submit at https://cursor.com/marketplace/publish with repository link; plugins reviewed by Cursor team; public Git repo required. [E1: Plugins reference §Submitting a plugin; Plugins overview — accessed 2026-07-29]
- `CLAIM` [E1] Every marketplace plugin manually reviewed before listing; updates also manually reviewed (not auto-updated from source); must be open source; no binaries shipped (largely markdown + supporting files); respect MCP allowlist/blocklist. [E1: Marketplace security — https://cursor.com/help/security-and-privacy/marketplace-security.md — accessed 2026-07-29]
- `CLAIM` [E1] Report issues to security-reports@cursor.com; authors expected to maintain plugins or risk delisting. [E1: Marketplace security — accessed 2026-07-29]
- `GAP` WebFetch of https://cursor.com/marketplace/publish returned near-empty page body (title only). Searched: WebFetch 2026-07-29. Result: form fields / publish UX not recoverable from fetch → treat publish UI details as insufficient_evidence.
- `CLAIM` [E1] Team marketplaces (Teams/Enterprise): Dashboard → Plugins; install modes Default Off / Default On / Required; Auto Refresh ≤ once / 10 minutes with GitHub App; new plugins need re-import. [E1: Plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]

### 4.9 Extension API `vscode.cursor.plugins.registerPath`

- `CLAIM` [E1] Cursor exposes `vscode.cursor.plugins.registerPath(path: string): void` and `unregisterPath(path: string): void` under `vscode.cursor` for extensions. [E1: Extension API — https://cursor.com/docs/extension-api — accessed 2026-07-29]
- `CLAIM` [E1] `registerPath` registers a directory as a plugin **source**; Cursor discovers and loads any valid plugins in that directory; intended so users need not copy to `~/.cursor/plugins/local/`. [E1: Extension API — accessed 2026-07-29]
- `CLAIM` [E1] Parameter: absolute filesystem path to a directory **containing** plugins. Examples: extension-bundled `cursor-plugins/` folder; workspace `.cursor-plugins` path. [E1: Extension API — accessed 2026-07-29]
- `CLAIM` [E1] For paths registered this way, `.cursor-plugin/plugin.json` is **optional**; without it, automatic folder-based discovery still picks up `rules/`, `skills/`, `agents/`, `commands/`, `mcp.json`, `hooks/hooks.json`. [E1: Extension API — accessed 2026-07-29]
- `OPEN` Whether `registerPath` expects a parent directory of many plugins vs a single plugin root is illustrated both ways in prose (“directory containing plugins” vs example tree that looks like one plugin). Follow-up: E0 runtime smoke or clearer docs. [E1: Extension API wording — accessed 2026-07-29]

### 4.10 `workspaceOpen` → plugin paths (linked official docs)

- `CLAIM` [E1] Plugins overview: a `workspaceOpen` hook can return plugin paths to load on workspace open. [E1: Plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Hooks reference: `workspaceOpen` output may include `pluginPaths: string[]` — absolute paths to plugin directories; fires on workspace open and folder change; skipped with zero folders; desktop + CLI; not for cloud agents. [E1: Hooks — https://cursor.com/docs/hooks.md — accessed 2026-07-29]

### 4.11 llms.txt indexes

- `FACT` [E1] `https://cursor.com/llms.txt` resolves and lists docs including `/docs/plugins.md`, `/docs/customize-cursor.md`, and help `/help/customization/plugins.md` (extension-api / reference/plugins not enumerated as separate bullets in the fetched customizing section, but sitemap links appear on fetched pages). [E1: https://cursor.com/llms.txt — accessed 2026-07-29]
- `FACT` [E1] `https://cursor.com/docs/llms.txt` returned **404 Not Found**. [E1: WebFetch status 404 — accessed 2026-07-29]

## 5. Hypothesis log (optional)

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Official docs fully specify `plugin.json` optional fields used by authors | revised | Template uses `displayName` not in reference table (§6 C1) |
| H2 | Local install path `~/.cursor/plugins/local/<name>` exists and is used on this host | confirmed | E0 listing |
| H3 | Manifest required for all load paths | rejected / conflict | Creating-plugins docs require manifest; extension-api says optional for registerPath (§6 C2) |
| H4 | Publish page documents form fields | open / weak | Fetch empty (§4.8 GAP) |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| C1 `displayName` in `plugin.json` | Plugins reference optional fields table — **no** `displayName` [E1: reference] | plugin-template `starter-simple` + README/add-a-plugin instruct `displayName` [E1: GitHub template] | Prefer reference as normative schema until Cursor documents `displayName`; treat template field as **undocumented-in-reference** / possible UI-only. Status: **OPEN** (do not invent semantics). |
| C2 Manifest required? | Plugins.md / reference: every plugin requires `.cursor-plugin/plugin.json` | Extension API: manifest optional; folder discovery still works for registered paths | Prefer: **marketplace/local plugin packages** require manifest; **extension-injected paths** may omit. Document both; no silent merge. Winner: unresolved for single SoT sentence — leave OPEN for integrator. |
| C3 Submit contact | Docs: cursor.com/marketplace/publish | Template README: Slack or kniparko@anysphere.com | Prefer docs URL as primary; template contact may be alternate/legacy. Status: **OPEN**. |
| C4 Precedence wording | “manifest values take precedence” when merging marketplace entry with per-plugin `plugin.json` | Same page also says prefer `plugin.json` for variables | Read carefully: marketplace **entry** overrides per-plugin file when both set; “prefer plugin.json” is authoring guidance. No contradiction if “manifest” means marketplace entry. Status: noted for careful reading. |

## 7. Gaps & OPEN

- `GAP` Publish page body / form fields not recoverable via WebFetch (empty shell).
- `GAP` `displayName` semantics not in plugins reference schema table.
- `GAP` `source` object “options” for marketplace entries unspecified.
- `GAP` Logo format/size requirements unspecified.
- `GAP` Complete JSON Schema keyword set for `variables` (“common length/numeric constraints”) underspecified.
- `GAP` `https://cursor.com/docs/llms.txt` 404.
- `GAP` Docs↔Cursor 3.13.25 behavior skew unknown (no docs version pin).
- `GAP` No docs-site automated local validator; only Reload Window + manual check (+ template script, not on docs site).
- `OPEN` Exact directory shape expected by `registerPath` (parent-of-plugins vs single plugin root).
- `OPEN` Whether Toolbelt should add `marketplace.json` (multi-plugin) — implication only; no design lock (out of scope).
- `OPEN` Windows symlink guidance: docs show Unix `ln -s` only; Windows equivalent not documented on fetched pages.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Authors writing marketplace/local plugins should treat plugins **reference** as the primary field contract and treat template-only fields (e.g. `displayName`) as non-normative until reference lists them. Premises: §4.2 required/optional tables; §6 C1.
- `INFERENCE` [E4] Local iteration path for Toolbelt-class plugins is `~\.cursor\plugins\local\<name>` + Reload Window; Extension `registerPath` and `workspaceOpen.pluginPaths` are alternate injection channels for extensions/hooks. Premises: §4.7–4.10.
- `INFERENCE` [E4] Multi-plugin distribution needs root `marketplace.json`; single-plugin repos can omit it (template README states this explicitly). Premises: template README; reference multi-plugin section.
- `INFERENCE` [E4] No design locks for Toolbelt skill redesign from this note (`status: draft`). Premises: PROTOCOL draft≠SoT; mission out-of-scope.

## 9. Source list (deduped)

1. https://cursor.com/docs/plugins.md — accessed 2026-07-29
2. https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29
3. https://cursor.com/docs/extension-api — accessed 2026-07-29
4. https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29
5. https://cursor.com/docs/hooks.md — accessed 2026-07-29 (workspaceOpen / pluginPaths only)
6. https://cursor.com/help/customization/plugins.md — accessed 2026-07-29
7. https://cursor.com/help/security-and-privacy/marketplace-security.md — accessed 2026-07-29
8. https://cursor.com/marketplace/publish — accessed 2026-07-29 (fetch body insufficient)
9. https://cursor.com/llms.txt — accessed 2026-07-29
10. https://cursor.com/docs/llms.txt — accessed 2026-07-29 (**404**)
11. https://github.com/cursor/plugin-template — accessed 2026-07-29
12. https://raw.githubusercontent.com/cursor/plugin-template/main/README.md — accessed 2026-07-29
13. https://raw.githubusercontent.com/cursor/plugin-template/main/.cursor-plugin/marketplace.json — accessed 2026-07-29
14. https://raw.githubusercontent.com/cursor/plugin-template/main/plugins/starter-simple/.cursor-plugin/plugin.json — accessed 2026-07-29
15. https://raw.githubusercontent.com/cursor/plugin-template/main/docs/add-a-plugin.md — accessed 2026-07-29
16. E0: `d:\Toolbelt\.cursor-plugin\plugin.json`; `C:\Users\Jonyc\.cursor\plugins\local\toolbelt\`; `C:\Users\Jonyc\.cursor\plugins\local\` — observed 2026-07-29
17. Campaign D0: `docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md` (build pin 3.13.25)
