---
title: "T6D W1 — GitHub plan-writing skills inventory"
status: draft
theme: theme-6-plan
created: 2026-07-29
updated: 2026-07-29
authors: [t6d-gatherer]
depth: deep
wave: 1
slice: T6D
aligned_with:
  - docs/research/notes/theme-6-plan/campaign-brief.md
  - docs/research/notes/theme-6-plan/t6-coordinator-pin.md
supersedes: null
---

# T6D W1 — GitHub plan-writing skills inventory

**Using `research-protocol`** · depth: **deep** · wave: **1** · slice: **T6D**.

**Stars = discovery (E3), not acceptance.** No repo locked as Toolbelt SoT. Design skills not elevated here.

## 1. Scope

- Question / goal: Which higher-signal GitHub projects/skills/rules teach **writing plans for coding agents**, and what structures do they share?
- In scope: High-star / highly discussed repos and skills that produce plan/task artifacts for agents; structural patterns (sections, granularity, verify steps); explicit separation of plan-writing vs execution/TDD/git packaging.
- Out of scope: Locking any repo as Toolbelt SoT; Design skills elevation; importing Superpowers git/worktree/TDD/PR policy; ML/robotics “planning”; full W2 corroboration.
- Comprehension / research goal type: reuse (inventory for later Plan pocket design).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebSearch; GitHub MCP `user-github` (`search_repositories`, `search_code`, `get_file_contents`); `gh` (`search repos`, `search code`, `api`, `repo view`); local Read of Cursor-cached Superpowers `writing-plans` |
| Corpora / URLs searched | github.com (obra/superpowers, github/spec-kit, bmad-code-org/BMAD-METHOD, Fission-AI/OpenSpec, forks/derivatives); docs.bmad-method.org (secondary); obra-superpowers / skills.sh listings (secondary) |
| Queries (exact) | Web: `obra/superpowers writing-plans`; `BMAD-METHOD bmadcode agent planning skills`; `github/spec-kit Spec-Driven Development`; `OpenSpec agent skills planning`; `"write-plan" OR "writing-plans" SKILL.md`; GitHub MCP: `repo:obra/superpowers`, `repo:github/spec-kit`, `repo:bmad-code-org/BMAD-METHOD`, `repo:Fission-AI/OpenSpec`; code search `filename:SKILL.md "writing-plans" OR "write-plan"`; `gh search repos "writing-plans"|"spec-kit"|"BMAD-METHOD"|"openspec"|"agent skills plan"` |
| What was *not* searched | Full BMAD story runtime examples in real projects; OpenSpec community schemas beyond default `spec-driven`; Discord/forum discussion volume metrics; Alexandria RAG corpora; non-GitHub marketplaces beyond discovery pointers; exhaustive fork tree of every Superpowers clone |
| Depth | deep |
| Waves / stop_reason | Wave 1 discovery only. `stop_reason`: **diminishing returns** — top four systems (Superpowers writing-plans, Spec Kit plan/tasks, OpenSpec tasks, BMAD epics/stories + build-auto plan) yield primary templates; further hits are mostly Superpowers clones or packaging/orchestration, not new plan-document grammar. Residual +1 deferred to coordinator. |
| Provenance (optional PROV) | Entity←GitHub primary files + star counts 2026-07-29/30; Activity=T6D inventory; Agent=cursor-grok gatherer |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Systematic search of named campaign targets + opportunistic code search for `writing-plans` / `write-plan` skills; deep-read only top structural sources |
| Scope boundary | Plan-*writing* artifacts and instructions; exclude pure execution skills except to demarcate boundary |

## 4. Findings

### 4.1 Ranked inventory (plan-writing specificity × community signal)

Signal ranking prioritizes **specificity to writing plans for coding agents**, then stars/recency as E3 discovery. Star counts accessed via GitHub API / `gh` on 2026-07-29–2026-07-30.

