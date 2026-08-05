---
title: "T23D-RAG — Keeping docs current when tools change"
status: draft
theme: theme-23-host-playbook
track: T23D
created: 2026-08-04
updated: 2026-08-04
authors: [t23d-rag-gatherer]
depth: deep
supersedes: null
aligned_with:
  - docs/research/notes/theme-23-host-playbook/campaign-brief.md
---

# T23D-RAG — Documentation drift / maintenance when surfaces change

**Using `research-protocol`**. Depth: **deep**. Draft ≠ SoT.

## 1. Scope

- **Question / goal:** Gather secondary (RAG) evidence on keeping host-facing documentation current when tools, APIs, or agent surfaces change; lightly observe Toolbelt local practice for update hooks.
- **In scope:** Documentation drift; docs-as-code / co-location; generated vs curated catalogs; change-coupled doc updates; Toolbelt E0 on `author-cursor-surfaces` + `CONTRIBUTING.md`; options for a Theme 23 maintenance contract.
- **Out of scope:** Elevating `docs/host-playbook.md` (T23C); Theme 24 learn-back; implementing CI now; inventing auto-generated playbook-as-law without human review.

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-04 |
| Tools used | Alexandria MCP `user-alexandria-rag` (`list_corpora`, `rag_probe`, `rag_query`); local file read/grep (E0) |
| Corpora / URLs searched | Prefer `software_engineering` (21 docs / 7712 chunks), `ai_llm_agents` (71 docs / 22720 chunks); both active index `v1` (ingest ~2026-07) |
| Queries (exact) | See §2.1 |
| What was *not* searched | Web / GitHub primary docs; other Alexandria shelves (`programming_algorithms_systems`, etc.); JOSS/Write the Docs primary sites outside RAG; Theme 13 report body beyond CONTRIBUTING pointer |
| Depth | deep |
| Waves / stop_reason | Wave 1 probes + full queries; Wave 2 sharpened (auto-gen API, colo docs, forget-update, tool versioning). **Stop:** diminishing returns — Wave 2 re-hit Silen / Irving / Winteringham; no dedicated “docs-as-code DoD / PR checklist” treatise in preferred corpora (`stop_rule` diminishing_returns_plus_2 satisfied for this gatherer) |
| Provenance (optional PROV) | Entity←Alexandria chunks + local paths; Activity=T23D RAG gather; Agent=Cursor gatherer |

### 2.1 Queries and probe verdicts

| # | Corpus | Query / probe | Probe verdict (when used) |
|---|--------|---------------|---------------------------|
| Q1 | `software_engineering` | probe: documentation drift keeping docs in sync with code APIs | partial |
| Q2 | `ai_llm_agents` | probe: documentation drift keeping docs in sync with code APIs | partial |
| Q3 | `software_engineering` | probe: docs-as-code maintenance checklist single source of truth generated documentation | strong |
| Q4 | `software_engineering` | probe: update documentation when changing APIs engineering process checklist | partial |
| Q5 | `software_engineering` | How do engineering teams prevent documentation drift and keep docs synchronized with changing code and APIs? | (rag_query k=10) |
| Q6 | `software_engineering` | docs-as-code single source of truth generated versus curated documentation catalogs maintenance | (rag_query k=10) |
| Q7 | `software_engineering` | When changing an API or feature, what process requires updating related documentation in the same change or PR? | (rag_query k=8) |
| Q8 | `ai_llm_agents` | keeping documentation current when tools APIs or agent skills change maintenance | (rag_query k=8) |
| Q9 | `software_engineering` | API documentation automatically generated from source code comments to avoid documentation out of sync | (rag_query k=8) |
| Q10 | `software_engineering` | documentation should live in the same repository as source code README docs directory CI documentation website | (rag_query k=8) |
| Q11 | `software_engineering` | forget to update documentation when code changes comments and docs out of sync maintenance burden | (rag_query k=8) |
| Q12 | `ai_llm_agents` | tool updates versioning deprecated features agents must adapt documentation of tools | (rag_query k=6) |
| Q13 | `software_engineering` | probe: docs as code review checklist documentation ownership Definition of Done update docs in same PR | partial (weak novelty) |

