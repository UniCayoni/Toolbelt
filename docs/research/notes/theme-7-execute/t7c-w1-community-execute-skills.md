---
title: "T7C W1 — Community execute-plan skills: transferable atoms vs park"
status: draft
theme: theme-7-execute
created: 2026-07-30
updated: 2026-07-30
authors: [t7c-gatherer]
depth: deep
wave: 1
slice: T7C
aligned_with:
  - docs/research/notes/theme-7-execute/scope-normal.md
  - docs/research/notes/theme-7-execute/campaign-brief.md
  - docs/PROTOCOL.md
supersedes: null
---

# T7C W1 — Community execute-plan skills: transferable atoms vs park

**Using `research-protocol`**; depth: **deep**; wave: **1**; slice: **T7C**.

**Status:** `draft`. Not Execution SoT. Stars = E3 discovery only. **Standalone Toolbelt** — inspire/cut; no runtime dependency on Superpowers / OpenSpec / Spec Kit / BMAD. Do **not** lock any of these repos as SoT. Do **not** elevate Toolbelt skills from this note.

## 1. Scope

- Question / goal: Deepen high-signal GitHub execute-plan skills into **transferable atoms** vs packaging to **park** (git / TDD / CLI / worktree / finish-branch); rank atoms for Toolbelt main spine vs supplementary broad-use skills.
- In scope: Deep-read of listed skills/commands; atom table; spine vs supplement ranking; GAPs for Wave 2.
- Out of scope: Writing/elevating Toolbelt skills; locking architecture; Theme 6 re-litigation; product/CLI adoption.
- Comprehension / research goal type: reuse

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Local Read (Superpowers cache); GitHub MCP `get_file_contents` + `search_code`; WebFetch (Spec Kit `converge.md` raw) |
| Corpora / URLs searched | Local Superpowers skills; `obra/superpowers` (via local cache = installed copy); `Fission-AI/OpenSpec`; `github/spec-kit`; `bmad-code-org/BMAD-METHOD`; campaign brief §7.1; scope-normal §4.2–4.3 |
| Queries (exact) | `repo:github/spec-kit implement`; `repo:github/spec-kit filename:converge.md`; `repo:bmad-code-org/BMAD-METHOD build-auto`; paths: `skills/openspec-apply-change/SKILL.md`, `templates/commands/implement.md`, `templates/commands/converge.md`, `presets/lean/commands/speckit.implement.md`, `src/bmm-skills/4-implementation/bmad-build-auto/*` |
| What was *not* searched | Full BMAD `step-04-review.md` body (only implement path + docs/reference); Superpowers `finishing-a-development-branch` / `test-driven-development` / `using-git-worktrees` full bodies (integration refs only); ECC/Karpathy; live E0 Toolbelt execute trials; star-count re-verify |
| Depth | deep |
| Waves / stop_reason | Wave 1 slice T7C. Stop: named sources deep-read; diminishing returns on further forks of same Superpowers grammar. Residual → W2 if integrator needs BMAD review-loop detail |
| Provenance (optional PROV) | Entity←community skill texts; Activity=T7C W1 deepen; Agent=t7c-gatherer (Grok) |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Named high-signal surfaces from scope-normal §4.2–4.3; deep-read primary skill/command bodies |
| Scope boundary | Execute-existing-plan grammar only; park product packaging; Theme 6 Plan remains input law |

## 4. Findings

### 4.1 Source deep-reads (primary)

#### Superpowers `executing-plans` [E0]

- `FACT` [E0] Process: load plan → critical review (raise concerns before code) → execute each task with listed verifications → mark complete → hand off to `finishing-a-development-branch`. Stop immediately on blocker / critical gaps / unclear instruction / repeated verify fail; ask, don’t guess. Announce skill at start. Prefer `subagent-driven-development` when subagents exist. [E0: local cache `…/skills/executing-plans/SKILL.md`]
- `FACT` [E0] **Required integration packaging:** `using-git-worktrees`, `writing-plans`, `finishing-a-development-branch`; “Never start implementation on main/master without explicit user consent.” [E0: same]

#### Superpowers `subagent-driven-development` [E0]

