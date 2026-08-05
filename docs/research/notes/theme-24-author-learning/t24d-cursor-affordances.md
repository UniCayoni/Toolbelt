---
title: "T24D — Cursor affordances for author-learning harvest"
status: draft
theme: theme-24-author-learning
track: T24D
created: 2026-08-05
updated: 2026-08-05
authors: [t24d-docs-gatherer]
depth: deep
wave: 1
aligned_with:
  - docs/research/notes/theme-24-author-learning/campaign-brief.md
  - docs/research/notes/theme-24-author-learning/deep-campaign-board.md
supersedes: null
---

# T24D — Cursor affordances for author-learning harvest

**Using `research-protocol`**. **Using `research-docs`** (lean D0–D14). Depth: **deep** Wave 1. **Draft ≠ law.**

## 1. Scope

- **Question:** Which Cursor built-ins best support **author-learning** (propose workspace skill/standard edits from harvested candidates) **without always-on auto-write**, and which are traps (ambient memory as law, always-on rules)?
- **In scope:** Official Cursor docs for Rules, Skills, Memories, Hooks, AGENTS.md, Subagents; E0 skim of Toolbelt `skills/author-cursor-surfaces/SKILL.md` and `docs/host-playbook.md` § setup only.
- **Out of scope:** Brain/RAG product; rewriting Toolbelt plugin `skills/*`; Wave 2 trigger/candidate design; inventing Cursor private APIs; runtime E0 of IDE Memory UI beyond docs.
- **Comprehension type:** reuse (map product surfaces → harvest workflow).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-05 |
| Tools used | WebFetch (`cursor.com/docs/*`, `cursor.com/llms.txt`, help pages); WebSearch (discovery only); Read/Grep local Toolbelt; Python path-exists (E0) |
| Corpora / URLs searched | `https://cursor.com/llms.txt`; `https://cursor.com/docs/rules.md`; `skills.md`; `hooks.md`; `subagents.md`; `customize-cursor.md`; `cloud-agent/automations.md`; `agent/prompting.md`; `https://cursor.com/help/customization/context.md` |
| Queries (exact) | Cursor docs rules skills memories hooks AGENTS.md subagents; site:cursor.com/docs Memories |
| What was *not* searched | GitHub issues/forums (E3); Alexandria RAG; Cursor Extension API private surfaces; live Customize UI click-through; `docs.cursor.com` (homepage fetch failed; canonical index is `cursor.com/llms.txt`) |
| Depth | deep |
| Waves / stop_reason | Wave 1 primary SoT (official docs + E0 Toolbelt). Stop for this gatherer: primary surfaces documented; remaining IDE “Memories” as ambient chat law is **confirmed GAP** (no dedicated docs page in llms.txt) — do not invent |
| Provenance | Entity=Cursor docs + Toolbelt paths; Activity=T24D lean docs research; Agent=t24d-docs-gatherer |

### D0 — Identity & version pin (lean)

| Field | Value |
|-------|-------|
| Product | Cursor IDE / Agent (hosted docs) |
| Installed version (E0) | `in_use` (session workspace Toolbelt); **build GAP** — not read from app this pass |
| Docs version / URL | Live untagged `https://cursor.com/docs/*.md` via `https://cursor.com/llms.txt` — accessed 2026-08-05 |
| Version skew? | unknown (docs↔build OPEN; same OPEN pattern as Theme 4) |

### Diátaxis (lean)

| URL | Type | Trust |
|-----|------|-------|
| rules.md, skills.md, hooks.md, subagents.md | reference / how-to hybrid | high for documented behavior; still E1 until local E0 |
| customize-cursor.md, prompting.md | explanation + inventory | medium |
| automations.md Memories | reference (Automations tool) | high for **that** product surface only |
| help/context.md | how-to | low for API truth |

OpenAPI/contracts: **N/A** (prose product docs).

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why | Official docs primary; local author/playbook for Toolbelt handoff fence |
| Scope boundary | Cursor customize surfaces + Automations Memories; Toolbelt author skill + host-playbook §5 only |

## 4. Findings

### 4.1 Skills (best fit for propose → human accept)

