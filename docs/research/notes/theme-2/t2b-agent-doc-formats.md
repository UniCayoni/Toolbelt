# Theme 2B — Documentation formats & structures for AI/agent consumption

Status: notes only (not integrated report)  
Created: 2026-07-27  
Agent: t2b-agent-doc-formats

## 1. Scope

Documentation **formats and structures** optimized for AI/agent consumption (not only human wiki prose):

- `llms.txt` / llmstxt.org
- `AGENTS.md` conventions
- Diátaxis framework (official)
- Architectural Decision Records (ADR / MADR)
- OpenAPI / JSON Schema as contracts for tools
- “Docs as context” patterns from Cursor / Claude / OpenAI official guidance
- Structured frontmatter, checklists, machine-readable metadata

Audience orientation is labeled per format: **human-oriented**, **agent-oriented**, or **dual**.

## 2. Method

| Item | Detail |
|------|--------|
| Date | 2026-07-27 |
| Tools | WebSearch, WebFetch, Shell (`Invoke-WebRequest` for pages that timed out on WebFetch), Alexandria `list_corpora` + `rag_query` |
| Primary queries | `llms.txt llmstxt.org specification`; `AGENTS.md convention`; `Diátaxis framework official`; `MADR Architectural Decision Records`; `Cursor docs AGENTS.md rules`; `OpenAI Claude Anthropic documentation for AI agents context`; `OpenAPI JSON Schema function calling tools`; `Michael Nygard Architecture Decision Record`; `OpenAI Codex AGENTS.md` |
| Alexandria | Corpus `ai_llm_agents` queried for AGENTS.md / llms.txt / Diátaxis; hits were general agent/RAG books, **not** these format specs → treated as low-signal for this slice |
| Primaries fetched | llmstxt.org; agents.md GitHub README; Cursor Rules docs; Claude Code memory docs; Cognitect Nygard ADR; MADR site; OpenAI Agents SDK context; OpenAI function-calling guide (cached fetch); Diátaxis start-here + explanation (via HTTP); OpenAPI Spec (informational) |

## 3. Findings

### 3.1 Comparison matrix (orientation + role)

| Format | Orientation | Primary job | Machine-parseable? | Best when |
|--------|-------------|-------------|--------------------|-----------|
| `llms.txt` (+ optional `.md` / ctx expand) | **Agent-oriented** (also human-readable Markdown) | Curated site/doc **index** for LLM inference | Spec is Markdown with fixed order; parsers/CLI exist | Public docs sites; packaging “what to read” under context limits |
| `AGENTS.md` | **Agent-oriented** | Repo **instructions** for coding agents | Freeform Markdown; **no** schema | In-repo build/test/style/boundaries for multi-tool agents |
| Cursor `.cursor/rules/*.mdc` | **Agent-oriented** | Conditional, scoped rules | YAML frontmatter (`description`, `globs`, `alwaysApply`) | Cursor-only need for glob/auto/manual activation |
| Claude `CLAUDE.md` / `.claude/rules/` | **Agent-oriented** | Persistent project memory + path-scoped rules | Markdown; rules may use `paths` frontmatter | Claude Code; path-conditional instruction load |
| Diátaxis | **Human-oriented** (authoring framework) | Separate tutorials / how-tos / reference / explanation | No machine schema | Structuring *what* humans (and agents retrieving docs) need; not a file convention for agents |
| ADR (Nygard) / MADR | **Dual** (written for humans; useful agent context) | Record **one** architecturally significant decision | MADR optional YAML status/date/etc.; still prose | Why the system is the way it is; supersession history |
| OpenAPI / JSON Schema | **Machine-first** (contract); docs are secondary | API / tool **parameters & I/O** | Yes (JSON/YAML Schema) | Tool calling, validation, generated clients; not narrative onboarding |
| README / CONTRIBUTING wiki | **Human-oriented** | Humans first; agents may fall back | Usually no | Marketing, contribution UX; keep agent ops out of here when possible |

---

### 3.2 `llms.txt` (llmstxt.org)

