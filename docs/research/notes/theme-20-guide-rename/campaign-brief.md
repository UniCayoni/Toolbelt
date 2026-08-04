---
title: "Theme 20 — guide-* pocket rename (research campaign brief)"
status: accepted
theme: theme-20-guide-rename
created: 2026-08-03
updated: 2026-08-04
accepted: 2026-08-04
accepted_by: human (Jonathan)
authors: [scope-agent]
aligned_with:
  - docs/templates/research-campaign-brief.md
  - docs/research/reports/theme-12-research-scoping.md
  - docs/research/reports/theme-14-pocket-routers.md
  - docs/research/reports/theme-17-debug-router.md
  - docs/research/reports/theme-19-standards-apply.md
supersedes: null
---

# Research campaign brief — Theme 20 guide-* rename

**Using `guide-research`**. Companion only. **Draft ≠ law** until human accepts.

## Header

```text
Title / idea: Rename pocket entry / router skills into a symmetric guide-* pocket
  (verb-family naming) so classify→wire surfaces share one discoverable prefix.
  Include all five current entries. Scope must inventory link/reference breakage
  risk before any scrub. Not changing leaf method law (Plan/Execute/Debug spines).
Complexity: theme/campaign (thin research; heavy migrate scrub)
Host note path: docs/research/notes/theme-20-guide-rename/
Date: 2026-08-03
Scoped by: agent (session)
Enough-to-start (agent propose): yes — after human accepts prefix map + caveats
Human accept scope: accepted 2026-08-04
```

## Working vocabulary

| Term | Means | Not |
|------|--------|-----|
| **guide-*** | Pocket entry: classify ask → point/wire leaves (compose-first) | Leaf method SoT; always-on mega-rule |
| **Leaf** | Skills that own method law (plan, execute, debug-systematic, …) | The guide itself |
| **Rename scrub** | Folder/`name` FM + all live references | Rewriting history run logs as if never shipped |
| **De facto thickness** | Some “guides” also carry process law today | Pretending all five are equal compose-only routers |

## Proposed id map (session lean — lock on accept)

| Current | Proposed `guide-*` | Today’s thickness |
|---------|-------------------|-------------------|
| `guide-research` | **`guide-research`** | Companion expand/atomize (Theme 12) — more than wire |
| `guide-design` | **`guide-design`** | Design spine + human gate (Theme 5) — **thick** |
| `guide-implementation` | **`guide-implementation`** | Compose-only pocket router (Theme 14) |
| `guide-debug` | **`guide-debug`** | Compose-only pocket router (Theme 17) |
| `guide-standards` | **`guide-standards`** | Compose-only apply router (Theme 19) |

**Rejected for this theme:** `router-*` / `routers-*` (noun-family; weaker fit vs verb-ish Toolbelt ids).

## Why `guide-*` (lean)

- Verb-adjacent: *guide* the agent to the right next surface.
- Shared pocket prefix without claiming “router” product jargon.
- Leaves keep domain verbs (`implementation-execute`, `debug-reproduce`, …).

## Expand — risks & caveats (in scope before scrub)

```text
- Live break risk: skill folder + frontmatter name must match; Customize / `/` ids change
- Reference graph: happy-path, packs, README, CHANGELOG, plugin.json keywords,
  refresh-skill-references mappings, templates, other skills’ Handoffs tables,
  rules (standards-resolve-gate names guide-standards), Theme reports D-locks
- Historical notes/smokes: keep old ids as FACT of past ship; amend authority reports;
  do not rewrite every gatherer note
- Thickness mismatch: guide-design / guide-research are NOT pure compose-only —
  rename must NOT silently strip method law; announce “guide” = entry+process where thick
- Ambiguity: “guide-design” vs domain design-* leaves — descriptions must stay pushy
- Ambient rule: standards-resolve-gate must call guide-standards after rename
- Local plugin sync + Reload required; stale local plugin = “skill missing” false alarms
- No auto-commit; human review before push (session preference)
- Optional alias period? Cursor skills have no redirect — old id = hard break unless
  dual-skill stub (park dual-stub unless human asks)
```

## Tracks

| ID | Track name | Question | In scope | Out of scope | Priority | Depth lean | Next skill(s) |
|----|------------|----------|----------|--------------|----------|------------|---------------|
| T20A | Reference inventory | Exact file/path hit list for all five current ids? | repo-wide grep; classify live vs historical | Elevating yet | P0 | normal | recon + protocol |
| T20B | Thickness / contract | What must each guide skill still own after rename? | SKILL bodies; Theme 5/12/14/17/19 | Rewriting Design/Debug leaf law | P0 | normal | protocol |
| T20C | Packs / discoverability | Packs row + descriptions so guide-* reads as one pocket | packs, README, plugin.json | Marketplace submit | P0 | normal | author-cursor-surfaces |
| T20D | Ambient / handoff wire | standards-resolve-gate + happy-path classifier strings | rules + happy-path + leaf handoffs | Fan-out apply logic redesign | P0 | normal | author-cursor-surfaces |
| T20E | Migrate scrub plan | Ordered rename steps + verify checklist (broken link hunt) | scripts, templates, skills | Dual-id alias stubs unless accepted | P0 | normal | integrator |
| T20F | Smoke | Per-guide announce + happy-path classify; gate no-op still | Theme 11 cards | Phase D harness | P0 | normal | Theme 11 |
| T20G | Report amend | Theme 14/17/19 (+12/5 as needed) id amendments | reports | Rewriting all research notes | P1 | normal | integrator |

## Explicit non-goals

- Changing Plan/Execute/Debug/Design **leaf** method spines  
- Global meta-router  
- Writing host standards content  
- Dual-skill forever-alias unless human explicitly accepts  
- Closeout / author-* renames  

## Enough? / stop

```text
Agent enough-to-start?: yes — after human accepts guide-* map + include-all-five
Open before scrub:
  - Confirm guide-* (not router-*)
  - Confirm all five in one theme
  - Confirm no dual-id stub (default: hard cutover + docs amend)
Human gate: accepted 2026-08-04
```

## After accept

T20A inventory note (broken-link risk table) → T20B thickness confirm → scrub via `/author-cursor-surfaces` → smoke → **human review → commit/push**.