- `FACT` [E0] Controller pattern: fresh implementer per task → task reviewer (spec compliance **and** code quality) → fix loop → progress ledger → continuous until BLOCKED / ambiguity / all done → final whole-branch reviewer → finishing-branch. [E0: local `…/subagent-driven-development/SKILL.md`]
- `FACT` [E0] Implementer status vocabulary: `DONE` \| `DONE_WITH_CONCERNS` \| `NEEDS_CONTEXT` \| `BLOCKED`; controller must not ignore escalation or blind-retry same model. [E0: same + `implementer-prompt.md`]
- `FACT` [E0] Durable progress: ledger file (path under `.superpowers/sdd/progress.md`); file handoffs for task brief / report / review-package (avoid paste bloat); pre-flight batched plan conflicts before Task 1; model selection by task complexity; **never** dispatch multiple implementation subagents in parallel. [E0: SKILL.md]
- `FACT` [E0] Task reviewer: two verdicts (spec ✅/❌ + quality Approved/Needs fixes); do not trust implementer report; Critical/Important block next task; plan-mandated defects escalate to human. [E0: `task-reviewer-prompt.md`]
- `FACT` [E0] **Park packaging:** required worktrees + finishing-branch + requesting-code-review; subagents “should use” TDD; commit-as-part-of-implementer job; Superpowers-specific scripts/`sdd` paths. [E0: SKILL.md Integration / Red Flags]

#### Superpowers `verification-before-completion` [E0]

- `FACT` [E0] Iron law: no completion claims without **fresh** verification evidence; gate = identify command → run full command → read output/exit → then claim. Applies before success language, commit/PR, moving to next task, trusting agent reports. [E0: local `…/verification-before-completion/SKILL.md`]

#### Superpowers `requesting-code-review` (relevant) [E0]

- `FACT` [E0] Dispatch fresh-context reviewer with description + plan/requirements + BASE/HEAD SHAs; fix Critical immediately, Important before proceed; used after each SDD task and before merge. [E0: local `…/requesting-code-review/SKILL.md`]
- `INFERENCE` [E4] Atom is Verify/review-adjacent; light use OK in Execute; fuller review deferred per campaign §7.1. Premises: skill description; brief companion note.

#### OpenSpec `openspec-apply-change` [E1]

- `FACT` [E1] Loop: select change → `openspec status --json` → `openspec instructions apply --json` → read `contextFiles` → implement pending tasks → mark `- [ ]` → `- [x]` → continue until done/blocked. States: `blocked` (missing artifacts), `all_done` (suggest archive), else implement. Pause on unclear / design issue / error; don’t guess. Treat CLI `context` as required project input; `operationGuidance` advisory. [E1: `Fission-AI/OpenSpec` `skills/openspec-apply-change/SKILL.md` via GitHub MCP 2026-07-30]
- `FACT` [E1] **Park packaging:** `compatibility: Requires openspec CLI`; store/`openspec/` root schema; Bash allowlist `openspec:*`. [E1: same]

#### Spec Kit `implement` [E1]

- `FACT` [E1] Full template: run prerequisite script → optional checklist completeness gate (HITL if incomplete) → load tasks.md + plan.md (+ optional data-model/contracts/research/constitution) → phase-by-phase execute → respect sequential vs `[P]` parallel → “Follow TDD approach” for test-before-impl → halt on non-parallel failure → mark `[X]` → completion validation vs spec/plan/tests → Done When checklist. Heavy ignore-file setup and extension hooks. [E1: `github/spec-kit` `templates/commands/implement.md` via GitHub MCP 2026-07-30]
- `FACT` [E1] Lean preset collapses to: load feature.json + constitution/spec/plan/tasks → execute in order → mark `- [x]` → halt on failure → validate matches spec. [E1: `presets/lean/commands/speckit.implement.md`]

#### Spec Kit `converge` [E1]

- `FACT` [E1] Post-implement gap closer: assess codebase against spec/plan/tasks (not git history); classify gaps `missing`/`partial`/`contradicts`/`unrequested`; **append-only** `## Phase N: Convergence` tasks; never rewrite existing tasks or edit app code; if clean, leave tasks.md byte-unchanged. Then hand off to implement again. [E1: WebFetch `https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/converge.md` + GitHub path `templates/commands/converge.md` 2026-07-30]
- `INFERENCE` [E4] Converge is a **gap-ledger** atom, not the primary execute loop — better as later review/touchup or optional supplement after first implement pass. Premises: command goal text; Execute pocket = drive approved plans.

#### BMAD `bmad-build-auto` implement path [E1]

