# Theme 1B — Web agent workspace / repo research patterns

Status: notes only (not integrated report)  
Access date for citations: 2026-07-27  
Agent id: `t1b-web-agent-workspace-patterns`

## 1. Scope

Public, primary documentation on how AI coding agents are instructed to research workspaces/repos:

- `AGENTS.md` / agent instruction files
- Cursor rules / skills / hooks exploration guidance (official Cursor docs only for Cursor claims)
- `llms.txt` / llmstxt.org
- Repo maps and codebase indexing patterns described by tool vendors (Cursor, Continue, Aider, Claude Code, Codex, Copilot/VS Code)
- “Explore before edit” / reconnaissance patterns in official agent docs

Out of scope: plugin scaffolding; locking GreyMatter implementation choices.

## 2. Method

| Item | Detail |
|------|--------|
| Date | 2026-07-27 |
| Tools | WebSearch, WebFetch |
| Preference | E1 official docs / specs / vendor docs; E3 only for forum/blog |
| Not assumed | Undocumented APIs, private agent system prompts, unpublished indexing algorithms |

### Queries (representative)

- `AGENTS.md agent instruction file specification documentation`
- `llms.txt llmstxt.org specification official documentation`
- `Cursor docs codebase indexing rules skills hooks AGENTS.md site:cursor.com/docs`
- `Claude Code CLAUDE.md explore codebase documentation official Anthropic`
- `Aider repository map repo-map documentation official`
- `Continue.dev codebase indexing documentation official`
- `OpenAI Codex AGENTS.md coding agent documentation`
- `GitHub Copilot custom instructions repository AGENTS.md official docs`
- `Cursor Explore subagent documentation site:cursor.com/docs`

### Primary URLs fetched / used

- https://agents.md/
- https://llmstxt.org/
- https://cursor.com/docs/rules.md
- https://cursor.com/docs/skills.md
- https://cursor.com/docs/hooks.md (search-result body + prior fetch content)
- https://cursor.com/docs/agent/tools/search.md
- https://cursor.com/docs/subagents.md
- https://cursor.com/docs/agent/prompting.md
- https://cursor.com/docs/reference/ignore-file.md
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/large-codebases
- https://code.claude.com/docs/en/best-practices
- https://developers.openai.com/codex/guides/agents-md (via developers.openai.com/codex/llms-full.txt)
- https://developers.openai.com/codex/learn/best-practices
- https://aider.chat/docs/repomap.html
- https://aider.chat/2023/10/22/repomap.html
- https://docs.continue.dev/guides/codebase-documentation-awareness
- https://docs.continue.dev/customize/deep-dives/custom-providers
- https://docs.continue.dev/reference/deprecated-codebase
- https://docs.github.com/en/copilot/reference/custom-instructions-support
- https://code.visualstudio.com/docs/agent-customization/custom-instructions
- https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/ (changelog = E1 for “supports AGENTS.md” announcement)

## 3. Findings

### 3.1 AGENTS.md (cross-tool instruction file)

