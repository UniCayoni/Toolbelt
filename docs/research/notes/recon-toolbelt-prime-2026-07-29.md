---
title: "Recon: Toolbelt (prime / understand)"
status: draft
created: 2026-07-29
workspace_roots: ["d:\\Toolbelt"]
project_id: null
aligned_with: docs/research/reports/theme-1-codebase-research-for-agents.md
protocol_steps: S0-S18
---

# Codebase / workspace reconnaissance

Use **before** documenting architecture or implementing changes.  
Authority: `docs/PROTOCOL.md` + Theme 1 integrated report (S0–S18).  
Full evidence table: `docs/research/reports/theme-1-codebase-research-for-agents.md` §2.

Checklist maps 1:1 to report steps. Mark unmet items `GAP` rather than inventing.

## S0 — Seed task context

- [x] README / CONTRIBUTING — `README.md` present; no `CONTRIBUTING` found (`GAP`)
- [x] Nearest `AGENTS.md` — none at repo root (`GAP`); Cursor rules under `rules/`
- [x] Exact build/test/lint commands recorded with path citations (`FACT` [E0])

| Command | Role | Citation |
|---------|------|----------|
| `python d:\Toolbelt\scripts\sync-toolbelt-local-plugin.py` | Install/sync → `~/.cursor/plugins/local/toolbelt` | [E0: `README.md`, `scripts/sync-toolbelt-local-plugin.py`] |
| `python d:\Toolbelt\scripts\refresh-skill-references.py` | Copy `docs/` SoT → `skills/*/references/` | [E0: `README.md`, `scripts/refresh-skill-references.py`] |
| Build/test/lint (npm/pytest/etc.) | N/A — docs/skills plugin, no app package | `GAP` — no `package.json` / test suite observed |

## S1 — Declare comprehension goal

| Field | Value |
|-------|-------|
| Goal / task type | understand-for-next-work |
| Why this goal | Human asked to prime on purpose + how Toolbelt works before follow-on tasks |

## S2 — Choose strategy mode

| Field | Value |
|-------|-------|
| Mode | systematic (scoped) |
| Scope boundary | Plugin surface: README, PROTOCOL, skills, rules, scripts, docs layout; not deep re-read of every gatherer note |
| Missed-interaction risk noted? | n/a (systematic) |

## S3 — Memory / prior-knowledge check

- [x] Prior accepted research notes / memory artifacts checked
- Findings: Theme 1–3 reports + secondary refinement under `docs/research/reports/`; archive ADR 0001 (status `proposed`); smoke/history under `docs/archive/`. Method SoT is `docs/PROTOCOL.md` + `docs/templates/`.

## S4 — Plan exploration agenda

1. Purpose / non-goals vs grey-matter (README + plugin.json)
2. Runtime path: edit repo → refresh references → sync local plugin
3. Skills + rules + PROTOCOL loop; theme research as justification history
4. Fill this checklist; stop before product/code implementation

Warn: no unbounded exploration without scope.

## S5 — Instruction / ignore surface

- [x] Root (+ nested) agent instructions read — `rules/*.mdc`; no `AGENTS.md`
- [x] Ignore/deny noise configured or noted — sync script ignores `.git`, `__pycache__`, `*.pyc`, `.cursor` [E0: `scripts/sync-toolbelt-local-plugin.py`]

Always-apply rules: `draft-is-not-sot.mdc`, `research-protocol-grades.mdc`.  
Intelligent/opt-in: `research-before-write.mdc`, `research-skill-coexistence.mdc`.

## S6 — Structure discovery

- [x] Top-level layout / tree / repo-map

```text
.cursor-plugin/plugin.json   manifest (name=toolbelt, v0.1.0)
README.md                    install + skill index
LICENSE
skills/                      codebase-recon, docs-research, research-protocol,
                             author-agents-md, draft-adr
rules/                       grades, draft≠SoT, explore-before-write, coexistence
docs/PROTOCOL.md             method law
docs/templates/              checklist/note SoT
docs/research/               theme reports + gatherer notes
docs/archive/                frozen smoke/sources/elevation/ADR
docs/packs/                  future packs stub
scripts/                     refresh-skill-references, sync-toolbelt-local-plugin
```

- Entry points / packages: Cursor plugin (skills + rules); not a runnable app server.

## S7 — Top-down hypotheses

| ID | Expected module/layer / beacon | Status |
|----|--------------------------------|--------|
| H1 | Agent research utility plugin, not Brain/RAG product | confirmed [E0: README, plugin.json] |
| H2 | PROTOCOL + templates are SoT; skills hold copies | confirmed [E0: refresh script, docs/README] |
| H3 | Operational load via `~/.cursor/plugins/local/toolbelt` sync | confirmed [E0: sync script, README] |
| H4 | Future quality/workflow packs already shipped | rejected — stub only [E0: docs/packs/README.md] |

## S8 — Locate before edit

- [x] Grep / path listing / selective reads run
- Hit list (path + why):
  - `README.md` — purpose/install
  - `docs/PROTOCOL.md` — grades/labels
  - `skills/*/SKILL.md` — when/how each skill runs
  - `scripts/*.py` — SoT → references → local plugin pipeline
  - `docs/research/reports/theme-*.md` — method justification (exec summaries)
  - `docs/archive/adr/0001-soft-explore-before-edit.md` — soft gate decision

