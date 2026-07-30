---
title: "T6A W1 — Plans for fresh agents / subagents (self-containment)"
status: draft
theme: theme-6-plan
created: 2026-07-29
updated: 2026-07-29
authors: [t6a-gatherer-grok]
supersedes: null
aligned_with:
  - docs/research/notes/theme-6-plan/campaign-brief.md
  - docs/research/notes/theme-6-plan/t6-coordinator-pin.md
  - docs/PROTOCOL.md
---

# T6A W1 — How to write implementation plans for fresh agents

## 1. Scope

- Question / goal: How should an **implementation plan** be written so a **fresh agent / subagent** (no prior chat) can execute it without hallucinating requirements or inventing design decisions?
- In scope:
  - Self-containment: what must live in the plan vs what may be linked (design docs, ADRs, research notes)
  - Anti-assumption / anti-hallucination patterns (constraints, “do not”, interfaces, verify steps, expected outputs)
  - Task granularity and checkability for agent readers
  - E1–E2 web sources on agent task specs, context engineering, “plans for LLMs”, subagent handoffs
  - Optional E0 inventory of Superpowers `writing-plans` structure (E3 community; not Toolbelt law)
- Out of scope:
  - Elevating Toolbelt Plan skills / templates mid-research
  - Re-litigating Theme 5 Design pocket (Design owns what/why; Plan owns checkable sequence)
  - UX planning methods (T5C deferred)
  - Importing Superpowers git / worktree / TDD / PR policies as Toolbelt locks
  - Multi-agent orchestration product choice (T6C); decomposition recipes (T6B)
- Comprehension / research goal type (if code): other (method research for Plan pocket)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Read (research-protocol, research-note template, campaign brief, coordinator pin, Superpowers writing-plans SKILL.md); WebSearch; WebFetch |
| Corpora / URLs searched | Anthropic engineering; Claude Code docs (sub-agents, best-practices); Cursor docs (plan-mode, subagents); OpenAI Codex best practices; OpenAI Agents orchestration + handoffs; LangChain context-engineering blog; Microsoft ai-agents-for-beginners lesson 12 (raw README); secondary/community blogs discovered via search (graded E3 only) |
| Queries (exact) | `LLM agent task specification context engineering plans for agents subagent handoff 2024 2025`; `Anthropic Claude agents effective context engineering skills writing instructions for subagents`; `OpenAI agents SDK handoff instructions task specification best practices`; `writing specifications for LLM coding agents prevent hallucination task checklist acceptance criteria`; `site:code.claude.com best practices plan mode subagents investigation self-contained` |
| What was *not* searched | Alexandria RAG corpora; GitHub star rankings of plan skills (T6D); BMAD / story-packet formalisms; live Cursor/Claude runtime E0 experiments; academic HCI papers on plan comprehension; Theme 5 Design report re-audit |
| Depth | deep |
| Waves / stop_reason | wave: 1; slice: T6A. `stop_reason` (this gatherer): W1 primary SoT + graded community inventory complete for the slice question; residual corroboration (RAG, deepen blogs→primary, acceptance-criteria formalisms) deferred to W2 / gap fleet — not escalated here. |
| Provenance (optional PROV) | Entity=plan-for-fresh-agents patterns; Activity=T6A W1 web+local gather; Agent=cursor-grok gatherer |

**Using `research-protocol`; depth: deep; wave: 1; slice: T6A.**

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Primary vendor docs (systematic WebFetch) + optional local Superpowers structure inventory; community blogs discovery-only |
| Scope boundary | Plan *document* quality for zero-prior-chat executors; not Design SoT; not Implement craft |

## 4. Findings

### 4.1 Why freshness forces self-containment

