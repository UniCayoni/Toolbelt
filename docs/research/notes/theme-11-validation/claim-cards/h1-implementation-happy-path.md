---
title: "Claim card H1 — implementation-happy-path"
status: draft
theme: theme-11-validation
surface_id: H1
---

# H1 — implementation-happy-path

| Field | Value |
|-------|-------|
| Surface | `implementation-happy-path` |
| Authority | Theme 10 |
| Lane | fresh_chat |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `implementation-happy-path` | H1-20260731-theme14 | **pass** |
| C2 | Classifies ask type | feature/bug/… | **pass** |
| C3 | Lists compose order via existing skills (no pasted pocket law) | Invokes/links skills | **pass** |
| C4 | Research as-needed preface | Can mark N/A | **pass** |
| C5 | Workers = one pocket note for subagents | Stated | **pass** |
| C6 | Optional `research-scope` when expand-first / tracks unclear (Theme 12) | Mentions scope only when appropriate; not mandatory on clear bug/feature | **pass** |
| C7 | Feature path uses **`implementation-router`** for Implementation stage (Theme 14) | Does not re-list plan→execute leaves as duplicate SoT | **pass** |
| C8 | Implementation-only asks prefer `implementation-router` over full ladder | Classifier table | **pass** |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Re-teach full Execute/Debug spines inline | **no** |
| A2 | Skip human design gate without documenting skip | **no** |
| A3 | Force `research-scope` on every research/bug path | **no** |
| A4 | Bypass Theme 14 by pasting old Implementation leaf ladder as SoT | **no** |

## Smoke

**Explicit:** “Using `implementation-happy-path`, classify and route: we need to fix smoke-app add() off-by-one end-to-end. Output classifier + checklist stages only; do not implement.”

**Explicit (Theme 12 / research branch):** “Using `implementation-happy-path`, classify and route: run a multi-surface theme campaign on ‘how agents should scope research tracks’ — checklist stages only; do not gather.”

**Implicit (discovery, separate fresh chat):** “What’s the Toolbelt order of skills for a small feature fix?”

**Negative:** “Only draft an ADR for logging.” → should route research-draft-adr / authoring, not full feature ladder as mandatory.
