---
name: reproduce-bug
description: >-
  Never-fix companion: turn a vague bug into a failing reproduction and light
  dossier (status, command, failing output, hypothesis ledger, handoff) before
  any product patch. Use when reproduce-bug, prove the bug, minimal repro,
  flaky/intermittent, NOT-YET-REPRODUCED, or hand a fixer a regression guard.
  Does not implement fixes — hand off to systematic-debug. Not Theme 8 verify;
  not PR packaging.
---

# Reproduce bug

Announce once: **Using `reproduce-bug`**.

Authority: Theme 9 accepted (`docs/research/reports/theme-9-debug-pocket.md`). **Never patches** product/app code (except clearly marked repro artifacts: failing test, repro script, seed data).

**Identity:** Never-fix **companion** to `systematic-debug`. Quality = honest failing repro + cold handoff.

## When to use

- User wants the bug **proved** before a fix
- Intermittent / “works on my machine” / need a dossier
- After Execute verify-fail when the next step is characterize, not patch
- Handoff to a fixer or to `systematic-debug` for the fix phase

**Out of scope:** Implementing the product fix; Theme 8 verify; PR/CI; shipping collectors; mutating shared/prod environments without explicit user confirmation.

## Prime directive

> **No fix without a failing reproduction.** This skill proves the bug. If it disappears, that is a finding (`NOT-YET-REPRODUCED` / flaky) — not a resolution.

## Hard rules

1. **Read-only on app code** except repro artifacts in marked locations  
2. **Local/dev bench** — production supplies evidence only; mutating shared envs is one-way (name command + get confirmation)  
3. **One variable at a time**; record failed attempts  
4. **Repro must fail** — green ≠ repro  

## Spine

1. **Intake** — symptom, expected vs actual, where/when  
2. **Evidence sweep** — logs, stacks, recent diffs, env notes (read-only)  
3. **Path trace** — symptom site → callers / value origin (enough to aim repro)  
4. **Reproduce** — same surface (browser/API/CLI/job); shrink until load-bearing  
5. **Flaky path** if intermittent — measure → force nondeterminism → deterministic or `RATE-BASED (n/N)`  
6. **Light dossier** — fill the 8 fields (below); self-check status honesty  
7. **Handoff** — point fixer at command + acceptance (“green when this repro passes”); for product fix use **`systematic-debug`**

Read `references/reproduce-bug-checklist.md` **when** running a full prove session.  
Read Toolbelt `docs/templates/repro-light.md` **when** writing the dossier artifact.

## Light dossier (8 fields)

| # | Field |
|---|-------|
| 1 | Status — `DETERMINISTIC` \| `RATE-BASED (n/N)` \| `NOT-YET-REPRODUCED` |
| 2 | Symptom |
| 3 | Command / steps |
| 4 | Failing output (verbatim excerpt) |
| 5 | Load-bearing triggers |
| 6 | Hypothesis ledger (append-only) |
| 7 | Attempt #0+ |
| 8 | Handoff acceptance |

Prefer writing `docs/repro/<slug>.md` or `REPRO.md` in the host repo.

## Anti-patterns

- Patching the bug “while reproducing”  
- Calling a green run a repro  
- Overselling `NOT-YET` as deterministic  
- Investigating only against production  
- Fat ceremony (full silkyland port) — keep the 8 fields  

## Handoffs

| Need | Use |
|------|-----|
| Fix with evidence | **`systematic-debug`** |
| Execute / verify loop | `implementation-execute` / `implementation-execute-verify` |
| Unfamiliar code | `codebase-recon` |

## References

- Read `references/reproduce-bug-checklist.md` **when** running a full prove session
- Template SoT: Toolbelt `docs/templates/repro-light.md`
- Theme 9: Toolbelt `docs/research/reports/theme-9-debug-pocket.md` (accepted)