- `FACT` [E1] Skill body is `uv run …/render_skill.py` launcher; real grammar in rendered `workflow.md` + steps. Stages: clarify → plan → implement → review; terminal statuses for orchestrators. [E1: `bmad-build-auto/SKILL.md`, `docs/reference/build-auto.md` via GitHub MCP 2026-07-30]
- `FACT` [E1] Status machine: `draft` → `ready-for-dev` → `in-progress` → `in-review` → `done` \| `blocked`; resume routes by status; HALT writes status + blocking condition to durable artifact. [E1: `docs/reference/build-auto.md`, `workflow.md`]
- `FACT` [E1] **Implement step (beyond plan HALT):** require spec_file → capture `baseline_revision` → set `in-progress` → dispatch **synchronous** implementation subagent with spec as sole SoT (handoff must not contradict spec) → run `## Verification` commands → optional matrix test audit → then `step-04-review`. No human questions in implement step. Blocking conditions include `missing spec_file before implementation`, `implementation verification failed`, `matrix test audit failed`, `handoff conflicts with spec`. [E1: `step-03-implement.md`]
- `FACT` [E1] **Park packaging:** uv/renderer dependency; mandatory subagents (`no subagents` → blocked); strongly recommends VCS + clean tree + local commits; epic/story ceremony; review repair loop (docs cite non-convergence after 5 iterations). [E1: build-auto.md, workflow.md, SKILL.md]

### 4.2 Transferable atom table

| Transferable atom | Source(s) | Park (git / TDD / CLI / worktree / finish-branch) |
|-------------------|-----------|---------------------------------------------------|
| Critical plan review before first code; batch concerns | SP executing-plans; SDD pre-flight | — |
| Announce execute skill / mode at start | SP executing-plans; OpenSpec “Using change:” | — |
| Task loop: in_progress → follow steps → verify → complete | SP executing-plans; OpenSpec; Spec Kit lean/full; BMAD implement | — |
| Update durable status ledger / checkboxes in plan or tasks file | OpenSpec; Spec Kit; SDD progress ledger | Park: `.superpowers/sdd/*` path & scripts |
| Run plan/spec-listed verification; evidence before “done” | SP executing-plans; verification-before-completion; BMAD Verify section; Spec Kit completion validation | Park: TDD-as-mandatory law (SP/Spec Kit full) |
| Stop / escalate — don’t guess (blocker, unclear, verify fail, intent gap) | SP executing-plans; OpenSpec pause; Spec Kit halt; BMAD HALT + blocking conditions | Park: BMAD-specific condition enum as SoT |
| Continuous green-path execution (no “should I continue?” every task) | SDD continuous execution; OpenSpec “keep going”; campaign §7.1 HITL | Conflict: Spec Kit checklist HITL before start — optional gate, not every task |
| Fresh implementer context per task (controller crafts packet) | SDD; BMAD implement subagent | Park: mandatory-subagents absolute; SP scripts |
| Implementer status vocabulary (done / concerns / needs context / blocked) | SDD | — |
| Per-task dual review (spec fidelity + quality) with fix loop | SDD task reviewer; requesting-code-review pattern | Park: commit-every-task; final merge packaging |
| File handoffs (brief / report / diff package) over paste | SDD | Park: bash script dependency |
| Model tier by task complexity | SDD | — |
| Serial implementers default (no parallel writers) | SDD “never parallel implementers” | Align with Theme 6 parallel-safe; don’t import absolute without Plan rules |
| Context pack: required files before implement | OpenSpec contextFiles; Spec Kit load list; BMAD spec SoT | Park: OpenSpec CLI schema; Spec Kit FEATURE_DIR scripts |
| Explicit blocked / all_done / resume-by-status machine | OpenSpec states; BMAD status frontmatter | Park: BMAD story/epic ceremony; OpenSpec archive |
| Spec/plan as sole SoT; no invent; conflict → human | BMAD intent-contract + handoff rule; SDD plan-mandated findings | — |
| Post-pass gap append (converge) then re-implement | Spec Kit converge | Park: Spec Kit hooks/prereq scripts; not primary spine |
| Final whole-branch / merge readiness review | SDD → requesting-code-review | Prefer later review touchup; light Execute companion OK |
| Isolation workspace / branch finish options | SP integrations | **PARK:** worktrees required; finishing-a-development-branch as Execute SoT |
| Mandatory TDD red-green for every task | SDD subagents; Spec Kit full “Follow TDD” | **PARK:** TDD law |
| Product CLI / renderer as runtime | OpenSpec CLI; BMAD uv render; Spec Kit `{SCRIPT}` prereqs | **PARK:** CLI / worktree / finish-branch packaging |

### 4.3 Ranked fit — main spine vs supplementary

Directional OPENs from campaign §7.1 applied: Toolbelt-native naming; main spine + supplements; escalate on major deviation/blocked (not pause every green task); light verify companion OK; no dependency.

