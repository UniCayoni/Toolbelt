---
name: author-standards
description: >-
  Author host-owned principles and checkable standards profiles, optionally
  derive brownfield candidates from recon and git history, or lightly
  bind-check Plan/Execute/Closeout consumption. Use when host standards,
  coding standards profile, project principles, engineering principles,
  style guide for agents, brownfield derive conventions, or feedstock for
  plan/execute/closeout. Prefer over inventing Toolbelt-universal coding law
  or dumping standards into AGENTS.md. Explicit / invoke.
disable-model-invocation: true
---

# Author standards

Announce once: **Using `author-standards`**.

Explicit skill (`/author-standards`). **Host feedstock** — not Toolbelt-universal coding law.  
Authority: Theme 16 accepted (`docs/research/reports/theme-16-host-standards.md`).  
**Draft ≠ law** (`draft-is-not-sot`) until human accepts profiles.

## When to use

- Define project **principles** (philosophy / tone / continuity)
- Define **standards** profiles (checkable naming, layout, patterns, tests/docs, safety, …)
- **Derive** proposed standards from an existing codebase (brownfield)
- Light **bind-check** that Plan / Execute / Closeout can find and use profiles
- User asks for a host style guide / principles doc agents can load

**Skip:** one-off ticket preference; ADR-sized architecture locks → `research-draft-adr`; AGENTS.md-only house ops → `author-agents-md` (keep a short pointer here).

**Out of scope:** Toolbelt-universal style as law; always-on standards rule; auto-promote derive; PR/merge ceremony; renaming `implementation-closeout`.

## Modes

| Mode | Delivers |
|------|----------|
| `principles` | Host principles profile from template |
| `standards` | Host standards profile from template |
| `derive` | Proposed candidates from recon + history → human accept |
| `bind-check` | Light verify profiles are discoverable and referenced |

## Instructions

1. **Classify mode** with the user (`principles` \| `standards` \| `derive` \| `bind-check`).
2. **Paths** — prefer existing host profiles; else copy SoT templates into an agreed host path (defaults lean: `docs/standards/principles.md`, `docs/standards/standards-profile.md`).
3. **`principles`** — fill principles template: short named guidance; conflict note; AGENTS pointer only. Stop at draft/proposed until human accept.
4. **`standards`** — fill standards template: scope; v1 types (naming, layout, patterns, tests/docs, safety/secrets; optional API/errors); checkable rules; enforcement pointer; evolution. Park perf/i18n/a11y/process/architecture-as-ADR unless host insists.
5. **`derive`**
   - As-needed: `research-codebase-recon`.
   - Prefer lint/formatter configs already in-repo.
   - Recency: host-declared window; hot paths / churn; `git blame` with `.git-blame-ignore-revs` when present (formatter mega-commits are noise).
   - Dual-era: quarantine legacy paths; do not force one era without host choice.
   - Emit **proposed** profile edits or a candidate list — **never** silent SoT.
6. **`bind-check`** — confirm AGENTS (or agreed path) points at profiles; Plan/Execute/Closeout can skip when absent; do not invent Cursor AGENTS vs Team/Project rule precedence (documented GAP).
7. **Conflict lean (host may adopt):** design/ADR > principles > standards > inferred-from-code — **host-authored method**, not claimed industry SoT.
8. Hand **human accept** before Plan/Execute/Closeout treat profiles as law.

Read `references/author-standards-checklist.md` **when** running a full mode session.  
Profile SoTs: `references/principles-profile.md`, `references/standards-profile.md` (SoT under `docs/templates/`).

## Anti-patterns

- Shipping Google/Airbnb/etc. as Toolbelt law  
- Dumping full standards into `AGENTS.md`  
- Treating derive output as accepted without human  
- Mixing principles (tone) with lint rules in one undifferentiated blob  
- Owning CI/merge ceremony as “standards”  

## Handoffs

| Need | Use |
|------|-----|
| AGENTS.md pointer / budgets | `author-agents-md` |
| Cursor skill/rule packaging | `author-cursor-surfaces` |
| Codebase recon for derive | `research-codebase-recon` |
| Architecture locks | `research-draft-adr` / `design-process` |
| Plan / Execute / Closeout | `implementation-plan`, `implementation-execute`, `implementation-closeout` |
| Full ladder | `implementation-happy-path` |

## References

- Read `references/author-standards-checklist.md` **when** defining, deriving, or bind-checking
- Read `references/principles-profile.md` **when** creating/updating principles (SoT: `docs/templates/principles-profile.md`)
- Read `references/standards-profile.md` **when** creating/updating standards (SoT: `docs/templates/standards-profile.md`)
- Theme 16: Toolbelt `docs/research/reports/theme-16-host-standards.md` (accepted)
