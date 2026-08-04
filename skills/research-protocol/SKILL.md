---
name: research-protocol
description: >-
  Write evidence-backed research notes and grade claims per Toolbelt PROTOCOL
  (FACT/CLAIM/INFERENCE/GAP/OPEN; E0–E4/U; cite-or-omit; conflict logs). Supports
  depth modes: normal (default) vs deep (parallel gatherers, waves, diminishing-
  returns stop). Use when documenting investigations, secondary research, design
  locks, auditing unsupported assertions, integrating parallel gatherer notes,
  theme/deep research campaigns, or adding Method envelopes and citations.
---

# Research protocol (notes + citations)

Announce once: **Using `research-protocol`**.

## When to use

- Any claim-bearing research write-up that needs a Method envelope
- Merging parallel notes into reports
- Auditing notes for missing citations or invented IDs
- Optional after `research-codebase-recon` / `research-docs` when a **full** note is warranted (short smokes may keep grades inside the checklist instead)
- **Deep** theme / multi-surface campaigns (user asks, or durable integrated-report goal)

## Note output path

Prefer (in order):

1. Host workspace `docs/research/notes/` (or `docs/research/reports/`) if present
2. A path the user specified
3. Ask before writing

## Depth (choose first)

Read `references/research-depth-modes.md` **when** choosing or running a campaign.

| Mode | Default? | Use when |
|------|----------|----------|
| **normal** | **Yes** | Ordinary lookups, smokes, single checklist/note |
| **deep** | No | User asks for deep/theme research, **or** goal is a multi-surface integrated report / method SoT redesign |

**Caveats (always):**

1. Do **not** auto-escalate normal questions to a gatherer fleet.
2. Deep **requires** the diminishing-returns stop rule (no endless agents).
3. Toolbelt owns deep dispatch, templates, grades, depth mode, and integrator merge — do not import third-party git/PR/worktree packaging as Toolbelt law.
4. Deep outputs stay `draft`/`proposed` until human acceptance (`draft-is-not-sot`).
5. Cite-or-omit binds every gatherer and the integrator.

Record in Method: `depth: normal | deep` (and for deep: `waves`, `stop_reason`).

## Instructions

1. Choose **depth** (default `normal`). If deep, follow `references/research-depth-modes.md` wave shape + stop rule.
2. Read `references/PROTOCOL.md` **when** enforcing grades, claim labels, or cite-or-omit — non-negotiables apply.
3. **Copy** `references/research-note.md` to the note output path **when** writing a full Method-envelope note (skip if only grading inside a recon/docs checklist). Fill Method (tools, queries, date, corpora/URLs, what was not searched, **depth**). Optional PROV light: Entity / Activity / Agent.
4. Every non-trivial finding: **label + grade + citation**. Consult `references/claim-citation.md` **when** choosing citation shape, conflict-log fields, or Alexandria locators.
5. **Citation defaults:** grade + locator (`url` | `path` | Alexandria `corpus`+`chunk_id` | E0). Short quotes recommended when contested. Spans optional. Markdown default; `claims[]` optional for machine merge.
6. **Conflicts:** cite both; prefer higher grade; runtime behavior → E0. Use conflict-log fields in claim-citation.
7. `draft` | `proposed` ≠ accepted SoT. No locks on `U` / uncorroborated E3.
8. Prefer `GAP`/`OPEN` over invention.
9. **Deep only — integrate:** merge gatherer notes into a draft report; no new facts; retain GAP/OPEN; record `stop_reason`.

## Self-check

- [ ] Depth chosen and recorded (`normal` default)
- [ ] If deep: stop rule applied and `stop_reason` recorded
- [ ] Method block present (for full notes)
- [ ] Every FACT/CLAIM has support
- [ ] INFERENCEs list premises
- [ ] No invented citations/APIs
- [ ] Conflicts logged when sources disagree
- [ ] Draft/proposed not treated as design law

## Handoffs

| Need | Use |
|------|-----|
| Expand / atomize / tracks before gather | **`guide-research`** (companion — when complex, theme/campaign, or user asks) |
| Codebase map first | `research-codebase-recon` |
| Product/docs pin | `research-docs` |
| After accepted research → design/plan | `guide-design` / `implementation-plan` |
| Full Toolbelt ladder | **`implementation-happy-path`** |
| Author Cursor surfaces from findings | `author-cursor-surfaces` |

## References

- Read `references/PROTOCOL.md` **when** enforcing grades, labels, or cite-or-omit (SoT: Toolbelt `docs/PROTOCOL.md`)
- Read `references/research-depth-modes.md` **when** choosing or running depth modes (SoT: `docs/templates/research-depth-modes.md`)
- Read `references/research-note.md` **when** writing a full Method-envelope note
- Read `references/claim-citation.md` **when** choosing citation shape or conflict-log fields