### 2.2 Local E0 paths read

- `skills/author-cursor-surfaces/SKILL.md`
- `skills/author-cursor-surfaces/references/author-cursor-surfaces.md`
- `docs/templates/author-cursor-surfaces.md` (grep: no playbook / host-facing update language)
- `CONTRIBUTING.md`

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | RAG secondary for industry patterns; targeted E0 for Toolbelt update hooks |
| Scope boundary | Theme-23 note under `docs/research/notes/theme-23-host-playbook/`; no elevate |

## 4. Findings

### 4.1 Documentation drift is real and often deferred

- `CLAIM` [E2] Documentation and release notes are often left to the end of a cycle or ignored under delivery pressure, despite quality value. [E2: Alexandria corpus=`software_engineering` source=`Software Testing with Generative AI (Mark Winteringham)` chunk_id=`bdf322688af0799a04b1c0d5` query=`Q5`/`Q11`] Quote: “documentation and release notes are sometimes left to languish at the end of a development cycle or are ignored entirely.”

- `CLAIM` [E2] Maintaining comments so they stay aligned with code is itself a cost; excess comments increase alignment work. [E2: same chunk_id=`bdf322688af0799a04b1c0d5`] Quote: “too much, and we create more work for ourselves in maintaining code and comments to ensure they align.”

- `CLAIM` [E2] Comments can become misleading when code changes and comments are not updated (“lies”). [E2: Alexandria corpus=`software_engineering` source=`Test-Driven Development with Python (Harry J.W. Percival)` chunk_id=`8da3f90b6c4a837a26f4f6f1` query=`Q11`] Quote: “you’ll forget to update the comments when you update the code, and they end up being misleading—lies!”

- `CLAIM` [E2] Hand-written API documentation via comments is error-prone: wrong info, or forgetting to update when API code changes. [E2: Alexandria corpus=`software_engineering` source=`Clean Code Principles And Patterns Python Edition (Petri Silen)` chunk_id=`68efee6fb47bdae924eea53b` query=`Q7`/`Q9`/`Q11`] Quote: “forget to update the documentation when you make changes to the API code itself.”

### 4.2 Mitigations: generate-from-source + co-locate + avoid duplicate SoT

- `CLAIM` [E2] For library public APIs, comments are justified specifically so API docs can be **automatically generated** from them, “to avoid situations where API comments and docs are out of sync.” [E2: Alexandria corpus=`software_engineering` source=`Clean Code Principles And Patterns Python Edition (Petri Silen)` chunk_id=`b594c791e9f5df63210b2a27` query=`Q9`]

- `CLAIM` [E2] Component docs should live **in the same repository** as source; root README plus split files under `docs/`; library API docs should be **auto-generated from source**; feature lists can **link** Gherkin features so the same information is not stored twice. [E2: Alexandria corpus=`software_engineering` source=`Clean Code Principles And Patterns Python Edition (Petri Silen)` chunk_id=`e90b23a2a0acaf64ae846e3b` query=`Q6`/`Q10`] Quote: “Software component documentation should reside in the same source code repository”; “you don’t have to store the same information in two places.”

- `CLAIM` [E2] Many web frameworks generate OpenAPI / interactive docs from source code (code-first preferred over maintaining parallel handwritten + generated artifacts). [E2: Alexandria corpus=`software_engineering` source=`Clean Code Principles And Patterns Python Edition (Petri Silen)` chunk_id=`54262889acedb4d2204b5467` query=`Q6`/`Q9`]

- `CLAIM` [E2] Manual cut-paste of function names/docstrings into docs is time-consuming and error-prone as APIs grow; generators (e.g. Sphinx autodoc) scan source instead. [E2: Alexandria corpus=`software_engineering` source=`Research Software Engineering with Python (Irving et al.)` chunk_id=`6a0749181f0bcc03e1cfde54` query=`Q10`] Quote: “manually cutting and pasting… would be a time-consuming process prone to errors as more functions are added over time.”

