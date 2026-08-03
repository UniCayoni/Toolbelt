---
title: "T19A — Local baseline (standards apply)"
status: draft
theme: theme-19-standards-apply
created: 2026-08-03
depth: normal
authors: [research-gatherer]
aligned_with:
  - docs/research/notes/theme-19-standards-apply/campaign-brief.md
---

# T19A — Local baseline

**Using `research-protocol`.** Depth: **normal**. Labels: FACT | GAP | OPEN.  
E0 via coordinator + [T19A baseline](dd5cf9f5-47b1-429b-bb55-038a40a35fca).

## 1. Scope

- **Question:** What does Theme 16 bind + Toolbelt routers/rules do today for standards *apply*? Gaps vs selective-load intent?
- **Out of scope:** Elevating surfaces; writing host standards content.

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-08-03 |
| Tools | Read/Grep; explore subagent E0 |
| Depth | normal |
| Not searched | External RAG/GitHub (deep tracks) |

## 3. Findings

- `FACT` [E0] Theme 16 **D10**: Plan/Execute/Closeout load profiles when present, skip when absent; AGENTS short pointer. [E0: `docs/research/reports/theme-16-host-standards.md`]
- `FACT` [E0] Theme 16 **D12**: no always-on standards rule; no auto-promote derive. [E0: same]
- `FACT` [E0] `author-standards` has `bind-check`; out-of-scope includes always-on standards rule. [E0: `skills/author-standards/SKILL.md`]
- `FACT` [E0] Handoffs to `author-standards` from plan, execute, closeout, happy-path, impl-router, author-agents-md, recon (derive). None implement module resolve. [E0: respective `skills/*/SKILL.md`]
- `FACT` [E0] Always-on rules: `draft-is-not-sot`, `research-protocol-grades` (`alwaysApply: true`); `research-before-write` (`false`). None mention standards profiles. [E0: `rules/*.mdc`]
- `FACT` [E0] Pocket routers (`implementation-router`, `debug-router`, de facto `research-scope` / `design-process`) do not resolve standards modules; impl-router only hands off to `author-standards`. [E0: router SKILL.md files; Theme 14 report]
- `FACT` [E0] Templates: single `principles-profile.md` + single `standards-profile.md` (optional dual-era section); no catalog/index template. [E0: `docs/templates/`]
- `FACT` [E0] No host `docs/standards/` tree in Toolbelt repo yet. [E0: glob 2026-08-03]
- `GAP` No `standards-router` skill; no ambient standards apply rule; no module catalog. [E0: skills/templates/rules absence]
- `OPEN` Skill id / D12 amend — T19I.

## 4. Implications for Theme 19

Baseline apply is **soft consumer bind** on three Implementation-adjacent skills + authoring skill — not selective module routing, not ambient resolve. Session candidate model is a greenfield *apply* layer on top of Theme 16 feedstock.
