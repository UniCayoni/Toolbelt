---
title: "T4K — Cursor plugin component testing & validation"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-T4K]
supersedes: null
wave: 2
access_date: 2026-07-29
cursor_version: "3.13.25"
---

# T4K — How can each Cursor plugin component be tested?

**Using `docs-research` + `research-protocol`.**

## 1. Scope

- **Question / goal:** For each Cursor plugin component (Rules, Skills, Agents, Commands, Hooks, MCP, Manifest), what **official** test/debug methods exist, what **community/E3** practices appear, what **E0** Toolbelt/create-plugin practices are observed — and which Wave 1 testing GAPs remain.
- **In scope:** Official Cursor docs (plugins, reference, hooks, skills, mcp, subagents, rules, extension-api, marketplace-security); Agent Skills `skills-ref` (where linked from skill ecosystem); Anthropic `skill-creator` eval loop as **E3/portable** discovery (not Cursor product law); Wave 1 notes Gaps; Toolbelt archive smoke (E0 historical only); create-plugin `review-plugin-submission` skill + plugin-template `validate-template.mjs` (E0/E1 GitHub).
- **Out of scope:** Inventing a Cursor-documented automated harness that does not exist; design locks from draft; treating Claude Code / skill-creator as Cursor IDE SoT; running new runtime smokes this pass.
- **Comprehension / research goal type:** reuse (authoring checklist for Toolbelt plugin QA)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch (plugins.md, reference/plugins.md, hooks.md, mcp.md, extension-api, marketplace-security, subagents.md, agentskills.io/specification, plugin-template README + validate-template.mjs); WebSearch (hooks testing, skill-creator eval); Read (Wave 1 `t4a`–`t4g` Gaps; smoke archive; create-plugin `review-plugin-submission`); Shell path-exists (`~/.cursor/plugins/local`, review skill) |
| Corpora / URLs searched | See §9; D0 pin from `d0-cursor-plugins-identity.md` |
| Queries (exact) | `Cursor IDE hooks testing plugin local test Hooks output channel 2026`; `anthropics skills skill-creator eval evaluation loop GitHub`; `site:cursor.com/docs MCP Logs registerPath plugin test skills-ref validate`; Wave 1 Gaps grep `GAP|testing|validat` |
| What was *not* searched | Alexandria RAG deep crawl; full Cursor changelog; exhaustive forum crawl beyond high-signal hooks threads; E0 live Reload Window smoke of each component this pass; Claude Code product docs as Cursor SoT |
| Provenance (optional PROV) | Entity=Cursor docs + Wave 1 notes + smoke archive + create-plugin cache; Activity=T4K Wave 2 gather; Agent=Cursor gatherer T4K |

**D0 identity (hosted IDE):** Cursor **in_use** build **3.13.25** [E0: `d0-cursor-plugins-identity.md` — Local AppData `package.json` — 2026-07-29]. Docs = live cursor.com (no release tag) → docs↔build skew **unknown** / `GAP`.

**Hard rule this note:** Cite-or-omit; **do not invent** a Cursor test harness the product does not document.

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Wave 1 already mapped components; this pass synthesizes **testing** atoms across official surfaces + cross-links GAPs + light E3/E0 |
| Scope boundary | Plugin components as listed in plugins inventory; AGENTS.md only where Wave 1 noted validator GAP |

## 4. Findings

### 4.1 Shared official local-test path (all components)

