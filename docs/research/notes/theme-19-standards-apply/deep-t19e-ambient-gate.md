---
title: "Deep T19E — Ambient gate / Cursor rules progressive disclosure"
status: draft
theme: theme-19-standards-apply
created: 2026-08-03
updated: 2026-08-03
authors: [research-gatherer]
depth: deep
aligned_with:
  - docs/research/notes/theme-19-standards-apply/campaign-brief.md
  - docs/research/notes/theme-19-standards-apply/t19i-shape-options-lean.md
supersedes: null
---

# Deep T19E — Ambient gate / Cursor rules progressive disclosure

**Using `research-protocol`.** Depth: **deep** (primary-docs gatherer for track T19E).  
`draft` ≠ design law (`draft-is-not-sot`). Relate findings to accepted O1 lean (thin always-on *resolve gate*, not standards *bodies*) without locking elevate.

## 1. Scope

- **Question / goal:** How do Cursor (primary) rules/skills — and quick peer AGENTS/memory guides — describe always-on vs intelligent vs path-scoped load, progressive disclosure, and “don’t dump large standards into every context”? What does that imply for Theme 19’s ambient gate?
- **In scope:** Cursor Rules + Skills + Agent overview (primary); Claude Code memory (+ skills skim); Codex AGENTS customization guides (primary URLs); Agent Skills open-spec progressive-disclosure section (linked from Cursor).
- **Out of scope:** RAG (T19F), GitHub sampling (T19G), elevating Toolbelt surfaces, inventing host standards content, runtime E0 experiments of Cursor attach behavior.

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-03 |
| Tools used | WebFetch; WebSearch (URL discovery); curl.exe (Codex HTML when WebFetch/IWR failed on 308); Read of returned markdown/HTML |
| Corpora / URLs searched | See §9 Source list (all accessed **2026-08-03**) |
| Queries (exact) | `site:cursor.com/docs rules alwaysApply Agent Requested globs skills progressive disclosure`; `Claude Code CLAUDE.md memory pointer progressive disclosure official docs`; `OpenAI Codex AGENTS.md official documentation keep short pointer` |
| What was *not* searched | Alexandria RAG; GitHub STANDARDS packs; community blogs as SoT; Cursor plugin marketplace internals; E0 attach telemetry in a live chat |
| Depth | deep |
| Waves / stop_reason | Wave 1 primary SoT (Cursor rules/skills/agent). Wave 1b peer primary skim (Claude memory/skills; Codex AGENTS; agentskills.io progressive disclosure). **stop_reason:** named T19E FACTS closed from primary docs; further web hits were E3 restatement; residual items need E0 runtime or design accept, not more docs. Campaign stop still governed by `diminishing_returns_plus_2` across T19E–G. |
| Provenance (optional PROV) | Entity=Cursor/Claude/Codex/AgentSkills docs; Activity=T19E fetch 2026-08-03; Agent=research-gatherer |

**URL note:** `https://cursor.com/docs/context/rules` and `.../context/skills` returned load errors on 2026-08-03. Working primary pages used: `https://cursor.com/docs/rules` and `https://cursor.com/docs/skills` (also linked from Agent overview as `rules.md` / skills). Codex `developers.openai.com` returned 308 to IWR; content corroborated via `curl.exe -sL` HTML and `learn.chatgpt.com` mirror of the same guide.

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | systematic (primary docs) + as-needed peer skim |
| Why this mode | Campaign track T19E = ambient gate patterns; O1 lean already accepted — corroborate/falsify “thin gate, not dump” against vendor docs |
| Scope boundary | Primary product docs only for FACT locks; peers for pointer-not-dump patterns |

## 4. Findings

### 4.1 Cursor Rules — apply modes

