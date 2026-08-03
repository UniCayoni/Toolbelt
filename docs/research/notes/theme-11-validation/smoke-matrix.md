---
title: "Theme 11 — P0 smoke matrix"
status: draft
theme: theme-11-validation
created: 2026-07-30
updated: 2026-07-31
authors: [coordinator]
campaign_phase: phase_b_integrated
aligned_with:
  - docs/research/notes/theme-11-validation/campaign-brief.md
  - docs/research/notes/theme-11-validation/phase-b-evaluation-20260730.md
  - docs/research/notes/theme-11-validation/runs/CONTROLLER-SUMMARY-20260730.md
  - docs/research/reports/theme-12-research-scoping.md
supersedes: null
---

# Theme 11 — P0 smoke matrix

**Model default:** `cursor-grok-4.5-high-fast`  
**Runs log:** `docs/research/notes/theme-11-validation/runs/`  
**Claim cards:** `claim-cards/`  
**Controller summary:** [CONTROLLER-SUMMARY-20260730.md](./runs/CONTROLLER-SUMMARY-20260730.md)  
**Phase B evaluation:** [phase-b-evaluation-20260730.md](./phase-b-evaluation-20260730.md) — **18/18 PASS**, 0 NEEDS REVISION (2026-07-30).  
**Theme 12 delta (2026-07-31):** re-smoke R1–R3, H1 + new **R7** `research-scope` — all **PASS** (see `*-20260731.md`).  
**Theme 14 delta (2026-07-31):** new **I1** `implementation-router` + H1 re-smoke — in-session **2/2** + fresh **2/2** = **4/4 PASS** ([theme-14-smoke-delta-20260731.md](./theme-14-smoke-delta-20260731.md)).  
**Theme 15 delta (2026-08-02):** new **C1** `implementation-closeout` — in-session + fresh **2/2 PASS**.  
**Theme 16 delta (2026-08-02):** new **S1** `author-standards` — in-session + fresh **2/2 PASS**.  
**Theme 17 delta (2026-08-02):** new **R8** `debug-router` — in-session + fresh **2/2 PASS**.  
**Theme 18 delta (2026-08-03):** new **R9** recon **S12b** / derive glue — in-session + fresh **2/2 PASS**.  
**Theme 19 delta (2026-08-03):** new **S2** `standards-router` — in-session PASS; fresh optional / pending review.

