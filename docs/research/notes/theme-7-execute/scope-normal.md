---
title: "Theme 7 — Execution pocket normal scope (prep for deep brief)"
status: draft
theme: theme-7-execute
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: normal
aligned_with:
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/research/reports/theme-5-design-pocket.md
  - docs/packs/README.md
  - docs/PROTOCOL.md
supersedes: null
---

# Theme 7 — Execution pocket: normal research scope

**Using `research-protocol`**; depth: **normal** (scoping for deep brief — not a deep fleet).

**Status:** `draft`. Not Execution SoT. No skills elevated from this note.

## 1. Scope

- Question / goal: What high-signal GitHub / web / Alexandria evidence exists for **driving cold agents to execute existing plans**, and which community skills are most compatible with Toolbelt’s essence (method over product; Plan already owns plan-writing; quality/readability lean; no Superpowers git/TDD law merge)?
- In scope: Discovery inventory; compatible skill shortlist + what they do; value filters for Toolbelt; inputs for a Theme 7 deep campaign brief.
- Out of scope: Writing Execution skills; locking git/worktree/TDD as Toolbelt law; re-litigating Plan density; deep waves.
- Comprehension / research goal type: reuse (inventory + scoping)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Alexandria `rag_probe`/`rag_query`; GitHub MCP `search_repositories` + `search_code`; `gh search`/`gh api`; WebSearch; WebFetch (partial timeouts); local Read of Superpowers `executing-plans` + `subagent-driven-development` |
| Corpora / URLs searched | Alexandria `ai_llm_agents`, `software_engineering`; github.com (obra/superpowers, OpenSpec apply, BMAD implementation skills, forks); code.claude.com best-practices; cursor.com blog agent best practices / plan mode; OpenAI Codex best practices (fetch timeout) |
| Queries (exact) | RAG: execute existing implementation plan task-by-task verify stop blocked; GitHub repos: `executing-plans OR "writing-plans" OR "agent skills" coding stars:>1000`; code: `filename:SKILL.md executing-plans`; `filename:SKILL.md openspec-apply`; Web: `executing implementation plans coding agents subagents Claude Code Cursor best practices 2025 2026`; `gh api` Superpowers skills list; BMAD `4-implementation` listing |
| What was *not* searched | Full Spec Kit `implement`/`converge` command bodies; ECC / Karpathy CLAUDE.md deep-read; live E0 Toolbelt execute trials; AutoGen/LangGraph product lock comparison; Quality/Verify pocket deep design |
| Depth | normal |
| Waves / stop_reason | N/A (normal). Stop: enough signal to brief deep tracks; further discovery → Theme 7 deep Wave 1 |
| Provenance (optional PROV) | Entity←vendor docs + community skills + Osmani/Huyen/Dibia books; Activity=T7 normal scope; Agent=coordinator |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Named Plan-adjacent systems + opportunistic high-star search; deep-read only execution-specific skills |
| Scope boundary | **Execute existing plans** with cold/fresh agents — not plan authoring (Theme 6), not Design (Theme 5) |

## 4. Findings

### 4.1 Toolbelt essence filter (E0 — framing)

- `FACT` [E0] Toolbelt is a Cursor **agent utility** for research/method + Design + Plan — not Brain/RAG product; packs elevate after accepted research. [E0: `README.md`, `docs/packs/README.md`]
- `FACT` [E0] Theme 6 Plan owns writing hybrid plans for fresh agents; explicitly **not** Implement craft; Superpowers git/TDD/PR not Plan SoT; exec default `serial_implement_review`; status vocab + escalate-on-gap already accepted. [E0: Theme 6 accepted report]
- `INFERENCE` [E4] Execution pocket should add value by teaching **how to drive plan → code → verify → stop/escalate** without becoming a language/framework Build cookbook or importing Superpowers packaging. Premises: essence + Theme 6 non-goals.

### 4.2 GitHub high-signal surfaces (stars = E3 discovery)

