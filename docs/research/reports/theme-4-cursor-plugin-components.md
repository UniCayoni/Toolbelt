---
title: "Theme 4 — Cursor plugin components (integrated report)"
status: accepted
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
accepted: 2026-07-29
acceptance_scope: full
accepted_by: human (Jonathan)
protocol: docs/PROTOCOL.md
product: Cursor IDE
product_version_in_use: "3.13.25"
docs_access_date: 2026-07-29
authors: [integrator]
wave3_status: complete (t4l/t4m/t4n done; diminishing returns)
---

# Theme 4 — Cursor plugin components for agents

**Status:** **accepted** (full) — 2026-07-29. Waves 1–3 merged; residual OPEN retained as documented absence (not invented closures).  
**Acceptance scope:** Full report — component contracts (E0/E1) **and** §6 Toolbelt implications as method/policy SoT for this plugin.  
**Protocol:** `docs/PROTOCOL.md` — cite-or-omit; GAP/OPEN remain non-locks.  
**Pin:** Cursor **3.13.25** [E0]; live `cursor.com/docs` (untagged) → docs↔build skew **unknown** (still OPEN).

### Sources merged

| ID | Path | Wave |
|----|------|------|
| D0 | `notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md` | 0 |
| T4A | `…/t4a-plugin-manifest-marketplace.md` | 1 |
| T4B | `…/t4b-rules-agentsmd.md` | 1 |
| T4C | `…/t4c-skills.md` | 1 |
| T4D | `…/t4d-agents-subagents.md` | 1 |
| T4E | `…/t4e-commands.md` | 1 |
| T4F | `…/t4f-hooks.md` | 1 |
| T4G | `…/t4g-mcp-in-plugins.md` | 1 |
| T4H | `…/t4h-agentskills-spec-writing.md` | 2 |
| T4I | `…/t4i-github-plugin-skill-patterns.md` | 2 |
| T4J | `…/t4j-alexandria-corroboration.md` | 2 |
| T4K | `…/t4k-testing-validation.md` | 2 |
| T4L | `…/t4l-residual-plugin-agents-wireup.md` | 3 (**done** — residuals remain GAP) |
| T4M | `…/t4m-residual-frontmatter-runtime.md` | 3 (**done** — see §7) |
| T4N | `…/t4n-residual-rules-agentsmd-precedence.md` | 3 (**done** — see §7) |

---

## 1. Executive summary

1. A Cursor **plugin** is a directory with `.cursor-plugin/plugin.json` (`name` required) that can bundle **Rules, Skills, Agents, Commands, MCP servers, Hooks**. [E1 T4A]
2. Without explicit manifest paths, Cursor **auto-discovers** default folders; an explicit field **replaces** (does not add to) that component’s discovery. [E1 T4A]
3. Operational load for authors: copy/symlink under `~/.cursor/plugins/local/<name>` → Reload Window; or `vscode.cursor.plugins.registerPath` (manifest optional). Marketplace = public Git + manual review. [E1 T4A/T4K]
4. **Rules** (`.mdc`): `alwaysApply` / `description` / `globs` → Always | Intelligent | Glob | Manual; Team→Project→User precedence; applied at start of model context (not Tab). [E1 T4B]
5. **`AGENTS.md`**: nested “more specific wins”; **not** a plugin component (ship guidance as plugin Rules); conflict order vs Team/Project/User rules still **GAP**. [E1 T4B/T4N]
6. **Skills**: discovery via name+description; `/` invoke; Cursor FM: `name`, `description`, `paths`, `disable-model-invocation`, `metadata` (+ legacy `globs`). Portable Spec adds `license`/`compatibility`/`allowed-tools` — Cursor runtime honor **OPEN**. [E1 T4C/T4H]
7. Cold-start skill quality (Spec + high-signal examples): pushy when/trigger **description**, lean procedural body, &lt;500 lines / &lt;5000 tokens, conditional `references/`, gotchas in body, clean-context evals. [E1 T4H; E0/E1 T4I]
8. **Agents (plugin)** ≠ **Subagents (runtime)** in docs: plugin Agents document only `name`+`description`; Subagents add `model`/`readonly`/`is_background`, Task tool, Explore/Bash/Browser. Wire-up of plugin `agents/` → Task **confirmed GAP**. [E1 T4D/T4L]
9. **Commands**: `commands/` + `/` prompts; migrate-to-skills converts user/workspace slash commands → skills with `disable-model-invocation: true`; plugin-command migrate scope **GAP**. [E1 T4E]
10. **Hooks**: 21 events (18 agent + 2 Tab + `workspaceOpen`); JSON stdio; exit 2 deny / fail-open unless `failClosed`; debug via Hooks tab + output channel — **no** official fixture harness. [E1 T4F/T4K]
11. **MCP-in-plugins**: root `mcp.json` or manifest `mcpServers` override; plugin secrets = dashboard `${VAR}` (not shell `${env:…}`); MCP Logs for debug. [E1 T4G]
12. Alexandria RAG is a **hard GAP** for Cursor plugin SoT; use only for adjacent MCP/agent-authoring patterns. [E0 T4J]
13. Honest test plan today: static validate (`validate-template.mjs` / `review-plugin-submission`) + local load + Hooks/MCP debug UIs + manual `/` and prompt triggers — not Cursor-native CI evals. [E1/E0 T4K]
14. Real Cursor marketplace shape exemplar: **Superpowers** (skills + hooks path override + `displayName`); many high-star “skills” repos are Claude/skills.sh packs **without** `.cursor-plugin` — do not treat as Cursor packaging SoT. [E0/E1 T4I]

