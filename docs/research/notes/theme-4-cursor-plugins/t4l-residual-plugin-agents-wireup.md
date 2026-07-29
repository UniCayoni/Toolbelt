---
title: "T4L: Residual GAPs — plugin agents wireup + Agents/subagents naming"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-T4L]
supersedes: null
campaign: theme-4-cursor-plugins
wave: 3
access_date: 2026-07-29
cursor_version: "3.13.25"
aligned_with: docs/research/notes/theme-4-cursor-plugins/t4d-agents-subagents.md
prior_note: docs/research/notes/theme-4-cursor-plugins/t4d-agents-subagents.md
---

# T4L — Residual plugin Agents ↔ Subagents / Task wireup

Using `docs-research` + `research-protocol`.

## 1. Scope

- Question / goal: Close (or firmly leave OPEN/GAP) two Wave-3 residuals from T4D:
  1. How plugin `agents/*.md` maps to runtime Subagents / Task / `.cursor/agents/` (load path, precedence, whether `model` / `readonly` / `is_background` work on plugin agents).
  2. Whether Customize’s “subagents” vs Plugins’ “Agents” has an **explicit synonym** statement.
- In scope: cursor.com/docs (plugins, plugins reference, customize, subagents, changelog); help center; GitHub `cursor/plugin-template` agents example; E0 inspect of local `~/.cursor/plugins/**/agents/`.
- Out of scope: Re-researching full Subagents product behavior; forums/E3 as design locks; behavioral harness proving `readonly` enforcement for plugin agents.
- Comprehension / research goal type: adaptive (authoring plugin agents correctly)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebSearch; WebFetch; Shell/Python (list + frontmatter parse under `~/.cursor/plugins`; Cursor `package.json` version); Read (T4D prior note; sample agent files) |
| Corpora / URLs searched | https://cursor.com/docs/reference/plugins.md ; https://cursor.com/docs/plugins.md ; https://cursor.com/docs/customize-cursor.md ; https://cursor.com/docs/subagents.md ; https://cursor.com/changelog/customize ; https://cursor.com/changelog/2-5 ; https://cursor.com/help/customization/plugins ; https://cursor.com/help/ai-features/agent ; https://cursor.com/help/ai-features/multi-agent ; https://raw.githubusercontent.com/cursor/plugin-template/main/plugins/starter-advanced/agents/security-reviewer.md ; GitHub repo listing for plugin-template |
| Queries (exact) | `site:cursor.com/docs plugin agents subagents "agents/" Task tool model readonly` ; `site:cursor.com/docs customize "subagents" Agents plugin synonym OR packages` ; `site:cursor.com/docs/changelog plugin agents subagents` ; `site:cursor.com/help plugin agents subagents` ; `github.com/cursor/plugin-template agents model readonly is_background` ; `site:cursor.com "agents" "subagents" plugin "also known" OR synonym OR "same as" OR "also called" OR "package"` |
| What was *not* searched | Alexandria RAG; community forums as SoT; runtime experiment invoking plugin agent with `readonly: true` to prove write denial; full SDK as plugin SoT (SDK pages hit by search only; IDE plugin load path not documented there for plugins) |
| Provenance (optional PROV) | Entity=Cursor docs + local plugin cache; Activity=Wave3 T4L residual close 2026-07-29; Agent=gatherer-T4L; wasDerivedFrom=T4D note |

### D0 pin

| Field | Value |
|-------|-------|
| Product | Cursor IDE (hosted) — status `in_use` |
| Installed version (E0) | `3.13.25` from `C:\Users\Jonyc\AppData\Local\Programs\cursor\resources\app\package.json` [E0: 2026-07-29] |
| Docs | Live cursor.com/docs + changelog + help — no release-tag pin → skew **unknown** vs build |

### Diátaxis (D2)

| URL | Type | Trust for this residual |
|-----|------|-------------------------|
| `/docs/reference/plugins` | reference | high for plugin Agents format / discovery |
| `/docs/plugins` | how-to + overview | medium (component inventory; local test) |
| `/docs/customize-cursor` | explanation / index | medium (packages “subagents”) |
| `/docs/subagents` | how-to + reference-ish | high for runtime locations / frontmatter; **silent** on plugins |
| `/changelog/2-5` | announcement | medium (plugins package “subagents”) |
| `/help/customization/plugins` | how-to FAQ | medium; **omits** Agents from plugin contents list |

OpenAPI/contracts: **N/A**.

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | as-needed residual close (max effort: close or firmly leave OPEN/GAP) |
| Why this mode | User-scoped Wave 3; do not re-sweep full subagent docs |
| Scope boundary | Two GAPs only; cite-or-omit |

---

## 4. Findings

### GAP-1 — Plugin `agents/*.md` → Subagents / Task / `.cursor/agents/`

#### 1a. Load path & precedence (docs)

