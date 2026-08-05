---
title: "T6B W1 — Decompose approved design → ordered implementation plan"
status: draft
theme: theme-6-plan
track: T6B
slice: T6B
wave: 1
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-t6b-w1]
supersedes: null
aligned_with:
  - docs/research/notes/theme-6-plan/campaign-brief.md
  - docs/research/notes/theme-6-plan/t6-coordinator-pin.md
  - docs/research/reports/theme-5-design-pocket.md
  - docs/PROTOCOL.md
---

# T6B W1 — Decompose approved design → ordered implementation plan

**Using `research-protocol`**; depth: **deep**; wave: **1**; slice: **T6B**.

**Status:** `draft`. Not Plan SoT. No Plan skill elevation. Does not re-litigate Design (Theme 5 accepted). Superpowers git/exec policy out of scope (E3 structure inventory only if named elsewhere — not used as law here).

## 1. Scope

- **Question / goal:** How to decompose an **approved design** (and the research it rests on) into an **ordered implementation plan** usable by agents (incl. fresh contexts)?
- **In scope:** WBS / task-breakdown / story-slicing methods; mapping design sections → tasks, file ownership, dependencies, acceptance criteria; simple vs complex scaling (atomize); plan vs ADR/design boundary.
- **Out of scope:** Coding-language tutorials; Superpowers as Toolbelt git/PR/TDD law; elevating Plan skills; T6A plan-document self-containment deep dive; T6C multi-agent execution shape locks; T6D community skill inventory; UX planning (T5C deferred); re-researching Design method.
- **Comprehension / research goal type:** other (process methodology research)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebSearch; WebFetch; Alexandria `rag_query` (`software_engineering`, `ai_llm_agents`); local read of Theme 5 pocket + `design-process` skill/checklist + Theme 6 campaign brief/pin + research-note template |
| Corpora / URLs searched | See §9; Alexandria corpora as Method queries |
| Queries (exact) | Web: `PMBOK work breakdown structure WBS decomposition software project official guidance`; `INVEST criteria user stories Bill Wake agile story slicing vertical slice`; `Mike Cohn splitting user stories patterns acceptance criteria Given When Then`; `Nygard Architecture Decision Records what belongs in ADR vs implementation plan`; `PMI Practice Standard Work Breakdown Structures 100% rule work package definition`. Alexandria SE: `How to decompose software design into work breakdown structure tasks work packages dependencies acceptance criteria for implementation planning`. Alexandria AI: `agent task decomposition planning from design specification into ordered implementation steps file ownership` |
| What was *not* searched | Full PMI Practice Standard PDF (paywall); MIL-STD-881F primary text; Mike Cohn book full text; Cucumber/Gherkin primary docs deep dive; Superpowers `writing-plans` as SoT; GitHub plan-skill inventories (T6D); Cursor Plan Mode E0 product behavior; BMAD / story-packet vendor methods; classical critical-path (PERT network) scheduling deep dive |
| Depth | deep |
| Waves / stop_reason | wave: **1** (primary / high-signal E1–E2 + Theme 5 E2 path reuse). Stop for this slice: **wave1_primary_complete** — WBS/INVEST/SPIDR/ADR-boundary cores covered; further W1 vendor-blog chase would restate; Alexandria corroboration deepen + residual “design-section→file-map schema” → W2 |
| Provenance (optional PROV) | Entity←PMI-aligned WBS secondary + Wake/Cohn/Thoughtworks story methods + Nygard ADR + Theme 5 Design path + Alexandria chunks; Activity=T6B W1 gather; Agent=WebSearch/WebFetch/Alexandria + coordinator brief |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Process literature + local Theme 5 path reuse; no codebase recon required for W1 |
| Scope boundary | External E1/E2 + Alexandria E2 + Theme 5 accepted/local Design surfaces as E2 path; no Plan skill elevation |

## 4. Findings

### 4.1 Methods — WBS / task breakdown / story slicing (agent-usable)

