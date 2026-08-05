---
title: "T24G — GitHub workspace learning loops (harvest → proposed → accept)"
status: draft
theme: theme-24-author-learning
track: T24G
created: 2026-08-05
updated: 2026-08-05
authors: [gatherer-t24g-gh]
supersedes: null
aligned_with:
  - docs/research/notes/theme-24-author-learning/campaign-brief.md
  - docs/research/notes/theme-24-author-learning/deep-campaign-board.md
---

# T24G — GitHub workspace learning loops

**Using `research-protocol`**. Depth: **deep** (Wave 1 gatherer). **Draft ≠ law.** External workflows are comparators only — do not copy as Toolbelt design locks.

## 1. Scope

- **Question / goal:** What open-source **repo patterns** show a **harvest → proposed → accept** loop for workspace-scoped skills, rules, standards, or `AGENTS.md` / `CLAUDE.md` learning?
- **In scope:** Public GitHub projects with file-path evidence of agent memory, skill/rule evolution in-repo, retrospective→docs, session-driven skill updates, Cursor/Claude skill update flows; star counts as popularity signal (not quality proof).
- **Out of scope:** Copying any workflow as Toolbelt law; personal (non-workspace) memory as sole SoT; CI/PR ceremony as Theme 24 method; inventing Cursor private APIs; rewriting Toolbelt plugin `skills/*`.
- **Comprehension / research goal type:** reuse (comparator patterns for author-learning).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-05 |
| Tools used | GitHub MCP `user-github` (`search_repositories`, `search_code`, `get_file_contents`); `gh` CLI (`gh search code`, `gh search repos`, `gh repo view`, `gh api`) |
| Corpora / URLs searched | GitHub code + repository search; primary file reads via Contents API / MCP |
| Queries (exact) | `topic:agent-memory stars:>20`; `self-learning agents CLAUDE.md OR AGENTS.md stars:>10`; code: `AGENTS.md learn OR retrospective OR propose filename:AGENTS.md`; `"propose" "CLAUDE.md" OR "AGENTS.md" "rules" path:.cursor OR path:.claude OR path:.agents`; `"update skill" OR "skill evolution" OR "learn from session"`; `gh search code "propose additions to CLAUDE.md"`; `gh search code "harvest" "AGENTS.md" "proposed"`; `"staging" "adopt" harvest skill OR CLAUDE.md OR AGENTS.md`; `gh search code "draft" "proposed" "AGENTS.md" "learning"` |
| What was *not* searched | Alexandria RAG; academic papers beyond what repos cite; private repos; exhaustive star-sorted crawl of all agent-memory topics; runtime verification of each tool’s behavior (E0 of third-party CLIs not run) |
| Depth | deep |
| Waves / stop_reason | Wave 1 gatherer only; `stop_reason: diminishing_returns` after ~12 repos with overlapping harvest→propose→gate→accept shapes (further hits were variants of same stages) |
| Provenance (optional PROV) | Entity=sampled repos/files; Activity=2026-08-05 GitHub search+fetch; Agent=gatherer via MCP/`gh` |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Systematic query fan-out for discovery; as-needed deep reads on highest-signal paths |
| Scope boundary | Public GitHub only; prefer workspace-scoped paths (`.cursor/skills/`, `.agents/`, `docs/learnings/`, project `CLAUDE.md`/`AGENTS.md`); note global `~/.claude` targets when present |

## 4. Findings

### 4.1 Pattern inventory (comparators)

Repo patterns that **name** harvest / propose / stage / gate / adopt (or human Apply/Accept) for workspace skills or agent instruction files:

| Pattern shape | Exemplar (stars 2026-08-05) | Key paths |
|---------------|----------------------------|-----------|
| Capture queue → human review → apply to `CLAUDE.md`/`AGENTS.md`/skills | `BayramAnnakov/claude-reflect` (1284★) | `README.md`, `commands/reflect.md`, hooks under `scripts/` |
| Harvest → mine → replay → consolidate → **stage** → **adopt** (validation gate) | `microsoft/SkillOpt` (15637★) | `plugins/codex/skills/skillopt-sleep/SKILL.md`, `README.md` |
| Feedback → normalize → **propose** patch → review → gate → **promote** (`proposed/`→`accepted/`/`rejected/`) | `gaotiexinqu/OneResearchClaw` (440★) | `.cursor/skills/skill-evolve/SKILL.md` |
| Session JSON → frequency filter → **Proposed Rule** → human Accept/Modify/Reject/Defer | `ngocsangyem/MeowKit` (14★) | `.claude/skills/memory/references/pattern-extraction.md` |
| `/learn` capture → `docs/learnings/` inbox/candidates → promote; artifacts `required` vs `proposed` | `divad12/dotfiles` (25★) | `docs/ai/learning-system.md`, `.agents/skills/learn/SKILL.md` |
| Retrospective → Proposed Skill IDs → SMART “Accept skill” → skillbook ADD/UPDATE + `AGENTS.md` | `rjmurillo/ai-agents` (40★) | `.agents/retrospective/2025-12-19-self-contained-agents.md` |
| Explicit “propose, don’t unilaterally rewrite” skills/rules/`CLAUDE.md` | `chrono-meta/forge-harness` (7★) | `.agents/rules/fh-governor.md` |
| Skill writes staged pending approve/reject | `NousResearch/hermes-agent` (225951★) | `website/docs/user-guide/configuration.md` |
| Reflect audit → evolve proposals → wait for approval (auto-fix only low-risk) | `alexiolan/craft-skills` (17★) | `skills/reflect/SKILL.md` |
| Lessons pipeline + `--rules` propose `CLAUDE.md`/`AGENTS.md` additions | `nvk/llm-wiki` (926★) | `AGENTS.md` |
| Research design: learnings file + retrospectives → consolidation → **propose** `CLAUDE.md` | `jedarden/NEEDLE` (15★) | `docs/research/self-learning-agents.md` |
| Session end: encode patterns; pre-merge propose retrospective | `spbu-se/spbu_se_site` (3★) | `AGENTS.md` |

Stars via `gh repo view … --json stargazerCount` on 2026-08-05.

### 4.2 Claim bullets

