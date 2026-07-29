---
title: "T4H — Agent Skills Spec writing guidance (Wave 2 corroboration)"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-T4H]
supersedes: null
product: Agent Skills open standard (+ Cursor Skills alignment)
cursor_version: "3.13.25"
access_date: 2026-07-29
aligned_with: docs/research/notes/theme-4-cursor-plugins/t4c-skills.md
wave: 2
---

# T4H — Agent Skills Spec + examples: writing for cold-start agents

**Using `docs-research` + `research-protocol`.**

## 1. Scope

- **Question / goal:** Cross-reference Cursor Skills docs findings (Wave 1 `t4c-skills.md`) with the **Agent Skills open standard** and high-signal official examples, producing **evidenced** writing/structure guidance that helps skills work for **fresh agents with little conversation context** (cold-start / clean-session activation).
- **In scope:** agentskills.io overview + specification + skill-creation guides (best practices, evaluating skills, optimizing descriptions); Cursor `skills.md` alignment/conflicts; `anthropics/skills` README, `skills/skill-creator`, and 2–3 example `SKILL.md` patterns; star count via GitHub API.
- **Out of scope:** Rewriting `t4c-skills.md`; inventing Cursor-only frontmatter; Alexandria/community skill lists as design locks; E0 runtime experiments in Cursor this pass.
- **Comprehension type:** reuse / adaptive (author Toolbelt skills for cold-start agents).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch; WebSearch (`site:agentskills.io`); `gh api repos/anthropics/skills`; GitHub MCP `get_file_contents`; Read of Wave 1 note (no rewrite) |
| Corpora / URLs searched | https://agentskills.io ; https://agentskills.io/specification ; https://agentskills.io/llms.txt ; https://agentskills.io/skill-creation/best-practices ; https://agentskills.io/skill-creation/evaluating-skills ; https://agentskills.io/skill-creation/optimizing-descriptions ; https://cursor.com/docs/skills.md ; https://github.com/anthropics/skills (README, template, skill-creator, pdf, frontend-design, mcp-builder) |
| Queries (exact) | `site:agentskills.io writing skills best practices OR guide` |
| What was *not* searched | Alexandria RAG; Cursor forum/SO; Claude support articles beyond README links; full crawl of every `anthropics/skills/*/SKILL.md`; E0 Cursor activation experiments; `skills-ref` binary install/run |
| Provenance | Entity←Agent Skills Spec site + Cursor docs + anthropics/skills @ `b29e7cf…` + Wave 1 T4C; Activity=T4H Wave 2 corroboration 2026-07-29; Agent=gatherer-T4H |

**D0 pin:** Cursor `in_use` build **3.13.25** [E0 via campaign D0 / T4C]. Spec docs = live agentskills.io (no release-tag pin) → Spec version skew **unknown**. Anthropic examples pin: commit SHA `b29e7cf65e5cb78a5ac33d582270551bc74a14eb` (from GitHub contents API `ref`).

**D2 Diátaxis:**

