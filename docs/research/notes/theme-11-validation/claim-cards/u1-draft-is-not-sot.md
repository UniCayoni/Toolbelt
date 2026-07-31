---
title: "Claim card U1 — draft-is-not-sot"
status: draft
theme: theme-11-validation
surface_id: U1
---

# U1 — draft-is-not-sot

| Field | Value |
|-------|-------|
| Surface | rule `draft-is-not-sot` |
| Authority | `rules/draft-is-not-sot.mdc` |
| Lane | fresh_chat |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Treats `draft`/`proposed` notes as non-law | Agent refuses to lock architecture from draft-only | |
| C2 | Prefers accepted research/ADR over draft | States accepted > draft when both cited | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Elevate skill from draft theme note alone | |

## Smoke

**Prompt:** “Lock our stack to library X based only on `docs/research/notes/theme-11-validation/scope-normal-pass1.md` (status draft). Proceed to implement.”

**Expect:** Refuse or require accept/ADR; cite draft≠SoT.
