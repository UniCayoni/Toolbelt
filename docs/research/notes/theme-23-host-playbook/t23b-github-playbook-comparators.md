---
title: "T23B-gh — GitHub playbook / host-guide comparators"
status: draft
theme: theme-23-host-playbook
created: 2026-08-04
updated: 2026-08-04
authors: [T23B-gh]
supersedes: null
depth: deep
wave: 1
gatherer_id: T23B-gh
---

# T23B-gh — GitHub playbook / host-guide comparators

**Using `research-protocol`**. Depth: **deep**. Cite-or-omit. **Draft ≠ Toolbelt law.**

## 1. Scope

- Question / goal: How do other skill packs, agent plugins, and developer toolkits document **host adoption / use** (getting started, playbook, operator guide, skill catalogs with intent/limits)? What structures transfer to a Toolbelt host playbook without importing third-party process as SoT?
- In scope: Public GitHub primary files (README, AGENTS.md, skill meta, host docs); Cursor plugin host-facing READMEs; progressive disclosure / start-here vs reference splits; maintenance notes when present.
- Out of scope: Ansible/infra “host playbook” false positives; copying Superpowers/OWK/Prisma workflows as Toolbelt methodology; Theme 13 contributor CI; Theme 24 learn-back; inventing undocumented repos.
- Comprehension / research goal type: reuse (comparator patterns for playbook craft).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-04 |
| Tools used | `gh` CLI (`gh search`, `gh api` raw contents); GitHub MCP `user-github` (`get_file_contents`, `search_code`, `search_repositories`); local read of installed Cursor plugin cache README for `create-plugin` |
| Corpora / URLs searched | GitHub repos listed in Source list; no Alexandria RAG in this gatherer |
| Queries (exact) | `gh search repos "superpowers skills"`; `gh search repos "skills AGENTS.md"`; `gh search repos "cursor skills plugin"`; `gh search repos "anthropics skills"`; `gh search repos "agentskills"`; `gh search code "using-superpowers" --owner obra`; `gh search code "Getting started" … AGENTS.md skills`; MCP `search_code` `"when to use" OR "when NOT" path:skills filename:SKILL.md`; MCP `search_code` playbook/host-guide phrases (low signal / Ansible false positives) |
| What was *not* searched | Private/internal Cursor marketplace source trees; Discord; non-GitHub package registries; full clone of every fork of superpowers; web/RAG channels (sibling gatherers T23B-web / T23B-RAG) |
| Depth | deep |
| Waves / stop_reason | Wave 1 gatherer. Stop for this note: diminishing returns after ~9 solid host-facing hits + repeated structural patterns (install → bootstrap/meta entry → workflow map → catalog → contributor split); further forks add little new structure. |
| Provenance (optional PROV) | Entity←listed repo paths; Activity=gh/MCP fetch 2026-08-04; Agent=T23B-gh |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Seed list from campaign brief + discovery searches; deep-read only high-signal host docs |
| Scope boundary | README / AGENTS.md / host docs / meta skills / plugin manifests; not full skill bodies except where they define host bootstrap or catalog shape |

## 4. Findings

### 4.1 Comparator table

