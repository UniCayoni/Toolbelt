---
title: "T16D/F deep — Typology, exemplars, STANDARDS.md sampling"
status: draft
theme: theme-16-host-standards
created: 2026-08-02
updated: 2026-08-02
depth: deep
track: T16D/F
authors: [research-gatherer]
supersedes: null
related:
  - docs/research/notes/theme-16-host-standards/t16d-f-typology-exemplars-light.md
  - docs/research/notes/theme-16-host-standards/t16e-g-anatomy-quality.md
  - docs/research/notes/theme-16-host-standards/t16k-shape-options-lean.md
---

# T16D/F deep — Typology, exemplars, STANDARDS.md sampling

**Using `research-protocol`.** Depth: **deep**. Labels: FACT | CLAIM | INFERENCE | GAP | OPEN. Grades: E0–E4 / U.

## 1. Scope

- **Question / goal:** Close G2/G4/G5 — broader typology of host coding standards + real exemplars + GitHub `STANDARDS.md` (and kin) sampling, so Theme 16 can ground v1 type shortlist vs park list and anatomy of good standards docs.
- **In scope:** Primary language/org style guides; repo-local standards packs (filename hits + content categories); taxonomy of standard *types*; recurring anatomy sections; enforcement pointers (formatters/linters) as observed, not ceremony-as-law.
- **Out of scope:** Locking Toolbelt-universal coding law; exhaustive ISO catalogs; CI/merge automation design; elevating draft lean to accepted SoT.
- **Comprehension / research goal type:** adaptive (feedstock for `author-standards` / standards-profile template).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-02 |
| Tools used | WebFetch (primary URLs); GitHub MCP `search_code` + `get_file_contents`; `gh api` (Airbnb repo meta/commits; Node `.editorconfig`); Alexandria RAG `rag_query` corpus=`software_engineering` |
| Corpora / URLs searched | Google Style Guides hub + README; PEP 8; Rust Style Guide; Clippy book; TypeScript Handbook Do’s and Don’ts; Google TypeScript Style Guide; Airbnb/javascript README + repo API; Chromium styleguide.md; LLVM CodingStandards.html; raw GitHub STANDARDS/CODING_STANDARDS/STYLEGUIDE exemplars (see §4.2); Alexandria SE |
| Queries (exact) | GitHub code: `filename:STANDARDS.md`, `filename:CODING_STANDARDS.md`, `filename:STYLEGUIDE.md`; Alexandria: `coding standards style guide typology naming layout testing documentation safety security Framework Design Guidelines anatomy of a good style guide`; `gh api repos/airbnb/javascript` |
| What was *not* searched | Full text of every Google language guide; ISO/IEEE formal standards catalogs; private Google-internal guides; exhaustive CONTRIBUTING.md corpus; `ai_llm_agents` corpus this pass; runtime E0 of linters in Toolbelt host |
| Depth | deep |
| Waves / stop_reason | Wave 1 primary SoT (style hubs) → Wave 2 GitHub pack sampling + content fetch (10+ files) → Wave 3 Alexandria corroboration. **stop_reason:** new fetches would restate naming/layout/tests/docs/safety categories already evidenced; remaining a11y/i18n breadth needs product-specific hosts not required to close G2/G4/G5; `gh search` rate-limited mid-pass (MCP search already succeeded). |
| Provenance (optional PROV) | Entity←primary URLs + GitHub raw paths + Alexandria chunks; Activity=this gather 2026-08-02; Agent=research-gatherer + WebFetch/GitHub MCP/Alexandria |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Systematic primary pins + as-needed exemplar content reads until category coverage saturated |
| Scope boundary | Host-facing coding/UX/docs standards; exclude Toolbelt plugin elevation |

## 4. Findings

### 4.1 Primary style guides

