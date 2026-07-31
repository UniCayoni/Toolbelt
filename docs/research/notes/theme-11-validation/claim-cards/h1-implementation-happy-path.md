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
| C1 | Announces Using `implementation-happy-path` | | |
| C2 | Classifies ask type | feature/bug/… | |
| C3 | Lists compose order via existing skills (no pasted pocket law) | Invokes/links skills | |
| C4 | Research as-needed preface | Can mark N/A | |
| C5 | Workers = one pocket note for subagents | Stated | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Re-teach full Execute/Debug spines inline | |
| A2 | Skip human design gate without documenting skip | |

## Smoke

**Explicit:** “Using `implementation-happy-path`, classify and route: we need to fix smoke-app add() off-by-one end-to-end. Output classifier + checklist stages only; do not implement.”

**Implicit (discovery, separate fresh chat):** “What’s the Toolbelt order of skills for a small feature fix?”

**Negative:** “Only draft an ADR for logging.” → should route draft-adr / authoring, not full feature ladder as mandatory.
