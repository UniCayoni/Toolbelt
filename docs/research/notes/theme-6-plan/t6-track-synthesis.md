---
title: "T6-SYNTH — Theme 6 Plan pocket track synthesis (integrate-prep)"
status: draft
theme: theme-6-plan
created: 2026-07-29
updated: 2026-07-29
authors: [t6-synth-integrator-grok]
supersedes: null
aligned_with:
  - docs/research/notes/theme-6-plan/campaign-brief.md
  - docs/research/notes/theme-6-plan/t6-coordinator-pin.md
  - docs/PROTOCOL.md
inputs:
  - docs/research/notes/theme-6-plan/t6a-w1-plan-for-fresh-agents.md
  - docs/research/notes/theme-6-plan/t6b-w1-design-to-plan-decompose.md
  - docs/research/notes/theme-6-plan/t6c-w1-multiagent-plan-execution.md
  - docs/research/notes/theme-6-plan/t6d-w1-github-plan-skills-inventory.md
  - docs/research/notes/theme-6-plan/t6-w2-exec-shape-serial-parallel.md
  - docs/research/notes/theme-6-plan/t6-w2-rag-schema-paste-link.md
  - docs/research/notes/theme-6-plan/t6-w2-gap-community-templates.md
  - docs/research/notes/theme-6-plan/t6-w3-plus1-residual.md
residual_note: merged_post_pass  # residual landed after first synth pass; §4.8 coordinator addendum
updated: 2026-07-29
---

# T6-SYNTH — Theme 6 Plan pocket track synthesis

**Using `research-protocol`**; depth: **deep**; wave: **integrate-prep**; slice: **T6-SYNTH**.

**Status:** `draft`. Not Plan SoT. No skill/rule/template elevation. Integrated report file is **coordinator-owned** (`docs/research/reports/theme-6-plan-pocket.md`) — not written here.

## 1. Scope

- Question / goal: Merge W1 (T6A–D) + W2 (exec-shape, RAG schema, community grammar) into a single integrate-prep synthesis: multi-source FACT cluster, conflict table, candidate method spine, elevation candidates, P0 OPENs for human, E1 source shortlist.
- In scope: Cross-track merge of existing gatherer notes only; label + grade discipline; residual-status callout.
- Out of scope: Writing the campaign integrated report; elevating Plan surfaces; inventing Cursor Task API; importing Superpowers git/TDD/PR as Toolbelt law; UX planning (T5C); new web/RAG gather.
- Comprehension / research goal type: other (integrator merge)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Read (research-protocol, research-note template, campaign brief, coordinator pin, all Theme 6 notes listed in frontmatter `inputs`) |
| Corpora / URLs searched | None new — integrator merge of local notes only |
| Queries (exact) | N/A (no new gather) |
| What was *not* searched | Fresh web/RAG; W3/+1 residual note (file absent); live E0 Toolbelt plan trials |
| Depth | deep |
| Waves / stop_reason | wave: **integrate-prep**; slice: **T6-SYNTH**. First pass: W1+W2 merge. Addendum §4.8: residual `low_return_plus_one` merged. Campaign stop: **low_return_plus_one**. |
| Provenance (optional PROV) | Entity←W1 T6A–D + W2 EXEC/RAG/GAP notes; Activity=T6-SYNTH integrate-prep; Agent=cursor-grok integrator |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Serial integrator merge of named note paths; no codebase recon |
| Scope boundary | `docs/research/notes/theme-6-plan/` gatherer outputs only; report file excluded |

## 4. Findings

### 4.1 Input inventory

| Wave | Note | Present |
|------|------|---------|
| Pin/brief | `campaign-brief.md`, `t6-coordinator-pin.md` | yes (framing only) |
| W1 | `t6a-w1-…`, `t6b-w1-…`, `t6c-w1-…`, `t6d-w1-…` | yes |
| W2 | `t6-w2-exec-shape-…`, `t6-w2-rag-schema-…`, `t6-w2-gap-community-…` | yes |
| W3 / +1 residual | `t6-w3-plus1-residual.md` | **yes** (landed after first synth pass; see §4.8) |

