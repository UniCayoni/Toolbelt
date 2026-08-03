---
title: "Theme 16 deep W2 — RAG + GitHub corroboration"
status: draft
theme: theme-16-host-standards
created: 2026-08-02
depth: deep
wave: W2
---

# Theme 16 deep W2 — RAG + GitHub corroboration

**Using `research-protocol`**.  
**depth:** deep  
**Method:** Coordinator parallel channels while W1 gatherers run. Cite-or-omit. Complements (does not replace) track deep notes.

## Channels

- Alexandria `software_engineering`, `ai_llm_agents` (`rag_query`, 2026-08-02)
- GitHub MCP `search_code`: `filename:PRINCIPLES.md`, `filename:STANDARDS.md`, `filename:AGENTS.md` + style terms

## Findings

### Principles vs standards (G1 / T16B–C)

| Label | Claim | Grade | Source |
|-------|-------|-------|--------|
| FACT | XP literature treats **coding standards** as team communication under collective ownership — sensible, not creativity-constricting. | E2 | Dooley/Kazakova *Software Development…* via Alexandria `software_engineering` chunk citing Beck 2000 |
| FACT | .NET *Framework Design Guidelines* appendix separates **framework design guidelines** (API) from **C# coding style conventions** (optional suggestions); style appendix starts from explicit **principles** (clarity over writer brevity; reduce noise in future diffs). | E2 | Cwalina et al. FDG 2020 via Alexandria |
| FACT | ACM/SE ethics framing: ethical tensions need **fundamental principles** more than blind detailed regulations (profession-level; not project coding law). | E2 | Dooley citing ACM SE Code via Alexandria |
| CLAIM | Profession ethics principles ≠ host project philosophy docs — useful analogy only for altitude (principles guide when rules conflict). | E4 | premises: above + Theme 16 ontology lean |

### Maintainability / formatters (G3 / T16I adjacent)

| Label | Claim | Grade | Source |
|-------|-------|-------|--------|
| FACT | Osmani *Beyond Vibe Coding*: use linters/formatters so AI outputs converge; define naming conventions and **refactor to one style** when AI mixes snake/camel. | E2 | Alexandria `software_engineering` |
| FACT | Fowler *Refactoring*: **parallel change / expand-contract** for gradual migration (illustrated on DB fields; general approach cited). | E2 | Alexandria |
| GAP | No high-score Alexandria hit for a concrete **git blame / recency recipe** for which style era wins — leave to W1 T16H/I + web primary. | — | this query |

### Agent bind of style (G6 / T16J)

| Label | Claim | Grade | Source |
|-------|-------|-------|--------|
| FACT | Multi-agent “Context Engine” literature separates **facts (what)** from **style/blueprint (how)**; Writer must follow retrieved style guide. | E2 | *Context Engineering for Multi-Agent Systems* via Alexandria `ai_llm_agents` |
| FACT | Coding-agent case study: agent reviews for **compliance with project standards**; standardized response templates including style guides improved suggestion relevance. | E2 | Bhavsar *Mastering AI Agents* via Alexandria |
| CLAIM | Bind pattern: load host standards/principles as procedural context, not only as chat vibes — aligns O1 `author-standards` feedstock. | E4 | premises: above + Theme 15 closeout consumer model |

### GitHub sampling — PRINCIPLES.md (G1 / G4)

Search `filename:PRINCIPLES.md` — many hits (discovery). High-signal samples (E3 until full fetch):

| Repo path | Snippet signal |
|-----------|----------------|
| `aws/containers-roadmap/PRINCIPLES.md` | Org culture principles; builds on Amazon Leadership Principles |
| `holochain/holochain/PRINCIPLES.md` | Explicitly **living** guiding principles; not prescription for every decision; includes doc-org expectations |
| `habitat-sh/habitat/UX_PRINCIPLES.md` | Domain UX principles (readable noun/verb CLI) |
| `slsa-framework/slsa/spec/principles.md` | Guiding principles behind design decisions |
| `openonion/connectonion/docs/principles.md` | Documentation principles (“Show, don't tell”) |
| `tensorflow/agents/PRINCIPLES.md` | Copies Google AI principles (org ethics — different altitude) |
| `perkeep/perkeep/doc/principles.md` | Short product principles sketch |

**INFERENCE (E4):** Real hosts publish short imperative/narrative principle lists separate from lintable style; some are product/org, some eng-team, some UX/docs — typology must not assume one filename = one altitude.

### GitHub sampling — STANDARDS.md (G2 / G4 / G5)

| Repo path | Snippet signal |
|-----------|----------------|
| `Corvusoft/restbed/docs/STANDARDS.md` | Expected coding style; pre-commit + Artistic Style enforcement |
| `intaro/pinboard/docs/standards.md` | “Foundational decisions the codebase follows”; language target |
| `redhat-cop/infra.aap_configuration/docs/STANDARDS.md` | Contributor YAML/Jinja conventions |
| `tektoncd/community/standards.md` | PR expectations for contributors/reviewers |
| `ogdf/ogdf/doc/standards.md` | Required coding standards for developers |

**FACT (E3 discovery):** Filename `STANDARDS.md` is overloaded — coding style, ISO language notes, CRA regulatory summaries, telemetry interop. Toolbelt templates must disambiguate by **frontmatter/purpose**, not filename alone.

### GitHub sampling — AGENTS.md bind (G6)

| Repo path | Snippet signal |
|-----------|----------------|
| `haifengl/smile/AGENTS.md` | Section **Coding Standards** → Google Java Style + local rules |
| `apache/flink/AGENTS.md` | Coding Standards + link to full Flink style guide URL |
| `apache/impala/AGENTS.md` | Coding Standards; Google C++ with exceptions |
| `chromium/chromium/.../cronet/AGENTS.md` | Points at Chromium styleguide paths |
| `cloudflare/sandbox-sdk/AGENTS.md` | Points to **coding-standards skill** under `.agents/skills/` |

**FACT (E3):** Common bind pattern = AGENTS.md short pointer → external style guide or local skill/pack. Matches Theme 16 lean (AGENTS short; standards durable).

## Named GAP status after this pass

| ID | Status |
|----|--------|
| G1 | Partially closed — exemplars listed; need W1 deep note + 2–3 full fetches |
| G2/G4 | Partially closed — typology feedstock + overload warning |
| G3/G8 | Still open for git-recency recipe (weak RAG) |
| G5 | Partially — anatomy signals (scope, enforcement, foundational decisions) |
| G6 | Strongly corroborated at E3/E2 |
| G7 | Still open |

## Stop note (this gatherer)

This note is corroboration only; does **not** count as a diminishing-returns residual pass.
