---
title: "Deep T16J — Bind patterns (AGENTS / rules / skills / feedstock vs gate)"
status: draft
theme: theme-16-host-standards
track: T16J
created: 2026-08-02
updated: 2026-08-02
authors: [gatherer-deep-t16j]
depth: deep
supersedes: null
aligned_with:
  - docs/research/notes/theme-16-host-standards/campaign-brief.md
  - docs/research/notes/theme-16-host-standards/t16j-bind.md
  - docs/research/reports/theme-15-closeout-readiness.md
---

# Deep T16J — Bind patterns

**Using `research-protocol`.** Depth: **deep**. Draft ≠ design law.

## 1. Scope

- **Question / goal:** How agent/host packs **bind** principles and standards into plan / execute / review / closeout — via `AGENTS.md`, `CLAUDE.md`, Cursor rules, skill references, and “always apply” rules — and how that maps to **author feedstock** vs **check against feedstock**.
- **In scope:** Official Cursor + vendor instruction-loading docs; public pointer patterns in `AGENTS.md`; Theme 15 closeout define/check; local Toolbelt E0 (T16J normal, T16A, closeout skill, `author-agents-md`); author-vs-gate patterns.
- **Out of scope:** Locking Toolbelt skill ids / profile paths (T16K); elevating `author-standards`; inventing Plan/Execute wire without design accept; ceremony/CI as bind law.
- **Closes toward:** campaign G6 (bind) + reinforce normal `t16j-bind.md`.

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-02 |
| Tools used | WebFetch, WebSearch, curl (Codex HTML), GitHub MCP `search_code`/`get_file_contents`, Alexandria `rag_query`, local Read/Grep |
| Corpora / URLs searched | cursor.com/docs (rules, skills, prompting); code.claude.com/docs/en/memory; developers.openai.com/codex/guides/agents-md; aider.chat/docs/usage/conventions; docs.continue.dev/customize/deep-dives/rules; GitHub `filename:AGENTS.md` + STANDARDS/STYLE; Alexandria `ai_llm_agents`; Toolbelt Theme 15 report + T15 notes; Theme 16 T16A/T16J/campaign brief; plugin skills `implementation-closeout`, `author-agents-md` |
| Queries (exact) | `Cursor IDE AGENTS.md rules documentation official`; `Anthropic Claude Code CLAUDE.md conventions`; `OpenAI Codex AGENTS.md`; `Aider CONVENTIONS.md`; `Continue.dev rules alwaysApply`; GitHub `STANDARDS.md filename:AGENTS.md`; GitHub `"style guide" OR STYLEGUIDE OR "coding standards" filename:AGENTS.md`; RAG `How do coding agents load project standards via AGENTS.md CLAUDE.md conventions rules alwaysApply?` |
| What was *not* searched | Live Cursor/Claude/Codex runtime injection E0 (no session instrument); Windsurf/Devin/Cline rule packs beyond Claude `/init` mention; full RAG `software_engineering` styleguide corpus; exhaustive AGENTS.md corpus census |
| Depth | deep |
| Waves / stop_reason | **W1** primary SoT (Cursor rules/skills/prompting; Claude memory; Codex AGENTS guide; Aider conventions; Continue rules) + local E0 Theme 15/16. **W2** corroboration (GitHub AGENTS.md pointer samples; Toolbelt skeleton/author-agents-md; prior T4N precedence GAP). **W3** residual — Alexandria weak on file-format bind; stop. `stop_reason`: new searches restated pointer/budget/alwaysApply FACTS without closing named GAPs (precedence AGENTS↔Team rules; Toolbelt plan/execute wire slots; skill-mode packaging = T16K). |
| Provenance (optional PROV) | Entity=bind surfaces (AGENTS/CLAUDE/rules/skills/profiles); Activity=deep T16J gather 2026-08-02; Agent=gatherer-deep-t16j |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Local Toolbelt closeout/AGENTS authoring is systematic E0; vendor bind surfaces are as-needed primary docs |
| Scope boundary | Plugin skills/rules/templates + Theme 15/16 notes/reports; not host product app code |