**Do not edit yet.** (Prime-only; research note write allowed under S16.)

## S9 — Isolate recon context

- [x] Broad search delegated to Explore — skipped (small, known layout; ~79 files)
- Summaries returned (not raw dumps): n/a — parent agent scoped reads

## S10 — Selective read (bottom-up)

| Path | Why | Program-model notes (control) | Situation-model notes (data/fn) | Open Q |
|------|-----|-------------------------------|----------------------------------|--------|
| README.md | Purpose | Sync → Reload; refresh after SoT edits | Skills table; note path preference | — |
| docs/PROTOCOL.md | Method law | Cite-or-omit; E0–E4/U; claim labels | Note schema + integration rules | — |
| skills/codebase-recon/SKILL.md | Recon loop | Copy checklist; S0–S16; soft S16 | Host `docs/research/notes/` preferred | — |
| skills/docs-research/SKILL.md | Docs loop | D0–D14; version pin; E3 discovery | Docs↔code corroboration | — |
| skills/research-protocol/SKILL.md | Full notes | Method envelope + grades | draft≠accepted | — |
| scripts/refresh + sync | Delivery | SoT → references → local plugin | Hardcoded `d:\Toolbelt` paths | Portable path? OPEN |
| docs/packs/README.md | Growth | Stub packs | No always-apply sprawl | When to add? OPEN |

## S11 — Inquiry episodes (delocalized plans)

| Question | Conjecture | Search | Result |
|----------|------------|--------|--------|
| App vs method plugin? | Method only | README, plugin.json | Confirmed method utility; grey-matter for Brain |
| Where do skills load from? | Local plugin sync | sync script, README | `~/.cursor/plugins/local/toolbelt` |
| Hard write gates? | Soft only | ADR 0001, research-before-write | Soft; hooks deferred; ADR still `proposed` |

## S12 — Architecture / dependency (conditional)

If skipped: reason = understand-for-next-work; no package dependency graph; plugin is markdown skills/rules + two Python sync scripts.

## S13 — Synthesize cited notes

Durable findings — **short/smoke** graded section (this note):

### Graded findings

1. **FACT [E0]** Toolbelt is a Cursor local plugin for agent *research method* (PROTOCOL grades, recon, docs research, ADRs, AGENTS.md), not the Brain/RAG product. Prefer grey-matter for that. [`README.md`, `.cursor-plugin/plugin.json`]
2. **FACT [E0]** Method SoT lives in `docs/PROTOCOL.md` + `docs/templates/`; `scripts/refresh-skill-references.py` copies into `skills/*/references/`; `scripts/sync-toolbelt-local-plugin.py` replaces `~/.cursor/plugins/local/toolbelt`. [`README.md`, scripts]
3. **FACT [E0]** v1 skills: `codebase-recon` (S0–S16), `docs-research` (D0–D14), `research-protocol`, `author-agents-md` (`/` invoke), `draft-adr` (`/` invoke). [`README.md`, skill fronts]
4. **FACT [E0]** Always-apply rules enforce grades + draft≠SoT; explore-before-write and Superpowers coexistence are soft/intelligent. [`rules/`]
5. **FACT [E0]** Themes 1–3 reports under `docs/research/reports/` justify recon / agent docs / docs-research protocols; `docs/archive/` is frozen harness history. [`docs/research/README.md`, report headers]
6. **FACT [E0]** Future quality/workflow packs are stub-only in v0.1.0. [`docs/packs/README.md`, plugin version]
7. **INFERENCE [E4]** Next work that changes method should edit docs SoT then refresh+sync+Reload; next work that *uses* Toolbelt should announce skills and write notes under host `docs/research/notes/`. Premises: findings 2–3.
8. **GAP** No root `AGENTS.md`, no CONTRIBUTING, no automated test suite observed this pass.
9. **OPEN** Sync/refresh scripts hardcode `d:\Toolbelt` — portability if repo moves.

- Parallel models: domain = research methodology for coding agents; program = plugin skills/rules + sync scripts; situation = edit SoT → refresh → sync → Reload for runtime
- Hypotheses: H1–H3 confirmed; H4 rejected

## S14 — Persist findings

- [x] This file under `docs/research/notes/`
- [ ] Instruction-file updates queued — none (no repeated mistakes; AGENTS.md still `GAP` if desired later)

## S15 — Reflect / re-plan

- [x] Evidence sufficient for prime? yes
- Tool-use calibration notes: small repo; Explore unnecessary; checklist short-form grades enough (no full research-protocol Method note)

## S16 — Completion gate (before implementation write tools)

Exploration complete only if:

- [x] Done-when / thoroughness criteria met **or** unmet items listed as `GAP`
- [x] No factual claims without citations
- [x] Verification commands from instructions identified (refresh + sync; no app tests)

**STOP.** No product/code implementation in this pass. Research note write allowed.

## S17 — Then implement (out of recon completion)

Deferred — human will direct next work.

## S18 — Reproducible investigation artifacts

- [x] Notes version-controlled (this path; commit deferred unless human asks)
- [x] Env / steps: Cursor workspace `d:\Toolbelt`, date 2026-07-29, tools=Read/Glob/Shell path listing
- [x] Raw vs derived: theme reports = prior derived SoT history; this note = E0 prime recon