---

## 2. Component inventory & composition

### 2.1 Plugin package surface

| Component | Default discovery | Manifest override | Primary authoring artifact |
|-----------|-------------------|-------------------|----------------------------|
| Rules | `rules/` (`.md`/`.mdc`/`.markdown`) | `rules` | `.mdc` + YAML FM |
| Skills | `skills/<dir>/SKILL.md` | `skills` | `SKILL.md` |
| Agents | `agents/` markdown | `agents` | agent prompt MD |
| Commands | `commands/` (`.md`/`.mdc`/`.markdown`/`.txt`) | `commands` | slash prompt MD |
| Hooks | `hooks/hooks.json` | `hooks` path or inline | hooks.json + scripts |
| MCP | `mcp.json` | `mcpServers` | mcpServers map |
| Root skill | root `SKILL.md` iff no `skills/` and no manifest skills | — | single-skill plugin |

[E1 T4A reference/plugins]

**Variables:** `variables` JSON Schema declares names; users set values in dashboard Configure; substitute `${VAR}` in plugin MCP/config — secrets must not live in repo. [E1 T4A/T4G]

**Multi-plugin repos:** root `.cursor-plugin/marketplace.json`; marketplace entry merges over per-plugin `plugin.json` (marketplace wins). [E1 T4A]

### 2.2 Choose the right surface (docs distinctions)

| Need | Prefer | Evidence |
|------|--------|----------|
| Always-on / short constraints | Rule (`alwaysApply` or globs) | T4B |
| Multi-step judgment workflow, progressive detail | Skill | T4C/T4H; elevation map archive |
| Explicit `/` only, no auto-apply | Skill with `disable-model-invocation: true` **or** Command | T4C/T4E |
| Isolated context / parallel search | Runtime Subagent (Task) | T4D |
| Custom agent persona packaged in plugin | Plugin Agent (`agents/*.md`) — wire-up GAP | T4D |
| Mechanical allow/deny / observe loop | Hook | T4F |
| External tools/data | MCP (plugin or user/project) | T4G |

`INFERENCE` [E4] Prefer skills over always-on rules for long checklists (token tax) — aligns with Cursor migrate guidance for dynamic rules → skills and with Toolbelt elevation map (archive). Premises: T4B soft &lt;500 lines; T4C migrate-to-skills; archive elevation map.

---

## 3. How each component works (contracts)

### 3.1 Manifest & install

- Required: `.cursor-plugin/plugin.json` → `name` (kebab-case). [E1 T4A]
- Local test: `~/.cursor/plugins/local/<plugin>` + Reload. [E1 T4A]
- `registerPath` loads directory; folder discovery applies even without manifest. [E1 T4A]
- `workspaceOpen` hook may return `pluginPaths`. [E1 T4A/T4F]
- `displayName`: official `plugin.schema.json` accepts it; template + official plugins use it; **docs optional-field table omits it** (docs↔schema drift). [E1 T4M]

### 3.2 Rules + AGENTS.md