- `FACT` [E2] PMBOK-aligned definition: a WBS is a **hierarchical decomposition of the total scope of work** to accomplish objectives and create required deliverables; each descending level is a more detailed definition of project work; lowest planning units are **work packages**. [E2: Wikipedia “Work breakdown structure” summarizing PMBOK — https://en.wikipedia.org/wiki/Work_breakdown_structure — accessed 2026-07-29]
- `FACT` [E2] PMI Practice Standard guidance (as quoted in PMI learning library / Wikipedia): the **100% rule** — WBS includes 100% of scope-defined work and all deliverables (internal, external, interim), including project management; at every level, child work sums to the parent; must not include work outside scope; also applies to activities inside a work package. Elements should be **mutually exclusive** (no overlapping scope). Prefer defining WBS elements as **outcomes/results**, not action laundry lists. [E2: Wikipedia 100% rule section citing Practice Standard — same URL — accessed 2026-07-29; corroborated by PMI “Practice Standard – Work Breakdown Structures” article quoting Haugan/Practice Standard — https://www.pmi.org/learning/library/practice-standard-work-breakdown-structures-8063 — accessed 2026-07-29 (snippet/quote in search+prior PMI library fetch; full PDF paywalled)]
- `FACT` [E2] PMI-aligned process: WBS (deliverable structure) precedes detailed schedule; **Activity Definition → Activity Sequencing → Schedule Development** turn work packages into ordered tasks (WBS ≠ schedule by itself). [E2: Haugan / PMI “Applying work breakdown structure to project lifecycle” — https://www.pmi.org/learning/library/applying-work-breakdown-structure-project-lifecycle-6979 — accessed 2026-07-29]
- `FACT` [E2] Work-package heuristics commonly cited with WBS: stop decomposing when a package can be confidently estimated/managed; common rules of thumb include **≤80 hours** effort at lowest level and/or not longer than one reporting period; PMI defines work package as lowest WBS level for which cost and duration are estimated and managed. [E2: Wikipedia Level of detail / Work package — same URL — accessed 2026-07-29]
- `FACT` [E1] Bill Wake **INVEST** for good stories: Independent, Negotiable, Valuable, Estimable, Small, Testable. Vertical (“multi-layer cake”) slicing: prefer thin slices through layers (network/persistence/logic/presentation) so each slice delivers customer-valuable essence; horizontal layer-only splits often deliver little value until other layers exist. [E1: Bill Wake, “INVEST in Good Stories, and SMART Tasks” — https://xp123.com/invest-in-good-stories-and-smart-tasks/ — accessed 2026-07-29]
- `FACT` [E1] Wake **SMART** tasks (under a story): Specific, Measurable (can mark done — intended behavior, tests, refactoring), Achievable, Relevant to the story, Time-boxed (expectation when to seek help / split). [E1: Wake — same URL — accessed 2026-07-29]
- `FACT` [E1] Mike Cohn **SPIDR** story-splitting techniques: Spike (timeboxed research/prototype to learn enough to implement or further split); Path (alternate workflows); Interfaces (platform/UI progressive fidelity); Data (subset of supported data first); Rules (defer/relax business rules initially). [E1: Mike Cohn, “SPIDR: Five Simple but Powerful Ways to Split User Stories” — https://www.mountaingoatsoftware.com/blog/five-simple-but-powerful-ways-to-split-user-stories — accessed 2026-07-29]
- `FACT` [E1] Cohn: add detail either by **splitting** into sub-stories or by attaching **acceptance criteria**; prefer split when too large for an iteration or when criteria would have **different priorities**; add acceptance criteria when the story stays iteration-sized and criteria share similar priority. [E1: Mike Cohn, “The Two Ways to Add Detail to User Stories” — https://www.mountaingoatsoftware.com/blog/the-two-ways-to-add-detail-to-user-stories — accessed 2026-07-29]
- `CLAIM` [E2] Thoughtworks restates Wake’s vertical cake-slice guidance and lists practical split angles (workflow steps, business rules, happy/unhappy path, data types, input options/platforms, vague terms/conjunctions); notes rigid “every story must alone deliver end-user value” can force oversized stories in multi-system flows — sometimes grow sophistication from simplest transversal slice. [E2: Thoughtworks, “Slicing your development work as a multi-layer cake” — https://www.thoughtworks.com/insights/blog/slicing-your-development-work-multi-layer-cake — accessed 2026-07-29]
- `FACT` [E2] Dooley & Kazakova (SE textbook): need detailed decomposition of features/stories into tasks before reliable effort estimates; break work into tasks completable in **at most a week, ideally 1–2 days**; small stories (≤ one iteration) decompose into tasks ideally **≤8 person-hours**; product owner writes **acceptance criteria** used as acceptance tests / definition of done; if PO cannot write criteria, restart story conversation. [E2: Alexandria corpus=`software_engineering` source=`Software Development, Design, and Coding... (Dooley & Kazakova).pdf` chunk_id=`1c545ae73acd19c9d0a4730c` and chunk_id=`354cdc82c80fb36bc1bc52b8` query=`How to decompose software design into work breakdown structure tasks...`]
- `CLAIM` [E2] Osmani (*Beyond Vibe Coding*): AI may draft a plan/WBS from a feature/user story, suggest subtasks, and **highlight dependencies** so the plan is logically ordered (B after A). Human managers still decide priorities. [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding... (Addy Osmani).epub` chunk_id=`9605dd89df91f04c7f7bafda` query=`How to decompose software design into work breakdown structure tasks...`]
- `FACT` [E2] Agent-planning literature: complex goals require dividing into manageable subtasks; patterns include **task decomposition**, **multi-plan selection**, **reflection/refinement**; decomposition-first (“devise a plan” then “carry out”) vs interleaved decompose/execute — first reduces hallucination/forgetting overview but cannot easily correct mid-plan errors; interleaved adapts but can explode cost on hard problems. [E2: Alexandria corpus=`ai_llm_agents` source=`Mastering AI Agents... (Pratik Bhavsar).pdf` chunk_id=`43c95091f33f7278c1569ab2`; source=`Building AI Agents with LLMs, RAG, and Knowledge Graphs...pdf` chunk_id=`033dc6de1c093929a05e11a8` query=`agent task decomposition planning from design specification...`]
- `CLAIM` [E2] Planner / orchestrator / executor role split: planner breaks goals into actionable steps and parameters; orchestrator assigns/schedules; executor performs steps — plan artifact is distinct from execution. [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh... (Broda).pdf` chunk_id=`d67976e21a81512df64f3a72` query=`agent task decomposition planning...`]
- `INFERENCE` [E4] For **agent-executable** plans after an approved design, a practical stack is: (1) deliverable-oriented WBS / work packages covering 100% of *approved design scope* (no silent extras); (2) slice packages into INVEST-ish vertical increments; (3) further split with SPIDR when a package is still too large or unknown-heavy; (4) under each slice, SMART tasks with explicit done-checks; (5) sequence via dependencies (activity sequencing), not by inventing new product decisions. Premises: WBS 100% + sequencing E2; Wake INVEST/SMART E1; Cohn SPIDR/AC E1; agent decompose E2.

### 4.2 Mapping design sections → tasks, file ownership, dependencies, acceptance criteria

- `FACT` [E2] Theme 5 / `design-process` (accepted Design method): present design **in sections** with human approval per section; scale section length to complexity; for multi-subsystem asks, **decompose into sub-designs first** before deep-designing a platform in one pass; gate before implementation / task planning. [E2 path: `docs/research/reports/theme-5-design-pocket.md` (accepted); `skills/design-process/SKILL.md` steps 2, 6, 11; `skills/design-process/references/design-process-checklist.md` — accessed 2026-07-29]
- `FACT` [E0] Theme 6 campaign brief (draft, non-SoT for Plan locks): Design owns *what/why*; Plan owns *how to sequence checkable work*. [E0: `docs/research/notes/theme-6-plan/campaign-brief.md` §2 — accessed 2026-07-29]
- `INFERENCE` [E4] **Design-section → plan-unit mapping (candidate method, not a lock):** treat each approved design section (or sub-design) as a candidate WBS parent / epic; expand into vertical work packages that realize that section’s deliverables; list **interfaces and constraints** by *linking* to the design/ADR rather than re-deriving options. Premises: (1) sectional design E2 Theme 5; (2) WBS outcome orientation E2; (3) campaign lane split E0.
- `INFERENCE` [E4] **File ownership / touch map:** for each work package or SMART task, name the primary paths (create/modify) and the responsibility of that package (what the files must accomplish). Prefer mutually exclusive ownership at the *task* level where possible (WBS mutual exclusion); when shared files are unavoidable, make the **dependency and merge order** explicit. Premises: WBS mutually exclusive elements E2; Wake SMART “Specific” reduces overlap E1; agent executor needs concrete file/tool actions E2 (Dibia SE-agent tools/prompts — Alexandria `0500925c70044c07eff46c04`).
- `GAP` No W1 E1 standard schema that mandates fields `{design_section_id, files[], owner, deps[], acceptance[]}` for coding agents. Searched: web WBS/story methods + Alexandria agent planning. Result: strong principles, weak portable schema. Follow-up: W2 / T6A artifact shape.
- `FACT` [E1] Acceptance criteria are the confirmation side of story detail (Wake: Cards / Conversation / Confirmation; Cohn: criteria as done-checks). Prefer criteria that make **testability** explicit. [E1: Wake INVEST “Testable” + Jeffries CCC mention — https://xp123.com/invest-in-good-stories-and-smart-tasks/ — accessed 2026-07-29; Cohn add-detail article — Mountain Goat URL above]
- `FACT` [E2] Dooley: acceptance criteria → acceptance tests confirming the story; unclear criteria ⇒ unclear story. [E2: Alexandria `software_engineering` chunk_id=`354cdc82c80fb36bc1bc52b8`]
- `INFERENCE` [E4] **Dependency ordering for agents:** (a) record hard deps (must land before); (b) prefer vertical slices that minimize long horizontal blocking chains; (c) extract Spikes (SPIDR-S) when estimate/approach is blocked on unknowns — spike output is knowledge for later tasks, not the feature itself. Premises: Cohn Spike E1; Thoughtworks horizontal-slice risks E2; PMI activity sequencing after WBS E2.
- `CLAIM` [E2] Parallel/concurrent design literature separates **decomposition** of work from **dependency analysis** and **ordering** of tasks/groups — useful reminder that “list of tasks” ≠ “ordered plan.” [E2: Alexandria corpus=`software_engineering` source=`Software Development, Design, and Coding... (Dooley & Kazakova).pdf` chunk_id=`268fff2c69fab83dae39c693` query=`How to decompose software design...` — parallel Finding Concurrency meta-patterns; apply cautiously outside parallel compute]

### 4.3 Simple vs complex scaling (atomize)

- `FACT` [E2] Theme 5 Design guidance: simple work may use a **short** design + approval; scale presentation length to complexity; multi-independent-subsystem asks → **sub-designs first** (atomize at design time before planning a mega-platform). [E2 path: `docs/research/reports/theme-5-design-pocket.md`; `skills/design-process/SKILL.md` “Simple work…” + scope check + sectional present — accessed 2026-07-29]
- `FACT` [E0] Theme 5 transfer note (draft) retained “decompose-before-deep-design” and “scale-to-complexity” as strengths transferred into Toolbelt Design spine (not Plan elevation). [E0/E2 path: `docs/research/notes/theme-5-design/brainstorm-vs-design-process.md` §3–§5 — accessed 2026-07-29; Design SoT remains Theme 5 pocket]
- `INFERENCE` [E4] **Scaling ladder for Plan (candidate):**

  | Complexity | Design input | Plan shape |
  |------------|--------------|------------|
  | Simple (few files, one clear outcome, accepted short design) | Short approved design / chat decision | Flat ordered SMART task list + acceptance checks; skip deep WBS tree |
  | Medium | Sectional approved design ± ADR | WBS 2–3 levels → vertical slices → SMART tasks; deps + file map |
  | Complex / multi-subsystem | Multiple accepted sub-designs + ADRs | Atomize: one plan (or plan chapter) per sub-design; integrate only at declared interfaces; SPIDR spikes for unknowns |
  Premises: Theme 5 scale/decompose E2; WBS depth heuristics E2; Wake Small/SMART E1; Cohn SPIDR E1.

- `FACT` [E1] Cohn Spike: when approach is unclear, timebox research/prototype **without** delivering the feature; then split/implement with better knowledge. [E1: Cohn SPIDR — Mountain Goat URL — accessed 2026-07-29]
- `FACT` [E2] Agent Mesh / SE: decomposability isolates errors and enables independent test/deploy of units; recursive handoff of subtasks is the agent analogue of modular breakdown. [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh...` chunk_id=`6149f282290bb3ce49e2b7e0`]
- `OPEN` Exact numeric sizing for agent sessions (e.g. “one PR per task”, token budgets) — not locked this wave; human/project heuristic until T6A/T6C corroborate.

### 4.4 Boundary — plan vs ADR / design

- `FACT` [E1] Nygard ADR: records **architecturally significant decisions** (structure, NFRs, dependencies, interfaces, construction techniques); short Context / Decision / Status / Consequences; one significant decision per record; **not** a substitute for large specs; motivation/rationale is the durable value. [E1: Michael Nygard, “Documenting Architecture Decisions” — https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — accessed 2026-07-29]
- `FACT` [E2] Theme 5 elevation: ADR house with Considered Options; draft/proposed ≠ accepted; Design spine ends with human decide + record + HITL gate **before** implement. [E2: `docs/research/reports/theme-5-design-pocket.md` §3, §9 — accessed 2026-07-29]
- `INFERENCE` [E4] **Belong in ADR / accepted design (not reinvented in plan):** problem framing, criteria, options considered, chosen architecture/stack boundaries, NFR commitments, interface contracts at decision level, consequences/constraints agents must not casually reverse. Plan should **cite** these (paths/IDs) and treat them as inputs. Premises: Nygard E1; Theme 5 E2; campaign Design vs Plan E0.
- `INFERENCE` [E4] **Belong in the implementation plan:** ordered work packages/tasks; file/path ownership; dependency edges; per-task or per-slice acceptance checks / verify steps; explicit out-of-scope / do-not-assume; spike tasks for unknowns; sequencing that respects ADR constraints without reopening the options matrix. Premises: WBS→activities E2; Wake SMART E1; Cohn AC E1; campaign brief E0.
- `CLAIM` [E3] Practitioner essays argue ADRs must not become schedules/owners/budgets/roadmaps, and implementation plans are scaffolding that can rot if treated as system description — useful discovery, **not** Toolbelt locks (esp. “never commit plans”). [E3 discovery only: e.g. community ADR hygiene posts — not used as SoT]
- `OPEN` Whether Toolbelt keeps durable plan artifacts in-repo vs ephemeral agent context — product meta-decision; out of T6B W1 locks (touches T6A).

### 4.5 Anti-patterns (design→plan)

- `INFERENCE` [E4] Horizontal-only plans (all DB, then all API, then all UI) conflict with Wake/Thoughtworks vertical-value guidance and tend to defer integration risk. Premises: Wake E1; Thoughtworks E2.
- `INFERENCE` [E4] Re-litigating options inside the plan (new stack choice, new architecture) without returning to Design/ADR violates Theme 5 gate and Nygard’s decision capture purpose. Premises: Theme 5 E2; Nygard E1.
- `INFERENCE` [E4] Plans that omit acceptance/verify steps fail Wake Testable / SMART Measurable and Dooley’s AC→done chain. Premises: Wake E1; Dooley E2.
- `INFERENCE` [E4] Mega-plans for multi-subsystem designs that were not atomized at design time inherit Theme 5’s “one mega-design” anti-pattern into the Plan pocket. Premises: Theme 5 design-process anti-patterns E2.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Deliverable WBS (100% rule) + vertical INVEST slices + SPIDR for oversized/unknowns + SMART tasks is a sufficient method core for agent-usable design→plan | confirmed (as W1 method guidance candidate) | §§4.1–4.3 |
| H2 | Design sections / sub-designs are the right parents for WBS epics after approval | open | Theme 5 sectional design E2; needs W2 schema trials / T6A |
| H3 | Explicit file maps + deps + acceptance per task materially reduce agent assumption/hallucination vs prose-only plans | open | Osmani CLAIM E2; agent planner literature E2; needs E0 Toolbelt trials |
| H4 | ADR/design must stay the options/why SoT; plan must not reopen decisions | confirmed (aligned with Theme 5 + Nygard) | §4.4 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Every story must alone deliver end-user value | Wake Valuable + vertical slice ideal [E1] | Thoughtworks: rigid value-only can force huge multi-system stories; sometimes grow complexity stepwise [E2] | Prefer vertical slices; when integration-heavy, allow thin transversal slices / staged sophistication; do not force horizontal layers. Leave OPEN exact “value vs testability” trade for project criteria |
| WBS outcome nouns vs agile verb stories | PMI: outcomes not actions [E2] | Agile stories/tasks are often action-oriented [E1 Wake/Cohn] | Use WBS for scope completeness (deliverables); use stories/tasks for executable slices under those deliverables — both layers |
| Plan durability in git | E3 “plans ephemeral” essays | Theme 6 candidate elevation of plan templates (campaign brief, non-lock) | **OPEN** — T6A / human meta-decision |

## 7. Gaps & OPEN

- `GAP` Portable agent plan schema (fields for design links, files, deps, AC) — W2 / T6A.
- `GAP` Full PMI Practice Standard PDF / MIL-STD-881F primary — W2 if needed for tighter E1 WBS wording.
- `GAP` Given-When-Then / Cucumber primary as AC syntax standard — optional W2 (Cohn/Wake already establish AC role).
- `OPEN` Numeric sizing for agent sessions / PR granularity.
- `OPEN` Plan artifact retention policy (repo vs ephemeral).
- `OPEN` T6C: how decomposition changes under 1..N executors (handoff packets) — do not lock here.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to Plan skill / SoT without Theme 6 accept + elevation.

- `INFERENCE` [E4] A future `implementation-plan` / write-plan skill should teach: **link approved design+ADR → WBS coverage check → vertical slice → SPIDR if needed → SMART tasks with files/deps/AC → ordered deps** — without importing Superpowers git law or reopening Design options.
- `INFERENCE` [E4] Simple vs complex scaling should mirror Design’s scale-to-complexity: short flat plans for short designs; atomized plans for atomized sub-designs.
- `INFERENCE` [E4] Checklist atoms for W2 synthesis (non-locks): (1) 100% scope vs approved design; (2) no new architecture in plan; (3) vertical over horizontal; (4) each task Specific + Measurable done; (5) unknowns → Spike; (6) cite research/design paths, do not re-derive.

## 9. Source list (deduped)

1. Bill Wake — INVEST / SMART — https://xp123.com/invest-in-good-stories-and-smart-tasks/ — accessed 2026-07-29 [E1]
2. Mike Cohn — SPIDR — https://www.mountaingoatsoftware.com/blog/five-simple-but-powerful-ways-to-split-user-stories — accessed 2026-07-29 [E1]
3. Mike Cohn — Two ways to add detail — https://www.mountaingoatsoftware.com/blog/the-two-ways-to-add-detail-to-user-stories — accessed 2026-07-29 [E1]
4. Michael Nygard — Documenting Architecture Decisions — https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — accessed 2026-07-29 [E1]
5. Wikipedia — Work breakdown structure (PMBOK / Practice Standard summary, 100% rule, work package) — https://en.wikipedia.org/wiki/Work_breakdown_structure — accessed 2026-07-29 [E2]
6. PMI — Practice Standard – Work Breakdown Structures (article) — https://www.pmi.org/learning/library/practice-standard-work-breakdown-structures-8063 — accessed 2026-07-29 [E2]
7. PMI / Haugan — Applying WBS to project lifecycle — https://www.pmi.org/learning/library/applying-work-breakdown-structure-project-lifecycle-6979 — accessed 2026-07-29 [E2]
8. Thoughtworks — Multi-layer cake slicing — https://www.thoughtworks.com/insights/blog/slicing-your-development-work-multi-layer-cake — accessed 2026-07-29 [E2]
9. Theme 5 Design pocket (accepted) — `docs/research/reports/theme-5-design-pocket.md` [E2 path]
10. Toolbelt `design-process` skill + checklist — `skills/design-process/` [E2 path / E0 local]
11. Theme 5 brainstorm-vs-design-process (draft transfer note) — `docs/research/notes/theme-5-design/brainstorm-vs-design-process.md` [E0/E2 path]
12. Theme 6 campaign brief — `docs/research/notes/theme-6-plan/campaign-brief.md` [E0]
13. Alexandria `software_engineering` — Dooley & Kazakova chunks `1c545ae73acd19c9d0a4730c`, `354cdc82c80fb36bc1bc52b8`, `268fff2c69fab83dae39c693` [E2]
14. Alexandria `software_engineering` — Osmani Beyond Vibe Coding chunk `9605dd89df91f04c7f7bafda` [E2]
15. Alexandria `ai_llm_agents` — Bhavsar `43c95091f33f7278c1569ab2`; Raieli/Iuculano `033dc6de1c093929a05e11a8`; Broda `d67976e21a81512df64f3a72`, `6149f282290bb3ce49e2b7e0`; Dibia `0500925c70044c07eff46c04` [E2]
