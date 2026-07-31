---
title: "Theme 11 Phase B evaluation — 2026-07-30"
status: accepted
theme: theme-11-validation
created: 2026-07-30
updated: 2026-07-30
accepted: 2026-07-30
accepted_by: human (Jonathan)
authors: [coordinator]
aligned_with:
  - docs/research/notes/theme-11-validation/campaign-brief.md
  - docs/research/notes/theme-11-validation/smoke-matrix.md
  - docs/research/notes/theme-11-validation/runs/CONTROLLER-SUMMARY-20260730.md
  - docs/research/notes/theme-11-validation/runs/exports/2026-07-30/
  - docs/research/reports/theme-11-validation.md
supersedes: null
---

# Theme 11 Phase B evaluation — 2026-07-30

**Using `research-protocol`**. **Accepted** with Theme 11 report — E0 P0 validation record.

## 1. Evidence ingested

| Source | Path |
|--------|------|
| Structured runs | `runs/*-20260730.md` + `CONTROLLER-SUMMARY-20260730.md` |
| Chat exports | `runs/exports/2026-07-30/` (`cursor_controller_pocket_smokes.md`, `cursor_draft_not_saved_issue.md` = U1, `cursor_u2_research_protocol_grades.md`, `cursor_happy_path_implementation.md`) |
| Artifacts | `runs/artifacts/` |

## 2. Scoreboard (P0)

| Result | Count | IDs |
|--------|------:|-----|
| **PASS** | **18** | U1, U2, R1–R6, D1–D2, P1–P2, E1–E3, G1–G2, H1 |
| PASS WITH NOTES (pocket) | 0 | — |
| **NEEDS REVISION** | **0** | — |

Inner-skill nuance (not pocket fail): **P2** plan-verify returned **PASS WITH NOTES** (assumed Decision) while the *smoke claim card* scored PASS — correct behavior.

## 3. Lane results

| Lane | Surfaces | Outcome |
|------|----------|---------|
| Fresh chat | U1, U2, H1 (A+B+C) | All PASS |
| Controller + subagents | R1–R6, D1–D2, P1→P2, G2→G1, E1–E3 | All PASS |

## 4. High-signal behaviors (quality)

- **U1:** Refused draft-only stack lock/implement; required accept/ADR.
- **U2:** E0 skill count ×3; private debug-server wire → GAP/OPEN (no invention).
- **H1:** Bug → Debug entry with documented design skip; feature ladder on B; ADR-only on C; workers=one pocket.
- **G2:** Never-fix + 8-field dossier; fixture `app.py` left buggy.
- **G1:** Repro → fix in `work-g1` only → same-repro green; fixture source untouched.
- **E1:** Verify evidence + N=2 policy stated; one-attempt green.
- **E3:** Correctly **rejected** fabricated “fixed” claim (Evidence fail).
- **P1/P2:** Plan + graded plan-verify without coding.

## 5. Optional NOTES (non-blocking)

| ID | Note | Priority |
|----|------|----------|
| P2 | Soft assumed Decision → PASS WITH NOTES; tighten fixture optional | P2 polish |
| E3 | Fabricated-evidence smoke — keep in regression set | keep |
| Matrix | Creative-* / intelligent rules **P1 deferred** | optional |
| Export | U1 file `cursor_draft_not_saved_issue.md` — content is U1 | hygiene |

## 6. Deep research?

**No.** Phase B E0 closed “does P0 work?” Deep harness only if automation becomes a goal.

## 7. Implications

- Theme 11 Phase B P0 validation **succeeds**; no mandatory tune wave.
- Integrated report: [`docs/research/reports/theme-11-validation.md`](../../reports/theme-11-validation.md).

## 8. Acceptance checklist

- [x] Accept this evaluation (P0 green)
- [x] Draft/accept Theme 11 validation report
- [x] Exports under `runs/exports/`
- [ ] Optional: P1 creatives / intelligent rules
