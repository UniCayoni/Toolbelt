---
title: "Theme 16 — Host standards (research campaign brief)"
status: accepted
theme: theme-16-host-standards
created: 2026-08-02
updated: 2026-08-02
authors: [scope-agent]
scope_note: T16C clarified as project philosophy/tone/continuity (humans+agents), not only standards-inclusion rules
aligned_with:
  - docs/templates/research-campaign-brief.md
  - docs/research/reports/theme-12-research-scoping.md
  - docs/research/reports/theme-15-closeout-readiness.md
  - docs/research/reports/theme-14-pocket-routers.md
supersedes: null
---

# Research campaign brief — Theme 16 Host standards

Authority: Theme 12 accepted. Used by skill **`research-scope`**.  
Companion only — does **not** replace `research-protocol` notes/grades.  
**Draft ≠ law** until human accepts scope / later report.

## Header

```text
Title / idea: Host standards — help define/maintain host-owned standards profiles
  that Plan, Execute, and Closeout can bind to; optional brownfield derive via
  recon + history with recency/conflict gates. Not Toolbelt-universal coding law.
  Rename of implementation-closeout deferred. Skill lean: author-standards (OPEN).
Complexity: theme/campaign (deep expected after normal wave + lean)
Host note path: docs/research/notes/theme-16-host-standards/
Date: 2026-08-02
Scoped by: agent (session)
Enough-to-start (agent propose): yes — tracks cover ontology through bind + principles
Human accept scope: accepted 2026-08-02 — normal done; deep authorized 2026-08-02
  (stop_rule: diminishing_returns_plus_2; O1 lean accepted)
```

## Working vocabulary (session lean — not locked)

| Term | Means | Not |
|------|--------|-----|
| **Standard** | Host-owned, explicit, checkable constraint set for work products | Vibes; unstated culture |
| **Guideline** | Softer preference; may be waived more freely | Always blocking |
| **Principle** | Project philosophy / tone / core values that guide decisions over time (humans + agents; early or late) | A lint rule; a one-off ticket preference |
| **Convention** | Local habitual pattern (naming, layout) | Architecture Decision Record |
| **Profile** | Durable artifact agents load | Always-on plugin rule |
| **Bind** | Plan/Execute/Closeout consume profile | Plugin owns merge ceremony |

## Expand (short)

```text
- Fence: help define/bind; do not ship “the Toolbelt style guide” as law
- Closeout integrates as consumer (Theme 15 kept); rename deferred
- Overlap with AGENTS.md / design accept / plan T0 — layer, don’t fight
- Brownfield: derive candidates from recon + history; proposed until human accept;
  recency so legacy ≠ SoT
- Foundational principles: guide what goes in a standard and how to decide conflicts
- Cap v1 types; park the rest
- Comparator channels (after accept): RAG, GitHub, web/primary, secondary — same spirit as T15
```

## Tracks

| ID | Track name | Question | In scope | Out of scope | Priority | Depth lean | Next skill(s) |
|----|------------|----------|----------|--------------|----------|------------|---------------|
| T16A | Local baseline | What already exists (AGENTS.md authoring, design/plan constraints, closeout profiles, draft≠SoT) and what gap remains? | Themes 4–15 surfaces; packs | Elevating yet | P0 | normal | recon + protocol |
| T16B | Ontology | What is a standard vs guideline vs convention vs policy vs ADR lock in Toolbelt terms? | Definitions + fences | Philosophy essay without product use | P0 | normal | protocol + docs |
| T16C | **Foundational principles** | What are *project* foundational principles (philosophy, tone, core that survives team/agent churn and early↔late phases), how are they authored/used, and how do they relate to concrete standards profiles? | Continuity across people/agents; decision tone; relationship to standards vs ADR vs vision; examples | Replacing design-process; Toolbelt-universal morality always-on rule | P0 | normal→deep | protocol + RAG/web/gh |
| T16D | Typology | Which types of standards are worth v1 support (naming, layout, patterns, tests/docs, security, …)? | Priority shortlist + park list | Exhaustive ISO catalog | P0 | normal→deep | protocol + RAG/gh |
| T16E | Anatomy | What is a good standard/profile *composed of* (scope, rules, examples, anti-patterns, evidence, evolution)? | Structure for template | Ceremony fields (merge/CI as law) | P0 | normal | protocol + exemplars |
| T16F | Exemplars | Design-wise examples of good/bad standards docs — compare focuses | Primary + packs + RAG | Copying one org’s guide as Toolbelt law | P0 | normal→deep | docs + gh + RAG |
| T16G | Quality bar | What makes a standard good, dangerous, or useless? | Overfit, unfalsifiable, ceremony creep, conflict with design | — | P0 | normal | protocol (ties T16C) |
| T16H | Lifecycle | Greenfield create vs mid-project adopt; how standards evolve | Create/adopt/amend/deprecate | Mandatory rewrite of all host code | P0 | normal | protocol |
| T16I | Brownfield derive | How to propose standards from codebase recon + history with recency and conflict gates? | Method using research-codebase-recon (+ git history signals); draft≠SoT until accept | Silent promote of legacy patterns to law | P0 | normal→deep | recon + protocol |
| T16J | Bind | How Plan / Execute / Closeout load and check profiles; skip when none? | Handoffs; Done-when slots; closeout criteria refs | Replacing Theme 15 closeout skill | P0 | normal | protocol |
| T16K | Shape options | `author-standards` (+ template); packs; relationship to author-* cluster; closeout rename deferred | Options matrix | Immediate rename of implementation-closeout | P0 | normal | integrator after A–J |

