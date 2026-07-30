---
title: "T6-W3 +1 RESIDUAL — paste/link tiers, validation atoms, design→plan consume"
status: draft
theme: theme-6-plan
created: 2026-07-29
updated: 2026-07-29
authors: [t6-w3-plus1-residual-grok]
supersedes: null
aligned_with:
  - docs/research/notes/theme-6-plan/campaign-brief.md
  - docs/research/notes/theme-6-plan/t6-coordinator-pin.md
  - docs/research/notes/theme-6-plan/t6-w2-rag-schema-paste-link.md
  - docs/research/notes/theme-6-plan/t6-w2-gap-community-templates.md
  - docs/research/notes/theme-6-plan/t6-w2-exec-shape-serial-parallel.md
  - docs/research/reports/theme-5-design-pocket.md
  - docs/PROTOCOL.md
---

# T6-W3 +1 RESIDUAL — paste/link tiers, validation atoms, design→plan consume

**Using `research-protocol`**; depth: **deep**; wave: **3**; slice: **T6-PLUS1-RESIDUAL**; stop intended: **low_return_plus_one**.

**Status:** `draft`. Not Plan SoT. **No skill elevation.** Does not reopen Theme 5 Design. Does **not** import Superpowers git/TDD as Toolbelt law. validating-plans deep `references/*.md` remain unavailable (W2 GAP retained).

## 1. Scope

- Question / goal: One residual (+1) pass after W2 diminishing returns — attempt to close or harden three P0/P1 residual items, then stop even if still GAP.
- In scope:
  1. Paste-vs-link / progressive disclosure from Anthropic + Cursor/Claude primary docs; if no numeric budget, durable GAP + labeled E4 tier *candidates*
  2. Plan validation / anti-hallucination **checkable atoms** from Claude best practices, Spec Kit, BMAD, OpenSpec, validating-plans SKILL.md summary only (no elevation of validating-plans skill)
  3. Design→plan handoff consume fields from local Toolbelt `design-process` + Theme 5 accepted report (E0/E2) — no Design re-research
- Out of scope:
  - Elevating Plan / validating-plans / Superpowers skills
  - Wave-3 fleet expansion; further Alexandria RAG on paste/schema
  - Inventing numeric token budgets without E1
  - Re-opening Theme 5 Design method locks
- Comprehension / research goal type: other (residual GAP closers)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Read (research-protocol + note template; W2 notes skim; `skills/design-process/SKILL.md` + checklist; Theme 5 report); WebSearch; WebFetch (Anthropic context engineering, Anthropic Agent Skills engineering, Anthropic skills best-practices, Claude Code best-practices, Cursor prompting); GitHub MCP `get_file_contents` (Spec Kit plan-template + plan command; OpenSpec schema.yaml; BMAD step-02-plan; validating-plans SKILL.md) |
| Corpora / URLs searched | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ; https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills ; https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/best-practices ; https://code.claude.com/docs/en/best-practices ; https://cursor.com/docs/agent/prompting ; https://cursor.com/help/customization/context (timeout); github.com/github/spec-kit ; bmad-code-org/BMAD-METHOD ; Fission-AI/OpenSpec ; majiayu000/claude-skill-registry validating-plans |
| Queries (exact) | Web: `Anthropic context engineering for AI agents include vs reference progressive disclosure 2025`; `Claude Code best practices self-contained context verify plan`; `Cursor docs context @files reference vs paste agent prompts progressive disclosure`; `Anthropic agent skills progressive disclosure SKILL.md metadata load on demand`. GitHub paths: `templates/plan-template.md`, `templates/commands/plan.md`, `schemas/spec-driven/schema.yaml`, `…/bmad-build-auto/step-02-plan.md`, `skills/testing/validating-plans/SKILL.md` |
| What was *not* searched | Fresh Alexandria RAG (W2 `rag_diminishing_returns`); PMI Practice Standard PDF; validating-plans `references/*.md` (known 404); E0 paste-heavy vs link-heavy plan trials; Cursor Task API internals; full Spec Kit constitution examples |
| Depth | deep |
| Waves / stop_reason | wave: **3**; slice: **T6-PLUS1-RESIDUAL**. `stop_reason`: **low_return_plus_one** — new E1 mostly restates W1/W2 (JIT identifiers, progressive disclosure, self-contained specs, NEEDS CLARIFICATION / HALT / reality-check). Numeric paste budget **still GAP**. Design→plan consume table is E0/E2 synthesis (no new Design research). Further gatherers would restate without closing named P0 GAPs. |
| Provenance (optional PROV) | Entity←Anthropic/Claude/Cursor E1 + community template E1 + local Design E0/E2; Activity=T6-W3 +1 residual; Agent=cursor-grok gatherer |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Residual closers need fresh primary fetch (systematic) + local Design path read (as-needed); no Design re-research |
| Scope boundary | Three named residual attacks only; stop after this note |

