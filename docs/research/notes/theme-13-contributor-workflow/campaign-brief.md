---
title: "Theme 13 — Contributor / GitHub change workflow (research-scope brief)"
status: proposed
theme: theme-13-contributor-workflow
created: 2026-07-31
updated: 2026-07-31
accepted_scope: 2026-07-31
accepted_by: human (Jonathan)
decision_lean: quality_over_ease
authors: [coordinator]
depth: normal
campaign_phase: elevated
aligned_with:
  - docs/research/reports/theme-12-research-scoping.md
  - docs/packs/README.md
  - docs/PROTOCOL.md
  - docs/research/reports/theme-10-happy-path.md
supersedes: null
---

# Theme 13 — Contributor / GitHub change workflow

**Using `research-scope`**. Complexity: **theme/campaign**.  
**Gather:** none yet. Human must **accept** this track board before normal/deep research.

**Intent:** Make Toolbelt safe and clear for forks, issues, and PRs — without importing megarepo CI religion or fighting Toolbelt’s accept/draft culture.

**Human decision lean (2026-07-31):** Prefer **quality** (protect method culture, clear gates, durable contributor UX) over ease of implement or shortest possible docs.

---

## Header

```text
Title / idea: Contributor-friendly GitHub change path for Toolbelt (forks, PRs, method/surface additions)
Complexity: theme/campaign
Host note path: docs/research/notes/theme-13-contributor-workflow/
Date: 2026-07-31
Scoped by: agent (research-scope) + human intent
Enough-to-start (agent propose): yes — tracks named; start with normal scope on T13A+T13B; deep only if GAPs remain
Human accept scope: accepted (2026-07-31)
```

---

## Expand (short)

What must be true / looked up / decided before gather?

```text
- What “friendly for contributors” means for a Cursor plugin (skills/rules/docs), not a typical app repo
- What Toolbelt already parks (PR/workflow Phase 2 stub) and must not reinvent mid-Execute/Debug
- What self-imposed standards already act as contribution law (draft≠SoT, cite-or-omit, theme accept→elevate, naming, author-cursor-surfaces)
- Which practices from large OSS repos are E1-worth copying vs false friends (heavy CLA/CI/bots)
- What minimal surfaces to elevate later (CONTRIBUTING, PR/issue templates, decision pointers) vs out of scope
- How historical Toolbelt leans (Themes 5–12) should be summarized so outsiders don’t fight the method
```

---

## Tracks

| ID | Track name | Question | In scope | Out of scope | Priority | Depth lean | Next skill(s) |
|----|------------|----------|----------|--------------|----------|------------|---------------|
| **T13A** | Toolbelt decision culture (E0) | What standards and leans already govern design/feature/method changes in this repo? | PROTOCOL, draft≠SoT, theme accept→elevate, packs Phase 2 parks, naming grammar, author-cursor-surfaces, happy-path stops, Theme 11/12 smoke culture; accepted report elevation decisions | Rewriting pocket law; inventing new method grades | **P0** | **normal** | `research-codebase-recon` (as-needed) → `research-protocol` (normal note) |
| **T13B** | Contribution UX (external E1) | How do high-signal OSS / agent-tooling repos guide “propose → discuss → change”? | CONTRIBUTING, PR/issue templates, CODEOWNERS, fork/PR etiquette, “design first” / ADR norms from primary docs of a small set of comparators | Copying any one repo’s CI as Toolbelt law; star-chasing | **P0** | **normal** first; **deep** only if comparator set still thin | `research-docs` + `research-protocol` |
| **T13C** | PR / workflow pack shape | What thin Toolbelt surfaces should Phase 2 own after research? | Candidates: CONTRIBUTING.md, `.github/` templates, optional thin skill/checklist, README pointer; map to packs stub | Fat Bugbot/CI mega-pack; mandatory TDD/git hooks as Toolbelt law | **P1** | **normal** (compose after T13A+B) | `research-protocol` → later `design-process` / `author-cursor-surfaces` |
| **T13D** | False friends / parks | What contributor practices should Toolbelt explicitly reject or defer? | CLA-heavy gates, always-on bot noise, treating draft research as mergeable design, drive-by skill dumps without Theme 4 reinforce | Implementing those parks as features | **P1** | **normal** | `research-protocol` (integrate with T13B) |

**Concept atoms ≠ D11 checkable atoms** — tracks above are campaign slices, not API greps.

---

## Recommended gather order (after human accept)

```text
1. T13A normal — inventory Toolbelt self-standards (E0)
2. T13B normal — small comparator set (primary CONTRIBUTING/PR docs)
3. T13D fold into B/A as parks table
4. T13C compose lean — only after A+B enough
5. Deep reopen T13B (or slice) only if named GAPs remain and human opts in
```

**Do not** auto-launch deep fleets from this brief.

---

## Enough? / stop

```text
Agent enough-to-start?: yes
Reason: Multi-surface idea atomized; P0 tracks clear; caution preserved (internal culture before megarepo copy); Phase 2 stub acknowledged
Open GAPs / OPENs before gather:
  - Comparator repo shortlist (which 3–6?) — choose in T13B Method or human pin
  - Whether Theme 13 elevates a skill vs docs-only — decide in T13C after evidence
stop_reason: (none — awaiting human accept of scope)
Human gate: **accepted** 2026-07-31
```

---

## After accept

| Step | Action |
|------|--------|
| 1 | ~~Human accept scope~~ **Done** |
| 2 | ~~T13A normal~~ → [`t13a-decision-culture.md`](./t13a-decision-culture.md) (`draft`) |
| 3 | ~~T13B normal~~ → [`t13b-contribution-ux.md`](./t13b-contribution-ux.md) (`draft`; T13D parks folded in §9) |
| 4 | ~~T13C lean~~ → [`t13c-surface-lean.md`](./t13c-surface-lean.md) (`draft`) |
| 5 | ~~Theme 13 report + elevate~~ **Done** 2026-07-31 — CONTRIBUTING + PR template + README/packs |

Handoffs: `research-codebase-recon` · `research-docs` · `research-protocol` — not this skill for gather.

---

## Non-goals (this theme)

- Implementing CONTRIBUTING/PR templates before research accept  
- Replacing Theme 10 happy-path stop with mandatory PR ceremony  
- Locking CI/Bugbot product choices from E3 alone  
- Relitigating Themes 1–12 pocket spines  

---

## Sources for scoping only (not gather)

1. User intent 2026-07-31 (contributor-friendly GitHub; compare large projects; historical leans)  
2. Theme 12 research-scope SoT  
3. Packs README — PR / workflow **stub** Phase 2  
4. Themes 9–10 parks — PR/CI not owned by Debug/Happy-path  