- Frontmatter: `description`, `alwaysApply`, `globs`. [E1 T4B]
- Precedence among rule layers: **Team → Project → User** (earlier wins). [E1 T4B]
- Nested AGENTS.md: combined; more specific wins. [E1 T4B]
- Project `.cursor/rules` plain `.md` ignored vs plugin `rules/` accepting `.md` — **OPEN conflict**. [E1 T4B]
- Soft guidance: keep rules short (&lt;500 lines mentioned); no numeric token budgets. [E1 T4B]

### 3.3 Skills (authoring for cold-start agents)

**Load model:** Discovery (name+description) → Activation (full SKILL.md) → Execution (optional scripts/refs). [E1 T4H/T4C]

**Write for fresh agents (evidenced):**

| Practice | Grade | Source |
|----------|-------|--------|
| Description = what + when + keywords; pushy; ≤1024 chars | E1 | Spec / skill-creator (T4H) |
| Body = agent wouldn’t already know; procedures & defaults | E1 | Spec best practices (T4H) |
| &lt;500 lines / &lt;5000 tokens; one-level `references/` | E1 | Spec (T4H); Cursor paraphrases progressive only |
| Conditional “read X when Y”, not bare “see references/” | E1 | Spec / examples (T4H) |
| Gotchas in main body | E1 | Spec / pdf skill (T4H) |
| `name` match folder (Cursor + Spec) | E1 | T4C/T4H; Vercel counterexample E0 T4I → enforcement OPEN |
| Cursor `paths` / `disable-model-invocation` | E1 | T4C |
| Clean-context with/without-skill evals | E1 Spec / E3 skill-creator | T4H/T4K — not Cursor IDE product |

### 3.4 Agents vs Subagents

| | Plugin Agents | Runtime Subagents |
|--|---------------|-------------------|
| Location | plugin `agents/` | `.cursor/agents/` (+ compat paths) |
| FM | `name`, `description` | + `model`, `readonly`, `is_background` |
| Invoke | (docs thin) | Task tool, `/name`, auto-delegate |
| Built-ins | — | Explore, Bash, Browser |

Customize calls packaged pieces “subagents”; plugins pages say “Agents” — synonym implied, **mapping unstated** (T4L). [E1 T4D]

### 3.5 Commands

- Discovery `commands/`; FM `name`/`description` (checklist expects frontmatter; format says “can include” → mild OPEN). [E1 T4E]
- `/migrate-to-skills` for **user/workspace** slash commands → skills with `disable-model-invocation: true`. Plugin `commands/` migrate eligibility **GAP**. [E1 T4E]
- Subagents docs: don’t use subagent for single-purpose slash work — use skill or command. [E1 T4D/T4E]

### 3.6 Hooks

- Events (complete inventory): see T4F — 18 agent + 2 Tab + `workspaceOpen`. [E1 T4F]
- Schema highlights: `command`, `matcher`, `timeout`, `failClosed`, `type` command|prompt. [E1 T4F]
- Exit codes: 0 use JSON; 2 deny; other fail-open unless `failClosed`. [E1 T4F]
- Merge priority: Enterprise → Team → Project → User. [E1 T4F]
- Plugin↔project same-event merge order **GAP**. [E1 T4F]

### 3.7 MCP in plugins

- Default `mcp.json` `{ "mcpServers": { … } }`; manifest override replaces discovery. [E1 T4G]
- Plugin `${VAR}` ≠ user mcp `${env:NAME}` / `${workspaceFolder}`. [E1 T4G]
- Agents consume via Available Tools / Run Modes; approval applies. [E1 T4G]
- IDE name-conflict precedence across plugin/project/user/API/team **GAP**. [E1 T4G]

---

## 4. How to test (honest matrix)

Shared official path: local plugin dir → Reload → verify components load + submission checklist. [E1 T4K]

| Component | Official | Practical add-ons | Still GAP |
|-----------|----------|-------------------|-----------|
| Manifest | Checklist + local load | `validate-template.mjs`; `review-plugin-submission` | No IDE validator UI |
| Rules | Local load; Customize; FAQ | Frontmatter review | No schema CLI |
| Skills | Local load; `/skill-name`; Customize | `skills-ref validate`; optional skill-creator evals (E3) | No Cursor CI eval runner |
| Agents | Local load; “test by prompts” | Explicit `/name` | Plugin↔Task wire-up; no harness |
| Commands | Local load + checklist | Manual `/` smoke | No dedicated procedure |
| Hooks | Hooks tab + output channel | Manual event triggers; exit-2 checks | No stdin fixtures / CLI |
| MCP | MCP Logs; Customize toggle | CLI `agent mcp list` (CLI surface) | No plugin MCP CI validator |