- `FACT` [E0] Residual closer note now present; first synth pass ran before it landed — §4.8 addendum merges residual without rewriting §§4.2–4.7. [E0: note root 2026-07-29]

### 4.2 Cross-track FACT cluster (multi-source only)

Claims below appear in **≥2 tracks** with independent citations (not single-note invent). Grades reflect the strongest supporting grade across tracks; citations point at gatherer notes that hold the primary locators.

1. `FACT` [E1] Fresh coding subagents start with **clean / isolated context**; the parent (or plan/handoff packet) must supply needed facts — they do not inherit prior chat. Multi-source: T6A (Cursor Subagents + Claude Code sub-agents); T6C (Anthropic fresh subagents / selective context); W2-RAG corroborates Isolate/selective packets [E2]. [E1 via T6A/T6C notes; E2 via `t6-w2-rag-schema-paste-link.md` §4.2]

2. `FACT` [E1] Agent-usable task prompts/plans converge on **Goal + Context/files + Constraints + Done-when / verify**. Multi-source: T6A (Codex best practices; Claude self-contained specs); W2-RAG (Osmani/Broda/Dibia/Dooley corroboration [E2]); T6D/W2-GAP community templates require paths + verify/AC. [E1 via T6A; E2 via W2-RAG; E1 community via T6D/W2-GAP]

3. `FACT` [E1] Self-contained specs name **files/interfaces**, state **out-of-scope**, and end with **checkable verification** (tests/commands/e2e). Multi-source: T6A Claude best practices; T6C Anthropic delegation fields (objective, output format, boundaries); T6D Spec Kit / BMAD / Superpowers structure. [E1 via T6A/T6C/T6D]

4. `FACT` [E1] Design/ADR owns **what/why / decisions**; implementation plans sequence **checkable work** without reopening the options matrix. Multi-source: T6B (Nygard ADR [E1] + Theme 5 pocket [E2 path]); campaign brief Design vs Plan [E0]; T6D OpenSpec specs≠implementation detail / Spec Kit plan↔tasks split. [E1/E2 via T6B; E1 via T6D]

5. `FACT` [E1] Decomposition stack for agent plans: deliverable coverage → vertical increments → further splits when oversized/unknown → SMART/checkable tasks with acceptance. Multi-source: T6B (Wake INVEST/SMART [E1], Cohn SPIDR [E1], WBS 100%/sequencing [E2]); W2-RAG re-corroborates AC↔done [E2]. [E1/E2 via T6B + W2-RAG]

6. `FACT` [E1] Multi-agent **research / independent** fan-out benefits from parallel workers; **most coding with shared context / many deps** is a weaker fit for unconstrained parallel implementers. Multi-source: T6C Anthropic multi-agent research caveat; W2-EXEC Claude agent-teams same-file/deps guidance + Cursor independent-vs-dependent plan steps. [E1 via T6C + `t6-w2-exec-shape-serial-parallel.md`]

7. `FACT` [E1] Parallel **writers** need **non-overlapping file ownership** and/or **worktree/branch isolation**; context isolation alone ≠ file isolation. Multi-source: W2-EXEC (Claude agent teams + Claude/Cursor worktrees); T6C Superpowers red-flag inventory [E0] aligns on conflict risk. [E1 via W2-EXEC; E0 via T6C]

8. `FACT` [E1] Review / verify gates (fresh-context reviewer, evaluator-optimizer, Planner→Implementer→Verifier) are first-class patterns before treating work done. Multi-source: T6A/T6C Claude adversarial review; W2-EXEC Cursor Verifier pattern + Anthropic gates; T6D/W2-GAP Independent Test / Verification sections. [E1 via T6A/T6C/W2-EXEC/T6D]

9. `FACT` [E1] Community plan-writing cluster (structure inventory, stars=E3): Superpowers `writing-plans`, Spec Kit plan+tasks, OpenSpec tasks, BMAD epics/stories + build-auto intent-contract — shared atoms: self-contained constraints, file/code map, ordered checkable units, verify/AC, anti-placeholder / clarify-or-halt. Multi-source: T6D W1 + W2-GAP primary fetches. [E1 content via T6D/W2-GAP; E3 stars]