| Rank | Project / skill | Stars (approx) | Specificity to *execute existing plans* | Notes |
|------|-----------------|----------------|----------------------------------------|-------|
| 1 | **obra/superpowers** · `executing-plans` | ~264k | **Highest** — dedicated execute-written-plan skill | Load → critical review → task loop → verify → stop/ask; prefers SDD if subagents |
| 1b | **obra/superpowers** · `subagent-driven-development` | same repo | **Highest** — per-task fresh implementer + review | Controller + implementer + task reviewer + final review; continuous exec; finishing-branch handoff |
| 2 | **Fission-AI/OpenSpec** · `openspec-apply-change` | ~63k (repo, T6) | **High** — apply checkbox tasks from change | CLI-driven status/instructions; blocked/all_done states; contextFiles handoff |
| 3 | **bmad-code-org/BMAD-METHOD** · `bmad-build` / `bmad-build-auto` / code-review | ~51k (repo, T6) | **High** — implement stories/specs | Build skill is renderer/CLI-heavy; build-auto plan+HALT already inventoried in Theme 6 |
| 4 | **github/spec-kit** | ~125k (T6) | **Medium** — implement/converge commands adjacent | Plan/tasks owned by Theme 6; execute path not deep-read this pass → GAP for deep |
| 5 | Superpowers **forks** of `executing-plans` | varies | **Low as method** | Diffusion of Superpowers grammar (E3) |
| 6 | **affaan-m/ECC**, **multica-ai/andrej-karpathy-skills** | ~236k / ~198k | **Low for this pocket** | Harness / CLAUDE.md pitfalls — adjacent quality, not plan-exec skills |
| — | interview-university, n8n, vscode, … | very high | **False friends** | Query noise; exclude |

- `FACT` [E0] Local Superpowers `executing-plans`: load plan; critical review + raise concerns; execute tasks with listed verifications; stop on blocker/unclear/repeated verify fail; ask don’t guess; handoff to finishing-branch; couples worktrees + writing-plans. [E0: cache path `…/skills/executing-plans/SKILL.md`]
- `FACT` [E0] Local Superpowers `subagent-driven-development`: fresh implementer per task; task review (spec + quality); fix loop; final branch review; no pause between tasks unless BLOCKED/ambiguity; forbids parallel implementers pattern elsewhere in Superpowers inventory (Theme 6). [E0: `…/skills/subagent-driven-development/SKILL.md`]
- `FACT` [E1] OpenSpec `openspec-apply-change`: select change → `openspec status` → `openspec instructions apply` → implement from task list/contextFiles; handle `blocked` / `all_done`; treat project `context` as required input. [E1: `Fission-AI/OpenSpec` `skills/openspec-apply-change/SKILL.md` via GitHub API 2026-07-30]
- `FACT` [E1] BMAD `bmad-build` skill body is a `uv run …/render.py` launcher (instruction-following via rendered stdout), not a portable markdown execute grammar. [E1: BMAD-METHOD `…/bmad-build/SKILL.md` via GitHub API 2026-07-30]
- `CLAIM` [E3] Stars measure popularity; method acceptance requires E0/E1 corroboration (Theme 6 stance). [E3: discovery ranking]

### 4.3 Most compatible skills — shortlist & what they do

Compatibility = aligns with Toolbelt Plan handoff + cold agents + quality/verify lean − Superpowers git/TDD/worktree law.

