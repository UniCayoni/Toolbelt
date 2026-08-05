---
title: "Toolbelt host playbook — surface catalog"
status: active
aligned_with:
  - docs/host-playbook.md
  - docs/research/reports/theme-23-host-playbook.md
created: 2026-08-04
updated: 2026-08-04
---

# Surface catalog (reference)

Companion to [host-playbook.md](./host-playbook.md). **Start there** — do not open with this table.  
Feedstock: Theme 23 T23A inventory (E0). If a row conflicts with live `SKILL.md`, **skill wins**.

Columns: **id** · **intent** · **good-for** · **limits** · **typical next**

## Guides / meta / ladder

| id | intent | good-for | limits | typical next |
|----|--------|----------|--------|--------------|
| guide-meta | Front door: one next surface | Fuzzy / which skill | Not always-on; not pocket work | guide-* / happy-path / author-* / closeout |
| guide-research | Expand/atomize research | Unclear tracks | Not graded notes | protocol / recon / docs |
| guide-design | Design spine + HITL | Options before code | UX deferred (T5C) | design-* → ADR → impl |
| guide-implementation | Wire Impl leaves | Which plan/execute skill | Not writing the plan | plan → verify → execute → verify |
| guide-debug | Wire Debug leaves | Prove vs fix | Not Theme 9 paste | reproduce / systematic |
| guide-standards | Module pointers | Selective host standards | No-op if no catalog | load modules; author-standards |
| implementation-happy-path | Feature ladder | End-to-end feature | Not trivial / single pocket | chain guide-* |

## Research leaves

| id | intent | good-for | limits | typical next |
|----|--------|----------|--------|--------------|
| research-protocol | Graded notes / deep waves | Claim-bearing research | Draft≠law | design / plan after accept |
| research-codebase-recon | S0–S16 recon | Unfamiliar repo | Don’t invent APIs | protocol / design / plan / derive |
| research-docs | D0–D14 docs pin | Third-party docs | Prefer corroboration | protocol / ADR |
| research-draft-adr | House ADR | Lock decisions | Explicit `/` | plan after accept |

## Design leaves

| id | intent | good-for | limits | typical next |
|----|--------|----------|--------|--------------|
| design-technical | Architecture at design-time | Boundaries / stack criteria | Not lint pack; not UX | ADR / plan |
| design-systems | Creative/game systems | Loops / economies | Not story/UX | guide-design / plan |
| design-narrative | Story / quests | Interactive narrative | Not world bible | guide-design / plan |
| design-world-character | World / characters | Continuity | Not quests/combat | guide-design / plan |

## Plan / Execute / Verify / Debug leaves

| id | intent | good-for | limits | typical next |
|----|--------|----------|--------|--------------|
| implementation-plan | Durable agent plans | Multi-task after design | Not from draft design as law | plan-verify |
| implementation-plan-verify | Pre-exec plan grade | Meta ready gate | Not Debug/PR | execute or rewrite |
| implementation-execute | Task loop Done-when N=2 | Approved plan | Not invent outside plan | execute-verify / debug |
| implementation-execute-subagents | Controller + workers | Multi-task fresh agents | Not tiny single task | execute-verify / debug |
| implementation-execute-verify | Post-green / EOP | Evidence iron law | Not PR pack | converge / debug |
| debug-reproduce | Prove + light dossier | Never-fix first | Does not patch | debug-systematic |
| debug-systematic | Investigate / fix | Bugs after N=2 | Not Theme 8 verify | execute-verify / design |

## Closeout / standards / authoring

| id | intent | good-for | limits | typical next |
|----|--------|----------|--------|--------------|
| implementation-closeout | Host readiness check | Ship-ready evidence | Not merge/push/PR | human ceremony |
| author-standards | Write/derive host profiles | Principles + standards | Not Toolbelt-universal law | guide-standards after accept |
| author-agents-md | AGENTS.md | House ops bootstrap | Keep standards as pointers | author-cursor-surfaces |
| author-cursor-surfaces | Author skills/rules/hooks | New Cursor surfaces | Explicit `/`; not marketplace audit | agents-md / research-docs |

## Rules (ambient)

| id | alwaysApply | intent | limits |
|----|-------------|--------|--------|
| draft-is-not-sot | yes | Draft≠accepted law | — |
| research-protocol-grades | yes | Cite-or-omit / grades | Thin; full notes → research-protocol |
| standards-resolve-gate | yes | Catalog → guide-standards else no-op | Not coding law body |
| research-before-write | no (intelligent) | Soft explore-before-edit | Soft only |

## Host-copy templates (setup)

| Template | Typical host use |
|----------|------------------|
| agents-md-skeleton.md | `AGENTS.md` |
| plan-minimal.md | `docs/plans/…` |
| standards-catalog.md / standards-module.md | `docs/standards/…` |
| principles-profile.md / standards-profile.md | feedstock for author-standards |
| closeout-profile.md / closeout-readiness-checklist.md | closeout |
| repro-light.md | repro dossier |
| research-note.md / research-campaign-brief.md / adr-minimal.md | research & ADR |

Copy out; don’t edit Toolbelt templates as working notes. Full inventory research: `docs/research/notes/theme-23-host-playbook/t23a-toolbox-inventory.md` (draft research — not playbook SoT).
