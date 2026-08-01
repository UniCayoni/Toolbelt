---
title: "Theme 13 T13B — Contribution UX comparators (normal)"
status: draft
theme: theme-13-contributor-workflow
track: T13B
created: 2026-07-31
updated: 2026-07-31
authors: [coordinator]
depth: normal
aligned_with:
  - docs/research/notes/theme-13-contributor-workflow/campaign-brief.md
  - docs/research/notes/theme-13-contributor-workflow/t13a-decision-culture.md
supersedes: null
---

# T13B — Contribution UX (external primary docs)

**Using `research-protocol`**; depth: **normal**.  
**Using `research-docs`** for GitHub + comparator CONTRIBUTING/PR surfaces.

**Status:** `draft`. Not Toolbelt contributor SoT. Stars ≠ acceptance.

**Comparator set (pinned this pass):**

| ID | Project | Why |
|----|---------|-----|
| GH | GitHub Docs — community health / PR templates | Platform E1 for file locations & discovery |
| SK | agentskills/agentskills | Spec + skills ecosystem; AI disclosure culture |
| SP | obra/superpowers | Cursor/agent **skills plugin** closest peer |
| AD | Aider-AI/aider | Large agent-tooling app; classic CONTRIBUTING |
| CN | continuedev/continue | Extension/agent tooling; CONTRIBUTING shape (repo now read-only — treat as historical E1 sample) |

---

## 1. Scope

- **Question:** How do high-signal projects guide propose → discuss → change on GitHub, and which atoms fit Toolbelt without fighting T13A culture?
- **In:** CONTRIBUTING locations, PR templates, discuss-before-large-PR, AI disclosure, skill-contribution gates, CLA notes as discovery.
- **Out:** Implementing Toolbelt files this pass; locking CLA/CI; deep multi-wave fleet.

---

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-31 |
| Tools used | WebSearch; WebFetch primary URLs/raw GitHub; gh api for agentskills CONTRIBUTING URL |
| Corpora / URLs | See §9 |
| Queries (exact) | CONTRIBUTING PR template GitHub docs; continue/aider/superpowers CONTRIBUTING |
| What was *not* searched | Full VS Code CONTRIBUTING body; CLA legal analysis; live E0 of other orgs’ private bots |
| Depth | normal |
| stop_reason | Comparator atoms + parks enough for T13C lean; deep not required unless human wants more repos |

---

## 3. Findings — GitHub platform (E1)

- `FACT` [E1] Contribution guidelines go in repo root, `docs/`, or `.github/` as `CONTRIBUTING` (case-insensitive); GitHub surfaces a Contributing tab/link and links when opening issues/PRs. [E1: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors — accessed 2026-07-31]
- `FACT` [E1] Suggested CONTRIBUTING contents include steps for good issues/PRs, links to external docs/CoC, community expectations. [E1: same]
- `FACT` [E1] PR templates live as `pull_request_template.md` in root, `docs/`, or `.github/`; or multiple under `.github/PULL_REQUEST_TEMPLATE/`; must be on default branch to apply; template can ask for issue refs, change description, reviewer mentions. [E1: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository — accessed 2026-07-31]

---

## 4. Findings — agentskills (E1)

