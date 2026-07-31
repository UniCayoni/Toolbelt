---
title: "Docs research: Cursor Debug Mode (R3 pocket smoke)"
status: draft
created: 2026-07-30
product: "Cursor IDE — Debug Mode"
installed_version: "in_use (workspace D:\\Toolbelt); build GAP"
docs_version_or_url: "https://cursor.com/docs/agent/debug-mode.md (accessed 2026-07-30)"
aligned_with: docs/research/reports/theme-3-researching-documentation.md
protocol_steps: D0-D14
smoke: theme-11-validation R3
---

# Documentation research checklist

Use when relying on **public / third-party / project documentation**.  
Authority: `docs/research/PROTOCOL.md` + Theme 3 report §2 (D0–D14).  
Related: Theme 1 code recon · Theme 2 `claim-citation.md`.

**Rule:** Official docs are E1 hypotheses until corroborated. Forums/issues are E3 **discovery** only — no design locks on E3 alone.

## D0 — Identity & version pin

| Field | Value |
|-------|-------|
| Product / package / homepage | Cursor IDE — Agent Debug Mode; https://cursor.com/docs |
| Installed version (E0) | `in_use` (session workspace `D:\Toolbelt`); Cursor app build **GAP** (not obtained this smoke) |
| Docs version / URL slug (E0) | https://cursor.com/docs/agent/debug-mode.md — fetched 2026-07-30 |
| Version skew? | unknown (build GAP) |

## D1 — Entry indexes

- [x] Official docs home — https://cursor.com/docs
- [x] Optional `/llms.txt` — linked from debug-mode page sitemap
- [ ] Repo `docs/` / tagged release docs — N/A for hosted product page
- URLs: https://cursor.com/docs/agent/debug-mode.md

## D2 — Diátaxis classify

| URL | Type | Trust for full API truth |
|-----|------|--------------------------|
| https://cursor.com/docs/agent/debug-mode.md | how-to / explanation (product behavior) | medium — behavioral overview, not wire-level reference |

## D3 — Contracts for API / behavioral truth

- [ ] OpenAPI / IDL / generated or hand **reference** consulted — **N/A** (prose product docs; no OpenAPI for Debug Mode)
- [x] Tutorials/quickstarts treated as non-exhaustive
- [ ] Note RFC 2119/8174-style MUST/SHOULD/MAY if present — none observed on page
- Claims: see Findings below

## D4 — Deltas / upgrades

- [ ] CHANGELOG / Releases / NEWS for span — light/waived for pocket smoke
- Blog cross-ref (not primary for this answer): https://cursor.com/blog/debug-mode

## D5 — Official limitation surfaces (E1 first)

- [x] Known issues / Limitations — page states when Debug Mode works best; no wire-schema section
- If absent for private API: `GAP` — see Findings

## D6 — Canonicalization

- Prefer VCS-co-located, owned, PR-reviewed docs over orphaned wikis.
- Notes: Official `cursor.com/docs/agent/debug-mode.md` used as primary E1 source.

## D7 — E3 limitation scan (discovery)

- Light/waived for pocket smoke (stated). Community reverse-engineering of Cursor APIs exists but is E3 only and **not** used for wire-schema claims.

## D8 — E3→E0/E1 corroboration

| Lead | Version match | Changelog/release | Reproduce E0 | Source/tests | Class | Outcome |
|------|---------------|-------------------|--------------|--------------|-------|---------|
| (waived) | — | — | — | — | — | no design lock |

## D9 — Anti-pattern self-check

- [x] Not inventing private debug-server wire schema from memory or E3
- [x] Not treating blog as higher than docs for this smoke
- [x] Not locking design on uncorroborated E3

## D10 — Docs as hypotheses (beacons)

`DOC_CLAIM` [E1]: Debug Mode uses hypotheses → instrumentation → human reproduce → log analysis → targeted fix → cleanup (from official page).

## D11 — Extract checkable atoms

- Mode name: Debug Mode
- Instrumentation target: “local debug server running in a Cursor extension”
- Mode switch: mode picker dropdown; Shift+Tab
- Private wire schema: **not published** on fetched page → GAP

## D12 — Corroborate & execute

| Atom | Check | Result |
|------|-------|--------|
| Debug Mode behavior paragraph | WebFetch official URL 2026-07-30 | MATCH (page content retrieved) |
| Private debug-server wire schema | Search official docs page for schema/protocol fields | MISSING → GAP |
| OpenAPI tools | N/A for prose HTML product docs | N/A |

## D13 — Resolve authority & record conflict

| Doc locator | Doc quote | Code/schema/cmd | Observation | Winner | Grades |
|-------------|-----------|-----------------|-------------|--------|--------|
| debug-mode.md §How it works | “send data to a local debug server running in a Cursor extension” | no public schema fetched | existence of local debug server mentioned; wire format unpublished | doc (existence only); schema unresolved | E1 / GAP |

## D14 — Freshness / RAG hygiene (if retrieving)

- [x] Versioned/timestamped sources preferred — URL + access date 2026-07-30
- [x] Sources returned with answers
- RAG not used this pass

## Stop conditions

- [x] D0 version pin recorded
- [x] Reference/contracts used for any API claims relied on (behavioral prose; wire schema GAP)
- [x] Limitation path done (D5–D9) or waived with reason (D7 light/waived)
- [x] Conflicts recorded with grades
- [x] No design lock on uncorroborated E3
- [x] Durable findings below

## Findings (smoke answers)

### What Cursor Debug Mode does (one paragraph) — `CLAIM` [E1]

Debug Mode helps find root causes and fix tricky bugs that are hard to reproduce or understand: instead of immediately writing code, the agent explores relevant files, generates multiple hypotheses, adds log instrumentation that sends data to a local debug server in a Cursor extension, asks you to reproduce the bug to capture real runtime behavior, analyzes those logs to identify the root cause, makes a focused fix, and after you verify, removes the instrumentation.

**Source accessed 2026-07-30:** https://cursor.com/docs/agent/debug-mode.md

### Private debug-server wire schema — `GAP` [E1 absence]

**GAP:** Official Cursor docs fetched today mention a “local debug server running in a Cursor extension” but do **not** publish a private debug-server wire schema (message framing, fields, endpoints, or IDL). No invention; do not treat community reverse-engineering as SoT.
