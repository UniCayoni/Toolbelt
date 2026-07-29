---
title: "T4N: Residual GAPs — AGENTS.md precedence, plugin packaging, .md dual surfaces"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-T4N]
supersedes: null
campaign: theme-4-cursor-plugins
wave: 3
product: "Cursor IDE"
product_version_in_use: "3.13.25"
prior: docs/research/notes/theme-4-cursor-plugins/t4b-rules-agentsmd.md
aligned_with: docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md
---

# T4N — Residual Rules / AGENTS.md GAP closer

Using `docs-research` + `research-protocol`.

## 1. Scope

- **Question / goal:** Close only these three residuals from T4B §7:
  1. Precedence when `AGENTS.md` conflicts with Team / Project / User rules
  2. Whether plugins can package `AGENTS.md` (not listed as a plugin component)
  3. Project rules ignore plain `.md` in `.cursor/rules` vs plugin `rules/` accepting `.md` — any clarification?
- **In scope:** Official Cursor docs + Help Center linked from `llms.txt`; CLI; enterprise LLM steering; plugins reference.
- **Out of scope:** Forums/E3 as design authority; runtime E0 of rule injection; token-budget GAPs; CLI nested-AGENTS (T4B OPEN, not this pass).
- **Comprehension type:** adaptive (contract clarification for Toolbelt authoring).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch; WebSearch (`site:cursor.com/docs`, `site:cursor.com/help`); Read prior T4B; llms.txt index walk |
| Corpora / URLs searched | See §9 |
| Queries (exact) | `site:cursor.com/docs AGENTS.md precedence Team Project User rules`; `site:cursor.com AGENTS.md plugin rules component package`; `site:cursor.com/docs plugin rules ".md" ".mdc" ignored frontmatter`; `site:cursor.com/help rules AGENTS.md .mdc precedence`; `site:cursor.com "AGENTS.md" "Project Rules" OR "alongside" OR "precedence" OR "conflict"`; `site:cursor.com/docs OR site:cursor.com/help plugin "AGENTS.md"`; `site:cursor.com "rules/" ".markdown" OR "plain .md" plugin frontmatter` |
| What was *not* searched | GitHub issues; changelogs archaeology; Extension API internals; Alexandria RAG; forum threads as authority (E3 discovery only if needed — not used to close) |
| Product pin | Cursor **3.13.25** in use (campaign D0); docs = live cursor.com 2026-07-29; skew **unknown** |
| Stop condition | Exhausted rules.md, Help rules, plugins + reference, customize, CLI using, cloud best-practices/setup, enterprise llm-safety, Help plugins, llms.txt customization/cli links for AGENTS/precedence/.md |
| Provenance (PROV light) | Entity=AGENTS.md/rules precedence docs; Activity=T4N Wave 3 residual fetch+grade; Agent=gatherer-T4N; wasDerivedFrom=T4B + URLs below |

**D0–D14 (docs-research) — condensed:**

| Step | Result |
|------|--------|
| D0 | Cursor IDE `in_use` 3.13.25; live docs accessed 2026-07-29; skew unknown |
| D1 | `https://cursor.com/llms.txt` lists rules, plugins, customize, CLI, Help customization/rules |
| D2 | `rules.md` how-to+explanation; `reference/plugins.md` **reference**; Help rules = how-to FAQ |
| D3 | No OpenAPI; precedence + component tables treated as E1 contracts |
| D5 | No dedicated limitations page for AGENTS↔Team conflict |
| D7 | Waived (official docs/help only; forums not used to close) |
| D10–D13 | Docs as hypotheses; atoms below; OpenAPI N/A |
| D14 | Live docs, no pin — freshness OPEN |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | as-needed residual closer on three named GAPs |
| Why this mode | Wave 3 mission: close residuals only; stop when exhausted |
| Scope boundary | Official docs + Help; no E0 runtime corroboration |

## 4. Findings (per residual)

### 4.1 Residual 1 — AGENTS.md vs Team / Project / User conflict precedence

**Verdict: still GAP** (partial atoms only; conflict order not stated).