- `FACT` [E1] Routes contribution **types**: docs PRs welcome; bugs → Issues; proposals/questions → **Discussions**; default to Discussions when unsure. [E1: https://raw.githubusercontent.com/agentskills/agentskills/main/CONTRIBUTING.md — accessed 2026-07-31]
- `FACT` [E1] Spec additions held to a high bar (“easier to add than remove”); proposals should show real implementation pain, not theory. [E1: same]
- `FACT` [E1] Explicitly **not accepting** (yet): community skill directory submissions; major architectural redesigns; reference-library code PRs while direction unsettled. [E1: same]
- `FACT` [E1] **AI assistance must be disclosed** in PR/issue (extent of use); human understanding + rationale + evidence expected; non-disclosure may close the PR. Trivial typo exception. [E1: same]
- `FACT` [E1] Submitting changes: fork → branch → verify locally → focused PR; link related issues. [E1: same]

---

## 5. Findings — Superpowers (E1)

- `FACT` [E1] README contributing: fork → work from **`dev`** → follow writing-skills skill → fill PR template; **generally do not accept new skills**; skill updates must work across supported agents. [E1: https://raw.githubusercontent.com/obra/superpowers/main/README.md — accessed 2026-07-31]
- `FACT` [E1] PR template requires: target `dev` not `main`; authoring environment table (model, harness, plugins, human partner); problem statement; evaluation/eval counts; rigor checkboxes for skill changes; human reviewed complete diff. [E1: https://raw.githubusercontent.com/obra/superpowers/main/.github/PULL_REQUEST_TEMPLATE.md — accessed 2026-07-31]
- `INFERENCE` [E4] Superpowers optimizes against **unattended agent spam** via disclosure + human-review gates — relevant to Toolbelt as an agent-facing plugin, but Toolbelt need not copy `dev`/`main` split or adversarial eval harness. Premises: SP template [E1]; T13A Phase 2 / thin docs lean [E0 t13a].

---

## 6. Findings — Aider (E1)

- `FACT` [E1] Issues for bugs/features; **small PRs OK directly**; **large/significant changes: discuss in an issue first**. [E1: https://raw.githubusercontent.com/Aider-AI/aider/main/CONTRIBUTING.md — accessed 2026-07-31]
- `FACT` [E1] Requires Individual CLA as part of PR process; long CONTRIBUTING covers env setup, tests, pre-commit, CI workflows. [E1: same]
- `INFERENCE` [E4] Aider’s “discuss large changes first” matches Toolbelt’s research/accept culture better than drive-by skill dumps; CLA + heavy CI are optional parks unless Toolbelt later needs legal/CI scale. Premises: AD PR section [E1]; T13A parks [E0].

---

## 7. Findings — Continue (E1 sample / caveat)

- `FACT` [E1] Historical CONTRIBUTING describes fork → feature branch from `main` → PR to `main`; project board / good-first-issues; includes CLA section and large setup TOC (from indexed blobs / search snippets). [E1: https://github.com/continuedev/continue/blob/main/CONTRIBUTING.md — accessed via search/blob 2026-07-31]
- `FACT` [E1] GitHub README states `continuedev/continue` is **no longer actively maintained / read-only** — do not treat as live contribution process. [E1: https://github.com/continuedev/continue — README note via search 2026-07-31]
- `CLAIM` [E2] Continue is useful as a **shape sample** (setup + git workflow + CLA), not as current maintainer policy. Premise: read-only notice [E1].

---

## 8. Cross-cutting atoms (for T13C)

| Atom | Seen in | Fit for Toolbelt (lean) |
|------|---------|-------------------------|
| Root/`docs`/`.github` CONTRIBUTING | GH | **Yes** — discoverability |
| `.github/pull_request_template.md` | GH, SP | **Yes** — thin checklist |
| Discuss / issue before large change | AD, SK | **Yes** — maps to research-scope / theme / design accept |
| Route proposals vs bugs | SK (Discussions vs Issues) | **Yes** — optional GitHub Discussions |
| AI/agent disclosure | SK, SP | **Yes** — high fit for this repo |
| Human reviewed full diff | SP | **Yes** — soft checklist item |
| “We don’t take random new skills” | SP, SK | **Yes** — point to theme accept + author-cursor-surfaces |
| Authoring env table (model/harness) | SP | **Optional** — useful; keep short |
| CLA | AD, CN | **Park** unless legal need (T13D) |
| `dev` vs `main` landing | SP | **Park** — Toolbelt currently ships on `main` |
| Heavy pre-commit/CI matrix | AD | **Park** — Phase 2 CI later if wanted |
| Adversarial skill eval harness | SP | **Park** — Theme 11 E0 smokes are enough for now |

---

## 9. T13D parks (folded — false friends)

| Park | Why |
|------|-----|
| Copy Superpowers eval harness / writing-skills as Toolbelt law | Different product; Toolbelt has Theme 4 + Theme 11 |
| Require CLA day-one | Legal overhead; not evidenced as needed for UniCayoni/toolbelt |
| Force `dev` branch workflow | Conflicts with current single-`main` shipping unless intentionally adopted |
| Fat CI as contribution blocker before CONTRIBUTING exists | Premature; Phase 2 |
| Accept drive-by skill PRs without research/accept | Fights T13A |
| Treat Continue CONTRIBUTING as live SoT | Repo read-only |

---

## 10. Implications (INFERENCE — not locks)

- `INFERENCE` [E4] Minimal viable contributor pack: **CONTRIBUTING.md** (culture from T13A + how to propose) + **thin PR template** (summary, type of change, AI disclosure, accept/research pointer, sync/Reload note for skills) + README link. Premises: GH discovery [E1]; SK/SP disclosure [E1]; T13A G1 [E0].
- `INFERENCE` [E4] CONTRIBUTING should say: method/skill changes need **issue or discussion + research/accept path**; typo/docs may PR directly; use `author-cursor-surfaces` + domain-first names; draft notes ≠ merge criteria. Premises: T13A [E0]; AD discuss-large [E1]; SK high bar [E1].
- `INFERENCE` [E4] **No deep T13B fleet needed** for first elevate draft — atoms above are enough. Premises: stop_reason; diminishing returns.

---

## 11. Gaps & OPEN

| ID | Item | Follow-up |
|----|------|-----------|
| G1 | Whether to enable GitHub Discussions | Human product choice in T13C |
| G2 | AI disclosure exact wording | Draft in T13C / elevate |
| G3 | CODEOWNERS / branch protection | Optional later; not required for MVP docs |
| OPEN | Legal CLA | Explicit human decision if ever |

---

## 12. Source list

1. https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors  
2. https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository  
3. https://raw.githubusercontent.com/agentskills/agentskills/main/CONTRIBUTING.md  
4. https://raw.githubusercontent.com/obra/superpowers/main/README.md  
5. https://raw.githubusercontent.com/obra/superpowers/main/.github/PULL_REQUEST_TEMPLATE.md  
6. https://raw.githubusercontent.com/Aider-AI/aider/main/CONTRIBUTING.md  
7. https://github.com/continuedev/continue (README maintenance note) + CONTRIBUTING.md blob  
8. T13A: `t13a-decision-culture.md`  
