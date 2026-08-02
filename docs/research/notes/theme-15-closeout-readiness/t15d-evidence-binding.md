---
title: "T15D — Evidence binding to Toolbelt artifacts"
status: draft
theme: theme-15-closeout-readiness
track: T15D
created: 2026-08-02
updated: 2026-08-02
authors: [gatherer]
---

# T15D — Evidence binding

## 1. Scope

- Question: How should closeout readiness bind to Toolbelt evidence without inventing passes?
- Out of scope: New verify grade systems

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-08-02 |
| Tools | Local skills/PROTOCOL knowledge + T15C |
| Depth | normal |

## 3. Findings

- `FACT` [E0] Toolbelt already produces checkable stage evidence: design human accept; plan Meta `ready` after plan-verify; execute Done-when/Verify; execute-verify; debug cycles; research accept; draft≠SoT. [E0: Themes 5–12 skills/reports]
- `INFERENCE` [E4] Closeout checklist items should require a **locator** (path, command+output note, run log, accept record) or explicit **N/A + reason** — same spirit as cite-or-omit / frontier “faithfully reported.” Premises: PROTOCOL; T15C frontier DoD #6.
- `INFERENCE` [E4] Mapping (proposed, not law):

| Typical slot | Toolbelt / host evidence |
|--------------|--------------------------|
| Design accepted | Design note/ADR status accepted or documented skip |
| Plan ready | Meta `ready` + plan-verify verdict |
| Implementation verified | Task Verify signals / execute-verify |
| Research accepted (if method change) | Report `status: accepted` |
| Draft not treated as SoT | No merge of draft-as-law (CONTRIBUTING) |
| Host tests / CI | Host command output or CI URL (host-owned) |
| Human reviewed diff | Human attestation (CONTRIBUTING culture) |
| Ceremony (PR opened) | **Out of readiness skill** — handoff note only |

- `INFERENCE` [E4] Verdict vocabulary lean: `ready` | `blocked` (missing evidence / intent-gap) | `waived` (documented host exception) | `n/a` (slot not in profile). Aligns with plan/execute status vocab without owning merge.
- `GAP` No existing template fields for host closeout profile — design later.
- `OPEN` Whether smoke Theme-11-style claim cards count as evidence for Toolbelt-self closeouts (likely yes as E0 run logs).

## 4. Next

T15F shape lean.