10. `FACT` [E0/E2] W2 RAG **did not** close paste-vs-link numeric budget or a portable JSON task schema SoT; principles (inline binding decisions + path/JIT for bulky rationale) remain. Multi-source: T6A GAP + W2-RAG GAP attack. [E0/E2 via T6A + `t6-w2-rag-schema-paste-link.md`]

### 4.3 CONFLICT table (named axes)

| Topic | Source A | Source B | Source C (if any) | Resolution (integrator) |
|-------|----------|----------|-------------------|-------------------------|
| **Code-in-plan density** | Superpowers: embed **full code snippets** in plan steps [E1 T6D/W2-GAP] | Spec Kit / OpenSpec: **thin** checkbox tasks (paths/actions; Spec Kit quickstart forbids full impl code) [E1 W2-GAP] | BMAD build-auto: **compact intent-contract** (~900–1600 tokens) + Code Map + `file -- action -- rationale` (boundaries, not how) [E1 W2-GAP] | **OPEN** for Toolbelt. No lock. Candidate middle path (INFERENCE only): binding interfaces + verify signals in-plan; no mandatory full-code dumps (§4.4). |
| **Serial vs parallel implementers** | Anthropic: most coding weaker multi-agent fit [E1 T6C/W2-EXEC]; Superpowers SDD: never parallel implementation subagents [E0/E3] | Cursor: Build in Parallel for **independent** steps [E1 W2-EXEC]; Claude: parallel OK when independent / non-overlapping files [E1 W2-EXEC] | — | **Compatible if scoped:** default coding on shared checkout → serial implementer + review; parallel only when independence + exclusive writes **or** worktree isolation. Token `[P]` name remains GAP (Spec Kit uses `[P]` [E1]; vendor SoT does not mandate Toolbelt token). **No absolute Superpowers ban as Toolbelt law.** |
| **TDD-in-plan** | Superpowers: TDD 5-step (incl. commit) in every task [E1]; validating-plans TDD Compliance Auditor [E1 W2-GAP] | Spec Kit: tests **optional** unless requested [E1 W2-GAP]; OpenSpec “verifiable” without mandating test tasks; BMAD Verification optional | — | **OPEN**. Campaign non-goal: do not import mandatory TDD/git as Plan law. Verify-with-expected-signal is multi-source FACT; *TDD ceremony as Plan grammar* is not. |
| **validating-plans home** | Workflow sits between write-plan and execute-plan (Plan-adjacent QA) [E1 W2-GAP] | Registry category `testing`; TDD auditor + commit/issue packaging lean Verify/execution [E1/E3 W2-GAP] | — | **OPEN** Plan vs Quality/Verify pocket. Transferable atoms: reality-check (files/APIs exist), severity gates. Exclude TDD-compliance + gh-issue packaging from Plan elevation candidates until human decides pocket. |

Additional logged conflicts (lower P0 for elevation; retain for report):

| Topic | Brief | Resolution |
|-------|-------|------------|
| Handoff history semantics | OpenAI handoffs may pass filterable history [E1 T6A] vs Cursor/Claude clean brief [E1] | Product-specific; Toolbelt plan docs prefer clean-brief model |
| Story “must deliver end-user value” | Wake Valuable [E1 T6B] vs Thoughtworks staged sophistication [E2 T6B] | Prefer vertical slices; allow thin transversal when integration-heavy |
| Plan durability in git | E3 “plans ephemeral” vs campaign candidate plan templates [E0] | **OPEN** meta-decision |

### 4.4 Candidate Plan pocket method spine (INFERENCE — not elevated)

`INFERENCE` [E4] A future `write-plan` / `implementation-plan` skill **might** teach the following section spine. **Not elevated.** Premises: §§4.2–4.3 multi-source FACTs + T6B/T6C/T6D/W2 implications.

