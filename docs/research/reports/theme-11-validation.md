---
title: "Theme 11 — Plugin surface validation (integrated report)"
status: accepted
theme: theme-11-validation
created: 2026-07-30
updated: 2026-07-30
accepted: 2026-07-30
acceptance_scope: e0_p0_validation_record
accepted_by: human (Jonathan)
authors: [integrator]
depth: normal
stop_reason: e0_smokes_sufficient
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-11-validation/campaign-brief.md
  - docs/research/notes/theme-11-validation/phase-b-evaluation-20260730.md
  - docs/research/notes/theme-11-validation/smoke-matrix.md
supersedes: null
---

# Theme 11 — Plugin surface validation

**Status:** **accepted** (E0 P0 validation record) — 2026-07-30.  
**Depth:** normal claim-card smokes (no deep harness).  
**Elevation:** none required — P0 surfaces already shipped; validation only.

**Using `research-protocol`** · integrator.

### Acceptance decisions

| # | Decision |
|---|----------|
| D1 | Phase B P0 scoreboard **18/18 PASS**, **0 NEEDS REVISION** |
| D2 | No mandatory skill/rule tune wave from this campaign |
| D3 | Deep validation harness **deferred** (opt-in Phase D) |
| D4 | Creative-* / intelligent rules remain **P1 deferred** |
| D5 | Evidence home: `docs/research/notes/theme-11-validation/runs/` (logs + `exports/` + `artifacts/`) |

---

## 1. Executive summary

Theme 11 asked whether shipped Toolbelt P0 surfaces behave as designed under E0 smokes. Hybrid lanes (fresh chat + pocket controller/subagents) on `cursor-grok-4.5-high-fast` produced a clean pass rate. No elevation and no blocking revisions.

---

## 2. Sources

- [`campaign-brief.md`](../notes/theme-11-validation/campaign-brief.md)
- [`smoke-matrix.md`](../notes/theme-11-validation/smoke-matrix.md)
- [`phase-b-evaluation-20260730.md`](../notes/theme-11-validation/phase-b-evaluation-20260730.md)
- [`CONTROLLER-SUMMARY-20260730.md`](../notes/theme-11-validation/runs/CONTROLLER-SUMMARY-20260730.md)
- Run logs + chat exports under [`runs/`](../notes/theme-11-validation/runs/)
- Fixture: [`docs/research/fixtures/smoke-app/`](../fixtures/smoke-app/)

---

## 3. Scoreboard

| Result | Count | IDs |
|--------|------:|-----|
| PASS | 18 | U1–U2, R1–R6, D1–D2, P1–P2, E1–E3, G1–G2, H1 |
| NEEDS REVISION | 0 | — |

Inner nuance: P2 skill verdict **PASS WITH NOTES** (soft Decision) while pocket claim-card scored PASS — expected.

---

## 4. High-signal checks

- Draft≠SoT refuse (U1); cite-or-omit / GAP on private wire (U2)
- Happy-path classify + compose order; workers = one pocket (H1)
- Reproduce never-fix (G2); debug fix scoped to work copy (G1)
- Execute verify-retry policy (E1); execute-verify rejects fabricated done (E3)

---

## 5. Out of scope / parked

| Item | Status |
|------|--------|
| Automated multi-run harness | Phase D opt-in |
| Creative design skills + intelligent rules smokes | P1 optional |
| Skill elevation from Theme 11 | Not indicated |

---

## 6. Acceptance checklist

- [x] Human accepted Phase B evaluation / P0 green  
- [x] Theme 11 report accepted as validation record  
- [x] Evidence under `runs/` (incl. exports)  
- [ ] Optional: P1 creative / intelligent-rule smokes  
- [ ] Optional: Phase D harness  
