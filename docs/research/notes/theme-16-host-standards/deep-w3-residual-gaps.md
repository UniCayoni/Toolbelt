---
title: "Deep W3 — Residual GAP closer (Theme 16)"
status: draft
theme: theme-16-host-standards
created: 2026-08-02
updated: 2026-08-02
depth: deep
wave: W3
authors: [residual-gap-closer-w3]
closes_toward:
  - deep-t16c-principles-exemplars.md
  - deep-t16j-bind-patterns.md
  - deep-t16h-i-brownfield-git.md
  - deep-campaign-board.md
supersedes: null
---

# Deep W3 — Residual GAP closer (Theme 16)

## 1. Scope

- **Question / goal:** First residual wave of `diminishing_returns_plus_2` — close or confirm named P0/P1 residuals only; prefer confirmed GAP over weak E3 spam; do not restate W1 notes.
- **In scope:** (1) agent-loadable separate PRINCIPLES / ENGINEERING_VALUES; (2) CONTRIBUTING → standards/principles links (5+ primaries); (3) conflict stack ADR/design > principles > coding standards; (4) Feathers (legacy) style-guide evolution/deprecate if quick; (5) Cursor AGENTS.md vs rules precedence; (6) optional one a11y/i18n coding-standards exemplar.
- **Out of scope:** Rewriting W1 T16C/T16J/T16H-I notes; locking Toolbelt host shape; exhaustive PRINCIPLES.md census; Alexandria unless high signal (skipped).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-02 |
| Tools used | GitHub MCP `search_code` / `get_file_contents`; WebSearch; WebFetch (Cursor rules.md success; Android/W3C a11y URLs timed out) |
| Corpora / URLs searched | cursor.com/docs/rules.md; GitHub raw contents listed in §9; Feathers *WELC* Pearson sample PDF (index/TOC only); Mozilla firefox-android a11y guide |
| Queries (exact) | GH: `PRINCIPLES.md filename:AGENTS.md`; `filename:ENGINEERING_VALUES.md`; `"style guide" OR styleguide OR "coding standards" OR "code style" filename:CONTRIBUTING.md`; `"see PRINCIPLES" OR "read PRINCIPLES" OR "PRINCIPLES.md" filename:AGENTS.md`; `PRINCIPLES.md OR "engineering principles" OR "coding principles" filename:CONTRIBUTING.md` (0 hits). Web: Cursor AGENTS vs Team/Project precedence; ADR/principles/coding-standards conflict rank; Feathers legacy style-guide deprecate; a11y coding standards exemplars |
| What was *not* searched | Full Feathers book body; private corpora; Alexandria (not high-signal for these residuals); exhaustive CONTRIBUTING→PRINCIPLES frequency study; live Cursor runtime E0 of AGENTS vs Team rule conflict |
| Depth | deep |
| Waves / stop_reason | **W3 (residual #1 of +2).** `stop_reason`: **named GAPs closed or confirmed still open** — (1)(2)(6) closed with new E1 samples; (3)(4)(5) confirmed GAP after targeted primary search (no weak E3 promotion). Not diminishing-only-restate. |
| Provenance (optional PROV) | Entity=Theme16 residual GAPs; Activity=W3 residual gather 2026-08-02; Agent=residual-gap-closer-w3 |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Campaign stop rule: only named residuals; cite-or-omit; confirm GAP when primary missing |
| Scope boundary | Named residuals only; skim prior deep notes GAPs sections (no rewrite) |

## 4. Findings

### 4.1 Residual 1 — Separate PRINCIPLES / ENGINEERING_VALUES agents would load

- `FACT` [E1] **facioquo/stock-indicators-dotnet** root `AGENTS.md` separates philosophy from ops: “See [PRINCIPLES.md](docs/PRINCIPLES.md) for constitutional philosophy and rationale. This file (AGENTS.md) provides operational implementation guidance.” [E1: https://raw.githubusercontent.com/facioquo/stock-indicators-dotnet/5f18d58f5271ca6b4a8dbcc3e02d46e8adf5668e/AGENTS.md — accessed 2026-08-02]
- `FACT` [E1] Same repo `docs/PRINCIPLES.md` is a loadable philosophy/rules file (six named principles + Governance: “**Authority**: Supersedes ad-hoc conventions”). [E1: https://raw.githubusercontent.com/facioquo/stock-indicators-dotnet/5f18d58f5271ca6b4a8dbcc3e02d46e8adf5668e/docs/PRINCIPLES.md — accessed 2026-08-02]
- `FACT` [E1] **dartsim/dart** root `AGENTS.md` mandates separate principles load: “Start every session by reading `docs/ai/principles.md`…”; task table: **Any task** → this file + `docs/ai/principles.md`. [E1: https://raw.githubusercontent.com/dartsim/dart/ef10cb2633b32d2fe061a19d1abd5f7d61561fe8/AGENTS.md — accessed 2026-08-02]
- `FACT` [E1] **dartsim/dart** `docs/ai/principles.md` is an always-loaded axiom pack (“This compact file is loaded for every DART agent session… Keep this file short. It spends always-loaded agent context…”). [E1: https://raw.githubusercontent.com/dartsim/dart/ef10cb2633b32d2fe061a19d1abd5f7d61561fe8/docs/ai/principles.md — accessed 2026-08-02]
- `FACT` [E1] **sustainable-computing-io/kepler** `AGENTS.md` Design Principles section points agents to `docs/developer/design/architecture/principles.md` (nine architectural principles with problem/solution anatomy). [E1: AGENTS.md + principles.md at sha `53620c7c4f916d8e2c9cf47bf0bf9a2b95722fde` — accessed 2026-08-02]
- `FACT` [E1] **bdbch/ai-dotfiles** ships agent-facing `instructions/ENGINEERING_VALUES.md` (values prose: DX, review-every-diff, agents as peers). [E1: https://raw.githubusercontent.com/bdbch/ai-dotfiles/ff2895946be4cea16d35c148eb9247051b4d5d3d/instructions/ENGINEERING_VALUES.md — accessed 2026-08-02]
- `FACT` [E1] GitHub `filename:ENGINEERING_VALUES.md` returns few hits (`total_count` ≈ 10 this pass); true root/path `ENGINEERING_VALUES.md` agent packs are sparse vs `filename:PRINCIPLES.md` abundance noted in W1. [E1: GitHub MCP `search_code` query=`filename:ENGINEERING_VALUES.md` — observed 2026-08-02]
- `INFERENCE` [E4] Separate agent-loadable principles files **exist** (stock-indicators, dart, kepler) as a **pointer-from-AGENTS** pattern; they remain rarer than Core Principles *sections inside* AGENTS.md (W1). Premises: FACTs above + W1 T16C AGENTS-embedding pattern (not restated).
- **Disposition:** **CLOSED** — 3–4 primary separate-file exemplars found (not “confirm rare-only GAP”).

### 4.2 Residual 2 — CONTRIBUTING.md → style guides / standards (5+)

- `FACT` [E1] **k4yt3x/video2x** `CONTRIBUTING.md` § Coding Standards: “C++ code must follow the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)” + clang-format. [E1: sha `7db9c18d…` — accessed 2026-08-02]
- `FACT` [E1] **winegui/WineGUI** `CONTRIBUTING.md` § Coding Standards links Google C++ Style Guide + C++ Core Guidelines + local `.clang-format`. [E1: sha `f10b6e40…` — accessed 2026-08-02]
- `FACT` [E1] **spcl/dace** `CONTRIBUTING.md` § Code Style: “We follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html), with a few notable exceptions…” + pre-commit/yapf. [E1: sha `a7f1669e…` — accessed 2026-08-02]
- `FACT` [E1] **zigpy/zigpy** `CONTRIBUTING.md` developer section: “Recommend read and follow [Google Python Style Guide]…” (+ black/ruff). [E1: sha `8f3a91ee…` — accessed 2026-08-02]
- `FACT` [E1] **carbonetes/diggity** `CONTRIBUTING.md` § Code Style: adhere to standards; “We recommend using [Go's official coding style and conventions](https://google.github.io/styleguide/go/).” [E1: sha `903ee10e…` — accessed 2026-08-02]
- `FACT` [E1] **camel-ai/camel** `CONTRIBUTING.md` code-review checklist: “Style: … take [Google Python Style Guide](…) as reference” (+ Ruff). Also has in-file “Principles” (naming/logging) — standards *and* principles prose in CONTRIBUTING. [E1: sha `7dfa2a75…` — accessed 2026-08-02]
- `GAP` GitHub search for CONTRIBUTING → `PRINCIPLES.md` / “engineering principles” as filename link returned **0** hits this pass. Searched: `PRINCIPLES.md OR "engineering principles" OR "coding principles" filename:CONTRIBUTING.md`. Result: style-guide links dominate; dedicated PRINCIPLES.md pointer from CONTRIBUTING not evidenced in this sample. [E1: GitHub MCP search — 2026-08-02]
- **Disposition:** **CLOSED** for CONTRIBUTING→style-guide/standards pattern (6 primaries). CONTRIBUTING→`PRINCIPLES.md` specifically remains thin (**confirmed GAP** for that sub-pattern).

### 4.3 Residual 3 — Conflict stack ADR/design > principles > coding standards

- `FACT` [E1] Google eng-practices (already in W1; re-checked for stack): on **style**, “the style guide is the absolute authority,” while design weighs “underlying principles” — principles vs style fence, **not** ADR > principles > standards ranking. [E1: https://google.github.io/eng-practices/review/reviewer/standard.html — accessed prior W1 / pattern unchanged]
- `FACT` [E1] AWS Prescriptive Guidance ADR process: accepted ADRs are immutable; code review may reject changes that violate ADRs (reviewer links ADR). Speaks to ADR vs *code*, not a three-tier stack over principles/standards. [E1: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html — accessed via search snippets 2026-08-02]
- `FACT` [E1] stock-indicators `PRINCIPLES.md` Governance: principles “Supersedes ad-hoc conventions” — local principles > ad-hoc, not ADR > principles > lintable standards. [E1: docs/PRINCIPLES.md above]
- `GAP` No primary/secondary found that **ranks** ADR/design docs **above** foundational principles **above** coding standards as a conflict resolution ladder. Searched: web phrases (“principles take precedence”, “ADR takes precedence”, conflict + style guide); GitHub/community hits were agent-file proximity rules or project-over-generic advice, not the named three-layer stack. Result: **confirmed GAP** (prior T16C INFERENCE remains inference-only).
- **Disposition:** **CONFIRMED GAP**.

### 4.4 Residual 4 — Feathers style-guide evolution / deprecate

- `FACT` [E1] Pearson sample pages for Michael C. Feathers *Working Effectively with Legacy Code* include foreword framing “rot” and incremental reverse-entropy via seams/tests; TOC lists class naming conventions etc. — **legacy change / testing**, not coding-standard deprecate/obsolete lifecycle. [E1: https://ptgmedia.pearsoncmg.com/images/9780131177055/samplepages/0131177052.pdf — accessed 2026-08-02]
- `GAP` Quick one-fetch pass did not surface Feathers primary guidance on **style-guide evolution / deprecate patterns** usable for G7. Full book body not retrieved. Result: leave residual **confirmed GAP** (do not invent). W1 H/I ADR + FDG Obsolete + Keep a Changelog patterns remain the citeable deprecate story.
- **Disposition:** **CONFIRMED GAP** (after quick fetch).

### 4.5 Residual 5 — Cursor AGENTS.md vs rules precedence (T16J bind)

- `FACT` [E1] Cursor Rules docs list four types including **AGENTS.md** as “Simple alternative to `.cursor/rules`.” [E1: https://cursor.com/docs/rules.md — accessed 2026-08-02]
- `FACT` [E1] Same page documents scope precedence **only** as: “Rules are applied in this order: **Team Rules → Project Rules → User Rules**. All applicable rules are merged; earlier sources take precedence when guidance conflicts.” **AGENTS.md is not named in that ladder.** [E1: https://cursor.com/docs/rules.md — Team Rules / Precedence — accessed 2026-08-02]
- `FACT` [E1] Nested `AGENTS.md`: “Instructions from nested `AGENTS.md` files are combined with parent directories, with more specific instructions taking precedence.” (AGENTS↔AGENTS only.) [E1: same URL — Nested AGENTS.md — accessed 2026-08-02]
- `CLAIM` [E3] Secondary writeups disagree on where AGENTS sits (e.g. some fold AGENTS into Project Rules; others list AGENTS below User/Legacy). Discovery only — do not elevate over Cursor primary. [E3: design.dev Cursor Rules Guide; voxmedia open-agent-toolkit cursor-rules-files.md — via WebSearch 2026-08-02]
- `GAP` Official Cursor docs still do **not** specify conflict precedence when `AGENTS.md` / nested AGENTS conflicts with Team Rules or Project `.mdc` rules. Searched: full rules.md fetch this pass. Result: **confirmed GAP** (aligns with prior T16J / T4N residual).
- **Disposition:** **CONFIRMED GAP**.

### 4.6 Residual 6 — Optional a11y / i18n coding-standards exemplar

- `FACT` [E1] **mozilla-mobile/firefox-android** `docs/shared/android/accessibility_guide.md` is a project coding/engineering a11y standard: TalkBack testing, `importantForAccessibility`, avoid dual code paths, Accessibility Scanner, automated a11y event tests; links official Android accessibility overview. [E1: https://raw.githubusercontent.com/mozilla-mobile/firefox-android/main/docs/shared/android/accessibility_guide.md — accessed 2026-08-02]
- `GAP` Direct WebFetch of Android developer a11y URLs and W3C WCAG overview timed out this pass; treat as park for primary pin of those vendors (URLs known via Mozilla links / search). i18n coding-standards exemplar not fetched this pass.
- **Disposition:** **CLOSED** for “one a11y exemplar” (Mozilla primary). i18n specifically **parked / OPEN**.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Separate PRINCIPLES files agents load are findable beyond AGENTS-embedded Core Principles | confirmed | stock-indicators, dart, kepler (+ ENGINEERING_VALUES ai-dotfiles) |
| H2 | CONTRIBUTING commonly points to external style guides | confirmed | 6 E1 CONTRIBUTING samples |
| H3 | Industry publishes ADR > principles > standards conflict ladder | rejected / GAP | no primary found |
| H4 | Cursor documents AGENTS vs Team/Project conflict order | rejected / GAP | rules.md omits AGENTS from ladder |
| H5 | Feathers primary closes style-guide deprecate residual in one fetch | rejected / GAP | sample ≠ deprecate lifecycle |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Where AGENTS.md sits in Cursor precedence | Cursor E1: Team→Project→User; AGENTS separate “alternative”; nested AGENTS specificity only | E3 blogs: AGENTS inside Project **or** below User | Prefer E1; leave AGENTS↔Team/Project conflict **OPEN/GAP** |
| Principles vs style authority | Google: style guide absolute on style | stock-indicators: PRINCIPLES supersede ad-hoc | Domain-scoped; not a universal three-tier stack |

## 7. Gaps & OPEN

- `GAP` Ranked conflict stack ADR/design > principles > coding standards — **confirmed** (no primary).
- `GAP` Cursor AGENTS.md vs Team / Project `.mdc` conflict precedence — **confirmed**.
- `GAP` Feathers primary on style-guide deprecate/evolution — **confirmed** after quick fetch.
- `GAP` CONTRIBUTING → `PRINCIPLES.md` link frequency — still thin (0 search hits this pass).
- `OPEN` i18n coding-standards exemplar (a11y closed via Mozilla).
- `OPEN` Live E0 Cursor session proving AGENTS vs enforced Team rule winner.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Host shape for principles can cite **AGENTS pointer → separate PRINCIPLES** (dart/stock-indicators) as a first-class pattern alongside AGENTS-embedded Core Principles — without claiming it is the majority pattern. Premises: §4.1 FACTs; W1 rarity INFERENCE.
- `INFERENCE` [E4] CONTRIBUTING→external style guide is a durable bind pattern for humans; agent packs more often bind via AGENTS→STYLE/STANDARDS (W1 T16J) — complementary channels. Premises: §4.2 + prior T16J pointers.
- `INFERENCE` [E4] Do **not** lock a Toolbelt conflict stack from industry SoT this campaign; design must invent/accept its own ladder if needed. Premises: §4.3 GAP.

## 9. Source list (deduped)

1. https://cursor.com/docs/rules.md — 2026-08-02
2. https://raw.githubusercontent.com/facioquo/stock-indicators-dotnet/5f18d58f5271ca6b4a8dbcc3e02d46e8adf5668e/AGENTS.md
3. https://raw.githubusercontent.com/facioquo/stock-indicators-dotnet/5f18d58f5271ca6b4a8dbcc3e02d46e8adf5668e/docs/PRINCIPLES.md
4. https://raw.githubusercontent.com/dartsim/dart/ef10cb2633b32d2fe061a19d1abd5f7d61561fe8/AGENTS.md
5. https://raw.githubusercontent.com/dartsim/dart/ef10cb2633b32d2fe061a19d1abd5f7d61561fe8/docs/ai/principles.md
6. https://github.com/sustainable-computing-io/kepler (AGENTS.md + docs/developer/design/architecture/principles.md @ 53620c7c…)
7. https://raw.githubusercontent.com/bdbch/ai-dotfiles/ff2895946be4cea16d35c148eb9247051b4d5d3d/instructions/ENGINEERING_VALUES.md
8. https://github.com/k4yt3x/video2x/blob/7db9c18d6278bbad9c3eda0e4e4ae210f9a688eb/CONTRIBUTING.md
9. https://github.com/winegui/WineGUI/blob/f10b6e4065e22bc156d4dc0c140f5e8873efacc1/CONTRIBUTING.md
10. https://github.com/spcl/dace/blob/a7f1669e821ddbb88fb906bd7e985fe098df5517/CONTRIBUTING.md
11. https://github.com/zigpy/zigpy/blob/8f3a91ee8327ce7ab20003927fa05ae8d4725ef6/CONTRIBUTING.md
12. https://github.com/carbonetes/diggity/blob/903ee10ed2f64aeff3d13838f78ee886f32869c5/CONTRIBUTING.md
13. https://github.com/camel-ai/camel/blob/7dfa2a75a7b17f35a91c4841c52877e1272cd559/CONTRIBUTING.md
14. https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html
15. https://google.github.io/eng-practices/review/reviewer/standard.html
16. https://ptgmedia.pearsoncmg.com/images/9780131177055/samplepages/0131177052.pdf
17. https://raw.githubusercontent.com/mozilla-mobile/firefox-android/main/docs/shared/android/accessibility_guide.md

## 10. W3 residual scorecard

| # | Residual | Result |
|---|----------|--------|
| 1 | Separate PRINCIPLES / ENGINEERING_VALUES for agents | **CLOSED** (4 E1 exemplars) |
| 2 | CONTRIBUTING → style guides / standards (5+) | **CLOSED** (6 E1); CONTRIBUTING→PRINCIPLES.md **CONFIRMED GAP** |
| 3 | Conflict stack ADR > principles > standards | **CONFIRMED GAP** |
| 4 | Feathers style-guide evolve/deprecate | **CONFIRMED GAP** |
| 5 | Cursor AGENTS vs rules precedence | **CONFIRMED GAP** |
| 6 | a11y / i18n exemplar | **CLOSED** (a11y Mozilla); i18n **OPEN/park** |
