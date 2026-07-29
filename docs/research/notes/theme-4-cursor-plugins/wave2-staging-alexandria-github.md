---
title: "Theme 4 Wave 2 staging — Alexandria + GitHub targets"
status: draft
created: 2026-07-29
theme: theme-4-cursor-plugins
wave: 2-prep
---

# Wave 2 staging (coordinator)

Using `research-protocol` (staging only; full notes after Wave 1 lands).

## Alexandria probe (2026-07-29)

| Corpus | Query focus | Result quality for Cursor **plugin components** |
|--------|-------------|--------------------------------------------------|
| `ai_llm_agents` | Cursor plugins / SKILL.md / rules / hooks | **Weak.** Top hits = MCP in general (Dibia), Cursor-as-MCP-host anecdotes (MCP landscape PDF), progressive disclosure as *framework API* design (not Agent Skills Spec). No high-relevance Cursor `SKILL.md` / hooks.json / plugin.json chunks observed this pass. |
| `ai_llm_agents` | Agent Skills Spec / SKILL.md frontmatter | **Weak.** Hits on AutoGen “skills”, LangGraph coding agents, RAG “progressive disclosure” — **not** agentskills.io / Cursor Skills docs. |
| `software_engineering` | AGENTS.md / llms.txt | **Weak/off-topic.** Indices, Copilot/Cursor product mentions in vibe-coding books — no AGENTS.md format law. |

**FACT [E0]** Corpora listed via `list_corpora`: `ai_llm_agents` (71 docs / 22720 chunks, index v1, last_ingest 2026-07-10), plus other shelves not needed for this theme. [E0: Alexandria `list_corpora` 2026-07-29]

**GAP** Alexandria currently does **not** appear to contain Cursor official plugin/skills/rules/hooks docs or agentskills.io Spec as first-class sources for this campaign. Wave 2 should still run targeted queries + cite any partial hits as E2, but **primary reinforcement must be web + GitHub**, not RAG alone.

**INFERENCE [E4]** For Toolbelt skill re-eval, treat Alexandria as useful for *adjacent* agent/MCP patterns (progressive disclosure of complexity, MCP host/client roles) — map carefully; do not treat as Cursor packaging SoT. Premises: weak retrieval above + strong E1 from cursor.com/docs in Wave 1.

## High-signal external targets (for Wave 2 agents)

Star counts from WebSearch snippets 2026-07-29 (verify with `gh` / page before locking):

| Target | Why | Grade when used |
|--------|-----|-----------------|
| https://cursor.com/docs/skills.md | Official skills (already Wave 1) | E1 |
| https://agentskills.io | Agent Skills open standard (if Cursor links / community treats as Spec) | E1 Spec / E2 if only community |
| https://github.com/anthropics/skills (~165k★ snippet) | Reference skill patterns + skill-creator | E1 Anthropic examples / E2 for Cursor-specific behavior |
| https://github.com/cursor/plugin-template | Official template | E1 |
| https://github.com/spencerpauly/awesome-cursor-skills (~629★) | Curated Cursor skills index | E3 discovery |
| cursor.directory / marketplace | Community + official plugins | E3 / E1 marketplace |
| create-plugin Cursor plugin (local cache) | Scaffold skill claims | E0 local + E1 if matches docs |

## Wave 2 agent plan (launch after Wave 1 notes exist)

| ID | Scope |
|----|-------|
| T4H | agentskills.io + anthropics/skills writing patterns vs Cursor skills.md |
| T4I | GitHub high-signal Cursor plugins/skills structure sampling (awesome lists + top marketplace plugins) |
| T4J | Alexandria deep pass: MCP packaging patterns transferable to plugin `mcp.json`; explicit GAP log for Cursor-specific misses |
| T4K | Testing/validation practices: official “tested locally” checklist + community smoke patterns + Toolbelt smoke archive cross-link |

## Diminishing-returns stop rule

Stop spawning gatherers when new notes only restate prior FACTS or add uncorroborated E3 without new GAPs closed.