Marketplace manual review ≠ author-run harness. [E1 T4K]

---

## 5. Evidence reinforcement (Wave 2)

| Channel | Outcome |
|---------|---------|
| Alexandria (`ai_llm_agents`) | **GAP** for SKILL.md / .mdc / hooks.json / plugin.json / AGENTS.md. Adjacent: MCP host/client, tool-description quality, progressive disclosure as UX. [T4J] |
| agentskills.io + anthropics/skills | Strong writing/eval law for skills; Cursor links Spec but omits some FM + budgets on skills.md. [T4H] |
| GitHub sampling | Template = full composition; Superpowers = real Cursor plugin; Sentry/Vercel/Matt = skill packs without `.cursor-plugin`. [T4I] |

---

## 6. Implications for Toolbelt (accepted method/policy)

**Status:** **accepted** with the full Theme 4 report (2026-07-29). These are Toolbelt method/policy locks derived as `INFERENCE` [E4] from accepted premises — not Cursor product API claims. Residual Cursor GAPs in §7 remain OPEN.

1. `INFERENCE` [E4] Keep Toolbelt as skills+thin rules plugin; avoid always-apply long checklists. Premises: §2.2; T4B; archive elevation.
2. `INFERENCE` [E4] Re-eval existing skills against Spec cold-start checklist (description pushiness, budgets, conditional refs, gotchas). Premises: T4H; T4C Toolbelt E0 already uses `disable-model-invocation` correctly for slash-like skills. *(Applied 2026-07-29 polish pass; continue on new skills.)*
3. `INFERENCE` [E4] Prefer documenting smoke as: refresh references → sync local plugin → Reload → Customize visibility → manual skill announce/`/` → Hooks/MCP only if those components added. Premises: T4K; Toolbelt README sync scripts [E0 README].
4. `INFERENCE` [E4] Do not add plugin `agents/` expecting Task isolation until Cursor documents the wire-up (T4L GAP) — use runtime subagents via skill instructions instead. Premises: T4D GAP; Toolbelt skills text.
5. `INFERENCE` [E4] Ship `displayName` in Toolbelt `plugin.json` (schema-accepted) even though reference docs table omits it; keep required `name` kebab-case. Premises: T4M schema FACT; docs drift FACT. *(Applied.)*
6. `INFERENCE` [E4] Alexandria will not replace Cursor docs for plugin packaging until corpus ingest includes those docs. Premises: T4J.

### Toolbelt skill re-eval checklist (accepted practice)

