---
title: "Docs research: {product or package}"
status: draft
created: YYYY-MM-DD
product: ""
installed_version: ""
docs_version_or_url: ""
aligned_with: docs/research/reports/theme-3-researching-documentation.md
protocol_steps: D0-D14
---

# Documentation research checklist

Use when relying on **public / third-party / project documentation**.  
Authority: `docs/research/PROTOCOL.md` + Theme 3 report §2 (D0–D14).  
Related: Theme 1 code recon · Theme 2 `claim-citation.md`.

**Rule:** Official docs are E1 hypotheses until corroborated. Forums/issues are E3 **discovery** only — no design locks on E3 alone.

## D0 — Identity & version pin

| Field | Value |
|-------|-------|
| Product / package / homepage |  |
| Installed version (E0) |  # packages: semver/tag. Hosted/IDE: `in_use` + build if known else GAP |
| Docs version / URL slug (E0) |  |
| Version skew? | yes/no/unknown |

Do not assume `latest` == installed. Prefer matching `stable` / tag.  
For hosted products/IDEs (e.g. Cursor): record `in_use` + workspace corroboration; leave build `GAP` rather than inventing.

## D1 — Entry indexes

- [ ] Official docs home
- [ ] Optional `/llms.txt` (+ `.md` mirrors) — **index only**
- [ ] Repo `docs/` / tagged release docs
- URLs:

## D2 — Diátaxis classify

| URL | Type | Trust for full API truth |
|-----|------|--------------------------|
|  | tutorial / how-to / reference / explanation | high only for **reference** (+ contracts) |

Default trust for behavior: reference+contracts > how-to > explanation > tutorial.

## D3 — Contracts for API / behavioral truth

- [ ] OpenAPI / IDL / generated or hand **reference** consulted
- [ ] Tutorials/quickstarts treated as non-exhaustive
- [ ] Note RFC 2119/8174-style MUST/SHOULD/MAY if present — capitalize + BCP 14 adoption = higher normative intent (still E1 until E0); lowercase tutorial “must” = guidance only
- Claims (use `claim-citation.md`):

## D4 — Deltas / upgrades

- [ ] CHANGELOG / Releases / NEWS for span
- [ ] Deprecated → Removed / Breaking noted
- Prefer changelog over marketing notes / raw git log.

## D5 — Official limitation surfaces (E1 first)

- [ ] Known issues / Limitations / Compatibility / Status
- [ ] Migration / breaking-changes guide
- If absent: `GAP`

## D6 — Canonicalization

- Prefer VCS-co-located, owned, PR-reviewed docs over orphaned wikis.
- Notes on duplicates / freshness:

## D7 — E3 limitation scan (discovery)

- [ ] Issues: bug + docs labels; `reason:"not planned"`; high-signal threads
- [ ] Discussions (if any)
- [ ] Vendor forums / SO (leads only)
- Capture URL, date, versions, maintainer stance → `CLAIM` [E3]

## D8 — E3→E0/E1 corroboration

| Lead | Version match | Changelog/release | Reproduce E0 | Source/tests | Class | Outcome |
|------|---------------|-------------------|--------------|--------------|-------|---------|
|  |  |  |  |  | product bug \| docs drift \| skew \| wontfix \| user error | FACT or CLAIM+OPEN |

Only E3 left → **do not lock design**.

## D9 — Anti-pattern self-check

- [ ] Not one unreproduced angry report
- [ ] Not ignoring “not planned”
- [ ] Not conflating docs bug vs product bug
- [ ] Not citing fixed issues against wrong install
- [ ] Not preferring forum over changelog when both exist
- [ ] Not treating “tracking” as shipped

## D10 — Docs as hypotheses (beacons)

Ingest README / architecture / AGENTS.md / how-to+reference as `DOC_CLAIM` — not ground truth.

## D11 — Extract checkable atoms

Paths, symbols, CLI, env vars, routes, version pins, code fences:

## D12 — Corroborate & execute

| Atom | Check | Result |
|------|-------|--------|
|  | grep/run/schema | MATCH \| MISSING \| RENAMED \| AMBIGUOUS |

Prefer executable checks when available ([Write the Docs — Testing your documentation](https://www.writethedocs.org/guide/tools/testing/)):

1. Docs **build** (exit 0; optional Sphinx nitpicky / Jekyll strict)
2. **Linkcheck** (Sphinx `linkcheck`, HTMLProofer, …)
3. Examples / **doctest** / smoke commands from fences marked executable
4. API **contracts** — **only if OpenAPI/GraphQL schema is in scope:** Spectral (lint) → Schemathesis / similar (runtime). Else mark **N/A** (prose/HTML product docs).
5. Optional prose lint (Vale)

**E0 tip (Windows):** Prefer path-exists / small Python checks when verifying local doc/code artifacts.

## D13 — Resolve authority & record conflict

| Doc locator | Doc quote | Code/schema/cmd | Observation | Winner | Grades |
|-------------|-----------|-----------------|-------------|--------|--------|
|  |  |  |  | code \| schema \| doc \| unresolved | E0/E1… |

On conflict for current behavior: prefer **E0**; keep E1 cite as `CONTRADICTED_BY_E0` / `STALE`. Never invent; cite both sides.  
Full field set: `templates/claim-citation.md` → Conflict log fields.

## D14 — Freshness / RAG hygiene (if retrieving)

- [ ] Versioned/timestamped sources preferred
- [ ] Stale KB filtered/removed; embeddings cascaded if applicable
- [ ] Sources returned with answers
- Retrieval↔model contradiction → re-run D12–D13, do not silent-merge

## Stop conditions

- [ ] D0 version pin recorded
- [ ] Reference/contracts used for any API claims relied on
- [ ] Limitation path done (D5–D9) or waived with reason
- [ ] Conflicts recorded with grades
- [ ] No design lock on uncorroborated E3
- [ ] Durable findings: graded section in this checklist **or** `research-note.md` / `research-protocol` if multi-pass
