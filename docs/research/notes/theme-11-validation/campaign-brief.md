---
title: "Theme 11 — Plugin surface validation campaign brief"
status: draft
theme: theme-11-validation
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: normal
campaign_phase: phase_b_integrated
aligned_with:
  - docs/research/notes/theme-11-validation/scope-normal-pass1.md
  - docs/research/notes/theme-11-validation/phase-b-evaluation-20260730.md
  - docs/PROTOCOL.md
supersedes: null
---

# Theme 11 — Validation campaign brief

**Using `research-protocol`**.  
**Status:** `draft` brief — **human approved** 2026-07-30 (recommended leans). Phase B P0 smokes integrated — see [`phase-b-evaluation-20260730.md`](./phase-b-evaluation-20260730.md). Not product SoT until a Theme 11 report is accepted.  
**Scoping:** [`scope-normal-pass1.md`](./scope-normal-pass1.md).

---

## 0. Depth verdict (locked)

| Decision | Lock |
|----------|------|
| Deep research **before** first smokes? | **No** |
| Deep later? | Only if automated harness / multi-run stats / judge SoT become goals |

---

## 1. Locked lean (human-accepted)

| Item | Value |
|------|-------|
| Method | Claim card → smoke → Theme 8 verdict → tune → re-smoke |
| Lanes | **Hybrid**: fresh chat (discovery) + subagents (pocket batch) |
| Metrics MVP | Checklist pass-rate, invoke success, artifact checks, anti-patterns |
| Order | Rules → Research → Design/Plan/Execute/Verify/Debug → Happy-path last |
| Smoke model default | `cursor-grok-4.5-high-fast` |
| Fixture home | `docs/research/fixtures/` (in-repo) |
| Automation | Deferred |

---

## 2. Phases

| Phase | Work | Status |
|-------|------|--------|
| A | Claim cards + smoke prompts + fixture stub | **done** |
| B | Run P0 smokes; log under `runs/` (incl. `exports/`) | **done** (18/18 PASS; 0 NEEDS REVISION) |
| C | Integrate + tune NEEDS REVISION | **done** (integrate); tune wave **N/A** |
| D | Optional deep harness | opt-in |
| Report | `docs/research/reports/theme-11-validation.md` | **accepted** 2026-07-30 |

---

## 3. Approval gate

- [x] Accept **no deep-before-E0** verdict  
- [x] Accept hybrid lanes + MVP metrics  
- [x] Smoke model `cursor-grok-4.5-high-fast`  
- [x] Fixture home `docs/research/fixtures/`  
- [x] Phase A authorized  

Hard rule: do not block validation on vendor eval fleets.