| Skill / surface | What it does | Compatibility | Transfer candidates | Park / exclude |
|-----------------|--------------|---------------|---------------------|----------------|
| Superpowers **executing-plans** | Same-session or fresh session: review plan → execute tasks → verify → stop/ask → finish branch | **High structure** | Critical review before code; task loop; stop don’t guess; announce skill | worktrees required; finishing-branch git options as SoT; TDD-in-plan coupling |
| Superpowers **subagent-driven-development** | Controller dispatches fresh implementer per task + reviewer | **High structure** | Per-task fresh context; spec+quality review gates; continuous until blocked; implementer prompt packets | Never-parallel-implementers absolute; commit-every-task; finishing-branch |
| Superpowers **verification-before-completion** | (listed in repo skills; not deep-read) | **Likely high** | Verify-with-evidence before done | Deep-read in Theme 7 |
| Superpowers **requesting-code-review** / **receiving-code-review** | Review request/response loop | **Medium** — Verify pocket adjacent | Fresh-context review | May land Quality/Verify |
| Superpowers **systematic-debugging** | Debug loop when verify fails | **Medium** | Escalate/debug vs invent | Future Debug pocket |
| OpenSpec **openspec-apply-change** | Drive CLI task list to completion | **High for checkbox apply** | Progress ledger; blocked states; context file packs | CLI dependency; schema-specific |
| BMAD **bmad-build** / **build-auto** | Implement from intent/story; HALT on gap | **Medium–high atoms** | HALT/blocked; ready-for-dev; Code Map already in Plan | Renderer/uv packaging; agile ceremony |
| Spec Kit implement/converge | (GAP this pass) | **Unknown pending deep** | Likely story-phase apply | Deep Wave 1 |
| ECC / Karpathy skills | Reduce LLM coding pitfalls | **Low for Execute core** | Optional later quality tips | Not plan-exec |

### 4.4 Web / vendor (E1) — cold agents executing plans

