---
title: "Deep W3+1 — Residual confirmed-GAP closer (Theme 16)"
status: draft
theme: theme-16-host-standards
created: 2026-08-02
updated: 2026-08-02
depth: deep
wave: W3+1
authors: [residual-gap-closer-w3p1]
closes_toward:
  - deep-w3-residual-gaps.md
  - deep-t16c-principles-exemplars.md
  - deep-t16j-bind-patterns.md
  - deep-t16h-i-brownfield-git.md
supersedes: null
---

# Deep W3+1 — Residual confirmed-GAP closer (Theme 16)

## 1. Scope

- **Question / goal:** First of two required diminishing-return passes under `diminishing_returns_plus_2` — attack only W3 **confirmed-open** residuals; close with E1 or reconfirm GAP with expanded search log.
- **In scope:** (1) conflict stack ADR/design > principles > coding standards; (2) Cursor AGENTS.md vs Team/Project/User precedence; (3) CONTRIBUTING.md → PRINCIPLES.md (≥2 real links); (4) style-guide deprecate/obsolete lifecycle (broaden beyond Feathers).
- **Out of scope:** Restating W3 closed residuals (separate PRINCIPLES agent packs; CONTRIBUTING→style guides; a11y exemplar); locking Toolbelt host shape; Alexandria.

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-02 |
| Tools used | GitHub MCP `search_code` / `get_file_contents`; WebSearch; WebFetch (Cursor rules + CLI; Google eng-practices; Cognitect Nygard; Thoughtworks Radar; Fowler ADR bliki; Google JS styleguide; PEP 8; Google docs style What’s new; koppajs DECISION_HIERARCHY raw) |
| Corpora / URLs searched | cursor.com/docs/rules.md; cursor.com/docs/cli/using; google.github.io/eng-practices/review/reviewer/standard.html; cognitect.com ADR post; thoughtworks.com lightweight ADR radar; martinfowler.com/bliki/ArchitectureDecisionRecord.html; google.github.io/styleguide/jsguide.html; peps.python.org/pep-0008/; developers.google.com/style/whats-new; raw koppajs DECISION_HIERARCHY; GH CONTRIBUTING hits listed in §9 |
| Queries (exact) | GH: `PRINCIPLES.md filename:CONTRIBUTING.md`; `"Decision Hierarchy" OR "precedence" ADR principles filename:DECISION_HIERARCHY.md`. Web: ADR vs style guide / principles conflict precedence; Thoughtworks/Nygard ADR; Cursor AGENTS Team Project precedence; Google/PEP/LLVM style guide deprecated obsolete changelog |
| What was *not* searched | Full Feathers book body (W3 miss; intentionally replaced by primary style-guide corpus); live Cursor E0 Team-vs-AGENTS conflict experiment; private Team Rules dashboards; Alexandria |
| Depth | deep |
| Waves / stop_reason | **W3+1 (residual #1 of +2).** `stop_reason`: **closed named GAPs** — CONTRIBUTING→PRINCIPLES.md and style-guide deprecate/obsolete lifecycle closed with new E1; conflict-stack and Cursor AGENTS↔Team/Project conflict remain **CONFIRMED GAP** after harder primary search. **Not diminishing** (not only restated / failed-all). |
| Provenance (optional PROV) | Entity=Theme16 W3 confirmed residuals; Activity=W3+1 residual gather 2026-08-02; Agent=residual-gap-closer-w3p1 |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Stop rule: only named open residuals; cite-or-omit; confirm GAP when primary missing |
| Scope boundary | W3 §7 confirmed opens only; skim W3 Method/GAPs (no rewrite of closed scorecard rows) |

## 4. Findings

### 4.1 Residual — Conflict stack ADR/design > principles > coding standards

- `FACT` [E1] Google eng-practices “Principles”: on **style**, “the style guide is the absolute authority”; on **design**, aspects “are based on underlying principles and should be weighed on those principles.” Domain fence (style vs design), **not** a ranked ADR > principles > coding-standards ladder. [E1: https://google.github.io/eng-practices/review/reviewer/standard.html — accessed 2026-08-02]
- `FACT` [E1] Michael Nygard Cognitect ADR primary defines Status including “deprecated” / “superseded” with replacement reference; records architecturally significant decisions. No ranking vs foundational principles or coding standards. [E1: https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — accessed 2026-08-02]
- `FACT` [E1] Thoughtworks Technology Radar (Lightweight Architecture Decision Records, Adopt): capture important decisions with context/consequences; prefer source control over wiki. No conflict stack vs principles/style guides. [E1: https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records — accessed 2026-08-02]
- `FACT` [E1] Martin Fowler ADR bliki: accepted ADRs immutable; change via superseding ADR. No three-tier precedence over principles/standards. [E1: https://martinfowler.com/bliki/ArchitectureDecisionRecord.html — accessed 2026-08-02]
- `FACT` [E1] Host example **koppajs/koppajs-vite-plugin** `DECISION_HIERARCHY.md` ranks: approved specs → accepted ADRs → ARCHITECTURE → AI_CONSTITUTION / instructions → DEVELOPMENT_RULES → … → CONTRIBUTING → informational docs. Near-miss **host** conflict ladder (ADR above development rules), but taxonomy ≠ named “ADR/design > principles > coding standards.” [E1: https://raw.githubusercontent.com/koppajs/koppajs-vite-plugin/main/DECISION_HIERARCHY.md — accessed 2026-08-02]
- `GAP` No Thoughtworks / Nygard / Fowler / Google eng-practices primary states the **named** three-layer stack ADR/design > foundational principles > coding standards as a universal conflict resolver. Searched: eng-practices standard.html; Cognitect ADR; Thoughtworks Radar blip; Fowler ADR; web phrases on ADR/principles/style precedence; GH `DECISION_HIERARCHY.md` (koppajs near-miss only). Result: **CONFIRMED GAP** (prior T16C INFERENCE stays inference-only).
- **Disposition:** **CONFIRMED GAP**.

### 4.2 Residual — Cursor AGENTS.md vs Team / Project / User rules precedence

- `FACT` [E1] Cursor Rules docs list four types including **AGENTS.md** (“Simple alternative to `.cursor/rules`”). Precedence sentence names only: “Rules are applied in this order: **Team Rules → Project Rules → User Rules**. All applicable rules are merged; earlier sources take precedence when guidance conflicts.” **AGENTS.md is not in that ordered list.** [E1: https://cursor.com/docs/rules.md — accessed 2026-08-02]
- `FACT` [E1] Nested AGENTS only: “Instructions from nested `AGENTS.md` files are combined with parent directories, with more specific instructions taking precedence.” (AGENTS↔AGENTS.) [E1: same URL — Nested AGENTS.md — accessed 2026-08-02]
- `FACT` [E1] Cursor CLI docs: CLI “reads `AGENTS.md` and `CLAUDE.md` at the project root (if present) and applies them as rules **alongside** `.cursor/rules`.” States co-application, **not** win-order vs Team or Project `.mdc` on conflict. [E1: https://cursor.com/docs/cli/using — accessed 2026-08-02]
- `GAP` Official Cursor docs (rules.md + cli/using this pass) still do **not** specify conflict precedence when `AGENTS.md` conflicts with Team Rules or Project `.mdc` rules. Result: **CONFIRMED GAP**.
- `OPEN` Live E0 Cursor session proving AGENTS vs enforced Team rule winner.
- **Disposition:** **CONFIRMED GAP**.

### 4.3 Residual — CONTRIBUTING.md → PRINCIPLES.md (≥2)

- `FACT` [E1] **spiceai/spiceai** root `CONTRIBUTING.md` § “Follow principles and guidelines” links `[Principles](/docs/PRINCIPLES.md)` (alongside Style Guide). Target `docs/PRINCIPLES.md` exists (“Spice.ai First Principles”). [E1: CONTRIBUTING.md + docs/PRINCIPLES.md @ sha `618bfb61d25aa62cc9b207f96e00a62b504c4cdf` — accessed 2026-08-02]
- `FACT` [E1] **huggingface/OpenEnv** root `CONTRIBUTING.md` Quick Links: “**Design principles**: See [.claude/docs/PRINCIPLES.md](.claude/docs/PRINCIPLES.md)”. Target exists (OpenEnv Design Principles / Core Principles from RFC 000). [E1: CONTRIBUTING.md + `.claude/docs/PRINCIPLES.md` @ sha `024eedc90305cc8bd7a5b44f44d1b987102e957b` — accessed 2026-08-02]
- `FACT` [E1] **foambubble/foam** `CONTRIBUTING.md` recommends reading `[Principles](docs/principles.md)` — “guiding principles behind Foam.” Target `docs/principles.md` exists. [E1: CONTRIBUTING.md + docs/principles.md @ sha `6635f557ae4e214f872d75f728880c0970d9f6a8` — accessed 2026-08-02]
- `FACT` [E1] Broader GH `PRINCIPLES.md filename:CONTRIBUTING.md` returns many hits (`total_count` ≈ 702 this pass); W3’s narrower 0-hit query under-sampled this pattern. [E1: GitHub MCP `search_code` query=`PRINCIPLES.md filename:CONTRIBUTING.md` — observed 2026-08-02]
- `CLAIM` [E3] Some CONTRIBUTING hits mention `PRINCIPLES.md` without a resolvable file at expected path (e.g. Devin-AXIS/iPolloWork CONTRIBUTING text vs missing root PRINCIPLES.md this fetch) — discovery only; do not count as bind exemplars. [E3: get_file_contents miss — 2026-08-02]
- **Disposition:** **CLOSED** — ≥2 verified CONTRIBUTING→principles-file links (spiceai, OpenEnv, foam).

### 4.4 Residual — Style-guide deprecate / obsolete lifecycle (broaden beyond Feathers)

- `FACT` [E1] **Google JavaScript Style Guide** opens with whole-guide lifecycle notice: “Please note: This guide is no longer being updated. Google recommends migrating to TypeScript, and following the TypeScript guide.” [E1: https://google.github.io/styleguide/jsguide.html — accessed 2026-08-02]
- `FACT` [E1] **PEP 8** Introduction: “This style guide evolves over time as additional conventions are identified and past conventions are rendered obsolete by changes in the language itself.” Also: project-specific guides take precedence on conflict for that project. [E1: https://peps.python.org/pep-0008/ — accessed 2026-08-02]
- `FACT` [E1] **Google developer documentation style guide** maintains a dated “What’s new” changelog of significant guidance changes (additions, softens, word-list updates) — explicit rule/guidance evolution surface for a primary style corpus. [E1: https://developers.google.com/style/whats-new — accessed 2026-08-02]
- `FACT` [E1] Nygard ADR Status “deprecated” / “superseded” is **ADR** lifecycle (already in W1 H/I), not a coding style-guide rule deprecate pattern — cited only to keep domains distinct. [E1: Cognitect URL above]
- `GAP` Feathers *WELC* primary on style-guide deprecate remains unclosed (W3); this pass **replaced** that miss with Google JS / PEP 8 / Google docs-style changelog primaries rather than re-fetching Feathers.
- **Disposition:** **CLOSED** for “primary style guide with deprecate/obsolete/changelog of rules” (Google JS deprecate-guide; PEP 8 obsolete-conventions language; Google docs style What’s new).

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Industry SoT publishes ADR > principles > standards ladder | rejected / GAP | Google fence + ADR literature + koppajs near-miss ≠ named stack |
| H2 | Cursor docs place AGENTS in Team→Project→User ladder | rejected / GAP | rules.md + CLI “alongside” only |
| H3 | ≥2 real CONTRIBUTING→PRINCIPLES(.md) binds exist | confirmed | spiceai, OpenEnv, foam |
| H4 | Primary style guides document deprecate/obsolete/changelog | confirmed | Google JS; PEP 8; Google docs What’s new |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Doc conflict ladders | Google: style absolute on style; principles weigh design | koppajs: specs/ADRs above AI constitution / development rules | Prefer E1 each in domain; neither is Toolbelt’s named three-tier stack |
| Cursor AGENTS load model | rules.md: AGENTS as alternative; nested specificity | CLI: AGENTS applied as rules **alongside** `.cursor/rules` | Both E1; still no AGENTS↔Team conflict winner |

## 7. Gaps & OPEN

- `GAP` Named conflict stack ADR/design > principles > coding standards — **CONFIRMED** after W3+1 harder search.
- `GAP` Cursor AGENTS.md vs Team / Project `.mdc` conflict precedence — **CONFIRMED**.
- `OPEN` Live E0 Cursor AGENTS vs enforced Team rule.
- `OPEN` Feathers primary on style-guide deprecate (parked; superseded for campaign purposes by Google/PEP exemplars).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] CONTRIBUTING→PRINCIPLES is a real human-facing bind pattern (not only AGENTS→PRINCIPLES). Premises: §4.3 FACTs.
- `INFERENCE` [E4] Style-standard evolution can cite **whole-guide deprecate** (Google JS), **in-guide obsolete conventions** (PEP 8), and **dated guidance changelog** (Google docs style) — complementary to ADR Deprecated/Superseded. Premises: §4.4 FACTs.
- `INFERENCE` [E4] Do **not** lock Toolbelt conflict stack from industry SoT; optional design may invent an accepted ladder (koppajs shows hosts sometimes publish local hierarchies). Premises: §4.1 GAP + koppajs FACT.

## 9. Source list (deduped)

1. https://google.github.io/eng-practices/review/reviewer/standard.html — 2026-08-02
2. https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — 2026-08-02
3. https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records — 2026-08-02
4. https://martinfowler.com/bliki/ArchitectureDecisionRecord.html — 2026-08-02
5. https://raw.githubusercontent.com/koppajs/koppajs-vite-plugin/main/DECISION_HIERARCHY.md — 2026-08-02
6. https://cursor.com/docs/rules.md — 2026-08-02
7. https://cursor.com/docs/cli/using — 2026-08-02
8. https://github.com/spiceai/spiceai/blob/618bfb61d25aa62cc9b207f96e00a62b504c4cdf/CONTRIBUTING.md
9. https://github.com/spiceai/spiceai/blob/618bfb61d25aa62cc9b207f96e00a62b504c4cdf/docs/PRINCIPLES.md
10. https://github.com/huggingface/OpenEnv/blob/024eedc90305cc8bd7a5b44f44d1b987102e957b/CONTRIBUTING.md
11. https://github.com/huggingface/OpenEnv/blob/024eedc90305cc8bd7a5b44f44d1b987102e957b/.claude/docs/PRINCIPLES.md
12. https://github.com/foambubble/foam/blob/6635f557ae4e214f872d75f728880c0970d9f6a8/CONTRIBUTING.md
13. https://github.com/foambubble/foam/blob/6635f557ae4e214f872d75f728880c0970d9f6a8/docs/principles.md
14. https://google.github.io/styleguide/jsguide.html — 2026-08-02
15. https://peps.python.org/pep-0008/ — 2026-08-02
16. https://developers.google.com/style/whats-new — 2026-08-02

## 10. W3+1 residual scorecard

| # | Residual (from W3 open) | Result |
|---|-------------------------|--------|
| 1 | Conflict stack ADR > principles > standards | **CONFIRMED GAP** |
| 2 | Cursor AGENTS vs Team/Project/User conflict | **CONFIRMED GAP** |
| 3 | CONTRIBUTING → PRINCIPLES.md (≥2) | **CLOSED** (3 verified) |
| 4 | Style-guide deprecate/obsolete lifecycle | **CLOSED** (Google JS + PEP 8 + docs What’s new) |

| Field | Value |
|-------|-------|
| Closed any named GAP? | **yes** (3, 4) |
| diminishing | **false** |
