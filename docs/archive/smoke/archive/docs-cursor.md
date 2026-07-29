---
title: "Docs research: Cursor Skills / Rules (smoke trial)"
status: draft
created: 2026-07-28
product: "Cursor IDE"
installed_version: "in use this session (exact app build GAP)"
docs_version_or_url: "https://cursor.com/docs/skills.md ; https://cursor.com/docs/rules.md ; https://cursor.com/llms.txt"
aligned_with: docs/research/reports/theme-3-researching-documentation.md
protocol_steps: D0-D14
skill: docs-research
smoke: true
---

# Documentation research checklist — Cursor docs smoke

Authority: PROTOCOL + skill `docs-research`.  
Corroboration target: GreyMatter workspace `.cursor/skills` + `.cursor/rules` created this project + live Agent session.

**Rule:** Official docs are E1 hypotheses until corroborated.

## D0 — Identity & version pin

| Field | Value |
|-------|-------|
| Product / package / homepage | Cursor — https://cursor.com |
| Installed version (E0) | Cursor Agent session active on GreyMatter workspace; **exact desktop build number GAP** (not queried) |
| Docs version / URL slug (E0) | Live docs pages fetched 2026-07-28 |
| Version skew? | unknown for app build; docs treated as current published |

## D1 — Entry indexes

- [x] Official docs home / customize section
- [x] `/llms.txt` — https://cursor.com/llms.txt (index; broken-looking line `https://cursor.comhttps://cursor.com/changelog.md` noted)
- [x] Skills + Rules pages
- URLs: skills.md, rules.md, llms.txt, hooks.md (prior research), subagents.md (prior)

## D2 — Diátaxis classify

| URL | Type | Trust for full API truth |
|-----|------|--------------------------|
| cursor.com/docs/skills.md | reference (+ how-to fragments) | high for skill dirs/frontmatter |
| cursor.com/docs/rules.md | reference | high for `.mdc` / AGENTS.md behavior |
| cursor.com/llms.txt | index | index only |
| Built-in skill table on skills.md | reference list | medium — names change; corroborate in product |

## D3 — Contracts for API / behavioral truth

- [x] Skills frontmatter contract: `name`, `description` required; optional `paths`, `disable-model-invocation`, `metadata`
- [x] Rules: `.mdc` required under `.cursor/rules`; plain `.md` ignored
- [ ] OpenAPI — N/A
- RFC 2119: docs use descriptive MUST-like prose inconsistently; treated as guidance unless capitalized BCP14 — mostly lowercase instructional

## D4 — Deltas / upgrades

- [ ] Full changelog not deep-fetched this smoke (`llms.txt` changelog URL looks malformed) → **GAP**
- Skills page mentions `/migrate-to-skills` in Cursor **2.4**

## D5 — Official limitation surfaces (E1 first)

- [ ] Dedicated “known issues” for Skills — **GAP** on skills.md itself
- Rules FAQ covers “why isn’t my rule applied”

## D6 — Canonicalization

Prefer cursor.com/docs over help center mirrors; used docs.skills / docs.rules.

## D7 — E3 limitation scan (discovery)

Light pass only (smoke): not exhaustively searched Cursor forum.  
**OPEN:** dedicated Cursor forum/issue scan for skills discovery bugs.

## D8 — E3→E0/E1 corroboration

| Lead | Version match | Changelog | Reproduce E0 | Class | Outcome |
|------|---------------|-----------|--------------|-------|---------|
| Skills load from `.cursor/skills/` | n/a | — | 5 SKILL.md present under GreyMatter | docs MATCH | FACT |
| `name` must match folder | n/a | — | all 5 match | MATCH | FACT |
| `disable-model-invocation: true` for slash-like | n/a | — | author-agents-md + draft-adr have it | MATCH | FACT |
| Rules need `.mdc` | n/a | — | 3 `.mdc` rules exist | MATCH | FACT |
| Always vs intelligent via frontmatter | n/a | — | grades+draft alwaysApply true; research-before-write false+description | MATCH | FACT |

## D9 — Anti-pattern self-check

- [x] Not one unreproduced angry report
- [x] Not treating E3 as lock
- [x] Not inventing Cursor APIs

## D10 — Docs as hypotheses (beacons)

DOC_CLAIM: project skills live in `.cursor/skills/` with `SKILL.md` + optional `references/`.  
DOC_CLAIM: agent auto-applies skills unless `disable-model-invocation: true`.  
DOC_CLAIM: project rules are `.mdc` with alwaysApply/description/globs.

## D11 — Extract checkable atoms

1. Path `.cursor/skills/<name>/SKILL.md`
2. Frontmatter `name` == folder name
3. Optional `references/` directory
4. `.cursor/rules/*.mdc`
5. `/llms.txt` lists skills.md under customizing

## D12 — Corroborate & execute

| Atom | Check | Result |
|------|-------|--------|
| 5 GreyMatter skills exist | `python notes/smoke/_e0_check.py` | MATCH |
| name==folder | same script | MATCH |
| dmi on author/draft only | same | MATCH |
| 3 rules `.mdc` | same | MATCH |
| Superpowers plugin skills visible in session | agent_skills list / cache 14 skills | MATCH (plugin install) |
| Docs build/linkcheck | N/A third-party site | GAP |
| Exact Cursor app version | — | GAP |

## D13 — Resolve authority & record conflict

| Doc locator | Doc quote | Code/schema/cmd | Observation | Winner | Grades |
|-------------|-----------|-----------------|-------------|--------|--------|
| llms.txt | changelog URL `cursor.comhttps://cursor.com/changelog.md` | WebFetch llms.txt | malformed concatenation | unresolved (typo in index) | E1 doc buggy |
| skills.md discovery dirs | lists `.cursor/skills/` | GreyMatter paths | present | code/docs agree | E0+E1 |

No conflict on core skill/rule contracts for this smoke.

## D14 — Freshness / RAG hygiene

- [x] Fetched live docs 2026-07-28
- [ ] App build pin — GAP
- Sources returned with answers above

## Stop conditions

- [x] D0 recorded (with GAP on app build)
- [x] Reference used for skill/rule claims
- [x] Limitation path light; waived deep forum scan for smoke
- [x] Conflicts recorded (llms.txt typo)
- [x] No design lock on E3
- [x] Durable note = this file

---

## Key findings (graded)

1. **FACT [E1]+[E0]:** Cursor Skills docs’ directory layout and frontmatter rules match GreyMatter’s elevated skills (paths, name match, `references/`, `disable-model-invocation` on explicit skills).  
2. **FACT [E1]+[E0]:** Rules docs’ `.mdc` + alwaysApply/description behavior matches GreyMatter’s three rules.  
3. **FACT [E1]:** `/llms.txt` exists and indexes Skills/Rules; contains at least one malformed changelog URL.  
4. **GAP:** Exact Cursor desktop/CLI version for this machine not captured.  
5. **INFERENCE [E4]:** `docs-research` smoke **passed** — version-pin + atom corroboration against live install worked without inventing APIs.