## 4. Findings

### 4.1 Cursor — rules, AGENTS.md, skills (primary)

- `FACT` [E1] Cursor documents **four** rule types: Project Rules (`.cursor/rules`), User Rules, Team Rules, and **`AGENTS.md`** as a simple markdown alternative to `.cursor/rules`. [E1: Rules — https://cursor.com/docs/rules.md — accessed 2026-08-02]
- `FACT` [E1] Project rules are `.mdc` with frontmatter; plain `.md` in `.cursor/rules` is ignored (no `description`/`globs`/`alwaysApply`). Prefer `AGENTS.md` for plain markdown. [E1: Rules — Rule file structure — https://cursor.com/docs/rules.md — accessed 2026-08-02]
- `FACT` [E1] Rule application modes: **Always Apply** (`alwaysApply: true`); **Apply to Specific Files** (`globs` + `alwaysApply: false`); **Apply Intelligently** (`description`, no globs); **Apply Manually** (`@`-mention only). [E1: Rules — Rule anatomy table — https://cursor.com/docs/rules.md — accessed 2026-08-02]
- `FACT` [E1] Team → Project → User precedence is documented for those three scopes (“earlier sources take precedence when guidance conflicts”). [E1: Rules — Team Rules Precedence — https://cursor.com/docs/rules.md — accessed 2026-08-02]
- `FACT` [E1] Best practice: **reference files instead of copying** contents; avoid copying entire style guides into rules (prefer linters); keep rules under 500 lines; split composable rules. [E1: Rules — Best practices / What to avoid — https://cursor.com/docs/rules.md — accessed 2026-08-02]
- `FACT` [E1] Nested `AGENTS.md` supported; combined with parents; **more specific** nested instructions take precedence. [E1: Rules — Nested AGENTS.md — https://cursor.com/docs/rules.md — accessed 2026-08-02]
- `FACT` [E1] Skills: auto-discovered from `.agents/skills/`, `.cursor/skills/`, user `~/.agents|~/.cursor/skills/`, plus Claude/Codex skill dirs for compatibility; agent sees skill catalog and decides relevance; optional `/skill-name`; progressive resources under `references/`. [E1: Agent Skills — https://cursor.com/docs/skills.md — accessed 2026-08-02]
- `FACT` [E1] Skill frontmatter includes `description` (relevance), optional `paths` globs, optional `disable-model-invocation: true` (slash-only). Dynamic rules (`alwaysApply: false`, no globs) can migrate to skills via `/migrate-to-skills`; **`alwaysApply: true` or globbed rules are not migrated**. [E1: Agent Skills — Frontmatter / Migrating — https://cursor.com/docs/skills.md — accessed 2026-08-02]
- `FACT` [E1] Prompt context breakdown lists **Rules** and **Skills** as separate injected categories (skill *descriptions* in system context). [E1: Prompting agents — Context usage — https://cursor.com/docs/agent/prompting.md — accessed 2026-08-02]
- `GAP` Documented conflict precedence when `AGENTS.md` / `CLAUDE.md` conflicts with Team / Project `.mdc` / User rules. Prior Theme 4 residual also open. Searched: rules.md precedence + AGENTS sections this pass; T4N note. Result: AGENTS.md not named in Team→Project→User ladder. [E0: `docs/research/notes/theme-4-cursor-plugins/t4n-residual-rules-agentsmd-precedence.md`]

### 4.2 Claude Code — CLAUDE.md / rules / imports

- `FACT` [E1] Claude Code loads **CLAUDE.md** (and related scopes) at session start as context, not enforced configuration; blocking actions → PreToolUse hooks. [E1: How Claude remembers your project — https://code.claude.com/docs/en/memory — accessed 2026-08-02]
- `FACT` [E1] Project instructions live in `./CLAUDE.md` or `./.claude/CLAUDE.md`; appropriate content includes coding standards, architecture, conventions, workflows; target **under ~200 lines**; move multi-step / narrow procedures to **skills** or **path-scoped** `.claude/rules/`. [E1: CLAUDE.md files / Write effective instructions — https://code.claude.com/docs/en/memory — accessed 2026-08-02]
- `FACT` [E1] `@path/to/import` imports additional files into context at launch (recursive up to four hops); backticks prevent import. [E1: Import additional files — https://code.claude.com/docs/en/memory — accessed 2026-08-02]
- `FACT` [E1] Claude reads `CLAUDE.md`, not `AGENTS.md`; recommended pattern: `CLAUDE.md` containing `@AGENTS.md` (or symlink) to share one instruction body. [E1: AGENTS.md section — https://code.claude.com/docs/en/memory — accessed 2026-08-02]
- `FACT` [E1] `.claude/rules/*.md` modularizes instructions; without `paths` frontmatter they load at launch like project CLAUDE.md; path-scoped rules load when matching files are in play; task-specific → skills. [E1: Organize rules with `.claude/rules/` — https://code.claude.com/docs/en/memory — accessed 2026-08-02]

### 4.3 OpenAI Codex — AGENTS.md discovery / budget

- `FACT` [E1] Codex builds an instruction chain at start: global `~/.codex/AGENTS.override.md` else `AGENTS.md`; then project walk root→cwd with per-directory `AGENTS.override.md` then `AGENTS.md` (or fallbacks); concatenate root→cwd so closer files appear later and override. [E1: Custom instructions with AGENTS.md — https://developers.openai.com/codex/guides/agents-md — accessed 2026-08-02]
- `FACT` [E1] Combined size stops at `project_doc_max_bytes` (**32 KiB default**); empty files skipped; fallback filenames configurable (`project_doc_fallback_filenames`). [E1: same URL — accessed 2026-08-02]
- `OPEN` Whether `project_doc_max_bytes` is strictly combined vs per-file in all Codex dumps — already flagged in Toolbelt secondary refinement / skeleton. Follow-up: pin wording in current Codex config docs if elevating budgets as law. [E0: `docs/research/reports/secondary-refinement.md`; `docs/templates/agents-md-skeleton.md`]

### 4.4 Aider — CONVENTIONS as read-only feedstock

- `FACT` [E1] Aider’s documented pattern: put coding guidelines in a small markdown file (example name `CONVENTIONS.md`), load with `/read` or `aider --read` (read-only / cache-friendly), or always via `.aider.conf.yml` `read:` list. [E1: Specifying coding conventions — https://aider.chat/docs/usage/conventions.html — accessed 2026-08-02]
- `INFERENCE` [E4] Aider treats conventions as **always-attached feedstock** in the chat, not as a separate “check mode” skill — enforcement is prompt adherence (+ optional lint/test cmds), not a readiness gate. Premises: (1) conventions.html load paths [E1]; (2) no define/check dual-mode in that page.

### 4.5 Continue.dev — rules → system message

- `FACT` [E1] Continue rules live in `.continue/rules` (markdown/YAML); joined into the system message for Agent/Chat/Edit; support `globs`, `description`, `alwaysApply` (true / false / default). Example frontmatter title “Documentation Standards”. [E1: How to Create and Manage Rules — https://docs.continue.dev/customize/deep-dives/rules — accessed 2026-08-02]
- `FACT` [E1] Continue docs position rules as guardrails for coding standards / org practices (not autocomplete). [E1: Rules overview — https://docs.continue.dev/customize/rules — accessed 2026-08-02]

### 4.6 GitHub samples — AGENTS.md → STYLE / STANDARDS pointers (community / discovery)

- `FACT` [E3] `Simple-XX/SimpleKernel` root `AGENTS.md` points conventions to full reference `docs/coding_standards.md` (“read it before generating any code”) rather than inlining the guide. [E3: https://github.com/Simple-XX/SimpleKernel/blob/d384aebcd9cc57c5e105c58b7ee1a47839526a68/AGENTS.md — accessed 2026-08-02]
- `FACT` [E3] `elastic/terraform-provider-elasticstack` `AGENTS.md`: “Follow … [`coding-standards.md`](./dev-docs/high-level/coding-standards.md)” plus contributing/workflow links — start-here index pattern. [E3: https://github.com/elastic/terraform-provider-elasticstack/blob/ff6aa6f1060475d33481a1617e504ff849b14ffc/AGENTS.md — accessed 2026-08-02]
- `FACT` [E3] `nadohq/nado-typescript-sdk` `AGENTS.md` section “TypeScript SDK Style Guide” links `./docs/STYLEGUIDE.md` and lists topic areas covered there; also binds a post-edit verify sequence (typecheck/lint/build/test). [E3: https://github.com/nadohq/nado-typescript-sdk/blob/64989d50de00614c9e437cbac5a6b5785e514df5/AGENTS.md — accessed 2026-08-02]
- `CLAIM` [E3] Additional hits (e.g. quran.com-frontend-next `.agents/.../core-standards.md`; chromium Cronet nested AGENTS → Google/Chromium style guides; westonruter PHP/JS + `.gemini/styleguide.md`) show the same **pointer-to-canonical-standards** pattern. Discovery only — do not lock Toolbelt layout from these. [E3: GitHub code search `STANDARDS.md filename:AGENTS.md` / style-guide query — 2026-08-02]
- `GAP` Alexandria `ai_llm_agents` query on AGENTS/CLAUDE/alwaysApply did not return high-signal chunks about these file formats (enterprise “coding conventions” prose only). Searched: rag_query corpus=`ai_llm_agents`. Result: weak for bind-surface specifics → prefer E1 vendor docs above.

### 4.7 Local Toolbelt + Theme 15/16 (E0) — feedstock vs gate

- `FACT` [E0] Theme 16 brief defines **Bind** as “Plan/Execute/Closeout consume profile”; elevation note: “standards as feedstock; closeout/plan/execute as consumers.” [E0: `docs/research/notes/theme-16-host-standards/campaign-brief.md`]
- `FACT` [E0] Theme 15 accepted D2/D9: shape **O1** skill+template with **define/update** + **check**; **no always-on rule**; no universal mega-checklist as law. [E0: `docs/research/reports/theme-15-closeout-readiness.md`]
- `FACT` [E0] Shipped `implementation-closeout` classifies modes `define-update` | `check`; check scores criteria with evidence locators (`ready|blocked|waived|n/a`); does not invent greens; skip when trivial / no profile. [E0: plugin `skills/implementation-closeout/SKILL.md`]
- `FACT` [E0] T15F lean: two modes in one skill — **define/update profile** | **check readiness** (classifier). [E0: `docs/research/notes/theme-15-closeout-readiness/t15f-shape-options-lean.md`]
- `FACT` [E0] Normal T16J lean (draft): Plan links profile in T0/Done-when; Execute workers load profile / verify may include standards checks; Closeout criteria *reference* standards paths+§; AGENTS.md = short pointer not full dump. [E0: `docs/research/notes/theme-16-host-standards/t16j-bind.md`]
- `FACT` [E0] T16A: `author-agents-md` exists; design/plan/closeout consumers exist; **no** dedicated `author-standards` / principles-profile skill yet. [E0: `docs/research/notes/theme-16-host-standards/t16a-local-baseline.md`]
- `FACT` [E0] `author-agents-md`: progressive disclosure + size budgets (Codex 32 KiB cited); prefer links over growth; optional Claude `@AGENTS.md`; Cursor `.mdc` adapters only when needed; `disable-model-invocation: true` (explicit `/`). [E0: plugin `skills/author-agents-md/SKILL.md`; `docs/templates/agents-md-skeleton.md`]
- `FACT` [E0] Toolbelt always-apply rule example: `draft-is-not-sot.mdc` uses YAML `alwaysApply: true` for cross-cutting method law (not a host coding style guide). [E0: plugin `rules/draft-is-not-sot.mdc`]
- `FACT` [E0] Theme 15 D7/happy-path: optional closeout before Stop; skip trivial by default — consumer bind is **opt-in / profile-gated**, not always-on. [E0: Theme 15 report elevation D7]

### 4.8 Pattern synthesis — author feedstock vs check gate

| Pattern | What it is | Surfaces observed | Role |
|---------|------------|-------------------|------|
| **A. Always-on instruction slice** | Small rules always in context | Cursor `alwaysApply: true`; Claude root CLAUDE.md / unscoped rules; Codex AGENTS chain; Continue `alwaysApply: true`; Aider `read:` | Bind *awareness* |
| **B. Scoped / intelligent attach** | Load when path/description matches | Cursor globs / Apply Intelligently; Claude `paths` rules; Continue globs; Cursor skill `paths` | Bind *relevance* |
| **C. Progressive pointer** | Thin index → deep STYLE/STANDARDS/docs | Cursor “reference files”; Claude `@import` + “don’t dump procedures”; Codex/Toolbelt budgets; GH AGENTS→`coding_standards.md` / `STYLEGUIDE.md` | Bind *without dump* |
| **D. Explicit skill load** | Task workflow when invoked / relevant | Cursor/Claude skills; Toolbelt `implementation-*` | Bind *procedure* |
| **E. Author feedstock** | Create/update durable profile/standards | Theme 15 `define-update`; future principles/standards author (OPEN T16K); `author-agents-md` for AGENTS layer | Produce feedstock |
| **F. Gate / check** | Score work vs feedstock + evidence | Theme 15 `check`; plan Done-when / execute verify (lean); post-edit command sequences in some AGENTS.md | Consume feedstock |

- `INFERENCE` [E4] **G6 bind stack (lean, not locked):** (1) host **principles/standards profiles** = feedstock (author skill/template — T16K); (2) **AGENTS.md / thin always-apply** = pointers + non-negotiable method crumbs only; (3) **Plan/Execute** cite profile paths in constraints / Done-when / verify; (4) **Closeout check** references standards/principles evidence locators rather than duplicating rule text; (5) skip consumers when no profile. Premises: Theme 16 brief feedstock language [E0]; Theme 15 define/check [E0]; Cursor/Claude/Codex pointer+budget [E1]; GH pointer samples [E3]; normal T16J [E0].
- `INFERENCE` [E4] “Review” in the mission list maps cleanly to **closeout check** and/or host review expectations encoded as AGENTS “after changes” command lists — not a separate Toolbelt review skill required for G6. Premises: Theme 15 readiness framing; nado AGENTS verify sequence [E3]; no Theme 16 track for a distinct review binder.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Host standards bind best as **pointer + consumer checks**, not mega always-apply paste | confirmed (research lean) | Cursor avoid style-guide dump [E1]; budgets [E1]; GH pointers [E3]; T16J [E0] |
| H2 | Theme 15 define/check is the reusable **author vs gate** template for standards/principles | confirmed (pattern reuse lean) | T15 D2/O1 + closeout skill [E0]; campaign feedstock wording [E0] |
| H3 | AGENTS.md should contain the full standards body | rejected (as design lean) | Conflicts with E1 budgets/best practices + E3 pointer samples |
| H4 | Always-apply rules are appropriate for host coding style guides | revised | Prefer always-apply for short method/safety crumbs; style/standards → profile + scoped rules/skills [E1+E0 Theme 15 D9] |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| AGENTS vs Team/Project/User precedence | Cursor Team→Project→User [E1] | AGENTS listed as 4th type / nested-only precedence [E1] | Prefer higher-grade docs; **GAP** on cross-type conflict — do not lock merge order |
| Claude vs Codex instruction filename | Claude: CLAUDE.md (+ `@AGENTS.md`) [E1] | Codex/Cursor: AGENTS.md [E1] | Interop via import/symlink (Claude E1); Toolbelt skeleton already documents |
| Always-on vs skip-if-absent | Vendor always-load memory files [E1] | Theme 15 skip trivial / no always-on closeout rule [E0] | Different layers: thin always-on pointers OK; **profile checks** stay optional |

## 7. Gaps & OPEN

- `GAP` Exact Cursor precedence when `AGENTS.md`/`CLAUDE.md` conflicts with Team/Project/User rules. Searched: official rules docs + T4N. Result: not found.
- `GAP` Official Cursor docs do not specify a “standards profile” artifact or Plan/Execute bind slots — Toolbelt must design consumers. Searched: rules.md, skills.md, prompting.md. Result: general rules/skills only.
- `GAP` No E1 vendor dual-mode “author standards profile | check conformance” skill analogue beyond Toolbelt Theme 15 closeout. Searched: vendor docs above; GH AGENTS samples. Result: pointers + always-on instructions dominate; checklists often in AGENTS command lists (E3).
- `OPEN` Skill packaging: single skill modes (define principles | define standards | derive | bind-check) vs multiple skills — **T16K**.
- `OPEN` Exact host path convention for principles/standards profiles (and whether AGENTS must list them) — design/elevate after lean.
- `OPEN` Whether Execute “verify” steps should hard-require standards checks or remain Done-when optional (intelligent skip) — needs design accept; T16J normal is lean only.
- `OPEN` Codex `project_doc_max_bytes` combined vs per-file wording clarification.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] For Theme 16 elevation: treat **author feedstock** (principles/standards profiles) and **bind-check** (plan/execute/closeout consumers) as separate jobs — reuse Theme 15’s define/check classifier pattern; keep AGENTS.md as **budgeted pointer**, not feedstock dump. Premises: §4.7–4.8.
- `INFERENCE` [E4] Prefer **scoped / intelligent / skill** attachment for large standards bodies; reserve `alwaysApply: true` for short cross-cutting method laws (Toolbelt’s own `draft-is-not-sot` pattern). Premises: Cursor migrate guidance [E1]; Theme 15 D9 [E0]; Claude size guidance [E1].
- `INFERENCE` [E4] Closeout criteria rows that *cite* `path+§` of standards/principles satisfy G6 without duplicating rule text — thins specificity while remaining checkable. Premises: normal T16J [E0]; Theme 15 evidence locators [E0].

## 9. Source list (deduped)

1. https://cursor.com/docs/rules.md — accessed 2026-08-02  
2. https://cursor.com/docs/skills.md — accessed 2026-08-02  
3. https://cursor.com/docs/agent/prompting.md — accessed 2026-08-02  
4. https://code.claude.com/docs/en/memory — accessed 2026-08-02  
5. https://developers.openai.com/codex/guides/agents-md — accessed 2026-08-02  
6. https://aider.chat/docs/usage/conventions.html — accessed 2026-08-02  
7. https://docs.continue.dev/customize/deep-dives/rules — accessed 2026-08-02  
8. https://docs.continue.dev/customize/rules — accessed 2026-08-02  
9. GitHub: Simple-XX/SimpleKernel `AGENTS.md` @ d384aeb — 2026-08-02  
10. GitHub: elastic/terraform-provider-elasticstack `AGENTS.md` @ ff6aa6f — 2026-08-02  
11. GitHub: nadohq/nado-typescript-sdk `AGENTS.md` @ 64989d5 — 2026-08-02  
12. `docs/research/reports/theme-15-closeout-readiness.md`  
13. `docs/research/notes/theme-15-closeout-readiness/t15f-shape-options-lean.md`  
14. `docs/research/notes/theme-16-host-standards/campaign-brief.md`  
15. `docs/research/notes/theme-16-host-standards/t16j-bind.md`  
16. `docs/research/notes/theme-16-host-standards/t16a-local-baseline.md`  
17. `docs/research/notes/theme-4-cursor-plugins/t4n-residual-rules-agentsmd-precedence.md`  
18. Plugin: `skills/implementation-closeout/SKILL.md`, `skills/author-agents-md/SKILL.md`, `rules/draft-is-not-sot.mdc`  
19. `docs/templates/agents-md-skeleton.md`  
20. Alexandria `ai_llm_agents` rag_query (weak for this topic) — 2026-08-02  
