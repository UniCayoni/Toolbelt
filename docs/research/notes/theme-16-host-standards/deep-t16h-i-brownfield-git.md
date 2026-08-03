---
title: "Deep T16H/I — Brownfield derive, git recency, dual eras, deprecate"
status: draft
theme: theme-16-host-standards
created: 2026-08-02
updated: 2026-08-02
depth: deep
track: T16H/I
authors: [research-gatherer]
supersedes: null
closes_gaps: [G3, G7, G8]
deepens: docs/research/notes/theme-16-host-standards/t16h-i-lifecycle-brownfield.md
---

# Deep T16H/I — Brownfield derive + git/history + dual eras + deprecate

**Using `research-protocol`.**

## 1. Scope

- **Question / goal:** Close campaign GAPs **G3** (git/history recency recipe), **G7** (evolution / deprecate / obsolete patterns), **G8** (two eras of style in one repo) for Theme 16 brownfield derive — without inventing Toolbelt law.
- **In scope:** Literature/practice for extracting conventions from existing code; git blame/log/churn as recency signals; dual-era strategies; deprecate/obsolete patterns for standards; local E0 relative to Toolbelt + normal-wave note.
- **Out of scope:** Auto-promoting inferred patterns to SoT; locking a Toolbelt-universal style guide; running host-repo churn experiments as acceptance criteria; ceremony/CI as standards content.
- **Comprehension goal type:** reuse / adaptive (method feedstock for later design).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-02 |
| Tools used | Alexandria `rag_query`; WebSearch; WebFetch; local Grep/Read of Theme 16 notes + Toolbelt recon skill/template |
| Corpora / URLs searched | Alexandria `software_engineering`, `ai_llm_agents`; Black intro guide; ESLint bulk suppressions; git-blame(1); GitHub viewing-a-file; Cognitect/Nygard ADR; understandlegacycode hotspots; Prettier ignore/install; community extract tools (discovery only) |
| Queries (exact) | See §9; Alexandria: brownfield conventions extract; git blame churn; deprecated obsolete style guides; brownfield derive agents; legacy strangler/Feathers |
| What was *not* searched | Full Feathers *Working Effectively with Legacy Code* primary PDF; CodeScene/Code Climate product docs deep-read; GitHub org STANDARDS.md pack sampling (G4); runtime E0 churn run on Toolbelt git history |
| Depth | deep |
| Waves / stop_reason | **W1** primary tooling docs (Git, Black, ESLint, GitHub, Nygard, FDG Obsolete via Alexandria). **W2** corroboration (Fowler refactoring/legacy via Alexandria; hotspot blogs E3; community convention-extract tools E3). **Stop:** named G3/G7/G8 have citeable building blocks + a labeled proposed recipe; further search would mostly restate E3 extract-tool marketing. Residual GAPs listed. `stop_reason`: diminishing returns on G3 recipe atoms (primary + E3 recipes cited; no single canonical “style-era winner” SoT found). |
| Provenance (optional PROV) | Entity=Theme16 brownfield method; Activity=this deep gather; Agent=research-gatherer; wasDerivedFrom=t16h-i-lifecycle-brownfield + campaign-brief + deep-campaign-board |

## 3. Strategy (workspace)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Deep gatherer note: systematic web/RAG for G3/G7/G8; as-needed local E0 against Toolbelt recon + Theme 16 notes |
| Scope boundary | Theme 16 notes under `docs/research/notes/theme-16-host-standards/`; Toolbelt `research-codebase-recon` skill + checklist; no product code changes |

## 4. Findings

### 4.1 Extracting conventions from existing codebases (brownfield)

