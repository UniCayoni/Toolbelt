---
title: "T4G: MCP servers in Cursor plugins (Wave 1 — official docs)"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-T4G]
supersedes: null
gatherer: T4G
wave: 1
product: "Cursor IDE (hosted)"
installed_version: "3.13.25 (campaign D0 pin)"
docs_access_date: 2026-07-29
aligned_with: docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md
---

# T4G — MCP servers in Cursor plugins

Using `docs-research` + `research-protocol`.

## 1. Scope

- **Question / goal:** Deep dive on how MCP servers are packaged, configured, scoped, consumed by agents, tested, and secured **in Cursor plugins** and related Cursor MCP surfaces (Wave 1: official Cursor docs only).
- **In scope:** Plugin `mcp.json` layout; `plugin.json` / marketplace `mcpServers` overrides; plugin `${VAR}` vs user-config `${env:…}` interpolation; extension API `registerServer`; user / team / workspace MCP scopes; agent consumption; documented testing/validation; security / allowlists / marketplace vetting.
- **Out of scope:** Inventing full MCP protocol behavior beyond what Cursor docs cite; E2/E3 community write-ups; Wave 2 Alexandria/GitHub; implementation against local plugin code (E0 deferred unless noted).
- **Comprehension type:** reuse / adaptive (authoring Toolbelt plugin MCP packaging).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch; WebSearch (URL discovery only); Read of Toolbelt `d0-cursor-plugins-identity.md` for version pin |
| Corpora / URLs searched | Listed mission URLs + docs linked from those pages (run-modes, install-links, marketplace-security, CLI MCP). SDK TypeScript MCP precedence fetched via search hit (Cursor docs). |
| Queries (exact) | Mission URL list; `site:cursor.com/docs extension-api mcp registerServer` |
| What was *not* searched | Alexandria RAG; GitHub issues/forums (E3); modelcontextprotocol.io full protocol dump (only Cursor-cited links noted); local Cursor binary reverse-engineering |
| Provenance (optional PROV) | Entity=Cursor public docs pages; Activity=WebFetch 2026-07-29; Agent=gatherer-T4G; wasDerivedFrom=campaign D0 note for version pin |

**D0 pin (campaign):** Cursor `in_use` build **3.13.25** [E0 via D0 note]. Docs = live `cursor.com/docs` (no release-tag pin) → skew **unknown**.

**Diátaxis (D2):** Primary trust for API shape = **reference** (`reference/plugins.md`, `extension-api`). How-to/explanation: `mcp.md`, `plugins.md`, `customize-cursor.md`.

**OpenAPI / schema tools (D12):** **N/A** (prose/HTML product docs).

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | systematic (mission URL list) + as-needed follow of in-doc links |
| Why this mode | Wave 1 requires official Cursor docs; follow-links only when primary pages cite them for MCP/plugin packaging |
| Scope boundary | Cursor packaging & product behavior; not upstream MCP spec authorship |

## 4. Findings

### 4.1 Plugin packaging: `mcp.json` + discovery

