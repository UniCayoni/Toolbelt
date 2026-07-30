---
title: Implementation execute-verify checklist
status: active
aligned_with: docs/research/reports/theme-8-verify-gates.md
---

# Implementation execute-verify checklist

Use with skill `implementation-execute-verify`.

## Evidence (iron law)

- [ ] IDENTIFY verify command from plan task
- [ ] RUN command
- [ ] READ full output / exit
- [ ] VERIFY expected signal matched
- [ ] No “should/looks/seems” completion claims

## Post-green review

- [ ] Required? (non-trivial task **or** EOP on durable plan) — else optional trivial note
- [ ] Fresh reviewer context when required
- [ ] Dimensions: Evidence · Faithfulness · Readability/coherence
- [ ] Findings: Critical / Important / Minor
- [ ] Critical/Important fixed or Theme 7 escalate; Minor noted
- [ ] N=2 unchanged (owned by Execute)

## EOP light converge (durable plans)

- [ ] Findings presented before write
- [ ] Gap types: missing / partial / contradicts / unrequested
- [ ] Append `## Convergence` tasks only if actionable (else byte-unchanged)
- [ ] No Goal / constraints / existing task rewrite
- [ ] No application code edits in converge pass
- [ ] Meta S1 sync if tasks appended (`in_progress` if was `done`)
- [ ] Not run as default after every task (EOP-only)

## Quality lean

- [ ] Faithful to plan + accepted design
- [ ] Readable / maintainable result (boundaries, naming, no drive-by)
- [ ] Unrequested scope not silently accepted