- `FACT` [E1] Claude Code: after a complete spec, **start a fresh session to execute**; self-contained specs + **e2e verification**; give runnable checks; adversarial/fresh subagent review; explore→plan→code separation. [E1: https://code.claude.com/docs/en/best-practices — accessed 2026-07-30]
- `FACT` [E1] Cursor: Plan Mode researches + writes plan; user approves then builds; save plans to workspace for resume / future agents; revert+refine plan often better than patching a wrong build. [E1: https://cursor.com/blog/agent-best-practices — accessed 2026-07-30]
- `CLAIM` [E3] Practitioner pattern: execute by referencing plan task IDs; mark tasks complete in the plan markdown after verify. [E3: Medium Rachel Cantor “How I use Cursor to plan and ship” — discovery only]
- `GAP` OpenAI Codex best-practices page timed out this pass; Goal/Constraints/Done-when already Theme 6 E1 — re-fetch in deep if needed.
- `GAP` Cursor docs `/docs/agent/plan-mode` timed out; blog coverage used.

### 4.5 Alexandria RAG

| Corpus | Probe | Signal for Execute |
|--------|-------|-------------------|
| `ai_llm_agents` | partial | Huyen: plan control flows + **reflection after each step**; ReAct thought/act/observe; Dibia SWE agent: understand → change → **test** → debug; transparency/control/escalation (Raieli) |
| `software_engineering` | partial (Osmani-heavy) | Autonomous agents: **plan → execute → verify → report**; HITL approve steps; well-defined tasks with clear success criteria; trust-but-verify via PR/review |

- `FACT` [E2] Osmani: defining loop for autonomous coding agents is plan / execute / verify / report; verification via tests/build; human reviews results. [E2: Alexandria chunk_ids `eb18ff3000ac18694b4d981d`, `373acdb75e7f59fe7c94a532`, `8288af2502849bd398a94eab` — Beyond Vibe Coding]
- `FACT` [E2] Huyen: reflection after each execution step + after whole plan; error correction paired with reflection. [E2: chunk_id `607ca6bdaea6eba8af862153` — AI Engineering]
- `INFERENCE` [E4] RAG corroborates verify-loop + escalate/HITL; it does **not** yield a Toolbelt-native execute skill grammar (same pattern as Theme 6 paste budget). Premises: partial coverage; book-level principles.

### 4.6 Highest-value Execution pocket candidates (for deep brief)

Ranked by Toolbelt fit (method + quality + Plan handoff − product sprawl):

| Priority | Candidate surface | Why value |
|----------|-------------------|-----------|
| P0 | **`execute-plan` / `implement-plan` skill** | Missing bridge: Theme 6 writes plans; nothing teaches cold-agent execution loop |
| P0 | **Task handoff packet + status ledger update** | Aligns with Plan status vocab + Theme 6 spine/packets |
| P0 | **Stop/escalate rules** (blocked reasons already Plan) | Anti-hallucination at implement time |
| P1 | **Per-task verify + optional fresh reviewer** | Quality/readability lean; Claude adversarial review E1 |
| P1 | **Serial default / parallel-safe respect** | Already Plan law — Execution must enforce, not reinvent |
| P2 | **Debug handoff** when verify fails | Thin pointer; full Debug later |
| P2 | **Finishing / PR packaging** | Prefer Quality/workflow later — do not import Superpowers finishing as Execute SoT |
| Out | Domain Build recipes (React/Unity/…) | Breaks Toolbelt essence |
| Out | Mandatory worktrees/TDD/commit-every-task | Theme 6 + coexistence |

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Community execute grammar clusters on Superpowers execute + SDD + OpenSpec apply | confirmed (discovery) | §4.2–4.3 |
| H2 | Vendor E1 agrees: fresh context, runnable verify, don’t guess | confirmed | §4.4 |
| H3 | RAG alone can specify Toolbelt execute skill shape | rejected | §4.5 principles only |
| H4 | Execution pocket should stay thin vs Plan | open | deep brief / accept |

## 6. Conflicts

| Topic | A | B | Scoping stance |
|-------|---|---|----------------|
| Continuous exec vs HITL between tasks | Superpowers SDD: no pause between tasks | Osmani/Cline: approve steps; Claude: human oversight | Deep: define Toolbelt default (likely serial + verify gate; human on blocked) |
| Verify pocket home | Execute owns Done-when run | Quality owns deep review/TDD | Keep light verify in Execute; deep review later |
| Git/worktree | Superpowers required | Toolbelt coexistence | Exclude from Execute SoT (same as Plan/Design) |

## 7. Gaps & OPEN

- `GAP` Spec Kit implement/converge primary deep-read
- `GAP` Superpowers `verification-before-completion` body
- `GAP` Codex best-practices re-fetch
- `GAP` Live BMAD build-auto implement step (beyond plan HALT)
- `OPEN` Skill name: `execute-plan` vs `implement-plan` vs `executing-plans`
- `OPEN` One skill vs split (in-session controller vs fresh-session executor) like Superpowers execute vs SDD
- `OPEN` How much of Verify/Debug belongs in Theme 7 vs later packs

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Normal scope is **sufficient to brief deep** Theme 7 with tracks: (A) cold-agent execute loop, (B) subagent controller patterns, (C) community execute-skill inventory deepen, (D) Toolbelt Plan↔Execute boundary + value filter. Premises: §§4.2–4.6.
- `INFERENCE` [E4] Do **not** elevate Execution skills from this draft. Premises: `draft-is-not-sot`.

## 9. Source list (deduped)

1. Local Superpowers `executing-plans/SKILL.md`, `subagent-driven-development/SKILL.md` [E0]
2. obra/superpowers skills listing via GitHub API [E1/E3]
3. Fission-AI/OpenSpec `openspec-apply-change/SKILL.md` [E1]
4. bmad-code-org/BMAD-METHOD `bmad-build/SKILL.md` [E1]
5. Claude Code best practices — https://code.claude.com/docs/en/best-practices [E1]
6. Cursor agent best practices — https://cursor.com/blog/agent-best-practices [E1]
7. Alexandria Osmani / Huyen / Dibia / Raieli chunks (ids in §4.5) [E2]
8. Theme 6 accepted report [E0/E2 path]
9. Medium Cantor plan-and-ship [E3]
10. gh search executing-plans forks [E3]

---

## Return summary

Compatible cluster: **Superpowers executing-plans + SDD**, **OpenSpec apply**, **BMAD build atoms**, vendor **fresh session + verify + don’t guess**. Highest Toolbelt value: thin **`execute-plan`** skill that consumes Theme 6 plans, enforces serial/verify/escalate, optional fresh reviewers — without git/TDD/Build recipes. Deep brief: [`campaign-brief.md`](./campaign-brief.md).
