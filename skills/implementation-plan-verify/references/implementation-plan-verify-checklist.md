---
title: Implementation plan-verify checklist
status: active
aligned_with: docs/research/reports/theme-8-verify-gates.md
---

# Implementation plan-verify checklist

Use with skill `implementation-plan-verify`.

## Phase

- [ ] After write-plan / plan update; before Meta `ready` / execute
- [ ] Trivial skip documented **or** full validate below
- [ ] Fix-plan-not-code; re-validate after edits

## Verification table (non-trivial)

- [ ] Claim · Method · Result · Severity for cited paths / APIs / packages / commands
- [ ] Reality BLOCKERs recorded

## Parallel lanes

- [ ] **Reality** — no hallucinated paths/APIs/commands
- [ ] **Drift** — reused plan matches tree/deps
- [ ] **Coverage** — in-scope FRs/sections have tasks; no orphan in-scope gaps
- [ ] **Actionability** — tasks not composite mash / ambiguous / misordered; deps acyclic
- [ ] **Verify quality** — command + expected signal; falsifiable (ban “looks good”)
- [ ] Light taxonomy notes: composite / ambiguous / coverage_gap / misordered

## Verdict

- [ ] Severities aggregated (BLOCKER / CRITICAL / WARNING / NIT)
- [ ] Verdict: PASS | PASS WITH NOTES | NEEDS REVISION
- [ ] Hard inventable gaps → NEEDS REVISION + `intent-gap` when invent required
- [ ] Soft ambiguity only → PASS WITH NOTES OK
- [ ] Meta not `ready` until PASS*

## Hard vs soft ambiguity

**Hard → BLOCKER/CRITICAL + NEEDS REVISION** (+ `intent-gap` if invent required):

- Multi-intent Goal/Done-when/Interfaces with no Decision/ADR close
- TBD / placeholder / “similar to Task N”
- Verify not falsifiable (“looks good”, no command/signal)
- In-scope FR/section with zero tasks
- Reality invent (nonexistent path/API treated as given)
- Dependency cycle

**Soft → WARNING → PASS WITH NOTES** (unique path still exists):

- Vague adjective but Done-when still unique/falsifiable
- Soft undeclared order preference (no cycle)
- Serial-safe composite (recommend split)
- Orphan task with explicit out-of-scope justification

## Quality lean (plan as agent contract)

- [ ] Faithful to accepted Design/ADR (no invent)
- [ ] Readable task units (coherent reviewable; clear Files/Interfaces)
- [ ] Notes recorded for PASS WITH NOTES
