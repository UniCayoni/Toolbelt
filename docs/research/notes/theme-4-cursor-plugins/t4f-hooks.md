---
title: "T4F — Cursor Hooks (Wave 1 official docs)"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-T4F]
supersedes: null
access_date: 2026-07-29
cursor_version_pin: "3.13.25"
product_status: in_use
---

# T4F — Cursor Hooks deep dive (Wave 1)

Using `docs-research` + `research-protocol`.

## 1. Scope

- **Question / goal:** Document Cursor Hooks from official docs only: `hooks.json` schema, all documented events, command/matcher fields, stdin/stdout contracts, deny/allow behavior, plugin distribution, security notes, testing guidance (if any), composition with skills/rules.
- **In scope:** https://cursor.com/docs/hooks.md (primary); https://cursor.com/docs/reference/plugins.md (Hooks format + event list); https://cursor.com/docs/plugins.md; linked marketplace security; linked third-party hooks reference; cloud-agent hooks section as linked from hooks.md.
- **Out of scope:** Wave 2 Alexandria/GitHub community; inventing event names; E0 runtime corroboration of hook behavior (not run this pass); treating create-hook skill as E1.
- **Comprehension type:** reuse / adaptive (plugin authoring + Toolbelt campaign).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch (hooks.md, plugins.md, reference/plugins.md, marketplace-security.md, third-party-hooks.md); WebSearch (`site:cursor.com/docs hooks testing`, Hooks tab); Read campaign D0 note for version pin |
| Corpora / URLs searched | See Source list §9 |
| Queries (exact) | `site:cursor.com/docs hooks testing hooks.json`; `Cursor hooks "Hooks tab" OR "how to test" hooks.json site:cursor.com` |
| What was *not* searched | GitHub issue deep-dive; forum as SoT; installed Cursor source for schema; Alexandria RAG (Wave 2) |
| Provenance | Entity=Cursor Hooks docs; Activity=T4F Wave 1 fetch+grade; Agent=gatherer-T4F |

### D0 identity (docs-research)

| Field | Value |
|-------|-------|
| Product | Cursor IDE — https://cursor.com |
| Installed version (E0) | `3.13.25` per campaign D0 note [E0 via `d0-cursor-plugins-identity.md` 2026-07-29] |
| Docs | Live https://cursor.com/docs/hooks.md — **no release-tag pin** → skew vs 3.13.25 = **unknown** |
| Status | `in_use` |

### Diátaxis (D2)

| URL | Type | Trust for API truth |
|-----|------|---------------------|
| https://cursor.com/docs/hooks.md | reference (+ how-to examples) | **high** for events/IO contracts |
| https://cursor.com/docs/reference/plugins.md | reference | **high** for plugin hooks path + event list |
| https://cursor.com/docs/plugins.md | explanation / how-to | medium (overview + local plugin test path) |
| https://cursor.com/help/security-and-privacy/marketplace-security.md | explanation | medium (marketplace risk; not hooks-runtime SoT) |
| https://cursor.com/docs/reference/third-party-hooks.md | reference | high for Claude mapping; secondary to native hooks.md |

OpenAPI / JSON Schema file for hooks: **N/A / GAP** (prose tables + examples only).

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | systematic (official docs Wave 1) |
| Why | Mission requires cite-or-omit inventory of events + contracts |
| Scope boundary | Official cursor.com docs pages listed; no inventing events |

## 4. Findings

### 4.1 What hooks are

- `FACT` [E1] Hooks observe, control, and extend the agent loop via custom scripts; defined in `hooks.json` at project or user level, or installed through plugins from **Customize**. They are spawned processes that communicate over stdio using JSON in both directions. [E1: Hooks — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] Documented use cases include: formatters after edits, analytics, PII/secrets scanning, gating risky ops, controlling subagent (Task) execution, injecting context at session start. [E1: same]

### 4.2 Configuration locations & priority

