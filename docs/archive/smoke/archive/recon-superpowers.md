---
title: "Recon: obra/superpowers (smoke trial)"
status: draft
created: 2026-07-28
workspace_roots:
  - "C:\\Users\\Jonyc\\.cursor\\plugins\\cache\\cursor-public\\superpowers\\d884ae04edebef577e82ff7c4e143debd0bbec99"
project_id: null
aligned_with: docs/research/reports/theme-1-codebase-research-for-agents.md
protocol_steps: S0-S18
skill: codebase-recon
smoke: true
---

# Codebase / workspace reconnaissance — Superpowers smoke

Use **before** documenting architecture or implementing changes.  
Authority: `docs/research/PROTOCOL.md` + skill `codebase-recon`.  
Remote: https://github.com/obra/superpowers  
Local install (E0): cache path above.

## S0 — Seed task context

- [x] README / CONTRIBUTING — README present; CLAUDE.md holds contributor rules [E0]
- [x] Nearest `AGENTS.md` — exists; content is pointer `CLAUDE.md` only [E0]
- [x] Exact build/test/lint commands recorded with path citations (`FACT` [E0])

**FACT [E0]:** Documented tests: `docs/testing.md` says run via directory `run-*.sh` or `npm test`; evals via `cd evals && uv sync --extra dev` then `uv run drill …`.  
**FACT [E0]:** `package.json` has **no** `scripts` field → `npm test` not defined in this install.  
**FACT [E0]:** `evals/` directory **absent** from local cache tree.

## S1 — Declare comprehension goal

| Field | Value |
|-------|-------|
| Goal / task type | understand-for-X (smoke trial of GreyMatter `codebase-recon`) |
| Why this goal | Validate skill on a real installed plugin + GitHub remote |

## S2 — Choose strategy mode

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Scope boundary | Plugin surface: manifest, skills/, hooks/, docs beacons; not full harness ports |
| Missed-interaction risk noted? | yes — multi-harness dirs (`.claude-plugin`, `.codex-plugin`, …) not deeply read |

## S3 — Memory / prior-knowledge check

- [x] Prior accepted research notes / memory artifacts checked
- Findings: GreyMatter elevation map; agent_skills list already exposes Superpowers skills in this Cursor session [E0 session]

## S4 — Plan exploration agenda

1. Local tree + `.cursor-plugin/plugin.json`
2. Skills list + hooks presence
3. Corroborate vs GitHub tip (version, layout)
4. E3 limitation scan sample (open bugs)

## S5 — Instruction / ignore surface

- [x] Root (+ nested) agent instructions read — AGENTS.md → CLAUDE.md
- [x] Ignore/deny noise configured or noted — `.gitignore` present; not fully audited

## S6 — Structure discovery

- [x] Top-level layout / tree / repo-map  
Entry points / packages: `skills/` (14), `hooks/`, `docs/`, `tests/`, `scripts/`, multi-harness plugin folders, `package.json` (metadata only)

Via [Explore superpowers](6a5163e5-b6cb-4999-8018-a4bc79298f91) + GitHub MCP list root [E0/E1].

## S7 — Top-down hypotheses

| ID | Expected module/layer / beacon | Status |
|----|--------------------------------|--------|
| H1 | Cursor plugin = skills + hooks | confirmed |
| H2 | `evals/` present as docs claim | rejected (missing local + remote tip) |
| H3 | Installed version == GitHub tip version | rejected (6.1.1 vs 6.2.0) |

## S8 — Locate before edit

- [x] Grep / search / Explore run
- Hit list: `plugin.json`, `skills/*/SKILL.md`, `docs/testing.md`, `using-superpowers/SKILL.md`

**Do not edit yet.** (Smoke is read-only.)

## S9 — Isolate recon context

- [x] Broad search delegated to Explore — [Explore superpowers](6a5163e5-b6cb-4999-8018-a4bc79298f91)
- Summaries returned (not raw dumps): yes

## S10 — Selective read (bottom-up)

| Path | Why | Program-model notes | Situation-model notes | Open Q |
|------|-----|---------------------|----------------------|--------|
| `.cursor-plugin/plugin.json` | Manifest | skills+hooks only | version 6.1.1 local | tip 6.2.0 |
| `skills/using-superpowers/SKILL.md` | Entry skill | forces skill invocation | aggressive wording | relates to E3 #1878 |
| `docs/testing.md` | Test beacons | tests/ + evals/ | evals GAP | docs drift? |
| `AGENTS.md` | Agent config | 9-byte pointer | progressive disclosure extreme | — |

## S11 — Inquiry episodes

| Question | Conjecture | Search | Result |
|----------|------------|--------|--------|
| Does tip have evals/? | Maybe only in cache miss | GitHub get_file_contents `evals` | **does not exist** on tip SHA [E1] |
| Skill count match remote? | 14 local | GitHub skills dir + local list | 14 local confirmed [E0]; remote skills tree present [E1] |

## S12 — Architecture / dependency (conditional)

Skipped — smoke goal is surface recon, not SAR. Reason = scope.

## S13 — Synthesize cited notes

- [x] This file + `smoke-trial-summary.md`
- Hypotheses H1 confirmed; H2/H3 rejected with evidence

## S14 — Persist findings

- [x] Notes under `docs/research/notes/smoke/`
- [ ] Instruction-file updates — N/A (no GreyMatter AGENTS.md yet)

## S15 — Reflect / re-plan

- [x] Evidence sufficient for smoke of `codebase-recon`
- Tool-use: Explore summary + GitHub MCP + local Read worked; PowerShell listing flaky — Python E0 script more reliable on Windows

## S16 — Completion gate (before write tools)

- [x] Done-when for smoke met; remaining items `GAP`/`OPEN` listed
- [x] Claims cited
- [x] Verification commands identified (with E0 caveats)

**STOP.** No implementation in Superpowers. Human smoke goal = research only → **waive implement**.

## S17 — Then implement

N/A — waived.

## S18 — Reproducible investigation artifacts

- [x] Notes version-controlled under GreyMatter `docs/research/notes/smoke/`
- [x] Env: local cache hash `d884ae04…`; remote tip SHA from MCP `3dcbd5c4…`
- [x] Raw helper: `_e0_check.py`

---

## Key findings (graded)

1. **FACT [E0]:** Local Cursor plugin install `superpowers` **6.1.1** at cache path; declares `skills` + `hooks` only.  
2. **FACT [E1]:** GitHub tip `.cursor-plugin/plugin.json` version **6.2.0** (same skills/hooks shape).  
3. **FACT [E0]:** 14 skill folders present locally (listed in `_e0_check.py` output).  
4. **FACT [E0]+[E1]:** `evals/` absent locally and on GitHub tip; `docs/testing.md` still documents `evals/` → **docs↔tree conflict** (prefer E0/E1 tree; doc claim `STALE`/`CONTRADICTED_BY_E0` until found elsewhere).  
5. **FACT [E0]:** `package.json` has no `scripts` → README/`testing.md` `npm test` not executable as stated.  
6. **CLAIM [E3]:** Open bugs include SDD ledger collision (#1936), SessionStart/Windows hooks (#1827), skill tone flagged as injection (#1878), git-workflow override complaints (#1856) — discovery only; not design locks.  
7. **INFERENCE [E4]:** GreyMatter `codebase-recon` smoke **passed** — checklist fillable; Explore useful; version-pin caught install≠tip.
