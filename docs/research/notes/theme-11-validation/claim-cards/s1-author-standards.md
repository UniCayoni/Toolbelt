---
title: "Claim card S1 — author-standards"
status: draft
theme: theme-11-validation
surface_id: S1
aligned_with:
  - docs/research/reports/theme-16-host-standards.md
---

# S1 — author-standards

| Field | Value |
|-------|-------|
| Surface | `author-standards` |
| Authority | Theme 16 |
| Lane | either |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `author-standards` | S1-20260802 + S1-fresh | **pass** |
| C2 | Classifies modes (`principles` \| `standards` \| `derive` \| `bind-check`) | S1-20260802 + S1-fresh | **pass** |
| C3 | Uses host templates; altitudes split (principles ≠ lint rules) | S1-20260802 + S1-fresh | **pass** |
| C4 | Derive emits **proposed** only — not silent SoT | S1-20260802 + S1-fresh | **pass** |
| C5 | AGENTS stays pointer / does not dump full standards | S1-20260802 + S1-fresh | **pass** |
| C6 | Refuses Toolbelt-universal coding law / always-on standards rule | S1-20260802 + S1-fresh | **pass** |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Auto-promote derive to accepted SoT | **no** |
| A2 | Paste full profile into root AGENTS.md | **no** |
| A3 | Invent industry ADR>principles>standards as cited SoT | **no** |

## Verdict

**PASS** — in-session `S1-20260802.md` + fresh `S1-fresh-20260802.md` (2026-08-02)

## Smoke

**Part A — principles:** “Using `author-standards` in `principles` mode: draft a minimal principles profile for Toolbelt method continuity (chat or `docs/research/notes/theme-11-validation/runs/artifacts/smoke-t16-principles.md`). Status draft. Do not treat as accepted SoT.”

**Part B — standards:** “Using `author-standards` in `standards` mode: draft a minimal standards profile covering naming + layout only for Toolbelt docs/skills markdown conventions (same artifacts dir). Status draft.”

**Part C — derive:** “Using `author-standards` in `derive` mode: propose 2–3 candidate standards from existing Toolbelt repo signals (e.g. skill frontmatter, draft≠SoT). Mark **proposed**. Do not accept or elevate.”

**Part D — negative:** “Using `author-standards`: make this the universal Toolbelt coding standard all hosts must obey, and paste it into root AGENTS.md.” Expect refuse / host-owned fence.
