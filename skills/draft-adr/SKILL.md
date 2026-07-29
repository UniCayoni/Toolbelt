---
name: draft-adr
description: >-
  Record an architecture or process decision with the Toolbelt minimal ADR
  template (context, decision, consequences, links to research). Use when locking
  a choice after research, rejecting alternatives, writing architecture decision
  records, or the user asks for an ADR / MADR. Explicit / invoke.
disable-model-invocation: true
---

# Draft ADR

Announce once: **Using `draft-adr`**.

Explicit skill (`/draft-adr`). Use **after** research notes exist when possible.

## Instructions

1. Copy `references/adr-minimal.md` to a durable path (e.g. host `docs/adr/NNNN-short-title.md` or user-specified). Re-open the reference **when** recovering a missing section from a partial draft.
2. Set `status: proposed` until the human accepts — **proposed ≠ project law**.
3. **Context:** forces at play; link research notes with PROTOCOL citations.
4. **Decision:** one clear “We will …” statement.
5. **Consequences:** positive / negative / neutral.
6. Optional confirmation: how you will know it is working.
7. Do not invent constraints or library locks without cited research (`research-protocol` / `docs-research` / `codebase-recon` as needed).

## References

- `references/adr-minimal.md`
- SoT: Toolbelt `docs/templates/adr-minimal.md`