- `CLAIM` [E2] Analogous SoT discipline (schema): keep the authoritative description in VCS; competing “model” stores create burden and lose history. [E2: Alexandria corpus=`software_engineering` source=`Unit Testing Principles, Practices, and Patterns (Vladimir Khorikov)` chunk_id=`2ba8415fb25d9e2b8d612185` query=`Q6`] — *database schema example; pattern transferable to catalogs, not literal Toolbelt law.*

### 4.3 Change-coupled process (partial evidence)

- `CLAIM` [E2] In a branch-per-feature workflow, changes that only make sense together (e.g. new parameter **and** all call sites) belong in **one** feature branch. [E2: Alexandria corpus=`software_engineering` source=`Research Software Engineering with Python (Irving et al.)` chunk_id=`8aba60db4c26f9bed4824e0f` query=`Q7`] Quote: “neither alteration makes sense without the other… should be done in one branch.”

- `CLAIM` [E2] Unrelated documentation updates discovered mid-feature should **not** ride along on the feature branch—commit, switch, new branch for the other work. [E2: Alexandria corpus=`software_engineering` source=`Research Software Engineering with Python (Irving et al.)` chunk_id=`6ad9a68bb9a4348193ba6368` / `8aba60db4c26f9bed4824e0f` query=`Q7`/`Q11`]

- `GAP` Corpora did **not** yield a clear, high-signal “update docs in the same PR / Definition of Done” checklist for product/operator playbooks. Probe Q13 remained **partial** with weak topical fit (QA / debt / vibe-coding index noise). Searched: Q4, Q7, Q13. Result: change-coupling for **code+callers** is evidenced; change-coupling for **surface→host playbook** is by analogy only.

### 4.4 Agent / tool surfaces (ai_llm_agents)

- `CLAIM` [E2] Agents need strategies for **tool updates and versioning**, deprecated features, and adapting to new tool interfaces. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Agentic AI Systems` chunk_id=`c4b3a514f592b5583f106a0d` query=`Q12`] Quote: “Agents need strategies to handle tool updates, version compatibility, and deprecated features.”

- `CLAIM` [E2] Maintaining tool definitions across multiple model-specific formats is cumbersome; frameworks help centralize definitions. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Agentic AI Systems` chunk_id=`bad68696dbef0f84b4fba63e` query=`Q8`/`Q12`]

- `CLAIM` [E2] Custom tools that call external services require ongoing testing, debugging, and **updates as APIs change**. [E2: Alexandria corpus=`ai_llm_agents` source=`RAG with Python Cookbook (Dominik Polzer)` chunk_id=`48662232d1fb4fbe046c7308` query=`Q8`] Quote: “each tool requires testing, debugging, and updates as APIs change.”

- `CLAIM` [E2] Knowledge-base / RAG content for agents: keep content fresh with regular updates and reviews; use version control. [E2: Alexandria corpus=`ai_llm_agents` source=`n8n BOOK FOR BEGINNERS… (Arsath Natheem S)` chunk_id=`e2d0cfa80cdb379cb5ce1789` query=`Q8`] Quote: “Keep content fresh – Regular updates and reviews.”

- `CLAIM` [E2] Point readers to official docs that “track API changes” rather than freezing a book snapshot as sole SoT. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Data-Driven Applications with LlamaIndex (Andrei Gheorghiu)` chunk_id=`a6dce17e1a1ba64427f28ccb` query=`Q8`] Quote: “These examples track API changes…”

- `CLAIM` [E2] Lifecycle / governance: trust and certification must evolve as agents are updated; recertification when critical changes occur. [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh (Eric Broda, Davis Broda)` chunk_id=`47a8ab33fff359c47a98a56b` query=`Q12`] — enterprise mesh framing; useful analogy for “surfaces change → re-validate host guidance,” not Toolbelt CI law.

### 4.5 Toolbelt local E0 — does authoring already require host-facing doc updates?