- `FACT` [E1] Before publish: copy/symlink plugin under `~/.cursor/plugins/local/<name>`, ensure `.cursor-plugin/plugin.json` at plugin root, Restart or **Developer: Reload Window**, “Verify your plugin components load in Cursor, such as rules, skills, or MCP servers.” [E1: Plugins §Test plugins locally — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Submission checklist includes “Plugin has been tested locally” plus manifest/frontmatter/path/variables checks. [E1: Plugins reference §Submission checklist — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Extension API `vscode.cursor.plugins.registerPath(path)` registers a directory so Cursor discovers plugins without copying to `~/.cursor/plugins/local/`; manifest optional (folder discovery still applies). [E1: Extension API — Plugin paths — https://cursor.com/docs/extension-api — accessed 2026-07-29]
- `CLAIM` [E1] Marketplace listing requires open source + **manual** Cursor team review (security, data handling, quality); updates also manually reviewed — **not** an author-run automated harness. [E1: Marketplace security — https://cursor.com/help/security-and-privacy/marketplace-security.md — accessed 2026-07-29]
- `FACT` [E0] Toolbelt + grey-matter present under `C:\Users\Jonyc\.cursor\plugins\local\` (path listing 2026-07-29). [E0: Shell listing]

### 4.2 Per-component testing matrix

Columns: **Official method (E1)** | **Community / E3** | **E0 observed** | **GAP** (Wave 1 cross-link + this pass)

| Component | Official method (E1) | Community / E3 | E0 observed | GAP |
|-----------|----------------------|----------------|-------------|-----|
| **Rules** | Local plugin load + verify components; Customize manage/toggle rule modes; Rules FAQ: check type, description for Apply Intelligently, globs match. Checklist: frontmatter on rules. [E1: plugins.md; rules.md via Wave 1 t4b; reference checklist] | No strong Cursor-official CLI rules linter found in this pass’s search. Forum/E3 not used for locks. | Toolbelt `.mdc` frontmatter examples; create-plugin quality-gate rule requires YAML frontmatter [E0: t4b §4.9; create-plugin cache]. Smoke archive: cold-start / coexistence prompt scoring for rule/skill auto-fire — **harness practice, not Cursor product law** [E0: `docs/archive/smoke/`]. | **t4b GAP:** no automated schema validator / CLI lint / CI for `.mdc` or AGENTS.md beyond manual local test + FAQ. |
| **Skills** | Local load; Customize → Skills / Agent Decides; invoke `/skill-name`; checklist frontmatter. Portable Agent Skills spec: `skills-ref validate ./my-skill` checks frontmatter/naming [E1: plugins.md; skills.md via t4c; https://agentskills.io/specification — accessed 2026-07-29]. | Anthropic **skill-creator** eval/improve/benchmark loop (`evals/evals.json`, with/without skill subagents, graders, `run_loop.py`) — **Claude/skill ecosystem**, not Cursor-documented IDE harness [E3: https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md — accessed 2026-07-29]. Community writeups of skill-creator (Medium/DEV) = discovery only. | review-plugin-submission checks `skills/*/SKILL.md` + `name`/`description` frontmatter [E0: create-plugin skill]. plugin-template `validate-template.mjs` requires skill frontmatter `name`+`description` [E1 GitHub: cursor/plugin-template]. Smoke v1–v4b: skill usability / announce / auto-fire scoring [E0: smoke archive]. | **t4c GAP:** no Cursor-docs automated skill unit-test / golden-prompt / CI runner beyond local load + `skills-ref` / template validator. |
| **Agents** | Local plugin load + checklist “tested locally.” Subagents best practices: refine `description`; “Test by making prompts and checking if the right subagent gets triggered”; FAQ: invoke explicitly with a simple task. [E1: plugins.md; https://cursor.com/docs/subagents.md §Best practices / FAQ — accessed 2026-07-29] | Forum threads on hook/subagent firing = E3 discovery (e.g. when `subagentStart` does not fire because no Task spawn) — not product test API. | create-plugin ships agent markdown with richer frontmatter than plugins Agents format table documents [E0: t4d]. review-plugin-submission: agents need `name`+`description` [E0]. | **t4d GAP:** no automated harness/schema validator for agent/subagent markdown; plugin agents ≡ project subagents load path still GAP. |
| **Commands** | Shared local plugin load + checklist frontmatter. Example verify sentence in plugins.md names rules/skills/MCP — **not** commands explicitly. [E1: plugins.md; reference Commands format] | No dedicated community CLI found this pass. | review-plugin-submission + validate-template require command frontmatter `name`+`description` [E0/E1]. | **t4e GAP:** command-specific testing / `/` smoke procedure not documented; E0 `/` listing OPEN in Wave 1. |
| **Hooks** | Troubleshooting: **Hooks tab** in **Customize** + **Hooks output channel** to debug configured/executed hooks and errors; config reload on save / restart; relative paths. Third-party hooks: exit `2` to block; check JSON; Hooks output channel; “Test your hooks in both tools” (Claude↔Cursor). Plugin hooks covered by local plugin path. [E1: https://cursor.com/docs/hooks.md §Troubleshooting — accessed 2026-07-29; third-party-hooks.md via t4f] | egghead: Output → Hooks dropdown shows INPUT/OUTPUT JSON [E3: egghead.io lesson]. Forum: View→Output→Hooks; Settings→Hooks→Execution Logs (last 100); disk log `cursor.hooks.log` under Cursor logs [E3: forum.cursor.com/t/unstable-cursor-hooks/162988 — discovery only]. | Wave 1 t4f confirmed debug UI wording; **no** Cursor-documented unit harness. validate-template only **warns** if `hooks/hooks.json` missing (optional). | **t4f GAP (high):** no official automated test / stdin fixture / `cursor hooks test` CLI — UI debug + manual event trigger only. |
| **MCP** | Local load verifies MCP servers load; Output → **MCP Logs** (init, tool calls, errors); Customize toggle enable/disable; checklist variables/`${VAR}` match. CLI: `agent mcp list` / tools / login / enable / disable (CLI docs cited in t4g). `vscode.cursor.mcp.registerServer` for programmatic registration (not a test runner). [E1: mcp.md FAQ; plugins.md; extension-api; t4g] | Community MCP test servers / images example linked from docs is implementation sample, not plugin CI. | validate-template warns if no `mcp.json` (optional); does **not** schema-validate MCP protocol. review-plugin-submission checks `mcp.json` / `mcpServers` path presence. | **t4g GAP:** no automated MCP schema validator / plugin MCP unit-test harness / CI beyond checklist + MCP Logs. |
| **Manifest** | Valid `.cursor-plugin/plugin.json`; kebab-case unique `name`; relative paths (no `..`, no absolute); variables schema vs `${VAR}`; multi-plugin `marketplace.json`; “tested locally.” [E1: reference submission checklist] | — | **plugin-template** `node scripts/validate-template.mjs`: JSON parse, name patterns, path safety, frontmatter on rules/skills/agents/commands, marketplace↔plugin name match [E1: https://raw.githubusercontent.com/cursor/plugin-template/main/scripts/validate-template.mjs — accessed 2026-07-29]. **review-plugin-submission** skill: pass/fail checklist mirroring discovery + metadata [E0: create-plugin cache]. Toolbelt `plugin.json` present under workspace / local plugin [E0]. | **t4a GAP:** no docs-site IDE “plugin validator” UI; template script is repo-local, not documented on cursor.com/docs as product command. Publish form fields weak via WebFetch. |

### 4.3 Cross-link — Wave 1 testing GAPs (verbatim themes)

| Wave 1 note | Testing-related GAP (summary) |
|-------------|-------------------------------|
| [t4a](./t4a-plugin-manifest-marketplace.md) | No docs-site automated local validator; Reload + manual check (+ template script off-site). |
| [t4b](./t4b-rules-agentsmd.md) | No automated validation tooling for rules/AGENTS.md. |
| [t4c](./t4c-skills.md) | No dedicated Cursor skill automated testing beyond local load / Customize. |
| [t4d](./t4d-agents-subagents.md) | No automated test harness for agents beyond local load + prompt-trigger checks. |
| [t4e](./t4e-commands.md) | Command-specific testing / verification procedure missing. |
| [t4f](./t4f-hooks.md) | No dedicated how-to-test-hooks; no unit harness / CLI / golden stdin fixtures. |
| [t4g](./t4g-mcp-in-plugins.md) | No formal automated plugin MCP testing beyond load + MCP Logs + checklist. |

### 4.4 E0 — create-plugin review skill (checklist claims only)

- `FACT` [E0] `review-plugin-submission` skill exists at create-plugin cache path; workflow verifies manifest JSON/name, component discovery paths, frontmatter (`name`/`description` for skills/agents/commands; rules frontmatter), marketplace registration, README; output = pass/fail by section. [E0: `C:\Users\Jonyc\.cursor\plugins\cache\cursor-public\create-plugin\45c66fde1f1681a902a30d1ae8bca1cc64465d6e\skills\review-plugin-submission\SKILL.md` — observed 2026-07-29]
- `INFERENCE` [E4] This skill is a **static submission audit**, not a runtime agent/hooks/MCP execution test. Premises: skill checklist text; no mention of Hooks channel / MCP Logs / Reload Window in that skill body.

### 4.5 E0 — Toolbelt smoke archive (historical practices ≠ Cursor law)

- `FACT` [E0] Archive documents human/agent smoke trials of elevated skills/rules (v1–v4b): usability, process gaps, coexistence, cold-start auto-fire scoring. [E0: `d:\Toolbelt\docs\archive\smoke\README.md` and summaries]
- `FACT` [E0] Smoke recon noted Superpowers `docs/testing.md` claiming `evals/` + `npm test` while tree lacked them — example of **docs↔tree** contradiction discipline, not a Cursor plugin test API. [E0: smoke-trial / v3 research-note-harness]
- `INFERENCE` [E4] Useful Toolbelt pattern: Method envelope + graded claims + path-exists helpers for harness QA; **must not** be cited as Cursor product testing law. Premises: smoke README purpose statement; PROTOCOL cite-or-omit.

### 4.6 skill-creator (E3 portable — do not lock as Cursor)

- `CLAIM` [E3] Anthropic skill-creator documents eval prompts, with/without-skill baselines, graders, benchmark aggregation, description optimization loop (`run_loop.py`). [E3: anthropics/skills skill-creator SKILL.md — accessed 2026-07-29]
- `GAP` Cursor docs do **not** document shipping or requiring skill-creator (or any equivalent) for marketplace plugins. Searched: skills.md, plugins.md, reference checklist. Result: absent → treat as optional external practice only.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Cursor documents a first-party automated plugin/component test harness (CLI or CI) | **rejected** | Shared path = local load + manual verify; component debug = Hooks channel / MCP Logs / prompt triggers; template validator is static GitHub script |
| H2 | Official “tested locally” means Reload Window + Customize visibility, not golden evals | **confirmed (docs)** | plugins.md Test section + checklist wording |
| H3 | skill-creator evals are applicable as optional author practice for Skills quality | **open / E3 only** | Portable ecosystem; not Cursor SoT |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| “How to test” depth | Plugins: one shared local path [E1] | Hooks/MCP: dedicated **debug** channels [E1]; Subagents: prompt-trigger tests [E1]; Commands/Rules: thinner [E1 Wave 1] | Prefer per-component surfaces; do not invent uniform harness |
| Skill validation | Cursor: local load [E1] | agentskills.io: `skills-ref validate` [E1 portable] | Cite both; Cursor does not claim `skills-ref` as IDE product feature |
| Template validate vs docs site | plugin-template README requires `validate-template.mjs` [E1 GitHub] | cursor.com/docs checklist omits that script [E1] | Template = authoring aid; docs checklist = marketplace prose; both E1 different surfaces |

## 7. Gaps & OPEN (ranked)

Priority = impact on Toolbelt plugin authoring / Wave 2 validation planning.

1. **P0 — Hooks:** No official automated / fixture-based hooks test protocol (t4f). Only Hooks tab + output channel + manual triggers.
2. **P0 — Commands:** No command-specific verify procedure (t4e); plugins.md verify examples omit commands.
3. **P1 — Rules / AGENTS.md validators:** No official CLI/schema lint (t4b).
4. **P1 — Skills behavioral evals in Cursor:** No Cursor golden-prompt / CI runner (t4c); skill-creator is external E3.
5. **P1 — Agents:** No automated agent markdown harness; plugin↔subagent wire-up still GAP (t4d).
6. **P1 — MCP:** No automated `mcp.json` / protocol validator for plugins (t4g); MCP Logs only.
7. **P2 — Manifest IDE validator:** Docs site has no product validator UI; rely on template script / review skill (t4a).
8. **P2 — Docs↔3.13.25 skew:** Live docs, no tag (D0 / all Wave 1 notes).
9. **OPEN — E0 runtime corroboration:** This pass did not Reload Window and observe each component load for Toolbelt; treat local path existence as install E0 only.

## 8. Implications (INFERENCE only — not design locks)

- `INFERENCE` [E4] A honest Toolbelt “plugin test plan” today is: (1) static checks via `validate-template.mjs` and/or `review-plugin-submission`; (2) optional `skills-ref validate` for skills; (3) local install + Reload; (4) component debug UIs (Hooks / MCP Logs); (5) manual prompt triggers for skills/agents/commands/rules. Premises: §4.1–4.2 matrix; rejected H1.
- `INFERENCE` [E4] Do **not** claim Cursor provides skill-creator-style eval loops or hooks unit tests in product docs. Premises: §4.6 GAP; t4f GAP.
- `INFERENCE` [E4] Marketplace “manual review” is Cursor’s quality gate, not a substitute author can run locally. Premises: marketplace-security.md.

## 9. Source list (deduped)

1. https://cursor.com/docs/plugins.md — accessed 2026-07-29  
2. https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29  
3. https://cursor.com/docs/hooks.md — accessed 2026-07-29  
4. https://cursor.com/docs/mcp.md — accessed 2026-07-29  
5. https://cursor.com/docs/skills.md — accessed 2026-07-29 (via Wave 1 + WebSearch)  
6. https://cursor.com/docs/subagents.md — accessed 2026-07-29  
7. https://cursor.com/docs/extension-api — accessed 2026-07-29  
8. https://cursor.com/help/security-and-privacy/marketplace-security.md — accessed 2026-07-29  
9. https://cursor.com/docs/reference/third-party-hooks.md — via Wave 1 t4f  
10. https://agentskills.io/specification — accessed 2026-07-29  
11. https://raw.githubusercontent.com/cursor/plugin-template/main/README.md — accessed 2026-07-29  
12. https://raw.githubusercontent.com/cursor/plugin-template/main/scripts/validate-template.mjs — accessed 2026-07-29  
13. https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md — accessed 2026-07-29  
14. Wave 1 notes: `t4a`–`t4g` under this directory — Gaps sections  
15. `d0-cursor-plugins-identity.md` — Cursor 3.13.25 pin  
16. E0: create-plugin `review-plugin-submission/SKILL.md`  
17. E0: `d:\Toolbelt\docs\archive\smoke\`  
18. E3 discovery: egghead Hooks output panels; forum.cursor.com/t/unstable-cursor-hooks/162988  

## Stop conditions (docs-research)

- [x] D0 version pin recorded (3.13.25 in_use; docs live / skew unknown)  
- [x] Reference/contracts used for checklist + debug surfaces  
- [x] Limitation/GAP path done (Wave 1 cross-link + ranked §7)  
- [x] Conflicts logged  
- [x] No design lock on uncorroborated E3 (skill-creator / forum)  
- [x] Durable findings in this `research-protocol` note  