| Check | Against |
|-------|---------|
| Description triggers without chat context? | T4H |
| Body lean; detail in `references/` with when-gates? | T4H/T4C |
| Announce **Using \`skill\`** still present for audit? | Toolbelt PROTOCOL / elevation |
| `disable-model-invocation` only on intentional slash skills? | T4C |
| No design locks from draft notes? | `draft-is-not-sot` rule |
| Coexistence with Superpowers stated? | coexistence rule; T4I Superpowers shape |

---

## 7. Residual GAPs & OPEN

### Wave 3 closers

| ID | Target | Outcome (2026-07-29) |
|----|--------|----------------------|
| T4L | Plugin `agents/` ↔ Task / `.cursor/agents/`; synonym Agents↔subagents; richer FM on plugin agents | **Confirmed GAP** — no load-path/precedence docs; no explicit synonym sentence; FM beyond `name`/`description` undocumented (E0: marketplace files may author richer fields; plugin agent `name`s observed as Task types only — not a contract). [T4L] |
| T4M | `displayName`; Spec-only skill FM; `name`==folder enforcement | **Partial close:** (1) `displayName` **CLOSED** via official `plugin.schema.json` (+ template/official plugins); docs table still omits (drift). (2) Spec-only `license`/`compatibility`/`allowed-tools` runtime **OPEN**; `metadata` on skills.md; `user-invocable` CLI-changelog only. (3) `name`==folder is docs MUST (**normative CLOSED**); runtime hard-fail vs lenient load **OPEN** (Spec client guide recommends warn/load; template validator doesn’t check; no E0). [T4M] |
| T4N | AGENTS.md vs rule-layer precedence; plugin AGENTS.md; project vs plugin `.md` rules | **Partial close:** (1) AGENTS.md↔Team/Project/User conflict order **still GAP**; (2) plugins **cannot** package AGENTS.md as a component — use `rules/` (**closed negative**); (3) project ignores plain `.md` in `.cursor/rules` vs plugin discovers `.md` — **dual surfaces clarified**, intentionality OPEN. Prefer `.mdc`+frontmatter. [T4N] |

### Campaign stop (diminishing returns)

No further gatherers. Remaining items need new Cursor primary docs or E0 runtime experiments (out of this research pass).

**P0 / structural (leave OPEN)**

- Plugin `agents/` ↔ Subagent/Task load path & richer FM acceptance [T4L]
- AGENTS.md vs Team/Project/User conflict precedence [T4N]
- Hooks/commands automated test protocols [T4K]

**P1 (leave OPEN)**

- Spec-only skill FM Cursor runtime honor; `name`≠folder hard-fail behavior [T4M]
- Plugin commands migrate-to-skills eligibility [T4E]
- MCP multi-source name conflicts; plugin↔project hooks merge [T4G/T4F]

**Closed this wave**

- Plugin-packaged `AGENTS.md` — absent; ship as Rules [T4N]
- `displayName` acceptance — schema-first-class; docs table stale [T4M]
- Project vs plugin `.md` rules — dual surfaces clarified [T4N]
- `name`==folder — normative MUST documented [T4M]

**P2**

- Docs↔3.13.25 skew; publish-page fetch empty; Windows symlink docs; marketplace ID→repo mapping; schema `$id` URL HTTP 500 this pass [T4M]

`INFERENCE` [E4] Implication §6.4 stands: do not rely on plugin `agents/` for Task isolation until Cursor documents the wire-up. Premises: T4D + T4L confirmed GAP.

`INFERENCE` [E4] Toolbelt should keep portable guidance in plugin `rules/*.mdc` (and host-project `AGENTS.md` when authoring for a repo), not expect plugins to distribute `AGENTS.md`. Premises: T4N §4.2.

---

## 8. Conflicts log (integrator)

| Topic | A | B | Resolution |
|-------|---|---|------------|
| Plugin rules `.md` | Project ignores plain `.md` in `.cursor/rules` [T4B] | Plugin discovery accepts `.md` under `rules/` [T4A] | Prefer `.mdc` for portability; leave conflict OPEN |
| Skills FM surface | Cursor paths/disable-model-invocation [T4C] | Spec license/compatibility/allowed-tools [T4H] | Dual surface; Cursor runtime for Spec-only = OPEN |
| Agents naming | Plugins “Agents” [T4A] | Customize “subagents” [T4D] | Treat as likely synonym; wire-up GAP |
| Marketplace “Sentry plugin” | Awesome E3 [T4I] | `getsentry/skills` no `.cursor-plugin` [T4I] | Don’t equate list row with that repo’s packaging |
| Frontmatter surfaces | Cursor skills.md omits Spec-only fields [T4C] | Spec has license/compatibility/allowed-tools [T4H] | Dual surface; runtime OPEN [T4M] |
| `displayName` | Docs optional table omits [T4A] | `plugin.schema.json` defines it [T4M] | Prefer schema; docs drift |

---

## 9. Source list (primary)

1. https://cursor.com/docs/plugins.md  
2. https://cursor.com/docs/reference/plugins.md  
3. https://cursor.com/docs/rules.md  
4. https://cursor.com/docs/skills.md  
5. https://cursor.com/docs/subagents.md  
6. https://cursor.com/docs/hooks.md  
7. https://cursor.com/docs/mcp.md  
8. https://cursor.com/docs/customize-cursor.md  
9. https://cursor.com/docs/extension-api  
10. https://agentskills.io / specification  
11. https://github.com/cursor/plugin-template  
12. https://github.com/obra/superpowers (E0/E1 packaging sample)  
13. https://github.com/cursor/plugins `schemas/plugin.schema.json` (displayName)  
14. Gatherer notes T4A–T4N under `docs/research/notes/theme-4-cursor-plugins/`

---

## 10. Integrator method

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Method | Merge graded gatherer notes; no new primary research in this file except cross-links |
| Not searched in integrator pass | Runtime E0 Reload experiments; full changelog archaeology |
| Wave 3 | T4L–T4N merged into §7; campaign stopped at diminishing returns |
| Acceptance | **full** — 2026-07-29 human accept; §6 elevated to Toolbelt method/policy SoT; §7 GAP/OPEN unchanged |