#### Main spine candidates (feed `execute-plan` / `implement-plan`)

Ranked by Toolbelt fit (faithfulness × thin method × Plan handoff × standalone):

| Rank | Atom | Why spine |
|------|------|-----------|
| 1 | Load plan → critical review → raise/batch concerns → then code | Prevents cold agents from executing a bad plan; SP + SDD |
| 2 | Task loop with status updates in the plan/tasks artifact | Plan status vocab compatibility; OpenSpec/Spec Kit/SDD ledger |
| 3 | Done-when / plan-listed verify + evidence-before-completion claims | Quality lean without importing TDD law |
| 4 | Stop/escalate don’t guess (blocked reasons: unclear, verify-fail, intent-gap, major deviation) | Anti-hallucination; aligns §7.1 HITL |
| 5 | Continuous green-path (no per-task human pause when green) | §7.1; SDD/OpenSpec |
| 6 | Required context pack before implement (plan + task + constraints files) | OpenSpec contextFiles / Spec Kit load / BMAD SoT — without their CLIs |

#### Supplementary broad-use skills (esp. subagent-driven patterns)

| Rank | Atom / skill shape | Why supplement |
|------|--------------------|----------------|
| 1 | Controller + fresh implementer per task + implementer status vocab | Broad-use across nearly all multi-task plans (T7B overlap); SDD core |
| 2 | Per-task spec+quality review + Critical/Important fix gate | Quality lean; optional when subagents available |
| 3 | Durable progress ledger for resume/compaction | Operational reliability; path should be Toolbelt-native, not `.superpowers` |
| 4 | File handoff packets (brief/report/diff) | Prevents context pollution; drop SP scripts or reimplement thinly |
| 5 | Model tiering by mechanical vs judgment tasks | Cost/quality; optional |
| 6 | Light final fresh-context review (or pointer to later review work) | requesting-code-review atom; don’t import finishing-branch |
| 7 | Converge-style append-only gap tasks after a first pass | Spec Kit; later review/touchup more than core Execute |

#### Park / exclude from Toolbelt Execute SoT

| Packaging | Sources | Stance |
|-----------|---------|--------|
| Required git worktrees | SP execute + SDD | Park (coexistence; Theme 6) |
| finishing-a-development-branch as required sub-skill | SP | Park — workflow/PR later |
| Commit-every-task / local-commit mandates | SDD implementer; BMAD | Park as law; optional project practice |
| Mandatory TDD | SDD; Spec Kit full | Park |
| OpenSpec CLI / store schema | OpenSpec | Park — inspire checkbox/status atoms only |
| BMAD uv renderer + agile story ceremony | BMAD | Park — inspire HALT/status/verify atoms only |
| Spec Kit prereq scripts, ignore-file bootstrap, extension hooks | Spec Kit full | Park — lean loop atoms only |
| Never-start-on-main absolute as Execute skill law | SP | Park or thin safety tip — not pocket SoT |
| Stars-as-method-acceptance | discovery ranking | E3 only |

### 4.4 Cross-source synthesis

- `CLAIM` [E3] High-star repos remain discovery signals; method acceptance needs E0/E1 bodies (this pass). [E3: scope-normal §4.2 stance]
- `INFERENCE` [E4] Community execute grammar **clusters** on: review→task loop→verify→ledger→stop/escalate; subagent controller is the main **broad-use** fork; CLI/status machines (OpenSpec/BMAD) and converge are packaging variants of the same atoms. Premises: §§4.1–4.3.
- `INFERENCE` [E4] Toolbelt should **not** depend on any of these projects; extract atoms into native skills after accept. Premises: campaign essence filter; draft-is-not-sot.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Superpowers execute + SDD remain highest-structure execute grammars | confirmed (this pass) | §4.1 E0 deep-reads |
| H2 | OpenSpec/BMAD add portable status/ledger/HALT atoms despite CLI/renderer packaging | confirmed | §4.1 E1 |
| H3 | Spec Kit implement is medium specificity; lean form is closer to Toolbelt thin spine | confirmed | lean vs full implement |
| H4 | Spec Kit converge belongs in Execute core | rejected for spine; open as supplement/later | §4.1 converge goal |
| H5 | verification-before-completion is a high-value light companion atom | confirmed | §4.1 E0 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| HITL between tasks | SDD/OpenSpec: continuous when green | Spec Kit: checklist HITL before implement; Osmani-style approve-steps (scope-normal) | Prefer §7.1: escalate on blocked/major deviation only; optional preflight checklist is not per-task pause |
| Parallel tasks | Spec Kit `[P]` parallel allowed | SDD: never parallel implementers | Prefer Theme 6 parallel-safe rules; default serial writers |
| Verify home | Execute Done-when + verification-before-completion | requesting-code-review / BMAD review step | Light verify in spine; deep review → later touchup/pocket |
| Git/worktree/finish | SP required | Toolbelt standalone | Park packaging |

