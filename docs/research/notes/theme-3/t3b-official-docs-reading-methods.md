# Theme 3B — Official guidance on researching & using product/project documentation

Status: notes only (not integrated report)  
Created: 2026-07-27  
Agent: t3b-official-docs-reading-methods  
Access date: 2026-07-27

## 1. Scope

Primary/official guidance on **how to research and use** product/project documentation (navigation, version pinning, distinguishing normative vs tutorial), not how to write pretty prose:

- Diátaxis (how different doc types should be read/used)
- Write the Docs / docs-as-code practices (official or primary community org docs)
- Vendor guidance: “read the docs”, versioned docs, release notes/changelogs
- `llms.txt` / machine-readable docs indexes as research entry points
- OpenAPI/reference vs tutorials — which to trust for API truth
- Google / Microsoft / AWS style “documentation best practices” when primary

Out of scope for this slice: GreyMatter plugin stub; locking RAG libraries; authoring style minutiae except where they imply research trust rules.

## 2. Method

| Item | Detail |
|------|--------|
| Date | 2026-07-27 |
| Tools | WebSearch, WebFetch, Shell (`Invoke-WebRequest` for Diátaxis pages that timed out on WebFetch) |
| Evidence preference | E1 preferred; E3 only for forums/discovery (none locked design here) |
| Primary queries | `Diátaxis documentation framework`; `Write the Docs docs as code`; `llms.txt llmstxt.org`; `OpenAPI Specification normative vs tutorials`; `Read the Docs versions`; `Keep a Changelog`; `Semantic Versioning`; `Google developer documentation style guide`; `Microsoft Writing Style Guide developer content`; `AWS DevOps guidance documentation lifecycle`; `Fuchsia documentation types`; `Software Engineering at Google documentation` |
| Primaries fetched | diataxis.fr (home, start-here, tutorials, how-to-guides, reference, explanation, tutorials-how-to, reference-explanation, compass); writethedocs.org/guide/docs-as-code; llmstxt.org/index.md; keepachangelog.com/en/2.0.0; semver.org/spec/v2.0.0; docs.readthedocs.com versions; learn.openapis.org; spec.openapis.org OAS 3.2.0 (local extract); developers.google.com/style; fuchsia.dev documentation-types; learn.microsoft.com style-guide developer-content; AWS Well-Architected DevOps DL.EAC.5; abseil.io SWE book ch.10 |
| Not used as locks | Secondary blogs (Kong, Mintlify, Sourcegraph, I’d Rather Be Writing); Stack Overflow RTD Q&A (E3 discovery only) |

## 3. Findings

### 3.1 Diátaxis — how to *read* / select doc types

