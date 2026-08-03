---
name: debug-systematic
description: >-
  Investigate and fix bugs with evidence: reproduce (or NOT-YET-REPRODUCED),
  hypothesize and falsify, backward root-cause, minimal fix, verify the same
  repro; compose Cursor Debug Mode / Terminal / Browser; stop after
  debug-fix-cycles=3. Use when debugging, root-cause, investigate failure,
  verify-fail after Execute N=2, race/intermittent bug, unexpected behavior,
  or debug-systematic. Prefer debug-reproduce first when the job is prove-only.
  Not Theme 8 plan/execute-verify; not PR/CI packaging. Formerly systematic-debug.
---

# Systematic debug

Announce once: **Using `debug-systematic`**.

Authority: Theme 9 accepted (`docs/research/reports/theme-9-debug-pocket.md`). Standalone Toolbelt — inspire from community; **do not import** third-party debug packaging as Toolbelt law. **Draft ≠ law** (`draft-is-not-sot`).

**Identity:** Debug / investigate / reproduce **method** pocket. **Not** Theme 8 Verify gates. **Not** PR/CI/Bugbot pack.

## When to use

- User reports a bug, regression, crash, or unexpected behavior
- Execute `verify-fail` after **verify-retry N=2** exhausted (do not burn more Execute retries)
- Major-deviation / weird runtime beyond plan Files; unclear Critical from execute-verify
- Cause unclear; races / intermittent / needs runtime evidence

**Prefer first:** **`debug-reproduce`** when the ask is prove/minimize/dossier only (never-fix).

**Out of scope:** Re-owning Execute N=2 or Theme 8 iron law/converge; inventing Cursor private debug-server APIs; shipping collectors/MCP; PR/merge packaging; default multi-agent swarm.

## Iron law

**No product/code fix until a failing reproduction exists, or the case is tagged `NOT-YET-REPRODUCED` with evidence of attempts and blockers.** Green ≠ repro.

## Spine (do in order)

1. **Intake** — expected vs actual; artifacts (error/stack/steps/env); frequency; surface (test/CLI/UI/API)
2. **Reproduce** — same surface as the report; shrink to load-bearing steps  
   - Intermittent → **flaky light checklist** (below)  
   - Cannot repro → `NOT-YET-REPRODUCED` (+ light dossier via `debug-reproduce` / `repro-light`); no guess-fix
3. **Evidence path** (compose Cursor — do not reimplement Debug Mode server):
   - Clear local fail → **Terminal** (run command; **READ** available output)
   - UI → **Browser** (console, network, greppable file logs, screenshots)
   - Unclear cause / race / timing / perf + human can drive repro → prefer **Cursor Debug Mode** (picker / Shift+Tab / CLI `/debug`; `/logs` for product path)
   - Prod spike → host **MCP observe** if configured → still seek local repro
   - Debug Mode unavailable → **Agent instrumentation** (below)
4. **Hypothesize** — 1–4 ranked falsifiable rows (serial default); 3–5 with `hypothesisId` when instrumenting in parallel
5. **Falsify** — smallest experiment; status `CONFIRMED` | `REJECTED` | `INCONCLUSIVE` with cited evidence
6. **Root cause** — backward trace (symptom → immediate cause → callers → original trigger); one-sentence cause before patch
7. **Minimal fix** — address cause; no drive-by; optional defense-in-depth note after invalid-data bugs
8. **Verify same repro** — re-run exact repro from step 2; evidence before “fixed”; **cleanup** temp instrumentation
9. **Stop / escalate** — after **`debug-fix-cycles` = 3** failed fix cycles (post strong/confirmed hypothesis) or architecture smell → human  
   - This budget is **not** Execute `verify-retry N=2`

Read `references/debug-systematic-checklist.md` **when** running a full session or recovering a skipped step.

## Flaky light checklist

1. **Measure** rate (e.g. 10–20 runs) before guessing  
2. **Classify** nondeterminism: concurrency, clock, ordering, randomness, network, cache/shared state, test pollution  
3. **Force** it (seeds, frozen clock, ordering, interleaving) → prefer deterministic repro  
4. Else deliver **RATE-BASED (n/N)** + recipe — never dress as deterministic  
5. Heisenbugs: prefer passive capture / non-timing levers before sleeps

## Agent instrumentation (when not using Cursor Debug Mode)

Teach protocol atoms only — **no Toolbelt collector**, no invented Cursor private wire:

- Tag logs with `hypothesisId`; classify CONFIRMED/REJECTED/INCONCLUSIVE  
- Prefer compact NDJSON-**shaped** fields (`location`, `message`, `data`, `timestamp`) via language I/O or tagged stdout  
- Mark probes (`#region debug log` / equivalent); **keep** through post-fix verify; then remove  
- Redact secrets; clear between runs; revert unproven speculative fixes  
- Cite log lines / command output in the claim

## Seam triggers (from Execute / Verify)

| ID | When |
|----|------|
| T-VF | `verify-fail` after Execute N=2 |
| T-UB | User bug outside plan |
| T-MD | Major-deviation / weird runtime |
| T-CR | Unclear Critical from execute-verify |
| T-NYR | Need prove-first → `debug-reproduce` |

## Anti-patterns

- Fixing from code-read alone without repro / NOT-YET tag  
- Conflating `debug-fix-cycles` with Execute `verify-retry N=2`  
- Reimplementing Cursor’s private debug-server  
- Shipping or depending on NDJSON collectors inside Toolbelt  
- Claiming fixed without re-running the **same** repro  
- Leaving instrumentation in the tree  
- Thrashing past 3 failed fix cycles without escalating

## Handoffs

| Need | Use |
|------|-----|
| Prove / dossier only (never-fix) | **`debug-reproduce`** |
| Which Debug skill / pocket wire | **`debug-router`** |
| Plan still wrong | `implementation-plan` + `implementation-plan-verify` |
| Execute task loop / N=2 | `implementation-execute` |
| Post-green / converge | `implementation-execute-verify` |
| Unfamiliar code before investigate | `research-codebase-recon` (as-needed) |
| PR / CI / Bugbot | Phase 2 — not this skill |

## References

- Read `references/debug-systematic-checklist.md` **when** running a full debug session
- Light dossier fields: Toolbelt `docs/templates/repro-light.md` / skill `debug-reproduce`
- Theme 9: Toolbelt `docs/research/reports/theme-9-debug-pocket.md` (accepted)
- Theme 7/8 boundaries: execute N=2 + verify companions stay owned there