| Rank | Entry | Stars (repo) | Recency | Specificity to *plan writing* | Primary plan artifact path(s) | Grade |
|------|-------|--------------|---------|-------------------------------|-------------------------------|-------|
| 1 | **obra/superpowers** · skill `writing-plans` | ~263k | pushed 2026-07-28 | **Highest** — dedicated skill for implementation plans | `skills/writing-plans/SKILL.md` | E1 content + E3 stars |
| 2 | **github/spec-kit** · `/speckit.plan` + `/speckit.tasks` | ~125k | pushed 2026-07-29 | **High** — splits technical plan vs actionable tasks | `templates/plan-template.md`, `templates/tasks-template.md`, `templates/commands/plan.md`, `templates/commands/tasks.md` | E1 + E3 |
| 3 | **Fission-AI/OpenSpec** · `openspec-propose` → `tasks.md` | ~63k | updated 2026-07-30 | **High** — schema-driven proposal/specs/design/**tasks** | `skills/openspec-propose/SKILL.md`, `schemas/spec-driven/schema.yaml`, `schemas/spec-driven/templates/tasks.md` | E1 + E3 |
| 4 | **bmad-code-org/BMAD-METHOD** · epics/stories + build-auto plan | ~51k | pushed 2026-07-30 | **High** — agile story packets + zero-context implementer specs | `src/bmm-skills/3-solutioning/bmad-create-epics-and-stories/` (+ `templates/epics-template.md`, steps); `src/bmm-skills/4-implementation/bmad-build-auto/step-02-plan.md` + `spec-template.md` | E1 + E3 |
| 5 | **majiayu000/claude-skill-registry** · `validating-plans` | ~524 | updated 2026-07-29 | **Medium** — plan *QA* after writing-plans, not authoring | `skills/testing/validating-plans/SKILL.md` (and mirrors under `skills/data/`) | E1 path + E3 |
| 6 | **Priivacy-ai/spec-kitty** | ~1.5k | updated 2026-07-30 | **Medium-low** — Spec Kit–adjacent SDD + kanban/worktrees (execution packaging heavy) | (repo-level; not deep-read this wave) | E3 discovery |
| 7 | **Superpowers forks / write-plan clones** (many) | varies, usually ≪ parent | varies | **Low as independent method** — mostly copy/adapt `writing-plans` | e.g. code-search hits: `bordenet/superpowers-plus`, `bradspit7/context-skills`, `guanyang/open-agent-hub`, etc. | E3 diffusion |
| 8 | **SixHq/Overture** | ~629 | updated 2026-07-26 | **Low for writing** — visualizes execution plan graph before coding | MCP UI product, not a plan-authoring skill | E3 |
| 9 | **vercel-labs/skills** + **agentskills/agentskills** | ~28k / ~24k | active | **Packaging only** — Agent Skills standard / CLI; not plan grammar | N/A for plan structure | E3 packaging |
| 10 | **anthropics/skills** | ~165k | — | **GAP for this slice** — high stars, no plan-writing skill found in W1 code search | Searched: `filename:SKILL.md plan` in repo → empty | GAP |

- `FACT` [E1] Superpowers `writing-plans` instructs zero-context plans with Goal/Architecture/Tech Stack/Global Constraints header; file map before tasks; Interfaces Consumes/Produces; bite-sized TDD steps with exact commands + expected output; No Placeholders; self-review (spec coverage, placeholder scan, type consistency); then execution handoff to other skills. [E1: obra/superpowers `skills/writing-plans/SKILL.md` — https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md — accessed 2026-07-29]
- `FACT` [E3] Repo `obra/superpowers` has ~263453 stars (API 2026-07-30). Stars measure repo popularity, not acceptance of plan method. [E3: GitHub API `repo:obra/superpowers`]
- `FACT` [E1] Spec Kit separates **plan** (technical context, constitution gates, research/data-model/contracts/quickstart) from **tasks** (checkbox IDs, [P] parallel, [USn] story labels, phases Setup→Foundational→per user story→Polish, independent test per story). Tasks must be “immediately executable” with exact file paths; tests optional unless requested. [E1: github/spec-kit `templates/plan-template.md`, `templates/tasks-template.md`, `templates/commands/tasks.md` — accessed 2026-07-29]
- `FACT` [E3] Repo `github/spec-kit` has ~124520 stars (API 2026-07-30). [E3: GitHub API]
- `FACT` [E1] OpenSpec default schema artifact order is proposal → specs → design → **tasks**; apply tracks checkbox `tasks.md`; tasks are small, dependency-ordered, grouped under numbered headings; design is conditional (architecture/how), specs forbid implementation detail. [E1: Fission-AI/OpenSpec `schemas/spec-driven/schema.yaml`, `skills/openspec-propose/SKILL.md` — accessed 2026-07-29]
- `FACT` [E3] Repo `Fission-AI/OpenSpec` has ~63114 stars (API 2026-07-30). [E3: `gh search repos openspec`]
- `FACT` [E1] BMAD `bmad-create-epics-and-stories` produces `epics.md` with FR inventory, coverage map, epics, and stories (As a/I want/So that + Given/When/Then ACs); stories sized for single dev agent; no forward dependencies within an epic. [E1: BMAD-METHOD `…/bmad-create-epics-and-stories/SKILL.md`, `templates/epics-template.md`, `steps/step-03-create-stories.md` — accessed 2026-07-29]
- `FACT` [E1] BMAD `bmad-build-auto` plan step writes a compact implementer spec: intent-contract (Always/Block If/Never), Code Map (annotated paths), Tasks & Acceptance (`file -- action -- rationale`), Verification commands; aims ~900–1600 tokens; HALT on intent gaps rather than inventing. [E1: `…/bmad-build-auto/step-02-plan.md`, `spec-template.md` — accessed 2026-07-29]
- `FACT` [E3] Repo `bmad-code-org/BMAD-METHOD` has ~51263 stars (API 2026-07-30). [E3: GitHub API]
- `CLAIM` [E3] Community `validating-plans` skills treat plan audit (hallucinations, TDD compliance, drift) as a phase between write-plan and execute-plan. [E3: majiayu000/claude-skill-registry validating-plans SKILL.md via WebSearch/GitHub path — accessed 2026-07-29]
- `FACT` [E0] Local Cursor Superpowers cache contains the same `writing-plans` skill family (aligned with upstream structure). [E0: `…/superpowers/…/skills/writing-plans/SKILL.md`]
- `GAP` W1 code search did not find a dedicated plan-writing skill inside `anthropics/skills` despite very high stars. Searched: `gh search code filename:SKILL.md plan --repo anthropics/skills`.
- `INFERENCE` [E4] Highest *method* signal for Toolbelt Plan pocket is not raw star rank: Superpowers writing-plans + Spec Kit tasks + BMAD story/AC + OpenSpec tasks form a convergent cluster; anthropics/skills and Agent Skills packaging are adjacent infrastructure. Premises: (1) specificity ranking table above; (2) E1 structural overlap in §4.3; (3) campaign brief: stars≠SoT.

### 4.2 Plan-writing method vs execution / TDD / git packaging

| Layer | Examples (inventory) | Keep for Plan pocket scan? |
|-------|----------------------|----------------------------|
| **Plan-writing method** | Header (goal/architecture/stack/constraints); file map; task units with paths; interfaces/consumes-produces; AC / independent test; no placeholders; self-review / readiness gate; FR↔task coverage | **Yes** (structure only) |
| **Execution packaging** | `executing-plans`, `subagent-driven-development`, OpenSpec `openspec-apply-change`, Spec Kit `implement`/`converge`, BMAD build-auto implement step | **No lock** — T6C adjacent; do not import as Plan SoT |
| **TDD ceremony in plan body** | Superpowers red/green/commit steps embedded in every task; Spec Kit tests *optional* unless requested | **Separate** — TDD as verify style ≠ required Plan grammar |
| **Git / worktree packaging** | Superpowers worktrees, frequent commits in plan steps; Spec Kitty worktrees/auto-merge; finishing-branch skills | **Out** — campaign brief non-goal |

- `FACT` [E1] Superpowers writing-plans ends by requiring handoff to `subagent-driven-development` or `executing-plans` — those are execution skills, not plan document structure. [E1: writing-plans SKILL.md Execution Handoff]
- `FACT` [E1] OpenSpec `openspec-apply-change` implements checkboxes from `tasks.md`; it is apply/execution, not task authoring. [E1: `skills/openspec-apply-change/SKILL.md`]

### 4.3 Shared structural patterns (across top hits)

| Pattern | Superpowers writing-plans | Spec Kit plan+tasks | OpenSpec tasks/design | BMAD epics/stories + build-auto |
|---------|---------------------------|---------------------|-----------------------|----------------------------------|
| Spec/design precedes plan | Yes (after brainstorm) | Yes (spec → plan → tasks) | Yes (proposal/specs/design → tasks) | Yes (PRD/architecture → epics; intent → plan spec) |
| Goal / summary header | Goal, Architecture, Tech Stack, Global Constraints | Summary + Technical Context | Via proposal/design; tasks thinner | Intent Problem/Approach + Boundaries |
| File / code map upfront | Explicit File Structure + per-task Files | Project Structure in plan; paths in tasks | Implicit in design; tasks describe work | **Code Map** (annotated paths) |
| Granularity | 2–5 min steps; task = reviewable unit | Phases + T00n tasks; story-independent | One session per task | Story = one agent session; build-auto: prefer one task per file |
| Interfaces / contracts | Consumes/Produces signatures | contracts/ + data-model | Specs = behavior contracts | AC Given/When/Then; I/O matrix |
| Verify steps | Exact Run + Expected FAIL/PASS | Independent Test per story; optional tests | “Each task should be verifiable” | Verification commands + AC |
| Anti-assumption | No Placeholders; self-review | NEEDS CLARIFICATION → research; ERROR on unresolved | Resolve open questions before tasks; no inventing | HALT on intent gap; Block If |
| Parallelism markers | Via execution skills | `[P]` on tasks | Not in default tasks template | Stories independent in sequence |
| Fresh-reader assumption | Explicit zero context | Tasks “without additional context” | Apply reads artifacts from disk | Spec is investigation map for implementer |

- `INFERENCE` [E4] Shared core for agent-readable plans: (1) self-contained facts + constraints, (2) explicit file targets, (3) ordered checkable units, (4) per-unit verify/AC, (5) ban on vague placeholders / unresolved clarifications, (6) coverage map from requirements→tasks/stories. Premises: E1 rows above.

### 4.4 Inventory entries (5–12) — short form

1. **obra/superpowers · writing-plans** — canonical detailed plan skill; richest task template (code-in-plan + TDD).  
2. **github/spec-kit · plan-template + tasks-template** — SDD split of technical plan vs story-phased task list.  
3. **Fission-AI/OpenSpec · openspec-propose + tasks artifact** — schema-enforced artifact DAG ending in trackable tasks.  
4. **bmad-code-org/BMAD-METHOD · create-epics-and-stories** — user-value story packets with AC for Developer agent.  
5. **bmad-code-org/BMAD-METHOD · build-auto plan/spec-template** — compact zero-context implementer plan (Code Map + Always/Block If/Never).  
6. **majiayu000/claude-skill-registry · validating-plans** — post-write plan audit pattern (discovery).  
7. **Priivacy-ai/spec-kitty** — Spec-driven tooling adjacent to Spec Kit (discovery; packaging-heavy).  
8. **Superpowers write-plan forks** — evidence of pattern diffusion; not independent SoT candidates.  
9. **vercel-labs/skills / agentskills/agentskills** — skill distribution standard (infra, not plan method).  
10. **anthropics/skills** — high-star GAP for plan-writing content.  
11. **SixHq/Overture** — plan *visualization* MCP (execution UX, not authoring skill).  

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | High-star agent ecosystems converge on checkbox tasks + exact paths + verify criteria for fresh agents | confirmed (W1 structure) | Superpowers, Spec Kit, OpenSpec, BMAD |
| H2 | Star count alone picks plan-writing SoT | rejected | anthropics/skills high stars, no plan skill found; packaging repos high stars |
| H3 | BMAD stories and Superpowers micro-TDD plans are the same granularity | revised | BMAD stories ≈ session-sized with AC; Superpowers steps ≈ minutes with embedded code — nested levels |
| H4 | Validating-plans is a useful Plan-pocket companion distinct from authoring | open | E3 skill exists; need W2 depth on quality of validators |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Tests mandatory in plan? | Superpowers: TDD steps in every task | Spec Kit: tests optional unless requested | Leave OPEN for Toolbelt — do not lock TDD-in-plan from stars |
| Plan vs Design artifact | Spec Kit `plan` includes design/contracts; OpenSpec separates design.md vs tasks | Superpowers plan embeds architecture + full code | Prefer Toolbelt Design pocket for what/why; Plan for sequenced checkable work (campaign brief) — structural note only |
| Story vs micro-task | BMAD story = agent session | Superpowers task step = 2–5 min | Both valid layers; OPEN how Toolbelt nests them |

## 7. Gaps & OPEN

- `GAP` No dedicated plan-writing skill found in `anthropics/skills` (W1 search).  
- `GAP` Thin primary read of Spec Kitty / forge-sdd / tuncss-plan-kit (low stars or derivative); structure not extracted.  
- `GAP` Discussion/issue heat metrics not collected (stars used as weak E3 proxy only).  
- `GAP` BMAD full example `epics.md` from a real shipped project not fetched (template + steps only).  
- `OPEN` Whether Toolbelt should adopt Superpowers-level code-in-plan vs Spec Kit/OpenSpec thinner tasks + separate design.  
- `OPEN` Whether a `validating-plans` companion belongs in Plan pocket or Verify.  
- `OPEN` W2: corroborate patterns via Alexandria + deeper BMAD story-packet examples named in campaign gap fleet.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] For Theme 6 Plan pocket design later: shortlist **writing-plans (structure)**, **Spec Kit tasks grammar**, **OpenSpec tasks checkbox contract**, **BMAD story AC + build-auto Code Map / Always-BlockIf-Never** as the transferable pattern set — **not** as imported skills/SoT. Premises: §4.1–4.3.  
- `INFERENCE` [E4] Explicitly **exclude from Plan elevation**: git/worktree skills, apply/implement skills, and mandatory TDD ceremony — treat as execution/verify packaging. Premises: §4.2; campaign brief.  
- `INFERENCE` [E4] Do **not** elevate Design skills from this note; Design vs Plan boundary remains Theme 5 / campaign brief. Premises: campaign non-goals.

## 9. Source list (deduped)

1. https://github.com/obra/superpowers — stars ~263453; `skills/writing-plans/SKILL.md`  
2. https://github.com/github/spec-kit — stars ~124520; `templates/plan-template.md`, `templates/tasks-template.md`, `templates/commands/plan.md`, `templates/commands/tasks.md`  
3. https://github.com/Fission-AI/OpenSpec — stars ~63114; `skills/openspec-propose/SKILL.md`, `skills/openspec-apply-change/SKILL.md`, `schemas/spec-driven/schema.yaml`, `schemas/spec-driven/templates/tasks.md`  
4. https://github.com/bmad-code-org/BMAD-METHOD — stars ~51263; `src/bmm-skills/3-solutioning/bmad-create-epics-and-stories/*`, `src/bmm-skills/4-implementation/bmad-build-auto/step-02-plan.md`, `spec-template.md`  
5. https://github.com/majiayu000/claude-skill-registry — stars ~524; `skills/testing/validating-plans/SKILL.md`  
6. https://github.com/Priivacy-ai/spec-kitty — stars ~1452 (discovery)  
7. https://github.com/anthropics/skills — stars ~165100 (GAP for plan-writing)  
8. https://github.com/vercel-labs/skills — stars ~27573 (packaging)  
9. https://github.com/agentskills/agentskills — stars ~23647 (spec)  
10. https://github.com/SixHq/Overture — stars ~629 (visualization)  
11. Local E0: Cursor Superpowers cache `skills/writing-plans/SKILL.md`  
12. Secondary: https://docs.bmad-method.org/reference/commands/ ; https://obra-superpowers.mintlify.app/skills/writing-plans ; GitHub Blog Spec Kit intro  

---

## Return to parent (ranked shortlist + patterns + GAPs)

**Ranked shortlist (plan-writing signal):**  
1) Superpowers `writing-plans` · 2) Spec Kit plan+tasks · 3) OpenSpec tasks (schema) · 4) BMAD epics/stories + build-auto plan · 5) validating-plans (QA companion) · then Spec Kitty / forks / packaging / Overture.

**Shared patterns:** self-contained header/constraints; file/code map; ordered checkbox or story units with paths; verify/AC; anti-placeholder / clarify-before-plan; requirements→task coverage; fresh-agent assumption.

**GAPs:** anthropics/skills has no plan skill found; thin reads on Spec Kitty & low-star plan kits; no discussion-heat metrics; BMAD real epics examples not fetched; OPEN on code-in-plan vs thin tasks and on validating-plans pocket home.

**Out (explicit):** no repo as Toolbelt SoT; no Design skills elevation; stars remain E3 discovery only.
