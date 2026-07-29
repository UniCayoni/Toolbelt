---
title: "T4I — GitHub plugin/skill structural patterns (Wave 2 corroboration)"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-T4I]
supersedes: null
campaign: theme-4-cursor-plugins
wave: 2
access_date: 2026-07-29
aligned_with: docs/research/notes/theme-4-cursor-plugins/t4a-plugin-manifest-marketplace.md
---

# T4I — Public GitHub plugin / skill pack patterns (Wave 2)

**Using `research-protocol`** (E3 discovery + E0 structure observation; E1 for official Cursor/Anthropic GitHub where sampled).

## 1. Scope

- **Question / goal:** Sample high-signal public Cursor plugins / skill packs and extract **structural** patterns that corroborate or challenge Wave 1 Cursor docs (`t4a`–`t4g`). Focus: composition (rules+skills+hooks+mcp), `SKILL.md` quality for low-context agents, README install/test/smoke claims.
- **In scope:** Required repos + 3–5 awesome-list–linked high-signal samples; star counts via GitHub API; path layout / frontmatter / progressive disclosure / hooks·mcp·agents·commands presence.
- **Out of scope:** Re-researching official Cursor docs; deep Agent Skills Spec rewrite (cite **T4H**); inventing marketplace packaging for repos that lack `.cursor-plugin`; runtime E0 install tests in Cursor this pass.
- **Comprehension type:** reuse / corroboration (pattern table for Toolbelt authoring).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | `gh api` (repos, git trees, contents); GitHub MCP `get_file_contents` (awesome README, plugin-template listing); Read Wave 1 notes `t4a`–`t4g` lightly + awareness of sibling Wave 2 `t4h`/`t4k` |
| Corpora / URLs searched | See §9; primary: `cursor/plugin-template`, `spencerpauly/awesome-cursor-skills`, `obra/superpowers`, `getsentry/skills`, `vercel-labs/agent-skills`, `mattpocock/skills`, `anthropics/skills` (structure-only) |
| Queries (exact) | `gh api repos/<owner>/<repo>`; recursive `git/trees/main?recursive=1`; contents of `plugin.json`, `SKILL.md`, hooks, READMEs, `validate-template.mjs`; awesome README Plugins section |
| What was *not* searched | Alexandria RAG; Cursor marketplace binary/blob packaging beyond public GitHub; forums; full Anthropic Spec deep-dive (deferred to T4H); `redhuntlabs/superpower-builder` deep tree (API redirects to `redhuntlabs/wizard`, 8★ — listed but not deep-sampled) |
| Provenance (PROV light) | Entity=public GitHub trees+files; Activity=T4I Wave 2 sample 2026-07-29; Agent=gatherer-T4I; wasDerivedFrom=awesome index + Wave 1 conflict targets |

**Star counts** (`gh api repos/... --jq .stargazers_count`, accessed **2026-07-29**):

| Repo | Stars (2026-07-29) | Role in sample |
|------|-------------------:|----------------|
| `cursor/plugin-template` | 80 | Official Cursor starter (E1 GitHub) |
| `spencerpauly/awesome-cursor-skills` | 629 | Index only (E3) |
| `obra/superpowers` | 263119 | Awesome “Official marketplace” Superpowers + `.cursor-plugin` |
| `getsentry/skills` | 892 | Awesome Sentry skill links; marketplace named in list |
| `vercel-labs/agent-skills` | 29600 | Awesome Vercel skill links |
| `mattpocock/skills` | 194255 | Awesome Matt Pocock skill links |
| `anthropics/skills` | 165010 | Structure-only; Spec depth → **T4H** |
| `redhuntlabs/wizard` (awesome “Superpower Builder”) | 8 | Listed; **not** deep-sampled (low stars / rename) |

**Wave 1 skim (corroboration targets only — not re-researched):** composition inventory + discovery overrides (`t4a`); rules frontmatter (`t4b`); skill frontmatter / progressive disclosure (`t4c`); agents/commands (`t4d`/`t4e`); hooks/MCP paths (`t4f`/`t4g`). Spec dual-surface → **T4H**; testing matrix → **t4k** (sibling; not re-done here).

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | hybrid (fixed required sources + star-preferential awesome sampling) |
| Why | Mission: high-signal corroboration, not exhaustive directory crawl |
| Scope boundary | Public default-branch trees + selected file bodies; no Cursor IDE runtime |