- `FACT` [E1] `AGENTS.md` is positioned as a README complementary to human `README.md`: agent-focused build/test/conventions that would clutter human docs. No required fields; standard Markdown. Stewarded by the Agentic AI Foundation under the Linux Foundation. [E1: agents.md — https://agents.md/ — accessed 2026-07-27]

- `FACT` [E1] Recommended content areas (popular choices, not schema): project overview; build and test commands; code style; testing instructions; security considerations; plus extras (commits/PRs, datasets, deployment). [E1: agents.md — https://agents.md/ — accessed 2026-07-27]

- `FACT` [E1] Nested monorepo pattern: place `AGENTS.md` per package; “closest one takes precedence”; user chat prompts override file instructions. Example claim on agents.md: OpenAI main repo had 88 `AGENTS.md` files at time of writing. [E1: agents.md — https://agents.md/ — accessed 2026-07-27]

- `FACT` [E1] FAQ states agents will attempt to run testing commands listed in `AGENTS.md` and fix failures before finishing (behavior claim from the standard site; actual tool adherence varies by product). [E1: agents.md — https://agents.md/ — accessed 2026-07-27]

- `FACT` [E1] Migration tips on agents.md: symlink/rename from older names; Aider config `read: AGENTS.md` in `.aider.conf.yml`; Gemini CLI `context.fileName: "AGENTS.md"` in `.gemini/settings.json`. [E1: agents.md — https://agents.md/ — accessed 2026-07-27]

### 3.2 OpenAI Codex — AGENTS.md discovery and “before work”

- `FACT` [E1] Codex “reads `AGENTS.md` files before doing any work.” Discovery: (1) global `~/.codex/AGENTS.override.md` else `AGENTS.md`; (2) walk from project root to CWD, at most one file per directory (`AGENTS.override.md` then `AGENTS.md` then fallbacks); (3) concatenate root→leaf so closer files appear later and override. Combined size capped by `project_doc_max_bytes` (default 32 KiB). [E1: Codex AGENTS.md guide via llms-full — https://developers.openai.com/codex/guides/agents-md — accessed 2026-07-27]

- `FACT` [E1] Best-practice content for Codex `AGENTS.md`: repo layout; how to run; build/test/lint; conventions/PR expectations; do-not rules; definition of done / verification. Prefer short accurate files; `/init` scaffolds then edit; update after repeated mistakes; progressive disclosure via referenced markdown when large. [E1: Codex best practices — https://developers.openai.com/codex/learn/best-practices — accessed 2026-07-27]

- `FACT` [E1] Codex prompting pattern for workspace work: Goal / Context / Constraints / Done when; Plan mode for complex tasks; use subagents for exploration/tests/triage so main thread stays focused. [E1: Codex best practices — https://developers.openai.com/codex/learn/best-practices — accessed 2026-07-27]

- `FACT` [E1] Hierarchical guidance also documented in Codex source message for agents: deeper `AGENTS.md` overrides higher; system/developer/user prompts outrank all `AGENTS.md`. [E1: openai/codex hierarchical_agents_message.md — https://github.com/openai/codex/blob/main/codex-rs/core/hierarchical_agents_message.md — accessed 2026-07-27]

### 3.3 Cursor — rules, AGENTS.md, skills, hooks, indexing, explore

- `FACT` [E1] Cursor rule types: Project (`.cursor/rules/*.mdc` with frontmatter), User, Team, and `AGENTS.md` as simple alternative without metadata. Applied rules are included at the start of model context. Plain `.md` in `.cursor/rules` is ignored (needs frontmatter). [E1: Cursor Rules — https://cursor.com/docs/rules.md — accessed 2026-07-27]

- `FACT` [E1] Project rule application modes via `alwaysApply` / `description` / `globs`: always; auto-attach by globs; agent-selected by description; manual `@`-mention. Best practices: keep under 500 lines; split; concrete examples; reference files with `@` instead of copying; avoid dumping style guides/commands the agent already knows; add rules after repeated mistakes. Example rule text includes “read the relevant source files before proposing changes.” [E1: Cursor Rules — https://cursor.com/docs/rules.md — accessed 2026-07-27]

- `FACT` [E1] Nested `AGENTS.md` supported; combined with parents; more specific takes precedence. Precedence when merging rule sources: Team → Project → User (earlier takes precedence on conflict). [E1: Cursor Rules — https://cursor.com/docs/rules.md — accessed 2026-07-27]

- `FACT` [E1] Skills: open standard (`agentskills.io`); discovered from `.agents/skills/`, `.cursor/skills/`, user-level mirrors, plus Claude/Codex skill dirs for compatibility. Each skill is a folder with `SKILL.md` (required `name`, `description`; optional `paths`, `disable-model-invocation`). Progressive loading of `scripts/`, `references/`, `assets/`. Nested package skills auto-scoped to that directory. Agent decides relevance; manual `/skill-name` also works. [E1: Cursor Skills — https://cursor.com/docs/skills.md — accessed 2026-07-27]

- `FACT` [E1] Hooks: `hooks.json` at project (`.cursor/hooks.json`) or user (`~/.cursor/hooks.json`); stdio JSON; lifecycle includes `sessionStart`/`sessionEnd`, `preToolUse`/`postToolUse`, `beforeReadFile`/`afterFileEdit`, shell/MCP hooks, etc. Can observe, block, or modify agent loop. Cloud agents run project hooks, not user-home hooks. [E1: Cursor Hooks — https://cursor.com/docs/hooks.md — accessed 2026-07-27]

- `FACT` [E1] Indexing / search: Cursor indexes codebase for features; `.cursorignore` blocks Agent/Tab/Inline/@ access (terminal/MCP not blocked by ignore); `.cursorindexingignore` excludes from indexing/search only while leaving files AI-accessible; respects `.gitignore` + default ignore list. Embeddings: docs state filenames obfuscated, chunks encrypted, no plaintext source stored; team index sharing with permission respect. Multi-root workspaces indexed; Cloud Agents do not support multi-root. [E1: Cursor ignore-file — https://cursor.com/docs/reference/ignore-file.md — accessed 2026-07-27] [E1: Cursor Search — https://cursor.com/docs/agent/tools/search.md — accessed 2026-07-27]

- `FACT` [E1] Explore-before-edit tooling: Instant Grep for exact/regex symbol search; Agent can spawn built-in **Explore** subagent (own context, faster model, parallel searches, returns summaries). Auto-invoked for broad search or on user request. Prompting docs: if unsure which files matter, skip `@` attachments — Agent finds files via its own search. [E1: Cursor Search — https://cursor.com/docs/agent/tools/search.md — accessed 2026-07-27] [E1: Cursor Subagents — https://cursor.com/docs/subagents.md — accessed 2026-07-27] [E1: Cursor Prompting — https://cursor.com/docs/agent/prompting.md — accessed 2026-07-27]

### 3.4 Claude Code — CLAUDE.md, large repos, explore-first

- `FACT` [E1] Claude Code reads `CLAUDE.md` (or `./.claude/CLAUDE.md`), not `AGENTS.md` natively. Interop: `@AGENTS.md` import in `CLAUDE.md`, or symlink `CLAUDE.md` → `AGENTS.md`. `/init` analyzes codebase (and can explore with subagent under `CLAUDE_CODE_NEW_INIT=1`) to draft CLAUDE.md; can incorporate Cursor/Copilot rules. Target under ~200 lines; path-scoped `.claude/rules/`; `@` imports (max 4 hops). Subdirectory CLAUDE.md loads on demand when files there are read. [E1: Claude Code memory — https://code.claude.com/docs/en/memory — accessed 2026-07-27]

- `FACT` [E1] Large/monorepo guidance: start Claude from package dir to scope file access + which CLAUDE.md load; layer root + per-package CLAUDE.md; `claudeMdExcludes`; deny `Read` of generated/vendored paths; code intelligence plugins (LSP) to reduce file scans; per-directory skills; sparse worktrees. [E1: Claude Code large-codebases — https://code.claude.com/docs/en/large-codebases — accessed 2026-07-27]

- `FACT` [E1] Official “Explore first, then plan, then code”: use plan mode to separate exploration from execution; example prompts ask Claude to read specific areas and understand before implementing. “Use subagents for investigation” so file reads stay out of main context; warn against “infinite exploration” without scope. Onboarding: ask Claude exploratory Qs as you would another engineer. CLAUDE.md vs hooks: instructions are context not enforcement; use PreToolUse hooks to hard-block. [E1: Claude Code best practices — https://code.claude.com/docs/en/best-practices — accessed 2026-07-27]

### 3.5 Aider — repository map

- `FACT` [E1] Aider sends a concise repo map with each change request: files + key symbols (classes/functions) with definition lines/signatures. For large repos, graph ranking over file-dependency graph selects map portions within `--map-tokens` budget (default ~1k tokens); map expands when few/no files are in chat. Map helps LLM decide which files to request next. [E1: Aider Repository map — https://aider.chat/docs/repomap.html — accessed 2026-07-27]

- `FACT` [E1] Construction: tree-sitter ASTs extract definitions/references; rank important identifiers; formerly ctags. Blog frames three steps for large-repo edits: (1) find code to change, (2) understand relation to rest of codebase, (3) make change — repo map targets (2). [E1: Aider blog tree-sitter repomap — https://aider.chat/2023/10/22/repomap.html — accessed 2026-07-27]

### 3.6 Continue — indexing, rules, agent exploration, repo-map provider

- `FACT` [E1] Current Agent-mode guidance: use built-in file exploration/search/git tools; put project architecture/standards in `.continue/rules`; for external code/docs use rules with links, `gh`/`glab`, DeepWiki MCP, Context7 MCP, or custom MCP/RAG. `@Codebase` / `@Folder` / `@Docs` context providers are **deprecated** in favor of that approach. [E1: Continue codebase awareness guide — https://docs.continue.dev/guides/codebase-documentation-awareness — accessed 2026-07-27]

- `FACT` [E1] Legacy `@Codebase` docs (preserved): local embeddings (`transformers.js`) + keyword search; index in `~/.continue/index`; ignore via `.gitignore` / `.continueignore`; params `nRetrieve`/`nFinal`/`useReranking`; not useful for exhaustive “find every call site” or full-repo spelling reviews. [E1: Continue deprecated @Codebase — https://docs.continue.dev/reference/deprecated-codebase — accessed 2026-07-27]

- `FACT` [E1] `@Repository Map` context provider still documented: outline of files + top-level signatures; `includeSignatures` default true; inspired by Aider’s repo map; signatures omitted if indexing disabled. Also `@Tree` for workspace structure. [E1: Continue context providers — https://docs.continue.dev/customize/deep-dives/custom-providers — accessed 2026-07-27]

### 3.7 GitHub Copilot / VS Code — instruction file matrix

- `FACT` [E1] Support matrix varies by product surface. Copilot cloud agent: `.github/copilot-instructions.md`, path-specific `.github/instructions/**/*.instructions.md`, and agent instructions via `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` (plus org instructions on github.com). Copilot Chat on github.com does **not** list `AGENTS.md` in the matrix (personal + repo-wide + org). [E1: GitHub Copilot custom instructions support — https://docs.github.com/en/copilot/reference/custom-instructions-support — accessed 2026-07-27]

- `FACT` [E1] Changelog: Copilot coding agent supports root and nested `AGENTS.md` alongside existing GitHub instruction formats. [E1: GitHub Changelog 2025-08-28 — https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/ — accessed 2026-07-27]

- `FACT` [E1] VS Code: `.github/copilot-instructions.md` for project-wide; `.instructions.md` for path/type-specific; `AGENTS.md` for multi-agent / nested monorepo instructions (settings `chat.useAgentsMdFile`, nested via `chat.useNestedAgentsMdFiles`). Nested AGENTS.md: relative paths added to context; agent decides which to use based on files being edited. [E1: VS Code custom instructions — https://code.visualstudio.com/docs/agent-customization/custom-instructions — accessed 2026-07-27]

### 3.8 llms.txt (site/docs map for LLMs — not a coding-agent repo protocol)

- `FACT` [E1] Spec at llmstxt.org: `/llms.txt` (or subpath) Markdown in fixed order — H1 name (required), optional blockquote summary, optional non-heading detail, then H2 sections of link lists `- [name](url): notes`. Special H2 `Optional` = skippable under context pressure. Complements robots.txt/sitemaps; proposal also suggests `.md` mirrors of HTML pages. Processing method intentionally unspecified; FastHTML example expands to `llms-ctx.txt` / `llms-ctx-full.txt`. [E1: llms.txt — https://llmstxt.org/ — accessed 2026-07-27]

- `INFERENCE` [E4] Premises: (P1) llms.txt indexes curated web/docs URLs for LLM inference; (P2) AGENTS.md/CLAUDE.md/.cursor/rules encode in-repo agent behavior and workspace commands. → Conclusion: llms.txt is a **documentation discovery** pattern for websites, not a substitute for repo agent instruction files, though both are Markdown “maps” for agents. [E4 from E1 premises above]

- `CLAIM` [E3] Secondary blogs report major LLM crawlers may not formally consume llms.txt; treat adoption claims as unverified for GreyMatter design locks. [E3: Ahrefs blog — https://ahrefs.com/blog/what-is-llms-txt/ — accessed 2026-07-27]

### 3.9 Cross-cutting reconnaissance / “explore before edit” patterns

- `FACT` [E1] Multiple vendors document **plan/explore then implement**: Claude Code plan mode + explore-first; Codex Plan mode + Goal/Context/Constraints/Done; Cursor Explore subagent + “Agent finds files if you don’t `@` them”. [E1: Claude best practices; Codex best practices; Cursor prompting/search — accessed 2026-07-27]

- `FACT` [E1] Context isolation for exploration is a recurring product pattern: Cursor Explore/Bash/Browser subagents; Claude Code investigation subagents; Codex subagents for exploration. Shared rationale: search/read noise should not fill the main implementation context. [E1: Cursor subagents; Claude best practices; Codex best practices — accessed 2026-07-27]

- `FACT` [E1] Structural context injection differs: Aider/Continue repo-map (symbol outline under token budget); Cursor semantic embeddings + Instant Grep; Continue migrating from embedding `@Codebase` toward tool-driven exploration + rules/MCP; Claude optional LSP plugins for symbol navigation. [E1: sources in §§3.3–3.6 — accessed 2026-07-27]

- `FACT` [E1] Instruction files are the durable “how to research/work this repo” layer: exact commands, layout, do-nots, verification — with nesting/scoping to avoid loading irrelevant monorepo conventions. [E1: agents.md; Codex AGENTS.md; Cursor rules; Claude memory/large-codebases — accessed 2026-07-27]

## 4. Contradictions / conflicts found

1. **Native instruction filename**
   - agents.md / Codex / Cursor / Copilot agent: `AGENTS.md`
   - Claude Code: `CLAUDE.md` only (interop via import/symlink)
   - Copilot Chat (github.com matrix): repo-wide `.github/copilot-instructions.md`, not AGENTS.md
   - Continue: `.continue/rules` (not AGENTS.md as primary)

2. **Nested file merge semantics**
   - agents.md FAQ: “closest wins”
   - Cursor nested AGENTS.md: “combined… more specific taking precedence”
   - Codex: concatenate root→leaf; later (closer) overrides earlier
   - Claude CLAUDE.md: concatenate all ancestors at launch; subdirectory files on demand (not the same as Codex override file)
   - VS Code nested AGENTS.md: paths listed in context; agent **decides** which to use
   → Same filename, **different merge/priority implementations**.

3. **Indexing strategy direction**
   - Cursor: active embeddings + Instant Grep + Explore subagent
   - Continue: deprecating `@Codebase` embeddings UX toward agent tools + MCP; still documents `@repo-map` and legacy index paths
   - Aider: symbolic tree-sitter map, not embeddings-centric in primary docs

4. **Size / budget limits**
   - Codex: hard default 32 KiB combined `AGENTS.md` budget
   - Claude: soft ~200 lines / CLAUDE.md guidance + auto-memory first 200 lines or 25KB
   - Cursor rules: soft &lt;500 lines per rule
   - Aider map: default ~1k tokens for map slice
   → No shared numeric standard.

5. **llms.txt vs agent instruction files**
   - Both Markdown maps for machines; different location (web root vs repo) and purpose (docs links vs build/edit conventions). Do not conflate.

## 5. Gaps

- `GAP` No single formal RFC/schema for `AGENTS.md` content beyond “standard Markdown” on agents.md; DeepWiki/third-party “spec” pages are secondary and were not treated as E1.
- `GAP` Cursor docs describe embeddings privacy and ignore files but do **not** publish a public algorithm comparable to Aider’s tree-sitter + PageRank write-up.
- `GAP` Official hooks docs describe `beforeReadFile` / lifecycle control; they do **not** mandate an “explore before edit” workflow — that remains agent/rules/skills guidance, not hook-enforced by default.
- `GAP` Major LLM provider **first-class crawl support** for llms.txt not evidenced as E1 in this pass (only proposal + tooling).
- `GAP` Did not deeply fetch Windsurf/Devin/Amp/Jules proprietary workspace-recon docs beyond agents.md ecosystem mentions.
- `GAP` Exact Copilot CLI discovery order for multiple concurrent instruction files was only partially covered via VS Code/GitHub support matrix (full CLI how-to page not fully fetched this pass).
- `OPEN` Whether GreyMatter templates should prefer one instruction filename (`AGENTS.md`) plus adapters (`CLAUDE.md` import) vs generating multiple vendor files.
- `OPEN` Whether GreyMatter research protocol should mirror Cursor Explore / Claude “investigation subagent” as a required step before edits (product choice, not forced by a universal standard).

## 6. Candidate patterns for templates (still cited)

These are **candidate steps** for GreyMatter research/agent templates, derived from E1 patterns — not locked design.

1. **Instruction file bootstrap** — Create root agent instructions covering: layout, exact build/test/lint commands, conventions, security do-nots, definition of done. Prefer `AGENTS.md` as portable baseline; add Claude `CLAUDE.md` that `@AGENTS.md` imports where needed. [E1: agents.md; Codex AGENTS.md; Claude memory]

2. **Progressive disclosure** — Keep root instruction file short; nest per-package/subdir instructions; use path-scoped rules/skills for domain workflows; point to deeper docs instead of inlining. [E1: agents.md nested; Cursor skills/rules; Claude rules/skills; Codex “reference task-specific markdown”]

3. **Explore → plan → edit** — Template steps: (a) recon with search/subagent, (b) plan/clarify, (c) edit, (d) run verification commands from instruction file. [E1: Claude best practices; Codex best practices; Cursor Explore/prompting]

4. **Context isolation for recon** — Delegate broad codebase search to a subagent/explore role; return summaries only into the main implementation thread. [E1: Cursor subagents; Claude “use subagents for investigation”; Codex subagents]

5. **Structural map when available** — Prefer a symbol/outline map (Aider-style / Continue `@repo-map`) or semantic search + exact grep (Cursor) before bulk file dumps; budget token use. [E1: Aider repomap; Continue repo-map; Cursor search]

6. **Ignore / deny noise** — Configure ignore lists for secrets, lockfiles, build artifacts, vendored trees so indexing and agent reads stay relevant (`.cursorignore` / `.cursorindexingignore`, `.continueignore`, Claude `permissions.deny` Reads, gitignore). [E1: Cursor ignore-file; Continue deprecated codebase; Claude large-codebases]

7. **Living feedback loop** — When the agent repeats a mistake, update the instruction file (and optionally hooks/linters for hard enforcement). [E1: Cursor rules best practices; Codex AGENTS.md “retrospective”; Claude “when to add to CLAUDE.md”; hooks for hard blocks]

8. **Docs map for external libraries** — For website/docs corpora (not the git tree itself), consider `/llms.txt` curated link maps + `.md` page mirrors; do not treat as repo agent config. [E1: llmstxt.org]

9. **Multi-tool interop** — Expect parallel instruction ecosystems (`.github/copilot-instructions.md`, `.cursor/rules`, `.continue/rules`, `CLAUDE.md`); template generators may need adapters or single-source + imports. [E1: GitHub support matrix; Cursor rules; Continue awareness guide; Claude AGENTS.md import]

## 7. Source list (deduped)

| Source | URL | Grade |
|--------|-----|-------|
| AGENTS.md home | https://agents.md/ | E1 |
| llms.txt proposal | https://llmstxt.org/ | E1 |
| Cursor Rules | https://cursor.com/docs/rules.md | E1 |
| Cursor Skills | https://cursor.com/docs/skills.md | E1 |
| Cursor Hooks | https://cursor.com/docs/hooks.md | E1 |
| Cursor Search | https://cursor.com/docs/agent/tools/search.md | E1 |
| Cursor Subagents | https://cursor.com/docs/subagents.md | E1 |
| Cursor Prompting | https://cursor.com/docs/agent/prompting.md | E1 |
| Cursor Ignore files | https://cursor.com/docs/reference/ignore-file.md | E1 |
| Claude Code Memory | https://code.claude.com/docs/en/memory | E1 |
| Claude Code Large codebases | https://code.claude.com/docs/en/large-codebases | E1 |
| Claude Code Best practices | https://code.claude.com/docs/en/best-practices | E1 |
| Codex AGENTS.md guide | https://developers.openai.com/codex/guides/agents-md | E1 |
| Codex Best practices | https://developers.openai.com/codex/learn/best-practices | E1 |
| Codex hierarchical AGENTS message | https://github.com/openai/codex/blob/main/codex-rs/core/hierarchical_agents_message.md | E1 |
| Aider Repository map | https://aider.chat/docs/repomap.html | E1 |
| Aider tree-sitter repomap blog | https://aider.chat/2023/10/22/repomap.html | E1 |
| Continue codebase awareness | https://docs.continue.dev/guides/codebase-documentation-awareness | E1 |
| Continue context providers | https://docs.continue.dev/customize/deep-dives/custom-providers | E1 |
| Continue deprecated @Codebase | https://docs.continue.dev/reference/deprecated-codebase | E1 |
| GitHub Copilot instructions support | https://docs.github.com/en/copilot/reference/custom-instructions-support | E1 |
| GitHub Changelog AGENTS.md | https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/ | E1 |
| VS Code custom instructions | https://code.visualstudio.com/docs/agent-customization/custom-instructions | E1 |
| Agent Skills standard (referenced by Cursor) | https://agentskills.io | E1 (referenced; not fully re-fetched) |
| Ahrefs on llms.txt adoption | https://ahrefs.com/blog/what-is-llms-txt/ | E3 |
