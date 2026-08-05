---
title: "Theme 23 — Host adoption playbook (research campaign brief)"
status: accepted
theme: theme-23-host-playbook
created: 2026-08-04
updated: 2026-08-04
accepted: 2026-08-04
accepted_by: human (Jonathan)
authors: [scope-agent]
depth: deep
stop_rule: diminishing_returns_plus_2
aligned_with:
  - docs/templates/research-campaign-brief.md
  - docs/research/reports/theme-22-meta-guide.md
  - docs/research/reports/theme-13-contributor-workflow.md
  - docs/research/notes/theme-24-learn-back/campaign-brief.md
  - docs/packs/README.md
supersedes:
  - docs/research/notes/theme-23-host-loop/campaign-brief.md
---

# Research campaign brief — Theme 23 host adoption playbook

**Using `guide-research`**. Companion only. **Draft ≠ law** until human accepts.

## Header

```text
Title / idea: Research the Toolbelt toolbox (each surface: intent, strengths,
  limits) and research how to write host playbooks from that inventory; elevate
  a durable host-facing playbook so plugin hosts can set up and use Toolbelt.
  Playbook must stay maintainable when skills/rules/templates change.
Complexity: theme/campaign (toolbox inventory + playbook-methods + elevate)
Host note path: docs/research/notes/theme-23-host-playbook/
Date: 2026-08-04
Scoped by: agent (session) + human intent refine 2026-08-04
Enough-to-start (agent propose): yes
Human accept scope: accepted 2026-08-04 — deep fleet authorized
Depth: deep
stop_rule: diminishing_returns_plus_2
```

## Intent (product)

Help the **host of the plugin** (consumer project) **set up and use** Toolbelt — not contributor/CI ceremony (Theme 13 / Phase 2), not learn-back (Theme 24).

## Research method (two legs)

```text
1) Toolbox research (E0 primary) — inventory every live surface
     → intent / good-for / limits / typical next skill
2) Playbook-writing research — how to turn that inventory into a maintainable
     host playbook (structure, progressive disclosure, update contract)
3) Elevate — host-playbook SoT + pointers + maintenance hook when surfaces change
```

## Expand (short)

```text
- What surfaces exist today (skills, rules, key templates, packs row)?
- Per surface: intent, when to use, limits, anti-patterns, handoffs
- How do good operator/host playbooks structure “start here” vs catalog depth?
- How do we keep the playbook honest when Toolbelt ships new/changed surfaces?
- Out: Theme 24 learn-back; Toolbelt-universal coding law; Phase 2 merge automation
```

## Recommended lean (**O1**)

| Piece | Shape |
|-------|--------|
| **T23A Toolbox inventory** | Graded note(s): matrix of skills + rules (+ template SoT where host-facing). Columns: id, pocket, intent, good-for, limits, next/handoff. E0 from `skills/*/SKILL.md`, `rules/*.mdc`, packs |
| **T23B Playbook methods** | How to write host playbooks given an inventory (TOC, progressive disclosure, examples vs encyclopedia). Normal→deep as needed (docs/RAG/gh patterns) — cite-or-omit |
| **T23C Playbook elevate** | Durable `docs/host-playbook.md` (or agreed path): setup + start `guide-meta` + flow map + “when not” + link to inventory or embedded compact catalog |
| **T23D Maintenance contract** | Required: when elevating/changing skills/rules/templates, update playbook (or inventory it derives from). Prefer wire into `author-cursor-surfaces` checklist + CONTRIBUTING/README note — not a stale one-shot doc |
| **Pointers** | README + packs + `guide-meta` (“how do I adopt / set up Toolbelt”) |

**Parks / out of theme:** learn-back (24); auto-generated playbook from FM only without human review; always-on playbook rule; contributor CI mega-pack.

## Tracks

| ID | Track name | Question | In scope | Out of scope | Priority | Depth lean | Next skill(s) |
|----|------------|----------|----------|--------------|----------|------------|---------------|
| T23A | Toolbox inventory | What is each Toolbelt surface for, good at, and not for? | All live skills + always-on/intelligent rules; host-facing templates | Historical renamed ids as current law; grey-matter | P0 | normal (deepen if gaps) | `research-codebase-recon` + protocol note |
| T23B | Playbook craft | How should a host playbook be structured from such an inventory? | Playbook patterns; progressive disclosure; adopt vs reference | Learn-back retrospectives | P0 | normal→deep | `research-docs` / protocol (+ RAG if useful) |
| T23C | Playbook shape + elevate | What is the SoT artifact + pointers? | `docs/host-playbook.md` (+ optional inventory appendix) | Merging Theme 24 | P0 | normal | `author-cursor-surfaces` |
| T23D | Drift / maintenance | How does the playbook stay current when surfaces change? | author-cursor-surfaces / CONTRIBUTING update gate; smoke “playbook lists guide-meta” | Auto-publish without review | P0 | normal | protocol + author-cursor-surfaces |
| T23E | Smoke | Host-facing: find playbook; setup path; smallest-entry guidance present | Theme 11 card | Phase D harness | P0 | normal | Theme 11 |

## Working vocabulary

| Term | Means | Not |
|------|--------|-----|
| Toolbox | Live Toolbelt skills/rules/templates hosts invoke | One host’s coding standards corpus |
| Inventory | Evidence table of intent / good-for / limits | Marketing blurbs without reading SKILL.md |
| Playbook | Host setup + use guide derived from inventory | CONTRIBUTING for plugin contributors |
| Maintenance contract | Surfaces change → playbook/inventory update required | Hope README stays in sync |

## Sequencing

```text
Accept scope → T23A inventory (E0) → T23B playbook craft → human lean on shape
  → T23C/D elevate + maintenance wire → T23E smoke
Theme 24 learn-back stays separate (after or parallel research; elevate after 23 preferred)
```

## Enough? / stop

```text
Agent enough-to-start?: yes — after human accepts research legs + O1 lean
Open GAPs before gather:
  - Playbook path name (lean: docs/host-playbook.md)
  - Inventory as appendix vs separate note path under theme-23
  - Maintenance: checklist-only vs skill instruction must-update
Human gate: accept | revise | defer
```

## Human accept (copy)

```text
Accept Theme 23 / host playbook scope? accepted 2026-08-04
  depth: deep — stop_rule diminishing_returns_plus_2
  research: (1) toolbox inventory intent/good-for/limits
            (2) playbook craft via RAG + web + GitHub comparators
            (3) maintenance when surfaces change
  elevate: after integrate (host-playbook + pointers + maintenance wire)
  out: learn-back (Theme 24); CI ceremony; universal style law
```
