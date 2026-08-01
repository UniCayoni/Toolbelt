---
name: docs-research
description: >-
  Research product or third-party documentation with Toolbelt D0–D14: version
  pin, Diátaxis classify, contracts, limitation scan (E3 discovery), and
  docs↔code corroboration. Use when verifying API/behavior from docs, hunting
  known issues, comparing docs to installed code, reading Cursor/official docs,
  pinning versions, or OpenAPI/reference contracts.
---

# Documentation research

Announce once: **Using `docs-research`**.

## When to use

- Relying on official or third-party docs for APIs, flags, or behavior
- Hunting limitations / known issues / drift
- Verifying docs against installed code or a product **in use**

## Note output path

Prefer (in order):

1. Host workspace `docs/research/notes/` if that directory exists
2. A path the user specified
3. Ask before writing

## Instructions

1. Read `references/d0-d14-checklist.md` **when** starting docs research, then **copy** it into a new note under the note output path (do not overwrite the reference).
2. **D0 first** — pin identity:
   - **Packages / libraries:** installed version (E0) + docs version/URL.
   - **Hosted products / IDEs (e.g. Cursor):** `status: in_use` + session/workspace corroboration; `build` or app version if obtainable, else **`GAP`** (do not invent).
   - Never assume `latest` == installed.
3. **D2–D3:** Classify (tutorial / how-to / reference / explanation). Prefer reference + contracts for behavioral truth. RFC 2119/8174 capitalized MUST/SHOULD = higher normative *intent* — still corroborate (D12).
4. **D5–D9:** Official limitations first; E3 scan as discovery only. Corroborate before design locks. Light/waived D7 OK for smokes if stated.
5. **D10–D13:** Docs as hypotheses; extract atoms; corroborate.
   - Executable checks when available: build → linkcheck → doctest/smoke.
   - **OpenAPI tools (Spectral / Schemathesis / Dredd) only when an OpenAPI/GraphQL schema is in scope** — skip for prose/HTML product docs (mark N/A).
   - Conflict: prefer E0 for current behavior; keep contradicted E1 as `CONTRADICTED_BY_E0` / `STALE`.
6. **D14:** If retrieving via RAG, prefer versioned sources; escalate contradictions to D12–D13.
7. **Persist (either OK):** graded findings in the checklist note, **or** full `research-protocol` note with Method block for multi-pass / merge.
8. **E0 on Windows:** Prefer path-exists / small Python checks over brittle shell one-liners when verifying local artifacts.

**Depth:** Default **normal** (this checklist). If the user asks for deep/theme docs research across many surfaces, escalate to skill **`research-protocol`** depth=`deep` (parallel gatherers + diminishing-returns stop) — see `research-protocol` / `research-depth-modes`. Do not fleet-gather for ordinary API lookups.

Re-open `references/d0-d14-checklist.md` only when recovering missing D-steps; keep work in the copied note.

## Hard constraints

- Official docs = E1 hypotheses until corroborated
- Never invent APIs, endpoints, or version pins
- Cite both sides of conflicts

## Handoffs

| Need | Use |
|------|-----|
| Expand / tracks before docs research | `research-scope` |
| Full Method-envelope note / deep campaign | `research-protocol` |
| Code corroboration | `codebase-recon` |
| Decision lock | `draft-adr` |
| Design / plan after facts | `design-process` / `implementation-plan` |

## References

- Read `references/d0-d14-checklist.md` **when** starting or recovering D0–D14 steps
- SoT: Toolbelt `docs/templates/documentation-research.md`
- Theme: Toolbelt `docs/research/reports/theme-3-researching-documentation.md`
