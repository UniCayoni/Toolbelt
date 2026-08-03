---
title: "Deep W3+3 — Final diminishing-return pass (Theme 16)"
status: draft
theme: theme-16-host-standards
created: 2026-08-02
updated: 2026-08-02
depth: deep
wave: W3+3
authors: [residual-gap-closer-w3p3]
closes_toward:
  - deep-w3p2-residual-last-gaps.md
  - deep-w3p1-residual-confirmed-gaps.md
  - deep-w3-residual-gaps.md
supersedes: null
---

# Deep W3+3 — Final diminishing-return pass (Theme 16)

**Using `research-protocol`**.  
**depth:** deep  

## 1. Scope

- **Question / goal:** Second successive diminishing-return pass under `diminishing_returns_plus_2` — last chance on the two W3+2 **CONFIRMED GAP** residuals only; close with real E1 citation or reconfirm GAP via *different* search angles than W3+2. After this pass the Theme 16 residual campaign **stops** even if GAPs remain.
- **In scope:** (1) conflict / precedence stack design/ADR > principles > standards — angles **not** used in W3+2 (ISO/IEEE process; Clean Architecture “policy”; XP coding standards vs values; Microsoft FDG principles vs style appendix; OpenAPI/design-first vs style). (2) Cursor AGENTS.md vs `.cursor/rules` — official docs / changelog only if primary; nested AGENTS merge implications only.
- **Out of scope:** Restating W3+2 Google/MADR/Azure/AWS/Stripe/Netflix primary log as new evidence; Reddit; Cursor forum as design SoT; live E0 AGENTS vs Team experiment; locking Toolbelt host shape; Alexandria; brownfield N-month glance.

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-02 |
| Tools used | WebSearch; WebFetch (Clean Architecture blog; MS Learn FDG index + Brad Abrams archive Internal Coding Guidelines; extremeprogramming.org Coding Standards; Ron Jeffries “When is it not XP?”; IEEE SA 42020 landing; ISO/IEC/IEEE 42010:2022 preview PDF; OAI learn.openapis.org Best Practices; Cursor docs/rules; Cursor docs/cli/using). O'Reilly FDG appendix HTML **Access Denied** — not used as FACT body. |
| Corpora / URLs searched | See §9 |
| Queries (exact) | `ISO IEEE software engineering process standards vs architecture decision principles precedence conflict`; `Clean Architecture Uncle Bob policy over details framework dependencies precedence`; `Extreme Programming XP coding standards vs values principles conflict precedence`; `Microsoft Framework Design Guidelines principles vs coding style appendix precedence`; `OpenAPI design-first vs coding style guide conflict precedence API design`; `Extreme Programming "Coding Standards" practice Kent Beck OR ronjeffries site:extremeprogramming.org OR site:ronjeffries.com`; `"UNLIKE THE FRAMEWORK DESIGN GUIDELINES" "coding style conventions are not required"`; `OpenAPI Specification official "source of truth" design-first coding standards conflict site:openapis.org OR site:swagger.io`; `site:cursor.com OR site:changelog.cursor.com AGENTS.md rules conflict precedence nested`; `site:changelog.cursor.com AGENTS.md rules precedence` |
| What was *not* searched | Reddit; Cursor Community Forum bodies as SoT (discovery hit titles only — not fetched/cited as FACT); live Cursor E0; paid full ISO/IEEE PDFs beyond 42010 preview + IEEE SA abstracts; FDG O'Reilly appendix body (blocked); Alexandria; W3+2 Google eng-practices / MADR / Azure WAF / AWS re-fetch |
| Depth | deep |
| Waves / stop_reason | **W3+3 (residual #2 of +2 — final).** `stop_reason`: **diminishing returns** — neither named GAP closed; fresh-angle primaries are domain fences / near-misses only; campaign stop per `diminishing_returns_plus_2`. |
| diminishing | **true** |
| Provenance (optional PROV) | Entity=Theme16 W3+2 confirmed residuals; Activity=W3+3 final residual gather 2026-08-02; Agent=residual-gap-closer-w3p3 |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Last-chance residual only; cite-or-omit; one fresh search per named angle |
| Scope boundary | W3+2 §4.1–4.2 opens only; no rewrite of closed scorecard rows |

## 4. Findings

### 4.1 Residual — Conflict / precedence stack (design/ADR > principles > standards)

#### Fresh angles (one search each; primaries fetched where reachable)

- `FACT` [E1] **ISO/IEC/IEEE 42010:2022** (preview) specifies requirements for architecture *descriptions* (AD), ADFs, ADLs, viewpoints, and recording of architecture decisions and rationale. Scope explicitly does **not** specify the processes, architecting methods, models, notations, techniques or tools by which an AD is created/utilized/managed. No ranked conflict stack of design/ADR docs over engineering principles over coding standards. [E1: ISO/IEC/IEEE 42010:2022 preview PDF — https://assets.vde-verlag.de/iec-normen/preview-pdf/info_isoiecieee42010%7Bed2.0%7Den.pdf — accessed 2026-08-02]
- `FACT` [E1] **IEEE SA 42020-2019** abstract: architecture processes (governance, management, conceptualization, evaluation, elaboration) complementary to 15288/12207; no three-tier host-doc conflict ladder vs principles/coding standards on the public landing text. [E1: https://standards.ieee.org/ieee/42020/7601/ — accessed 2026-08-02]
- `FACT` [E1] **Clean Architecture** (Martin): inner circles = higher-level **policies**; outer = mechanisms/details; Dependency Rule = source-code dependencies point inward. This is a *code-layer* dependency rule, not a document precedence stack (ADR/design > principles > lintable coding standards). [E1: https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html — accessed 2026-08-02]
- `FACT` [E1] **XP Coding Standards** (extremeprogramming.org): team agrees formatting/standards so code looks consistent and supports collective ownership. Does not rank coding standards below ADRs or foundational principles docs. [E1: http://www.extremeprogramming.org/rules/standards.html — accessed 2026-08-02]
- `FACT` [E1] **Ron Jeffries** “When is it not XP?”: the twelve practices (including Coding Standards) are a starting route; **values** (communication, feedback, simplicity, courage) are the yardstick — “practices will change, the values will not.” Values > practices hierarchy is methodology identity, **not** Toolbelt’s named ADR/design > principles > coding-standards conflict stack. [E1: https://ronjeffries.com/xprog/articles/when-is-it-not-xp/ — accessed 2026-08-02]
- `FACT` [E1] **Brad Abrams** (MS archive) Internal Coding Guidelines: “First, read the .NET Framework Design Guidelines… Unlike the Design Guidelines document, you should treat this document as a set of suggested guidelines. These generally do not effect the customer view so they are not required.” Domain fence: public API design guidelines vs internal style suggestions — **not** ADR > principles > standards. [E1: https://learn.microsoft.com/en-us/archive/blogs/brada/internal-coding-guidelines — accessed 2026-08-02]
- `FACT` [E1] MS Learn **Framework Design Guidelines** index: Do/Consider/Avoid/Do not for library design; rare justified violations allowed; no conflict ranking vs a separate coding-standards layer or ADR stack. [E1: https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/ — accessed 2026-08-02]
- `CLAIM` [E2/U] FDG book Appendix A search snippets assert coding style conventions are “not required” / “suggestions” unlike the Framework Design Guidelines — consistent with Abrams archive, but O'Reilly appendix page returned Access Denied this pass; do **not** grade the appendix body as fetched FACT. [U: https://www.oreilly.com/library/view/framework-design-guidelines/9780321578815/apa.html — fetch failed 2026-08-02]
- `FACT` [E1] **OpenAPI Initiative** Best Practices: OAI opinion strongly prefers Design-first; “Keep a Single Source of Truth” for OAD vs duplicated artifacts (incl. annotations). Domain = API description vs implementation drift — **not** ADR/design > engineering principles > general coding style conflict stack. [E1: https://learn.openapis.org/best-practices.html — accessed 2026-08-02]

#### Disposition

- `GAP` **CONFIRMED GAP.** W3+3 fresh angles expand the negative-space log (ISO/IEEE AD standards; Clean Architecture policy; XP values vs Coding Standards practice; Microsoft design-vs-style fence; OAI design-first / single SoT) but none state Toolbelt’s named three-layer conflict stack (design/ADR > principles > standards, with inferred-from-code lowest). Result: **CONFIRMED GAP**.

### 4.2 Residual — Cursor AGENTS.md vs Rules precedence (official primary only)

#### Official docs re-checked / nested-merge probe

- `FACT` [E1] Cursor Rules: four types include AGENTS.md (“Simple alternative to `.cursor/rules`”). Precedence: “Rules are applied in this order: **Team Rules → Project Rules → User Rules**. All applicable rules are merged; earlier sources take precedence when guidance conflicts.” **AGENTS.md is not named in that ordered list.** Nested AGENTS: “Instructions from nested `AGENTS.md` files are combined with parent directories, with more specific instructions taking precedence” — **AGENTS↔AGENTS only**; no statement that nested-specificity semantics extend to conflicts with `.cursor/rules` / Team / User / `alwaysApply`. [E1: https://cursor.com/docs/rules — accessed 2026-08-02]
- `FACT` [E1] Cursor CLI: reads root `AGENTS.md` / `CLAUDE.md` and applies them as rules **alongside** `.cursor/rules`. Co-application stated; conflict winner vs Team or Project `.mdc` / `alwaysApply` **not** stated. [E1: https://cursor.com/docs/cli/using — accessed 2026-08-02]
- `GAP` `site:changelog.cursor.com AGENTS.md rules precedence` — **no results** this pass. No changelog primary found defining AGENTS↔rules conflict order.
- `INFERENCE` [E4] Nested AGENTS merge (“more specific wins”) does **not** imply a documented win-order when AGENTS conflicts with Project `.mdc` or Team Rules. Premises: (1) nested language is scoped to AGENTS.md files only [E1 rules]; (2) Team→Project→User list omits AGENTS [E1 rules]; (3) CLI says “alongside” without winner [E1 cli/using].
- Forum titles appeared in web search (nested scoping / setup questions); **not fetched** — community help is not official primary; Reddit not searched per scope.

#### Disposition

- `GAP` **CONFIRMED GAP.** Official Cursor docs still do **not** specify whether `AGENTS.md` overrides or loses to Team Rules, Project `.mdc` (incl. `alwaysApply: true`), or User Rules on conflicting guidance. Nested AGENTS specificity does not close the cross-type gap. Result: **CONFIRMED GAP**.
- `OPEN` Live E0 Cursor session proving AGENTS vs enforced Team rule winner (unchanged; not run).

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Fresh ISO/IEEE / Clean Arch / XP / FDG / OpenAPI angle publishes named ADR > principles > standards stack | rejected / GAP | All domain fences or methodology values≠practices; none = named stack |
| H2 | Nested AGENTS merge semantics or changelog define AGENTS vs `.cursor/rules` conflict | rejected / GAP | Nested = AGENTS↔AGENTS; changelog empty; rules/CLI unchanged |
| H3 | Either residual closes with real citation this pass | rejected | Both CONFIRMED GAP |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| “Policy” / design authority metaphors | Clean Arch: policy > details (code deps) | OAI: design-first / single SoT for OAD | Prefer each E1 in domain; neither = Toolbelt three-tier doc stack |
| Design vs style weight | Abrams: FDG required; internal style suggested | Google eng-practices (W3+2): style absolute *on style* | Prefer each E1; both are domain fences, not named stack |
| Cursor load model | rules: AGENTS alternative + nested specificity | CLI: AGENTS **alongside** `.cursor/rules` | Both E1; still no AGENTS↔Team/Project winner |

## 7. Gaps & OPEN

- `GAP` Named conflict stack design/ADR > principles > coding standards (> inferred) — **CONFIRMED** after W3+3 final angle expansion.
- `GAP` Cursor AGENTS.md vs Team / Project `.mdc` / User / alwaysApply conflict precedence — **CONFIRMED**.
- `OPEN` Live E0 Cursor AGENTS vs enforced Team rule.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Theme 16 may **author** an accepted host conflict ladder in design, but must not cite industry SoT as already defining ADR > principles > standards — even after ISO/IEEE, Clean Arch, XP, FDG/Abrams, and OAI angles. Premises: §4.1 GAP + listed FACTs.
- `INFERENCE` [E4] Host bind guidance should treat AGENTS↔Team/Project conflict as **product-undefined** until Cursor documents it or an E0 experiment is run. Premises: §4.2 FACTs + GAP + nested-merge non-implication.
- `INFERENCE` [E4] Further residual gatherers on these two items would be pure restatement risk; stop per `diminishing_returns_plus_2`. Premises: W3+2 diminishing=true + this pass closed none.

## 9. Source list (deduped)

1. https://assets.vde-verlag.de/iec-normen/preview-pdf/info_isoiecieee42010%7Bed2.0%7Den.pdf — 2026-08-02
2. https://standards.ieee.org/ieee/42020/7601/ — 2026-08-02
3. https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html — 2026-08-02
4. http://www.extremeprogramming.org/rules/standards.html — 2026-08-02
5. https://ronjeffries.com/xprog/articles/when-is-it-not-xp/ — 2026-08-02
6. https://learn.microsoft.com/en-us/archive/blogs/brada/internal-coding-guidelines — 2026-08-02
7. https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/ — 2026-08-02
8. https://learn.openapis.org/best-practices.html — 2026-08-02
9. https://cursor.com/docs/rules — 2026-08-02
10. https://cursor.com/docs/cli/using — 2026-08-02
11. https://www.oreilly.com/library/view/framework-design-guidelines/9780321578815/apa.html — fetch **Access Denied** 2026-08-02 (not used as FACT body)

## 10. W3+3 residual scorecard

| # | Residual (from W3+2 open) | Result |
|---|---------------------------|--------|
| 1 | Conflict stack ADR/design > principles > standards | **CONFIRMED GAP** |
| 2 | Cursor AGENTS vs Team/Project/User conflict | **CONFIRMED GAP** |

| Field | Value |
|-------|-------|
| Closed any named GAP? | **no** |
| New FACT beyond restating W3+2? | Expanded negative-space only (ISO/IEEE, Clean Arch, XP, Abrams/FDG, OAI; Cursor nested non-implication) — no disposition change |
| diminishing | **true** |
| Campaign stop | **yes** — second successive diminishing-return pass complete |
