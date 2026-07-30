---
title: "T8 track synthesis — Verify gates"
status: draft
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: deep
campaign_phase: deep_integrate
aligned_with:
  - docs/research/notes/theme-8-verify/t8-w3-plus1-residual.md
  - docs/research/notes/theme-8-verify/campaign-brief.md
supersedes: null
---

# T8 track synthesis

**Using `research-protocol`** · integrator merge · no new facts.

**Identity:** Missing verification extensions of Plan + Execute — **not** Debug/PR.  
**stop_reason:** `low_return_plus_one` (from PLUS1).

## Merged spine

```text
Plan pocket
  write-plan (implementation-plan) → V1–V8 light
  → implementation-plan-verify (explicit phase)
      Reality ‖ Drift ‖ Coverage/Actionability
      severity + PASS / PASS WITH NOTES / NEEDS REVISION
      fix-plan-not-code; hard intent-gap
  → Meta ready (or blocked)

Execute pocket
  implementation-execute (/ -subagents)
  → Done-when signal verify (N=2 frozen)
  → implementation-execute-verify
      iron law audit
      post-green Evidence+Faithfulness+Readability (when non_trivial; fresh)
      EOP: review + light converge (append Convergence tasks)
  → Theme 7 HITL on blocked / major deviation
```

## Decisions for draft report (from §0 + PLUS1 FC-*)

See [`t8-w3-plus1-residual.md`](./t8-w3-plus1-residual.md) freeze table — surface C, G1/G2/G3, dual-lane severity, EOP-only converge, append grammar, parks.

## Source index

| Wave | Notes |
|------|-------|
| Scope | pass1–3, campaign-brief, coordinator-pin |
| W1 | t8a–t8d w1 notes, t8-w1-track-board |
| W2 | t8-w2-rubrics, t8-w2-thresholds |
| +1 | t8-w3-plus1-residual |
| Input law | Theme 6 + Theme 7 accepted reports |

## Next

Draft report `docs/research/reports/theme-8-verify-gates.md` → human accept → elevate companions + wire orchestrators.