- `CLAIM` [E1] Documented cross-type precedence among layered rule sources is only **Team Rules → Project Rules → User Rules**; all applicable rules merge; earlier sources win on conflict. AGENTS.md is **not** named in that ordered list. [E1: Rules — Precedence — https://cursor.com/docs/rules.md — accessed 2026-07-29]; same wording [E1: Help — How do team rules work? — https://cursor.com/help/customization/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] Cursor lists **four** rule types including AGENTS.md as a peer surface (“simple alternative to `.cursor/rules`”), separate from the three-scope precedence bullet. [E1: Rules — intro + AGENTS.md — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] CLI applies root `AGENTS.md` and `CLAUDE.md` **as rules alongside** `.cursor/rules` (merge language; no conflict-order vs Team/User). [E1: CLI using — Rules — https://cursor.com/docs/cli/using.md — accessed 2026-07-29]
- `CLAIM` [E1] Help: Cursor reads `CLAUDE.md` the same way as `AGENTS.md`; `CLAUDE.md` is **always applied to every conversation** (regardless of any `alwaysApply` frontmatter). Conditional control → use project rules in `.cursor/rules/`. [E1: Help — How does CLAUDE.md work — https://cursor.com/help/customization/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] Nested `AGENTS.md` only: instructions combine with parents; **more specific** (deeper) wins — scope is AGENTS↔AGENTS, not Team/Project/User. [E1: Rules — Nested AGENTS.md — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] Enterprise LLM steering documents rules at **three** scopes only (User / Project / Team); does not mention AGENTS.md or a four-way conflict order. [E1: LLM Safety — Rules — https://cursor.com/docs/enterprise/llm-safety-and-controls.md — accessed 2026-07-29]
- `CLAIM` [E1] Cloud best practices list User / Team / Repo (`.cursor/rules/*.mdc`) for conventions; AGENTS.md discussed separately for agent configuration, not in a conflict ladder. [E1: Cloud agent best practices — https://cursor.com/docs/cloud-agent/best-practices.md — accessed 2026-07-29]
- `GAP` Exact precedence when `AGENTS.md` (or `CLAUDE.md`) guidance **conflicts** with Team Rules, Project Rules (`.mdc`), or User Rules. Searched: rules.md precedence + AGENTS.md sections; Help rules (AGENTS / CLAUDE / team precedence); CLI using; customize-cursor; plugins; enterprise llm-safety; cloud best-practices/setup; WebSearch site:cursor.com docs/help. Result: **not found** — no sentence places AGENTS.md into Team→Project→User or states which wins on conflict.
- `INFERENCE` [E4] Treat AGENTS.md as project-local always-on guidance that is **merged** with other applicable rules, but do **not** lock “AGENTS.md ≡ Project Rules tier” or “Team beats AGENTS.md” without a cite. Premises: (1) listed as fourth type / alternative to `.cursor/rules` [E1 rules]; (2) CLI “alongside” `.cursor/rules` [E1 cli]; (3) precedence list omits AGENTS.md [E1 rules/help]; (4) CLAUDE.md always applied [E1 help].

### 4.2 Residual 2 — Can plugins package AGENTS.md?

**Verdict: closed (negative / documented absence).**

- `CLAIM` [E1] Plugin component inventories list Rules, Skills, Agents, Commands, MCP Servers, Hooks — **not** AGENTS.md. [E1: Plugins — What plugins contain — https://cursor.com/docs/plugins.md — accessed 2026-07-29]; [E1: Plugins reference — structure + Component discovery — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]; [E1: Help plugins — What are plugins? — https://cursor.com/help/customization/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Rules are the plugin packaging path: default discovery `rules/` (`.md` / `.mdc` / `.markdown`); optional manifest `rules` field; format examples use `.mdc` + YAML frontmatter. [E1: Plugins reference — Component discovery; Rules format — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Customize treats AGENTS.md as a **workspace Rules** option (project/user/team/`AGENTS.md`), while Plugins are separate distributable bundles of rules/skills/… — no AGENTS.md packaging path. [E1: Customize — Extension components — https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29]
- `GAP` → **closed as absence:** No official doc states that a plugin may ship, discover, or declare root/nested `AGENTS.md` as a first-class plugin component. Exhaustive component tables omit it. Searched: plugins.md, reference/plugins.md, Help plugins, customize-cursor, WebSearch `plugin "AGENTS.md"`. Result: **not listed; use `rules/` instead.**
- `INFERENCE` [E4] For Toolbelt/plugin distribution, ship guidance as plugin **Rules** under `rules/`, not as plugin-bundled `AGENTS.md`. Premises: (1) AGENTS.md absent from all component lists [E1]; (2) Rules is the documented packaging surface [E1 reference].

### 4.3 Residual 3 — Project `.md` ignored vs plugin `rules/` `.md` accepted

**Verdict: clarified (dual surfaces); intentionality still soft OPEN.**

- `CLAIM` [E1] **Project rules surface:** files live in `.cursor/rules` as **`.mdc`**; plain **`.md` is ignored** because it has no frontmatter for `description`, `globs`, and `alwaysApply`; for plain markdown use **AGENTS.md** instead. [E1: Rules — Project rules / Rule file structure — https://cursor.com/docs/rules.md — accessed 2026-07-29]
- `CLAIM` [E1] **Plugin rules surface:** automatic discovery under `rules/` includes all **`.md`, `.mdc`, or `.markdown`** files. [E1: Plugins reference — Component discovery — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Same plugins reference still describes Rules format as **`.mdc` files** that **require YAML frontmatter** (`description`, `alwaysApply`, `globs`); plugins overview table labels Rules as “`.mdc` files”; submission checklist requires proper frontmatter for rules. [E1: Plugins reference — Rules format; Submitting — https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]; [E1: Plugins — What plugins contain — https://cursor.com/docs/plugins.md — accessed 2026-07-29]
- `CLAIM` [E1] Help does not restate the `.md`-ignored project rule; it points authors to `.cursor/rules/` via “New Cursor Rule” / type dropdown (frontmatter-backed application modes). [E1: Help — How do I create a project rule? — https://cursor.com/help/customization/rules.md — accessed 2026-07-29]
- `OPEN` Why plugin discovery accepts `.md`/`.markdown` while project `.cursor/rules` rejects plain `.md` — **no explicit “intentional dual parser” rationale** found in docs/help after search. Practical contract is still clear: different directories/systems; project path requires `.mdc`; plugin path discovers broader extensions but still documents frontmatter-required `.mdc` format.
- `INFERENCE` [E4] Do not collapse the two surfaces into one rule. Prefer `.mdc` + frontmatter for both project and plugin rules; use root/nested `AGENTS.md` only for workspace plain-markdown instructions (not for plugin bundles). Premises: E1 project ignore+AGENTS redirect; E1 plugin discovery vs format/checklist.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H-T4B-2 | AGENTS.md sits outside Team→Project→User or merges as Project-like | **still open** | Precedence omits AGENTS; CLI “alongside”; no conflict cite → Residual 1 GAP |
| H-T4B-1 | Plugin `rules/` `.md` vs project ignore `.md` is dual-surface not contradiction | **revised → clarified** | Both E1 contracts documented; intentionality OPEN |
| H-plugin-AGENTS | Plugins may ship AGENTS.md as a component | **rejected (docs)** | Component tables omit AGENTS.md; Rules is packaging path |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Rule file extensions | Project: `.md` in `.cursor/rules` ignored [E1 rules.md] | Plugin: `rules/` discovers `.md`/`.mdc`/`.markdown` [E1 reference/plugins.md] | **Dual surfaces** — cite both; do not collapse. Prefer `.mdc`+frontmatter for authored rules. Intentionality OPEN. |
| Plugin Rules extension wording | Discovery: `.md`/`.mdc`/`.markdown` [E1 reference] | Format/overview: “`.mdc` files” + require frontmatter [E1 reference/plugins.md, plugins.md] | Prefer **format + checklist** for authoring; discovery may be broader than recommended format. Mark discovery as permissive, format as normative intent. |
| Four types vs three-scope precedence | Four types include AGENTS.md [E1 rules.md] | Precedence only Team→Project→User [E1 rules.md / Help] | **Unresolved for AGENTS conflicts** — Residual 1 remains GAP |

## 7. Gaps & OPEN (this pass)

| # | Item | Status after T4N |
|---|------|------------------|
| 1 | AGENTS.md vs Team / Project / User **conflict precedence** | **still GAP** |
| 2 | Plugin packaging of AGENTS.md | **closed** (not a listed component; use `rules/`) |
| 3 | Project `.md` ignore vs plugin `rules/` `.md` | **clarified** dual surfaces; **OPEN** intentionality only |
| — | Always-on nature of CLAUDE.md (same path as AGENTS.md) | new supporting atom [E1 Help] — does not close #1 |
| — | Docs version skew vs 3.13.25 | OPEN (live docs) |

## 8. Implications (INFERENCE only — not design locks)

- `INFERENCE` [E4] Do not encode “Team beats AGENTS.md” (or the reverse) in Toolbelt SoT until Residual 1 is documented or E0-corroborated. Premises: §4.1 GAP.
- `INFERENCE` [E4] Plugin authors: distribute Cursor rules via `rules/*.mdc` with frontmatter; keep `AGENTS.md` as repo/workspace files, not plugin components. Premises: §4.2 closed absence.
- `INFERENCE` [E4] Never put plain `.md` in project `.cursor/rules` expecting application; use `.mdc` or `AGENTS.md`. For plugins, discovery may pick up `.md`, but ship `.mdc`+frontmatter to match format/checklist. Premises: §4.3.

## 9. Source list (deduped)

1. https://cursor.com/docs/rules.md — accessed 2026-07-29
2. https://cursor.com/help/customization/rules.md — accessed 2026-07-29
3. https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29
4. https://cursor.com/docs/plugins.md — accessed 2026-07-29
5. https://cursor.com/help/customization/plugins.md — accessed 2026-07-29
6. https://cursor.com/docs/customize-cursor.md — accessed 2026-07-29
7. https://cursor.com/docs/cli/using.md — accessed 2026-07-29
8. https://cursor.com/docs/cloud-agent/best-practices.md — accessed 2026-07-29
9. https://cursor.com/docs/cloud-agent/setup.md — accessed 2026-07-29 (AGENTS.md cloud section; no precedence)
10. https://cursor.com/docs/enterprise/llm-safety-and-controls.md — accessed 2026-07-29
11. https://cursor.com/llms.txt — accessed 2026-07-29 (index)
12. Prior: `docs/research/notes/theme-4-cursor-plugins/t4b-rules-agentsmd.md`
13. Campaign D0: `docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md` (3.13.25)

## Self-check

- [x] Method block present
- [x] Every FACT/CLAIM has support
- [x] INFERENCEs list premises
- [x] No invented precedence / APIs
- [x] Conflicts logged
- [x] `status: draft` — not SoT
- [x] Stopped when official docs/help exhausted for the three residuals