- `FACT` [E1] Cursor documents **four** project-rule application types: **Always Apply** (every chat session); **Apply Intelligently** (Agent decides from `description`); **Apply to Specific Files** (glob / file match); **Apply Manually** (`@`-mention). [E1: Cursor Rules — https://cursor.com/docs/rules — accessed 2026-08-03]
- `FACT` [E1] Frontmatter interaction table: `alwaysApply: true` → always included (**globs and description ignored**); `alwaysApply: false` + `globs` → auto-attached when a matching file is in context; `alwaysApply: false` + `description` (globs omitted) → Agent reads description and pulls rule when relevant; `alwaysApply: false` with both omitted → only via `@`-mention. [E1: same]
- `FACT` [E1] “When applied, rule contents are included **at the start of the model context**.” [E1: same — “How rules work”]
- `FACT` [E1] Project rules are `.mdc` with frontmatter (`description`, `globs`, `alwaysApply`); plain `.md` under `.cursor/rules` is ignored by the rules system. [E1: same]
- `FACT` [E1] Nested `AGENTS.md` is supported; subdirectory instructions combine with parents, **more specific taking precedence**. [E1: same — “Nested AGENTS.md support”]
- `FACT` [E1] Agent lists a **Fetch Rules** tool: “Retrieve specific rules based on type and description.” [E1: Cursor Agent — https://cursor.com/docs/agent — accessed 2026-08-03]
- `GAP` Exact runtime algorithm for “Apply Intelligently” (ranking, token budget, when Fetch Rules fires) is not specified beyond description-based relevance. Searched: Cursor Rules + Agent pages. Result: behavioral summary only.

### 4.2 Cursor Rules — thinness & anti-dump guidance

- `FACT` [E1] Best practices: “Good rules are focused, actionable, and scoped.” Explicit bullets include **keep rules under 500 lines**; **split large rules into multiple, composable rules**; **reference files instead of copying their contents** — “keeps rules short and prevents them from becoming stale.” [E1: https://cursor.com/docs/rules — accessed 2026-08-03]
- `FACT` [E1] **What to avoid:** “**Copying entire style guides**: Use a linter instead. Agent already knows common style conventions.” Also avoid documenting every possible command; edge cases that rarely apply; duplicating what’s already in the codebase — “Point to canonical examples instead of copying code.” [E1: same]
- `FACT` [E1] “Start simple. Add rules only when you notice Agent making the same mistake repeatedly.” [E1: same]
- `INFERENCE` [E4] Cursor’s primary guidance is strongly against stuffing large coding-standards corpora into always-attached rule bodies. Premises: (1) always-applied rules enter every chat start context; (2) docs warn against copying entire style guides and urge reference-not-copy + split composable rules. → Supports O1: ambient surface should not embed full standards modules.

### 4.3 Cursor Skills — progressive disclosure / references

- `FACT` [E1] Skills are described as **Progressive**: “Skills load resources on demand, keeping context usage efficient.” [E1: Cursor Agent Skills — https://cursor.com/docs/skills — accessed 2026-08-03]
- `FACT` [E1] On startup Cursor discovers skills and “makes them available to Agent. The agent is presented with available skills and decides when they are relevant based on context.” Skills may also be invoked via `/`. [E1: same]
- `FACT` [E1] Optional dirs include `references/` (“Additional documentation loaded on demand”) and `scripts/` / `assets/`. Guidance: “Keep your main `SKILL.md` focused and move detailed reference material to separate files. This keeps context usage efficient since agents load resources progressively—only when needed.” [E1: same]
- `FACT` [E1] Skill `paths` (preferred over legacy `globs`) scopes when a skill is surfaced to matching files — “keeps file-specific guidance out of context for unrelated work.” [E1: same]
- `FACT` [E1] `/migrate-to-skills` converts **dynamic** (“Apply Intelligently”) rules — `alwaysApply: false`/unset and **no** `globs` — into skills. Rules with `alwaysApply: true` or specific `globs` **are not migrated**, “as they have explicit triggering conditions that differ from skill behavior.” [E1: same]
- `INFERENCE` [E4] Cursor product shape separates **always/glob-triggered persistent rules** from **description-triggered skills with progressive body/refs** — aligning with O1’s split: thin always-on *gate* vs skill `standards-router` that points/loads selectively. Premises: migration exclusion of alwaysApply/globs; skills progressive + references on demand.

### 4.4 Agent Skills open standard (corroboration)

- `FACT` [E1] agentskills.io Specification: agents load skills progressively — metadata/description first; full `SKILL.md` when activated; `scripts/` / `references/` / `assets/` only as needed. “Keep your main `SKILL.md` under 500 lines. Move detailed reference material to separate files.” “Keep individual reference files focused… smaller files mean less use of context.” [E1: Agent Skills Specification — https://agentskills.io/specification — accessed 2026-08-03]
- `FACT` [E1] Spec: once activated, agent loads the entire `SKILL.md` — “Consider splitting longer `SKILL.md` content into referenced files.” [E1: same]

### 4.5 Claude Code memory / skills (peer primary — pointer patterns)

- `FACT` [E1] CLAUDE.md (and auto memory) load at the start of every conversation; “The more specific and concise your instructions, the more consistently Claude follows them.” **Size target: under 200 lines per CLAUDE.md**; longer files consume more context and reduce adherence — prefer path-scoped rules or skills for large/growing content. [E1: Claude Code memory — https://docs.anthropic.com/en/docs/claude-code/memory (also https://code.claude.com/docs/en/memory) — accessed 2026-08-03]
- `FACT` [E1] “Keep it to facts Claude should hold in every session… If an entry is a multi-step procedure or only matters for one part of the codebase, move it to a **skill** or a **path-scoped rule** instead.” [E1: same]
- `FACT` [E1] Path-scoped `.claude/rules/` with `paths` frontmatter “only load into context when Claude works with matching files, reducing noise and saving context space.” Rules **without** `paths` load at launch unconditionally. [E1: same]
- `FACT` [E1] Docs contrast: rules load every session or on path match; **skills** for “task-specific instructions that don’t need to be in context all the time… which only load when you invoke them or when Claude determines they’re relevant.” [E1: same]
- `FACT` [E1] Subdirectory `CLAUDE.md` under cwd is **not** loaded at launch; included when Claude reads files in those subdirectories. [E1: same]
- `FACT` [E1] `@path` imports in CLAUDE.md are expanded and loaded at launch (recursive, max depth 4) — i.e. `@` is include-at-start, not deferred load. Backticks prevent import. [E1: same]
- `FACT` [E1] Skills: “Unlike CLAUDE.md content, a skill’s body loads only when it’s used, so long reference material costs almost nothing until you need it.” Supporting files: “Large reference docs… don’t need to load into context every time the skill runs.” Default: description in listing context; full skill on invoke. [E1: Claude Code skills — https://code.claude.com/docs/en/skills — accessed 2026-08-03]
- `INFERENCE` [E4] Claude’s “pointer not dump” pattern for always-on memory is: keep root CLAUDE.md short; defer procedures/domain corpora to skills or path-scoped rules; avoid treating `@import` as progressive disclosure (it still dumps at launch). Premises: 200-line target; procedure→skill/path rule; `@` loads at launch.

### 4.6 Codex AGENTS.md (peer primary — pointer / size patterns)

- `FACT` [E1] Customization overview: “`AGENTS.md` gives Codex durable project guidance that travels with your repository and applies before the agent starts work. **Keep it small.**” Also: “Start with only the instructions that matter… put guidance in the closest directory where it applies”; pair with linters/hooks for enforcement rather than bloating agent text. [E1: Codex Customization — https://developers.openai.com/codex/concepts/customization (HTML via curl 2026-08-03; mirror learn.chatgpt.com) — accessed 2026-08-03]
- `FACT` [E1] AGENTS discovery concatenates global → root → nested path to cwd; closer files override; empty files skipped; combined size capped by `project_doc_max_bytes` (**32 KiB default**). Guidance when truncated: “Raise `project_doc_max_bytes` or **split large files across nested directories** to keep critical guidance intact.” [E1: Custom instructions with AGENTS.md — https://developers.openai.com/codex/guides/agents-md / https://learn.chatgpt.com/docs/agent-configuration/agents-md — accessed 2026-08-03]
- `FACT` [E1] For review rules in AGENTS.md: “Keep rules concise… and reserve formatting and lint checks for CI.” [E1: same]
- `INFERENCE` [E4] Codex treats always-loaded AGENTS as a **budgeted, nestable pointer layer**, not an unbounded standards dump (byte cap + “keep it small” + nest by directory). Premises: Keep it small; 32 KiB default; nest/split guidance.

### 4.7 Relation to O1 lean (Theme 19)

Accepted O1 (`t19i-shape-options-lean.md`): new skill `standards-router` + catalog + **thin ambient rule** (`alwaysApply: true`, empty/absent → no-op) that invokes resolve — **do not paste module bodies in the rule**; amend D12 to forbid always-on *standards bodies* but allow always-on *resolve gate*.

| O1 element | Doc corroboration | Label |
|------------|-------------------|--------|
| Thin always-on gate (not standards body) | Cursor: avoid entire style guides in rules; alwaysApply content is session-start context; keep &lt;500 lines / split / `@` reference files. Claude: &lt;200 lines always-on; procedures → skills. Codex: keep AGENTS small + byte cap. | `INFERENCE` [E4] Strong support |
| Router as skill (compose / selective load) | Cursor skills progressive + `references/` on demand; migrate intelligent rules → skills; Claude skills body deferred until use. | `INFERENCE` [E4] Support |
| Empty/absent → no-op | Not documented as a Cursor product primitive for “missing catalog.” O1 pattern is Toolbelt design, not vendor API. | `GAP` / design |
| Path/globs for module bodies | Cursor rule globs + skill `paths`; Claude rule `paths`; nested AGENTS — all support *scoped* attach of domain guidance without global dump. | `INFERENCE` [E4] Support for catalog modules as non-alwaysApply / path or skill-loaded |
| O4 rejected (embed full standards in ambient) | Directly conflicts with Cursor “What to avoid” + Claude size targets + Codex keep-small. | `INFERENCE` [E4] Corroborates reject |

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Primary Cursor docs discourage large always-on standards dumps | confirmed | §4.2 FACTS |
| H2 | Skills/`references` are the progressive channel; alwaysApply is for short persistent constraints | confirmed | §4.1–4.3 |
| H3 | Vendors document an explicit “if catalog missing, alwaysApply no-op” API | rejected / GAP | No such API; O1 no-op is host rule text design |
| H4 | Peer AGENTS/CLAUDE memory guides converge on “pointer / nest / budget,” not monolith | confirmed | §4.5–4.6 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Size heuristics | Cursor rules “under 500 lines”; Agent Skills / Cursor skills “SKILL.md under 500 lines” | Claude CLAUDE.md “under 200 lines” | No contradiction — different surfaces (rule/skill body vs always-on memory). Prefer each product’s own limit for that surface. |
| Progressive `@` | Cursor rules: reference files instead of copying (keeps short) | Claude: `@path` imports expand **at launch** | Different semantics. Claude `@` ≠ deferred load. For O1 ambient gate, prefer explicit “read module paths” / skill refs over Claude-style eager `@import` of full standards. |
| Docs URL | `/docs/context/rules` error | `/docs/rules` works | Cite working URLs; note failed aliases in Method. |

## 7. Gaps & OPEN

- `GAP` Empty/absent catalog → product-level no-op: not in Cursor docs; remains Toolbelt rule-authoring pattern under O1.
- `GAP` Whether an `alwaysApply: true` rule that only says “invoke skill X” reliably triggers skill load every session (vs relying on Agent Decide) — needs E0 smoke after elevate; not claimed here.
- `OPEN` Prefer ambient as Always Apply vs Apply Intelligently for the resolve gate? O1 leans Always Apply + no-op; Cursor also offers description-triggered. Design choice at elevate, not locked by this note.
- `OPEN` Team Rules without globs “apply to every conversation” — org-level fat standards risk; out of Theme 19 host elevate unless host uses Team plan.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] **T19E supports O1’s ambient shape:** a short always-on (or carefully scoped) rule that *resolves pointers* matches Cursor/Claude/Codex guidance better than O4 (full standards in always-on). Premises: §4.2–4.6.
- `INFERENCE` [E4] **Module bodies belong in progressive channels:** description-triggered skill (`standards-router`) + on-demand `references/` / file reads / path-scoped rules — not in `alwaysApply` payload. Premises: skills progressive FACTS; migration excludes alwaysApply from skill conversion.
- `INFERENCE` [E4] **D12 amend direction** (forbid always-on standards *bodies*; allow always-on *resolve gate*) is consistent with primary Cursor “What to avoid” and peer keep-small memory. Premises: O1 lean + §4.2/4.5/4.6. Still requires human accept on elevate — this note stays `draft`.
- Do **not** treat this note as accepted architecture.

## 9. Source list (deduped)

1. Cursor Rules — https://cursor.com/docs/rules — accessed 2026-08-03  
2. Cursor Agent Skills — https://cursor.com/docs/skills — accessed 2026-08-03  
3. Cursor Agent — https://cursor.com/docs/agent — accessed 2026-08-03  
4. Agent Skills Specification — https://agentskills.io/specification — accessed 2026-08-03  
5. Claude Code — How Claude remembers your project — https://docs.anthropic.com/en/docs/claude-code/memory — accessed 2026-08-03  
6. Claude Code — memory (code.claude.com mirror) — https://code.claude.com/docs/en/memory — accessed 2026-08-03  
7. Claude Code — Skills — https://code.claude.com/docs/en/skills — accessed 2026-08-03  
8. Codex — Custom instructions with AGENTS.md — https://developers.openai.com/codex/guides/agents-md — accessed 2026-08-03 (via curl HTML; content also via https://learn.chatgpt.com/docs/agent-configuration/agents-md)  
9. Codex — Customization — https://developers.openai.com/codex/concepts/customization — accessed 2026-08-03 (via curl HTML)  
10. Theme 19 O1 lean (accepted local) — `docs/research/notes/theme-19-standards-apply/t19i-shape-options-lean.md` — E0 context for relation only  

**Attempted / failed (not cited for FACTS):** `https://cursor.com/docs/context/rules`, `https://cursor.com/docs/context/skills` (page errors 2026-08-03).

## 10. Self-check

- [x] Depth recorded: deep + stop_reason  
- [x] Method block present  
- [x] FACT/CLAIM supported; INFERENCEs list premises  
- [x] No invented APIs; GAPs for undocumented no-op product behavior  
- [x] Conflicts logged  
- [x] `status: draft` — not design law  
- [x] No commit (per request)
