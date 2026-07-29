---
title: "Smoke v4 — coexistence stress + auto-fire probe"
status: draft
created: 2026-07-28
---

# Plan

## A. Coexistence stress

**Task:** Add a short root `CONTRIBUTING.md` that points agents at `AGENTS.md` + research harness (implementation-like write outside `docs/research/`).

**Staging:**
1. `using-superpowers` — skill check first
2. `codebase-recon` (GreyMatter) — as-needed recon before write (template/grades)
3. Optional brief graded note under smoke/
4. Write `CONTRIBUTING.md` (only E0-known links)
5. `verification-before-completion` — fresh E0 verify before claiming pass

**Pass criteria:** Both layers announced; GreyMatter template/grades used; no invented Superpowers git workflow; file exists and links resolve.

## B. Auto-fire probe

**Question:** Without the human naming `codebase-recon` / `research-before-write`, does the agent still recon before a non-trivial implementation write when the intelligent rule *should* apply?

**Limits:** Same-session contamination (rules already discussed). Score as:
- **PASS** if probe task runs recon/announce GreyMatter recon *before* write without human naming those skills in the probe instruction
- **PARTIAL** if recon happens only because this plan named it
- **GAP** if we cannot separate contamination from true Cursor auto-inject

This plan file names the skills for coexistence (A). For auto-fire (B), the probe instruction in the summary will be evaluated against whether the *human* message required naming — human asked for coexistence + auto-fire smoke generally, which implies testing auto-fire; we treat **v4 human ask as naming the test, not naming the skill mid-edit**. Score: if agent runs recon before CONTRIBUTING write as part of staged coexistence, that proves coexistence path more than silent auto-fire.  

**Additional auto-fire micro-probe:** After CONTRIBUTING exists, make a **second** tiny edit (`CONTRIBUTING.md` add one “Smoke v4” line) while *consciously not* re-reading the rule file first — only follow ambient always-apply rules + whether intelligent rule content is in context. Record whether recon was re-done (as-needed skip for known file is allowed by skill).

## Determination table

| Surface | Pass | Partial | Fail/GAP |
|---------|------|---------|----------|
| Coexistence staging | Both layers used; GM templates win for artifacts | Soft note only | Conflict/invented merge |
| Auto-fire | Unprompted recon before implement write | Contaminated / plan-led | Skipped recon on unfamiliar implement |
