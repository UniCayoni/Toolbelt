---
title: "Toolbelt closeout profile (host-owned)"
status: active
aligned_with: docs/research/reports/theme-15-closeout-readiness.md
created: 2026-08-02
updated: 2026-08-02
---

# Closeout profile

Authority: Theme 15 accepted. Used by skill **`implementation-closeout`**.  
**Host-owned** — copy to e.g. `docs/closeout/closeout-profile.md` (path override OK).  
This file defines **readiness**, not git/PR/merge **ceremony**.

## Header

```text
Host / product:
Profile version / date:
Owner (human):
Applies to: feature | bugfix | docs | method/skill change | other:
Ceremony note (optional — human/host only): e.g. follow CONTRIBUTING / open PR when ready
```

## Criteria (edit for this host)

For each row: **status** = `ready` | `blocked` | `waived` | `n/a`.  
**Evidence** = path, command+signal, accept record, or run log — or reason for N/A/waiver.  
Do **not** invent greens.

| ID | Criterion | Required? | Status | Evidence / reason |
|----|-----------|-----------|--------|-------------------|
| C1 | Design accepted or documented Design skip | yes* | | |
| C2 | Plan Meta `ready` (plan-verify) or trivial plan skip | yes* | | |
| C3 | Implementation Verify / execute-verify for non-trivial work | yes* | | |
| C4 | Draft/proposed artifacts not treated as SoT for merge | yes | | |
| C5 | Host tests / checks the host cares about | host | | |
| C6 | Human reviewed the diff (esp. agent-authored) | host | | |
| C7 | Docs / CHANGELOG updated if host requires | host | | |
| C8 | Secrets / destructive ops handled per host rules | yes | | |
| C9 | Host standards/principles profiles respected when present (or N/A if none) | host | | |
| C10 | *(add host-specific)* | | | |

\*Toolbelt defaults — mark `n/a` with reason when intelligent exception applies (e.g. trivial one-file).

## Check summary

```text
Overall: ready | blocked | waived-with-notes
Gaps (blocked IDs):
Waivers (who / why / date):
Next: hand human for host ceremony — do not auto-merge from this profile
```
