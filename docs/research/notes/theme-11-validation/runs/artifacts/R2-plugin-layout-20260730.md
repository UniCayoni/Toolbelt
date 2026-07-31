---
title: "Recon: d:\\Toolbelt plugin layout (R2 pocket smoke)"
status: draft
created: 2026-07-30
workspace_roots: ["d:\\Toolbelt"]
project_id: null
aligned_with: docs/research/reports/theme-1-codebase-research-for-agents.md
protocol_steps: S0-S18
smoke: R2-codebase-recon
---

# Codebase / workspace reconnaissance (short / as-needed)

**Using `codebase-recon`**. Mode: **as-needed**.  
Authority: `docs/PROTOCOL.md` + Theme 1. Mark unmet `GAP` — never invent.

## S0 — Seed task context

- [x] README / CONTRIBUTING — skipped (layout counts only); plugin manifest read instead
- [ ] Nearest `AGENTS.md` — `GAP` (not required for this smoke)
- [ ] Exact build/test/lint — `GAP` (out of scope)

## S1 — Declare comprehension goal

| Field | Value |
|-------|-------|
| Goal / task type | understand-for-X (plugin layout map) |
| Why this goal | Theme 11 R2 pocket smoke: skills count, rules count, PROTOCOL.md location |

## S2 — Choose strategy mode

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Scope boundary | `d:\Toolbelt` plugin dirs: `skills/`, `rules/`, `docs/PROTOCOL.md`, `.cursor-plugin/` |
| Missed-interaction risk noted? | yes — skill↔rule coupling, agents/, commands/, pack wiring not mapped |

## S3 — Memory / prior-knowledge check

- [x] Prior notes: Theme 11 R1 artifact noted 19 skills under `skills/` (draft, not SoT)
- Findings: corroborate with fresh E0 glob/Python this run

## S4 — Plan exploration agenda

1. Count `skills/*/SKILL.md`
2. Count `rules/*.mdc`
3. Locate `PROTOCOL.md`

## S5 — Instruction / ignore surface

- [x] Plugin manifest `.cursor-plugin/plugin.json` (name: toolbelt)
- [ ] Full agent instruction tree — `GAP` (out of scope)

## S6 — Structure discovery

- [x] Top-level plugin layout (scoped)

Entrypoints / packages (observed):

| Path | Role |
|------|------|
| `d:\Toolbelt\.cursor-plugin\plugin.json` | Plugin manifest (`name`: `toolbelt`) |
| `d:\Toolbelt\skills\` | 19 skill dirs each with `SKILL.md` |
| `d:\Toolbelt\rules\` | 4 rule files (`*.mdc`) |
| `d:\Toolbelt\docs\PROTOCOL.md` | Research protocol SoT (active) |
| `d:\Toolbelt\skills\research-protocol\references\PROTOCOL.md` | Skill-bundled PROTOCOL copy/reference |

## S7 — Top-down hypotheses

| ID | Expected module/layer / beacon | Status |
|----|--------------------------------|--------|
| H1 | Skills live under repo `skills/` with `SKILL.md` | confirmed |
| H2 | Rules live under repo `rules/` as `.mdc` | confirmed |
| H3 | Canonical PROTOCOL at `docs/PROTOCOL.md` | confirmed |

## S8 — Locate before edit

- [x] Glob + Python path checks
- Hit list: 19× `skills/*/SKILL.md`; 4× `rules/*.mdc`; `docs/PROTOCOL.md`; skill ref PROTOCOL

**Do not edit yet.** (No product/code edits; research notes under `docs/research/` OK.)

## S9 — Isolate recon context

- [x] Explore subagent skipped — tiny scoped as-needed smoke
- Summaries: N/A (direct glob/Python)

## S10 — Selective read (bottom-up)

| Path | Why | Program-model notes | Situation-model notes | Open Q |
|------|-----|---------------------|----------------------|--------|
| `.cursor-plugin/plugin.json` | confirm plugin identity | manifest JSON | name=toolbelt | — |
| `docs/PROTOCOL.md` | confirm PROTOCOL home | research protocol doc | status: active | — |

## S11 — Inquiry episodes

| Question | Conjecture | Search | Result |
|----------|------------|--------|--------|
| How many skills? | ~19 from R1 | glob `skills/*/SKILL.md` + Python | 19 [E0] |
| How many rules? | unknown | glob `rules/*.mdc` + Python | 4 [E0] |
| Where is PROTOCOL.md? | docs/ | glob `**/PROTOCOL.md` | `docs/PROTOCOL.md` + skill ref [E0] |

## S12 — Architecture / dependency (conditional)

Skipped: reason = layout counts only; no dependency recovery warranted.

## S13 — Synthesize cited notes (short/smoke)

### Graded findings

1. `FACT` [E0] There are **19** skills under `d:\Toolbelt\skills` (one `SKILL.md` each): author-agents-md, author-cursor-surfaces, codebase-recon, creative-narrative-design, creative-systems-design, creative-world-character-design, design-process, docs-research, draft-adr, implementation-execute, implementation-execute-subagents, implementation-execute-verify, implementation-happy-path, implementation-plan, implementation-plan-verify, reproduce-bug, research-protocol, systematic-debug, technical-design.
2. `FACT` [E0] There are **4** rules under `d:\Toolbelt\rules`: `draft-is-not-sot.mdc`, `research-before-write.mdc`, `research-protocol-grades.mdc`, `research-skill-coexistence.mdc`.
3. `FACT` [E0] Canonical research protocol lives at `d:\Toolbelt\docs\PROTOCOL.md` (header: “Toolbelt Research Protocol”; Status: active). A second copy exists at `d:\Toolbelt\skills\research-protocol\references\PROTOCOL.md`.
4. `FACT` [E0] Plugin manifest at `d:\Toolbelt\.cursor-plugin\plugin.json` declares `"name": "toolbelt"`.

## S14 — Persist findings

- [x] This checklist under `runs/artifacts/`
- [ ] Instruction-file updates — none

## S15 — Reflect / re-plan

- [x] Evidence sufficient for smoke goal
- Tool-use: glob + Python path-exists (Windows-safe); no invented modules

## S16 — Completion gate

- [x] Done-when met for layout map; out-of-scope items listed as `GAP`
- [x] No factual claims without citations
- [ ] Verification commands — `GAP` (not needed; no implementation)

**STOP.** No product/code implementation in this smoke.