| # | Candidate section | Intent (agent-readable) | Primary premises |
|---|-------------------|-------------------------|------------------|
| 0 | **Preconditions** | Approved design/ADR (or short accepted decision) linked; Plan does not reopen options | T6B Design gate; campaign brief |
| 1 | **Plan header** | Goal; Architecture/stack *as already decided*; Global Constraints / Always–Block If–Never; Out-of-scope / do-not | T6A Codex; BMAD intent-contract; Superpowers header inventory |
| 2 | **Coverage map** | FR/design-section → work packages/stories/tasks (100% of approved scope) | T6B WBS 100%; BMAD FR Coverage Map |
| 3 | **File / Code Map** | Annotated create/modify paths before tasks; exclusive-write ownership for any parallel tranche | T6A/T6D; W2-EXEC ownership |
| 4 | **Scaling shape** | Simple → flat SMART list; medium → WBS→vertical slices→tasks; complex → one plan chapter per sub-design | T6B scaling ladder |
| 5 | **Task units** | Ordered checkable units: Files; Interfaces Consumes/Produces (or binding contracts); deps; acceptance/verify (command + expected signal **or** GWT AC); no TBD placeholders | T6A/T6B/T6D; W2 candidate schema bag |
| 6 | **Execution spine** | `exec_default` (candidate: serial_implement_review for shared checkout); optional `[P]` / parallel-safe with independence + ownership/worktree + merge gate; review gates; escalate-to-human exits | T6C + W2-EXEC |
| 7 | **Handoff packets** | Controller-readable spine + per-task packet (objective, I/O, boundaries, path refs) for fresh contexts — not chat dump | T6A/T6C |
| 8 | **Paste-vs-link rule (guidance)** | Inline binding decisions/constraints/interfaces/verify; link design/ADR/research with extract instruction — **no numeric budget** until human convention / E0 trials | T6A + W2-RAG GAP |
| 9 | **Self-review / optional validate** | Spec coverage, placeholder scan, reality-check (paths/APIs exist); optional companion QA — pocket home OPEN | T6A Superpowers self-review; W2-GAP validating-plans |
| 10 | **Explicit non-imports** | No mandatory TDD/git/worktree/PR packaging as Plan grammar; no Design skill elevation from this pocket | campaign brief; T6D §4.2 |

### 4.5 Elevation candidates (post-accept only)

| Candidate | Type | Depends on human accept | Notes / blockers |
|-----------|------|-------------------------|------------------|
| `implementation-plan` / `write-plan` skill | skill | Theme 6 report accept + `author-cursor-surfaces` | Core pocket; teach spine §4.4 without Superpowers git/TDD law |
| Plan checklist / task template in `references/` | template | Same | Checkbox + ID; files; constraints; verify; optional `[P]`; design_ref; coverage map |
| Intent-contract atoms (Always / Block If / Never + HALT-on-gap) | template fragment | Density decision (compact vs thin vs code-in-plan) | From BMAD [E1 inventory]; not SoT until accept |
| Thin rule: no implement without plan when non-trivial | rule | Explicit human yes; intelligent exceptions (one-sentence diffs — Claude E1) | Optional; campaign brief already lists |
| Compose / entry-flow skill | skill | After pieces proven | Later; not W1/W2 elevation |
| `validating-plans`-style companion | skill | **Pocket home** decision (Plan vs Verify) | Reality-check atoms transferable; TDD auditor + issue packaging deferred |
| Spec Kit–style `[P]` / story labels | template markers | Serial/parallel + nesting decisions | Token name OPEN vs vendor SoT |

**Do not elevate from this draft** (`draft-is-not-sot`).

### 4.6 P0 OPEN questions for human (after report)

