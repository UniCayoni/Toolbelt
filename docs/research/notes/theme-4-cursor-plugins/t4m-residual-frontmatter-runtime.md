---
title: "T4M — Residual frontmatter / runtime GAPs (Wave 3)"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-T4M]
supersedes: null
product: Cursor IDE
cursor_version: "3.13.25"
access_date: 2026-07-29
priors:
  - docs/research/notes/theme-4-cursor-plugins/t4a-plugin-manifest-marketplace.md
  - docs/research/notes/theme-4-cursor-plugins/t4c-skills.md
  - docs/research/notes/theme-4-cursor-plugins/t4h-agentskills-spec-writing.md
  - docs/research/notes/theme-4-cursor-plugins/t4i-github-plugin-skill-patterns.md
aligned_with: docs/research/notes/theme-4-cursor-plugins/d0-cursor-plugins-identity.md
---

# T4M — Residual frontmatter / runtime GAP closer

**Using `docs-research` + `research-protocol`.**

## 1. Scope

- **Question / goal:** Close or re-grade three residual Theme 4 GAPs with cite-or-omit evidence: (1) `displayName` acceptance, (2) Cursor runtime vs Spec-only / community skill frontmatter, (3) enforcement of skill `name` == parent folder.
- **In scope:** cursor.com/docs (+ CLI changelog), agentskills.io Spec + client-impl guidance, cursor/plugins schemas + commits, cursor/plugin-template, high-signal GitHub/forum leads; priors t4a/t4c/t4h/t4i.
- **Out of scope:** E0 IDE smoke (mismatch load / unknown-key ignore); design locks; inventing schema hosting URLs that 500.
- **Comprehension type:** corrective (close OPEN/GAP from Wave 1–2).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch; WebSearch; `gh` / GitHub MCP (`search_issues`, raw contents); Read priors |
| Corpora / URLs searched | https://cursor.com/docs/reference/plugins.md ; https://cursor.com/docs/skills.md ; https://cursor.com/docs/cli/changelog ; https://agentskills.io/specification ; https://agentskills.io/client-implementation/adding-skills-support (raw MDX); https://github.com/cursor/plugins/blob/main/schemas/plugin.schema.json ; https://github.com/cursor/plugin-template ; forum thread 153003 |
| Queries (exact) | `displayName` site:cursor.com / repo:cursor/* ; `allowed-tools` / `user-invocable` owner:cursor ; `Must match the parent` ; changelog skills frontmatter ; agentskills client “warn, load anyway” |
| What was *not* searched | Alexandria RAG; marketplace publish UI re-fetch; full cursor.com/changelog HTML crawl beyond targeted pages; E0 Reload Window skill-mismatch experiment |
| Provenance | Entity←Cursor docs + schemas + Spec + template + forum staff reply; Activity=T4M Wave 3 residual pass 2026-07-29; Agent=gatherer-T4M |

**D0 pin:** Cursor `in_use` build **3.13.25** per campaign D0 / t4c [E0]. Docs = live cursor.com (no release-tag pin) → skew **unknown**.

**D2 Diátaxis (this pass):**

| URL | Type | Trust |
|-----|------|-------|
| plugins.md optional-field table | reference (incomplete vs schema) | high for published docs text; not exhaustive vs schema |
| cursor/plugins `plugin.schema.json` | machine contract (repo) | high for accepted `plugin.json` keys |
| skills.md frontmatter table | reference | high for Cursor-documented skill FM |
| agentskills.io/specification | reference | high for portable Spec |
| agentskills client-impl guide | how-to for *implementers* | high for recommended client leniency; **not** Cursor product SoT |
| CLI changelog | product changelog | high for CLI-documented FM (`user-invocable`) |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | hybrid (targeted residual only) |
| Why | Wave 3 GAP closer; priors already cover surfaces |
| Scope boundary | Three GAPs only; no re-survey of full plugin/skills surface |

## 4. Findings

### 4.1 GAP-1 — `displayName` in `plugin.json` / marketplace

**Verdict: CLOSED** for Cursor schema acceptance of the field. Residual: plugins **docs table** still omits it (docs↔schema drift).

- `FACT` [E1] Live Plugins reference optional-field table still lists `description`, `version`, `author`, `homepage`, `repository`, `license`, `keywords`, `logo`, component paths, `hooks`, `mcpServers`, `variables` — **no** `displayName`. Example manifest also omits it. [E1: https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29]
- `FACT` [E1] Official `cursor/plugins` schema `$id` `https://cursor.com/schemas/cursor-plugin/plugin.json` defines optional `displayName` (string): “Human-readable display name for the plugin.” Schema uses `"additionalProperties": false` and includes `displayName` in `properties` → field is a **first-class accepted key**, not an extension hole. [E1: https://raw.githubusercontent.com/cursor/plugins/main/schemas/plugin.schema.json — accessed 2026-07-29; commit message “Add JSON schemas…” sha `920a87f` 2026-02-11]
- `FACT` [E1] `cursor/plugin-template` README instructs authors to set `displayName` on `plugin.json`; starter manifests include it (e.g. `"displayName": "Simple Starter"`). [E1: https://github.com/cursor/plugin-template README + `plugins/starter-simple/.cursor-plugin/plugin.json` — accessed 2026-07-29]
- `FACT` [E1] Official `cursor/plugins` commit “Add displayName to all plugin manifests” (`7067f9d`, 2026-02-11) added the field across official plugin manifests. [E1: GitHub commit metadata — accessed 2026-07-29]
- `CLAIM` [E3] Third-party commit message (Microsoft azure-sql-database-container #111) asserts Cursor template lists `displayName` and that it is “the human-readable name shown on the marketplace card,” with kebab-case `name` as fallback — **not** Cursor-owned docs. [E3: https://github.com/microsoft/azure-sql-database-container/commit/c64639ce9d03731180560ccca214695892a72fe4 — accessed 2026-07-29]
- `GAP` No cursor.com/changelog page found that narrates “we added `displayName` to the manifest contract.” Searched: WebSearch `site:cursor.com/changelog` plugin/skills/`displayName`; plugins 2.5 / team marketplace pages. Result: product launches mentioned; field-level acceptance not spelled out in changelog prose.
- `GAP` HTTP fetch of schema `$id` URL `https://cursor.com/schemas/cursor-plugin/plugin.json` returned **500** this pass — prefer GitHub raw schema as citeable E1 artifact. Searched: WebFetch 2026-07-29. Result: hosting unreliable; content corroborated via GitHub.
- `FACT` [E1] Marketplace entry schema (`marketplace.schema.json`) does **not** define `displayName` on marketplace plugin entries (entry requires `name`+`source`; optional `description` only in that schema’s `pluginEntry`). Per-plugin UI name remains a `plugin.json` concern in this contract. [E1: https://raw.githubusercontent.com/cursor/plugins/main/schemas/marketplace.schema.json — accessed 2026-07-29]
- `INFERENCE` [E4] t4a C1 (“template-only / OPEN until reference lists it”) is **revised**: acceptance is established by official JSON Schema + template + official plugins usage; docs optional-field table is **stale/incomplete**, not evidence of rejection. Premises: schema FACT; template FACT; docs omission FACT.

### 4.2 GAP-2 — Cursor runtime acceptance of Spec-only / community skill fields

**Verdict: OPEN** for runtime behavior of Spec-only `license`, `compatibility`, `allowed-tools`. **Partial closes** on documentation surfaces for `metadata` (Cursor skills.md) and `user-invocable` (CLI changelog only).

| Field | Spec | Cursor skills.md (IDE docs) | Other Cursor product surface | Runtime honor |
|-------|------|-----------------------------|------------------------------|---------------|
| `license` | optional | absent | not found this pass | **OPEN** |
| `compatibility` | optional | absent | Spec client guide notes model may see it if frontmatter kept | **OPEN** (Cursor) |
| `allowed-tools` | optional, experimental | absent | Spec: “support may vary” | **OPEN** |
| `metadata` | optional | optional (documented) | — | Docs-accepted; runtime semantics still thin |
| `user-invocable` | not in Spec table | absent from skills.md table | CLI changelog documents `user-invocable: false` | CLI-documented; IDE table **GAP** |
| `paths` / `disable-model-invocation` | absent from Spec table | documented | — | Cursor extensions (priors) |

- `FACT` [E1] Cursor skills.md frontmatter table (2026-07-29): required `name`, `description`; optional `paths`, `disable-model-invocation`, `metadata`. No `license`, `compatibility`, `allowed-tools`, `user-invocable`. [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] Agent Skills Spec still lists optional `license`, `compatibility`, `metadata`, `allowed-tools` (experimental; “Support for this field may vary between agent implementations”). [E1: https://agentskills.io/specification — accessed 2026-07-29]
- `FACT` [E1] Cursor CLI changelog documents: set `user-invocable: false` in `SKILL.md` frontmatter to hide a skill from `/` autocomplete and typed `/skill-name` while keeping it available to the model. [E1: https://cursor.com/docs/cli/changelog — accessed 2026-07-29]
- `GAP` IDE skills.md does not list `user-invocable` despite CLI changelog. Searched: skills.md frontmatter table this pass. Result: absent → treat IDE documentation as incomplete relative to CLI.
- `GAP` No Cursor docs page found stating that unknown / Spec-only keys are ignored, stripped, or cause discovery failure. Searched: skills.md; plugins reference Skills format; CLI changelog keywords `allowed-tools`/`license`/`compatibility`. Result: not found.
- `CLAIM` [E3] Community packs (t4i) ship Spec/community keys (`allowed-tools`, `license`, `user-invocable`) without proving Cursor honors them — discovery evidence only. [E3 via E0 in t4i — prior]
- `OPEN` Follow-up still required: E0 local plugin/skill load observing Customize / `/` menu / tool-gating for each Spec-only key. No runtime experiment in this pass.

### 4.3 GAP-3 — Enforcement of skill `name` == parent folder

**Verdict: CLOSED** for **normative Cursor docs** (must match). **OPEN** for whether Cursor **hard-fails** vs **lenient-loads** on mismatch (Vercel-style violation). Spec tooling is strict; Spec *client* guidance recommends warn-and-load.

- `FACT` [E1] Cursor skills.md: `name` “Must match the parent folder name.” [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] Agent Skills Spec: `name` “Must match the parent directory name.” [E1: https://agentskills.io/specification — accessed 2026-07-29]
- `FACT` [E1] Official `skills-ref` validator errors when directory name ≠ skill `name` (`Directory name '…' must match skill name '…'`). [E1: https://raw.githubusercontent.com/agentskills/agentskills/main/skills-ref/src/skills_ref/validator.py — accessed 2026-07-29]
- `FACT` [E1] Agent Skills **client implementation** guide (lenient validation): “Name doesn't match the parent directory name → **warn, load anyway**”; notes Spec is strict and leniency is deliberate for cross-client compatibility. [E1: https://raw.githubusercontent.com/agentskills/agentskills/main/docs/client-implementation/adding-skills-support.mdx — accessed 2026-07-29; HTML: https://agentskills.io/client-implementation/adding-skills-support]
- `FACT` [E1] `cursor/plugin-template` `validate-template.mjs` requires skill frontmatter keys `name` + `description` only — **does not** assert `name` equals parent directory of `SKILL.md`. [E1: https://raw.githubusercontent.com/cursor/plugin-template/main/scripts/validate-template.mjs — accessed 2026-07-29]
- `CLAIM` [E3] Cursor staff (Dean Rie) on forum: “The `name` field has to match the parent folder name exactly. If it doesn’t, Cursor **might** not recognize it as a valid skill.” Soft modality; not a hard-fail guarantee. [E3: https://forum.cursor.com/t/npx-skills-are-not-recognized-as-skills/153003 — accessed 2026-07-29]
- `FACT` [E0] t4i recorded Vercel skill folder `react-best-practices/` with frontmatter `name: vercel-react-best-practices` (Spec violation in the wild). [E0 via t4i prior — 2026-07-29]
- `OPEN` Whether Cursor IDE/CLI currently follows Spec-strict reject, staff “might not recognize,” or Spec client-impl “warn, load anyway” for mismatches — **not E0-tested** this pass.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | `displayName` is an accepted `plugin.json` property in Cursor’s machine schema | **confirmed** | §4.1 schema FACT |
| H2 | Plugins reference optional table is the complete accepted field set | **rejected** | omits schema’s `displayName` (+ schema also has `publisher`/`category`/`tags` not pursued here) |
| H3 | Cursor documents Spec-only `license`/`compatibility`/`allowed-tools` as runtime features | **rejected** | skills.md table |
| H4 | Cursor CLI documents `user-invocable` | **confirmed** | CLI changelog |
| H5 | Cursor hard-rejects `name`≠folder at discovery | **open** | docs MUST + staff “might” + Spec client leniency + no E0 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| C1 `displayName` acceptance | plugins.md optional table omits | official `plugin.schema.json` includes + template/official plugins use | Prefer **schema + official usage** for acceptance; mark docs table **STALE/incomplete**. Closes t4a C1 OPEN for *acceptance*; keeps docs-sync GAP. |
| C2 name↔folder strictness | Spec + Cursor skills.md MUST match; `skills-ref` errors | Spec client-impl: warn, load anyway; template validator skips check; staff “might” | Document both layers: **authoring MUST** vs **client enforcement OPEN**. Prefer E0 for Cursor product behavior. |
| C3 Spec-only FM | Spec defines license/compatibility/allowed-tools | Cursor skills.md omits | Dual surface unchanged (t4c/t4h); runtime still OPEN |

## 7. Gaps & OPEN (residual after this pass)

| ID | Residual | Status |
|----|----------|--------|
| R1 | plugins.md optional-field table / example omit `displayName` despite schema | **GAP** (docs drift) — acceptance itself **CLOSED** |
| R2 | Marketplace card UX semantics of `displayName` (vs schema “human-readable”) | **OPEN** / weak (E3 only for “marketplace card”) |
| R3 | Runtime honor of `license`, `compatibility`, `allowed-tools` in Cursor IDE | **OPEN** (needs E0) |
| R4 | Whether IDE honors `user-invocable` like CLI changelog | **OPEN** / docs GAP |
| R5 | Hard-fail vs lenient load when `name` ≠ parent folder in Cursor | **OPEN** (needs E0); Spec client guide ≠ Cursor SoT |
| R6 | `https://cursor.com/schemas/cursor-plugin/plugin.json` HTTP 500 | **GAP** (hosting); GitHub raw OK |

## 8. Implications (INFERENCE only — not design locks)

- `INFERENCE` [E4] Authors may safely include `displayName` in Toolbelt/`plugin.json` for human-readable labeling; treat plugins.md omission as docs lag. Premises: §4.1 H1/C1.
- `INFERENCE` [E4] Do **not** lock Toolbelt skill design on Cursor enforcing `allowed-tools` / `compatibility` / `license`. Premises: §4.2 OPEN.
- `INFERENCE` [E4] Prefer `name` == folder for Spec/`skills-ref` portability and Cursor docs compliance; do not assume marketplace/community mismatches prove Cursor leniency. Premises: §4.3 C2; Vercel E0 is practice, not Cursor policy.
- `INFERENCE` [E4] If adopting `user-invocable`, cite CLI changelog and verify IDE Customize/`/` behavior with E0 before relying on it in IDE-only workflows. Premises: §4.2 R4.

## 9. Closed vs OPEN summary (return)

| # | Residual GAP (mission) | Result | Notes |
|---|------------------------|--------|-------|
| 1 | `displayName` acceptance | **CLOSED** | Official schema + template + official plugins; changelog silent; docs table still omits |
| 2 | Spec-only / community FM runtime | **OPEN** | `license`/`compatibility`/`allowed-tools` undocumented + untested; `metadata` docs-OK; `user-invocable` CLI-only doc |
| 3 | `name` == folder enforcement | **OPEN** (runtime) / **CLOSED** (docs MUST) | Spec client-impl suggests warn-and-load; Cursor E0 unknown |

**Note path:** `d:\Toolbelt\docs\research\notes\theme-4-cursor-plugins\t4m-residual-frontmatter-runtime.md`

## 10. Source list (deduped)

1. https://cursor.com/docs/reference/plugins.md — accessed 2026-07-29
2. https://cursor.com/docs/skills.md — accessed 2026-07-29
3. https://cursor.com/docs/cli/changelog — accessed 2026-07-29
4. https://raw.githubusercontent.com/cursor/plugins/main/schemas/plugin.schema.json — accessed 2026-07-29
5. https://raw.githubusercontent.com/cursor/plugins/main/schemas/marketplace.schema.json — accessed 2026-07-29
6. https://github.com/cursor/plugins/commit/920a87f3e71e5ee472ebe0441f31ed8004ef14dc — accessed 2026-07-29
7. https://github.com/cursor/plugins/commit/7067f9d3409cf38d6478caa2b1d48396b95ae292 — accessed 2026-07-29
8. https://github.com/cursor/plugin-template — README + starter `plugin.json` + `scripts/validate-template.mjs` — accessed 2026-07-29
9. https://agentskills.io/specification — accessed 2026-07-29
10. https://raw.githubusercontent.com/agentskills/agentskills/main/docs/client-implementation/adding-skills-support.mdx — accessed 2026-07-29
11. https://raw.githubusercontent.com/agentskills/agentskills/main/skills-ref/src/skills_ref/validator.py — accessed 2026-07-29
12. https://forum.cursor.com/t/npx-skills-are-not-recognized-as-skills/153003 — accessed 2026-07-29
13. Priors: t4a, t4c, t4h, t4i under `docs/research/notes/theme-4-cursor-plugins/`