- `FACT` [E0] `author-cursor-surfaces` SKILL + checklist (`skills/author-cursor-surfaces/…`, SoT template `docs/templates/author-cursor-surfaces.md`) cover outcome, surface choice, reinforce, compose map, and verify (paths, reload, slash, secrets, human accept). They do **not** mention host playbook, inventory, or updating host-facing adoption docs when surfaces change. Observed 2026-08-04. [E0: path=`skills/author-cursor-surfaces/SKILL.md`; path=`skills/author-cursor-surfaces/references/author-cursor-surfaces.md`; grep empty on playbook/host-facing]

- `FACT` [E0] `CONTRIBUTING.md` § “Changing skills or rules” already requires: wire Handoffs; **update `docs/packs/README.md` and README skill tables when adding surfaces**; refresh references + sync + Reload. It does **not** name a host playbook or Theme-23 inventory. Observed 2026-08-04. [E0: path=`CONTRIBUTING.md` — “Wire Handoffs; update docs/packs/README.md and README skill tables when adding surfaces.”]

- `FACT` [E0] No `docs/host-playbook.md` (or similarly named file) exists in the workspace yet. Observed 2026-08-04. [E0: glob `**/host-playbook*`]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Prefer generate-or-derive catalog rows from live surfaces; curate narrative playbook | open | §4.2 Silen/Irving; campaign parks auto-publish without review |
| H2 | Checklist gate in author-cursor-surfaces + CONTRIBUTING beats hope-based README sync | open | §4.1 Winteringham lag; §4.5 partial CONTRIBUTING already |
| H3 | CI doc-smoke is Phase 2 for Toolbelt | open | Campaign brief parks CI; CONTRIBUTING Phase 2 for CI |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Bundle docs with feature vs separate branch | Irving: coupled code changes one branch (`8aba60…`) | Irving: unrelated doc fix → separate branch (`6ad9a…`) | Prefer **coupled** updates when playbook/inventory **describes the changed surface** (same change set); unrelated doc polish can stay separate. Leave playbook-PR coupling as INFERENCE. |
| Manual API comments vs avoid comments | Silen: avoid comments except library public API for generation (`93a893…` / `b594c…`) | Winteringham: LLMs to write comments/release notes (`bdf322…`) | Different layers: prefer **generate-from-source** for catalogs; LLM-assisted prose is optional aid, not SoT. |

## 7. Gaps & OPEN

- `GAP` Preferred corpora are **weak** on explicit “docs-as-code Definition of Done / same-PR docs checklist / documentation ownership” for operator playbooks. Stronger hits are co-location, auto-gen API, and drift warnings. Searched: Q3–Q4, Q7, Q13.
- `GAP` No RAG hit that maps cleanly onto Cursor skills/rules → host playbook maintenance (agent books discuss tool **runtime** versioning, not plugin playbooks).
- `OPEN` Exact playbook path name and inventory appendix vs separate note (campaign enough-to-start GAPs) — not resolved by this gatherer.
- `OPEN` Whether inventory rows can be partially machine-listed from skill frontmatter without becoming unreviewed law (campaign park).

## 8. Implications — Options for Toolbelt maintenance contract

Label: `INFERENCE` [E4] only. Not design locks.

Premises shared by options below: (P1) Drift is common when docs are end-of-cycle (§4.1). (P2) Co-locate + single SoT + generate-where-possible reduce drift (§4.2). (P3) Coupled changes should travel together when neither makes sense alone (§4.3). (P4) Tool/agent surfaces need update strategies as interfaces evolve (§4.4). (P5) `author-cursor-surfaces` has **no** playbook update step; CONTRIBUTING already updates packs/README + README tables but not a host playbook (§4.5). (P6) Campaign / CONTRIBUTING park fat CI as Phase 2.

### Ranked options (lean → heavier)