1. **Plan body density:** code-in-plan vs thin checkbox tasks vs compact intent-contract (or hybrid)?
2. **Default execution shape:** lock `serial_implement_review` for shared-checkout coding plans, with explicit parallel-safe criteria — yes/no?
3. **Verify grammar in Plan:** Done-when + command/Expected only, optional Gherkin GWT, or Independent Test per story — which default?
4. **TDD-in-plan:** never / optional when requested / required — given campaign non-goal for Superpowers TDD import?
5. **`validating-plans` pocket home:** Plan-adjacent QA vs Quality/Verify?
6. **Paste-vs-link:** accept principle-only hybrid guidance now, or require E0 trials before any convention?
7. **Plan artifact retention:** durable in-repo plans vs ephemeral agent context?
8. **Nesting levels:** how do Spec Kit story phases / BMAD session stories / Superpowers 2–5 min steps nest in Toolbelt?
9. **Status vocabulary:** adopt Superpowers-like `DONE`/`BLOCKED`/… or Toolbelt-native escalate exits?
10. **Residual W3/+1:** authorize residual closer note now (named GAPs: paste budget trials, schema field freeze, validating-plans refs, live BMAD epics example)?

### 4.7 Source shortlist (highest-value E1)

| # | Source | Why high value |
|---|--------|----------------|
| 1 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | No false shared context; JIT identifiers; lead/subagent pattern |
| 2 | https://www.anthropic.com/engineering/building-effective-agents | Workflows vs agents; parallelization; evaluator-optimizer; coding-agent review |
| 3 | https://www.anthropic.com/engineering/multi-agent-research-system | Orchestrator-workers; coding multi-agent caveat; artifact refs; fresh contexts |
| 4 | https://code.claude.com/docs/en/best-practices | Self-contained specs; verify + evidence; adversarial fresh review |
| 5 | https://code.claude.com/docs/en/sub-agents | Fresh isolated context; parallel research when independent |
| 6 | https://code.claude.com/docs/en/agent-teams | Same-file/deps → serial; file ownership for parallel writers |
| 7 | https://cursor.com/docs/subagents | Clean context; Planner→Implementer→Verifier; parallel Task calls |
| 8 | https://cursor.com/docs/agent/plan-mode | Implementation plan before Build; precise plans for multi-file |
| 9 | https://cursor.com/help/ai-features/multi-agent | Independent vs dependent plan steps (Build in Parallel) |
| 10 | https://developers.openai.com/codex/learn/best-practices | Goal / Context / Constraints / Done-when |
| 11 | https://xp123.com/invest-in-good-stories-and-smart-tasks/ | INVEST + SMART (T6B method core) |
| 12 | https://www.mountaingoatsoftware.com/blog/five-simple-but-powerful-ways-to-split-user-stories | SPIDR (incl. Spike) |
| 13 | https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions | ADR vs plan boundary |
| 14 | https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md | Richest plan-structure inventory (E3 process couplings excluded) |
| 15 | https://github.com/github/spec-kit/blob/main/templates/tasks-template.md (+ `plan-template.md`, `commands/tasks.md`) | Thin tasks; `[P]`/`[USn]`; tests optional |
| 16 | https://github.com/bmad-code-org/BMAD-METHOD `…/bmad-build-auto/spec-template.md` (+ epics/stories steps) | Intent-contract + Code Map + HALT-on-gap |
| 17 | https://github.com/Fission-AI/OpenSpec/blob/main/schemas/spec-driven/schema.yaml | proposal→specs→design→tasks DAG |
| 18 | Local E0: Superpowers `subagent-driven-development/SKILL.md` (cache) | Controller + task brief + review gates inventory |
| 19 | Accepted Design input: `docs/research/reports/theme-5-design-pocket.md` | Design→plan gate / sectional design [E2 path] |

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Fresh-context + Goal/Constraints/Verify is the stable Plan core across tracks | confirmed (W1+W2) | §4.2 cluster #1–3, #8 |
| H2 | WBS→vertical→SMART is sufficient design→plan method candidate | confirmed as candidate | T6B; W2-RAG not weakened |
| H3 | Coding plans should default to parallel implementers | rejected as default | T6C H3 + W2-EXEC H3 |
| H4 | Community converges on one plan density | rejected | W2-GAP H5 / §4.3 |
| H5 | RAG closes paste budget + portable schema | rejected | W2-RAG H3/H4 |
| H6 | Residual W3 note already closed campaign stop rule | **confirmed** (addendum) | §4.8; residual `stop_reason: low_return_plus_one` |

