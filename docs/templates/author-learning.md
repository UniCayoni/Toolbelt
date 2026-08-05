---
title: "Author-learning checklist (quality-gated harvest)"
status: active
aligned_with: docs/research/reports/theme-24-author-learning.md
created: 2026-08-05
---

# Author-learning — checklist

Authority: Theme 24 accepted. Used by skill **`author-learning`**.  
**Quality-gated harvest** — ease is a side effect, not the goal.  
Copy into a host note for multi-candidate jobs; do not edit this SoT as the deliverable.  
**Draft / proposed ≠ law** until human accepts each promotion.

## 0 — Trigger & intent

| Field | Value |
|-------|-------|
| Trigger | `explicit /` \| `closeout + citable friction` \| other (name evidence) |
| Host workspace paths in scope |  |
| Toolbelt plugin `skills/*` as target? | **No** (refuse) |

- [ ] Evidence-warranted (not ambient / always-on)
- [ ] Intent: keep only learnings that survive quality + evidence floors

## 1 — Quality gate (before any propose)

For **each** candidate, complete before status may be `proposed`:

| Check | Pass? |
|-------|-------|
| Recurring pain / problem named | |
| Evidence + locator present | |
| Label + grade (FACT/CLAIM/… ; E0–E4) — **not U** | |
| Change type chosen (principles \| standards \| host-skill \| AGENTS pointer \| ADR) | |
| Target **host** path agreed | |
| Checkability / strength (DO vs CONSIDER) if rule-like | |
| Trade-offs + catalog conflict / migration note | |
| Pulls weight (not ease-driven minimalism) | |

**Refuse / park** (do not propose): no locator; grade U; pattern name only; vibes; wrong-place complexity; vague success; auto-accept implication; conflict with no migration.

## 2 — Candidate atom (qualified only)

```text
Candidate id:
Pain / recurring problem:
Evidence + locator:
Label + grade:
Change type: principles | standards | host-skill | AGENTS-pointer | ADR
Target host path:
Checkability / strength:
Trade-offs / catalog conflict:
Corroboration / recurrence note:
Status: proposed | parked | refused
Refuse/park reason (if any):
```

## 3 — Human accept (last gate)

- [ ] Human reviewed **qualified** proposals only  
- [ ] Accepted → invoke author path (below); Rejected → leave parked/refused  
- [ ] **Never** silent SoT write from this skill  

## 4 — Author compose (after accept)

| Change type | Next skill |
|-------------|------------|
| principles / standards | `author-standards` |
| AGENTS pointer / house ops | `author-agents-md` |
| Host skill / rule / hook | `author-cursor-surfaces` (host path) |
| Architecture / process lock | `research-draft-adr` |

Do **not** paste those skills’ spines here — announce **Using `<skill>`** and hand off.

## 5 — Stop

```text
Do: quality gate → proposed → human → author-*
Do not: auto-accept; Toolbelt plugin skill rewrite; Memories-as-law;
      always-on harvest; stop-followup SoT rewrite; vibes-as-proposal
```
