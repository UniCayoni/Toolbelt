---
title: "Deep W3+2 — Residual last GAPs (Theme 16)"
status: draft
theme: theme-16-host-standards
created: 2026-08-02
updated: 2026-08-02
depth: deep
wave: W3+2
authors: [residual-gap-closer-w3p2]
closes_toward:
  - deep-w3p1-residual-confirmed-gaps.md
  - deep-w3-residual-gaps.md
supersedes: null
---

# Deep W3+2 — Residual last GAPs (Theme 16)

**Using `research-protocol`**.  
**depth:** deep  

## 1. Scope

- **Question / goal:** Second (final) diminishing-return pass under `diminishing_returns_plus_2` — attack only the two W3+1 **CONFIRMED GAP** residuals; close with E1 or reconfirm GAP with expanded primary search log.
- **In scope:** (1) conflict / precedence stack among architecture decisions, engineering principles, and coding standards; (2) official Cursor docs only — AGENTS.md vs Team / Project / User / alwaysApply conflict precedence.
- **Out of scope:** Restating closed W3 / W3+1 items (CONTRIBUTING→PRINCIPLES, style-guide deprecate lifecycle, separate PRINCIPLES agent packs, a11y exemplar); locking Toolbelt host shape; Alexandria; live Cursor E0 conflict experiment; community forum precedence claims as SoT.
- **Optional glance:** brownfield normative **N-month recency** default — note only if a normative primary appears; else leave alone.

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-02 |
| Tools used | WebSearch; WebFetch (Google eng-practices standard + looking-for; MADR about; Azure WAF ADR; AWS DevOps DL.CR.1; AWS Architecture Blog ADR practices; Cursor docs/rules, help/customization/rules, docs/cli/using, help/customization/ignore-files; ignore-file reference timed out) |
| Corpora / URLs searched | See §9; Stripe jobs/culture (fetch timeout — used search snippet only as discovery, not graded FACT); Netflix techblog culture (search only — paved road / F&R, not graded as conflict-stack primary) |
| Queries (exact) | `"when style guide conflicts with design"`; `"takes precedence" ADR OR "architecture decision" "coding standard" OR "style guide" OR "engineering principles"`; `Markdown Any Decision Records MADR precedence principles coding standards conflict`; `AWS Well-Architected design principles vs coding standards conflict precedence`; `Stripe engineering culture coding standards vs design principles precedence`; `Netflix technology blog engineering principles coding standards conflict authority`; `site:cursor.com AGENTS.md rules precedence priority Team Project User`; `site:cursor.com ignore files .cursorignore AGENTS.md precedence`; `site:google.github.io/eng-practices design principles style guide absolute authority`; brownfield `"N months" OR months style recency git blame` (optional glance) |
| What was *not* searched | Live Cursor Team-vs-AGENTS runtime E0; private Team Rules dashboards; full Stripe culture page body (timeout); Jeff Bailey / Codexical blogs as design law (E3 only — not promoted); Feathers book body; Alexandria |
| Depth | deep |
| Waves / stop_reason | **W3+2 (residual #2 of +2).** `stop_reason`: **diminishing returns** — neither named GAP closed; new fetches only expand negative-space search log (additional primaries also omit the named stack / AGENTS ladder slot). Optional N-month glance: no normative primary. |
| diminishing | **true** |
| Provenance (optional PROV) | Entity=Theme16 W3+1 confirmed residuals; Activity=W3+2 residual gather 2026-08-02; Agent=residual-gap-closer-w3p2 |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Stop rule: only two open residuals; cite-or-omit; confirm GAP when primary missing |
| Scope boundary | W3+1 §4.1–4.2 / §7 opens only; no rewrite of closed scorecard rows |

## 4. Findings

### 4.1 Residual — Conflict / precedence stack (design/ADR > principles > standards > inferred-from-code)

#### What Toolbelt lean wants (context only — not industry SoT)

Lean host conflict order resembles: **design/ADR > principles > standards > inferred-from-code**. This pass asks whether any **primary or strong secondary** states that (or equivalent) explicit precedence when those layers conflict.

#### Primaries re-checked / newly fetched

- `FACT` [E1] Google eng-practices “Principles”: on **style**, “the style guide is the absolute authority”; on **design**, aspects “are based on underlying principles and should be weighed on those principles.” This is a **domain fence** (style vs design), not a ranked ADR > principles > coding-standards ladder. Same page’s “Resolving Conflicts” escalates to TL / maintainer / Eng Manager — process escalation, not document-layer precedence. [E1: https://google.github.io/eng-practices/review/reviewer/standard.html — accessed 2026-08-02]
- `FACT` [E1] Google eng-practices “What to look for”: if existing code is inconsistent with the style guide, “the style guide is the absolute authority” for required style points; recommendations vs surrounding code are a judgment call. Still style-domain authority, not cross-layer stack vs ADRs/principles docs. [E1: https://google.github.io/eng-practices/review/reviewer/looking-for.html — accessed 2026-08-02]
- `FACT` [E1] MADR project docs define ADR template, status lifecycle language in templates, and scope of architectural / “any” decisions. No section ranks ADRs above foundational principles above coding standards as a conflict resolver. [E1: https://adr.github.io/madr/ — accessed 2026-08-02]
- `FACT` [E1] Azure Well-Architected “Maintain an architecture decision record”: ADRs for architecturally significant choices; append-only / supersede pattern; “Avoid making decision records design guides.” No three-tier precedence vs engineering principles or coding standards. [E1: https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record — accessed 2026-08-02]
- `FACT` [E1] AWS Well-Architected DevOps Guidance **DL.CR.1** Standardize coding practices: coding standards promote consistency; teams may extend; standards “not prevent innovation”; suggest linters / industry guides (PEP8, etc.). No conflict ranking vs design principles or ADRs. [E1: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.1-standardize-coding-practices.html — accessed 2026-08-02]
- `FACT` [E1] AWS Architecture Blog ADR best practices: treat ADRs as “team law” for **architectural decisions**; supersede/link when changing; separate design docs from decisions. Speaks to ADR process authority within architecture decisions — **not** ADR > principles > lintable coding standards. [E1: https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/ — accessed 2026-08-02]

#### Culture / eng-standards near-misses (not the named stack)

- `CLAIM` [E3] Stripe public Operating Principles describe how the company works (users first, craft, etc.); secondary writeups discuss culture vs “best practices.” No verified primary stating ADR/design > eng principles > coding standards conflict ladder. Stripe culture page fetch timed out this pass — do not invent body text. [E3: search hits for https://stripe.com/jobs/culture + Pragmatic Engineer Stripe culture — 2026-08-02]
- `CLAIM` [E3] Netflix techblog “paved road” / Freedom & Responsibility frames optional standards vs autonomy — culture of tooling adoption, not a three-layer doc precedence stack. Discovery only. [E3: Netflix techblog search snippets — 2026-08-02]
- `FACT` [E1] Prior W3+1 host near-miss **koppajs** `DECISION_HIERARCHY.md` (specs → ADRs → ARCHITECTURE → AI constitution → DEVELOPMENT_RULES → …) remains the closest published host ladder; taxonomy still ≠ named “ADR/design > principles > coding standards.” Not re-fetched this pass; cite W3+1. [E1 via W3+1: https://raw.githubusercontent.com/koppajs/koppajs-vite-plugin/main/DECISION_HIERARCHY.md]

#### Disposition

- `GAP` **CONFIRMED GAP.** After W3, W3+1, and this W3+2 expansion (Google eng-practices standard + looking-for; MADR; Azure WAF ADR; AWS DevOps DL.CR.1; AWS Architecture Blog ADR practices; Stripe/Netflix culture searches; prior Cognitect/Thoughtworks/Fowler/koppajs from W3+1), no primary or strong secondary states Toolbelt’s named three-layer conflict stack (design/ADR > principles > standards, with inferred-from-code lowest). Result: **CONFIRMED GAP**.

### 4.2 Residual — Cursor AGENTS.md vs Rules precedence (official docs only)

#### Official docs fetched this pass

- `FACT` [E1] Cursor Rules reference lists four types including **AGENTS.md** (“Simple alternative to `.cursor/rules`”). Precedence sentence: “Rules are applied in this order: **Team Rules → Project Rules → User Rules**. All applicable rules are merged; earlier sources take precedence when guidance conflicts.” **AGENTS.md is not named in that ordered list.** Nested AGENTS: more specific nested files take precedence over parents (AGENTS↔AGENTS only). [E1: https://cursor.com/docs/rules — accessed 2026-08-02]
- `FACT` [E1] Cursor Help “Rules”: same conflict precedence “Team Rules > Project Rules > User Rules”; AGENTS.md section says create root file / use project rules for more control — **no** AGENTS vs Team/Project win-order. CLAUDE.md “read the same way as AGENTS.md” and “always applied” — still no cross-type conflict with Team Rules. [E1: https://cursor.com/help/customization/rules — accessed 2026-08-02]
- `FACT` [E1] Cursor CLI docs: CLI “reads `AGENTS.md` and `CLAUDE.md` at the project root (if present) and applies them as rules **alongside** `.cursor/rules`.” Co-application stated; conflict winner vs Team or Project `.mdc` / `alwaysApply` **not** stated. [E1: https://cursor.com/docs/cli/using — accessed 2026-08-02]
- `FACT` [E1] Cursor Help “Ignore files”: `.cursorignore` / `.gitignore` control indexing and Agent file access; no rule-type precedence involving AGENTS.md vs Team/Project/User. [E1: https://cursor.com/help/customization/ignore-files — accessed 2026-08-02]
- `GAP` Official ignore-file **reference** (`https://cursor.com/docs/reference/ignore-file`) timed out this pass; help page above covers the same topic at help depth. No indication from help text that ignore docs define AGENTS↔rules conflict order.

#### Disposition

- `GAP` **CONFIRMED GAP.** Official Cursor docs (rules reference, help/rules, CLI using, help/ignore-files) still do **not** specify whether `AGENTS.md` overrides or loses to Team Rules, Project `.mdc` (including `alwaysApply: true`), or User Rules on conflicting guidance. Result: **CONFIRMED GAP**.
- `OPEN` Live E0 Cursor session proving AGENTS vs enforced Team rule winner (unchanged; not run).

### 4.3 Optional glance — brownfield N-month recency default

- `GAP` No normative primary found this pass stating a universal **N-month** window as the default for which style era wins in brownfield derive. Search glance: brownfield coding standards + months / recent code / git blame. Leave prior T16H/I / deep-t16i recipe atoms as-is; do not invent a month count.
- **Disposition:** leave alone (no unexpected high-signal close).

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Industry SoT publishes ADR/design > principles > standards ladder | rejected / GAP | Google fence + MADR + Azure/AWS ADR + DevOps coding practices omit named stack |
| H2 | Official Cursor docs place AGENTS in Team→Project→User ladder or define AGENTS win/lose | rejected / GAP | rules + help + CLI “alongside”; AGENTS absent from precedence list |
| H3 | Normative primary states N-month brownfield style-era default | rejected / GAP | optional glance — none |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Style vs design authority | Google: style guide absolute **on style**; design weighed on principles | AWS DL.CR.1: coding standards for consistency, not vs ADR stack | Prefer each E1 in its domain; neither is Toolbelt’s three-tier stack |
| Cursor AGENTS load model | rules.md: AGENTS as alternative; nested specificity | CLI: AGENTS applied **alongside** `.cursor/rules` | Both E1; still no AGENTS↔Team conflict winner |
| ADR “team law” language | AWS Architecture Blog: ADRs as team law for architectural decisions | Toolbelt lean: ADR above principles above standards | Blog law is ADR-process scoped; do not read as cross-layer stack |

## 7. Gaps & OPEN

- `GAP` Named conflict stack design/ADR > principles > coding standards (> inferred) — **CONFIRMED** after W3+2 expanded primary search.
- `GAP` Cursor AGENTS.md vs Team / Project `.mdc` / User / alwaysApply conflict precedence — **CONFIRMED**.
- `OPEN` Live E0 Cursor AGENTS vs enforced Team rule.
- `GAP` Normative N-month brownfield style-era default — untouched / still open (not campaign-blocking for this note).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Toolbelt may **author** an accepted host conflict ladder in design (koppajs shows hosts sometimes publish local hierarchies), but must not cite industry SoT as already defining ADR > principles > standards. Premises: §4.1 GAP + Google domain fence FACTs + Azure/AWS/MADR omissions.
- `INFERENCE` [E4] Until Cursor documents AGENTS in the Team→Project→User ladder (or an explicit “alongside / merge / lose” rule), host bind guidance should treat AGENTS↔Team conflict as **product-undefined** (prefer E0 or conservative “do not rely”). Premises: §4.2 FACTs + GAP.

## 9. Source list (deduped)

1. https://google.github.io/eng-practices/review/reviewer/standard.html — 2026-08-02
2. https://google.github.io/eng-practices/review/reviewer/looking-for.html — 2026-08-02
3. https://adr.github.io/madr/ — 2026-08-02
4. https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record — 2026-08-02
5. https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.1-standardize-coding-practices.html — 2026-08-02
6. https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/ — 2026-08-02
7. https://cursor.com/docs/rules — 2026-08-02
8. https://cursor.com/help/customization/rules — 2026-08-02
9. https://cursor.com/docs/cli/using — 2026-08-02
10. https://cursor.com/help/customization/ignore-files — 2026-08-02
11. https://raw.githubusercontent.com/koppajs/koppajs-vite-plugin/main/DECISION_HIERARCHY.md — via W3+1 (not re-fetched)
12. https://cursor.com/docs/reference/ignore-file — fetch **timeout** 2026-08-02 (not used as FACT body)

## 10. W3+2 residual scorecard

| # | Residual (from W3+1 open) | Result |
|---|---------------------------|--------|
| 1 | Conflict stack ADR/design > principles > standards | **CONFIRMED GAP** |
| 2 | Cursor AGENTS vs Team/Project/User conflict | **CONFIRMED GAP** |

| Field | Value |
|-------|-------|
| Closed any named GAP? | **no** |
| New FACT beyond restating W3+1? | Expanded negative-space primaries only (MADR, Azure WAF ADR, AWS DL.CR.1, AWS ADR blog, Cursor help/ignore) — no disposition change |
| diminishing | **true** |
| Optional N-month glance | no close — left alone |
