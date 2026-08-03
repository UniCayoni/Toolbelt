---
title: "Smoke T16 — principles profile (S1 fresh)"
status: draft
theme: theme-11-validation
surface_id: S1
mode: principles
aligned_with: docs/research/reports/theme-16-host-standards.md
created: 2026-08-02
note: Theme 11 smoke artifact only — not accepted SoT.
---

# Principles profile

Authority: Theme 16 accepted. Skill **`author-standards`** mode `principles`.  
**Host-owned** smoke draft for Toolbelt method continuity.  
**Altitude:** philosophy / tone / continuity — **not** checkable lint rules.

## Header

```text
Host / product: Toolbelt (smoke host)
Profile version / date: 0.1-smoke / 2026-08-02
Owner (human): Theme 11 validator (unaccepted)
Status: draft
Audience: humans + agents
```

## Intent

```text
What must survive team/agent churn and early↔late phases?
  Method continuity: evidence grades, draft≠law, host-owned feedstock, thin AGENTS pointers.
Tone: cautious / clarity-first — prefer absence (GAP/OPEN) over invention.
```

## Principles

| ID | Name | Guidance |
|----|------|----------|
| P1 | Draft is not law | Treat `draft` / `proposed` notes, plans, and ADRs as feedstock until a human accepts them. Do not lock architecture or multi-file implementation from drafts alone. |
| P2 | Cite or omit | Prefer labeled absence (GAP / OPEN) over invented APIs, URLs, or “industry ladders” presented as SoT. |
| P3 | Host owns standards | Toolbelt ships templates and skills; each host accepts its own principles/standards profiles. Do not impose Toolbelt-universal coding law on every host. |

## Conflict guidance (host)

```text
When principles conflict with each other: prefer explicit accepted ADRs/design over continuity vibes; escalate to human.
Suggested Toolbelt lean (host may adopt): design/ADR > principles > standards > inferred-from-code
Note: industry SoT for that ladder was not found — treat as host-authored method if accepted.
```

## Pointers (keep AGENTS.md thin)

```text
AGENTS.md / CLAUDE.md should link here — do not paste the full list into AGENTS.
Related standards profile path (if any): docs/research/notes/theme-11-validation/runs/artifacts/smoke-t16-standards-fresh.md
Related ADRs / design accept paths: (none for this smoke)
```

## Evolution

```text
How to amend (who accepts): human Theme 11 / host owner — smoke discard after validation.
Changelog / last change: 2026-08-02 S1 fresh smoke draft created.
```
