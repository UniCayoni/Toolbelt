---
title: "Theme 8 — Verify gates normal scope (pass 3: GitHub + web inventory)"
status: draft
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: normal
aligned_with:
  - docs/research/notes/theme-8-verify/scope-normal-pass1.md
  - docs/research/notes/theme-8-verify/scope-normal-pass2-expand.md
  - docs/research/notes/theme-8-verify/campaign-brief.md
supersedes: null
---

# Theme 8 — Pass 3: online + GitHub verify/validate surfaces

**Using `research-protocol`**; depth: **normal** (discovery inventory for deep T8C — not deep fleets).

**Lean:** quality + readability; Toolbelt standalone (inspire/cut). Stars = E3 discovery.

## 1. Scope

- Question: What verification/validation **skills and surfaces** do other GitHub/web projects use for plans and implementations, and which insights should feed Theme 8 deep research?
- In: Plan-validate, execute-verify, converge/gap, code-review-as-gate, evidence-before-completion patterns.
- Out: Elevating Toolbelt skills; locking CLI frameworks as dependencies; Debug/PR pack design.

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | WebSearch; `gh api` / `gh search`; GitHub MCP search_code (empty results this pass); Read prior Theme 6/7 notes |
| Queries (exact) | Web: agent skills validating plans verification-before-completion; Spec Kit converge/analyze/checklist; OpenSpec verify; `site:github.com SKILL.md validating-plans OR review-plan OR validate-plan`. gh: obra/superpowers requesting-code-review; majiayu000 validating-plans; Fission-AI openspec-verify-change; github/spec-kit analyze.md + checklist.md; kdcokenny plan-review |
| What was *not* searched | Exhaustive fork tree of every Superpowers clone; Discord heat metrics; live E0 Toolbelt trials |
| Depth | normal |
| stop_reason | High-signal cluster inventoried; further repos mostly forks/mirrors — diminishing returns for **normal** discovery; deepen in T8C deep wave |

## 3. Inventory (ranked by Toolbelt relevance)

### Tier A — Highest relevance to Plan/Execute gates