- `CLAIM` [E1] Plugins may include MCP servers as a first-class component alongside rules, skills, agents, commands, and hooks. [E1: Plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Default discovery: MCP config file at plugin root `mcp.json` is parsed for server entries when the manifest does not override. [E1: Plugins reference — Component discovery — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Plugin MCP config file should contain server entries under a top-level `mcpServers` key (example: named server with `command` / `args` / `env`). [E1: Plugins reference — MCP servers — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Example plugin tree places `mcp.json` at plugin root (sibling of `.cursor-plugin/`, `rules/`, `skills/`, etc.). [E1: Plugins reference — Plugin structure — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]

### 4.2 `plugin.json` / marketplace `mcpServers` overrides

- `CLAIM` [E1] Optional manifest field `mcpServers` type is **string, object, or array**: “Path to MCP config file, inline MCP server config, or an array of either. **Overrides default `mcp.json` discovery.**” [E1: Plugins reference — Optional fields — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] “You only need to specify the `mcpServers` field in `plugin.json` if using a custom path or inline config.” [E1: Plugins reference — MCP servers — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] If a manifest field **is** specified for a component type, it **replaces** folder discovery for that component; the default folder is not also scanned. [E1: Plugins reference — Component discovery — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Marketplace plugin entries also support `mcpServers` as string or object (path or inline). [E1: Plugins reference — Plugin entry fields — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `GAP` Marketplace entry table lists `mcpServers` as **string or object** only (no explicit **array**), while `plugin.json` optional fields allow **array**. Searched: plugins reference plugin entry fields vs optional fields. Result: possible schema asymmetry undocumented; do not assume array works on marketplace entries without corroboration.

### 4.3 Variables: plugin `${VAR}` vs user `mcp.json` `${env:…}` / path tokens

- `CLAIM` [E1] Plugin `variables` in `plugin.json` is a JSON Schema declaring variable **names** (tokens, connection strings). The plugin does **not** store secret values; users/admins set values in the dashboard (**Plugins** → **Configure**). Substituted into `${VAR}` placeholders. [E1: Plugins reference — Optional fields / Variables — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Docs explicitly contrast: in plugin `mcp.json`, `${POSTGRES_URL}` is a **plugin variable** placeholder (**not** shell `${env:…}`). Declare under `variables`, put only the placeholder in plugin config, set value in dashboard. “Plugin-managed MCP config is **read-only** in the dashboard.” [E1: Plugins reference — MCP servers — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Variables schema top level must be `{ "type": "object", "properties": { … } }`. Accepted keywords limited to a fixed set (`type`, `title`, `description`, `default`, `enum`, `const`, `properties`, `required`, `items`, and common length/numeric constraints). [E1: Plugins reference — Variables — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Submission checklist: if using `variables`, schema must be valid and every `${VAR}` in `mcp.json` must have a matching property. [E1: Plugins reference — Submission checklist — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] For **user/project** `mcp.json` (non-plugin), Cursor resolves interpolation in fields `command`, `args`, `env`, `url`, and `headers` with: `${env:NAME}`, `${userHome}`, `${workspaceFolder}`, `${workspaceFolderBasename}`, `${pathSeparator}` / `${/}`. [E1: Model Context Protocol (MCP) — Config interpolation — https://cursor.com/docs/mcp.md — accessed 2026-07-29]
- `CLAIM` [E1] Static OAuth `auth` values on remote servers also support the same interpolation (example `${env:MCP_CLIENT_ID}`). [E1: MCP — Combining with config interpolation — https://cursor.com/docs/mcp.md — accessed 2026-07-29]
- `CLAIM` [E1] STDIO `envFile` is documented for user/project STDIO servers; remote HTTP/SSE do not support `envFile` — use interpolation with shell/system env instead. [E1: MCP — STDIO server configuration — https://cursor.com/docs/mcp.md — accessed 2026-07-29]
- `GAP` Whether plugin `mcp.json` may also use `${env:NAME}`, `${workspaceFolder}`, etc. Searched: plugins reference Variables + MCP servers sections; mcp.md config interpolation. Result: plugins docs teach `${VAR}` dashboard vars and warn against shell `${env:…}` as the plugin-variable mechanism; **no explicit statement** that `${env:…}` / workspace tokens are forbidden or allowed inside plugin MCP configs.

### 4.4 User / project `mcp.json` layout (non-plugin baseline)

- `CLAIM` [E1] Custom servers use `mcpServers` map with STDIO (`command` / `args` / `env`) or remote (`url` / `headers`) shapes; static OAuth via `auth` (`CLIENT_ID` required; `CLIENT_SECRET` / `scopes` optional). [E1: MCP — Using mcp.json / Static OAuth — https://cursor.com/docs/mcp.md — accessed 2026-07-29]
- `CLAIM` [E1] Project config: `.cursor/mcp.json`; global: `~/.cursor/mcp.json`. [E1: MCP — Configuration locations — https://cursor.com/docs/mcp.md — accessed 2026-07-29]
- `CLAIM` [E1] Transports documented for Cursor: **stdio**, **SSE**, **Streamable HTTP** (with execution/auth columns). [E1: MCP — How it works — https://cursor.com/docs/mcp.md — accessed 2026-07-29]
- `OPEN` STDIO field table lists **`type` Required** with value `"stdio"`, but introductory STDIO JSON examples omit `type`. Conflict within mcp.md — unresolved which is authoritative without E0. Prefer recording both; do not lock schema on either alone. [E1: MCP — STDIO server configuration vs examples — https://cursor.com/docs/mcp.md — accessed 2026-07-29]

### 4.5 Extension API: `registerServer`

- `CLAIM` [E1] Programmatic registration without editing `mcp.json`: `vscode.cursor.mcp.registerServer(config)` and `unregisterServer(serverName)`. [E1: Extension API — https://cursor.com/docs/extension-api — accessed 2026-07-29]; also pointed from [E1: MCP — Using the Extension API — https://cursor.com/docs/mcp.md — accessed 2026-07-29]
- `CLAIM` [E1] Config union: `StdioServerConfig` (`name` + `server.command` / `args` / `env`) or `RemoteServerConfig` (`name` + `server.url` / optional `headers`). Docs state support for HTTP(S) (SSE/streamable HTTP) and local stdio. [E1: Extension API — MCP servers — https://cursor.com/docs/extension-api — accessed 2026-07-29]
- `CLAIM` [E1] Related: `vscode.cursor.plugins.registerPath` / `unregisterPath` can register a directory; without a manifest, automatic discovery still picks up `mcp.json` among default locations. [E1: Extension API — Plugin paths — https://cursor.com/docs/extension-api — accessed 2026-07-29]
- `GAP` Extension API docs do not document interaction with plugin `${VAR}` dashboard substitution, OAuth `auth` object, `envFile`, or allowlist policy for API-registered servers. Searched: extension-api page. Result: not found.

### 4.6 Scopes: user / workspace / team / enterprise

- `CLAIM` [E1] Customize page manages plugins, MCP servers, rules, skills at **user, team, or workspace** level; filter by scope to see what is installed. [E1: Customize Cursor — https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29]; [E1: Plugins — Managing installed plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Plugins can be scoped to a **project** or installed at the **user** level. [E1: Plugins — Installing plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Team-distributed MCP servers appear in Customize alongside personal and workspace MCP servers; install/configure for Agent Window, IDE, and CLI. [E1: MCP — One-click installation — https://cursor.com/docs/mcp.md — accessed 2026-07-29]; [E1: Plugins — Default team marketplace / Where developers find team marketplaces — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Team MCP distribution: Dashboard → Integrations & MCP; Cloud Agents get shared Team MCP; **Add to Team Marketplace** links to Default team marketplace without interrupting Cloud Agent access. Linking does **not** install/enable for everyone — Marketplace Access + installation modes still apply; teammates may need to authenticate. [E1: MCP — Team MCP distribution — https://cursor.com/docs/mcp.md — accessed 2026-07-29]; [E1: Plugins — Migrate existing Team MCPs — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Plugin installation modes: **Default Off**, **Default On**, **Required**. [E1: Plugins — Plugin installation modes — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Warning: removing a linked MCP plugin from marketplace or deleting marketplace **can delete** the Team MCP server for local users and Cloud Agents. [E1: Plugins — Migrate existing Team MCPs — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Enterprise: MCP **Allowlist** (command patterns for stdio; URL patterns for remote; optional tool allowlists) approves configuration but does **not** distribute/install. Separate network controls and User MCP extensions / denylist. [E1: MCP — Enterprise admin controls — https://cursor.com/docs/mcp.md — accessed 2026-07-29]
- `GAP` Exact runtime precedence when the **same server name** exists in plugin MCP + `.cursor/mcp.json` + `~/.cursor/mcp.json` + extension API + team marketplace for the **IDE Agent** (not SDK). Searched: mcp.md, plugins.md, customize-cursor.md. Result: IDE docs describe locations/scopes but not a single first-match-wins table for IDE (SDK docs do — see §4.7).

### 4.7 How agents consume MCP

- `CLAIM` [E1] In chat, Cursor automatically uses MCP tools listed under **Available Tools** when relevant, including Plan Mode; users can ask by name; enable/disable from Customize. [E1: MCP — Using MCP in chat — https://cursor.com/docs/mcp.md — accessed 2026-07-29]
- `CLAIM` [E1] Default: approval before MCP tool use; arguments inspectable. MCP follows the same **Run Modes** as terminal commands (e.g. Auto-review: allowlisted MCP tools run immediately; else classifier). [E1: MCP — Tool approval — https://cursor.com/docs/mcp.md — accessed 2026-07-29]; [E1: Run Modes — https://cursor.com/docs/agent/security/run-modes.md — accessed 2026-07-29]
- `CLAIM` [E1] Protocol capabilities Cursor lists as supported: Tools, Prompts, Resources, Roots, Elicitation, Apps (extension). Cursor cites MCP Apps extension overview. [E1: MCP — Protocol and extension support / MCP apps — https://cursor.com/docs/mcp.md — accessed 2026-07-29] — **packaging grade E1 Cursor**; linked intro/Apps pages are **upstream MCP protocol** (treat protocol detail as E1 MCP only if quoting those URLs; this note does not expand them).
- `CLAIM` [E1] CLI: MCP uses the **same configuration as the editor**; `agent` auto-discovers/uses tools; commands include `agent mcp list`, `list-tools`, `login`, `enable`, `disable`; `--approve-mcps`; precedence phrasing “project → global → nested”. [E1: CLI MCP — https://cursor.com/docs/cli/mcp — accessed 2026-07-29]
- `CLAIM` [E1] Cursor SDK (TypeScript) documents local agent MCP load order (first-match-wins on conflicting names): send inline → create inline → **plugins** (if `local.settingSources` includes `"plugins"`) → project `.cursor/mcp.json` → user `~/.cursor/mcp.json`. Cloud: send → create → user/team from cursor.com/agents; cloud ignores `local.settingSources` and always loads project/team/plugins. [E1: Cursor SDK TypeScript — MCP servers — https://cursor.com/docs/sdk/typescript — accessed 2026-07-29]
- `INFERENCE` [E4] SDK precedence is the strongest **documented** name-conflict order that includes **plugin** servers; applying it unchanged to IDE Agent chat is **not** explicitly stated on mcp.md/plugins.md. Premises: (1) SDK claim above [E1 sdk/typescript]; (2) IDE docs omit equivalent table [GAP §4.6].
- `CLAIM` [E1] Hooks surface includes `beforeMCPExecution` / `afterMCPExecution` (agent hooks list on plugins reference). Behavioral detail deferred to hooks docs / T4F. [E1: Plugins reference — Available hook events — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]

### 4.8 Testing / validation (as documented)

- `CLAIM` [E1] Local plugin test path: copy/symlink under `~/.cursor/plugins/local/<plugin>`, reload window, “Verify your plugin components load in Cursor, such as rules, skills, or **MCP servers**.” [E1: Plugins — Test plugins locally — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Submission checklist includes “Plugin has been tested locally” and variables/`mcp.json` placeholder matching. [E1: Plugins reference — Submission checklist — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Debug MCP: Output panel → **MCP Logs** (init, tool calls, errors). Disable via Customize toggle without removing config. [E1: MCP — FAQ — https://cursor.com/docs/mcp.md — accessed 2026-07-29]
- `CLAIM` [E1] CLI can list servers/tools and login/enable/disable for validation workflows. [E1: CLI MCP — https://cursor.com/docs/cli/mcp — accessed 2026-07-29]
- `GAP` No documented automated MCP schema validator, plugin MCP unit-test harness, or CI check for `mcp.json` beyond checklist prose. Searched: mcp.md FAQ, plugins.md local test, plugins reference submission. Result: not found.

### 4.9 Security

- `CLAIM` [E1] MCP security practices (mcp.md): verify source; review permissions; limit API keys; audit code; servers can access external services and execute code. Prefer env vars for secrets; sensitive servers via local stdio; minimal key permissions. [E1: MCP — Security considerations / FAQ sensitive data — https://cursor.com/docs/mcp.md — accessed 2026-07-29]
- `CLAIM` [E1] Marketplace: every plugin manually reviewed; open source required; updates reviewed; plugins “respect your MCP allowlist and blocklist” — blocked MCP in a plugin installs but **cannot make calls**. [E1: Marketplace security — https://cursor.com/help/security-and-privacy/marketplace-security.md — accessed 2026-07-29]; [E1: Plugins FAQ — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Plugin docs: do not put secret values in the plugin repo; use `${VAR}` + dashboard. [E1: Plugins reference — Variables — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Enterprise allowlist + network modes for local command MCP (Allow all / Allowlist / Deny all / No sandbox). Auto-review classifier “is not a security boundary.” Cloud Agents do not use Run Modes. [E1: MCP — Enterprise — https://cursor.com/docs/mcp.md — accessed 2026-07-29]; [E1: Run Modes — https://cursor.com/docs/agent/security/run-modes.md — accessed 2026-07-29]
- `CLAIM` [E1] Deeplink install format for sharing MCP configs (plugins.md points to install-links); same shape as `mcp.json` transport config, base64-encoded. [E1: MCP Install Links — https://cursor.com/docs/mcp/install-links.md — accessed 2026-07-29]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Plugin MCP uses dashboard `${VAR}` substitution, distinct from user mcp.json `${env:…}` | confirmed (docs) | plugins reference MCP servers + Variables [E1] |
| H2 | Specifying `mcpServers` in manifest disables root `mcp.json` auto-discovery | confirmed (docs) | Component discovery “replaces” [E1] |
| H3 | IDE Agent name-conflict precedence matches SDK (plugins before project/user) | open | SDK [E1]; IDE [GAP] |
| H4 | STDIO `type: "stdio"` is always required in files | open | table Required vs examples omit [E1 conflict] |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| STDIO `type` required? | mcp.md STDIO table: `type` Required `"stdio"` | mcp.md CLI Server examples omit `type` | OPEN — leave unresolved; no E0 this wave |
| Marketplace `mcpServers` arity | plugin.json: string \| object \| **array** | marketplace plugin entry: string \| object | OPEN / GAP — do not assume array on marketplace entries |
| Name conflict precedence | SDK: plugins > project > user (gated) | IDE mcp.md: locations only | Prefer documenting SDK as SDK-scoped; IDE precedence = GAP |

## 7. Gaps & OPEN

- `GAP` Plugin MCP support (or ban) for `${env:…}` / `${workspaceFolder}` / `envFile` / static OAuth `auth` block.
- `GAP` IDE Agent merge/precedence rules for duplicate MCP server names across plugin / project / user / extension API / team.
- `GAP` Formal automated testing/validation for plugin MCP beyond local load + MCP Logs + checklist.
- `GAP` Extension-registered servers vs plugin variables, allowlist, and OAuth flows.
- `GAP` Whether marketplace entry `mcpServers` accepts arrays like `plugin.json`.
- `OPEN` Resolve STDIO `type` Required vs example omission (E0 or Cursor clarification).
- `OPEN` Confirm whether SDK local precedence applies to IDE chat Agent (H3).
- `OPEN` Deep behavior of `beforeMCPExecution` / `afterMCPExecution` (T4F / hooks docs).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] For Toolbelt-style plugins shipping MCP, Wave 1 docs imply: root `mcp.json` + optional `variables` schema + dashboard secrets; avoid embedding secrets; do not rely on shell `${env:…}` as the **documented** plugin secret path. Premises: §4.3 claims.
- `INFERENCE` [E4] Team distribution of MCP via Default marketplace is opt-in per developer (unless Required mode), separate from Cloud Agent Team MCP availability. Premises: §4.6 Team MCP claims.
- `INFERENCE` [E4] Do not treat Auto-review / marketplace review as a hard security boundary for MCP tool execution. Premises: marketplace-security + run-modes “not a security boundary”.

**No design locks** — note status `draft`; E1 uncorroborated by E0 this wave.

## 9. Source list (deduped)

1. https://cursor.com/docs/mcp.md — accessed 2026-07-29
2. https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29
3. https://cursor.com/docs/plugins.md — accessed 2026-07-29
4. https://cursor.com/docs/extension-api — accessed 2026-07-29
5. https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29
6. https://cursor.com/help/security-and-privacy/marketplace-security.md — accessed 2026-07-29 (linked from plugins FAQ)
7. https://cursor.com/docs/agent/security/run-modes.md — accessed 2026-07-29 (linked from mcp.md tool approval)
8. https://cursor.com/docs/mcp/install-links.md — accessed 2026-07-29 (linked from plugins.md)
9. https://cursor.com/docs/cli/mcp — accessed 2026-07-29 (Cursor CLI; same config claim)
10. https://cursor.com/docs/sdk/typescript — accessed 2026-07-29 (plugin MCP load order for SDK agents)
11. Campaign D0: `docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md` — version pin 3.13.25
12. Upstream citations **not expanded** (Cursor links only): https://modelcontextprotocol.io/introduction ; https://modelcontextprotocol.io/extensions/apps/overview

## 10. D0–D14 stop check (light)

- [x] D0 version pin recorded (3.13.25 / docs live / skew unknown)
- [x] Reference used for plugin MCP API claims (`reference/plugins.md`, `extension-api`)
- [x] Limitation path: official security/enterprise + marketplace-security; E3 scan **waived** (Wave 1 official-only)
- [x] Conflicts logged
- [x] No design lock on uncorroborated E3 (none used)
- [x] Durable findings in this research-protocol note