| ID | Surface | Lane | Fixture | Card | Run status |
|----|---------|------|---------|------|------------|
| U1 | draft-is-not-sot | fresh_chat | none | [u1](./claim-cards/u1-draft-is-not-sot.md) | PASS (`U1-20260730.md`; not re-run) |
| U2 | research-protocol-grades | fresh_chat | none | [u2](./claim-cards/u2-research-protocol-grades.md) | PASS (`U2-20260730.md`; not re-run) |
| R1 | research-protocol | subagent | none / notes path | [r1](./claim-cards/r1-research-protocol.md) | PASS (`R1-20260731.md`; prior `R1-20260730.md`) |
| R2 | research-codebase-recon | subagent | Toolbelt repo | [r2](./claim-cards/r2-research-codebase-recon.md) | PASS (`R2-20260731.md`) |
| R3 | research-docs | subagent | public URL pin | [r3](./claim-cards/r3-research-docs.md) | PASS (`R3-20260731.md`) |
| R4 | research-draft-adr | subagent | temp | [r4](./claim-cards/r4-research-draft-adr.md) | PASS (`R4-20260730.md`; not re-run) |
| R5 | author-agents-md | subagent | temp | [r5](./claim-cards/r5-author-agents-md.md) | PASS (`R5-20260730.md`; not re-run) |
| R6 | author-cursor-surfaces | subagent | temp | [r6](./claim-cards/r6-author-cursor-surfaces.md) | PASS (`R6-20260730.md`; not re-run) |
| R7 | research-scope | subagent | none | [r7](./claim-cards/r7-research-scope.md) | PASS (`R7-20260731.md`) **Theme 12** |
| D1 | design-process | subagent | none | [d1](./claim-cards/d1-design-process.md) | PASS (`D1-20260730.md`; not re-run) |
| D2 | design-technical | subagent | none | [d2](./claim-cards/d2-design-technical.md) | PASS (`D2-20260730.md`; not re-run) |
| P1 | implementation-plan | subagent | smoke-app context | [p1](./claim-cards/p1-implementation-plan.md) | PASS (`P1-20260730.md`; not re-run) |
| P2 | implementation-plan-verify | subagent | plan from P1 or stub | [p2](./claim-cards/p2-implementation-plan-verify.md) | PASS (`P2-20260730.md`; not re-run) |
| E1 | implementation-execute | subagent | copy of smoke-app | [e1](./claim-cards/e1-implementation-execute.md) | PASS (`E1-20260730.md`; not re-run) |
| E2 | implementation-execute-subagents | subagent | copy of smoke-app | [e2](./claim-cards/e2-implementation-execute-subagents.md) | PASS (`E2-20260730.md`; not re-run) |
| E3 | implementation-execute-verify | subagent | after green task | [e3](./claim-cards/e3-implementation-execute-verify.md) | PASS (`E3-20260730.md`; not re-run) |
| G1 | debug-systematic | subagent | copy of smoke-app | [g1](./claim-cards/g1-debug-systematic.md) | PASS (`G1-20260730.md`; not re-run) |
| G2 | debug-reproduce | subagent | copy of smoke-app | [g2](./claim-cards/g2-debug-reproduce.md) | PASS (`G2-20260730.md`; not re-run) |
| H1 | implementation-happy-path | fresh_chat | Toolbelt | [h1](./claim-cards/h1-implementation-happy-path.md) | PASS fresh (`H1-fresh-20260731.md`); prior in-session `H1-20260731-theme14.md` **Theme 14** |
| I1 | implementation-router | either | none | [i1](./claim-cards/i1-implementation-router.md) | PASS fresh (`I1-fresh-20260731.md`); prior in-session `I1-20260731.md` **Theme 14** |
| C1 | implementation-closeout | either | none | [c1](./claim-cards/c1-implementation-closeout.md) | PASS fresh (`C1-fresh-20260802.md`); prior in-session `C1-20260802.md` **Theme 15** |
| S1 | author-standards | either | none | [s1](./claim-cards/s1-author-standards.md) | PASS fresh (`S1-fresh-20260802.md`); prior in-session `S1-20260802.md` **Theme 16** |
| S2 | standards-router | either | t19-catalog artifact | [s2](./claim-cards/s2-standards-router.md) | in-session PASS (`S2-20260803.md`); fresh optional **Theme 19** |
| R8 | debug-router | either | none | [r8](./claim-cards/r8-debug-router.md) | PASS fresh (`R8-fresh-20260802.md`); prior in-session `R8-20260802.md` **Theme 17** |
| R9 | recon S12b / derive glue | either | none | [r9](./claim-cards/r9-recon-history.md) | PASS fresh (`R9-fresh-20260803.md`); prior in-session `R9-20260803.md` **Theme 18** |

**P1 (deferred):** design-systems / narrative / world-character deep smokes; research-before-write.

## Phase B run order

1. U1, U2 (fresh)  
2. R1–R6 (parallel subagents OK)  
3. D1, D2  
4. P1 → P2  
5. G2 → G1 (prove then fix) **or** E1 on fixed plan  
6. E1 / E2 / E3  
7. H1 fresh chat  

## Runner instructions (subagent)

1. Read claim card.  
2. Announce Using the target skill.  
3. Follow pinned smoke prompt only; do not elevate or redesign.  
4. Fill Score columns + Verdict.  
5. Write run log: `runs/<ID>-YYYYMMDD.md` with evidence quotes.  