- `FACT` [E1] Google Style Guides hub states that every major OSS project has its own style guide; “style” ranges from naming (e.g. camelCase) to bans (e.g. global variables, exceptions); guides assist work on Google-originated projects. [E1: Google Style Guides — https://google.github.io/styleguide/ — accessed 2026-08-02]
- `FACT` [E1] google/styleguide README lists in-repo guides including AngularJS, Common Lisp, C++, C#, Go, HTML/CSS, JavaScript, Java, JSON, Markdown, Objective-C, Python, R, Shell, Swift, TypeScript, Vim script; Effective Dart and Kotlin Style Guide live outside the repo. [E1: google/styleguide README — https://raw.githubusercontent.com/google/styleguide/gh-pages/README.md — accessed 2026-08-02]
- `FACT` [E1] Google hub/README: external contributions are **not** accepted; changes flow from Google internal guides first. [E1: same hub + README — accessed 2026-08-02]
- `FACT` [E1] PEP 8 is an Active Process PEP: coding conventions for the Python standard library; project-specific guides take precedence on conflict; consistency within a project/module outranks blind PEP consistency; explicit reasons to ignore guidelines (readability, surrounding code, pre-existing code, older Python). Covers layout, whitespace, comments/docstrings, naming, programming recommendations. [E1: PEP 8 — https://peps.python.org/pep-0008/ — accessed 2026-08-02]
- `FACT` [E1] Rust Style Guide defines the **default** Rust style for tools such as `rustfmt` (spaces not tabs; 4-space indent; 100-char line width; trailing commas; etc.); does not forbid non-default styles or tool configuration. [E1: Rust Style Guide — https://doc.rust-lang.org/style-guide/ — accessed 2026-08-02]
- `FACT` [E1] Clippy documents lint categories with default levels: `correctness` (deny), `suspicious`/`style`/`complexity`/`perf` (warn), `pedantic`/`restriction`/`nursery`/`cargo` (allow); `restriction` must **not** be enabled as a whole — case-by-case (e.g. strict styles, CI bans, panic prevention). [E1: Clippy Documentation — https://doc.rust-lang.org/clippy/ — accessed 2026-08-02]
- `FACT` [E1] TypeScript Handbook **Do’s and Don’ts** page focuses on declaration-file / typing pitfalls (boxed `Number`/`String`, `any`, callback/`void`, overload ordering)—not a general formatting style guide. [E1: TypeScript Do’s and Don’ts — https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html — accessed 2026-08-02]
- `FACT` [E1] Google TypeScript Style Guide is a public, slightly adjusted copy of Google’s internal TS guide; uses RFC 2119 must/should; covers source file basics/structure, and notes there is no automatic deployment process for the public copy (pushed on-demand by volunteers). [E1: Google TypeScript Style Guide — https://google.github.io/styleguide/tsguide.html — accessed 2026-08-02]
- `FACT` [E1] Airbnb JavaScript Style Guide repo (`airbnb/javascript`): description “JavaScript Style Guide”; **not archived**; `pushed_at` 2026-04-16; ~148k stars; README covers Types through Testing/Performance, Naming Conventions, etc.; ES5 guide marked Deprecated. [E1: GitHub API `repos/airbnb/javascript` + README — https://github.com/airbnb/javascript — accessed 2026-08-02]
- `CLAIM` [E1/E3] Airbnb guide maintenance is **intermittent**: recent commits include README/example fixes (2026-02), Actions updates (2026-01), eslint-config notes (2025-08), with longer gaps for large content rewrites—not abandoned, not continuously rewritten as a living product SoT. [E1: `gh api repos/airbnb/javascript/commits`; E3 community perception not surveyed this pass]
- `FACT` [E1] Chromium coding style hub points to language-specific guides (C++, Blink C++, Obj-C, Rust, Swift, Java Android, Python, GN, Markdown, Web Dev Style Guide for JS/HTML/CSS, plus lesser: Kernel C, WebIDL, Mojo IDL, Jinja, SQLite SQL); asks contributors to keep code inclusive. [E1: Chromium styleguide — https://chromium.googlesource.com/chromium/src/+/main/styleguide/styleguide.md — accessed 2026-08-02]
- `FACT` [E1] LLVM Coding Standards: not absolute in all instances; golden rule—when extending existing code, match surrounding style; goal is readability/maintainability; C++17 preference with toolchain constraints; Python should follow PEP 8 and format with `black` (pinned major); microscopic formatting not treated as fixed standards. [E1: LLVM Coding Standards — https://llvm.org/docs/CodingStandards.html — accessed 2026-08-02]

### 4.2 Repo-local standards packs (GitHub sampling)

**Search hit counts (GitHub code search, 2026-08-02):**

| Query | `total_count` (MCP) |
|-------|---------------------|
| `filename:STANDARDS.md` | 10200 |
| `filename:CODING_STANDARDS.md` | 2336 |
| `filename:STYLEGUIDE.md` | 3712 |

- `FACT` [E1] Filename search returns thousands of hits for `STANDARDS.md` / `CODING_STANDARDS.md` / `STYLEGUIDE.md` across GitHub (counts above). [E1: GitHub MCP `search_code` — accessed 2026-08-02]
- `GAP` Exact global prevalence of `.editorconfig` + CONTRIBUTING “style” sections not fully enumerated this pass (`gh search` hit rate limit after Airbnb/Node probes). Searched: planned `filename:.editorconfig`; Result: Node exemplar fetched instead.

**Sampled files (org/repo/path → categories observed):**

| # | org/repo/path | Categories covered (observed) |
|---|---------------|-------------------------------|
| 1 | `tektoncd/community` `standards.md` | **docs**, **tests**, **API patterns** (Go packages/export surface), PR/commit process, release notes, functionality gates; points to Google Go Style + Effective Go |
| 2 | `Corvusoft/restbed` `docs/STANDARDS.md` | **naming**, **layout** (Allman braces, 4 spaces), comments, exceptions, namespaces, **performance** (avoid premature opt); RFC 2119; astyle **enforcement** via pre-commit |
| 3 | `bullhorn/novo-elements` `STANDARDS.md` | **naming**, **layout**/style, **API patterns** (Angular/signals/DI), **tests**, **docs**/demos, **i18n** (labels via service), module boundaries/safety of public API |
| 4 | `NASA-SW-VnV/ikos` `doc/CODING_STANDARDS.md` | **layout**, **naming** (via clang-tidy), **docs** (Doxygen), **safety** (sanitizers, treat warnings as errors); clang-format/tidy **enforcement** |
| 5 | `apache/mynewt-core` `CODING_STANDARDS.md` | **naming**, **layout**, **docs** (public API Doxygen), license headers; clang-format check; skip-style-check escape hatch |
| 6 | `arangodb/arangodb` `STYLEGUIDE.md` | **enforcement** (clang-format CI/hooks) + Google-derived **naming**/comments/file headers; brownfield “new code follows; old drifts” |
| 7 | `citusdata/citus` `STYLEGUIDE.md` | **layout** via uncrustify/`citus_indent` CI; **naming** (CamelCase); comments; include order; Postgres style-conflict exception note |
| 8 | `stripe/stripe-ios` `STYLEGUIDE.md` | **naming**, **layout**/spacing, **docs** (header docs), **API patterns** (imports, nullability, categories), folder **structure** |
| 9 | `redhat-cop/infra.aap_configuration` `docs/STANDARDS.md` | Ansible **naming**/paths, **layout** (2-space YAML), role structure, Controller compatibility |
| 10 | `ekristen/aws-nuke` `docs/standards.md` | Thin stub → CONTRIBUTING; CLI flag naming convention only |
| 11 | `R2Northstar/NorthstarLauncher` `STANDARDS.md` | **naming** (PascalCase, prefixes), **docs** (Valve-style headers), exceptions via ask; split formatting PRs |
| 12 | `pulumi/docs` `UX-STANDARDS.md` | **a11y**/UX (primary action, link text, line length)—docs/marketing, not code layout |
| 13 | `nodejs/node` `.editorconfig` | Mechanical **layout** only: charset, EOL, indent 2 spaces, trailing whitespace, quote_type |

- `FACT` [E1] Each row above was fetched/read from the cited raw GitHub path on 2026-08-02 (WebFetch or Node editorconfig raw). [E1: raw.githubusercontent.com paths as listed]
- `FACT` [E1] Filename `STANDARDS.md` is overloaded: Tekton’s file is primarily contributor/PR expectations; aws-nuke’s is a stub; Restbed/Novo/Northstar are code standards; Pulumi’s related UX file is product UX—not interchangeable content types. [E1: content of rows 1, 2, 3, 10, 12]
- `INFERENCE` [E4] Host standards packs cluster into (a) mechanical layout + naming, (b) language/API idioms, (c) tests/docs expectations, (d) process/PR gates, (e) enforcement tool pins—with many files mixing several. Premises: sampled table; Google hub breadth claim; FDG layering (§4.4).

### 4.3 Typology table (proposed taxonomy × v1 lean)

Grounded in primary guides + sampled packs + Alexandria FDG/Clean Architecture/Beyond Vibe Coding. **v1 lean / park** aligns with Theme 16 normal-wave convergence and accepted T16K lean (not design law until Theme report accept).

| Type | What it constrains | Exemplars (support) | v1 lean? |
|------|--------------------|---------------------|----------|
| **Naming** | Identifiers, files, packages, prefixes/suffixes | PEP 8 Naming; Google/Arango/Stripe/Mynewt/Restbed/Novo/Northstar; Alexandria naming chunks | **v1** |
| **Layout / structure** | Indent, braces, line width, file/folder layout, imports order | PEP 8 Code Lay-out; Rustfmt defaults; EditorConfig; Citus/Arango format tools; Chromium language hubs | **v1** |
| **API / error patterns** | Public surface, errors, DI, package export, nullability | FDG chapters (Naming/Type/Member/Exceptions); Tekton Go packages; Stripe interfaces; Novo public API | **v1 optional** (if host needs) |
| **Patterns prefer/avoid** | Idioms, banned features, framework conventions | Clippy style/restriction; Chromium Modern C++ allow/ban; Novo Angular patterns; LLVM “prefer LLVM libs” | **v1** (prefer/avoid list) |
| **Tests** | Coverage, table tests, where tests live, no `.only` | Tekton Tests; Novo Testing; Beyond Vibe Coding checklist (Alexandria) | **v1** |
| **Docs** | Docstrings, public API docs, examples/demos, commit/release notes | PEP 257 link from PEP 8; Tekton Docs; Stripe header docs; Mynewt Doxygen; FDG self-documenting OM | **v1** (with tests as tests/docs bucket) |
| **Safety / security / secrets** | Sanitizers, warnings-as-errors, secrets, insecure patterns, assert | IKOS sanitizers; Clippy correctness; Beyond Vibe Coding security hygiene; Tekton “don’t panic”/error handling | **v1** (safety/secrets) |
| **Performance** | Hot-path rules, avoid premature opt, Clippy `perf` | Clippy `perf`; Restbed Optimisations; Beyond Vibe “power-hungry patterns” | **park** (unless host-critical) |
| **i18n** | User-facing strings, locale | Novo Labels & User-Facing Strings | **park** (elevate if host UI) |
| **a11y / UX content** | Inclusive UI, link text, actions | Pulumi UX-STANDARDS; Chromium “inclusive” note | **park** (elevate if host UI) |
| **Process / PR / release** | PR size, commit messages, release notes | Tekton standards.md | **park** as *coding-standard type* (belongs process/CONTRIBUTING; may link) |
| **Architecture locks** | Layering, module boundaries as *design law* | Novo module boundaries (borderline); FDG framework fundamentals | **park** → ADR/design-process (per campaign fence) |

- `INFERENCE` [E4] Cap v1 host-standard *types* at: **naming · layout/structure · patterns prefer/avoid · tests/docs · safety/secrets**, plus **API/error** when the host ships a library/API; park performance/i18n/a11y/process/architecture-as-standard until a host profile explicitly needs them. Premises: light T16D/F lean; sampled coverage density; campaign “cap v1 types”; T16K accepted feedstock model.
- `CLAIM` [E2] Framework Design Guidelines structure philosophy → fundamentals → naming → type/member → extensibility → exceptions → usage → patterns → obsolete appendix — shows multi-type layering in one canon. [E2: Alexandria corpus=`software_engineering` chunk_id=`6fe850ffc19e0fa77be3ae05` source=`Framework Design Guidelines…` query=`coding standards style guide typology…`]
- `CLAIM` [E2] Team style practices commonly include indentation/bracing, meaningful naming, language naming conventions, spacing. [E2: Alexandria corpus=`software_engineering` chunk_id=`f39c5f586518dd88f13e438c` source=`Clean Architecture with .NET` …]
- `CLAIM` [E2] AI-era checklists pair style/naming with tests, security hygiene, secret leaks, dependency license risk. [E2: Alexandria corpus=`software_engineering` chunk_id=`d0369fad9ec1c3e4c6d4b750` / `3a1b985f972b4f955812e20d` source=`Beyond Vibe Coding` …]

### 4.4 Anatomy — recurring sections in good standards docs

Observed across primary + packs (and T16E lean):

| Section | Role | Seen in |
|---------|------|---------|
| **Purpose / preamble** | Why the doc exists; audience | Google hub; Restbed Overview; Arango Preamble; Northstar Preamble; Tekton purpose bullets |
| **Scope** | Languages/paths/which code (new vs old) | Arango (new code); Citus (new vs match surroundings); Mynewt (C/asm only); Novo (`projects/novo-elements/`) |
| **Normative language** | MUST/SHOULD or RFC 2119 | Restbed; Google TS guide |
| **Rules by category** | Checkable constraints | PEP 8 TOC; all dense packs |
| **Examples** (good/bad) | Make rules falsifiable | PEP 8; Airbnb; Novo ❌/✅; Tekton release-note poor/good |
| **Exceptions / when to ignore** | Escape hatches | PEP 8 “foolish consistency”; LLVM golden rule; Restbed Guido quote; Citus Postgres-copy exception; Mynewt skip-style-check; Northstar “ask for them” |
| **Enforcement** | Formatter/linter/hook/CI pins | Restbed astyle hook; IKOS clang-format/tidy; Arango/Citus CI; Rustfmt/Clippy; EditorConfig |
| **Evolution / obsolete** | How guidance ages | FDG Obsolete Guidance appendix; Arango brownfield drift note; Airbnb ES5 Deprecated |
| **Pointers out** | Link to language SoT / principles / CONTRIBUTING | Tekton → Google Go + design principles; aws-nuke → CONTRIBUTING; Chromium hub → language guides |

- `INFERENCE` [E4] A good **host standards profile** should include at least: purpose, scope, rules (what), examples, exceptions, how-to-check/enforcement pointer, evolution/version—plus optional link to principles (T16C) and ADR fence for architecture. Premises: table above; T16E anatomy lean; FDG layering.
- `FACT` [E1] Multiple exemplars bind mechanical layout to tools (rustfmt, clang-format, uncrustify, astyle, EditorConfig, black) rather than prose alone. [E1: Rust Style Guide; IKOS; Arango; Citus; Restbed; Node `.editorconfig`; LLVM black — accessed 2026-08-02]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Filename `STANDARDS.md` alone is a weak signal of “coding style guide” content | confirmed | Tekton process vs Restbed code vs aws-nuke stub |
| H2 | v1 types naming/layout/patterns/tests-docs/safety cover most dense packs | confirmed | §4.2 category columns |
| H3 | TypeScript “handbook style” is a primary formatting SoT | rejected | Handbook Do’s and Don’ts = typing; Google TS guide is the formatting/API-style primary |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Indentation tabs vs spaces | Clean Architecture .NET text prefers tabs [E2 Alexandria `f39c5f586518dd88f13e438c`] | PEP 8 / Google / Rust / most packs: spaces [E1] | Prefer E1 host/language SoT; do not universalize tabs |
| Short vs descriptive names | Tekton “prefer short variable names” [E1] | Novo “no abbreviated names” [E1] | Host-local; both valid standards—profile must choose |
| Airbnb as living SoT | High star count + unarchived [E1] | Sparse large-content commits [E1] | Treat as influential community guide (E1 text + E3 popularity); pin date when citing; prefer host-owned profile |

## 7. Gaps & OPEN

- `GAP` Broader CONTRIBUTING.md “Coding Style” section corpus (beyond Golang pointer-only CONTRIBUTING). Searched: golang/go CONTRIBUTING; Result: defers to contribute.html—no deep sample matrix.
- `GAP` Systematic a11y/i18n coding-standard exemplars beyond Pulumi UX + Novo labels. Searched: Pulumi UX-STANDARDS, Novo Labels; Result: thin for general code hosts.
- `GAP` Chromium Web Development Style Guide and individual Google language guides not fully fetched beyond hub listings.
- `OPEN` Exact schema fields for `docs/templates/standards-profile.md` (T16E/K) — follow-up at design/elevate, not this note.
- `OPEN` Whether process/PR standards should share a profile file with coding standards or stay CONTRIBUTING-only (H1 suggests separate or clearly sectioned).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Deep T16D/F **closes** the light-note OPEN for primary pins + pack sampling enough for typology: v1 type shortlist remains naming / layout / patterns / tests+docs / safety(+secrets), optional API/error; park performance, i18n, a11y, process, architecture-locks. Premises: §4.1–4.3; normal-wave summary; T16K lean.
- `INFERENCE` [E4] Exemplar quality pattern for Toolbelt feedstock: purpose + scope + checkable rules + examples + exceptions + enforcement pointer + evolution—not a pasted Google/Airbnb guide as Toolbelt law. Premises: §4.4; campaign fence.
- `INFERENCE` [E4] Agents discovering `STANDARDS.md` must **read content** (or frontmatter type), not assume coding-style semantics from filename. Premises: H1.

## 9. Source list (deduped)

1. https://google.github.io/styleguide/ — Google Style Guides hub (2026-08-02)
2. https://raw.githubusercontent.com/google/styleguide/gh-pages/README.md — language list (2026-08-02)
3. https://peps.python.org/pep-0008/ — PEP 8 (2026-08-02)
4. https://doc.rust-lang.org/style-guide/ — Rust Style Guide (2026-08-02)
5. https://doc.rust-lang.org/clippy/ — Clippy Documentation (2026-08-02)
6. https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html — TS Do’s and Don’ts (2026-08-02)
7. https://google.github.io/styleguide/tsguide.html — Google TypeScript Style Guide (2026-08-02)
8. https://github.com/airbnb/javascript — Airbnb JS Style Guide (+ API meta/commits) (2026-08-02)
9. https://chromium.googlesource.com/chromium/src/+/main/styleguide/styleguide.md — Chromium (2026-08-02)
10. https://llvm.org/docs/CodingStandards.html — LLVM Coding Standards (2026-08-02)
11. GitHub raw exemplars: tektoncd/community/standards.md; Corvusoft/restbed/docs/STANDARDS.md; bullhorn/novo-elements/STANDARDS.md; NASA-SW-VnV/ikos/doc/CODING_STANDARDS.md; apache/mynewt-core/CODING_STANDARDS.md; arangodb/arangodb/STYLEGUIDE.md; citusdata/citus/STYLEGUIDE.md; stripe/stripe-ios/STYLEGUIDE.md; redhat-cop/infra.aap_configuration/docs/STANDARDS.md; ekristen/aws-nuke/docs/standards.md; R2Northstar/NorthstarLauncher/STANDARDS.md; pulumi/docs/UX-STANDARDS.md; nodejs/node/.editorconfig (2026-08-02)
12. Alexandria `software_engineering`: chunk_ids `6fe850ffc19e0fa77be3ae05`, `f39c5f586518dd88f13e438c`, `d0369fad9ec1c3e4c6d4b750`, `3a1b985f972b4f955812e20d` (2026-08-02)
13. Local: `t16d-f-typology-exemplars-light.md`, `t16e-g-anatomy-quality.md`, `t16k-shape-options-lean.md`, `campaign-brief.md` (context; draft/accepted as labeled)

## Self-check

- [x] Depth chosen and recorded (`deep`)
- [x] stop_reason recorded
- [x] Method block present
- [x] Every FACT/CLAIM has support
- [x] INFERENCEs list premises
- [x] No invented citations/APIs
- [x] Conflicts logged
- [x] Draft ≠ design law
