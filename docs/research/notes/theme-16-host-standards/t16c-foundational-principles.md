---
title: "T16C — Foundational principles (philosophy, tone, continuity)"
status: draft
theme: theme-16-host-standards
track: T16C
created: 2026-08-02
---

# T16C — Foundational principles

**Intent:** Principles as project philosophy/tone/core that survive early↔late development and human/agent churn — not only inclusion rules for standards files.

## Method

RAG `software_engineering` + `ai_llm_agents`; web; depth normal (deep deferred).

## Findings

### Continuity / philosophy

- `CLAIM` [E2] Explicit shared values/principles counter tribalism and incoherent decisions as teams grow; without them, unspoken principles still operate. [E2: Pete Hodgson engineering values / architectural principles]
- `CLAIM` [E2] Architecture principles: declarative, guide reasoning (not requirements); actionable + carry rationale; standards codify specific choices. [E2: atam chapter highlights — accessed 2026-08-02]
- `CLAIM` [E2] “You write code for other people and your future self” — continuity across ownership change. [E2: Alexandria Clean Code Principles chunk_id=`f41010b0c258a33ce7823f9c`]
- `CLAIM` [E2] Agent systems need persistent memory/context across sessions for continuity; STM alone loses project identity. [E2: Alexandria Building LLM Agents… chunk_id=`9c608d8289520a410880ed19`]
- `CLAIM` [E2] Agent principles (trust, durability, explainability, collaboration) steer design toward org values — architecture framing. [E2: Alexandria Agentic Mesh chunk_id=`0476fa273518ec98ee1300a8`]
- `INFERENCE` [E4] For Toolbelt hosts: principles docs are **loadable continuity** for fresh agents (with AGENTS.md), fewer/stabler than standards; they set tone for decisions when people/agents change. Premises: human intent + above CLAIMs.

### Quality of a principle

- `CLAIM` [E2/E3] Good principles: actionable, testable-in-decision, rationale present; bad ones = bureaucracy without value. [E2/E3: archman / atam]
- `INFERENCE` [E4] Slogan-without-rationale or unfalsifiable wallpaper fails the bar; principles should help decide conflicts, not decorate README.

### Relation to standards / Toolbelt stack

- `INFERENCE` [E4] Proposed conflict stack (draft): **accepted design/ADR > host principles > host standards profile > inferred-from-code (proposed)**. Premises: T16B; Theme 15 draft≠SoT; design-process human accept.
- `INFERENCE` [E4] Principles inform *which* standards to write; standards remain checkable feedstock for Plan/Execute/Closeout.

### Gaps

- `GAP` Thin primary on “agent-readable project principles” as a named genre — often folded into AGENTS.md / CLAUDE.md. Deep may expand exemplars.
- `OPEN` Separate PRINCIPLES.md vs section inside standards pack vs AGENTS.md only — shape track.