| Rank | Option | Shape | Pros (premises) | Cons / parks |
|------|--------|-------|-----------------|--------------|
| **1** | **Checklist in `author-cursor-surfaces` (+ template SoT)** | New § verify / reinforce items: when adding/changing/removing skills, rules, or host-facing templates → update host playbook **or** the inventory it derives from; smoke that entry surface (`guide-meta`) still named | Puts gate on the skill already required for surface elevates (P5, campaign T23D); process not CI (P6) | Needs human accept of checklist wording; inventory must exist (T23A/C) |
| **2** | **CONTRIBUTING mirror line** | Extend “Changing skills or rules” bullet next to packs/README: also host-playbook / inventory | Matches existing contributor habit (P5); discoverable without invoking skill | Easy to skip if authoring outside CONTRIBUTING path |
| **3** | **Skill-body must-update (instruction, not only checkbox)** | Explicit step in `author-cursor-surfaces` Instructions: stop before draft complete until playbook/inventory touched or waived | Stronger than checkbox alone (P1) | Heavier; may feel out of Theme 4 scope if not accepted |
| **4** | **Derive inventory, curate playbook** | Machine-assisted listing from live `SKILL.md` / rules FM → human-curated playbook narrative; playbook links inventory | Aligns with generate-vs-duplicate (P2); campaign park on auto-publish without review | Generator not built; still needs update gate when FM changes |
| **5** | **Phase 2 CI smoke (parked)** | Later: fail/warn if playbook missing `guide-meta` / packs row drift vs filesystem | Automates P1 detection | Explicitly Phase 2 / out of Theme 23 elevate path; do **not** block T23C on CI |

**Lean recommendation (INFERENCE):** Rank **1 + 2** now when elevating Theme 23; keep **5** parked; treat **4** as optional helper after inventory shape accepted—not a substitute for human review.

## 9. Source list (deduped)

1. Alexandria `software_engineering` — Silen, *Clean Code Principles And Patterns Python Edition* — chunks `b594c791e9f5df63210b2a27`, `93a893ef69ac40bfdc7b513d`, `e90b23a2a0acaf64ae846e3b`, `54262889acedb4d2204b5467`, `68efee6fb47bdae924eea53b`
2. Alexandria `software_engineering` — Winteringham, *Software Testing with Generative AI* — `bdf322688af0799a04b1c0d5`
3. Alexandria `software_engineering` — Percival, *Test-Driven Development with Python* — `8da3f90b6c4a837a26f4f6f1`
4. Alexandria `software_engineering` — Irving et al., *Research Software Engineering with Python* — `6a0749181f0bcc03e1cfde54`, `6ad9a68bb9a4348193ba6368`, `8aba60db4c26f9bed4824e0f`, `694142cdb985baf0b327ffcf`
5. Alexandria `software_engineering` — Khorikov, *Unit Testing Principles…* — `2ba8415fb25d9e2b8d612185`
6. Alexandria `ai_llm_agents` — *Building Agentic AI Systems* — `c4b3a514f592b5583f106a0d`, `bad68696dbef0f84b4fba63e`
7. Alexandria `ai_llm_agents` — Polzer, *RAG with Python Cookbook* — `48662232d1fb4fbe046c7308`
8. Alexandria `ai_llm_agents` — Natheem, n8n beginners handbook — `e2d0cfa80cdb379cb5ce1789`
9. Alexandria `ai_llm_agents` — Gheorghiu, *Building Data-Driven Applications with LlamaIndex* — `a6dce17e1a1ba64427f28ccb`
10. Alexandria `ai_llm_agents` — Broda, *Agentic Mesh* — `47a8ab33fff359c47a98a56b`
11. E0 — `skills/author-cursor-surfaces/SKILL.md`, `skills/author-cursor-surfaces/references/author-cursor-surfaces.md`, `docs/templates/author-cursor-surfaces.md`, `CONTRIBUTING.md`

## Self-check

- [x] Depth recorded (deep) + stop_reason
- [x] Method + queries + chunk citations
- [x] FACT/CLAIM supported; INFERENCEs list premises
- [x] GAP on weak DoD/PR checklist corpus coverage
- [x] Draft not treated as law
- [x] Phase 2 CI parked
