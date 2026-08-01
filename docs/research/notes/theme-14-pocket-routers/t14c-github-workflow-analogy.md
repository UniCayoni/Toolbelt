---
title: "T14C — GitHub reusable workflows as routing analogy"
status: draft
theme: theme-14-pocket-routers
track: T14C
created: 2026-07-31
updated: 2026-07-31
authors: [gatherer]
aligned_with:
  - docs/research/notes/theme-14-pocket-routers/campaign-brief.md
supersedes: null
---

# T14C — GitHub workflow analogies

## 1. Scope

- Question: What does GitHub document for composable/callable workflows that loosely maps to pocket routers + happy-path?
- In scope: Official Actions reusable workflows (`workflow_call`), nesting, inputs/outputs
- Out of scope: Implementing Toolbelt as Actions; Phase 2 CI ownership

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-31 |
| Tools used | WebFetch, WebSearch |
| Corpora / URLs | https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows ; GitHub Blog reusable workflows |
| Queries | reusable workflows workflow_call nesting |
| What was *not* searched | Composite actions deep dive; Environments full docs |
| Depth | normal |

## 3. Findings

- `FACT` [E1] A workflow becomes reusable when `on` includes `workflow_call`; callers invoke via job-level `uses:` (not a step). [E1: GitHub Docs — Reuse workflows — https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows — accessed 2026-07-31]
- `FACT` [E1] Callers pass typed **inputs** (`with:`) and **secrets**; reusable workflows can define **outputs** mapped from jobs for the caller. [E1: same URL]
- `FACT` [E1] Reusable workflows may be **nested** (caller → called → …); Docs state a maximum of **ten levels**; **loops not permitted**; permissions may only stay same or tighten down the chain. [E1: same URL]
- `FACT` [E1] Matrix jobs can call the same reusable workflow with different inputs (variation without rewriting the callee). [E1: same URL]
- `CLAIM` [E2] GitHub Blog contrasts reusable workflows (multi-job, conditionals, secrets) vs composite actions (steps bundled as one action). [E2: https://github.blog/developer-skills/github/using-reusable-workflows-github-actions/ — accessed 2026-07-31]
- `INFERENCE` [E4] Mapping (analogy only, not law): **leaf skill ≈ job/steps inside a reusable workflow**; **pocket router ≈ reusable workflow with `workflow_call` + inputs (ask type)**; **happy-path ≈ top-level caller** that chains routers and passes “outputs” (stage status) forward; **skip/classify ≈ job `if:` / inputs**. Premises: (1) E1 nesting+inputs; (2) Theme 10 compose-only ladder.
- `INFERENCE` [E4] GitHub’s **no-loops / explicit chain** bias favors Toolbelt’s **predictable ladder + documented skips** over fully emergent swarm routing for the default happy-path. Premises: (1) loops forbidden E1; (2) Anthropic workflows vs agents (T14D).
- `GAP` GitHub Docs do not describe “agent skill routers”; analogy is structural only.

## 4. Conflicts

| Topic | Docs (2026-07-31) | Older Blog | Prefer |
|-------|-------------------|------------|--------|
| Nesting depth | Docs: up to **ten** levels | Blog snippet: “up to four levels” | **E1 Docs** over E2 Blog |

## 5. Next

T14D agentic dynamic stages; keep Actions as metaphor only.