## 4. Findings

### 4.0 W2 residual targets (skim)

| W2 note | Residual carried into this pass |
|---------|----------------------------------|
| `t6-w2-rag-schema-paste-link.md` | Paste-vs-link **numeric/policy budget** still GAP; portable schema candidate bag only |
| `t6-w2-gap-community-templates.md` | Spec Kit / BMAD / OpenSpec grammar E1; validating-plans `references/*.md` **404**; anti-assumption gates (NEEDS CLARIFICATION / HALT) |
| `t6-w2-exec-shape-serial-parallel.md` | Serial vs parallel criteria closed as guidance candidates; `[P]` token name still GAP — **not re-attacked** here |

### 4.1 Paste-vs-link / progressive disclosure (attempt once more)

#### 4.1.1 Primary principles (re-fetch + deepen)

- `FACT` [E1] Anthropic: treat context as a finite **attention budget**; prefer the **smallest set of high-signal tokens** that still fully outlines expected behavior (“minimal ≠ short”). [E1: Effective context engineering for AI agents — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — accessed 2026-07-29]
- `FACT` [E1] Anthropic: **just-in-time** agents keep **lightweight identifiers** (file paths, stored queries, web links) and load data at runtime via tools; enables **progressive disclosure** — discover context layer by layer rather than preloading exhaustive material. [E1: same — accessed 2026-07-29]
- `FACT` [E1] Anthropic hybrid example: Claude Code drops `CLAUDE.md` **up front** while using glob/grep for **JIT** file retrieval. [E1: same — accessed 2026-07-29]
- `FACT` [E1] Anthropic Agent Skills: progressive disclosure has **three levels** — (1) YAML `name`/`description` always in system prompt; (2) `SKILL.md` body loaded when relevant; (3) additional linked files read only as needed. [E1: Equipping agents for the real world with Agent Skills — https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills — accessed 2026-07-29]
- `FACT` [E1] Anthropic Skills best practices: keep `SKILL.md` body under **~500 lines** for performance; move detail to linked reference files; keep references **one level deep** from `SKILL.md`; for reference files **>100 lines**, include a table of contents. [E1: Agent Skills best practices — https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/best-practices — accessed 2026-07-29]
- `FACT` [E1] Claude Code: most useful specs are **self-contained** — name **files and interfaces**, state **out of scope**, end with an **end-to-end verification** step; then execute in a **fresh session**. [E1: Best practices — https://code.claude.com/docs/en/best-practices — accessed 2026-07-29]
- `FACT` [E1] Claude Code CLAUDE.md guidance (project memory): include commands/style/workflow; do **not** put long explanations/tutorials in always-loaded memory (prefer architectural decisions that cannot be inferred). [E1: same best-practices — CLAUDE.md section — accessed 2026-07-29]
- `FACT` [E1] Cursor: `@` mentions attach specific files/folders/docs when you **know** what is relevant; if unsure, skip — Agent finds files via search; context window is fixed and compresses when full. [E1: Prompting agents — https://cursor.com/docs/agent/prompting — accessed 2026-07-29]
- `GAP` Cursor help page `https://cursor.com/help/customization/context` **timed out** this pass; prompting doc above used as E1 for `@` attach behavior. Searched: WebFetch help URL 2026-07-29. Result: timeout — no additional paste-budget wording obtained.

#### 4.1.2 Durable GAP — numeric paste budget

- `GAP` **Durable:** No E1 (Anthropic / Claude Code / Cursor) states a universal **numeric** plan↔ADR/design paste budget (N lines, N tokens, or % of context) for coding-agent briefs. Searched this wave: Anthropic context engineering + Agent Skills progressive disclosure + Claude best practices + Cursor prompting; W1/W2 already negative. Result: **principles yes; numeric budget no.** Closing needs E0 Toolbelt trials or an accepted house convention — not another primary-doc pass.
- `INFERENCE` [E4] Skills “~500 lines / >100-line TOC” guidance is **not** a Plan paste budget; it is sizing for skill progressive disclosure. Premises: Skills best-practices FACT; GAP on plan budgets.

#### 4.1.3 E4 tier *candidates* (INFERENCE only — not locks)

Labeled **INFERENCE** / guidance candidates for a future Plan template. **Do not elevate.**

| Tier | Candidate contents | Load style | Premises |
|------|-------------------|------------|----------|
| **T0 always-inline** (hot brief) | Goal / objective; binding **constraints** + **do-not**; **interfaces/consumes-produces** needed to execute; **out-of-scope**; **verify / done-when** (runnable check + expected signal); task order + file touch list for *this* packet | Paste or restate in plan / task handoff | Claude self-contained FACT; Anthropic “minimal set that fully outlines behavior” FACT; Codex Goal/Constraints/Done-when [E1 W1] |
| **T1 index / locator** | Paths + section IDs + one-line “what to extract” (e.g. `docs/adr/0007-….md` §Decision; design note §Interfaces) | Lightweight identifiers in plan; agent reads on demand | Anthropic JIT identifiers FACT; progressive disclosure FACT; Cursor `@` when known FACT |
| **T2 link+extract (cold body)** | Full ADR options matrices, long design rationale, research notes, large code dumps | Link + explicit extract instruction; do **not** require re-deriving Decision | Anthropic progressive disclosure + Skills L3 linked files FACT; W1/W2 hybrid INFERENCE |
| **T3 never-inline in worker brief** | Unrelated chat history; full exploration traces; laundry-list edge rules; entire monorepo | Omit; isolate via fresh subagent + selective packet | Anthropic no false shared context [E1 W1]; subagent clean context [E1 W1/W2]; Claude fresh-session FACT |

- `INFERENCE` [E4] **Candidate policy (non-lock):** treat T0 as mandatory self-containment for fresh agents; T1/T2 for Design/ADR/research bodies; reject “link-only ADR with no Decision/Interfaces restated” as insufficient for coding workers. Premises: Claude self-contained FACT; Anthropic JIT+progressive disclosure FACT; durable numeric GAP above; T6A W1 INFERENCE.

### 4.2 Plan validation / anti-hallucination checklist atoms

Extract **checkable atoms** from primary sources. **Do not elevate** validating-plans skill (W2: `references/*.md` 404). Exclude Superpowers TDD/git/issue packaging from Plan-law candidates.

#### 4.2.1 Claude — self-contained + verify

- `FACT` [E1] Self-contained checklist atoms: (a) name **files**; (b) name **interfaces**; (c) state **out of scope**; (d) end with **e2e verification** that proves the feature works. [E1: Claude Code best practices — accessed 2026-07-29]
- `FACT` [E1] Verification atom: give Claude a **check it can run** (tests, build, screenshot compare) producing pass/fail; “if you can’t verify it, don’t ship it.” [E1: same — accessed 2026-07-29]
- `FACT` [E1] Fresh-context atom: after writing a complete spec, start a **fresh session** to execute. [E1: same — accessed 2026-07-29]

#### 4.2.2 Spec Kit — NEEDS CLARIFICATION + gates

- `FACT` [E1] Technical Context fields may be marked **`NEEDS CLARIFICATION`**; Phase 0 research must **resolve all** NEEDS CLARIFICATION into `research.md` (Decision / Rationale / Alternatives). [E1: github/spec-kit `templates/plan-template.md`, `templates/commands/plan.md` — accessed 2026-07-29]
- `FACT` [E1] **Constitution Check** is a gate (before Phase 0; re-check after Phase 1); key rule: **ERROR on gate failures or unresolved clarifications**. [E1: same — accessed 2026-07-29]
- `FACT` [E1] Quickstart validation guide: runnable scenarios + expected outcomes; **do not** embed full implementation code in that artifact. [E1: `templates/commands/plan.md` Phase 1 — accessed 2026-07-29]

#### 4.2.3 BMAD build-auto — HALT + ready-for-dev

- `FACT` [E1] On **intent gaps** (multiple defensible readings → observably different outcomes, nothing in intent to select): **do not fantasize** / **do not leave open questions** — **HALT** with status `blocked`, blocking condition `intent gap`, include unanswered questions + evidence. [E1: BMAD-METHOD `…/bmad-build-auto/step-02-plan.md` — accessed 2026-07-29]
- `FACT` [E1] Ready-for-development gate: set status `ready-for-dev` or HALT (`spec failed ready-for-development standard` after one repair attempt). [E1: same — accessed 2026-07-29]
- `FACT` [E1] Intent-contract tiers (from W2 primary, not re-fetched body this pass): **Always** / **Block If** / **Never** + Code Map + Verification — compact anti-assumption surface. [E1: W2 note citing `spec-template.md`; this pass re-confirmed HALT/gate via step-02-plan.md]

#### 4.2.4 OpenSpec — readiness before tasks / apply

- `FACT` [E1] Design **Open Questions**: only defer unknowns that will **not** change specs, approach, or task breakdown; otherwise resolve / ask — do not guess. [E1: Fission-AI/OpenSpec `schemas/spec-driven/schema.yaml` design instruction — accessed 2026-07-29]
- `FACT` [E1] Tasks instruction: before writing tasks, if design Open Questions would change what gets built, **resolve with user first** — do not bake unstated assumptions into the task list; each task **verifiable**. [E1: same schema.yaml tasks instruction — accessed 2026-07-29]
- `FACT` [E1] Apply requires `[tasks]`; artifact order proposal → specs → design → tasks; `openspec validate` rejects zero-delta changes unless `skip_specs: true`. [E1: same schema.yaml — accessed 2026-07-29]

#### 4.2.5 validating-plans — SKILL.md atoms only (refs still GAP)

- `FACT` [E1] SKILL.md Reality Check Verifier checks (summary): file existence + line numbers; package registry existence; API signatures/exports; imports; command availability. Severity: BLOCKER / CRITICAL / WARNING / NIT. Verdicts: PASS | PASS WITH NOTES | NEEDS REVISION. Todos fix **the plan**, not the code. [E1: majiayu000/claude-skill-registry `skills/testing/validating-plans/SKILL.md` — accessed 2026-07-29]
- `FACT` [E1] Drift Detector (summary): files changed after plan; uncommitted tree; dependency file updates; drift risk. [E1: same]
- `GAP` Deep checklist bodies in `references/validating-plans-*.md` still **not published** (W2 confirmed 404). This pass: did **not** re-fetch refs (known dead); used SKILL.md summaries only. **Do not elevate** skill; transferable atoms = reality-check + drift + severity gates — **not** TDD Compliance Auditor / commit / gh-issue packaging as Plan SoT.
- `CLAIM` [E3] TDD Compliance Auditor + GitHub issue packaging remain Superpowers-coupled community process — inventory only. [E3: same SKILL.md — not Toolbelt Plan law]

#### 4.2.6 Consolidated checkable atoms (INFERENCE synthesis)

- `INFERENCE` [E4] **Candidate pre-execution validation checklist** (structure only; not elevated):

  | # | Atom | Source grades |
  |---|------|---------------|
  | V1 | No unresolved clarifications / intent gaps (halt or ERROR — don’t invent) | Spec Kit E1; BMAD E1; OpenSpec E1 |
  | V2 | Self-contained: files + interfaces + out-of-scope + verify step present | Claude E1 |
  | V3 | Verify step is **runnable** with expected pass/fail signal | Claude E1; BMAD Verification (W2); Spec Kit quickstart E1 |
  | V4 | Reality-check: cited files/packages/APIs/commands exist | validating-plans SKILL.md E1 (summary) |
  | V5 | Drift check if plan is stale vs tree/deps | validating-plans SKILL.md E1 |
  | V6 | Design Open Questions that change build are closed before tasks | OpenSpec E1 |
  | V7 | Binding constraints / Always·Block-If·Never (or equivalent do-not) explicit | BMAD W2 E1; T6A Constraints cluster |
  | V8 | No full impl-code dump required in plan/quickstart (thin-task arm) | Spec Kit E1 — **conflicts** with Superpowers code-in-plan [E1 W2]; leave OPEN |

  Premises: §§4.2.1–4.2.5. **Exclude from elevation:** mandatory TDD 5-step, git commit ceremony, GitHub issue creation.

### 4.3 Design→plan handoff — what plans should consume (E0/E2 local)

No Design re-research. Sources: elevated `design-process` skill + checklist; Theme 5 accepted report.

- `FACT` [E0] `design-process` spine outputs relevant to planning: purpose / **constraints** / **success criteria**; **2–3 options + recommendation** (human decides); design presented **in sections** with per-section approval; optional design note `docs/design/YYYY-MM-DD-<topic>-design.md`; significant locks → ADR `docs/adr/NNNN-slug.md`; self-review (placeholders, contradictions, scope, ambiguity); **gate** — only after approval proceed to implement / **task planning**. [E0: path=`d:\Toolbelt\skills\design-process\SKILL.md`, `…/references/design-process-checklist.md` — observed 2026-07-29]
- `FACT` [E2] Theme 5 accepted: shared spine frame+constraints → criteria → alternatives → critique → **human decide** → record ADR/MADR → HITL gate before implementation; ADR house requires **Considered Options** (+ pros/cons) before Decision; draft/proposed ≠ accepted. [E2: `docs/research/reports/theme-5-design-pocket.md` §§3, 9 — accessed 2026-07-29]
- `FACT` [E0] Campaign brief: Design owns *what/why*; Plan owns *how to sequence checkable work*; reuse Theme 5 Design spine as **input**; do not re-litigate Design. [E0: `docs/research/notes/theme-6-plan/campaign-brief.md` — observed 2026-07-29]
- `FACT` [E2] Theme 5 / design-process (also in T6B): multi-subsystem asks → **sub-designs first**; scale short vs sectional design. [E2: Theme 5 report + design-process SKILL — accessed 2026-07-29]

#### 4.3.1 Consume-field candidates (INFERENCE — not locks)

| Design artifact field / atom | Plan should consume as… | Notes |
|------------------------------|-------------------------|-------|
| Approved **section IDs** / headings (sectional design) | WBS parent / epic / plan chapter anchors; `design_ref: path#section` | Map section → work package coverage (T6B INFERENCE) |
| Human **decision** (chat clear + ADR Decision) | Binding input — restate Decision text or cite path+§; **do not reopen options** | Theme 5 gate; Nygard ADR [E1 T6B] |
| **Considered Options** (ADR) | Link only (T2); do not re-run matrix in plan | Theme 5 ADR house |
| **Constraints** / NFRs / consequences | Always-inline (T0) or extract into Global Constraints | design-process clarify + ADR Consequences |
| **Success criteria** | Seed Done-when / acceptance / verify | design-process criteria step |
| **Interfaces** / deps / construction techniques (ADR triggers) | Inline contracts needed to code; path to ADR for rationale | Theme 5 ADR significance axes |
| Sub-design boundaries | Separate plan chapters or plans; integrate only at declared interfaces | design-process scope check |
| Self-review flags (TODO/ambiguity) | Must be cleared or become V1 NEEDS CLARIFICATION / HALT items | design-process checklist |
| Design note path | T1 locator + extract instruction for Interfaces/Decisions | `docs/design/…` convention |
| Unapproved / draft design | **Not** plan input for locking work — wait for gate | `draft-is-not-sot`; Theme 5 |

- `INFERENCE` [E4] Plans should **consume** sectional IDs, accepted Decision+constraints+interfaces+success criteria, and design/ADR **paths**; plans should **not consume** unresolved options matrices or draft Design as law. Premises: table above; campaign brief E0; Theme 5 E2.
- `GAP` No Toolbelt-accepted Plan template field schema that encodes the table (still candidate). Portable JSON schema GAP from W2 retained.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | W3 primary re-fetch will yield a numeric paste budget | **rejected** | §4.1.2 durable GAP |
| H2 | Progressive disclosure + self-contained specs suffice to propose E4 tiers | confirmed (as candidates only) | §4.1.3 |
| H3 | Validation atoms can be extracted without elevating validating-plans | confirmed | §4.2.6; refs still GAP |
| H4 | Design→plan consume fields closable from local E0/E2 without Design re-research | confirmed (candidate table) | §4.3 |
| H5 | New FACT yield vs W1/W2 is thin (diminishing returns) | confirmed | Method stop_reason |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Plan density vs validation | Spec Kit thin tasks + no full impl in quickstart [E1] | Superpowers code-in-plan + TDD steps [E1 W2] | Retain W2 CONFLICT / OPEN; validation atom V8 notes both arms |
| Skills 500-line sizing vs plan paste | Anthropic Skills ~500 lines [E1] | No plan budget E1 | Do **not** transfer 500-line rule to Plan paste; durable GAP |
| validating-plans pocket | Plan-adjacent QA (reality/drift) [E1 summary] | TDD/git/issue packaging [E3] | Transferable atoms only; no elevation; pocket home OPEN (W2) |

## 7. Gaps & OPEN

### Closed / hardened this pass (not SoT locks)

- Progressive disclosure + JIT identifiers **reconfirmed** E1 (Anthropic context engineering + Agent Skills).
- Claude self-contained + runnable-verify atoms **reconfirmed** E1.
- Spec Kit NEEDS CLARIFICATION / ERROR gates; BMAD HALT + ready-for-dev; OpenSpec open-question readiness — **reconfirmed** E1 for checklist atoms.
- Design→plan **consume-field candidate table** from local Design E0/E2 (new synthesis for integrator; not elevation).
- E4 paste/link **tier candidates** documented (T0–T3) with clear non-lock labeling.

### Durable GAPs (stop — do not keep searching)

- `GAP` **Numeric / mandatory paste budget** for plan↔ADR/design (lines/tokens/%) — durable after W1+W2+W3.
- `GAP` Portable agent task **JSON schema as SoT** (W2 retained).
- `GAP` validating-plans `references/*.md` unpublished; claimed upstream 404 (W2 retained).
- `GAP` Prescribed `[P]` plan token in vendor SoT (W2-EXEC retained; not re-attacked).
- `GAP` Cursor help/context page paste-policy wording (timeout this pass; prompting E1 only).

### OPEN (acceptance / trials — not more gatherers)

- `OPEN` Whether Toolbelt adopts T0–T3 tier language in a future plan template.
- `OPEN` Plan density arm (code-in-plan vs thin tasks vs intent-contract) — W2 conflict.
- `OPEN` E0 trials: hallucination rate paste-heavy vs link+binding-excerpt.
- `OPEN` Integrator merge into Theme 6 draft report.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Wave-3 +1 should **stop** here: residual yield is mostly corroboration + candidate tables; named numeric paste GAP is durable. Premises: H1 rejected; H5 confirmed; depth-modes diminishing-returns stop.
- `INFERENCE` [E4] A future proposed Plan checklist can merge: T0 always-inline fields + V1–V7 validation atoms + design consume table — still requiring human accept + `author-cursor-surfaces` before elevation. Premises: §§4.1–4.3; campaign brief non-goals; `draft-is-not-sot`.
- `INFERENCE` [E4] **Out of Plan elevation:** Superpowers git/TDD/PR law; validating-plans as a whole skill; Skills 500-line rule as paste budget. Premises: campaign brief; §4.1.2; §4.2.5.

## 9. Source list (deduped)

1. Anthropic — Effective context engineering for AI agents — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — accessed 2026-07-29 [E1]
2. Anthropic — Equipping agents for the real world with Agent Skills — https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills — accessed 2026-07-29 [E1]
3. Anthropic docs — Agent Skills best practices — https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/best-practices — accessed 2026-07-29 [E1]
4. Claude Code — Best practices — https://code.claude.com/docs/en/best-practices — accessed 2026-07-29 [E1]
5. Cursor — Prompting agents — https://cursor.com/docs/agent/prompting — accessed 2026-07-29 [E1]
6. github/spec-kit — `templates/plan-template.md`, `templates/commands/plan.md` — accessed 2026-07-29 [E1]
7. bmad-code-org/BMAD-METHOD — `…/bmad-build-auto/step-02-plan.md` — accessed 2026-07-29 [E1]
8. Fission-AI/OpenSpec — `schemas/spec-driven/schema.yaml` — accessed 2026-07-29 [E1]
9. majiayu000/claude-skill-registry — `skills/testing/validating-plans/SKILL.md` — accessed 2026-07-29 [E1]
10. Local — `skills/design-process/SKILL.md` + `references/design-process-checklist.md` — observed 2026-07-29 [E0]
11. Local — `docs/research/reports/theme-5-design-pocket.md` (accepted) — accessed 2026-07-29 [E2]
12. Local — Theme 6 W2 notes (skim) + `campaign-brief.md` — observed 2026-07-29 [E0]

---

## Return to parent

**Using `research-protocol`**; depth: **deep**; wave: **3**; slice: **T6-PLUS1-RESIDUAL**.

**stop_reason:** `low_return_plus_one`

### Durable GAPs
- Numeric paste-vs-link budget (W1→W3)
- Portable task JSON schema SoT (W2)
- validating-plans `references/*.md` unpublished (W2)
- Vendor `[P]` token (W2-EXEC)
- Cursor help/context fetch timeout (this pass)

### Closed / hardened (candidates only — not locks)
- E1 progressive disclosure / JIT / Skills L1–L3 reconfirmed
- E4 T0–T3 paste/link **tier candidates** (INFERENCE)
- Checkable validation atoms V1–V8 from Claude / Spec Kit / BMAD / OpenSpec / validating-plans SKILL.md summary
- Design→plan consume-field table from local Design E0/E2

### Out
- No Plan / validating-plans skill elevation
- No Superpowers git/TDD law
