# Research templates (agent-reusable)

Status: aligned to integrated reports (Themes 1–3) + Theme 4 accepted (2026-07-29); SoT for Toolbelt plugin  
Authority: `docs/PROTOCOL.md`  
Reports:
- Theme 1: `docs/research/reports/theme-1-codebase-research-for-agents.md`
- Theme 2: `docs/research/reports/theme-2-agent-usable-documentation.md`
- Theme 3: `docs/research/reports/theme-3-researching-documentation.md`
- Theme 4: `docs/research/reports/theme-4-cursor-plugin-components.md` (**accepted** — plugin packaging / skills+rules policy)

## When agents must use these

| Situation | Template |
|-----------|----------|
| Any research / evidence-gathering write-up | `research-note.md` |
| Choosing normal vs deep research campaigns | `research-depth-modes.md` |
| Exploring a codebase/workspace before docs or code changes | `codebase-reconnaissance.md` (Theme 1 **S0–S18**; skill `research-codebase-recon`) |
| Emitting / checking claims with citations | `claim-citation.md` |
| Choosing which doc format to create | `doc-layers.md` |
| Researching public/third-party documentation | `documentation-research.md` (Theme 3 **D0–D14**) |
| Portable repo agent instructions | `agents-md-skeleton.md` |
| Recording a design decision (after research) | `adr-minimal.md` |
| Author/compose Cursor skills, rules, commands, hooks | `author-cursor-surfaces.md` |
| Host principles / standards profiles | `principles-profile.md`, `standards-profile.md`, `author-standards-checklist.md` |
| Standards apply (catalog / module / router) | `standards-catalog.md`, `standards-module.md`, `guide-standards.md` |
| Global meta-guide checklist | `guide-meta.md` |
| Debug pocket router checklist | `guide-debug.md` |

## Rules

1. Copy a template into a new file under the **host project** note path; do not edit the template in place as a working note.
2. Fill every required field or mark it `GAP` / `N/A` with reason.
3. No unsupported factual claims (PROTOCOL cite-or-omit).
4. Treat `draft` / `proposed` notes as non-authoritative until status is `accepted`.
5. Do not invent APIs, source IDs, or citations (Theme 2).
6. After editing these templates or `docs/PROTOCOL.md`, run `scripts/refresh-skill-references.py`.

## Provenance

Derived from Theme 1/2/3 notes + integrated reports, plus Theme 4 (Cursor plugin components, accepted 2026-07-29). Template structure is local convention; content rules cite external E1/E2 inside the reports.