- `FACT` [E1] `claude-reflect` documents a two-stage loop: automatic hook **capture** into a queue, then manual `/reflect` with human options **Apply / Edit before applying / Skip**, writing approved learnings to project/`~` `CLAUDE.md`, optional `AGENTS.md`, and skill command files; `/reflect --dry-run` previews without applying; `/reflect-skills` discovers skill candidates with “you approve” before generating `.claude/commands/`. Quote: “`(automatic)` … `(manual review)`” and “Apply - Accept the learning”. [E1: BayramAnnakov/claude-reflect README.md — https://github.com/BayramAnnakov/claude-reflect/blob/main/README.md — accessed 2026-08-05]

- `FACT` [E1] SkillOpt-Sleep names an explicit cycle: **Harvest → Mine → Replay → Consolidate → Gate → Stage → Adopt**; staged under `<project>/.skillopt-sleep/staging/<date>/`; “Live files change only through explicit adoption or a user-requested `--auto-adopt`”; “Treat generated edits as proposals, not as source of truth.” [E1: microsoft/SkillOpt `plugins/codex/skills/skillopt-sleep/SKILL.md` — https://github.com/microsoft/SkillOpt/blob/main/plugins/codex/skills/skillopt-sleep/SKILL.md — accessed 2026-08-05]

- `FACT` [E1] SkillOpt README describes SkillOpt-Sleep as “harvest → mine → replay → consolidate behind a held-out validation gate” and positions skill documents as trainable state with candidate edits accepted only when held-out score improves (paper-style path). [E1: microsoft/SkillOpt README.md — https://github.com/microsoft/SkillOpt/blob/main/README.md — accessed 2026-08-05]

- `FACT` [E1] OneResearchClaw `skill-evolve` is opt-in; writes patch proposals to `{WORKSPACE}/.skill-evolve-data/patch_proposals/proposed/`; requires human review before apply; regression gate; promote creates versioned snapshot; directories include `accepted/` and `rejected/`; “Preserve the default `.cursor/skills/` tree unchanged unless a human later chooses to merge approved changes manually”; promotion with `--sync` updates stable skills only when explicitly requested. [E1: gaotiexinqu/OneResearchClaw `.cursor/skills/skill-evolve/SKILL.md` — https://github.com/gaotiexinqu/OneResearchClaw/blob/main/.cursor/skills/skill-evolve/SKILL.md — accessed 2026-08-05]

- `FACT` [E1] MeowKit pattern-extraction requires frequency/severity filters, drafts “### Proposed Rule”, then human **Accept / Modify / Reject / Defer**, and states “**Do NOT automatically modify CLAUDE.md.**” Accepted rules go to `CLAUDE.md`; JSON entries get `promoted`/`rejected`. [E1: ngocsangyem/MeowKit `.claude/skills/memory/references/pattern-extraction.md` — https://github.com/ngocsangyem/MeowKit/blob/main/.claude/skills/memory/references/pattern-extraction.md — accessed 2026-08-05]

- `FACT` [E1] divad12 learning-system keeps canonical store in `docs/learnings/` (`inbox.md`, `candidates.md`, dashboard); prevention artifacts use `docs (required), test (required), skill (proposed)` wording; `/learn` captures, automation may promote; “Review is optional calibration, not a daily approval gate” (acts by default on clear work — different accept posture). [E1: divad12/dotfiles `docs/ai/learning-system.md` — https://github.com/divad12/dotfiles/blob/master/docs/ai/learning-system.md — accessed 2026-08-05]

- `FACT` [E1] rjmurillo retrospective closes with Proposed Skill IDs, SMART tables marked “Accept skill”, then Skillbook **ADD/UPDATE/TAG**, and action “Document deployment model in AGENTS.md”. Path: `.agents/retrospective/2025-12-19-self-contained-agents.md`. [E1: rjmurillo/ai-agents retrospective — https://github.com/rjmurillo/ai-agents/blob/main/.agents/retrospective/2025-12-19-self-contained-agents.md — accessed 2026-08-05]

- `FACT` [E1] forge-harness governor rule: “**No silent FH-asset edits**: propose, don't unilaterally rewrite SKILL.md / rules / CLAUDE.md.” [E1: chrono-meta/forge-harness `.agents/rules/fh-governor.md` — https://github.com/chrono-meta/forge-harness/blob/main/.agents/rules/fh-governor.md — accessed 2026-08-05]

- `FACT` [E1] Hermes Agent docs: `skills.write_approval` stages skill writes under `~/.hermes/pending/skills/` for `/skills approve` / `/skills reject` (CLI). Quote: “stage every write for review”. [E1: NousResearch/hermes-agent `website/docs/user-guide/configuration.md` — https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/configuration.md — accessed 2026-08-05]

- `FACT` [E1] craft-skills `reflect`: Phase 2 generates ranked proposals and “Present to user for approval”; Phase 3.2 “Wait for user approval before making changes (except auto-fix tier).” [E1: alexiolan/craft-skills `skills/reflect/SKILL.md` — https://github.com/alexiolan/craft-skills/blob/main/skills/reflect/SKILL.md — accessed 2026-08-05]

- `FACT` [E1] llm-wiki `AGENTS.md` Lessons Learned flags include: “`--dry-run` (preview without writing), `--rules` (also propose CLAUDE.md/AGENTS.md rule additions)”. [E1: nvk/llm-wiki AGENTS.md — https://github.com/nvk/llm-wiki/blob/main/AGENTS.md — accessed 2026-08-05]

- `FACT` [E1] NEEDLE research note (workspace design, not shipped product claim): “workers that discover conventions can **propose** additions to CLAUDE.md, gated by a consolidation step”; learnings.md + bead retrospectives → consolidation; Allen-style promotion of repeated patterns to `.claude/rules/`. [E1: jedarden/NEEDLE `docs/research/self-learning-agents.md` — https://github.com/jedarden/NEEDLE/blob/main/docs/research/self-learning-agents.md — accessed 2026-08-05]

- `FACT` [E1] spbu_se_site `AGENTS.md`: “Before merge: if session involved doc restructuring, **propose retrospective** as the final step”; “Always learn, never forget — encode patterns before session ends”. [E1: spbu-se/spbu_se_site AGENTS.md — https://github.com/spbu-se/spbu_se_site/blob/staging/AGENTS.md — accessed 2026-08-05]

- `CLAIM` [E3] Community/marketing descriptions of “autonomous skill evolution” (e.g. `vibeeval/vibecosystem` repo description, 523★) were not file-traced in this pass to an explicit harvest→proposed→accept directory convention. [E3: github.com/vibeeval/vibecosystem description via search_repositories — accessed 2026-08-05]

- `GAP` Searched: code for a single shared vocabulary `harvest` + `proposed` + `accept` tied to Toolbelt-like host standards catalogs. Result: overlapping **stages** appear widely; no canonical shared schema or status enum reused across projects; naming varies (`staging`/`adopt`, `proposed`/`accepted`, Apply/Skip, approve/reject).

- `OPEN` Follow-up: Does Cursor product docs define a first-party “accept learning” API for workspace skills, or only file-based conventions? (Defer to T24D-docs.)

### 4.3 Harvest → proposed → accept (stage map)

| Stage | Observed mechanisms (not Toolbelt law) | Exemplars |
|-------|----------------------------------------|-----------|
| **Harvest** | Hooks on prompts/commits; session transcript harvest; `/learn` capture; retrospective debrief; feedback scripts | claude-reflect; SkillOpt-Sleep; divad12; MeowKit; ai-agents |
| **Proposed** | Queue + dry-run; `.skillopt-sleep/staging/`; `patch_proposals/proposed/`; “Proposed Rule” markdown; SMART proposed skills; `~/.hermes/pending/skills/` | SkillOpt; OneResearchClaw; MeowKit; hermes; llm-wiki `--rules` |
| **Gate / accept** | Human Apply/Skip; held-out score gate; regression assertions; frequency thresholds; SMART pass; `/skills approve`; explicit promote/`--sync` | claude-reflect; SkillOpt; OneResearchClaw; MeowKit; hermes |
| **Land in workspace SoT** | `CLAUDE.md` / `AGENTS.md` / `.claude/commands/` / `.cursor/skills/` / `docs/learnings/` / skillbook memory | most samples |

`INFERENCE` [E4] A recurring comparator shape is **asymmetric trust**: harvest may be automatic, but **writes to durable instruction surfaces** are staged or human-gated (or validation-gated). Premises: (1) claude-reflect manual review; (2) SkillOpt stage/adopt; (3) OneResearchClaw opt-in promote; (4) MeowKit “Do NOT automatically modify CLAUDE.md”; (5) forge-harness “propose, don't unilaterally rewrite”.

`INFERENCE` [E4] “Accept” is not one mechanism: human click (Apply/Approve), metric gate (held-out score), or frequency+human (MeowKit). Premises: FACT bullets for claude-reflect, SkillOpt, MeowKit.

`CLAIM` [E3/E4] Stars correlate with discoverability, not with fitness for Toolbelt host-standards authoring. Premises: star counts observed; no outcome evals run here.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Mature workspace learning loops separate capture from promotion into instruction files | confirmed (in sampled set) | claude-reflect, SkillOpt-Sleep, MeowKit, OneResearchClaw |
| H2 | Most repos use identical status vocabulary `proposed`/`accepted` for standards | rejected | vocabulary fragmented; only some use those directory names |
| H3 | Retrospective→skillbook is rarer than correction→CLAUDE.md | open | one strong retrospective sample (ai-agents); many CLAUDE.md sync samples |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Human gate vs act-by-default | MeowKit / claude-reflect / SkillOpt default stage-only require human (or explicit adopt) before durable write | divad12: “Review is optional calibration… act by default” | Leave OPEN for Theme 24 trigger design; both are workspace patterns; do not pick as law |
| Global vs project memory targets | claude-reflect syncs `~/.claude/CLAUDE.md` and project files | Theme 24 brief: host/workspace-bound surfaces | Note as comparator tension; prefer project-scoped paths when mapping to Toolbelt host feedstock |

## 7. Gaps & OPEN

- No E0 runtime of SkillOpt-Sleep / claude-reflect in this session (docs-only FACT).
- `MemSkill` (556★) is research/code for evolving memory *skills* as ML objects — not sampled for workspace markdown accept loop; may be out of T24 host-surface target.
- Cursor-specific first-party product docs not loaded here (`OPEN` → T24D).
- Weak evidence that any popular repo implements Toolbelt’s exact `draft`/`proposed`/`accepted` frontmatter statuses for host standards modules.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] For Theme 24 author-learning, comparator pressure favors: (1) structured harvest candidates, (2) a visible **proposed** staging surface, (3) human (or explicit) accept before host skills/standards/`AGENTS` become SoT — matching campaign brief hard fence “never auto-promote”. Premises: §4.2–4.3 FACTs + accepted campaign brief O1 fence (local, not re-proven here).
- `INFERENCE` [E4] Optional dry-run / preview and frequency or validation gates are common quality filters before accept. Premises: claude-reflect `--dry-run`; SkillOpt held-out gate; MeowKit frequency≥3; OneResearchClaw regression gate.
- `CLAIM` [E3] Copying SkillOpt’s metric gate or claude-reflect’s correction regex as Toolbelt law would overfit third-party product assumptions — use as pattern language only.

## 9. Source list (deduped)

1. https://github.com/BayramAnnakov/claude-reflect — README.md (1284★)
2. https://github.com/microsoft/SkillOpt — README.md; `plugins/codex/skills/skillopt-sleep/SKILL.md` (15637★)
3. https://github.com/gaotiexinqu/OneResearchClaw — `.cursor/skills/skill-evolve/SKILL.md` (440★)
4. https://github.com/ngocsangyem/MeowKit — `.claude/skills/memory/references/pattern-extraction.md` (14★)
5. https://github.com/divad12/dotfiles — `docs/ai/learning-system.md` (25★)
6. https://github.com/rjmurillo/ai-agents — `.agents/retrospective/2025-12-19-self-contained-agents.md` (40★)
7. https://github.com/chrono-meta/forge-harness — `.agents/rules/fh-governor.md` (7★)
8. https://github.com/NousResearch/hermes-agent — `website/docs/user-guide/configuration.md` (225951★)
9. https://github.com/alexiolan/craft-skills — `skills/reflect/SKILL.md` (17★)
10. https://github.com/nvk/llm-wiki — `AGENTS.md` (926★)
11. https://github.com/jedarden/NEEDLE — `docs/research/self-learning-agents.md` (15★)
12. https://github.com/spbu-se/spbu_se_site — `AGENTS.md` (3★)
13. https://github.com/vibeeval/vibecosystem — repository metadata only (523★; file loop not verified)
14. https://github.com/ViktorAxelsen/MemSkill — metadata/README skim only (556★; not mapped to markdown accept loop)

## Self-check

- [x] Depth chosen and recorded (`deep`)
- [x] Stop rule applied (`diminishing_returns` after overlapping stage shapes)
- [x] Method block present
- [x] Every FACT/CLAIM has support
- [x] INFERENCEs list premises
- [x] No invented citations/APIs
- [x] Conflicts logged
- [x] Draft/proposed not treated as design law
