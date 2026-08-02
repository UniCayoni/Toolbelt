---
title: "T15C — DoD / readiness analogues (multi-channel)"
status: draft
theme: theme-15-closeout-readiness
track: T15C
created: 2026-08-02
updated: 2026-08-02
authors: [gatherer]
---

# T15C — DoD / readiness analogues

## 1. Scope

- Question: How do industry + agent packs express done/ship/handoff *without* Toolbelt needing to own VCS ceremony?
- Channels: RAG, GitHub, web/primary, secondary

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-08-02 |
| Tools | Alexandria RAG; WebSearch; WebFetch; `gh` search/api |
| Queries | DoD / release readiness / ready for PR; skill packs |
| What was *not* searched | Exhaustive all GitHub DoD skills; academic lit review |
| Depth | normal (light pass all channels) |

## 3. Findings

### Primary / web

- `CLAIM` [E1] Scrum Guide: Definition of Done is a **formal description** of Increment quality; creates shared transparency; items not meeting DoD are not released/presented; org standard is minimum else **team creates** DoD appropriate to the product. [E1: https://scrumguides.org/scrum-guide.html — accessed 2026-08-02 via search highlights]
- `CLAIM` [E2] Agile Alliance glossary: team **agrees and displays** criteria; explicit contract; obsessing over endless criteria can be counterproductive — minimum generally required. [E2: https://agilealliance.org/glossary/definition-of-done/ — fetch timed out; from search highlights]
- `FACT` [E1] GitHub Docs: PR templates live in the **repository** (e.g. `.github/pull_request_template.md`); content is host-chosen (issues, description, reviewers). [E1: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository — accessed 2026-08-02]
- `CLAIM` [E2] Release/exit criteria practice: criteria should be **honest, measurable, falsifiable**; trace to requirements/risks; evidence artifacts; waiver path pre-declared. [E2: https://rexblack.com/resources/writing/exit-and-release-criteria — accessed 2026-08-02]
- `CLAIM` [E3] Release readiness reviews emphasize evidence-driven gates (tests, telemetry, rollback) with human go/no-go — secondary blogs. [E3: e.g. DevSecOps School RRR — discovery]

### Alexandria

- `CLAIM` [E2] Agile “done” often = acceptance criteria → acceptance tests; unclear AC ⇒ restart story conversation. [E2: Alexandria `software_engineering` chunk_id=`354cdc82c80fb36bc1bc52b8` source=Software Development Design and Coding…]
- `CLAIM` [E2] Team “done-ness” lists (docs, tests, threat model, observability) + templates/checklists so work is not forgotten. [E2: Alexandria `software_engineering` chunk_id=`f41010b0c258a33ce7823f9c` source=Clean Code Principles…]
- `CLAIM` [E2] “Gold/ready for marketplace” ≠ “done” — shipping can precede polish (game QA). Useful for Toolbelt: **ship-ready vs method-complete** may differ. [E2: Alexandria game QA gold milestone chunks]
- `CLAIM` [E2] Agent task completion: clear completion criteria in prompt; todo/checklist hooks; optional LLM judge vs agent claim; early-stopping risk. [E2: Alexandria `ai_llm_agents` chunk_id=`5e8d0ad3dbccf383dd55bec5` Designing Multi-Agent Systems…]
- `CLAIM` [E2] Shared workspace: users define **end conditions / success criteria** so agents know when to stop. [E2: Alexandria `ai_llm_agents` chunk_id=`a38dd17afd31062ba4c33def` Agentic Mesh…]

### GitHub skill packs

- `FACT` [E1] `zhengbingquant/frontier-skills` ships host-copied **`DEFINITION_OF_DONE.md`**: observed working, named proving command, guarded by test, clean diff, docs current, faithfully reported (gaps explicit), safe — “almost done” with gaps ≠ done. [E1: https://github.com/zhengbingquant/frontier-skills/blob/main/skills/new-python-project/assets/DEFINITION_OF_DONE.md — accessed 2026-08-02]
- `CLAIM` [E3] `DevOtts/build-it`: goal + numbered DoD drives autonomous run + honest report (repo discovery). [E3: repo README via `gh api` — accessed 2026-08-02]
- `GAP` Broad `filename:SKILL.md` “ready for PR” search returned weak/noisy hits; DoD often lives as **host asset/template**, not only skill prose. Searched: gh search code. Result: few clean skill-router analogues; stronger as profile files.

### Compare axes (session)

| Focus | Typical home | Toolbelt lean |
|-------|--------------|---------------|
| Ceremony (approve/merge/CI required) | Host GitHub/Actions | **Out** of plugin skill |
| Shared quality DoD (team-created) | Scrum / frontier DoD file | **In** — help define/check |
| Evidence-first “prove it” | frontier DoD #1–2; release criteria | **In** — bind to Toolbelt verify |
| Universal fixed mega-checklist | Some release templates | **Avoid** as law; offer slots |
| Agent completion criteria | Multi-agent books | Align with Done-when / Meta ready |

- `INFERENCE` [E4] Strongest transferable pattern: **explicit host-owned DoD/profile + evidence-linked check + honest gaps** — not merge automation. Premises: Scrum team-creates DoD; frontier DoD file; GitHub PR template is host content; Rex Black falsifiable criteria.

## 4. Conflicts

| Topic | Sources | Prefer |
|-------|---------|--------|
| Ship vs done | Game “gold ≠ done” vs Scrum “not Done ⇒ not released” | Toolbelt: separate **method ready** vs **host ship ceremony**; don’t equate |
| Fixed vs team DoD | Org minimum vs team-created (Scrum) | Host profile with optional org baseline slots |

## 5. Next

T15D evidence binding; T15F shape.
