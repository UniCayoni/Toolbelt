---
status: proposed
date: 2026-07-28
---

# ADR 0001: Soft explore-before-edit for GreyMatter research harness

> Template grounded in Nygard ADR + MADR (Theme 2).  
> **Using `draft-adr`.** Copied from skill reference, then filled.  
> Do not treat `proposed` as project law.

## Status

proposed

## Context

GreyMatter needs agents to research code/docs before locking design or editing product code. Cursor Skills/Rules are soft (prompt/relevance); Hooks can hard-deny tool use [E1: Cursor skills/hooks docs via elevation research]. Vendors do not mandate explore-before-edit by default [E0: Theme 1 report]. Smoke v1–v2 showed soft skills work for research quality; hard hooks deferred. Superpowers-style “MUST invoke skill before any response” can conflict with GreyMatter soft research skills [E0: coexistence rule + smoke notes].

Forces: evidence quality vs agent friction; soft guidance vs deterministic enforcement; multi-plugin coexistence.

Research: `docs/research/notes/secondary/sec-elevation-gates-skills.md`; `docs/research/notes/smoke/archive/v3-research-note-harness.md`; Theme 1 implications.

## Decision

We will use **soft** explore-before-edit: skills (`codebase-recon`) + thin rules (`research-before-write`, evidence grades, draft≠SoT). We will **not** enable hard `preToolUse` write denies until soft guidance fails in observed E0 trials. Research notes under `docs/research/` are allowed during recon and are not treated as implementation writes.

## Consequences

- Positive: lower friction; aligns with Cursor’s soft skill/rule model; smoke-tested path exists
- Negative: agents may skip recon; no deterministic guarantee
- Neutral: hooks remain available as a future escalation; coexistence with Superpowers remains advisory

## Confirmation (optional)

- Future smokes / real tasks: non-trivial code edits preceded by recon note or explicit human waive
- If repeated skip observed (E0), reconsider opt-in hook

## Notes / links

- Research: `docs/research/notes/smoke/archive/v3-research-note-harness.md`
- Elevation: `docs/research/reports/cursor-elevation-map.md`
- Rule: `.cursor/rules/research-before-write.mdc`
- Related ADRs: none yet