| URL | Type | Trust for writing truth |
|-----|------|-------------------------|
| agentskills.io/specification | reference (normative format) | high for portable structure/fields |
| agentskills.io/skill-creation/* | how-to / explanation | high for authoring intent; still E1 until E0 |
| cursor.com/docs/skills.md | how-to + reference | high for Cursor product behavior |
| anthropics/skills examples | how-to exemplars (official Anthropic) | E1 for patterns shown; disclaimer: educational |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | systematic (required URLs) + hybrid (skill-creation guides from llms.txt index; 3 example skills + skill-creator) |
| Why | Mission = corroboration for cold-start writing; Spec + official creator guides + examples are the primary evidence surface |
| Scope boundary | Spec site + Cursor skills.md + anthropics/skills selected paths; Wave 1 T4C as comparison baseline (read-only) |

## 4. Findings

### 4.1 Progressive disclosure & cold-start load model (Spec + Cursor)

- `FACT` [E1] Agents load skills in three stages: (1) Discovery — name + description at startup; (2) Activation — full `SKILL.md` when task matches; (3) Execution — follow instructions, optionally run bundled code / load referenced files. [E1: Agent Skills Overview — https://agentskills.io — accessed 2026-07-29]
- `FACT` [E1] Spec progressive disclosure budgets: Metadata ~100 tokens (name+description at startup); Instructions <5000 tokens recommended (full body on activate); Resources as needed. Keep main `SKILL.md` under 500 lines; move detail to separate files; relative paths from skill root; keep references one level deep. [E1: https://agentskills.io/specification — accessed 2026-07-29]
- `FACT` [E1] Cursor: on start, discovers skills and presents them to Agent; relevance from context; progressive/on-demand resource loading paraphrased; does **not** restate Spec token/line budgets on skills.md. [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29] (aligns with T4C §4.3 / conflict log)
- `INFERENCE` [E4] For a **cold-start / fresh-session** agent, discovery depends almost entirely on `description` quality; body text is invisible until activation. Premises: (1) Spec three-stage load [E1 overview/spec]; (2) optimizing-descriptions: “description carries the entire burden of triggering” [E1: https://agentskills.io/skill-creation/optimizing-descriptions — accessed 2026-07-29].
- `FACT` [E1] Eval guidance for output quality: each eval run should start with a **clean context** — no leftover state from prior runs or skill development — so the agent follows only what `SKILL.md` tells it. [E1: https://agentskills.io/skill-creation/evaluating-skills — accessed 2026-07-29]

### 4.2 Spec frontmatter vs Cursor (corroboration of Wave 1)

- `FACT` [E1] Spec required: `name`, `description`. Optional: `license`, `compatibility`, `metadata`, `allowed-tools` (experimental, space-separated). Name constraints include max 64 chars, no leading/trailing/consecutive hyphens, must match parent directory. Description max 1024 chars; should describe what + when + keywords. [E1: https://agentskills.io/specification — accessed 2026-07-29]
- `FACT` [E1] Cursor-documented skill frontmatter: `name`, `description`, `paths`, `disable-model-invocation`, `metadata` (+ legacy `globs`). [E1: https://cursor.com/docs/skills.md — accessed 2026-07-29]
- `FACT` [E1] Spec body: no format restrictions; recommended sections = step-by-step instructions, I/O examples, common edge cases; entire body loads on activation. [E1: https://agentskills.io/specification — accessed 2026-07-29]
- `CLAIM` [E1] Wave 1 dual-surface inference remains valid this pass: Cursor extensions `paths` / `disable-model-invocation` absent from Spec frontmatter table; Spec-only `license` / `compatibility` / `allowed-tools` absent from Cursor skills.md table. [E1 both tables 2026-07-29; compare T4C §4.4]
- `OPEN` Cursor runtime honor of Spec-only fields — still not stated on Cursor skills.md (same OPEN as T4C).

### 4.3 Official writing guidance (agentskills.io skill-creation) — cold-start relevant

- `FACT` [E1] Best practices: avoid LLM-generated skills from generic training knowledge alone; ground in real expertise (extract from hands-on agent tasks; synthesize from project artifacts). [E1: https://agentskills.io/skill-creation/best-practices — accessed 2026-07-29]
- `FACT` [E1] Context budget: after activation, full body competes with conversation + system + other skills; “Add what the agent lacks, omit what it knows”; cut content the agent would not get wrong without the skill. [E1: best-practices — accessed 2026-07-29]
- `FACT` [E1] Scope as coherent units (like functions): too narrow → many skills load / conflict; too broad → imprecise activation. Prefer moderate detail + working example over exhaustive edge-case dumps. [E1: best-practices — accessed 2026-07-29]
- `FACT` [E1] Progressive disclosure authoring: when moving content to `references/`, tell the agent **when** to load each file (conditional pointers), not only “see references/”. [E1: best-practices — accessed 2026-07-29]
- `FACT` [E1] Instruction patterns documented as effective: gotchas sections (concrete assumption-breakers kept in main body); output templates; multi-step checklists; validation loops; plan-validate-execute for fragile/batch ops; defaults-not-menus; procedures-over-instance-answers; match specificity to fragility; favor explaining *why* over rigid ALL-CAPS MUST. [E1: best-practices — accessed 2026-07-29]
- `FACT` [E1] Description optimization: use imperative “Use this skill when…”; focus on user intent not internals; “err on the side of being pushy”; include contexts even without domain keywords; stay under 1024 chars; description is primary trigger mechanism. [E1: https://agentskills.io/skill-creation/optimizing-descriptions — accessed 2026-07-29]
- `FACT` [E1] Trigger nuance: agents may skip skills for trivial one-step tasks they can do with basic tools even if description matches; specialized/multi-step tasks are where good descriptions matter most. [E1: optimizing-descriptions — accessed 2026-07-29]
- `FACT` [E1] Eval-driven improvement: `evals/evals.json` with prompts + expected outputs; with-skill vs without-skill (or prior version) baselines; assertions after seeing outputs; grade with evidence; iterate; prefer clean-context runs. Description evals: ~20 queries (should/should-not), train/validation split, multiple runs for trigger rate. [E1: evaluating-skills + optimizing-descriptions — accessed 2026-07-29]
- `FACT` [E1] Spec validation tooling: `skills-ref validate ./my-skill` for frontmatter/naming. [E1: https://agentskills.io/specification — accessed 2026-07-29]

### 4.4 anthropics/skills — repo identity + skill-creator + example patterns

- `FACT` [E1] Repo `anthropics/skills`: description “Public repository for Agent Skills”; default branch `main`; **stargazers_count = 165010** as of API call 2026-07-29; points readers to agentskills.io for the standard. [E1: `gh api repos/anthropics/skills` — accessed 2026-07-29]
- `FACT` [E1] README: skills = folders of instructions/scripts/resources; `SKILL.md` with YAML frontmatter + instructions; required frontmatter only `name` + `description`; template in `./template`; includes `skills/skill-creator`; disclaimer that examples are educational and behaviors may differ in product. Observed commit via contents API: `b29e7cf65e5cb78a5ac33d582270551bc74a14eb`. [E1: https://github.com/anthropics/skills/blob/b29e7cf65e5cb78a5ac33d582270551bc74a14eb/README.md — accessed 2026-07-29]
- `FACT` [E1] `template/SKILL.md` minimal: `name: template-skill` + placeholder description + “Insert instructions below”. [E1: template/SKILL.md @ that commit]
- `FACT` [E1] `skills/skill-creator/SKILL.md` frontmatter: `name` + long pushy `description` covering create/edit/optimize/evals/triggering; body teaches draft → test prompts in clean runs → quantitative+qualitative eval → rewrite; progressive disclosure anatomy (`scripts/` / `references/` / `assets/`); keep SKILL.md under ~500 lines; clear when-to-read references; TOC for large refs; description should include all “when to use” (pushy to combat under-trigger); prefer imperative; explain why over heavy MUST; bundle scripts when traces show repeated reinvented helpers; automates eval/description loops via bundled scripts/agents. [E1: skills/skill-creator/SKILL.md @ that commit]
- `FACT` [E1] Official skill-creation pages link `skill-creator` as automation for eval + description optimization loops. [E1: evaluating-skills + optimizing-descriptions — accessed 2026-07-29]
- `FACT` [E1] Example pattern **pdf**: pushy description enumerating PDF tasks + “If the user mentions a .pdf… use this skill”; `license` present; body = quick-start defaults (library choices) + gotcha (ReportLab subscripts) + conditional “see REFERENCE.md / FORMS.md when…”. [E1: skills/pdf/SKILL.md @ that commit]
- `FACT` [E1] Example pattern **frontend-design**: description states when (new/reshape UI) without listing every UI synonym; `license` present; body = opinionated principles + brainstorm→critique→build process + anti-default aesthetics; no scripts dir required in the pattern observed in SKILL.md alone. [E1: skills/frontend-design/SKILL.md @ that commit]
- `FACT` [E1] Example pattern **mcp-builder**: description = what + when (build MCP servers / FastMCP or TS SDK); phased workflow; **conditional reference loading** (`./reference/*.md`, WebFetch SDK READMEs); ends with evaluation phase creating independent Q/A pairs. [E1: skills/mcp-builder/SKILL.md @ that commit]
- `INFERENCE` [E4] High-signal official examples converge on: (a) discovery-heavy descriptions, (b) defaults + gotchas in body, (c) detail behind when-gated references, (d) procedures that generalize. Premises: §4.3 best-practices + §4.4 three examples + skill-creator writing guide.

### 4.5 Alignment with Wave 1 T4C (no rewrite)

- `FACT` [E0] Read `d:\Toolbelt\docs\research\notes\theme-4-cursor-plugins\t4c-skills.md` (Wave 1). T4C already recorded Spec progressive disclosure, Spec vs Cursor frontmatter split, Cursor `paths` / `disable-model-invocation`, and testing GAP vs `skills-ref` / local plugin load. [E0: path=t4c-skills.md — read 2026-07-29]
- `FACT` [E1] This Wave 2 pass **adds** agentskills.io skill-creation guides (best-practices, evaluating-skills, optimizing-descriptions) and anthropics example/skill-creator patterns that T4C Method explicitly did **not** search (“Claude Code Anthropic docs beyond agentskills.io”). [E1: T4C Method “What was not searched”; this note Method]
- `CLAIM` [E1] Cursor skills.md writing sample (When to Use / Instructions / ask-questions tip) is thinner than Spec skill-creation guidance; Cursor still links agentskills.io as “Learn more.” [E1: skills.md + agentskills.io — accessed 2026-07-29]

### 4.6 Cursor-only behavior still GAP for writing locks

- `GAP` No Cursor docs page found (this pass or T4C) that adopts Spec “<5000 tokens / 500 lines,” description-optimization loops, or `evals/evals.json` harness as a Cursor product feature. Searched: skills.md this pass; T4C §4.7. Result: Cursor testing story remains local plugin load / Customize visibility + Spec `skills-ref`.
- `GAP` Whether Cursor Agent under-triggers skills the same way skill-creator assumes (“tendency to undertrigger”) is **not** stated on Cursor docs → prefer GAP over assuming Cursor parity with Claude Code triggering. Searched: skills.md. Result: not found.
- `GAP` Whether Cursor honors Spec `allowed-tools` / `compatibility` / `license` at runtime — unchanged OPEN from T4C.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Cold-start effectiveness hinges on description (discovery) + lean procedural body (activation) | confirmed (Spec/guides) | overview + optimizing-descriptions + best-practices |
| H2 | Cursor documents the same authoring budgets as Spec (500 lines / 5k tokens) | rejected | absent on skills.md; present on Spec |
| H3 | Official Anthropic examples exemplify pushy descriptions + progressive refs | confirmed | pdf, mcp-builder, skill-creator |
| H4 | Cursor runtime implements Spec eval/description tooling | open | not claimed on Cursor docs; GAP |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Frontmatter surfaces | Spec: license, compatibility, allowed-tools | Cursor: paths, disable-model-invocation | Dual surface (same as T4C); portable subset = name+description+metadata overlap; do not invent Cursor support for Spec-only fields |
| Writing depth | Spec skill-creation guides: extensive patterns + evals | Cursor skills.md: short structure sample | Use Spec/guides for *how to write*; Cursor for *how Cursor loads/invokes* |
| Progressive budgets | Spec: ~100 / <5000 tokens, <500 lines | Cursor: “progressive / on demand” without budgets | Prefer Spec for portable authoring targets; OPEN whether Cursor enforces |
| Testing | Spec + skill-creator: evals, baselines, trigger rates | Cursor: local plugin load; skills-ref mentioned only via Spec | Document both; no Cursor-native harness found |
| Trigger psychology | skill-creator / optimizing-descriptions: under-trigger → pushy descriptions | Cursor: agent decides relevance from context; no under-trigger claim | Treat pushy-description as Spec/Anthropic guidance (E1); Cursor-specific under-trigger = GAP |

## 7. Gaps & OPEN

- `GAP` Cursor product docs do not document Spec skill-creation eval / description-optimization workflows.
- `GAP` Cursor runtime behavior for Spec-only frontmatter fields.
- `GAP` Cursor-specific under-trigger / over-trigger rates vs Claude Code assumptions in skill-creator.
- `GAP` Exact line count of long production examples (e.g. pdf) vs Spec “under 500 lines” recommendation — not measured this pass (could exceed; Spec says recommended not hard fail).
- `OPEN` Should Toolbelt skills adopt Spec `license`/`compatibility` for portability even if Cursor ignores them?
- `OPEN` Should Toolbelt adopt `evals/` + clean-context harness as authoring SoT (Spec E1) despite Cursor GAP?
- `OPEN` Interaction of Cursor `paths` / nested monorepo scoping with Spec-portable skills used outside Cursor.

## 8. Implications (INFERENCE only — not design locks)

- `INFERENCE` [E4] For Toolbelt skills aimed at fresh agents: invest first in **pushy, intent-focused `description`**; keep `SKILL.md` body as lean procedures + gotchas + defaults; gate deep material with **when-to-read** pointers. Premises: §4.1, §4.3, §4.4.
- `INFERENCE` [E4] Prefer Spec skill-creation patterns as writing law for portable skills; overlay Cursor fields (`paths`, `disable-model-invocation`) only when targeting Cursor product behavior. Premises: §4.2, §6.
- `INFERENCE` [E4] Treat eval-with-clean-context as the evidence method for “works for cold-start,” not anecdotal single-chat success. Premises: §4.1 evaluating-skills; §4.3.
- `INFERENCE` [E4] Do not lock “Cursor honors allowed-tools/compatibility” or “Cursor under-triggers like Claude” without E0. Premises: §4.6 GAPs.

## 9. Source list (deduped)

1. https://agentskills.io — accessed 2026-07-29
2. https://agentskills.io/specification — accessed 2026-07-29
3. https://agentskills.io/llms.txt — accessed 2026-07-29
4. https://agentskills.io/skill-creation/best-practices — accessed 2026-07-29
5. https://agentskills.io/skill-creation/evaluating-skills — accessed 2026-07-29
6. https://agentskills.io/skill-creation/optimizing-descriptions — accessed 2026-07-29
7. https://cursor.com/docs/skills.md — accessed 2026-07-29
8. https://github.com/anthropics/skills (API metadata: 165010 stars; commit `b29e7cf…`) — accessed 2026-07-29
9. anthropics/skills README.md, template/SKILL.md, skills/skill-creator/SKILL.md, skills/pdf/SKILL.md, skills/frontend-design/SKILL.md, skills/mcp-builder/SKILL.md @ `b29e7cf…` — accessed 2026-07-29
10. Wave 1 baseline (read-only): `docs/research/notes/theme-4-cursor-plugins/t4c-skills.md`
11. Campaign D0 / T4C: Cursor 3.13.25