- `FACT` — Diátaxis identifies four kinds of documentation responding to four needs: **tutorials**, **how-to guides**, **reference**, **explanation**. Each has a different purpose and must be written (and therefore *used*) differently. [E1: Diátaxis start-here — https://www.diataxis.fr/start-here/ — accessed 2026-07-27]
- `FACT` — **Tutorial** = lesson / learning experience; practical under guidance; purpose is skill/confidence acquisition (study), **not** getting a real-world job done. Example framing: create a simple game to learn, not to ship. Instructor is absent in written docs → tutorials are fragile and often conflated with how-tos. [E1: start-here; Tutorials — https://www.diataxis.fr/tutorials/ — accessed 2026-07-27]
- `FACT` — Tutorial research implication: tutorials **minimize explanation**, ignore options/alternatives, prioritize reliability of a single path; they are **not** the place for exhaustive API truth or “why”. [E1: https://www.diataxis.fr/tutorials/ — accessed 2026-07-27]
- `FACT` — **How-to guide** = directions for a **real-world goal/problem**; addresses an already-competent user at **work**; task-oriented (configure X, troubleshoot Y). Distinct obligation from tutorials: accomplish a task vs provide a learning experience. [E1: start-here; How-to guides — https://www.diataxis.fr/how-to-guides/; Tutorials vs how-to — https://www.diataxis.fr/tutorials-how-to/ — accessed 2026-07-27]
- `FACT` — **Reference** = technical description / **facts**; propositional knowledge consulted while working; “one hardly reads reference material; one **consults** it”; should be austere, authoritative, free of distraction and interpretation; structure should mirror the product/machinery (map ↔ territory). Users need it for **truth and certainty**. [E1: start-here; Reference — https://www.diataxis.fr/reference/ — accessed 2026-07-27]
- `FACT` — Diátaxis warns that auto-generated API reference is often treated as *all* documentation; it is powerful for fidelity to code but is still only the reference quadrant. [E1: https://www.diataxis.fr/reference/ — accessed 2026-07-27]
- `FACT` — **Explanation** = context/background; answers **why**; joins topics; serves **study** (understanding), not step-by-step work. [E1: start-here; Explanation — https://www.diataxis.fr/explanation/ — accessed 2026-07-27]
- `FACT` — Reference vs explanation test: would the reader turn to this **while executing a task** (reference) or **after stepping away to think** (explanation)? Mixing expansive “why” into reference harms both. [E1: https://www.diataxis.fr/reference-explanation/ — accessed 2026-07-27]
- `FACT` — Diátaxis **compass** (decision table for researchers/authors):

  | Content informs… | Serves user’s… | Doc type |
  |------------------|----------------|----------|
  | action | acquisition of skill | tutorial |
  | action | application of skill | how-to |
  | cognition | application of skill | reference |
  | cognition | acquisition of skill | explanation |

  [E1: The compass — https://www.diataxis.fr/compass/ — accessed 2026-07-27]

- `INFERENCE` — For GreyMatter-style **docs research**, default trust order for *behavioral / API truth* is: **reference (and machine contracts)** > how-to (for a specific task path) > explanation (for intent/design) > tutorial (for orientation only). Premises: Diátaxis reference = facts/authority; tutorials explicitly not for explanation or alternatives; how-tos assume competence and a goal. [E4]

### 3.2 Write the Docs — docs-as-code (research implications)

- `FACT` — Write the Docs defines **Docs as Code** as writing documentation with the same tools as code: issue trackers, **version control (Git)**, plain-text markup (Markdown / reStructuredText / AsciiDoc), code reviews, automated tests; same workflows as development teams. [E1: Write the Docs — Docs as Code — https://www.writethedocs.org/guide/docs-as-code/ — accessed 2026-07-27]
- `FACT` — Stated benefits include blocking merges without docs and first drafts by developers — i.e. docs co-evolve with code under review. [E1: same]
- `INFERENCE` — When researching a docs-as-code project, prefer sources that share VCS history with the product (repo `docs/`, tagged releases, PR-reviewed pages) over orphaned wiki copies; staleness risk is lower when docs ship with the same review gate. Premises: WTD definition + merge-gate benefit. [E4]

### 3.3 Versioned docs (“read the docs” for the version you run)

- `FACT` — Read the Docs’ purpose for multi-version hosting: users can “read the **exact documentation** for the **specific version** of the project they are using.” [E1: RTD Versions — https://docs.readthedocs.com/platform/latest/versions.html — accessed 2026-07-27]
- `FACT` — RTD creates `latest` → default Git branch (usually `main`); if SemVer-like tags/branches exist, creates `stable` → greatest **stable** SemVer release (excludes pre-releases). Root URL redirects to **Default version** (defaults to `latest`; often reconfigured to `stable`). [E1: same]
- `FACT` — RTD Addons can warn when viewing non-`stable` (may be outdated relative to stable) and when viewing `latest` (development; features may not be deployed). [E1: same]
- `FACT` — SemVer: MAJOR = incompatible API changes; MINOR = backward-compatible functionality; PATCH = backward-compatible bug fixes. Software using SemVer **MUST declare a public API** (in code or documentation); once a version is released, that version’s contents **MUST NOT** be modified — changes ship as a new version. [E1: Semantic Versioning 2.0.0 — https://semver.org/spec/v2.0.0.html — accessed 2026-07-27]
- `FACT` — SemVer deprecation path: update docs + issue a **minor** with deprecation before removing in a **major**. [E1: same FAQ]
- `INFERENCE` — Research protocol should **pin doc version to product version** (`stable` / tag matching installed package), and treat `latest` as foreshadowing unless researching unreleased APIs. Premises: RTD versioning model + SemVer immutability of released artifacts. [E4]

### 3.4 Changelogs & release notes (delta research)

- `FACT` — Keep a Changelog 2.0.0: a changelog is a curated, chronologically ordered list of **notable** changes per version; for humans; every version should have an entry; latest first; show dates; **note which versioning scheme** you use; group by types: Added / Changed / Deprecated / Removed / Fixed / Security. [E1: https://keepachangelog.com/en/2.0.0/ — accessed 2026-07-27]
- `FACT` — Changelog ≠ release notes: changelog = complete ongoing record in-repo; release notes = curated announcement for one release (may be marketing-shaped). Prefer changelog as the **source** record. [E1: same]
- `FACT` — Breaking changes should be marked clearly (e.g. `**Breaking:**`); say **which interface** breaks (CLI, library API, protocol, file format, config). Prefer upgrade links over burying long procedures in the changelog (how-to is a different doc type). [E1: same]
- `FACT` — Deprecations: announce as `Deprecated` before `Removed` so upgraders meet the warning first. [E1: same]
- `FACT` — Do **not** treat raw git commit logs as a changelog. LLM/auto-generated drafts need human curation of what is “notable.” [E1: same]
- `INFERENCE` — For researching “what changed / what broke,” read changelog + SemVer major bumps first; use release notes as secondary curated summaries; do not use commit spam as normative. Premises: Keep a Changelog distinctions + SemVer signaling. [E4]

### 3.5 `llms.txt` as research entry point

- `FACT` — Proposal (Jeremy Howard, 2024-09-03): `/llms.txt` Markdown index giving LLMs brief background, guidance, and links to detailed Markdown — motivated by small context windows and noisy HTML. [E1: https://llmstxt.org/index.md — accessed 2026-07-27]
- `FACT` — Spec order: optional BOM → **H1 name (only required)** → optional blockquote summary → zero+ non-heading detail sections → zero+ H2 “file lists” of `[name](url)` plus optional `: notes`. H2 named **`Optional`** may be skipped when shorter context is needed. [E1: same]
- `FACT` — Companion practice: clean Markdown at same URL + `.md` (or `index.html.md`). Complements `robots.txt` / `sitemap.xml`; expected use mainly at **inference** time (on-demand research), not training. Sitemap is not a substitute (too large, not LLM-oriented, may miss `.md` variants). [E1: same]
- `FACT` — Example FastHTML `llms.txt` mixes tutorials, **HTMX reference**, and examples — i.e. the index can point at Diátaxis-style types; the researcher still must choose which linked page is normative. [E1: same]
- `INFERENCE` — Treat `llms.txt` as a **navigation/index** entry point for agent research, not as the source of API truth. Prefer linked reference / OpenAPI / `.md` page over summary bullets in the index. Premises: llms.txt is an index; Diátaxis reference is for facts. [E4]

### 3.6 OpenAPI / reference vs tutorials — API truth

- `FACT` — OAS: a properly defined OpenAPI Description lets consumers understand and interact with a service **without** requiring source code, **additional documentation**, or traffic inspection. [E1: OpenAPI Specification v3.2.0 — https://spec.openapis.org/oas/v3.2.0 — accessed 2026-07-27]
- `FACT` — Within OAS itself: the specification text for the Description format is the **only normative** description of that format; hosted JSON Schema is informational — if they differ, the **text MUST** be considered authoritative. [E1: same § Structure of an OpenAPI Description]
- `FACT` — OpenAPI Initiative Learn site: Learn pages are a **companion** to the OAS for learning and “best way to…” questions **out of scope of the specification**; readers should “always refer to the actual OpenAPI Specification for **reference**.” Human docs can be **generated from** the machine-readable description and stay up-to-date. [E1: https://learn.openapis.org/ — accessed 2026-07-27]
- `FACT` — spec.openapis.org hosts **authoritative** HTML renderings of OAI specs; Learn OpenAPI is for additional documentation/examples (non-normative relative to the OAS text). [E1: https://spec.openapis.org/ — via OAS cross-links; Learn — accessed 2026-07-27]
- `INFERENCE` — For **product API** truth when an OpenAPI Description exists and is maintained: trust the **OpenAPI document (paths/schemas/parameters)** over narrative tutorials/quickstarts; use tutorials only for workflows/side effects not encoded in the contract. For questions *about the OAS format itself*, trust the OAS text over Learn tutorials. Premises: OAS consumer claim + Learn’s own companion disclaimer + Diátaxis reference-as-facts. [E4]
- `GAP` — No single E1 vendor page found that says globally “always prefer OpenAPI over human reference when they conflict”; conflict-resolution when docs and OpenAPI diverge is product-specific (`OPEN` to check per-vendor “source of truth” statements).

### 3.7 Google / Microsoft / AWS / Fuchsia — primary patterns useful for *research*

#### Google developer style + Fuchsia doc types + SWE book

- `FACT` — Google developer documentation style guide: editorial guidelines for clarity/consistency; hierarchy is **project-specific style first**, then Google guide, then third-party (Merriam-Webster / Chicago; Microsoft Writing Style Guide for some technical style). Guidelines not rigid rules. [E1: https://developers.google.com/style — accessed 2026-07-27]
- `FACT` — Google style is primarily **authoring** guidance (voice, procedures, accessibility); limited direct “how to research docs” protocol. Procedures are numbered task sequences (how-to-like). [E1: https://developers.google.com/style/procedures — via search; About guide — accessed 2026-07-27]
- `FACT` — Fuchsia (Google) documentation types: **procedures/guides** (get-started, development how-tos), **concepts**, **reference** (APIs/CLIs; much auto-generated). Procedures should not explain concepts (link to concepts); reference examples should stay generic/simple — elaborate examples → procedural docs. [E1: https://fuchsia.dev/fuchsia-src/contribute/docs/documentation-types — accessed 2026-07-27]
- `FACT` — *Software Engineering at Google* (SWE book, docs chapter): treat documentation **like code** (VCS, owners, review, issue tracking); identify audience; **do not mix document types** — a document should have a singular purpose. Types include reference (incl. comments), design docs, tutorials, conceptual docs, etc. Conceptual docs **augment, not replace** reference; may sacrifice some edge-case completeness for clarity; reference should cover edge cases “religiously.” Seekers need consistency; stumblers need clarity/overviews. Keep customer-facing docs apart from provider/implementation docs. [E1: https://abseil.io/resources/swe-book/html/ch10.html — accessed 2026-07-27]
- `INFERENCE` — Google-aligned research habit: locate **canonical** doc (ownership / go-link / next-to-code), classify type (concept vs procedure vs reference), and for API edge cases prefer reference over conceptual overviews. Premises: SWE book canonicalization + Fuchsia type split. [E4]

#### Microsoft

- `FACT` — Microsoft Writing Style Guide (Learn): foundation of developer documentation is **reference documentation** (encyclopedia of programming elements) plus **code examples** showing use. [E1: https://learn.microsoft.com/en-us/style-guide/developer-content/ — accessed 2026-07-27]
- `FACT` — Microsoft Open Specifications (MS-DOCO): protocol docs carry version numbers and revision-class tables (Major/Minor/Editorial) with change-tracking appendices — i.e. **document version** is first-class for researchers of Windows protocols. [E1: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-doco/85e7630a-9dd5-462c-98ed-ce5451567c6d — accessed 2026-07-27 via search fetch]
- `INFERENCE` — Microsoft-shaped research: treat Learn **reference** pages as the encyclopedia for APIs; treat conceptual/how-to as usage paths; for protocol work, check document revision history. Premises: Style Guide developer-content + MS-DOCO. [E4]

#### AWS

- `FACT` — AWS Well-Architected DevOps Guidance **[DL.EAC.5]** (Recommended): integrate technical/operational docs into the development lifecycle — same tools/processes as app development; store docs in a **versioned** repo in machine-readable markup (e.g. Markdown); generate API references/changelogs from structured commits (e.g. Conventional Commits) and comments; automate generation on releasable branches; enables review, tests that suggest doc updates, and auditability. Explicitly links Write the Docs Docs as Code. [E1: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.5-integrate-technical-and-operational-documentation-into-the-development-lifecycle.html — accessed 2026-07-27]
- `INFERENCE` — AWS-aligned research: prefer docs that live with the releasable branch/tag and generated API reference over static marketing pages. Premises: DL.EAC.5. [E4]

### 3.8 Normative vs non-normative (cross-cutting)

| Source class | Role for researchers | Typical trust for “what does the product do?” |
|--------------|----------------------|-----------------------------------------------|
| OpenAPI / IDL / generated API reference | Contract / machine description | Highest when maintained |
| Hand-written Diátaxis **reference** | Human-consultable facts | High |
| How-to / procedure | One validated path for a goal | Medium (path-specific; may omit options) |
| Tutorial / quickstart / codelab | Learning path | Low for edge cases / full API surface |
| Explanation / concept / design doc | Why / mental model | High for intent; not for parameter tables |
| Changelog / SemVer | Delta / break signaling | High for “what changed” |
| Release notes / blog | Curated announcement | Medium |
| `llms.txt` | Index | Navigation only |
| Community forums / issues | Discovery of bugs/staleness | E3 — corroborate with E0/E1 |

## 4. Contradictions / conflicts found

- `FACT` — Diátaxis and Google SWE/Fuchsia agree on separating reference vs conceptual/tutorial content; Microsoft emphasizes reference + examples as the developer-doc foundation (examples sit near how-to/tutorial). No hard conflict — different granularity. [E1: sources in §3.1, §3.7]
- `CLAIM` — Keep a Changelog says changelogs are for humans and rejects a separate machine format; `llms.txt` / OpenAPI pursue machine-readable indexes/contracts. Compatible if roles stay separate (changelog = human delta; OpenAPI = API contract; llms.txt = LLM index). [E1: Keep a Changelog; llmstxt.org; OAS]
- `OPEN` — When **human reference prose** and **OpenAPI** disagree for a given product, which vendors formally declare the winner is under-documented in this pass (`GAP` in §3.6).
- `OPEN` — RTD `latest` vs `stable` default redirect: platform defaults to `latest`, but many projects point default at `stable` — researchers must check the project’s default, not assume RTD defaults. [E1: RTD Versions]

## 5. Gaps

- `GAP` — No single primary “Documentation Research Protocol” standard from Google/Microsoft/AWS analogous to Diátaxis for *reading* (most are authoring guides). Research methods must be **composed** from Diátaxis + versioning + contracts.
- `GAP` — Limited E1 on “Read the Docs” as a *phrase* beyond the RTD product; vendor “how to use our docs” landing pages vary per product and were not exhaustively surveyed.
- `GAP` — Sphinx / MkDocs / Docusaurus versioning UX not deeply fetched (RTD covers a major hosted pattern).
- `GAP` — IETF RFC 2119 keyword discipline in product docs (MUST/SHOULD) as a trust signal — not systematically surveyed this pass (`OPEN`).
- `GAP` — Alexandria RAG not queried this slice (web primaries sufficient for scope).

## 6. Candidate patterns for templates (“docs research protocol”)

Candidate steps for a GreyMatter **docs research protocol** template (still cited; not locked):

1. **Identify product + version under study** — pin installed/library version; open matching docs version (`stable`/tag), not assumed `latest`. [E1: RTD Versions; SemVer]
2. **Locate entry indexes** — official docs home; optional `/llms.txt` + `.md` mirrors; repo `docs/` if docs-as-code. [E1: llmstxt.org; Write the Docs Docs as Code; AWS DL.EAC.5]
3. **Classify pages with Diátaxis compass** (action/cognition × acquisition/application) before extracting claims. [E1: Diátaxis compass]
4. **For API / behavioral truth** — prefer OpenAPI/IDL/generated or hand-written **reference**; treat tutorials/quickstarts as non-exhaustive. [E1: OAS; Diátaxis reference; Learn OpenAPI companion disclaimer; Microsoft developer-content]
5. **For task completion** — use how-to/procedure matching the goal; do not generalize the single path as the full API. [E1: Diátaxis how-to; Fuchsia procedures]
6. **For “why / design intent”** — use explanation/concept/design docs; do not treat as parameter authority. [E1: Diátaxis explanation; SWE book conceptual vs reference]
7. **For deltas / upgrades** — read Keep a Changelog (or equivalent) + SemVer major/minor; note Deprecated→Removed; prefer changelog over git log / marketing release notes. [E1: Keep a Changelog; SemVer]
8. **Canonicalization** — prefer docs owned next to code / with clear owners / reviewed with code; deprecate duplicate wikis. [E1: SWE book ch.10; Write the Docs; AWS DL.EAC.5]
9. **Conflict handling** — if narrative ≠ contract, flag conflict; prefer contract + file `OPEN`/`GAP` until product-specific source-of-truth statement found. [E4 from §3.6 GAP]
10. **Staleness discovery (E3 allowed)** — issues/forums may surface outdated docs; corroborate with E0/E1 (current reference, version pin, changelog). [E1: PROTOCOL E3 exception for docs research; Keep a Changelog on inconsistent changelogs misleading]

## 7. Source list (deduped)

| Source | URL | Grade |
|--------|-----|-------|
| Diátaxis — home | https://www.diataxis.fr/ | E1 |
| Diátaxis — start here | https://www.diataxis.fr/start-here/ | E1 |
| Diátaxis — tutorials | https://www.diataxis.fr/tutorials/ | E1 |
| Diátaxis — how-to guides | https://www.diataxis.fr/how-to-guides/ | E1 |
| Diátaxis — reference | https://www.diataxis.fr/reference/ | E1 |
| Diátaxis — explanation | https://www.diataxis.fr/explanation/ | E1 |
| Diátaxis — tutorials vs how-to | https://www.diataxis.fr/tutorials-how-to/ | E1 |
| Diátaxis — reference vs explanation | https://www.diataxis.fr/reference-explanation/ | E1 |
| Diátaxis — compass | https://www.diataxis.fr/compass/ | E1 |
| Write the Docs — Docs as Code | https://www.writethedocs.org/guide/docs-as-code/ | E1 |
| llms.txt proposal | https://llmstxt.org/index.md | E1 |
| Keep a Changelog 2.0.0 | https://keepachangelog.com/en/2.0.0/ | E1 |
| Semantic Versioning 2.0.0 | https://semver.org/spec/v2.0.0.html | E1 |
| Read the Docs — Versions | https://docs.readthedocs.com/platform/latest/versions.html | E1 |
| OpenAPI Specification v3.2.0 | https://spec.openapis.org/oas/v3.2.0 | E1 |
| OpenAPI Learn — Getting started | https://learn.openapis.org/ | E1 |
| OpenAPI Initiative publications | https://spec.openapis.org/ | E1 |
| Google developer documentation style guide | https://developers.google.com/style | E1 |
| Fuchsia — Documentation types | https://fuchsia.dev/fuchsia-src/contribute/docs/documentation-types | E1 |
| Software Engineering at Google — Documentation | https://abseil.io/resources/swe-book/html/ch10.html | E1 |
| Microsoft Writing Style Guide — Developer content | https://learn.microsoft.com/en-us/style-guide/developer-content/ | E1 |
| Microsoft Open Specs — Document Versions (MS-DOCO) | https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-doco/85e7630a-9dd5-462c-98ed-ce5451567c6d | E1 |
| AWS Well-Architected DevOps — DL.EAC.5 | https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.5-integrate-technical-and-operational-documentation-into-the-development-lifecycle.html | E1 |
| GreyMatter Research Protocol | `d:\GreyMatter\docs\research\PROTOCOL.md` | E0 |

---

*End of notes — Theme 3B.*