- `FACT` [E1] Plugins discover Agents as markdown under `agents/` (or manifest `agents` override). Documented fields: `name`, `description` only. [E1: Plugins reference § Agents format / Component discovery — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Runtime custom subagents are documented only under project/user paths: `.cursor/agents/` (and `.claude/` / `.codex/` variants) and `~/.cursor/agents/` (and Claude/Codex user paths). Precedence: project over user; among same name, `.cursor/` over `.claude/`/`.codex/`. **No plugin install path appears in that table.** [E1: Subagents § File locations — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] Help Agent FAQ: create custom subagents by adding markdown to `.cursor/agents/` — no plugin/`agents/` mention. [E1: https://cursor.com/help/ai-features/agent — accessed 2026-07-29]
- `FACT` [E1] Plugins overview local-test verification sentence names “rules, skills, or MCP servers” — not Agents. [E1: https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `GAP` **Load path / install merge / precedence vs `.cursor/agents/` and `~/.cursor/agents/`** — not stated on official docs/help/changelog pages searched this pass. Searched: plugins.md, reference/plugins.md, subagents.md, customize-cursor.md, changelog/2-5, changelog/customize, help/customization/plugins, help/ai-features/agent, help/ai-features/multi-agent. Result: **searched, not found.**

#### 1b. Runtime Task / Subagents surfacing (E0 only — does not replace docs load path)

- `CLAIM` [E0] On this machine, marketplace/local plugin agent files exist under `~/.cursor/plugins/**/agents/` (11 files observed: create-plugin, cursor-team-kit, thermos, agent-compatibility, continual-learning, grey-matter). [E0: path listing 2026-07-29]
- `CLAIM` [E0] Several of those agent `name` values match Task/subagent-type identifiers available to the IDE agent in this session (e.g. `plugin-architect`, `ci-watcher`, `grey-matter-agent`, thermos `*-subagent` names). This is **runtime presence evidence**, not a documented load algorithm. [E0: session Task `subagent_type` inventory ↔ local `agents/*.md` names — 2026-07-29]
- `INFERENCE` [E4] Plugin Agents are *intended* to become runtime subagents (Task-delegable). Premises: (1) Customize + changelog 2.5 say plugins package **subagents** [E1]; (2) Plugins docs ship an **Agents** / `agents/` component and no separate subagents folder [E1]; (3) E0 name↔Task-type coincidence [E0]. **Not a design lock** — load path/precedence remain GAP.

#### 1c. Whether `model` / `readonly` / `is_background` work on plugin agents

- `FACT` [E1] Plugins reference Agents frontmatter table lists only `name` and `description`. [E1: https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Subagents docs document `model`, `readonly`, `is_background` for custom subagents under `.cursor/agents/` (etc.). [E1: https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] Official `cursor/plugin-template` starter agent (`plugins/starter-advanced/agents/security-reviewer.md`) uses only `name` + `description` — no richer fields. [E1: https://raw.githubusercontent.com/cursor/plugin-template/main/plugins/starter-advanced/agents/security-reviewer.md — accessed 2026-07-29]
- `CLAIM` [E0] Cursor-published cached marketplace plugins **author** richer frontmatter in `agents/`: e.g. `plugin-architect` has `model: inherit`, `readonly: true`; `ci-watcher` has `model: fast`, `is_background: true`; agent-compatibility agents use `model: fast`, `readonly: true`. [E0: frontmatter parse under `~/.cursor/plugins/cache/...` — 2026-07-29]
- `GAP` Official statement that plugin Agents **may** declare / that the IDE **honors** `model` / `readonly` / `is_background` for plugin-sourced agents — **searched, not found** (plugins reference, plugins.md, subagents.md, plugin-template README/agent example, create-plugin scaffold skill text lists Agents as `name`+`description` only). No E0 behavioral proof in this pass that `readonly`/`is_background`/`model` are enforced for plugin-sourced agents (authorship ≠ runtime contract).

**GAP-1 verdict:** **Still open (GAP).** Partial E0/E4 support that Agents map into Task/subagents registry by name; **docs still omit load path, precedence, and richer-frontmatter contract for plugin Agents.**

---

### GAP-2 — Explicit synonym: Customize “subagents” vs Plugins “Agents”

- `FACT` [E1] Plugins docs name the component **Agents** (“Custom agent configurations and prompts”) and folder `agents/`. [E1: https://cursor.com/docs/plugins.md + https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Customize extension table: Plugins “package rules, skills, **subagents**, commands, MCP servers, and hooks”; separate row **Subagents** links to `/docs/subagents`. [E1: https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29]
- `FACT` [E1] Changelog 2.5: “Plugins package skills, **subagents**, MCP servers, hooks, and rules, into a single install.” (Uses “subagents,” not “Agents.”) [E1: https://cursor.com/changelog/2-5 — accessed 2026-07-29]
- `FACT` [E1] Help `/help/customization/plugins` lists plugin contents as Rules, Skills, Commands, MCP servers, Hooks — **omits both Agents and subagents**. Conflicts with plugins.md inventory. [E1: https://cursor.com/help/customization/plugins — accessed 2026-07-29]
- `GAP` **Explicit synonym statement** (e.g. “Agents are also called subagents,” “the Agents component installs as Subagents”) — **searched, not found.** Queries covered docs, help, changelog, and synonym-oriented web search (`also known` / synonym / `same as` / `also called`). Result: parallel packaging labels only; no definitional synonym sentence.

**GAP-2 verdict:** **Still open (GAP)** for *explicit* synonym. Parallel naming remains documented fact (Agents vs subagents across pages); treat as synonym only as **INFERENCE**, not accepted SoT.

---

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 (from T4D) | Plugin `agents/*.md` = distributable custom Subagents (Task-delegable) | still open; E0 strengthens plausibility | Customize/changelog “package subagents” + E0 Task-type names; load path still GAP |
| H2 (from T4D) | Richer frontmatter applies to plugin agents | still open | Marketplace E0 authorship; plugins reference + template omit fields |
| H-syn | “Agents” ≡ “subagents” in product language | still open as synonym claim | Parallel lists; no explicit synonym sentence |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Packaged component name | Plugins: **Agents** [E1 plugins.md] | Customize + changelog 2.5: plugins package **subagents** [E1] | Retain both; synonym **GAP** (no explicit equation) |
| Help plugin contents | Help omits Agents/subagents [E1 help/plugins] | Docs plugins include Agents [E1] | Prefer docs reference for authoring; flag help as incomplete/STALE candidate |
| Frontmatter richness | Plugins Agents: `name`, `description` [E1] | Subagents + marketplace E0: + `model`/`readonly`/`is_background` | Document both surfaces; plugin honor **GAP** |

## 7. Gaps & OPEN (this note)

| ID | Status | Statement |
|----|--------|-----------|
| GAP-1a | **GAP** (confirmed) | Documented load path / merge / precedence of plugin `agents/` vs `.cursor/agents/` / `~/.cursor/agents/` / Task registry — searched, not found |
| GAP-1b | **GAP** (confirmed) | Official contract that `model` / `readonly` / `is_background` are valid and honored on plugin Agents — searched, not found (E0 authorship only) |
| GAP-2 | **GAP** (confirmed) | Explicit Agents ↔ subagents synonym statement — searched, not found |
| Partial | **CLAIM** [E0] only | Plugin agent `name`s appear as Task/subagent types in-session — does **not** close GAP-1a |
| OPEN | optional follow-up | E0 experiment: invoke plugin agent with `readonly: true` and attempt write; record pass/fail. Out of this residual’s max effort. |

### Closed vs still-open (return checklist)

| Residual | Closed? | Notes |
|----------|---------|-------|
| GAP-1 load path / precedence | **Still GAP** | Docs silent; E0 Task-name coincidence only |
| GAP-1 richer frontmatter on plugin agents | **Still GAP** | Docs/template omit; marketplace authors fields |
| GAP-2 explicit synonym | **Still GAP** | Parallel packaging labels only |

**Nothing in this residual fully closed to FACT[E1].**

## 8. Implications (INFERENCE only — not design locks)

- `INFERENCE` [E4] For Toolbelt/plugin authoring: keep dual surfaces — package under `agents/` per plugins reference; assume Task/subagent behavior per subagents.md **only as hypothesis** until product docs state load path. Premises: GAP-1a; H1 open.
- `INFERENCE` [E4] Prefer documenting both labels (“Agents” / “subagents”) rather than collapsing them in SoT text. Premises: GAP-2; conflicts table.

## 9. Source list (deduped)

1. https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29
2. https://cursor.com/docs/plugins.md — accessed 2026-07-29
3. https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29
4. https://cursor.com/docs/subagents.md — accessed 2026-07-29
5. https://cursor.com/changelog/2-5 — accessed 2026-07-29
6. https://cursor.com/changelog/customize — accessed 2026-07-29
7. https://cursor.com/help/customization/plugins — accessed 2026-07-29
8. https://cursor.com/help/ai-features/agent — accessed 2026-07-29
9. https://cursor.com/help/ai-features/multi-agent — accessed 2026-07-29
10. https://raw.githubusercontent.com/cursor/plugin-template/main/plugins/starter-advanced/agents/security-reviewer.md — accessed 2026-07-29
11. https://github.com/cursor/plugin-template — accessed 2026-07-29
12. E0: Cursor `package.json` version `3.13.25` — 2026-07-29
13. E0: `~/.cursor/plugins/**/agents/*.md` listing + frontmatter parse — 2026-07-29
14. Prior: `docs/research/notes/theme-4-cursor-plugins/t4d-agents-subagents.md`

## Stop conditions

- [x] Targeted residual only (no full subagent re-research)
- [x] Each GAP has explicit “searched, not found” or closed claim with citation
- [x] No invented load path / synonym sentence
- [x] Durable research-protocol note written