## 7. Gaps & OPEN

- `GAP` BMAD `step-04-review.md` full body (repair loop, deferred findings detail) — only docs/reference + implement step this pass. Searched: step-03 + build-auto.md. Result: implement path closed; review packaging residual for W2/T7D.
- `GAP` Superpowers `finishing-a-development-branch` / `using-git-worktrees` / `test-driven-development` bodies not re-deep-read (integration refs only). Result: park stance from Integration sections; fine-grained options unlisted.
- `GAP` Live star counts / fork diffusion not re-measured (scope-normal E3 stands).
- `GAP` ECC / Karpathy intentionally out (low execute specificity).
- `OPEN` Exact Toolbelt ledger path/filename (not `.superpowers/sdd/`).
- `OPEN` Whether converge-style pass is Execute supplement vs later review work.
- `OPEN` How strictly serial-implementers is stated vs Theme 6 parallel-safe (T7B/T7D).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] **Do not elevate** Toolbelt skills from this draft; **do not** lock Superpowers/OpenSpec/Spec Kit/BMAD as SoT. Premises: draft-is-not-sot; campaign non-goals.
- `INFERENCE` [E4] Highest-value extraction for main spine: critical review + task loop + ledger + evidence-verify + escalate-on-blocked + continuous green-path + context pack — Toolbelt-native wording. Premises: §4.3.
- `INFERENCE` [E4] Highest-value supplement: SDD-like controller (fresh implementer, status vocab, optional per-task dual review, file handoffs, resume ledger) without worktree/TDD/finish-branch coupling. Premises: §4.3; §7.1 one-skill-vs-two.

## 9. Source list (deduped)

1. Local Superpowers `executing-plans/SKILL.md` [E0]
2. Local Superpowers `subagent-driven-development/SKILL.md` + `implementer-prompt.md` + `task-reviewer-prompt.md` [E0]
3. Local Superpowers `verification-before-completion/SKILL.md` [E0]
4. Local Superpowers `requesting-code-review/SKILL.md` [E0]
5. Fission-AI/OpenSpec `skills/openspec-apply-change/SKILL.md` [E1]
6. github/spec-kit `templates/commands/implement.md` [E1]
7. github/spec-kit `presets/lean/commands/speckit.implement.md` [E1]
8. github/spec-kit `templates/commands/converge.md` [E1]
9. bmad-code-org/BMAD-METHOD `docs/reference/build-auto.md` [E1]
10. bmad-code-org/BMAD-METHOD `src/bmm-skills/4-implementation/bmad-build-auto/{SKILL.md,workflow.md,step-03-implement.md}` [E1]
11. scope-normal.md §4.2–4.3; campaign-brief.md §7.1 [E0 framing]

---

## Return to parent (ranked atoms + GAPs)

### Main spine atoms (ranked)

1. Critical plan review (batch concerns) before code  
2. Task loop + durable status/checkbox ledger in plan artifact  
3. Plan/spec-listed verify + evidence-before-completion  
4. Stop/escalate don’t guess (blocked / unclear / verify-fail / intent-gap / major deviation)  
5. Continuous green-path (HITL only when blocked/major deviation)  
6. Required context pack (plan + task + constraints) without foreign CLI  

### Supplementary broad-use atoms (ranked)

1. Controller + fresh implementer per task + status vocab (`DONE` / concerns / needs context / blocked)  
2. Per-task spec+quality review + Critical/Important fix gate  
3. Toolbelt-native progress ledger for resume/compaction  
4. File handoff packets (brief/report/diff)  
5. Model tiering by task complexity  
6. Light final fresh-context review (or defer to later review work)  
7. Converge-style append-only gap tasks (optional / later)

### Park

worktrees-required · finishing-branch SoT · commit-every-task law · mandatory TDD · OpenSpec/BMAD/Spec Kit CLI-renderer-hooks packaging · stars-as-acceptance

### GAPs for W2 / integrator

- BMAD `step-04-review` deep-read residual  
- SP finishing/worktree/TDD bodies if park nuances matter  
- OPEN: ledger path; converge home (Execute vs later review); serial vs Plan parallel-safe wording  

**Out:** locking any community repo as SoT; elevating Toolbelt skills from this draft.
