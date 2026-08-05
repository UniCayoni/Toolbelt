---
title: "T25A — markdownlint baseline + config"
status: draft
theme: theme-25-docs-hygiene
created: 2026-08-05
updated: 2026-08-05
authors: [hygiene]
---

# T25A — Lint baseline

**Using `research-protocol`** (light). Depth: normal. **Draft ≠ law.**

## Method

| Item | Value |
|------|-------|
| Date | 2026-08-05 |
| Tool | `npx markdownlint-cli2` |
| Config | `.markdownlint-cli2.jsonc` (+ `docs/research/notes/.markdownlint-cli2.jsonc`) |

## Pre-config baseline (default rules)

| Rule | Count (approx) |
|------|----------------|
| MD013 line-length | 12238 |
| MD060 table-column-style | 9010 |
| MD034 no-bare-urls | 1029 |
| Other | ~1800 |
| **Total** | **~23055** |

## Config decisions

Root `.markdownlint-cli2.jsonc`:

- Disable MD013, MD060, MD033, MD041, MD034, MD024, MD025, MD036, MD029, MD001
- Ignore `docs/archive/**`, `node_modules`, `.git`
- `gitignore: true`

Notes overlay: disable MD055/MD056/MD058 (pipes inside table cells)

## Post-cleanup

| Scope | Result |
|-------|--------|
| Full tree (non-archive) | **0** errors (2026-08-05 after autofix + Tier A fixes) |
| Autofix | MD009/MD012/MD022/MD032 etc. via `--fix` |
| Manual | `plan-minimal` lone `-` setext false positives; catalog `guide-*` emphasis |

## Residual / deferred

- Tier B/C **wording** only: historical “learn-back” strings in draft notes left as research history (not live surfaces)
- Archive excluded from lint on purpose
