# Secondary research round — gap priorities

Date: 2026-07-27  
Purpose: Close or shrink **highest-impact** gaps from Themes 1–3 before elevating templates into Cursor skills.

## Selection rule

Prioritize gaps that (a) change template steps, (b) decide skill vs rule vs hook, or (c) were fetch-timeouts of known primaries. Defer catalog-style OPENs (ecosystem known-issues URLs) and product locks.

## P0 — must attempt this round

| ID | Gap | Why it matters | Status |
|----|-----|----------------|--------|
| T2-G6 / O5 | Codex AGENTS.md guide primary re-fetch (size/layering) | `agents-md-skeleton` budgets; skill progressive disclosure | **closed** |
| T3-G12 | Write the Docs “Testing your documentation” | Strengthens D12 executable-docs guidance | **closed** |
| T1-Yang | SWE-agent ACI paper arXiv:2405.15793 | Grounds S6–S9 tool surface in primary | **closed** (cite arXiv; local PDF removed) |
| T3-O2 | Conflict-log schema fields | Close as local convention for `documentation-research` + skill | **closed** [E4] |

## P1 — should attempt

| ID | Gap | Why | Status |
|----|-----|-----|--------|
| T2-O1 / O2 | Quote spans vs chunk_id; dual markdown+JSON claims | Research-note / claim-citation skill defaults | **closed** [E4] |
| T3-G8 | RFC 2119 in product docs as trust signal | Docs research D3 trust weighting | **closed** |
| T1-OPEN gate | Hard hook vs soft skill for explore-before-edit | Elevation map (skill vs hook) | **recommended** |
| T3-G15 | Schemathesis / Spectral (OpenAPI testing) | Optional D12 tools | **narrowed** |
| T2-G10 | W3C PROV-DM/PROV-O brief | Provenance vocabulary for notes | **closed** brief |

See `reports/secondary-refinement.md`.

## P2 — nice if time

| ID | Gap |
|----|-----|
| FAIR4RS Lamprecht 2020 | Research software FAIR primary |
| Cursor changelog / known issues | Cursor-specific D7 surface |
| T3-G9 | Sphinx/MkDocs/Docusaurus versioning UX |

## Explicitly deferred

- Per-ecosystem known-issues URL catalogs (T3-O1)
- GreyMatter `/llms.txt` product decision (T2-O3)
- Full PC primary corpus backfill (Littman/Letovsky) unless quick PDF
- GraphRAG Microsoft citation UX deep dive (T2-G2)
- IEEE 29148/1016 deep read (T2-G9)

## Outputs expected

1. `notes/secondary/` gap-closure notes  
2. `reports/secondary-refinement.md` — what closed, what remains, template diffs  
3. Updated templates where evidence supports  
4. `reports/cursor-elevation-map.md` — which artifacts → skills / rules / hooks / commands