- `FACT` [E1] Cursor: subagents start with a **clean context**; the parent must include relevant information in the prompt because subagents **do not have access to prior conversation history**. [E1: Cursor Docs — Subagents — https://cursor.com/docs/subagents.md — accessed 2026-07-29]
- `FACT` [E1] Claude Code: each subagent starts with a **fresh, isolated context window**; it does **not** see conversation history, already-invoked skills, or files the parent already read; Claude **composes a delegation message** that summarizes the task. [E1: Claude Code Docs — Create custom subagents — https://code.claude.com/docs/en/sub-agents — accessed 2026-07-29]
- `FACT` [E1] Claude Code: custom subagents receive **only their system prompt plus basic environment details** (e.g. working directory), **not** the full Claude Code system prompt. [E1: same sub-agents page — accessed 2026-07-29]
- `FACT` [E1] Anthropic (engineering): a common failure mode is prompts that are **overly general or falsely assume shared context**; system prompts should be clear, at the right “altitude,” and include the **minimal set of information that fully outlines expected behavior** (minimal ≠ short). [E1: Effective context engineering for AI agents — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — accessed 2026-07-29]
- `FACT` [E1] Claude Code best practices: after writing a complete spec, **start a fresh session to execute it**; the most useful specs are **self-contained**: name files and interfaces, state out-of-scope, end with an **end-to-end verification** step. [E1: Claude Code best practices — https://code.claude.com/docs/en/best-practices — accessed 2026-07-29]
- `INFERENCE` [E4] An implementation plan intended for a fresh agent/subagent must treat the plan (plus explicitly linked, readable artifacts) as the **entire** shared world — chat history is unavailable by product design. Premises: (1) Cursor clean-context FACT; (2) Claude Code isolation FACT; (3) Anthropic “no false shared context” FACT; (4) Claude “self-contained spec + fresh session” FACT.

### 4.2 Self-containment: in-plan vs linked

#### Must be explicit in the plan (or in the handoff packet that *is* the plan slice)

- `FACT` [E1] OpenAI Codex prompting default: include **Goal**, **Context** (files/folders/docs/examples/errors), **Constraints**, and **Done when** (tests, behavior, bug no longer reproduces). [E1: Codex best practices — https://developers.openai.com/codex/learn/best-practices — accessed 2026-07-29]
- `FACT` [E1] Claude Code: self-contained specs name **files and interfaces**, state **what is out of scope**, and end with **e2e verification**. [E1: Claude Code best practices — accessed 2026-07-29]
- `FACT` [E1] Anthropic: organize prompts into distinct sections (e.g. background, tool guidance, output description); use XML/Markdown delineation; prefer **diverse canonical examples** over laundry lists of edge-case rules. [E1: Effective context engineering… — accessed 2026-07-29]
- `FACT` [E1] Microsoft Learn curriculum (agents for beginners): context engineering planning steps — (1) **Define clear results** (“what will the world look like when done?”), (2) **Map the context** the agent needs, (3) **Create context pipelines** (how the agent obtains it: RAG, MCP, tools). [E1: microsoft/ai-agents-for-beginners `12-context-engineering/README.md` — https://raw.githubusercontent.com/microsoft/ai-agents-for-beginners/main/12-context-engineering/README.md — accessed 2026-07-29]
- `FACT` [E1] Cursor Plan Mode: produces a **comprehensive implementation plan** after clarifying questions + codebase research; user reviews/edits before Build; for larger changes, spend time on a **precise, well-scoped plan**. [E1: Cursor Docs — Plan Mode — https://cursor.com/docs/agent/plan-mode — accessed 2026-07-29]
- `FACT` [E0] Superpowers `writing-plans` (structure inventory only): every plan header includes Goal, Architecture, Tech Stack, **Global Constraints**; each task lists Files (create/modify/test paths), **Interfaces (Consumes / Produces)** with exact signatures; steps use checkboxes; **no placeholders** (“TBD”, “add appropriate error handling”, “similar to Task N”). [E0: path=`C:\Users\Jonyc\.cursor\plugins\cache\cursor-public\superpowers\d884ae04edebef577e82ff7c4e143debd0bbec99\skills\writing-plans\SKILL.md` — observed 2026-07-29] `CLAIM` [E3] Same file is a community skill, not Toolbelt SoT. [E3: Superpowers plugin skill]

#### Safe to link (with locator + what to extract)

- `FACT` [E1] Anthropic: agents can keep **lightweight identifiers** (file paths, queries, links) and load data **just-in-time** via tools; hybrid of some upfront context + autonomous retrieval; Claude Code drops `CLAUDE.md` upfront while using glob/grep JIT. [E1: Effective context engineering… — accessed 2026-07-29]
- `FACT` [E1] Codex: keep `AGENTS.md` concise; for large guidance, **reference task-specific markdown** (planning, review, architecture) rather than stuffing everything into one always-on file. [E1: Codex best practices — accessed 2026-07-29]
- `INFERENCE` [E4] For Toolbelt Plan artifacts: **decided requirements, constraints, interfaces, acceptance/verify steps, and out-of-scope** should be **copied or restated in the plan** (or in a per-task handoff packet); **long design rationale, ADR options matrices, and research notes** can stay **linked by path** if the plan states the **binding excerpts** (accepted decisions, interfaces, non-goals) so the executor need not re-derive Design. Premises: (1) Codex Goal/Context/Constraints/Done; (2) Claude self-contained-spec FACT; (3) Anthropic JIT identifiers FACT; (4) campaign brief Plan vs Design separation [E0: `docs/research/notes/theme-6-plan/campaign-brief.md`].
- `GAP` No E1 vendor standard found that specifies a universal “plan ↔ ADR ↔ design-doc” embedding policy (how many lines of ADR to paste vs link). Searched: Cursor plan-mode, Codex best practices, Claude best practices, Anthropic context engineering. Result: vendors describe self-containment and references, not a Toolbelt-grade citation budget.

#### Anti-pattern: forcing the executor to re-derive Design

- `FACT` [E1] Anthropic multi-agent pattern: lead agent holds a **high-level plan**; subagents do focused work and return **condensed summaries** (often ~1k–2k tokens), not full exploration. [E1: Effective context engineering… — accessed 2026-07-29]
- `GAP` No primary doc found that says “link-only to an ADR is always enough for a coding subagent.” Prefer GAP over inventing a paste-vs-link threshold.

### 4.3 Anti-assumption / anti-hallucination patterns

- `FACT` [E1] Anthropic: do **not** falsely assume shared context; be specific enough to guide behavior; tools/contracts should be **unambiguous**. [E1: Effective context engineering… — accessed 2026-07-29]
- `FACT` [E1] Claude Code: give a **check the agent can run** (tests, build, screenshot compare); provide **verification criteria** with concrete examples; have Claude show **evidence** (command + output), not bare assertion. [E1: Claude Code best practices — accessed 2026-07-29]
- `FACT` [E1] Claude Code: adversarial review in a **fresh subagent** sees **only the diff and the criteria you give it**, not the implementer’s reasoning — so the review prompt must name the work, the plan/criteria, and what counts as a finding. [E1: Claude Code best practices — accessed 2026-07-29]
- `FACT` [E1] Codex: encode **constraints and do-not rules** and **what done means / how to verify** in prompts and/or `AGENTS.md`; ask the agent to create/run tests, confirm behavior, review before accept. [E1: Codex best practices — accessed 2026-07-29]
- `FACT` [E1] OpenAI Agents: keep specialists **narrow**; keep `handoffDescription` **short and concrete**; use **structured `outputType`** when downstream needs typed data; put facts the model needs in instructions/input/retrieval/tools. [E1: Orchestration and handoffs — https://developers.openai.com/api/docs/guides/agents/orchestration — accessed 2026-07-29] [E1: Agent definitions (via orchestration “Next steps” / define-agents guide) — https://developers.openai.com/api/docs/guides/agents/define-agents — accessed 2026-07-29]
- `FACT` [E1] OpenAI Agents SDK handoffs: optional **`input_type`** schema for handoff metadata; **`input_filter`** to control what history the next agent sees (default may pass full conversation history — product-specific). [E1: Handoffs — https://openai.github.io/openai-agents-python/handoffs/ — accessed 2026-07-29]
- `FACT` [E1] Microsoft curriculum: context failures include **poisoning** (hallucination enters context and is reused), **clash** (conflicting instructions remain), **confusion** (too many overlapping tools); mitigations include validation/quarantine, pruning superseded instructions, tool loadout management. [E1: microsoft/ai-agents-for-beginners lesson 12 — accessed 2026-07-29]
- `FACT` [E2] LangChain blog synthesizes write/select/compress/isolate; notes multi-agent needs **careful prompt engineering to plan sub-agent work**; cites Cognition on summarization at agent–agent boundaries. [E2: Context Engineering — https://www.langchain.com/blog/context-engineering-for-agents — accessed 2026-07-29]
- `FACT` [E0] Superpowers `writing-plans`: **Global Constraints** copied verbatim from spec; Interfaces Consumes/Produces; every code step shows actual code; every verify step has **exact command + Expected: PASS/FAIL**; ban vague steps. [E0: writing-plans/SKILL.md — observed 2026-07-29] `CLAIM` [E3] Community skill — discovery of structure only; **do not** import its TDD/commit cadence as Toolbelt law. [E3: Superpowers]
- `CLAIM` [E3] Community “spec for AI agents” blogs recommend Always / Ask-first / Never constraint tiers, Given/When/Then acceptance criteria, and writing specs backward from checks. Discovery only — not locks. [E3: e.g. https://www.fundesk.io/how-to-write-specs-ai-coding-agents ; https://pooyagolchian.com/blog/how-to-write-specs-for-ai-agents-2026/ ; https://spec-coding.dev/ai-coding-acceptance-criteria — accessed 2026-07-29]
- `INFERENCE` [E4] Anti-hallucination plan patterns that converge across E1 sources (not a locked checklist): (a) **explicit constraints + out-of-scope / do-not**; (b) **interfaces and file paths named**, not “follow existing patterns” alone; (c) **verify steps with expected signals**; (d) **no TBD placeholders** for decisions the agent would otherwise invent; (e) **fresh-context review against stated criteria**. Premises: Codex; Claude best practices; Anthropic altitude/shared-context; Superpowers E0 structure; Microsoft clash/poisoning.

### 4.4 Task granularity and checkability

- `FACT` [E1] Claude Code: planning most useful when approach uncertain, multi-file, or unfamiliar code; skip plan if the diff is one sentence; implementation should **verify against its plan**. [E1: Claude Code best practices — accessed 2026-07-29]
- `FACT` [E1] Cursor: Plan Mode best for complex/multi-file/unclear/architectural; if Build misses intent, **refine the plan to be more specific** and re-run rather than endless follow-ups. [E1: Cursor Plan Mode — accessed 2026-07-29]
- `FACT` [E1] OpenAI Agents: **start with one agent**; add specialists only when the **contract** (instructions/tools/policy) changes; splitting too early adds prompts/traces without benefit. [E1: Orchestration and handoffs — accessed 2026-07-29]
- `FACT` [E1] Anthropic: lead agent coordinates with a **high-level plan**; subagents get **focused** tasks with clean windows. [E1: Effective context engineering… — accessed 2026-07-29]
- `FACT` [E0] Superpowers `writing-plans`: a task is the smallest unit with its **own test cycle** and worth a reviewer gate; steps often **2–5 minutes / one action**; fold scaffolding into the deliverable’s task; checkbox tracking. [E0: writing-plans/SKILL.md — Task Right-Sizing / Bite-Sized — observed 2026-07-29] `CLAIM` [E3] Community timing heuristic — not empirically validated here; not Toolbelt lock.
- `INFERENCE` [E4] For agent readers, checkability beats narrative: each task should answer **what files**, **what interface contracts**, **what command proves done**, **what must not change**. Premises: Claude verification FACT; Codex Done-when FACT; Superpowers Expected output E0; Cursor “precise plan” FACT.
- `GAP` No E1 source found that mandates a universal minute-budget (e.g. “2–5 minutes”) for Toolbelt tasks. Superpowers timing remains E0/E3 inventory only.

### 4.5 Subagent handoffs vs plan documents

- `FACT` [E1] Cursor: parent includes **all necessary context** in the subagent prompt; subagent returns a **final message** with results. [E1: Cursor Subagents — accessed 2026-07-29]
- `FACT` [E1] Claude Code: use subagents when work is **self-contained** and can return a summary; Explore/Plan built-ins intentionally **skip** `CLAUDE.md` + parent git status for cheap research (custom agents differ). [E1: Claude Code sub-agents — accessed 2026-07-29]
- `FACT` [E1] OpenAI Agents: **handoff** = specialist owns next turn (may see filtered/full history depending on filters); **agent-as-tool** = manager keeps ownership and gets a bounded specialist result. [E1: Orchestration and handoffs — accessed 2026-07-29]
- `INFERENCE` [E4] A Toolbelt **implementation plan** for fresh executors should resemble a **handoff packet** (goal, constraints, interfaces, verify, do-not) more than a chat transcript summary. Premises: Cursor/Claude isolation FACTs; OpenAI ownership patterns; Anthropic condensed return summaries. Full 1..N execution shape deferred to T6C.
- `GAP` Exact recommended token size / section template for Toolbelt plan handoff packets: not specified by E1 sources in this pass.

### 4.6 Optional: Superpowers `writing-plans` structure inventory (not law)

- `FACT` [E0] Observed sections/patterns: Scope Check (split multi-subsystem); File Structure map before tasks; Plan header (Goal/Architecture/Tech Stack/Global Constraints); Task N with Files + Interfaces + checkbox steps; No Placeholders; Self-Review (spec coverage, placeholder scan, type consistency); Execution Handoff to `subagent-driven-development` or `executing-plans`. [E0: writing-plans/SKILL.md — observed 2026-07-29]
- `CLAIM` [E3] Skill also embeds **TDD step order**, **frequent commits**, worktree/execution skill coupling — **explicitly out of T6A locks** per campaign brief. [E3: same skill; campaign-brief non-goals]
- `INFERENCE` [E4] Structure worth *considering* later (post-accept Plan elevation, not this note): Global Constraints; Interfaces Consumes/Produces; exact paths; Expected output on verify steps; placeholder ban; plan self-review against design/spec. Premises: E0 inventory + corroborating E1 FACTs in §§4.2–4.4. **Do not elevate** a Toolbelt skill from this draft alone (`draft-is-not-sot`).

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Fresh-agent plans fail mainly from false shared-context assumptions, not from missing “more prose.” | open | Anthropic altitude FACT; Cursor/Claude isolation FACTs |
| H2 | Binding decisions must be restated in-plan; ADR/design links alone are insufficient for coding subagents. | open | Claude self-contained-spec FACT; GAP on paste budget |
| H3 | Verify-with-expected-signal is the strongest anti-hallucination lever vendors agree on. | open | Claude + Codex E1; Superpowers E0 Expected lines |
| H4 | Superpowers 2–5 min step size is optimal for Toolbelt. | open | E0/E3 only; no E1 corroboration |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| How much history a “handoff” receives | OpenAI Agents handoffs default toward conversation continuity (filterable) [E1] | Cursor/Claude Code coding subagents start clean; parent must brief [E1] | **Product-specific.** For Toolbelt *plan docs* aimed at Cursor/Claude-style fresh subagents, prefer clean-brief model; do not assume OpenAI history semantics. Leave OPEN for T6C. |
| Plan granularity | Superpowers: many tiny TDD steps [E0/E3] | OpenAI: don’t split agents too early [E1]; Claude: skip plan for one-sentence diffs [E1] | Prefer **checkable tasks** over a fixed minute budget; size to uncertainty/multi-file (Claude/Cursor E1). Tiny-step TDD cadence = non-lock. |
| Spec vs plan vs Design | Cursor Plan Mode = implementation plan before Build [E1] | Theme 5: Design/ADR ≠ Plan Mode identity [prior notes; out of T6A re-litigation] | Plan pocket sequences **accepted** design; does not replace Design. |

## 7. Gaps & OPEN

- `GAP` Universal paste-vs-link budget for ADRs / design docs / research notes into plan bodies. Searched: vendor plan/context docs listed in Method. Result: not found.
- `GAP` E1 formal “acceptance criteria schema” for coding-agent plans (Given/When/Then as standard). Searched: vendor docs above; community blogs only (E3). Result: vendors use Done-when / verification criteria / tests; no shared schema.
- `GAP` Alexandria / RAG corroboration of context-engineering + plan-handoff literature (W2).
- `GAP` Empirical eval that Superpowers-style Interfaces + Expected-output blocks reduce requirement hallucination vs prose plans.
- `OPEN` Candidate Toolbelt plan template fields (post W2/W3 + human accept) — not elevating now.
- `OPEN` Whether Plan skill should hard-require “Do not invent / stop and ask” language vs relying on constraints + verify alone.
- `OPEN` T6B/T6C interfaces: how decomposition and 1..N execution reshape the same self-containment rules.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock or skill elevation without separate acceptance.

- `INFERENCE` [E4] A Toolbelt implementation plan for fresh agents should be written as a **standalone handoff**: Goal + binding constraints/do-not + file map + interface contracts + ordered checkable tasks + verify commands with expected signals + explicit out-of-scope — with design/ADR/research **linked for rationale** but **not required to re-derive decisions**. Premises: §§4.1–4.5 FACTs.
- `INFERENCE` [E4] Placeholders and “follow good taste / existing patterns” without named interfaces are **plan defects** for agent executors (hallucination attractors). Premises: Superpowers No Placeholders E0; Anthropic false-shared-context E1; Codex Constraints E1.
- `INFERENCE` [E4] Structure from Superpowers `writing-plans` is a useful **inventory** for later Plan skill drafting; **git/worktree/TDD/commit** couplings stay non-transferable without separate research + accept. Premises: E0 inventory; campaign-brief non-goals; `draft-is-not-sot`.

## 9. Source list (deduped)

1. Anthropic — Effective context engineering for AI agents — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — accessed 2026-07-29 (E1)
2. Claude Code Docs — Create custom subagents — https://code.claude.com/docs/en/sub-agents — accessed 2026-07-29 (E1)
3. Claude Code Docs — Best practices — https://code.claude.com/docs/en/best-practices — accessed 2026-07-29 (E1)
4. Cursor Docs — Plan Mode — https://cursor.com/docs/agent/plan-mode — accessed 2026-07-29 (E1)
5. Cursor Docs — Subagents — https://cursor.com/docs/subagents.md — accessed 2026-07-29 (E1)
6. OpenAI Codex — Best practices — https://developers.openai.com/codex/learn/best-practices — accessed 2026-07-29 (E1)
7. OpenAI — Orchestration and handoffs — https://developers.openai.com/api/docs/guides/agents/orchestration — accessed 2026-07-29 (E1)
8. OpenAI — Agent definitions — https://developers.openai.com/api/docs/guides/agents/define-agents — accessed 2026-07-29 (E1)
9. OpenAI Agents SDK — Handoffs — https://openai.github.io/openai-agents-python/handoffs/ — accessed 2026-07-29 (E1)
10. Microsoft — ai-agents-for-beginners lesson 12 Context Engineering — https://raw.githubusercontent.com/microsoft/ai-agents-for-beginners/main/12-context-engineering/README.md — accessed 2026-07-29 (E1 curriculum)
11. LangChain — Context Engineering — https://www.langchain.com/blog/context-engineering-for-agents — accessed 2026-07-29 (E2)
12. Superpowers `writing-plans/SKILL.md` — local path under `…/superpowers/…/skills/writing-plans/SKILL.md` — observed 2026-07-29 (E0 structure / E3 community)
13. Community blogs (discovery only, E3): fundesk.io specs guide; pooyagolchian.com specs guide; spec-coding.dev acceptance criteria — accessed 2026-07-29
14. Toolbelt — `docs/research/notes/theme-6-plan/campaign-brief.md`, `t6-coordinator-pin.md` — E0 campaign framing