- `FACT` [E1] Config sources (priority highest→lowest for conflict merge): **Enterprise** (MDM paths) → **Team** (Enterprise dashboard) → **Project** (`<project>/.cursor/hooks.json`) → **User** (`~/.cursor/hooks.json`). All matching hooks from every source run; higher-priority sources win on conflicting responses. [E1: Hooks §Configuration — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] Enterprise paths: macOS `/Library/Application Support/Cursor/hooks.json`; Linux/WSL `/etc/cursor/hooks.json`; Windows `C:\ProgramData\Cursor\hooks.json`. [E1: same]
- `FACT` [E1] Working directory: project hooks run from **project root**; user hooks from `~/.cursor/`; enterprise from enterprise config dir; team from managed hooks directory. Project script paths should be like `.cursor/hooks/script.sh`, not `./hooks/script.sh`. [E1: same]
- `FACT` [E1] Project hooks require a **trusted workspace** to run. [E1: Hooks §Team Distribution — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] With Claude third-party hooks enabled, full priority extends: Enterprise → Team → Project → User → Claude project local → Claude project → Claude user. [E1: Third Party Hooks — https://cursor.com/docs/reference/third-party-hooks.md — accessed 2026-07-29]

### 4.3 `hooks.json` schema (documented fields)

- `FACT` [E1] Global option: `version` — number, default `1` — “Config schema version”. [E1: Hooks §Global Configuration Options — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] Top-level `hooks` object maps **hook event names** → arrays of hook definitions. [E1: same]
- `FACT` [E1] Per-script options documented:

| Option | Type (as documented) | Default | Description (doc paraphrase) |
|--------|----------------------|---------|------------------------------|
| `command` | string | required | Script path or command |
| `type` | `"command"` \| `"prompt"` | `"command"` | Execution type |
| `timeout` | number | platform default | Timeout in seconds |
| `loop_limit` | number \| null | `5` (Cursor); `null` (Claude Code hooks) | Per-script loop limit for `stop` / `subagentStop`; `null` = no limit |
| `failClosed` | boolean | `false` | On `true`, crash/timeout/invalid JSON **blocks** action (fail-closed) |
| `matcher` | **object** (table) vs **string** (all examples) | — | Filter when hook runs |

[E1: Hooks §Per-Script Configuration Options — https://cursor.com/docs/hooks.md — accessed 2026-07-29]

- `CLAIM` [E1] Prompt hooks may also use `prompt` (natural-language condition) and optional `model` to override the default LLM. [E1: Hooks §Prompt-Based Hooks — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `GAP` Formal standalone JSON Schema / OpenAPI for `hooks.json` not published on the fetched pages. Searched: hooks.md tables + examples only. Result: prose schema only.
- `OPEN` Matcher type conflict: options table says `matcher` type `object`; every example uses a **string** (regex). Follow-up: confirm accepted shapes via E0 or deeper docs. See §6 Conflicts.

### 4.4 Hook execution types

- `FACT` [E1] **Command hooks** (default): shell scripts; JSON on stdin; JSON on stdout. Exit `0` = success use JSON; exit `2` = block (≡ `permission: "deny"`); other non-zero = fail-open (action proceeds) unless `failClosed: true`. [E1: Hooks §Command-Based Hooks / Troubleshooting — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] **Prompt hooks**: LLM evaluates natural language; returns structured `{ ok: boolean, reason?: string }`; `$ARGUMENTS` replaced with hook input JSON (or input auto-appended if absent); uses a fast model; optional `model` override. [E1: Hooks §Prompt-Based Hooks — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] Cloud agents run **command-based hooks only**; prompt-based hooks are not available in cloud (auth wiring gap). [E1: Hooks §Cloud agent support — https://cursor.com/docs/hooks.md — accessed 2026-07-29]

### 4.5 Matchers

- `FACT` [E1] Matcher field filtering by hook (documented):

| Hook(s) | Matcher applied to |
|---------|-------------------|
| `preToolUse` / `postToolUse` / `postToolUseFailure` | Tool type: e.g. `Shell`, `Read`, `Write`, `Grep`, `Delete`, `Task`, MCP as `MCP:<tool_name>` |
| `subagentStart` / `subagentStop` | Subagent type: e.g. `generalPurpose`, `explore`, `shell`, etc. |
| `beforeShellExecution` / `afterShellExecution` | Full shell command string |
| `beforeReadFile` | Tool type: e.g. `TabRead`, `Read` |
| `afterFileEdit` | Tool type: e.g. `TabWrite`, `Write` |
| `beforeSubmitPrompt` | Value `UserPromptSubmit` |
| `stop` | Value `Stop` |
| `afterAgentResponse` | Value `AgentResponse` |
| `afterAgentThought` | Value `AgentThought` |

[E1: Hooks §Matcher Configuration — https://cursor.com/docs/hooks.md — accessed 2026-07-29]

- `GAP` Matcher semantics for events not listed in the matcher table (e.g. `sessionStart`, `sessionEnd`, `beforeMCPExecution`, `afterMCPExecution`, `beforeTabFileRead`, `afterTabFileEdit`, `preCompact`, `workspaceOpen`) — not specified on that page section.

### 4.6 Deny / allow / ask behavior (by event)

- `FACT` [E1] `beforeShellExecution` / `beforeMCPExecution` output: `permission`: `"allow"` \| `"deny"` \| `"ask"`; optional `user_message`, `agent_message`. Default failures fail-open; set `failClosed: true` for security-critical (esp. recommended for `beforeMCPExecution`). [E1: Hooks §beforeShellExecution / beforeMCPExecution — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] `preToolUse` output: `permission` `"allow"` \| `"deny"`; `"ask"` “accepted by the schema but **not enforced** for `preToolUse` today”; optional `user_message`, `agent_message`, `updated_input`. [E1: Hooks §preToolUse — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] `subagentStart`: `permission` `"allow"` \| `"deny"`; `"ask"` **not supported** and treated as `"deny"`; optional `user_message`. [E1: Hooks §subagentStart — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] `beforeReadFile` / `beforeTabFileRead`: `permission` `"allow"` \| `"deny"`; `beforeReadFile` may include `user_message`; failures default allow unless `failClosed: true`. [E1: Hooks §§beforeReadFile, beforeTabFileRead — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] `beforeSubmitPrompt`: `continue` true\|false (+ optional `user_message`) to allow/block submission. [E1: Hooks §beforeSubmitPrompt — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] `sessionStart`: schema accepts `continue` / `user_message` but “current callers do not enforce them”; session creation is **not blocked** even when `continue` is `false`. Fire-and-forget relative to agent loop wait. Useful outputs: `env`, `additional_context`. [E1: Hooks §sessionStart — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] Exit code `2` blocks (≡ deny), matching Claude Code compatibility. [E1: Hooks §Troubleshooting; Third Party Hooks §Exit Code Behavior — accessed 2026-07-29]

### 4.7 Common stdin fields & environment

- `FACT` [E1] Common input fields (agent/session hooks): `conversation_id`, `generation_id`, `model`, `model_id`, `model_params`, `hook_event_name`, `cursor_version`, `workspace_roots`, `user_email`, `transcript_path`. [E1: Hooks §Common schema — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] `workspaceOpen` omits `conversation_id`, `generation_id`, `model`, `session_id`, `transcript_path`; still gets `hook_event_name`, `cursor_version`, `workspace_roots`, `user_email`. [E1: same]
- `FACT` [E1] Env vars for hook scripts: `CURSOR_PROJECT_DIR`, `CURSOR_VERSION`, `CURSOR_USER_EMAIL` (if logged in), `CURSOR_TRANSCRIPT_PATH` (if transcripts enabled), `CURSOR_CODE_REMOTE` (`"true"` when remote), `CLAUDE_PROJECT_DIR` (compat alias). Session `env` from `sessionStart` passed to subsequent hooks in that session. [E1: Hooks §Environment Variables — https://cursor.com/docs/hooks.md — accessed 2026-07-29]

### 4.8 Complete event inventory (cited — only names on official pages)

Sources: hooks.md categories + reference section; plugins reference “Available hook events”; cloud support matrices.

#### Agent hooks (Cmd+K / Agent Chat)

| Event | Role (doc) | Blocking / notable IO | Cloud agent |
|-------|------------|----------------------|-------------|
| `sessionStart` | New composer conversation; inject `env` / `additional_context` | Non-blocking for session create; `continue` not enforced | **No** (deferred) |
| `sessionEnd` | Conversation end; fire-and-forget | Output unused | **No** |
| `preToolUse` | Before any tool | `permission` allow/deny; `updated_input` | **Yes** |
| `postToolUse` | After successful tool | `additional_context`; MCP: `updated_mcp_tool_output` | **Yes** |
| `postToolUseFailure` | Tool fail/timeout/deny | No output fields currently | **Yes** |
| `subagentStart` | Before Task/subagent | allow/deny (`ask`→deny) | **Yes** |
| `subagentStop` | Subagent done | `followup_message` if status completed; loop_limit | **Yes** |
| `beforeShellExecution` | Before shell | allow/deny/ask | **Yes** |
| `afterShellExecution` | After shell | Audit (`command`, `output`, `duration`, `sandbox`) | **Yes** |
| `beforeMCPExecution` | Before MCP tool | allow/deny/ask; failClosed recommended | **No** (deferred) |
| `afterMCPExecution` | After MCP tool | Audit (`result_json`, etc.) | **No** (deferred) |
| `beforeReadFile` | Before Agent file read | allow/deny; content in input | **Yes** |
| `afterFileEdit` | After Agent file edit | edits payload; formatters | **Yes** |
| `beforeSubmitPrompt` | After send, before backend | `continue` | **Yes** |
| `preCompact` | Before compaction | Observational; optional `user_message` | **Yes** |
| `stop` | Agent loop ends | optional `followup_message`; `loop_limit` default 5 | **Yes** |
| `afterAgentResponse` | After assistant message | input `text` | **Yes** |
| `afterAgentThought` | After thinking block | input `text`, `duration_ms`; no output fields | **Yes** |

[E1: Hooks §Hook categories, §Hook events, §Cloud agent support — https://cursor.com/docs/hooks.md — accessed 2026-07-29]

#### Tab hooks (inline completions)

| Event | Role | Notable IO | Cloud |
|-------|------|------------|-------|
| `beforeTabFileRead` | Tab file access control | allow/deny; no `attachments` | **No** (IDE-only) |
| `afterTabFileEdit` | Tab post-edit | richer edit `range` / line fields; no output fields | **No** |

[E1: Hooks §§Tab hooks, beforeTabFileRead, afterTabFileEdit, Cloud agent — https://cursor.com/docs/hooks.md — accessed 2026-07-29]

#### App lifecycle

| Event | Role | Notable IO | Cloud |
|-------|------|------------|-------|
| `workspaceOpen` | Workspace open / folder change; skip if zero folders; desktop app + CLI | optional `pluginPaths` absolute paths to load | **No** (IDE lifecycle) |

[E1: Hooks §workspaceOpen; Plugins overview §Using the workspaceOpen hook — https://cursor.com/docs/hooks.md + https://cursor.com/docs/plugins.md — accessed 2026-07-29]

#### Count check

- `FACT` [E1] Plugins reference lists the same Agent (18) + Tab (2) + App (`workspaceOpen`) event names as hooks.md categories. [E1: Plugins reference §Available hook events — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `INFERENCE` [E4] Total documented Cursor-native event names on these pages = **21**. Premises: (1) 18 agent names in plugins reference agent list; (2) 2 Tab; (3) 1 app. [E1 cites above]

**Do not invent:** No other event names claimed in this note.

### 4.9 Distribution via plugins

- `FACT` [E1] Plugins may include Hooks as a component; default discovery path `hooks/hooks.json` (“Parsed for hook event names”). [E1: Plugins reference §Component discovery — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Manifest optional field `hooks`: string or object — “Path to hooks config file, or inline hook config”. Specifying a path **replaces** folder discovery for that component. [E1: Plugins reference §Plugin manifest / discovery — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Example plugin `hooks/hooks.json` uses `afterFileEdit`, `beforeShellExecution` (+ matcher), `sessionEnd` with `./scripts/...` commands. [E1: Plugins reference §Hooks format — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Hooks overview: install hooks through plugins from **Customize**. [E1: Hooks intro — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] `workspaceOpen` can return `pluginPaths` to load workspace-dependent plugins. [E1: Hooks §workspaceOpen; Plugins §Using the workspaceOpen hook — accessed 2026-07-29]
- `FACT` [E1] Local plugin test path: copy/symlink under `~/.cursor/plugins/local/<name>`, reload window, verify components load — then marketplace publish. [E1: Plugins §Test plugins locally — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `GAP` Official docs do not describe merge/order semantics when the **same event** is defined in both a plugin’s `hooks/hooks.json` and project `.cursor/hooks.json` beyond the Enterprise→Team→Project→User priority (plugins’ placement in that stack not spelled out on fetched pages).

### 4.10 Composition with skills / rules

- `FACT` [E1] A plugin can bundle any combination of Rules, Skills, Agents, Commands, MCP Servers, and Hooks. [E1: Plugins overview §What plugins contain — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Customize manages plugins, MCP, rules, and skills together; skills appear under Agent Decides / `/skill-name`. [E1: Plugins §Managing installed plugins — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `GAP` No official page section found that defines runtime composition rules between hooks and skills/rules (e.g. whether a skill can register hooks, or hook↔rule precedence beyond co-packaging in a plugin). Searched: hooks.md, plugins.md, reference/plugins.md. Result: co-bundle + discovery only.
- `INFERENCE` [E4] Hooks are an **event/stdio automation surface**; rules/skills are **prompt/guidance surfaces** — composition in practice is “same plugin / same workspace,” not a documented shared execution graph. Premises: (1) component table separates Hooks from Rules/Skills; (2) hooks communicate via JSON stdio; (3) no cross-component API on fetched pages.

### 4.11 Security notes (official)

- `FACT` [E1] Project hooks run only in **trusted** workspaces. [E1: Hooks §Project Hooks — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] `failClosed: true` recommended for security-critical hooks (explicitly called out for `beforeMCPExecution` and available for `beforeReadFile`). [E1: Hooks §§failClosed, beforeMCPExecution, beforeReadFile — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] Marketplace plugins: manually reviewed; open source required; no binaries; MCP allowlist/blocklist respected; install at user risk; updates manually reviewed; report to security-reports@cursor.com. [E1: Marketplace security — https://cursor.com/help/security-and-privacy/marketplace-security.md — accessed 2026-07-29]
- `CLAIM` [E1] Marketplace security page describes plugins as “largely markdown… No binaries” — hooks scripts in plugins are still executable automation when present; page does not specially call out hooks as higher risk. [E1: same] → treat as incomplete threat model for hooks-bearing plugins (`OPEN` for Wave 2).
- `FACT` [E1] Partner integrations section lists ecosystem vendors for MCP governance, code/dependency/agent security, secrets (e.g. Semgrep, Snyk, 1Password) via hooks. [E1: Hooks §Partner Integrations — https://cursor.com/docs/hooks.md — accessed 2026-07-29]

### 4.12 How to test hooks (documented)

- `FACT` [E1] Troubleshooting: **Hooks tab** in **Customize** and a **Hooks output channel** to debug configured/executed hooks and errors. [E1: Hooks §Troubleshooting — https://cursor.com/docs/hooks.md — accessed 2026-07-29]
- `FACT` [E1] Config reload: Cursor watches `hooks.json` and reloads on save; if still not loading, restart Cursor. Check relative paths per source. [E1: same]
- `FACT` [E1] Third-party hooks troubleshooting: exit `2` to block; check JSON schema; view Hooks output channel; “Test your hooks in both tools” for Claude↔Cursor compatibility. [E1: Third Party Hooks §Troubleshooting — https://cursor.com/docs/reference/third-party-hooks.md — accessed 2026-07-29]
- `FACT` [E1] Plugins local install under `~/.cursor/plugins/local` is documented for testing **plugins** (including hook components by implication of “verify your plugin components load”). [E1: Plugins §Test plugins locally — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `GAP` **No dedicated “how to test hooks” guide** found on official docs (no unit-test harness, no CLI `cursor hooks test`, no golden stdin fixtures page). Searched: hooks.md Troubleshooting; plugins local test; site search for hooks testing. Result: debug UI + manual trigger implied by examples only.
- `GAP` Wave 1 did not deep-crawl GitHub `cursor/plugin-template` or example repos for test scripts (mission allowed search; formal E1 GitHub SoT deferred to Wave 2). WebSearch returned forum/E3 leads only — not used as locks.

### 4.13 Cloud agent constraints (summary)

- `FACT` [E1] Cloud loads project `.cursor/hooks.json` + Enterprise team/enterprise hooks; **not** user `~/.cursor/hooks.json`. Command hooks only. Hooks skip early read-only exploratory turns. Unsupported in cloud: `sessionStart`, `sessionEnd`, MCP before/after, Tab hooks, `workspaceOpen` (reasons documented). [E1: Hooks §Cloud agent support — https://cursor.com/docs/hooks.md — accessed 2026-07-29]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Official docs document ≥20 named hook events including `workspaceOpen` | confirmed | Event inventory §4.8 |
| H2 | Official docs include a dedicated automated hook test harness | rejected | GAP §4.12 |
| H3 | `matcher` accepts object configs as well as strings | open | Type table vs examples conflict §6 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| `matcher` type | Per-script table: type `object` [hooks.md] | Examples: string regex `"Shell"`, `"curl\|wget\|nc "` [hooks.md] | Prefer examples for observed config shape; leave type formalization **OPEN**; do not invent object schema |
| Plugin event list vs hooks.md | Same 21 names [reference/plugins.md] | Full IO contracts only on [hooks.md] | Prefer hooks.md for contracts; lists **agree** on names |

## 7. Gaps & OPEN

1. **Testing:** No official automated test / fixture protocol for hooks (UI debug only) — high-priority GAP for Toolbelt authoring.
2. **Matcher type:** string vs object schema unresolved.
3. **Matcher coverage:** several events lack documented matcher fields.
4. **Plugin vs project hook merge order** when both define the same event.
5. **JSON Schema artifact** for `hooks.json` not published.
6. **Docs ↔ Cursor 3.13.25 skew** unknown (live docs, no tag).
7. **Hooks-specific marketplace threat model** thin (generic plugin security).
8. Wave 2: GitHub examples, forum Windows hook quirks, create-hook skill vs docs drift (skill is not E1).

## 8. Implications (INFERENCE only — not design locks)

- `INFERENCE` [E4] For Toolbelt/plugin authors: treat **hooks.md Reference** as SoT for event IO; use plugins reference only for packaging paths (`hooks/hooks.json`, manifest `hooks` field). Premises: Diátaxis + detail depth.
- `INFERENCE` [E4] Security-sensitive gates should prefer `beforeShellExecution` / `beforeMCPExecution` / `beforeReadFile` with `failClosed: true` and exit `2` / `permission: deny`. Premises: §4.6 + failClosed docs.
- `INFERENCE` [E4] Do not rely on `sessionStart.continue` or `preToolUse` `"ask"` for enforcement. Premises: explicit non-enforcement notes in docs.
- `INFERENCE` [E4] Wave 1 cannot lock a hooks testing strategy beyond “Hooks tab + output channel + manual event trigger + local plugin path.” Premises: GAP §4.12.

## 9. Source list (deduped)

1. https://cursor.com/docs/hooks.md — accessed 2026-07-29 (primary)
2. https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29
3. https://cursor.com/docs/plugins.md — accessed 2026-07-29
4. https://cursor.com/help/security-and-privacy/marketplace-security.md — accessed 2026-07-29
5. https://cursor.com/docs/reference/third-party-hooks.md — accessed 2026-07-29 (linked from hooks.md)
6. Campaign D0: `docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md` (version pin 3.13.25)

## 10. Docs-research stop checklist

- [x] D0 version pin recorded (`in_use` 3.13.25; docs untagged)
- [x] Reference used for API claims (hooks.md)
- [x] Limitation path: cloud matrix + fail-open + non-enforced fields; E3 forum scan not used as locks
- [x] Conflicts recorded (matcher type)
- [x] No design lock on uncorroborated E3
- [x] Durable findings in this `research-protocol` note
