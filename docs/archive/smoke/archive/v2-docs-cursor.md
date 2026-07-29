---
title: "Docs research: Cursor Skills / Rules (smoke v2 — patched harness)"
status: draft
created: 2026-07-28
updated: 2026-07-28
product: "Cursor IDE"
installed_version: "in_use (build GAP)"
docs_version_or_url: "https://cursor.com/docs/skills.md ; https://cursor.com/docs/rules.md ; https://cursor.com/llms.txt"
aligned_with: docs/research/reports/theme-3-researching-documentation.md
protocol_steps: D0-D14
skill: docs-research
smoke: v2
harness_announce: "Using docs-research"
literal_copy: true
---

# Documentation research checklist

**Using `docs-research`.**  
Copied from skill `references/d0-d14-checklist.md`, then filled.  
Corroboration: GreyMatter `.cursor/skills` + `.cursor/rules` after patches.

## D0 — Identity & version pin

| Field | Value |
|-------|-------|
| Product / package / homepage | Cursor — https://cursor.com |
| Installed version (E0) | `in_use` this Agent session on `d:\GreyMatter`; **build GAP** |
| Docs version / URL slug (E0) | Live docs (skills/rules/llms.txt) — prior fetch 2026-07-28; atoms rechecked via local files |
| Version skew? | unknown (build GAP) |

## D1 — Entry indexes

- [x] Official docs (skills.md, rules.md)
- [x] `/llms.txt` (index; malformed changelog URL known from v1)
- [x] Local skill/rule trees as corroboration targets

## D2 — Diátaxis classify

| URL | Type | Trust |
|-----|------|-------|
| docs/skills.md | reference | high for layout/frontmatter |
| docs/rules.md | reference | high for `.mdc` |
| llms.txt | index | index only |

## D3 — Contracts

- [x] Skill frontmatter `name`+`description`; optional `disable-model-invocation`
- [x] Rules `.mdc` + alwaysApply/description
- [ ] OpenAPI — **N/A** (prose product docs; patched skill)

## D4 — Deltas

- [ ] Changelog deep fetch — GAP (waived smoke v2)

## D5 — Official limitations

- [ ] Skills known-issues page — GAP
- Rules FAQ exists for non-application

## D6 — Canonicalization

Prefer cursor.com/docs over mirrors.

## D7 — E3 limitation scan

- [x] Waived deep forum scan (smoke) — reason: harness retest focus

## D8 — E3→E0/E1 corroboration

| Lead | E0 check | Result |
|------|----------|--------|
| `.cursor/skills/` layout | `_e0_check_v2.py` | MATCH |
| name==folder | same | MATCH |
| dmi on author/draft | same | MATCH |
| `.mdc` rules incl. coexistence | same | MATCH (4 rules) |
| Patch strings in skills | same | MATCH |

## D9 — Anti-pattern self-check

- [x] Not inventing build number
- [x] Not locking on E3
- [x] OpenAPI tools marked N/A

## D10 — Docs as hypotheses

DOC_CLAIM: skills discoverable from `.cursor/skills/`; progressive `references/` OK.

## D11 — Atoms

Paths, frontmatter fields, rule extensions — listed in D8.

## D12 — Corroborate & execute

| Atom | Check | Result |
|------|-------|--------|
| Skills/rules exist post-patch | Python path-exists | MATCH |
| OpenAPI Spectral | schema in scope? | **N/A** |
| Docs site linkcheck | — | GAP (waived) |

## D13 — Conflict log

| Doc | Observation | Winner | Grades |
|-----|-------------|--------|--------|
| llms.txt malformed changelog URL (v1) | not re-fetched v2 | unresolved / doc typo | E1 prior |
| None on core skill contracts | local MATCH | agree | E0+E1 |

## D14 — Freshness

- [x] Local harness files are current SoT for “did patches land”
- [ ] App build still GAP

## Stop conditions

- [x] D0 with `in_use` + build GAP (patched form)
- [x] Reference used for skill/rule claims
- [x] D7 waived with reason
- [x] No design locks
- [x] Graded findings in checklist (either-OK)

### Graded findings

1. **FACT [E0]:** Patched skills/rules present; coexistence rule file exists.  
2. **FACT [E0]:** D0 `in_use` + build GAP form usable without inventing Cursor build.  
3. **FACT [E0]:** OpenAPI tool step correctly N/A for Cursor prose docs.  
4. **INFERENCE [E4]:** Patched `docs-research` reduces false OpenAPI pressure and clarifies hosted-product pin.
