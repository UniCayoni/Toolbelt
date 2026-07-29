---
title: "Recon: {repo or workspace}"
status: draft
created: YYYY-MM-DD
workspace_roots: []
project_id: null
aligned_with: docs/research/reports/theme-1-codebase-research-for-agents.md
protocol_steps: S0-S18
---

# Codebase / workspace reconnaissance

Use **before** documenting architecture or implementing changes.  
Authority: `docs/research/PROTOCOL.md` + Theme 1 integrated report (S0–S18).  
Full evidence table: `docs/research/reports/theme-1-codebase-research-for-agents.md` §2.

Checklist maps 1:1 to report steps. Mark unmet items `GAP` rather than inventing.

## S0 — Seed task context

- [ ] README / CONTRIBUTING
- [ ] Nearest `AGENTS.md` (and `CLAUDE.md` / `.cursor/rules` if present)
- [ ] Exact build/test/lint commands recorded with path citations (`FACT` [E0])

## S1 — Declare comprehension goal

| Field | Value |
|-------|-------|
| Goal / task type |  # corrective \| perfective \| adaptive \| reuse \| understand-for-X |
| Why this goal |  |

## S2 — Choose strategy mode

| Field | Value |
|-------|-------|
| Mode | systematic \| as-needed \| hybrid |
| Scope boundary |  # prefer scoped systematic on large repos |
| Missed-interaction risk noted? | yes/no (required if as-needed) |

## S3 — Memory / prior-knowledge check

- [ ] Prior accepted research notes / memory artifacts checked
- Findings:

## S4 — Plan exploration agenda

1. 
2. 
3. 

Warn: no unbounded exploration without scope.

## S5 — Instruction / ignore surface

- [ ] Root (+ nested) agent instructions read
- [ ] Ignore/deny noise configured or noted (secrets, vendor, generated)

## S6 — Structure discovery

- [ ] Top-level layout / tree / repo-map
- Entry points / packages:

## S7 — Top-down hypotheses

| ID | Expected module/layer / beacon | Status |
|----|--------------------------------|--------|
| H1 |  | open \| confirmed \| rejected \| revised |

## S8 — Locate before edit

- [ ] Grep / Instant Grep / NL / index / LSP searches run
- Hit list (path + why):

**Do not edit yet.**  
ACI lens (Yang et al. SWE-agent, arXiv:2405.15793): prefer simple locate/view actions with concise feedback before edit; avoid raw unbounded shell sprawl for core recon. [E1 secondary]

## S9 — Isolate recon context

- [ ] Broad search delegated to Explore / investigation subagent (if available) — **recommended** for large/unfamiliar repos; optional for tiny single-file as-needed work
- Summaries returned (not raw dumps):

## S10 — Selective read (bottom-up)

| Path | Why | Program-model notes (control) | Situation-model notes (data/fn) | Open Q |
|------|-----|-------------------------------|----------------------------------|--------|
|  |  |  |  |  |

Summarize large files; no whole-tree dumps.

## S11 — Inquiry episodes (delocalized plans)

| Question | Conjecture | Search | Result |
|----------|------------|--------|--------|
|  |  |  |  |

## S12 — Architecture / dependency (conditional)

Only if goal warrants:

- [ ] Dep extract → abstract modules → view
- [ ] Expected vs observed
- [ ] Cycles flagged
- If skipped: reason =

## S13 — Synthesize cited notes

Durable findings — **either is OK**:

- [ ] **Short/smoke:** graded findings section in this checklist (FACT/CLAIM/INFERENCE/GAP + citations), **or**
- [ ] **Full:** separate note via `templates/research-note.md` / skill `research-protocol` with Method block

- Parallel models: domain / program / situation updated
- Hypotheses updated

## S14 — Persist findings

- [ ] Memory/todos/file maps updated
- [ ] Instruction-file updates queued if repeated mistakes found

## S15 — Reflect / re-plan

- [ ] Evidence sufficient? if no → re-plan (return to S4)
- Tool-use calibration notes:

## S16 — Completion gate (before implementation write tools)

Exploration complete only if:

- [ ] Done-when / thoroughness criteria met **or** unmet items listed as `GAP`
- [ ] No factual claims without citations
- [ ] Verification commands from instructions identified

**STOP.** Do not **implement product/code** until gate passes or human waives in writing.  
Research notes under `docs/research/` during recon are allowed (not an S16 violation).

**Enforcement (elevation):** Soft default via skill/rule. Optional hard deny of code write tools via Cursor hooks only if soft guidance fails in practice — vendors do not mandate explore-before-edit.

**E0 tip (Windows):** Prefer path-exists / small Python checks over brittle PowerShell one-liners when listing trees.

## S17 — Then implement (out of recon completion)

Incremental edit → run verify/test from instruction file → treat AI summaries as conjectures.

## S18 — Reproducible investigation artifacts

- [ ] Notes version-controlled
- [ ] Env / steps recorded if analysis produced
- [ ] Raw vs derived separated if data involved