## 4. Findings

### 4.1 Sample inventory (path layout)

#### A. `cursor/plugin-template` (official)

- `FACT` [E1] Multi-plugin marketplace layout: root `.cursor-plugin/marketplace.json` + `plugins/starter-simple` and `plugins/starter-advanced`, each with `.cursor-plugin/plugin.json`. [E1: https://github.com/cursor/plugin-template — tree @ `46216072…` — accessed 2026-07-29]
- `FACT` [E1] README: **starter-simple** = rules+skills only; **starter-advanced** = rules, skills, agents, commands, hooks, MCP, scripts; submission checklist includes `node scripts/validate-template.mjs`. [E1: README.md — accessed 2026-07-29]
- `FACT` [E0] Observed advanced composition paths: `rules/*.mdc`, `skills/*/SKILL.md`, `agents/*.md`, `commands/*.md`, `hooks/hooks.json`, root `mcp.json`, `scripts/`, `assets/logo.svg`. No `references/` under the starter skill. [E0: recursive tree 2026-07-29]
- `FACT` [E1] Both starter `plugin.json` files include `displayName` plus `name`, `version`, `description`, `author`, `license`, `keywords`, `logo` — **no** explicit `rules`/`skills`/… path overrides (auto-discovery). [E1: `plugins/starter-*/.cursor-plugin/plugin.json` — accessed 2026-07-29]

#### B. `obra/superpowers` (marketplace-adjacent, Cursor plugin descriptor)

- `FACT` [E0] Has `.cursor-plugin/plugin.json` with `displayName`, explicit `"skills": "./skills/"`, `"hooks": "./hooks/hooks-cursor.json"` (non-default hooks filename). Also multi-harness manifests (`.claude-plugin/`, `.codex-plugin/`, etc.). [E0: tree + plugin.json 2026-07-29]
- `FACT` [E0] Composition: many `skills/*/SKILL.md`; `hooks/hooks.json` + `hooks/hooks-cursor.json`; `AGENTS.md` at repo root; **no** plugin-level `agents/`, `commands/`, `rules/`, or `mcp.json` in tree sample. Progressive disclosure: `skills/using-superpowers/references/*.md` plus many sibling `.md` files under skills (not only `references/`). [E0: recursive tree 2026-07-29]
- `FACT` [E1] README Cursor install: `/add-plugin superpowers` or marketplace search. [E1: README.md — accessed 2026-07-29]
- `FACT` [E1] `docs/testing.md` documents `tests/` (non-LLM integration) and `evals/` (real LLM sessions; “not part of CI today”). [E1: docs/testing.md — accessed 2026-07-29]

#### C. `getsentry/skills` (awesome + marketplace name; Claude-first packaging)

- `FACT` [E0] **No** `.cursor-plugin/` directory on `main` (API 404). Has `.claude-plugin/plugin.json` (`name`: `sentry-skills`), root `skills/`, `agents/`, `AGENTS.md`. [E0: presence check + tree 2026-07-29]
- `FACT` [E0] Heavy progressive disclosure: **83** blobs under `**/references/` across skills; optional `scripts/`; agents at repo `agents/*.md`. No `hooks/`, `mcp.json`, or plugin `commands/`/`rules/` observed. [E0: tree counts 2026-07-29]
- `FACT` [E1] README install: Claude plugin marketplace + `npx skills add getsentry/skills` (claims Cursor among skills.sh agents). CONTRIBUTING “Testing Skills” = local Claude install → invoke → verify — **manual**, not automated harness. [E1: README.md, CONTRIBUTING.md — accessed 2026-07-29]
- `CLAIM` [E3] Awesome list places **Sentry** under “Official Cursor marketplace plugins” with marketplace URL. [E3: https://github.com/spencerpauly/awesome-cursor-skills README — accessed 2026-07-29] **GAP:** this GitHub repo alone does not show Cursor plugin packaging; marketplace source mapping unverified here.

#### D. `vercel-labs/agent-skills`

- `FACT` [E0] Skill pack (no `.cursor-plugin`). Skills under `skills/*/SKILL.md`; progressive content often as `skills/*/rules/*.md` (120 rule blobs) and some `references/` — **not** Cursor plugin `rules/` component. Extensive `packages/*/test/*.mjs` for optimize tooling; README install `npx skills add vercel-labs/agent-skills`. [E0/E1: tree + README — accessed 2026-07-29]
- `GAP` README does not claim Cursor marketplace plugin install or a Cursor-specific smoke suite beyond skills.sh install. Searched: README Installation/Usage. Result: generic agent install only.

#### E. `mattpocock/skills`

- `FACT` [E0] No `.cursor-plugin`. Nested skill folders (`skills/engineering/*/SKILL.md`); many sibling docs (`tests.md`, etc.); per-skill `agents/openai.yaml` (Codex); **0** `references/` path blobs in tree count. README: Claude plugin + `npx skills add`; setup skill `/setup-matt-pocock-skills`. [E0/E1: tree + README — accessed 2026-07-29]
- `GAP` No automated skill-behavior test suite claimed in the README excerpt reviewed; ADRs under `.agents/adr/` describe shipping as Claude plugin. Searched: README installation sections. Result: install/setup, not CI eval claims.

#### F. `anthropics/skills` (structure only)

- `FACT` [E1] Layout: `skills/<name>/SKILL.md`, `template/SKILL.md`, `spec/`, `skills/skill-creator/`; Claude marketplace install docs in README. No `.cursor-plugin` observed. [E1: README + tree sample — accessed 2026-07-29]
- `CLAIM` [E1] Spec / writing / eval depth for this repo is covered by **T4H** — not duplicated here. [cross-ref: `t4h-agentskills-spec-writing.md`]

#### G. Awesome index + one vendored skill

- `CLAIM` [E3] Awesome distinguishes vendored `resources/*/SKILL.md`, external GitHub skill links, and “Official Cursor marketplace plugins” (Figma, Linear, Sentry, Superpowers, Vercel, …). [E3: awesome README — accessed 2026-07-29]
- `FACT` [E0] Sample vendored skill `resources/systematic-debugging/SKILL.md` frontmatter: `name`, `description`, plus **`user-invocable: true`**. [E0: file contents 2026-07-29]

### 4.2 Pattern table (composition / SKILL quality / testing)

| Pattern | Observed in | Grade | Wave 1 link |
|---------|-------------|-------|-------------|
| Multi-plugin repo + `marketplace.json` + per-plugin `.cursor-plugin/plugin.json` | `cursor/plugin-template` | E1 | Corroborates `t4a` marketplace packaging |
| Single-plugin `.cursor-plugin/plugin.json` at repo root | `obra/superpowers` | E0 | Corroborates `t4a` single-plugin layout |
| Full component set (rules+skills+agents+commands+hooks+mcp) in one plugin | `plugin-template` starter-advanced only | E1 | Corroborates `t4a` inventory; rare in star-heavy community packs |
| Skills-only (or skills+agents) packs **without** Cursor plugin descriptor | `getsentry/skills`, `vercel-labs/agent-skills`, `mattpocock/skills`, `anthropics/skills` | E0 | Challenges assuming “marketplace plugin” ≡ public `.cursor-plugin` on the linked skills repo |
| Explicit manifest path overrides (`skills`, `hooks` → non-default file) | `obra/superpowers` | E0 | Corroborates `t4a` “manifest field replaces discovery” |
| Default auto-discovery (no path fields) | `plugin-template` starters | E1 | Corroborates `t4a` |
| `displayName` in `plugin.json` | template + Superpowers | E1/E0 | Corroborates `t4a` GAP vs reference optional-field table |
| Skill required FM: `name` + `description` (when/trigger keywords) | All sampled SKILL.md | E0/E1 | Corroborates `t4c` / Spec (`T4H`) |
| Spec/Cursor-optional FM: `license`, `metadata`, `allowed-tools`, `disable-model-invocation` | Sentry security-review; Vercel skills; Matt `grill-with-docs` | E0 | Corroborates dual-surface (`t4c`/`T4H`); not in plugins-reference Skills table alone |
| Undocumented/community FM: `user-invocable` | awesome vendored skill | E0/E3 | `OPEN` vs Cursor skills.md |
| Progressive disclosure via `references/` | Superpowers (few), Sentry (heavy), Anthropic (skill-creator pattern per T4H) | E0 | Corroborates `t4c` optional dirs |
| Progressive disclosure via **`rules/` inside skill** (not plugin Rules) | Vercel `skills/*/rules/` | E0 | Challenges Wave 1 soft that skill side files are only `scripts/`/`references/`/`assets/` |
| Sibling markdown (not under `references/`) | Superpowers, Matt Pocock | E0 | Common practical pattern; Spec still prefers named folders (`T4H`) |
| `name` ≠ parent folder | Vercel `react-best-practices/` vs `name: vercel-react-best-practices` | E0 | **Conflict** with Spec “name matches directory” (`T4H`); Cursor strictness `OPEN` |
| Hooks in Cursor plugin | template `hooks/hooks.json`; Superpowers `hooks-cursor.json` via manifest | E1/E0 | Corroborates `t4f` path + events sample (`afterFileEdit`, `beforeShellExecution`, `sessionEnd`, `sessionStart`) |
| Plugin `mcp.json` with `${VAR}` | template starter-advanced | E1 | Corroborates `t4g` / `t4a` variables in MCP |
| Static validate script for marketplace template | `scripts/validate-template.mjs` | E1 | Corroborates `t4a`/`t4k`; requires skill/agent/command `name`+`description`; rules only `description` |
| Real test/eval trees | Superpowers `tests/` + `evals/`; Vercel package unit tests | E1/E0 | Stronger than Cursor docs “tested locally”; still not a Cursor product harness |
| README smoke = manual invoke after install | Sentry CONTRIBUTING; most skill READMEs | E1 | Prefer **GAP** for untested Cursor marketplace behavior |

### 4.3 Frontmatter atoms (examples)

- `FACT` [E1] Template skill: `name`, `description` only; body = when-to-use + numbered instructions (low-context checklist). [E1: `plugins/starter-advanced/skills/code-reviewer/SKILL.md`]
- `FACT` [E1] Template rule always-apply: `description` + `alwaysApply: true`. Globbed rule: `alwaysApply: false` + `globs: ["**/*"]`. [E1: `rules/coding-standards.mdc`, `rules/review-checklist.mdc`]
- `FACT` [E0] Superpowers bootstrap skill: long pushy `description` (“starting any conversation”); body forces skill invocation before other work; points to `references/` for harness adaptation. [E0: `skills/using-superpowers/SKILL.md`]
- `FACT` [E0] Sentry `security-review`: `allowed-tools`, `license` + large `references/` load table by code type. [E0: `skills/security-review/SKILL.md`]
- `FACT` [E0] Sentry `AGENTS.md` authoring law: keep SKILL.md under 500 lines; move refs to `references/`; `name` must match directory; put eval/intent in `SPEC.md`. [E0: `AGENTS.md`]

### 4.4 Testing / smoke claims (README-facing)

- `FACT` [E1] Official template: structural validator + “tested locally” implied by submission checklist wording in README. Does **not** ship LLM eval harness. [E1: plugin-template README + `validate-template.mjs`]
- `FACT` [E1] Superpowers: documented dual test layers; evals slow / not CI. [E1: `docs/testing.md`]
- `FACT` [E1] Sentry: manual Claude local install smoke in CONTRIBUTING. [E1: CONTRIBUTING.md]
- `GAP` No sampled high-star skill pack README claimed an automated **Cursor IDE** plugin load + Hooks/MCP Logs smoke suite. Searched: Superpowers Cursor section, Sentry/Vercel/Matt READMEs, template README. Result: absent or harness-generic.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Wave 1 component inventory (rules/skills/agents/commands/hooks/mcp) appears in real public starters | confirmed | plugin-template starter-advanced |
| H2 | High-star “marketplace” skill repos always ship `.cursor-plugin` | rejected | getsentry/vercel/matt/anthropics lack it; Superpowers has it |
| H3 | Progressive disclosure converges on `references/` only | rejected | Vercel `rules/` under skill; sibling `.md` common |
| H4 | Community packs exceed Cursor plugins-reference frontmatter subset | confirmed | `allowed-tools`, `metadata`, `disable-model-invocation`, `user-invocable` |
| H5 | Public packs commonly automate Cursor plugin testing | rejected | mostly manual / non-Cursor harnesses; template static validate only |

## 6. Conflicts (vs Wave 1 docs notes)

| Topic | Wave 1 / Spec (cite note) | GitHub observation (this pass) | Resolution |
|-------|---------------------------|--------------------------------|------------|
| `displayName` in manifest | `t4a` GAP: in template, absent from reference optional table | Also in Superpowers `.cursor-plugin/plugin.json` | Prefer E0/E1 GitHub presence; docs table incomplete → keep OPEN/GAP |
| Skill side folders | `t4c`: optional `scripts/`, `references/`, `assets/` | Vercel uses `skills/*/rules/`; packs use sibling `.md` | Not a docs contradiction of plugin Rules; document as authoring pattern / Spec soft preference (`T4H`) |
| Skill `name` = directory | Spec via `T4H` / Sentry `AGENTS.md` | Vercel prefixed names ≠ folder | Conflict Spec↔practice; Cursor enforcement `OPEN` |
| Marketplace plugin = GitHub skills repo | `t4a` CLAIM plugins are Git repos | Awesome lists Sentry marketplace; `getsentry/skills` has no `.cursor-plugin` | Cite both; do not equate awesome marketplace row with this repo’s packaging |
| Hooks path | `t4f` / reference: `hooks/hooks.json` | Superpowers uses `hooks/hooks-cursor.json` via manifest `hooks` field | Corroborates override semantics (`t4a`) |
| Testing depth | Docs: local test checklist (`t4a`/`t4k`) | Superpowers/Vercel deeper non-Cursor harnesses | Higher practice bar exists in community; not Cursor product SoT |

## 7. Gaps & OPEN

- `GAP` Mapping from Cursor marketplace plugin IDs (Figma, Sentry, …) → canonical public GitHub repos with `.cursor-plugin` (except Superpowers + official template). Searched: getsentry tree; gh search “sentry cursor plugin”. Result: insufficient.
- `GAP` Whether Cursor accepts Spec-only / community frontmatter (`allowed-tools`, `user-invocable`) or ignores unknown keys. Not runtime-tested.
- `GAP` Whether `name`≠directory breaks Cursor discovery. Not runtime-tested.
- `OPEN` Awesome list marketplace URLs use `cursor.com/cn/marketplace/...` — regional path significance unknown.
- `OPEN` Follow T4H for Spec budgets/writing; t4k for official testing matrix — this note only samples GitHub practice.
- `GAP` `redhuntlabs/superpower-builder` renamed/low-star (`wizard`, 8★) — do not treat as high-signal packaging exemplar without re-check.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] For Toolbelt-as-Cursor-plugin, treat **`cursor/plugin-template` starter-advanced** as the composition scaffold to corroborate Wave 1, and **Superpowers** as the high-signal real-world Cursor marketplace shape (skills + hooks override + `displayName`). Premises: H1; §4.1 A–B.
- `INFERENCE` [E4] Do **not** lock Toolbelt architecture from skills.sh / Claude-plugin repos alone (Sentry/Vercel/Matt) without a Cursor `.cursor-plugin` (or verified marketplace packaging). Premises: H2 rejected; §6 marketplace row.
- `INFERENCE` [E4] Low-context skill quality in the wild favors: trigger-rich `description`, numbered procedures, conditional pointers into `references/` (or equivalent split files), and pushy “when to use” — aligning with `t4c`/`T4H` writing guidance more than with the minimal template skill. Premises: Superpowers/Sentry/Vercel samples.
- `INFERENCE` [E4] Honest smoke story remains: static validate (template / review skill) + local plugin load + manual invoke; LLM evals are optional community practice (Superpowers/Anthropic skill-creator via T4H), not Cursor docs law. Premises: §4.4; t4k.

## 9. Source list (deduped)

1. https://github.com/cursor/plugin-template — accessed 2026-07-29 (stars **80**)
2. https://github.com/spencerpauly/awesome-cursor-skills — accessed 2026-07-29 (stars **629**)
3. https://github.com/obra/superpowers — accessed 2026-07-29 (stars **263119**)
4. https://github.com/getsentry/skills — accessed 2026-07-29 (stars **892**)
5. https://github.com/vercel-labs/agent-skills — accessed 2026-07-29 (stars **29600**)
6. https://github.com/mattpocock/skills — accessed 2026-07-29 (stars **194255**)
7. https://github.com/anthropics/skills — accessed 2026-07-29 (stars **165010**; Spec depth → T4H)
8. Wave 1 notes: `docs/research/notes/theme-4-cursor-plugins/t4a-*.md` … `t4g-*.md` (skim only)
9. Cross-refs: `t4h-agentskills-spec-writing.md`, `t4k-testing-validation.md` (sibling Wave 2; not re-executed)

## Self-check

- [x] Method block present
- [x] Every FACT/CLAIM has support
- [x] INFERENCEs list premises
- [x] No invented APIs
- [x] Conflicts logged when sources disagree
- [x] Star counts dated 2026-07-29