- `FACT` — Proposal (Jeremy Howard / Answer.AI lineage) for a Markdown file at `/llms.txt` (or optional subpath) so LLMs get concise, expert-oriented guidance and links instead of scraping HTML with nav/ads/JS. Explicitly motivated by **small context windows**. [E1: llmstxt.org — https://llmstxt.org/index.md — accessed 2026-07-27]
- `FACT` — Spec order: optional BOM → **H1 name (only required section)** → optional blockquote summary → zero+ non-heading detail sections → zero+ **H2 sections of file lists**; each list item is `[name](url)` plus optional `: notes`. [E1: same]
- `FACT` — H2 named **`Optional`** is special: those URLs **may be skipped** when shorter context is needed. [E1: same]
- `FACT` — Companion practice: clean Markdown at same URL + `.md` (or `index.html.md`); tooling such as `llms_txt2ctx` expands links into LLM context files; FastHTML documents `llms-ctx.txt` / `llms-ctx-full.txt` pattern. [E1: same]
- `FACT` — Spec says Markdown was chosen **because** files are expected to be read by language models and agents, while remaining parseable by classical tools. [E1: same]
- `FACT` — Positioned as complementary to `robots.txt` / `sitemap.xml`; expected use mainly at **inference** time, not training (with open speculation if usage spreads). [E1: same]
- `INFERENCE` — Agent-oriented discovery layer for **published documentation**, not a substitute for in-repo coding instructions. Premises: audience is websites/docs; coding agents use repo files like `AGENTS.md` (see §3.3). [E4]

**Orientation:** agent-oriented index; dual readability.

---

### 3.3 `AGENTS.md`

- `FACT` — Open format: “README for agents”; dedicated place for agent context (build steps, tests, conventions) that would clutter a human README. [E1: agentsmd/agents.md README — https://raw.githubusercontent.com/agentsmd/agents.md/main/README.md — accessed 2026-07-27]
- `FACT` — Official sample sections: Dev environment tips, Testing instructions, PR instructions (commands, filters, title format). [E1: same]
- `FACT` — Cursor: `AGENTS.md` is a **plain markdown** alternative to `.cursor/rules`; **no** metadata/globs; supported in root and subdirectories; nested files combine with parents, **more specific take precedence**. [E1: Cursor Rules — https://cursor.com/docs/rules.md — accessed 2026-07-27]
- `FACT` — Cursor Project Rules (`.mdc`) **require** frontmatter fields (`description`, `globs`, `alwaysApply`); plain `.md` under `.cursor/rules` is **ignored**. [E1: same]
- `FACT` — Claude Code reads **`CLAUDE.md`**, not `AGENTS.md`; recommends `@AGENTS.md` import or symlink so one source feeds both. [E1: Claude Code memory — https://code.claude.com/docs/en/memory.md — accessed 2026-07-27]
- `CLAIM` — OpenAI Codex docs (search snippets / secondary mirrors): Codex discovers layered `AGENTS.md` / `AGENTS.override.md` from global `~/.codex` and project path; concatenates root→cwd; default size cap ~**32 KiB** (`project_doc_max_bytes`). Prefer citing Codex guide when re-fetched. [E2/E3: WebSearch synthesis from developers.openai.com/codex/guides/agents-md — fetch 308’d this pass — treat details as OPEN to reconfirm]
- `FACT` — agents.md site FAQ pattern (from earlier search hits aligned with README): no required schema; use any headings; nested monorepo files; closest/later guidance wins depending on tool. [E1: README example; E2: agents.md site summaries]

**Orientation:** agent-oriented; freeform Markdown (portability over structure).

---

### 3.4 Cursor / Claude / OpenAI — “docs as context”

#### Cursor

- `FACT` — Rules inject persistent context at prompt start because models don’t retain memory between completions. [E1: https://cursor.com/docs/rules.md — accessed 2026-07-27]
- `FACT` — Application modes via frontmatter: always / intelligent (description) / globs / manual `@`-mention. Best practices: &lt;500 lines, split rules, concrete examples, **reference files with `@`** instead of copying; avoid dumping entire style guides or rare edge cases. [E1: same]
- `FACT` — Precedence stated for team vs project vs user: Team → Project → User (earlier sources take precedence on conflict). [E1: same]

#### Claude Code

- `FACT` — `CLAUDE.md` + auto memory both load every session; treated as **context, not enforced config**; use hooks to block actions. Target **&lt;200 lines**; specific verifiable bullets; path-scoped `.claude/rules/` with YAML `paths`. [E1: https://code.claude.com/docs/en/memory.md — accessed 2026-07-27]
- `FACT` — Load order: managed policy → user → project → local; tree walk concatenates; closer instructions read later; subdirectory CLAUDE.md loads **on demand** when working in that subtree. [E1: same]
- `FACT` — HTML comments in CLAUDE.md stripped before injection (human-only notes). Imports via `@path` (max depth 4). [E1: same]

#### OpenAI Agents SDK

- `FACT` — Split: **local** `RunContextWrapper.context` (not sent to LLM) vs **LLM context** only via conversation history. LLM-facing tactics: Agent `instructions`, run `input`, function tools (on-demand), retrieval/web search. [E1: https://openai.github.io/openai-agents-python/context/ — accessed 2026-07-27]
- `INFERENCE` — “Docs as context” for agents should prefer: always-on short instructions + **tools/retrieval** for large docs, not stuffing full wikis into system prompts. Premises: SDK guidance above + llms.txt context-window motivation. [E4]

**Orientation:** all three are agent-runtime context mechanisms; Diátaxis/wiki remain content architecture underneath.

---

### 3.5 Diátaxis (official)

- `FACT` — Four kinds of documentation for four needs: **tutorials**, **how-to guides**, **reference**, **explanation**; each written differently. [E1: https://diataxis.fr/start-here/ — accessed 2026-07-27 via HTTP]
- `FACT` — Tutorial = practical **lesson** (learning experience; instructor guides; success/safety). How-to = practical directions for a **competent** user achieving a real-world goal (work, not study). Reference = accurate technical **facts**, propositional, free of distraction; architecture should reflect the thing described. [E1: same]
- `FACT` — Explanation = discursive, **understanding-oriented**, reflective; broader perspective; answer to “Can you tell me about…?”; may be read away from the product. [E1: https://diataxis.fr/explanation/ — accessed 2026-07-27]
- `INFERENCE` — Diátaxis is **human authoring/architecture**; agents benefit when retrieval surfaces the *right type* (e.g. reference for API facts, how-to for procedures). It is not itself an agent file format. Premises: official Diátaxis purpose statements; no agent-schema in Diátaxis site. [E4]

**Orientation:** human-oriented framework; agent-useful as taxonomy for chunking/routing.

---

### 3.6 ADR / MADR

#### Nygard ADR (canonical idea)

- `FACT` — Keep short records of architecturally significant decisions (structure, NFRs, dependencies, interfaces, construction). Format: Title, Context, Decision, Status, Consequences; ~1–2 pages; Markdown in repo (e.g. `doc/arch/adr-NNN.md`); sequential numbers; superseded decisions retained. Write as conversation with future developer. [E1: Cognitect / Michael Nygard — https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — accessed 2026-07-27]
- `FACT` — Status values include proposed / accepted / deprecated / superseded. [E1: same]

#### MADR

- `FACT` — Markdown Architectural Decision Records: lean Markdown template for ADRs; copy to `docs/decisions/NNNN-title-with-dashes.md`. [E1: https://adr.github.io/madr/ — accessed 2026-07-27]
- `FACT` — Full template sections include optional YAML (status, date, decision-makers, consulted, informed) plus Context and Problem Statement, Decision Drivers, Considered Options, Decision Outcome (+ Consequences, Confirmation), Pros and Cons, More Information. Minimal templates exist. [E1: same]
- `INFERENCE` — Dual: written for humans; for agents, ADRs are high-signal **rationale** context (why not what) complementary to `AGENTS.md` (how to operate). Premises: Nygard “future developer”; AGENTS.md purpose from agents.md. [E4]

**Orientation:** dual (human decision log; agent rationale corpus).

---

### 3.7 OpenAPI / JSON Schema as tool contracts

- `FACT` — OpenAPI Description is a JSON object (JSON or YAML). Spec text is normative; hosted JSON Schema for OAS is informational. Schema Objects relate to JSON Schema (OAS 3.1+ aligned with JSON Schema Draft 2020-12 concepts). [E1: OpenAPI Specification — https://spec.openapis.org/oas/latest.html — accessed 2026-07-27]
- `FACT` — OpenAI function/tool calling: a **function** tool is defined by a **JSON schema** for parameters; model returns structured arguments; app executes and returns tool output. Flow: define tools → model tool call → execute → return output → continue. [E1: OpenAI Function calling — https://developers.openai.com/api/docs/guides/function-calling — accessed 2026-07-27]
- `INFERENCE` — For agent systems, OpenAPI/JSON Schema are the right **contract** layer for callable tools and APIs; narrative docs (Diátaxis reference) should stay consistent with schemas but schemas win for validation. Premises: OpenAI tool schema requirement; OAS Schema Object role. [E4]
- `GAP` — No primary in this pass asserting “publish OpenAPI *as* AGENTS.md replacement”; they solve different layers (I/O contract vs behavioral instructions).

**Orientation:** machine-first contracts; human docs generated/secondary.

---

### 3.8 Structured frontmatter, checklists, metadata

- `FACT` — Cursor `.mdc` frontmatter drives **when** rules enter context (`alwaysApply`, `description`, `globs`). [E1: Cursor Rules]
- `FACT` — Claude `.claude/rules/` optional YAML `paths:` for path-specific load. [E1: Claude memory]
- `FACT` — MADR optional YAML for status/date/decision-makers (human + tooling/nav metadata). [E1: MADR]
- `FACT` — `AGENTS.md` / `llms.txt` deliberately **avoid** mandatory YAML schemas (Markdown-first for LLM readability / portability). [E1: llmstxt.org; agents.md README; Cursor AGENTS.md section]
- `INFERENCE` — Use frontmatter when the **runtime** needs activation metadata (Cursor/Claude rules); keep portable agent instructions as plain Markdown; use schemas for executable contracts. Premises: above FACTS. [E4]
- `CLAIM` — Community guidance often recommends short checklists/commands in AGENTS.md (e.g. “under 150 lines”) — useful but not a single primary standard; verify per tool. [E3]

## 4. Contradictions / conflicts

| Topic | Conflict | Resolution for integrator |
|-------|----------|---------------------------|
| Single instruction file name | `AGENTS.md` (open) vs `CLAUDE.md` (Claude Code) vs `.cursor/rules/*.mdc` (Cursor) | Prefer `AGENTS.md` as portable SoT; Claude imports via `@AGENTS.md`; Cursor uses AGENTS.md **plus** `.mdc` only when globs/modes needed. [E1: Claude memory; Cursor rules] |
| Nested precedence | Cursor: combine with more specific precedence; Codex (claimed): concatenate root→cwd with later override; Claude: concatenate, closer last | Same *idea* (local wins) but merge semantics differ — **do not assume one merge algorithm**. [E1 Cursor/Claude; OPEN Codex] |
| Structured vs freeform | llms.txt/AGENTS.md freeform Markdown vs Cursor/Claude frontmatter vs OpenAPI schemas | Different layers: discovery / behavior / activation / I/O. |
| Diátaxis vs agent files | Diátaxis organizes human docs; agent files organize model prompts | Complementary, not competing. |
| Alexandria | Query did not surface llms.txt/AGENTS.md/Diátaxis primaries | Do not use Alexandria hits as evidence for this slice. |

## 5. Gaps

- `GAP` — Direct WebFetch of https://agents.md/ and https://diataxis.fr/ timed out; Diátaxis recovered via HTTP; agents.md recovered via GitHub raw README (site FAQ pages partially from search snippets).
- `GAP` — OpenAI Codex AGENTS.md guide returned HTTP 308 on this host; discovery/32KiB details need primary re-fetch.
- `GAP` — No GreyMatter-local examples of these formats yet (E0 empty for project adoption).
- `GAP` — Mintlify/`llms-full.txt` origin story appears in secondary blogs; official llmstxt.org emphasizes `.md` companions and `llms_txt2ctx` — treat `llms-full.txt` naming as **OPEN** unless confirmed on llmstxt.org.
- `GAP` — Formal JSON Schema for AGENTS.md / llms.txt: intentionally absent; any “strict template” would be local convention only.
- `OPEN` — Whether GreyMatter public docs should ship `/llms.txt` vs repo-only `AGENTS.md` (product decision, not evidenced).
- `OPEN` — Best mapping of Diátaxis types → RAG chunk metadata labels for agents.

## 6. Candidate patterns for templates (cited / grounded)

Use only as **skeletons** derived from primaries — not GreyMatter locks.

### 6.1 `llms.txt` skeleton [E1: llmstxt.org]

```markdown
# {ProjectOrSiteName}

> {One-sentence summary with key facts for interpreting the rest}

{Optional short guidance on how to use linked files}

## Docs
- [{Title}](https://example.com/path.md): {notes}

## Optional
- [{Secondary}](https://example.com/other.md)
```

### 6.2 `AGENTS.md` skeleton [E1: agents.md README + Cursor example]

```markdown
# {Project} agent instructions

## Dev environment / commands
- {exact install/build/test commands}

## Code / architecture conventions
- {short, verifiable bullets}

## Testing / PR
- {how to verify; title format}

## Boundaries
- {do-not / never-touch}
```

### 6.3 Cursor rule frontmatter [E1: Cursor Rules]

```markdown
---
description: "{when agent should pull this in}"
globs: src/**/*.ts
alwaysApply: false
---
- {actionable rule}
```

### 6.4 Claude path-scoped rule [E1: Claude memory]

```markdown
---
paths:
  - "src/api/**/*.ts"
---
# API rules
- {concrete requirement}
```

### 6.5 MADR bare outline [E1: MADR]

```markdown
---
status: "{proposed|accepted|…}"
date: {YYYY-MM-DD}
---
# {short title}

## Context and Problem Statement
{…}

## Decision Drivers
- {…}

## Considered Options
- {…}

## Decision Outcome
Chosen option: "{…}", because {…}.
```

### 6.6 Nygard minimal ADR [E1: Cognitect]

```markdown
# ADR {N}: {Title}

## Status
{Proposed|Accepted|Superseded by ADR-M}

## Context
{forces, value-neutral}

## Decision
We will …

## Consequences
{positive, negative, neutral}
```

### 6.7 Function tool schema shape [E1: OpenAI function calling]

```json
{
  "type": "function",
  "name": "{tool_name}",
  "description": "{when to call}",
  "parameters": {
    "type": "object",
    "properties": {},
    "required": []
  }
}
```

### 6.8 When to use which (integrator cheat sheet)

| Need | Prefer |
|------|--------|
| Public docs discovery under context limits | `llms.txt` + `.md` pages |
| Cross-tool repo coding instructions | `AGENTS.md` |
| Cursor-only conditional/scoped rules | `.cursor/rules/*.mdc` |
| Claude path-scoped / memory | `CLAUDE.md` + `.claude/rules/` (import AGENTS.md) |
| Human doc IA / writing quality | Diátaxis types |
| Decision rationale history | ADR/MADR |
| Tool/API I/O enforcement | JSON Schema / OpenAPI |
| Large knowledge on demand | Retrieval/tools (OpenAI SDK pattern), not always-on paste |

## 7. Source list (deduped)

1. https://llmstxt.org/index.md — llms.txt proposal/spec  
2. https://raw.githubusercontent.com/agentsmd/agents.md/main/README.md — AGENTS.md format  
3. https://agents.md/ — AGENTS.md site (WebFetch timeout; content partially via search)  
4. https://cursor.com/docs/rules.md — Cursor Rules + AGENTS.md  
5. https://code.claude.com/docs/en/memory.md — CLAUDE.md / rules / AGENTS.md import  
6. https://diataxis.fr/start-here/ — Diátaxis four types  
7. https://diataxis.fr/explanation/ — Explanation type  
8. https://diataxis.fr/ — Diátaxis home  
9. https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — Nygard ADR  
10. https://adr.github.io/madr/ — MADR  
11. https://github.com/adr/madr — MADR repo/templates  
12. https://openai.github.io/openai-agents-python/context/ — LLM vs local context  
13. https://developers.openai.com/api/docs/guides/function-calling — JSON Schema tools  
14. https://spec.openapis.org/oas/latest.html — OpenAPI Specification  
15. https://developers.openai.com/codex/guides/agents-md — Codex AGENTS.md (OPEN: 308 this pass)  
16. https://www.answer.ai/posts/2024-09-03-llmstxt.html — Answer.AI announcement (overlaps llmstxt.org)  
17. Alexandria corpus `ai_llm_agents` — queried; **no high-value primary hits** for this slice  

---

*End of notes. Integrator should merge without inventing facts; retain OPEN/GAP labels.*