## Foundational principles track (T16C) — expand hints

**Intent (human):** Principles drive the *philosophy* behind project decisions, set *tone*, and carry the *core* of the project forward through early or late development — including through team/people change and agents. Research this *as continuity infrastructure*, not only as “rules for writing a standards file.”

What to look up / decide (not locks yet):

```text
Continuity / philosophy
- How orgs express “north star” principles that outlive individuals and agent sessions
- Tone-setting vs operational checklists (principles vs standards vs conventions)
- Early-project principle capture vs late-project rediscovery / drift
- Agent-relevant: what must be loadable so a fresh agent inherits project core, not chat vibe

Relationship to standards pocket
- Principles inform *what* standards to write and *how* to resolve conflicts
- Standards remain more checkable/concrete; principles stay fewer, stabler, higher-altitude
- Conflict stack lean (to validate): accepted design/ADR > principles > standards profile >
  inferred-from-code (proposed until accept)

Authoring / quality (still needed)
- What makes a principle useful vs slogan / unfalsifiable wallpaper
- Evolution: amend rarely, with reason; don’t silent-overwrite
- Inclusion of principle *docs* in host profile set vs separate PRINCIPLES.md
- Brownfield: “observed culture in code” ≠ principle until human accept + recency
- Fence: not a Toolbelt always-on morality rule; host-owned
```

## Comparator discovery (after accept — same spirit as Theme 15)

| Channel | Use for |
|---------|---------|
| Alexandria RAG | `software_engineering`, `ai_llm_agents` — coding standards, principles, styleguides, architecture principles |
| GitHub | Skill packs / CONTRIBUTING / STANDARDS.md / AGENTS.md patterns |
| Web / primary | Canonical style/guide docs; “definition of done” vs coding standard distinctions |
| Secondary | Curated comparisons — E2/E3 discipline |

## Recommended gather order (after accept)

1. **Normal wave:** T16A–B–C–E–G–J (baseline, ontology, principles, anatomy, quality, bind) + light T16D/F/H/I  
2. **Lean** on T16K (shape) — human accept  
3. **Deep** on T16C/D/F/I (and others that stayed thin) only if needed  
4. Draft Theme 16 report → accept → elevate  

Do **not** auto-launch deep fleets from this brief alone.

## Explicit non-goals (scope fence)

- Shipping a single Toolbelt-universal coding standard as law  
- Replacing `implementation-closeout` or forcing rename in this theme  
- Auto-applying inferred brownfield patterns without human accept  
- Ceremony/merge/CI automation as standards content  

## Enough? / stop

```text
Agent enough-to-start?: yes — for scope accept, then normal wave (not immediate deep)
Open GAPs / OPENs:
  - Skill id (`author-standards` vs other) — OPEN until T16K
  - v1 type shortlist — OPEN until T16D lean
  - Exact profile path convention — OPEN until design/elevate
Human gate: accepted 2026-08-02 — normal gather; deep only after lean if needed
```

## After accept

Hand off per track; keep notes `draft` until integrated report accept.  
Elevation only after accept — standards as feedstock; closeout/plan/execute as consumers.
