---
title: "Recon: obra/superpowers (smoke v2 — patched harness)"
status: draft
created: 2026-07-28
updated: 2026-07-28
workspace_roots:
  - "C:\\Users\\Jonyc\\.cursor\\plugins\\cache\\cursor-public\\superpowers\\d884ae04edebef577e82ff7c4e143debd0bbec99"
project_id: null
aligned_with: docs/research/reports/theme-1-codebase-research-for-agents.md
protocol_steps: S0-S18
skill: codebase-recon
smoke: v2
harness_announce: "Using codebase-recon"
literal_copy: true
---

# Codebase / workspace reconnaissance

**Using `codebase-recon`.**  
Copied from skill `references/s0-s18-checklist.md` (literal copy), then filled.  
Remote: https://github.com/obra/superpowers

## S0 — Seed task context

- [x] README / CONTRIBUTING
- [x] Nearest `AGENTS.md` (pointer to `CLAUDE.md`)
- [x] Exact build/test/lint commands recorded with path citations (`FACT` [E0])

**FACT [E0]:** Local plugin.json version `6.1.1`.  
**FACT [E1]:** GitHub tip plugin.json version `6.2.0` (reconfirmed 2026-07-28).  
**FACT [E0]:** `docs/testing.md` claims `npm test` / `evals/`; `package.json` has no `scripts`; `evals/` absent — via `_e0_check_v2.py`.

## S1 — Declare comprehension goal

| Field | Value |
|-------|-------|
| Goal / task type | understand-for-X — smoke v2 of patched `codebase-recon` |
| Why this goal | Re-test harness after patches (announce, literal copy, S13 either-OK, Windows E0) |

## S2 — Choose strategy mode

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Scope boundary | Reconfirm prior smoke atoms + harness process; not full re-map |
| Missed-interaction risk noted? | yes — harness ports not re-walked |

## S3 — Memory / prior-knowledge check

- [x] Prior notes: `notes/smoke/archive/recon-superpowers.md` (v1)
- Findings reused as hypotheses; re-corroborated below

## S4 — Plan exploration agenda

1. Literal checklist copy
2. Python E0 re-check local version / evals / skills count
3. GitHub tip version reconfirm
4. Stop at S16 (research-only waive)

## S5 — Instruction / ignore surface

- [x] AGENTS.md / CLAUDE.md known from v1
- [x] Noise: N/A deep audit this pass

## S6 — Structure discovery

- [x] Top-level known: skills(14), hooks, docs, tests, scripts [E0 prior + skill count recheck]
- Entry: `.cursor-plugin/plugin.json`

## S7 — Top-down hypotheses

| ID | Expected | Status |
|----|----------|--------|
| H1 | Local still 6.1.1 | confirmed |
| H2 | Tip still 6.2.0 | confirmed |
| H3 | evals still missing | confirmed |

## S8 — Locate before edit

- [x] Path checks via Python (not brittle PS listing)
- Hit list: plugin.json, skills/, docs/testing.md

**Do not edit yet.**

## S9 — Isolate recon context

- [x] Explore used in v1; v2 as-needed reconfirm — Explore not re-spawned (scope tiny; skill allows skip for known paths)

## S10 — Selective read

| Path | Why | Notes | Open Q |
|------|-----|-------|--------|
| local plugin.json | version pin | 6.1.1 | — |
| remote plugin.json | skew | 6.2.0 | — |

## S11 — Inquiry episodes

| Question | Result |
|----------|--------|
| Did patches break skill paths? | No — all SKILL.md OK [E0 `_e0_check_v2.py`] |

## S12 — Architecture / dependency

Skipped — smoke harness retest. Reason = scope.

## S13 — Synthesize cited notes

- [x] **Short/smoke:** graded findings in this checklist (either-OK path)
- [ ] Full research-protocol note — not required this pass

## S14 — Persist findings

- [x] This file + `smoke-v2-summary.md`

## S15 — Reflect / re-plan

- [x] Sufficient for harness smoke v2
- Tool calibration: Python E0 preferred — MATCH vs prior Windows tip

## S16 — Completion gate (before implementation write tools)

- [x] Done-when for smoke v2 met
- [x] Claims cited
- [x] Verify cmds identified (with known drift)

**STOP.** Research-only — **human waive implement** (smoke).  
Research notes under `docs/research/` written — allowed under patched S16.

## S17 / S18

N/A implement. Artifacts: this note + `_e0_check_v2.py`.

### Graded findings

1. **FACT [E0]+[E1]:** Install 6.1.1 vs tip 6.2.0 skew still holds.  
2. **FACT [E0]:** `evals/` still absent; no package scripts.  
3. **FACT [E0]:** Literal checklist copy + announce performed (harness process).  
4. **INFERENCE [E4]:** Patched `codebase-recon` is operable without inventing APIs; S13 either-OK avoids false research-protocol tax.
