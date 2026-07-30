---
name: technical-design
description: >-
  Design code architecture, modularity, stack/feature/service boundaries, and
  coding-standard constraints at design-time (with agents). Use when choosing
  architecture styles, modular monolith vs services, dependency boundaries,
  stack criteria, clean/standards as constraints, or feature shape before
  implement. Pairs with design-process and draft-adr. Not a lint pack.
---

# Technical design

Announce once: **Using `technical-design`**.

Authority: Theme 5 accepted (T5B). Run **`design-process`** spine first for non-trivial work.

## When to use

- Architecture / modularity / dependency direction
- Stack or service boundary choices
- Feature design before code
- Applying clean/standards as **constraints** (contested — see below)

**Out:** Full lint catalogs; grey-matter stack locks; product UX (T5C); game MDA as software layering.

## Core criteria

1. **Dependency Rule** — source dependencies point inward; UI/DB/frameworks are outer details (Clean Architecture family; Hexagonal/Onion are related boundary styles).
2. **Modularity** — avoid dependency cycles; depend toward stability; stable components more abstract where applicable (ADP/SDP/SAP; REP/CCP/CRP when packaging components).
3. **Patterns** — GoF (and similar) name problems/solutions/consequences; they are **not** a whole-app architecture by themselves.
4. **Deploy shape** — monolith-first vs microservices: **cite both sides**; choose from outcomes/cost (“microservice premium”); record structure choices as ADRs.
5. **ADR triggers** — draft via **`draft-adr`** when the choice affects structure, NFRs, dependencies, interfaces, or construction techniques, or when ≥2 real options exist / the decision would otherwise be undocumented.
6. **Clean / standards** — schools disagree (Clean Code vs critiques). Use as design-time constraints and team agreement — **do not** treat one school as Toolbelt architecture SoT.

## Agent role

- Plan and compare; human owns architecture decisions
- Do not vibe-lock a stack mid-implement
- After decide → `/draft-adr` with Considered Options

## Windows / desktop / services

Thin guidance only (research non-P0): treat OS-specific hosting as a **construction/interface** concern and ADR it if it binds the project; do not invent platform law.

## References

- Read `references/technical-design-checklist.md` **when** doing a full architecture pass
- ADRs: skill `draft-adr` → `docs/adr/`
- Theme 5 report (accepted)