- `FACT` [E1] Skills are portable `SKILL.md` packages; Agent discovers them and may apply when relevant, **or** user invokes via `/`. Progressive load (`references/`, scripts). Project paths include `.cursor/skills/` and `.agents/skills/` (plus user/compat roots). [E1: Agent Skills — https://cursor.com/docs/skills.md — accessed 2026-08-05]
- `FACT` [E1] `disable-model-invocation: true` makes a skill **slash-only** — not auto-applied from context. [E1: same skills.md — “Disabling automatic invocation”]
- `FACT` [E1] Built-ins `/create-skill`, `/create-rule`, `/migrate-to-skills`, `/create-subagent`, `/create-hook` scaffold surfaces from chat. [E1: skills.md built-in table]
- `FACT` [E1] `/migrate-to-skills` converts **Apply Intelligently** dynamic rules (no globs) and slash commands → skills; does **not** migrate `alwaysApply: true` or glob-scoped rules. [E1: skills.md — Migrating rules and commands]
- `FACT` [E0] Toolbelt `author-cursor-surfaces` is explicit `/` (`disable-model-invocation: true`); prefers skill over always-on for multi-step; scaffolds optional; draft until human accept; thin always-on rules. [E0: `skills/author-cursor-surfaces/SKILL.md`]
- `INFERENCE` [E4] For author-learning harvest into **host** skills: prefer a host-bound skill with `disable-model-invocation: true` (or explicit `/author-learning`) that writes **proposed** deltas, then human accept — not ambient auto-apply that rewrites standards mid-task. Premises: (1) skills.md slash-only flag; (2) campaign brief never auto-promote; (3) author-cursor-surfaces caveats.

### 4.2 Rules + AGENTS.md

- `FACT` [E1] Rules inject persistent prompt context; types: Always Apply / Apply Intelligently / Apply to Specific Files / Apply Manually (`alwaysApply` + `description` + `globs`). Project rules: `.cursor/rules/*.mdc` (plain `.md` ignored). Precedence when conflicting: **Team → Project → User**. [E1: Rules — https://cursor.com/docs/rules.md — accessed 2026-08-05]
- `FACT` [E1] Docs state LLMs don’t retain memory between completions; rules supply reusable context at prompt level. [E1: rules.md — How rules work]
- `FACT` [E1] Best practice: add rules when Agent repeats mistakes; keep focused; avoid dumping entire style guides into rules. [E1: rules.md — Best practices / What to avoid]
- `FACT` [E1] `AGENTS.md` is plain markdown alternative to `.cursor/rules`; root + nested; nested combine with **more specific winning**. No frontmatter/globs. [E1: rules.md — AGENTS.md]
- `FACT` [E0] Host playbook setup lists lean host path `AGENTS.md` (copy from `docs/templates/agents-md-skeleton.md`); standards catalog `docs/standards/index.md`; learn-back called out as Theme 24 separate from playbook. Always-on Toolbelt rules are three thin gates (`draft-is-not-sot`, grades, standards-resolve). [E0: `docs/host-playbook.md` §§1,5–6]
- `INFERENCE` [E4] **Trap:** stuffing harvested “learnings” into `alwaysApply: true` (or Team-enforced) rules makes them ambient law every chat — conflicts with proposed-only harvest. Premises: (1) alwaysApply always included; (2) Theme 24 O1 never auto-promote; (3) author-cursor-surfaces “thin always-on”.
- `INFERENCE` [E4] **Better rule use for harvest:** short always-on **fence** only (e.g. draft≠SoT), or manual/@ / intelligent rule that points to harvest skill — not the body of new standards. Premises: rules.md types; host-playbook always-on pattern.

### 4.3 Memories

- `FACT` [E1] Documented **Memories** under Automations: agent read/write persistent notes across runs for the **same automation**; default named entry `MEMORIES.md` **outside** the agent’s working filesystem; enabled by default; disable/edit/delete via tool config UI; caution with untrusted input (poisoned memories affect future runs). [E1: Automations — https://cursor.com/docs/cloud-agent/automations.md — Memories — accessed 2026-08-05]
- `FACT` [E1] `https://cursor.com/llms.txt` (accessed 2026-08-05) lists Rules, Skills, Subagents, Hooks under customizing — **no** dedicated IDE “Memories” docs page. [E1: llms.txt index]
- `GAP` Searched: llms.txt, rules/skills/hooks/subagents/customize/prompting/help context, WebSearch for IDE Memories. Result: no primary reference for Agent-chat ambient Memories as workspace skill/standard SoT. Team members help text mentions “Memories” as deletable user data [E2/help adjacency only — not used to lock]. Do **not** invent IDE Memory APIs.
- `INFERENCE` [E4] **Trap:** treating Automations (or undocumented ambient) Memories as host standards law — they are outside repo VCS, auto-writable, and docs warn of malicious/misleading persistence. Premises: automations.md Memories + Theme 24 host-bound skills/standards target.

### 4.4 Hooks

- `FACT` [E1] Hooks are stdio JSON scripts at project (`.cursor/hooks.json`) or user (`~/.cursor/hooks.json`) (also enterprise/MDM paths); can observe, block, or modify agent-loop stages. Events include `sessionStart`/`sessionEnd`, `stop`, `afterAgentResponse`, tool/file gates, `subagentStart`/`subagentStop`, etc. [E1: Hooks — https://cursor.com/docs/hooks.md — accessed 2026-08-05]
- `FACT` [E1] `stop` (and `subagentStop`) may return `followup_message` to **auto-submit** another user message; default `loop_limit` 5 (configurable; `null` = uncapped). Common payload includes `transcript_path` when transcripts enabled. [E1: hooks.md — stop / subagentStop]
- `FACT` [E1] Project hooks run from project root; cloud agents load repo `.cursor/hooks.json` but not user-home hooks. [E1: hooks.md]
- `INFERENCE` [E4] Hooks fit **observe / soft nudge / structured capture** (e.g. on `stop` after closeout: write candidate note or prompt “run harvest?”) — **not** silent auto-accept of standards. Premises: observe/control model; followup can spam if always-on; campaign never auto-promote.
- `INFERENCE` [E4] **Trap:** `stop` + unconditional `followup_message` that instructs Agent to rewrite `.cursor/skills` or standards every completion → always-on auto-write loop. Premises: followup_message behavior + loop_limit.

### 4.5 Subagents

- `FACT` [E1] Subagents: isolated context; project `.cursor/agents/` or user `~/.cursor/agents/`; FM includes `readonly`, `is_background`, `model`. Prefer **skills** for simple single-purpose tasks without isolation need. [E1: Subagents — https://cursor.com/docs/subagents.md — accessed 2026-08-05]
- `FACT` [E1] Docs suggest hooks when subagents should produce structured output files consistently. [E1: subagents.md — best practices]
- `FACT` [E0] Toolbelt author skill: no plugin `agents/` for Task isolation until Cursor documents plugin-agent wire-up (Theme 4 GAP); use runtime Subagent/Task or `/create-subagent` for `.cursor/agents/`. [E0: `skills/author-cursor-surfaces/SKILL.md`]
- `INFERENCE` [E4] Subagents help **research/isolate** harvest analysis (`readonly: true` for propose-only passes) but are not the durable SoT for standards — durable edits still go through host skill/author path + human accept. Premises: subagents.md skill-vs-subagent table; Theme 24 target surfaces.

### 4.6 Context composition (why ambient surfaces matter)

- `FACT` [E1] Prompt context breakdown includes Rules, Skills (descriptions), Subagents docs, etc. — ambient injection competes for the window. [E1: Prompting — https://cursor.com/docs/agent/prompting.md — Context usage — accessed 2026-08-05]
- `FACT` [E1] Customize sidebar manages plugins, rules, skills, subagents, commands, hooks by scope. [E1: Customize — https://cursor.com/docs/customize-cursor.md — accessed 2026-08-05]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Explicit skill (+ optional author scaffolds) is the primary Cursor fit for propose-only harvest | confirmed (docs+E0) | skills.md `disable-model-invocation`; author-cursor-surfaces |
| H2 | Always-on rules / Automations Memories are poor primary SoT for harvested learnings | confirmed for rules; Memories scoped to Automations + GAP for IDE ambient | rules.md alwaysApply; automations.md; llms.txt GAP |
| H3 | Hooks can gate/nudge harvest without writing law if followup is opt-in/gated | open (design) | hooks.md stop/followup; no Toolbelt harvest hook E0 yet |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| “Memories” as IDE feature vs Automations tool | Campaign/user ask lists Memories | Docs: Memories under Automations; no llms.txt IDE page | Prefer documented Automations Memories [E1]; IDE ambient Memories = **GAP** — do not invent |
| docs.cursor.com vs cursor.com/docs | Historical Theme 4 cites cursor.com/docs | `docs.cursor.com` homepage fetch error this pass | Use `cursor.com/docs` + `cursor.com/llms.txt` as working E1 index |

## 7. Gaps & OPEN

- `GAP` IDE Agent-chat **Memories** product surface (create/edit/precedence vs Rules/AGENTS) — not in llms.txt; no API invented.
- `GAP` Exact Cursor build/version for this session — not captured.
- `GAP` Whether `stop` hook + transcript can reliably detect “closeout finished” without false positives — needs E0 experiment (Wave 2 / design), not asserted here.
- `OPEN` AGENTS.md vs Team/Project/User conflict order still Theme 4 residual GAP — do not lock harvest routing on undocumented precedence.
- `OPEN` Plugin-packaged `agents/` ↔ Task wire-up still Theme 4 GAP.

## 8. Implications (INFERENCE only — not design law)

### Best support (propose workspace skill/standard edits, not always-on auto-write)

1. **Host/workspace Skills** with explicit `/` (`disable-model-invocation: true`) or carefully scoped intelligent apply — body = harvest → **proposed** skill/standards/AGENTS deltas via `author-cursor-surfaces` / `author-standards` / AGENTS author path. [E4 from §4.1 + E0 author skill]
2. **Built-in scaffolds** `/create-skill`, `/create-rule`, `/migrate-to-skills` — authoring aids after human accepts a candidate; not ambient law. [E1 skills.md]
3. **Thin Rules / AGENTS.md** — short fences (draft≠SoT) or house pointers; AGENTS for readable host ops (playbook §5). [E1 rules.md + E0 playbook]
4. **Hooks (optional)** — observe `stop` / session boundaries; soft prompt or write **candidate** artifacts; avoid unconditional followup that edits SoT. [E4 from hooks.md]
5. **Subagents** — optional isolated/read-only analysis of session evidence; hand results to author skill. [E1 subagents.md]

### Traps

1. **`alwaysApply: true` (or Team-enforced) rules** as dump for every learning → ambient law every chat. [E1 rules.md]
2. **Automations Memories** (and undocumented IDE Memories) as primary host standards SoT → out-of-repo, auto-writable, poisonable. [E1 automations.md + GAP]
3. **`stop`/`subagentStop` `followup_message` loops** that auto-rewrite skills/standards without human accept. [E1 hooks.md]
4. **Long always-on rules** instead of skills for multi-step harvest (docs + Toolbelt author guidance). [E1 skills migrate notes + E0 author-cursor-surfaces]

## 9. Source list (deduped)

1. https://cursor.com/llms.txt — accessed 2026-08-05
2. https://cursor.com/docs/rules.md — accessed 2026-08-05
3. https://cursor.com/docs/skills.md — accessed 2026-08-05
4. https://cursor.com/docs/hooks.md — accessed 2026-08-05
5. https://cursor.com/docs/subagents.md — accessed 2026-08-05
6. https://cursor.com/docs/customize-cursor.md — accessed 2026-08-05
7. https://cursor.com/docs/cloud-agent/automations.md — accessed 2026-08-05
8. https://cursor.com/docs/agent/prompting.md — accessed 2026-08-05
9. https://cursor.com/help/customization/context.md — accessed 2026-08-05
10. E0: `d:\Toolbelt\skills\author-cursor-surfaces\SKILL.md`
11. E0: `d:\Toolbelt\docs\host-playbook.md` (§§1,5–6 setup/always-on)
12. Scope: `docs/research/notes/theme-24-author-learning/campaign-brief.md` (accepted; not used as Cursor API evidence)
