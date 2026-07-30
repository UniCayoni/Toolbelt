---
title: "Theme 7 — Execution pocket (integrated report)"
status: accepted
theme: theme-7-execute
created: 2026-07-30
updated: 2026-07-30
accepted: 2026-07-30
acceptance_scope: method_guidance_t7_execute
accepted_by: human (Jonathan)
authors: [integrator]
depth: deep
stop_reason: low_return_plus_one
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-7-execute/campaign-brief.md
  - docs/research/notes/theme-7-execute/t7-track-synthesis.md
  - docs/research/notes/theme-7-execute/t7-w3-plus1-residual.md
  - docs/research/reports/theme-6-plan-pocket.md
  - skills/implementation-execute/SKILL.md
  - skills/implementation-execute-subagents/SKILL.md
supersedes: null
---

# Theme 7 — Execution pocket (integrated report)

**Status:** **accepted** (method guidance) — 2026-07-30.  
**Elevated:** `implementation-execute` + `implementation-execute-subagents`.  
**Campaign stop:** `low_return_plus_one`.

**Using `research-protocol`** · integrator merge.

**Pocket scope:** drive approved Theme 6 plans to code with cold/fresh agents — verify, escalate, quality/readability. Standalone Toolbelt (inspire; **do not depend** on Superpowers/OpenSpec/BMAD). Fuller review → later (pocket or touchups).

### Elevation decisions (accepted 2026-07-30)

| # | Decision |
|---|----------|
| D1–D4 | Brief §7.1 directional (standalone; spine+supplements; HITL blocked/major deviation; light companions / review later) |
| O-NAME | Spine skill **`implementation-execute`** (pairs with `implementation-plan`) |
| O-N | Verify-retry **N=2** then `blocked`+`verify-fail` |
| O-MD | Major-deviation checklist from PLUS1 (File map, Interfaces, deps, Never/Do-not, Goal/Done-when, irreversible ops, drive-by refactors) |
| O-SYNC | Meta↔task **S1** (aggregate) |
| O-FRESH | **Highly recommend** fresh context at plan→execute — **new chat or fresh subagent** (same idea for short parent context) |
| O-SUB | Separate supplementary skill **`implementation-execute-subagents`** |
| O-VFOLD | Light evidence-before-done **folded** into spine |
| — | Ledger default = plan file Status/checkboxes; park foreign packaging |

---

## 1. Executive summary

1. Execute teaches load → critical review → statused task loop → Done-when evidence → escalate don’t invent → continuous when green.  
2. Vendors/community converge on the loop; packaging parked.  
3. Subagent controller is the broad-use supplement.  
4. Skills elevated: `implementation-execute`, `implementation-execute-subagents`.

---

## 2. Sources merged

Notes under `docs/research/notes/theme-7-execute/` (W1–W3 + synth). Subagents: `cursor-grok-4.5-high-fast`.

---

## 3. Method spine (accepted)

```text
0. Plan ready (or waive) · highly recommend fresh chat or fresh subagent
1. Load plan
2. Critical review (raise ≠ invent)
3. Task loop — serial default; Plan #2 parallel-safe; Verify; N=2; Meta S1
4. Escalate — intent-gap | verify-fail | needs-human | major-deviation
5. Continuous when green
```

Controller mode: same spine via `implementation-execute-subagents`.

---

## 4. Boundaries

| Execute | Plan | Later review/debug | Out |
|---------|------|--------------------|-----|
| Run loop; light verify; subagent controller | Author; V1–V8; grammar; `implementation-plan` | Fuller review; deep validate; PR/finish; debug | Build cookbooks; plugin dependency |

---

## 5. Elevation status

| Surface | Status |
|---------|--------|
| `implementation-execute` | **Shipped** |
| `implementation-execute-subagents` | **Shipped** |
| Checklist | `skills/implementation-execute/references/` |
| `plan-minimal` execution notes | Updated |

---

## 6. Acceptance checklist

- [x] Accept method guidance  
- [x] P0 OPENs decided  
- [x] Elevate spine + subagent supplement  
- [ ] Later: review home (pocket vs touchups) — deferred  
