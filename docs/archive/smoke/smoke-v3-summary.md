---
title: "Smoke v3 — previously untested surfaces"
status: draft
created: 2026-07-28
---

# Smoke v3 coverage report

## Subjects chosen

| Surface | Trigger subject | Why it fires the skill |
|---------|-----------------|------------------------|
| `research-protocol` | Synthesize harness elevation + smoke v1/v2 | Needs Method envelope, conflict log, graded findings |
| `codebase-recon` + `research-before-write` | GreyMatter workspace before writing `AGENTS.md` | Unfamiliar-enough empty product surface; gate before implementation-like write |
| `author-agents-md` | **No root `AGENTS.md` existed** | Exact skill purpose; E0 proved MISS then write |
| `draft-adr` | Soft vs hard explore-before-edit | Decision already researched; ADR skill requires post-research record |
| Coexistence | Dual-plugin environment (Superpowers installed) | Announce GreyMatter skill; note MUST-invoke tension |
| Intelligent-rule **auto-fire** | — | **Still GAP** (no telemetry) |

## Process compliance

| Discipline | Done? |
|------------|-------|
| Announce Using skill | yes (recon, research-protocol, author-agents-md, draft-adr) |
| Literal template copy where required | research-note + adr copied; AGENTS authored from skeleton fields |
| No invented build/test commands | yes — `GAP` in AGENTS.md |
| draft/proposed ≠ law | ADR `proposed`; research note `draft` |
| research-before-write before AGENTS.md | yes — `v3-recon-greymatter.md` first |

## Gaps found this run (new harness issues?)

| Item | Severity | Notes |
|------|----------|-------|
| Intelligent-rule auto-fire still unproven | known GAP | Manual path exercised instead |
| `author-agents-md` workcopy (`v3-agents-md-workcopy.md`) unused after skeleton read | low | Wrote root `AGENTS.md` directly from skeleton — slight literal-copy skip vs recon/docs skills |
| Coexistence not a hard conflict test | low | Documented only; Superpowers not force-invoked |
| No failure that invented APIs | — | Good |

## Verdict

| Surface | Result |
|---------|--------|
| `research-protocol` | **Pass** — full Method note + conflict YAML |
| `author-agents-md` | **Pass** — root `AGENTS.md` with GAP commands |
| `draft-adr` | **Pass** — `docs/adr/0001-soft-explore-before-edit.md` proposed |
| `research-before-write` path | **Pass** (manual exercise) |
| Coexistence | **Partial pass** (applied as note, not stress test) |
| Auto-fire proof | **Still GAP** |

## Artifacts

- Working notes under `archive/` (`v3-*.md`)
- `AGENTS.md` (repo root)
- `docs/adr/0001-soft-explore-before-edit.md`
- This report
