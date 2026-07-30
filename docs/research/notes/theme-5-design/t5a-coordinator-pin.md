---
title: "T5A coordinator pin — Agent / AI-assisted design process"
status: draft
theme: theme-5-design
track: T5A
created: 2026-07-29
updated: 2026-07-29
authors: [coordinator]
depth: deep
waves: [pin]
campaign_phase: t5a_synthesis_done
stop_reason: low_return_plus_one
aligned_with:
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/research/notes/theme-5-design/scope-normal-deep-prep.md
  - docs/templates/research-depth-modes.md
  - docs/PROTOCOL.md
supersedes: null
---

# T5A coordinator pin

**Using `research-protocol`** · depth: **deep** · Theme 5 Design campaign (approved brief).

## 1. Scope

| Field | Value |
|-------|-------|
| Question | How should humans + coding/creative agents run a **design process** (options, constraints, tradeoffs, decision, record)? |
| In | Design loops, critique, alternatives, ADR/MADR, agent roles (propose/critique/decide), HITL, anti-patterns |
| Out | T5B arch content, T5C UX (deferred), T5D creative content, Theme 4 plugin FM, inventing Design skills, stack locks |
| Reuse | Theme 2 ADR/MADR FACTS — do not re-litigate ADR existence |

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Depth | deep |
| Waves plan | W1 primary → W2 Alexandria/web/community → W3 residual / Plan Mode if OPEN → synthesis |
| Stop | Theme 5: low-return detect → +1 residual → `low_return_plus_one`; short-circuit if budget/unavailable |
| Subagents | `cursor-grok-4.5-high-fast` (not Sonnet) |
| Corpora | `ai_llm_agents`, `software_engineering` (partial for process; watch false friends) |
| Note root | `docs/research/notes/theme-5-design/` |
| What was not searched (pin) | Full W1–W3 evidence (starts after this pin) |

## 3. Gatherer slices

| ID | Slice | W1 focus |
|----|-------|----------|
| T5A-S1 | ADR/MADR + Theme 2 cross-link | Nygard, Fowler, MADR primaries; cite Theme 2 §2.5 |
| T5A-S2 | Agent-assisted design process | HITL, alternatives/critique, human-led AI design loops (E1/E2 preferred) |
| T5A-S3 | Community agent workflows | Superpowers brainstorming/writing-plans; AgDR — **E3 structure inventory only** |

## 4. Progress board

| Wave | Status | Notes |
|------|--------|-------|
| Pin | done | this file |
| W1 S1–S3 | done | Grok gatherers |
| W2 | done | RAG + web (Grok) |
| W3 / +1 | done | residual = +1 after low return |
| Track synthesis | done | `t5a-track-synthesis.md` |
| stop_reason | `low_return_plus_one` | |

## 5. Hard constraints (remind gatherers)

- Cite-or-omit; draft ≠ SoT  
- No Design skill elevation  
- No mega-skill claiming all design types  
- T5C out of campaign  
- Stars = discovery only  