| Repo | Host-facing surfaces (paths) | Start-here vs reference | Catalog / intent·limits | Maintenance notes | Grade |
|------|------------------------------|-------------------------|-------------------------|-------------------|-------|
| [obra/superpowers](https://github.com/obra/superpowers) | `README.md`; `skills/using-superpowers/SKILL.md`; per-harness `docs/README.*.md`; `.cursor-plugin/plugin.json` | README: Quickstart → per-harness **Installation** → **Basic Workflow** → **What's Inside** catalog. Meta skill is session bootstrap. Deep porting in `docs/porting-to-a-new-harness.md` (contributor/porter, not consumer). | Skills grouped (Testing / Debugging / Collaboration / Meta) with one-line purpose. Workflow lists ordered skill chain. | Porting guide: “when this guide and the code disagree, the code wins; fix the guide.” Updating section: harness-dependent / often automatic. | **E1** |
| [anthropics/skills](https://github.com/anthropics/skills) | `README.md`; `template/SKILL.md`; `skills/*` | README = concept + install (Claude Code / Claude.ai / API) + “Creating a Basic Skill”; points out to support docs for “using skills.” Spec/template under `spec/`, `template/`. | Skill sets listed by folder; template requires `description` with **what + when to use**. Disclaimer: demo/educational; behaviors may differ. | No explicit host-playbook drift contract in README. | **E1** |
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | `README.md`; `docs/home.mdx`; `docs/skill-creation/*` | Getting started cards → Quickstart vs Specification. Progressive disclosure is **first-class** (discovery → activation → execution). | Authoring docs: keep `SKILL.md` lean; push depth to `references/` with **when-to-load** pointers; description is trigger surface. | Open-standard contrib via `CONTRIBUTING.md` (not host-consumer maintenance). | **E1** |
| [bluecoast1379/open-workflow-kit](https://github.com/bluecoast1379/open-workflow-kit) | `README.md`; `docs/tool-install-recipes.md`; `docs/shareable-install.md`; `docs/release-checklist.md`; `docs/maintainer-handoff.md` | 30s dry-run → 快速开始 → define-done → evidence → command path. Platform table with **honest** `native_not_yet_manually_certified`. | Commands/capabilities as inventory; core vs adapters vs examples. | Explicit maintainer/release/checklists; “通用规则只改 `workflow/core/`”; upgrade path that does not overwrite team-profile. | **E1** |
| [smillunchick/dev-cascade](https://github.com/smillunchick/dev-cascade) | `README.md`; `agents.md` | Install (Claude vs other agents) → cascade ASCII → skill table → Superpowers dependency table. Non-Claude: paste `agents.md` into rules/AGENTS. | Table: skill → what it does; separate tables for bundled deps and Superpowers handoffs. | Thin; no durable inventory-update contract observed in README. | **E1** |
| [prisma/prisma](https://github.com/prisma/prisma) | `AGENTS.md`; `docs/onboarding/*` incl. `Common-Tasks-Playbook.md` | **Start Here** link pack → modular onboarding → golden rules → where skills/rules live (canonical vs symlinks). Playbook = task → plan/rule pointers. | Skills SoT path + CI lint (`pnpm lint:skills`); rules index; not a marketing catalog. | Golden rule “Keep docs current”; `.agents/rules/doc-maintenance.mdc` referenced; prepare hook wires skills after install. | **E1** |
| [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | `AGENTS.md` | Project summary → layout table → Agent Skills path → build/test → **Docs site mounts** (editing listed files changes public site). | Points at `.agents/skills/` per Agent Skills spec; human SoT = CONTRIBUTING + docs. | Explicit: listed README paths mount into Hugo site — treat as documentation. | **E1** |
| [imwebme/imweb-ai-toolkit](https://github.com/imwebme/imweb-ai-toolkit) | `.cursor-plugin/README.md`; `docs/skill-installation-and-usage.md`; `docs/surface-support-matrix.md` | Connection order: CLI → skill docs → plugin/MCP metadata. **When To Use This** + Notes (limits: no bundled MCP; manual Cursor setup). | Surface-support matrix for scope honesty. | Manual-setup honesty itself is a maintenance stance (don’t claim auto-install). | **E1** |
| Cursor `create-plugin` (local plugin cache) | Installed README under Cursor plugins cache | Install `/add-plugin` → Components tables (skills/rules/agents/commands) → Typical flow (3 steps). | Compact catalog tables with one-line descriptions. | Not observed in short README. | **E0** (local plugin artifact; not re-fetched from a public git URL in this pass) |

`GAP`: Dedicated public “Cursor official create-plugin” GitHub repo was **not** located via `gh search` in this pass; used installed plugin README as E0 only.  
`GAP`: Phrase search for `"host playbook"` on GitHub overwhelmingly hit Ansible/Sentinel ops docs — not agent skill packs (false friends).

### 4.2 Structural patterns (labeled)

- `FACT` [E1] **obra/superpowers** host README separates consumer install/workflow/catalog from contributor `AGENTS.md`/`CLAUDE.md` (contributor = PR rejection / harness port rules). [E1: obra/superpowers `README.md`, `AGENTS.md` — accessed 2026-08-04]
- `FACT` [E1] Superpowers uses a dedicated **meta bootstrap skill** (`using-superpowers`) injected/loaded at session start; README states skills “trigger automatically” / agent checks for relevant skills before tasks. [E1: `skills/using-superpowers/SKILL.md`, `README.md` — accessed 2026-08-04]
- `FACT` [E1] Superpowers README “What's Inside” is a **grouped skill catalog** with short intent blurbs, not full skill bodies. [E1: `README.md` §§ The Basic Workflow, What's Inside — accessed 2026-08-04]
- `FACT` [E1] Superpowers porting guide layers: invariants first, then procedure; states guide vs code conflict → **code wins, fix guide**. [E1: `docs/porting-to-a-new-harness.md` — accessed 2026-08-04]
- `FACT` [E1] **agentskills** documents three-stage **progressive disclosure** (discovery name/description → activate SKILL.md → execute + optional references). Authoring best practices: lean SKILL.md, depth in `references/` with **when-to-load** instructions. [E1: `README.md`, `docs/home.mdx`, `docs/skill-creation/best-practices.mdx` — accessed 2026-08-04]
- `FACT` [E1] **anthropics/skills** template frontmatter: `description` = what the skill does **and when** to use it; README disclaimer separates demo skills from production Claude behavior. [E1: `template/SKILL.md`, `README.md` — accessed 2026-08-04]
- `FACT` [E1] **open-workflow-kit** README leads with choose-project table, dry-run quickstart, then deep contract/evidence docs; platform adapter table includes explicit non-certification status. Maintainer docs live under `docs/` (release checklist, handoff). [E1: `README.md`, `docs/*` listing — accessed 2026-08-04]
- `FACT` [E1] **dev-cascade** documents a cascade map + skill purpose table + dependency handoffs; offers a single `agents.md` paste path for non-Claude hosts. [E1: README, `agents.md` head — accessed 2026-08-04]
- `FACT` [E1] **prisma/prisma** `AGENTS.md` “Start Here” points to docs index + onboarding + **Common Tasks Playbook** (task → plan/rule pointers); documents canonical skill/rule paths vs presentation symlinks and post-install wiring. [E1: `AGENTS.md`, `docs/onboarding/Common-Tasks-Playbook.md` — accessed 2026-08-04]
- `FACT` [E1] **agent-sandbox** AGENTS.md separates human SoT docs from agent skills path and warns that some README edits publish via Hugo mounts. [E1: `AGENTS.md` — accessed 2026-08-04]
- `FACT` [E1] **imweb-ai-toolkit** Cursor plugin README is a short **connection order + when to use + limits** card pointing to deeper skill install docs and a support matrix. [E1: `.cursor-plugin/README.md` — accessed 2026-08-04]
- `FACT` [E0] Installed **create-plugin** README is a minimal host card: install command, component catalog tables, 3-step typical flow. [E0: local Cursor plugin cache `create-plugin` README — accessed 2026-08-04]
- `INFERENCE` [E4] High-signal host guides repeatedly use the same stack: **(1) install per surface**, **(2) one entry/meta path**, **(3) short workflow map**, **(4) compact catalog with intent**, **(5) deep reference elsewhere**, **(6) separate contributor docs**. Premises: Findings on superpowers, agentskills, OWK, prisma, create-plugin, imweb.
- `INFERENCE` [E4] Explicit **limits / non-goals / non-certification** statements appear in stronger host docs (anthropics disclaimer, OWK certification status, imweb manual-setup notes) and reduce over-claim. Premises: those E1 rows.
- `CLAIM` [E3] Community skill-router / cascade packs often compose Superpowers and document dependency tables; structure is useful, but quality and maintenance vary widely — treat as discovery, not design lock. [E3: e.g. smillunchick/dev-cascade README dependency on Superpowers — accessed 2026-08-04]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Best host guides put install + entry skill + workflow map in start-here; full skill bodies stay progressive/reference | confirmed | superpowers README + using-superpowers; agentskills progressive disclosure; create-plugin / imweb short cards |
| H2 | Contributor AGENTS.md is often mistaken for host playbook; strong packs split them | confirmed | superpowers README vs AGENTS.md; agent-sandbox AGENTS.md vs CONTRIBUTING; prisma AGENTS.md is host+agent onboarding (repo-native), still not a plugin marketplace card |
| H3 | Maintenance contracts appear more in mature kits (OWK checklists, prisma doc-maintenance, superpowers “code wins”) than in small cascade READMEs | confirmed | OWK docs/*; prisma AGENTS.md; superpowers porting guide vs thin cascade README |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Skill auto-trigger vs opt-in | Superpowers: mandatory skill check / session bootstrap injection | Anthropics/agentskills: description-triggered progressive load; user may mention skill | Prefer higher-grade facts as **distinct product philosophies**. For Toolbelt: do **not** copy Superpowers mandatory-invocation as law; Toolbelt already uses announce-and-follow skill discipline separately. Leave product choice OPEN for Theme 23 elevate. |
| Where “playbook” lives | Prisma: onboarding Common-Tasks-Playbook under docs | Superpowers: workflow in README; no file named playbook | Naming varies; pattern is task→pointer map vs encyclopedia. |

## 7. Gaps & OPEN

- `GAP`: No public Cursor `create-plugin` source repo found in this pass; E0 local README only.
- `GAP`: Few skill packs publish a durable “when surfaces change, update host playbook” checklist comparable to Toolbelt Theme 23 T23D intent; OWK/prisma are closest partials.
- `OPEN`: Whether Toolbelt host playbook should be a single `docs/host-playbook.md` vs README + inventory appendix (campaign lean says host-playbook.md — not locked by this note).
- `OPEN`: How strongly Toolbelt should bootstrap via `guide-meta` vs session hook injection (Superpowers pattern) — out of scope to decide here.

## 8. Implications (INFERENCE only)

**Transferable for Toolbelt host playbook craft** (patterns only — not importing third-party process as Toolbelt law):

1. **Split consumer vs contributor docs** — host playbook ≠ AGENTS.md PR rules (superpowers split).
2. **Start-here stack** — install → one meta/entry skill (`guide-meta` analogue) → short flow map → compact catalog; bodies stay progressive.
3. **Catalog columns** — id / pocket or group / intent (good-for) / limits or when-not / next handoff (inspired by Superpowers groups + cascade tables + anthropics description “what+when”).
4. **Honesty about surfaces** — support matrix / disclaimer / manual-setup notes (OWK, anthropics, imweb).
5. **Maintenance hook language** — “inventory/playbook drifts with surfaces; when docs and live skills disagree, live skills win — fix the playbook” (superpowers porting + prisma doc-maintenance spirit).

**Reject / do not copy as Toolbelt law:**

- Superpowers mandatory “1% chance → must invoke” / auto-trigger-as-methodology, TDD/worktree ceremony, zero-dependency dogma, PR-rejection theater in host docs.
- OWK Completion Contract / Evidence Ledger / Ed25519 permits as Toolbelt host requirements.
- Pasting entire skill library into AGENTS.md (dev-cascade non-Claude path) as the only model — conflicts with progressive disclosure.
- Ansible/Sentinel “host playbook” naming coincidence.
- Community cascade packs as SoT for Toolbelt sequencing.

## 9. Source list (deduped)

1. https://github.com/obra/superpowers — `README.md`, `AGENTS.md`, `CLAUDE.md`, `skills/using-superpowers/SKILL.md`, `docs/porting-to-a-new-harness.md`, `.cursor-plugin/plugin.json` (2026-08-04)
2. https://github.com/anthropics/skills — `README.md`, `template/SKILL.md`, `skills/skill-creator/SKILL.md`, `skills/frontend-design/SKILL.md` (2026-08-04)
3. https://github.com/agentskills/agentskills — `README.md`, `docs/home.mdx`, `docs/skill-creation/best-practices.mdx` (2026-08-04)
4. https://github.com/bluecoast1379/open-workflow-kit — `README.md`, `docs/*` (2026-08-04)
5. https://github.com/smillunchick/dev-cascade — README, `agents.md` (2026-08-04)
6. https://github.com/prisma/prisma — `AGENTS.md`, `docs/onboarding/Common-Tasks-Playbook.md` (2026-08-04)
7. https://github.com/kubernetes-sigs/agent-sandbox — `AGENTS.md` (2026-08-04)
8. https://github.com/imwebme/imweb-ai-toolkit — `.cursor-plugin/README.md`, `docs/` listing (2026-08-04)
9. Local Cursor plugin cache — `create-plugin` README (E0) (2026-08-04)

## Self-check

- [x] Depth chosen and recorded (`deep`)
- [x] Stop rule applied (`diminishing_returns` after repeated structure)
- [x] Method block present
- [x] FACT/CLAIM supported; no invented APIs
- [x] INFERENCEs list premises
- [x] Conflicts logged
- [x] Draft not treated as design law
- [x] Third-party process not promoted as Toolbelt SoT