| Surface | Repo / path | What it does | Transferable atoms | Park |
|---------|-------------|--------------|-------------------|------|
| **verification-before-completion** | obra/superpowers (+ many mirrors) | Iron law: no completion claim without IDENTIFY→RUN→READ→VERIFY; rejects “should/looks” | Evidence gate; red-flag wording; requirements checklist ≠ tests-only | TDD red-green ceremony; commit/PR mandatories |
| **validating-plans** | majiayu000/claude-skill-registry `skills/testing/validating-plans` | Between write-plan and execute: **3 parallel agents** — TDD auditor, **Reality Check**, **Drift**; severity BLOCKER/CRITICAL/WARNING/NIT; verdicts PASS / PASS WITH NOTES / NEEDS REVISION; todos fix **the plan** not code | Parallel plan QA; reality-check; drift; severity+verdict; fix-plan-not-code | TDD auditor as law; gh issue packaging; Superpowers path coupling; refs/*.md often 404 |
| **review-plan** (council) | rube-de/cc-skills `plugins/council/skills/review-plan` | Codebase verification table (paths, APIs, imports, duplicates) **then** external consultant subagents | Codebase verify table before consultants; CRITICAL fail-fast | Multi-consultant ceremony may be heavy |
| **plan-review** | kdcokenny/opencode-workspace | Rubric: Citation quality, Completeness, **Actionability** (no vague tasks; clear deps) | Actionability / anti-ambiguity rubric for plans | Citation-specific house rules |
| **review-plan** (trello-mcp) | mab-go/trello-mcp | Task item review: incomplete/composite/ambiguous/trivial/misordered/**coverage gap**; don’t edit until approve | Task quality taxonomy; coverage gap | Product-specific follow-ons |
| **validate-plan** (kanbanzai) | sambeau/kanbanzai | Structural D-checks: sections, traceability matrix, acyclic deps, actionable tasks; pass/fail + report | Traceability / acyclic deps / structural completeness | Heavy D1–D13 rubric; product-specific |
| **openspec-verify-change** | Fission-AI/OpenSpec | Post-implement verify vs change artifacts: **Completeness / Correctness / Coherence** dimensions; CRITICAL/WARNING/SUGGESTION | Three-dimension report; coherence/design adherence | OpenSpec CLI dependency |
| **speckit.converge** | github/spec-kit | Code vs spec/plan/tasks; gap types missing/partial/contradicts/**unrequested**; append-only tasks; no code edit | Gap taxonomy; unrequested=scope creep; append remediation | Spec Kit paths/CLI |
| **speckit.analyze** | github/spec-kit | Cross-artifact consistency **before** implement (read-only report) | Pre-exec artifact consistency analysis | Spec Kit packaging |
| **speckit.checklist** | github/spec-kit | “Unit tests for English” — requirements completeness/clarity checklists | Requirements-quality checklists as validate layer | Spec Kit packaging |
| **requesting-code-review** | obra/superpowers | Fresh reviewer subagent with plan/requirements + SHAs; Critical/Important/Minor; fix before proceed | Fresh-context review; severity triage; don’t self-review in coordinator context | Git SHA ceremony as SoT |

### Tier B — Adjacent / packaging-heavy

| Surface | Insight | Toolbelt stance |
|---------|---------|-----------------|
| rune-kit `converge` | Same gap types; “verification asks does it build; converge asks is everything promised in the code?” | Atom: split **signal verify** vs **intent coverage** |
| Copilot code review + skills GA (2026-07-29) | Skills inject standards into **PR review** | Later Debug/PR pack — not Theme 8 spine |
| faulkdev Copilot Completion Checklist | Requirements/Correctness/Quality/Verification buckets | Aligns with OpenSpec three dimensions + quality lean |

### Tier C — False friends / low priority

| Surface | Why low for Theme 8 |
|---------|---------------------|
| Pure Superpowers forks of verification-before-completion | No new method |
| Issue/kanban product validators without agent plan grammar | Domain packaging |

## 4. Cross-cutting insights (for deep)

1. **Two verify problems, not one**  
   - **Plan validate** (pre-exec): reality, drift, coverage, actionability, ambiguity  
   - **Implementation verify** (post-task / post-plan): evidence-before-claim **and** intent coverage (converge) **and** quality/coherence review  

2. **Severity + verdict language is common**  
   BLOCKER/CRITICAL/WARNING + PASS / PASS WITH NOTES / NEEDS REVISION — useful for Toolbelt plan-validate without importing TDD auditor.

3. **Fix the artifact you audited**  
   validating-plans: todos fix the **plan**; converge: append **tasks**, don’t rewrite spec silently — matches Toolbelt do-not-invent.

4. **Parallel specialist validators**  
   Reality vs drift vs (parked) TDD — Toolbelt can parallelize Reality+Drift+Actionability/Coverage without TDD law.

5. **Fresh reviewer ≠ evidence gate**  
   verification-before-completion = run commands; requesting-code-review / Claude adversarial = quality+faithfulness in clean context. Theme 8 needs **both** for quality lean.

6. **Pre-implement analyze vs post-implement converge**  
   Spec Kit analyze (artifacts) vs converge (code vs intent) — Plan pocket + Execute pocket both get gates.

7. **Actionability / coverage-gap taxonomies**  
   Strong fit for strengthening Plan beyond V1–V8 (pass-2 foreshadowed).

8. **CLI-heavy verify** (OpenSpec verify-change)  
   Method atoms yes; dependency no.

## 5. Updates to surface-shape lean (pass 2→3)

- `INFERENCE` [E4] Community strongly supports a **distinct plan-validate phase** between write-plan and execute (validating-plans, review-plan, validate-plan, speckit.analyze/checklist) — strengthens option **B or C** over pure A. Premises: Tier A inventory.
- `INFERENCE` [E4] Execute side needs **evidence gate + optional/required fresh review + optional converge-style intent check** — not evidence alone. Premises: verification-before-completion + requesting-code-review + converge/openspec-verify.
- `INFERENCE` [E4] Entering deep lean still: thin shared companion **or** plan-validate companion + execute-verify fold; **not** fat Quality pack. Premises: Toolbelt spirit; pass-2 options.
- `FACT` [E0] **Human lock 2026-07-30:** **C** with `implementation-plan-verify` + `implementation-execute-verify`; D2–D30 leans in [`campaign-brief.md`](./campaign-brief.md) §0. Supersedes B-lean for campaign constraints.

## 6. Gaps for deep T8C (named)

- Deep-read rube-de review-plan verification table + consultant prompts  
- OpenSpec verify-change full Completeness/Correctness/Coherence rubrics  
- Spec Kit analyze.md + checklist.md full grammar  
- kanbanzai D-check subset worth Toolbelt (traceability/acyclic) vs overfit  
- Confirm validating-plans `references/*.md` still 404 (Theme 6) — use SKILL.md summaries only  

## 7. Implications

- `INFERENCE` [E4] Pass 3 **sufficient** to enrich campaign brief T8C + T8A/T8B atom lists; no pass 4 normal required. Premises: diminishing returns on forks; deep will deep-read Tier A.
- `INFERENCE` [E4] Do not elevate from this draft. Premises: `draft-is-not-sot`.

## 8. Source list (deduped)

1. obra/superpowers `verification-before-completion`, `requesting-code-review` [E1]  
2. majiayu000/claude-skill-registry `validating-plans/SKILL.md` [E1]  
3. Fission-AI/OpenSpec `openspec-verify-change/SKILL.md` [E1]  
4. github/spec-kit `converge.md`, `analyze.md`, `checklist.md` (+ docs agentic-sdd) [E1]  
5. rube-de/cc-skills `review-plan` [E1 via WebSearch/snippet]  
6. kdcokenny/opencode-workspace `plan-review` [E1 via WebSearch]  
7. mab-go/trello-mcp `review-plan` [E1 via WebSearch]  
8. sambeau/kanbanzai `validate-plan` [E1 via WebSearch]  
9. rune-kit/rune `converge` [E3/E1 snippet]  
10. GitHub Changelog Copilot skills in code review 2026-07-29 [E1 product]  
11. Pass 1–2 Theme 8 notes [E0]