- `FACT` [E2] Maintainers routinely rewrite or adapt contributions so code adheres to project coding standards and style; following existing project conventions helps new contributors and converges old and new code. Quote: “follow conventions used in an existing project… helps the project converge code, both old and new.” [E2: Alexandria corpus=`software_engineering` source=`Framework Design Guidelines…` chunk_id=`95542d0ca16cd64a8670970c` query=`deprecated obsolete coding standards style guide changelog`]
- `FACT` [E2] Fowler: when working legacy, prefer improving areas visited frequently rather than boiling the ocean — payoff tracks visit frequency. Quote: “I’ll do more refactoring in areas I visit frequently.” [E2: Alexandria corpus=`software_engineering` source=`Refactoring (Fowler 2018)` chunk_id=`631cbc7d42c249cf1648e534` query=`Working Effectively with Legacy Code…`]
- `FACT` [E2] Fowler points readers to Feathers *Working Effectively with Legacy Code* for getting untested legacy under test via seams (secondary pointer in corpus; Feathers text itself not retrieved this pass). [E2: same chunk_id=`631cbc7d42c249cf1648e534`]
- `FACT` [E2] Strangler Fig: build around edges of an old system, gradually intercept/replace until old can be switched off — gradual dual-system coexistence. [E2: Alexandria corpus=`software_engineering` source=`Architecture Patterns with Python` chunk_id=`2f484602fd6a7cc8386079b5` query=`…strangler fig…`]
- `CLAIM` [E3] Community tools advertise AST/static extraction of naming, architecture, error-handling, and confidence-scored conventions into AGENTS.md / Cursor rules / CLAUDE.md (ez-context, codespec, legacy-rule-miner, codebase-archaeologist). Discovery only — no Toolbelt lock. [E3: https://github.com/ezcorp-org/ez-context — accessed 2026-08-02; https://github.com/ralf9090/codespec — accessed 2026-08-02]
- `CLAIM` [E3] Normal-wave lean (prior note): prefer config files (eslint/prettier) as high-confidence signals; AST/stats for implicit patterns; document majority vs conflict boundaries with evidence. [E3 via prior draft: `t16h-i-lifecycle-brownfield.md` — not re-accepted here]
- `INFERENCE` [E4] “Code as documentation of norms” is real practice (match existing project culture; visit-frequency bias; strangler coexistence) but **observed majority ≠ accepted standard** until human accept — aligns with Theme 16 fence. Premises: FDG foreword FACT; campaign-brief brownfield fence; draft≠SoT.
- `GAP` No peer-reviewed / primary “brownfield standards derivation protocol” found that specifies exact sample sizes, confidence thresholds, or git-window defaults as normative law. Searched: web + Alexandria software_engineering. Result: practice fragments + tool marketing.

### 4.2 Git / history as recency signal (closes G3 atoms)

- `FACT` [E1] `git blame` annotates each line with the revision that last modified it; supports `--since=<date>` and revision ranges (e.g. `git blame --since=3.weeks -- foo`); lines unchanged since the range boundary are attributed to that boundary. [E1: https://www.kernel.org/pub/software/scm/git/docs/git-blame.html — accessed 2026-08-02]
- `FACT` [E1] Git ≥2.23: `--ignore-rev` / `--ignore-revs-file` skip listed revisions when assigning blame; config `blame.ignoreRevsFile`; ignored lines attributed to prior meaningful revision. [E1: same git-blame(1)]
- `FACT` [E1] Black’s official migration guide: after a bulk reformat commit, put full 40-char SHA(s) in `.git-blame-ignore-revs`; optional `git config blame.ignoreRevsFile .git-blame-ignore-revs`. [E1: https://black.readthedocs.io/en/stable/guides/introducing_black_to_your_project.html — accessed 2026-08-02]
- `FACT` [E1] GitHub blame UI hides revisions listed in repo-root `.git-blame-ignore-revs` by default; documents recommended comment+SHA file shape. [E1: https://docs.github.com/en/repositories/working-with-files/using-files/viewing-a-file — accessed 2026-08-02]
- `CLAIM` [E3] Hotspot practice: limit churn analysis to ~last 12 months; use `git log --format=format: --name-only --since=12.month` then count/sort top files; combine with complexity; prioritize high-churn+high-complexity; leave stable complex files alone (Sandi Metz: “If the code never changes, it’s not costing us money”). [E3: https://understandlegacycode.com/blog/focus-refactoring-with-hotspots-analysis/ — accessed 2026-08-02 — community blog; not primary SoT]
- `CLAIM` [E3] Same churn recipe restated for “reading new codebases” (1-year window, top-N files). [E3: https://paulund.co.uk/notebook/git/git-commands-for-reading-new-codebases/ — accessed 2026-08-02]
- `CLAIM` [E3] Agent-oriented git-intel tools weight recent changes higher (e.g. repo-intel hotspot score with ~90-day recency window relative to last commit). Discovery. [E3: https://github.com/agent-sh/repo-intel — accessed 2026-08-02]
- `FACT` [E2] RSE Python textbook: `git blame` line output includes commit id, author, when modified, and line content; does not report removed lines. [E2: Alexandria corpus=`software_engineering` source=`Research Software Engineering with Python` chunk_id=`7388699fc32b3f8f1157f0bc` query=`git blame log history churn…`]
- `INFERENCE` [E4] Recency for **style-era** decisions should weight (a) paths with recent churn, (b) line ages via blame/`--since`, (c) config/tooling files as high-confidence — **not** whole-repo historical majority. Premises: hotspot E3; git blame E1; FDG converge-old-and-new E2; campaign “legacy ≠ SoT”.
- `GAP` No primary source found that states a normative default window (e.g. “N months”) specifically for **coding-standard derivation** (as opposed to tech-debt hotspot prioritization). Searched: web + Alexandria. Result: 12-month / 90-day appear as E3 practice heuristics only.
- `OPEN` Whether Toolbelt should hard-code a recency window vs require host-declared window in the derive profile.

### 4.3 Two eras in one repo (closes G8)

- `FACT` [E1] ESLint bulk suppressions: enable rule as `"error"`, then `eslint --fix --suppress-all` (or `--suppress-rule`) to record existing violations in `eslint-suppressions.json`; new violations still fail; prune with `--prune-suppressions`. Explicit goal: enforce for new code while addressing legacy at own pace. [E1: https://eslint.org/docs/latest/use/suppressions — accessed 2026-08-02]
- `FACT` [E1] Black recommends one massive reformat commit + `.git-blame-ignore-revs` so history/blame remain usable across the style-era boundary. [E1: Black introducing guide — same URL]
- `FACT` [E1] Prettier documents `.prettierignore` (gitignore syntax) and default respect for `.gitignore` so formatting can exclude trees; supports incremental ignore of paths not yet migrated. [E1: https://prettier.io/docs/ignore — accessed 2026-08-02]
- `CLAIM` [E3] Pre-bulk-suppressions practice: lint only files changed vs main (`git diff … --name-only` piped to eslint) so touched files must clean up — gradual improvement without boiling the ocean. [E3: https://stricker.digital/posts/integrating-eslint-into-a-legacy-codebase/ — accessed 2026-08-02]
- `CLAIM` [E3] “Lint to the Future” / seatbelt-style tools: freeze baseline violations, prevent new ones, track debt down over time. [E3: https://mainmatter.com/blog/2025/03/03/lttf-process/ — accessed 2026-08-02; eslint-seatbelt npm discovery]
- `FACT` [E2] Parallel change / expand-contract (Fowler): introduce new field/API alongside old, migrate readers gradually, remove old later — general dual-era coexistence pattern beyond style. [E2: Alexandria corpus=`software_engineering` source=`Refactoring (Fowler 2018)` chunk_id=`86d890eefd7b540f82162849` query=`…legacy…`]
- `INFERENCE` [E4] Documented dual-era toolkit for hosts: (1) suppress/baseline old lint debt, (2) ignore/quarantine legacy dirs from formatter, (3) optional big-bang format + blame-ignore-revs, (4) touch-to-clean (lint changed files), (5) ADR/status for which era is “current.” Premises: ESLint/Black/Prettier E1; E3 blogs; Nygard status §4.4.
- `GAP` No Toolbelt-local dual-era profile field names or templates yet (design after accept).

### 4.4 Deprecate / obsolete standards (closes G7)

- `FACT` [E1] Nygard ADR status: proposed → accepted; later may be **deprecated** or **superseded** with reference to replacement; keep old record; do not reuse numbers. [E1: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions — accessed 2026-08-02]
- `FACT` [E2] Framework Design Guidelines 3e ships **Appendix B: Obsolete Guidance** — archives guidance no longer generally applicable; each archived section has a “Why this is Here” marker; modified-but-still-active guidance is *not* dumped to the appendix. [E2: Alexandria corpus=`software_engineering` source=`Framework Design Guidelines…` chunk_id=`6545c48b1c5e2d859bdb9731` query=`deprecated obsolete…`]
- `FACT` [E2] FDG editions add cloud-era guidelines while retaining obsolete appendix — standards are living documents across editions. [E2: Alexandria chunk_id=`95542d0ca16cd64a8670970c` + preface chunk_id=`6fe850ffc19e0fa77be3ae05`]
- `FACT` [E1] Keep a Changelog: group changes including **Deprecated** before **Removed** so consumers meet the warning first. [E1: prior Toolbelt Theme 3 note citing https://keepachangelog.com/en/1.1.0/ — corroborated pattern; not re-fetched this pass]
- `FACT` [E0] Toolbelt ADR template already uses `proposed | accepted | deprecated | superseded`. [E0: `docs/templates/adr-minimal.md` observed 2026-08-02]
- `INFERENCE` [E4] Standards lifecycle should mirror ADR/changelog discipline: mark rules **deprecated** with reason + successor; keep obsolete appendix or changelog of standards; never silent-delete active guidance that agents might still retrieve. Premises: Nygard E1; FDG Obsolete E2; Keep a Changelog E1; Theme 2 status metadata patterns.
- `OPEN` Whether host standards profiles use ADR-like status per rule, a single profile changelog, or an “Obsolete” appendix section (design choice).

### 4.5 Local E0 — Toolbelt / host patterns (deepens normal note)

- `FACT` [E0] Campaign brief (accepted scope): brownfield derive via recon + history with **recency/conflict gates**; “observed culture in code ≠ principle until human accept + recency”; no silent auto-apply. [E0: `docs/research/notes/theme-16-host-standards/campaign-brief.md`]
- `FACT` [E0] Deep board names G3/G7/G8 explicitly; normal wave left git recipe as GAP. [E0: `deep-campaign-board.md`; `t16h-i-lifecycle-brownfield.md`]
- `FACT` [E0] `research-codebase-recon` skill + Theme 1 recon framing emphasize structure, locate→view, conventions in instruction files — **no** checklist step for git log/blame/churn/recency windows found in skill body or `docs/templates/codebase-reconnaissance.md` (grep 2026-08-02). [E0: plugin skill path; template path]
- `FACT` [E0] Toolbelt repo has **no** `.git-blame-ignore-revs` file (glob 2026-08-02).
- `FACT` [E0] T16C lean conflict stack already places inferred-from-code below accepted design/principles/standards and marks it proposed. [E0: `t16c-foundational-principles.md`]
- `INFERENCE` [E4] Closing G3 in product terms likely means **extending** brownfield derive (future `author-standards` mode or recon companion step) with history/recency — not assuming recon already does it. Premises: E0 recon absence; campaign intent.
- `GAP` No E0 of a host already using Toolbelt brownfield-derive end-to-end (skill not built). Searched: Theme 16 notes + skills. Result: intent only.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Hot-path majority + recent blame beats whole-repo historical majority for style-era | confirmed (as practice lean) | Hotspot E3; Fowler visit-frequency E2; campaign recency fence |
| H2 | Dual-era is best handled by suppress/ignore + optional format wave, not silent rewrite of law | confirmed | ESLint/Black/Prettier E1 |
| H3 | Deprecate patterns for standards should copy ADR + Obsolete appendix + changelog Deprecated | confirmed (pattern) | Nygard E1; FDG E2; Keep a Changelog E1 |
| H4 | A single universal N-month window is already industry SoT | rejected | Only E3 heuristics; GAP remains |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Big-bang format vs gradual lint | Black: one massive reformat + ignore-revs [E1] | ESLint suppressions / touch-to-clean [E1/E3] | Not contradictory: format waves vs rule enablement are different levers; hosts may combine. Leave choice **OPEN** for design. |
| Recency window length | ~12 months (hotspot blogs) [E3] | ~90 days (repo-intel) [E3] | Prefer host-declared window; do not lock. Record as GAP/OPEN. |
| ADR immutability vs edit-in-place | Nygard: supersede/deprecate, keep old [E1] | Some community ADR processes edit in place (E3 discovery) | Prefer Nygard/Toolbelt template (E0/E1) for Toolbelt-adjacent advice. |

## 7. Gaps & OPEN

- `GAP` Canonical primary protocol for “derive standards from code+git” with normative sample sizes / windows — not found.
- `GAP` Toolbelt recon S0–S16 does not yet include history/recency steps (product gap vs campaign intent).
- `GAP` Feathers primary not retrieved this pass (only Fowler pointer).
- `GAP` G4 GitHub STANDARDS.md pack sampling still separate (not this note).
- `OPEN` Host-declared vs Toolbelt-default recency window.
- `OPEN` Profile shape for dual-era (quarantine paths, suppressions file pointers, current-era ADR id).
- `OPEN` Automation of extract (community tools) vs human-led recon checklist — carry forward from normal wave.

## 8. Implications — proposed brownfield recipe

**Label: `CLAIM` / `INFERENCE` [E4] — proposed method, not accepted SoT.**

Premises: §4.1–4.5 FACT/CLAIM set; campaign fence (draft≠SoT; human accept); T16C conflict stack.

### Proposed recipe (Toolbelt brownfield derive lean)

1. **Recon sample (as-is)** — Run `research-codebase-recon` (structure, configs, instruction files). Prefer explicit configs (formatter/linter/tsconfig) as high-confidence convention candidates. [premises: E0 recon; E3 extract tools; normal-wave]

2. **Recency map (git signals)** — Within a **host-declared** window (practice defaults seen: ~90 days–12 months — **not locked**):
   - List high-churn paths via `git log --format=format: --name-only --since=<window>` + count/sort (recipe cited E3 understandlegacycode / paulund — treat as **example**, not FACT law).
   - Optionally inspect line age with `git blame --since=<window>` on conflicted exemplars [E1 git-blame].
   - If `.git-blame-ignore-revs` exists, use ignore-revs when reading blame so format waves do not dominate “who/when” [E1 Black/GitHub].

3. **Conflict of eras** — When two styles coexist:
   - Prefer majority **in hot (recent-churn) paths** over cold legacy trees.
   - Quarantine legacy dirs (document as `legacy` / out-of-scope for new work; Prettier/ESLint ignore or suppressions) [E1 Prettier; E1 ESLint].
   - Record conflict log: path/pattern → era A vs era B → evidence (file:line + churn note).

4. **Propose, don’t promote** — Emit **proposed** standards/principles candidates with evidence locators + confidence. Human accept required. Stack: accepted ADR/design > principles > standards profile > inferred-from-code. [E0 campaign + T16C]

5. **Adopt / dual-era enforcement** — When accepting a new era: enable rules with bulk suppressions or touch-to-clean; optional format wave + `.git-blame-ignore-revs`; do not require whole-repo rewrite. [E1 ESLint/Black]

6. **Evolve / deprecate** — Amend rarely with reason; mark old rules deprecated/superseded (ADR status or Obsolete appendix + standards changelog Deprecated→Removed). Keep records for agents/retrieval. [E1 Nygard; E2 FDG; E1 Keep a Changelog]

### What this note does **not** claim as FACT

- Exact CLI one-liners as mandatory Toolbelt procedure beyond what E1 docs state for those tools.
- A fixed N-month window.
- That community extract tools are accurate enough to skip human accept.

## 9. Source list (deduped)

1. git-blame(1) — https://www.kernel.org/pub/software/scm/git/docs/git-blame.html
2. Black — Introducing Black to your project — https://black.readthedocs.io/en/stable/guides/introducing_black_to_your_project.html
3. GitHub Docs — Viewing a file / ignore commits in blame — https://docs.github.com/en/repositories/working-with-files/using-files/viewing-a-file
4. ESLint — Bulk Suppressions — https://eslint.org/docs/latest/use/suppressions
5. Prettier — Ignoring Code — https://prettier.io/docs/ignore
6. Nygard — Documenting Architecture Decisions — https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
7. Alexandria `software_engineering` — Framework Design Guidelines (FDG) Obsolete appendix + foreword — chunk_ids `6545c48b1c5e2d859bdb9731`, `95542d0ca16cd64a8670970c`, `6fe850ffc19e0fa77be3ae05`
8. Alexandria `software_engineering` — Fowler Refactoring — chunk_ids `631cbc7d42c249cf1648e534`, `86d890eefd7b540f82162849`
9. Alexandria `software_engineering` — Architecture Patterns with Python (Strangler) — chunk_id `2f484602fd6a7cc8386079b5`
10. Alexandria `software_engineering` — RSE with Python (blame) — chunk_id `7388699fc32b3f8f1157f0bc`
11. Nicolas Carlo — Hotspots analysis — https://understandlegacycode.com/blog/focus-refactoring-with-hotspots-analysis/
12. Paulund — Git commands for reading new codebases — https://paulund.co.uk/notebook/git/git-commands-for-reading-new-codebases/
13. Johannes Stricker — Integrating ESLint into a legacy codebase — https://stricker.digital/posts/integrating-eslint-into-a-legacy-codebase/
14. Mainmatter — Lint to the Future — https://mainmatter.com/blog/2025/03/03/lttf-process/
15. Community extract tools (E3 discovery): ez-context, codespec, repo-intel
16. Local: `campaign-brief.md`, `t16h-i-lifecycle-brownfield.md`, `deep-campaign-board.md`, `t16c-foundational-principles.md`, `docs/templates/adr-minimal.md`, `research-codebase-recon` skill
17. Keep a Changelog (via Theme 3 prior citation) — https://keepachangelog.com/en/1.1.0/