### 4.8 Residual addendum (`t6-w3-plus1-residual.md`)

Coordinator merge after residual landed (first synth pass was W1+W2 only).

| Residual deliverable | Status for report |
|----------------------|-------------------|
| Numeric paste budget | Still **GAP** (durable) |
| E4 paste/link tiers **T0–T3** | Candidate guidance only — fold into spine §4.4 #8 |
| Validation atoms **V1–V8** | Candidate pre-exec checklist — fold into spine §4.4 #9 |
| Design→plan **consume-field table** | Candidate — supports Preconditions + Coverage map |
| validating-plans refs | Still **GAP** (404) |
| Campaign stop | **`low_return_plus_one`** |

P0 #10 in §4.6 (“authorize residual”) is **closed** — residual ran.

## 6. Conflicts

See **§4.3 CONFLICT table** (primary axes for human). Residual adds V8 thin-vs-code density note (same OPEN).

## 7. Gaps & OPEN

### Stable after W1–W3 (do not re-gather same questions)

- Goal + Constraints + Done-when/verify cluster
- Fresh / selective task packets
- Design/ADR vs Plan boundary + consume-field candidates
- Serial default for dependent coding writers; parallel for independent research/review
- Community grammar atoms + V1–V8 validation candidates
- Progressive disclosure / JIT principles (no numeric budget)

### Remaining GAPs (accept / E0 trials — not more gatherers)

- `GAP` Paste-vs-link **numeric** budget — durable after W3.
- `GAP` Portable task **schema as SoT** — candidate field bag only.
- `GAP` Prescribed Toolbelt `[P]` token in vendor SoT.
- `GAP` validating-plans `references/*.md` unpublished (404).
- `OPEN` P0 questions §4.6 #1–9 (density, serial default, verify grammar, TDD, validating-plans home, paste tiers, retention, nesting, status vocab).
- `OPEN` Coordinator writes `docs/research/reports/theme-6-plan-pocket.md`.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Campaign ready for **draft integrated report** with FACT cluster, conflicts, spine (incl. T0–T3 + V1–V8 candidates), elevation table, P0 OPENs — still `draft` until human accept. Premises: W1–W3; `stop_reason: low_return_plus_one`.
- `INFERENCE` [E4] **Top transferable method atoms** (structure only): (1) self-contained handoff header; (2) file/code map + interfaces; (3) ordered checkable tasks with verify signals; (4) design→WBS→vertical→SMART without reopening ADR; (5) controller spine + per-task packets with serial-default / explicit parallel-safe. Premises: §4.2 #1–9; §4.4; §4.8.
- `INFERENCE` [E4] Do **not** elevate Plan skills, lock density/TDD/parallel policy, or treat community templates as SoT from this note. Premises: `draft-is-not-sot`; campaign brief; §4.3 OPENs.

## 9. Source list (deduped)

### Gatherer notes (this merge)

1. `docs/research/notes/theme-6-plan/t6a-w1-plan-for-fresh-agents.md`
2. `docs/research/notes/theme-6-plan/t6b-w1-design-to-plan-decompose.md`
3. `docs/research/notes/theme-6-plan/t6c-w1-multiagent-plan-execution.md`
4. `docs/research/notes/theme-6-plan/t6d-w1-github-plan-skills-inventory.md`
5. `docs/research/notes/theme-6-plan/t6-w2-exec-shape-serial-parallel.md`
6. `docs/research/notes/theme-6-plan/t6-w2-rag-schema-paste-link.md`
7. `docs/research/notes/theme-6-plan/t6-w2-gap-community-templates.md`
8. `docs/research/notes/theme-6-plan/t6-w3-plus1-residual.md`
9. `docs/research/notes/theme-6-plan/campaign-brief.md` (framing)
10. `docs/research/notes/theme-6-plan/t6-coordinator-pin.md` (framing)

### Highest-value E1 (see §4.7)

11–29. Listed in §4.7 shortlist (+ Anthropic Agent Skills progressive disclosure from residual).
