---
name: research-draft-adr
description: >-
  Record an architecture or process decision with the Toolbelt house ADR
  (docs/adr/NNNN-slug.md: context, considered options, decision, consequences).
  Use when locking a choice after design/research, rejecting alternatives,
  writing ADRs/MADR-style records, or the user asks for an ADR. Explicit / invoke.
  Formerly draft-adr.
disable-model-invocation: true
---

# Draft ADR

Announce once: **Using `research-draft-adr`**.

Explicit skill (`/research-draft-adr`). Prefer after `guide-design` / research notes when possible.

## House defaults (Theme 5)

| Field | Value |
|-------|-------|
| Path | Host `docs/adr/NNNN-short-title.md` (unless user specifies otherwise) |
| Status enum | `proposed` \| `accepted` \| `deprecated` \| `superseded` |
| Required body | Context, **Considered Options** (+ pros/cons), Decision (+ because), Consequences |

## Instructions

1. Read `references/adr-minimal.md` **when** creating an ADR, then copy it to `docs/adr/NNNN-short-title.md` (or user path). Re-open the reference **when** recovering a missing section.
2. Set `status: proposed` until the human accepts — **proposed ≠ project law**.
3. **Context:** forces at play; link research/design notes.
4. **Considered Options:** real alternatives with pros/cons (skip only when there is truly one forced option — say so).
5. **Decision:** one clear “We will …” + because (vs rejected options).
6. **Consequences:** positive / negative / neutral.
7. Optional confirmation: how you will know it is working.
8. Do not invent constraints or library locks without cited research (`research-protocol` / `research-docs` / `research-codebase-recon` as needed).
9. When the decision changes later: **supersede** with a new ADR — do not rewrite history in place.

## Handoffs

| Need | Use |
|------|-----|
| Design options first | `guide-design` / `design-technical` |
| Evidence before locking | `research-protocol` / `research-docs` / `research-codebase-recon` |
| After accept → plan | `implementation-plan` → `implementation-plan-verify` |

## References

- Read `references/adr-minimal.md` **when** creating or recovering ADR sections
- SoT: Toolbelt `docs/templates/adr-minimal.md`
- Method: Theme 5 / Theme 2 accepted reports
