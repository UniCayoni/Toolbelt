---
title: "GreyMatter research harness — elevation & smoke synthesis"
status: draft
theme: smoke
created: 2026-07-28
updated: 2026-07-28
authors: [cursor-agent]
supersedes: null
skill: research-protocol
smoke: v3
harness_announce: "Using research-protocol"
---

# GreyMatter research harness — elevation & smoke synthesis

**Using `research-protocol`.**  
Literal start: copied from skill `references/research-note.md`.

## 1. Scope

- Question / goal: Produce a **full Method-envelope** note covering harness elevation decisions and smoke outcomes, to exercise `research-protocol` (previously only checklist either-OK).
- In scope: skills/rules elevation, smoke v1/v2 process gaps, patches, remaining OPEN.
- Out of scope: plugin stub, RAG library choice, accepting ADRs as law.
- Comprehension / research goal type: perfective (harness quality)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-28 |
| Tools used | Read (skills/rules/notes), Python path-exists, prior GitHub MCP / WebFetch results from smoke v1–v2 |
| Corpora / URLs searched | Local `docs/research/**`, `.cursor/**`; prior cites: cursor.com/docs/skills.md, rules.md; obra/superpowers |
| Queries (exact) | path exists GreyMatter layout; re-read smoke-v2-summary, harness-patch-crosswalk, elevation map |
| What was *not* searched | Cursor desktop About build ID; Superpowers 6.2.0 full changelog; Alexandria this pass |
| Provenance (optional PROV) | Entity=smoke notes+skills; Activity=v3 research-protocol smoke; Agent=Cursor agent + human |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Synthesis of existing E0/E1 notes, not new large-repo recon |
| Scope boundary | Harness docs + smoke artifacts |

## 4. Findings

- `FACT` [E0] Five project skills exist under `d:\GreyMatter\.cursor\skills\` with `name` matching folder names. [E0: `_e0_check_v2.py` / v3 path check]
- `FACT` [E0] Always-apply rules include evidence grades and draft≠SoT; intelligent rules include research-before-write and coexistence. [E0: `.cursor/rules/*.mdc`]
- `FACT` [E1] Cursor Skills docs: skills load from `.cursor/skills/`; `disable-model-invocation: true` makes slash-like skills. [E1: https://cursor.com/docs/skills.md — accessed 2026-07-28 smoke]
- `FACT` [E0] Smoke v1 process gaps: skipped literal copy; under-invoked `research-protocol`; intelligent-rule auto-fire unproven. [E0: conversation retrospective + `smoke-trial-summary.md`]
- `FACT` [E0] Smoke v2 applied patches (announce, either-OK, `in_use` D0, OpenAPI N/A, Windows E0 tip) and reconfirmed Superpowers 6.1.1 vs tip 6.2.0. [E0: `smoke-v2-summary.md`]
- `FACT` [E0]+[E1] Superpowers local install 6.1.1; GitHub tip plugin.json 6.2.0; `evals/` missing vs `docs/testing.md`. [E0/E1: smoke recon notes]
- `INFERENCE` [E4] Soft explore-before-edit via skills/rules is the evidenced default; hard hooks remain optional. Premises: (1) Cursor hooks are enforcement [E1 elevation note]; (2) vendors do not mandate explore-before-edit [E0 Theme 1]; (3) smoke used soft gate successfully.
- `GAP` Exact Cursor app/build version for this machine — not queried.
- `OPEN` Whether Cursor auto-selects `research-before-write` without user naming research — needs session telemetry / controlled trial.
- `CLAIM` [E3] Superpowers open issues (e.g. SDD ledger #1936, tone-as-injection #1878) are discovery only — not harness locks. [E3: GitHub search smoke v1]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Full research-note Method block is fillable without invention | confirmed | this note |
| H2 | Intelligent rule auto-fires on implementation tasks | open | not measurable here |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Superpowers testing docs vs tree | `docs/testing.md` claims `evals/` + `npm test` [E0] | no `evals/`; no package scripts [E0/E1] | Prefer tree E0/E1; doc `STALE`/`CONTRADICTED_BY_E0` until fixed upstream |
| Soft GreyMatter vs Superpowers MUST-invoke | GreyMatter soft skills [E0] | `using-superpowers` non-negotiable invoke [E0] | Coexistence rule: use GreyMatter skill for GreyMatter research tasks; do not invent merged git policy |

### Conflict log (local convention)

```yaml
conflict_id: C-SMOKE-SP-EVALS
status: open
doc_locator: { path: "superpowers/docs/testing.md", version: "local 6.1.1" }
doc_quote: "Live in evals/ … Run plugin tests via … npm test"
code_locator: { path: "superpowers/package.json + missing evals/" }
observation: "evals absent; scripts null"
winner: code
evidence_grades: { doc: E0, observation: E0 }
claim_labels: [CONTRADICTED_BY_E0, STALE]
```

## 7. Gaps & OPEN

- Cursor build ID
- Intelligent-rule auto-fire proof
- Full acceptance of soft-gate ADR (separate human step)

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Keep checklist either-OK for short smokes; require this Method form when synthesizing multi-pass harness decisions. Premises: §4 smoke v1/v2.
- `INFERENCE` [E4] Safe next artifacts: root `AGENTS.md` (no invented commands) + proposed ADR for soft gates. Premises: GreyMatter recon v3; elevation research.

## 9. Source list (deduped)

1. `docs/research/PROTOCOL.md` [E0]
2. `docs/research/notes/smoke/smoke-v2-summary.md` [E0]
3. `docs/research/notes/smoke/archive/harness-patch-crosswalk.md` [E0]
4. `docs/research/reports/cursor-elevation-map.md` [E0]
5. https://cursor.com/docs/skills.md [E1]
6. Superpowers local + GitHub tip plugin.json [E0/E1]
7. `docs/research/notes/secondary/sec-elevation-gates-skills.md` [E0/E1 cites within]
