---
name: research-codebase-recon
description: >-
  Run Toolbelt S0–S16 codebase/workspace reconnaissance before implementation
  or architecture docs. Use when exploring an unfamiliar repo, mapping structure,
  locating symbols before edits, investigating before coding, priming on a
  codebase, soft explore-before-edit, or brownfield derive needing git history /
  recency (conditional S12b). Prefer locate→view before edit; recommend Explore
  for broad searches; do not invent APIs. Formerly codebase-recon.
---

# Codebase reconnaissance

Announce once: **Using `research-codebase-recon`**.

## When to use

- Unfamiliar or large repos before non-trivial **implementation** changes
- User asks to explore / map / investigate before coding
- Soft explore-before-edit gate (S16) before **code** write tools

Skip for trivial single-file edits the user already scoped — still cite what you touch.

Writing research notes under the host project's research notes path is allowed during recon (not an S16 violation).

## Note output path

Prefer (in order):

1. Host workspace `docs/research/notes/` if that directory exists
2. A path the user specified
3. Ask before writing

Do not assume a foreign product or plugin layout.

## Instructions

1. Read `references/s0-s18-checklist.md` **when** starting recon, then **copy** it to a new file under the note output path. Do not edit the skill reference as the deliverable.
2. Fill **S0–S16**. Mark unmet items `GAP` — never invent paths, APIs, or commands.
3. **S2:** `systematic` | `as-needed` | `hybrid`; if as-needed, note missed-interaction risk.
4. **S8–S9:** Locate/search before edit. Prefer search → view → then edit. For large/unfamiliar scope, **recommend** Explore / investigation subagent; return summaries. Not mandatory for tiny known-file fixes.
5. **E0 on Windows:** Prefer small path-exists / Python checks over brittle PowerShell one-liners when listing trees (smoke: empty PS output ≠ missing files).
6. **S12:** Architecture/dependency recovery only if the goal warrants it.
7. **S12b (conditional):** Git history / recency when derive, brownfield, era conflict, or user asks — default window **12 months** (host may override date/months/years). On conflicting patterns, prefer **most recent non-one-off** as propose candidate; light hot-path churn only supports one-off/quarantine. Honor `.git-blame-ignore-revs` when present. Skip + reason otherwise. Cite-or-omit; output stays evidence for **proposed** standards, not silent SoT (Theme 18).
8. **S13 durable findings (either is OK):**
   - **Short / smoke:** graded findings section inside the filled checklist note (FACT/CLAIM/… + citations), **or**
   - **Full / multi-pass:** also run `research-protocol` / copy `research-note.md` with Method block.
9. **S16:** Do **not implement product/code changes** until gate passes or human waives. Soft only (no hard hooks unless product opts in later).
10. After gate: incremental edit → verify/test from repo instructions (S17).

**Depth:** Default **normal** (this S0–S16 checklist). If the user asks for deep/theme codebase research across many subsystems with an integrated report, escalate to skill **`research-protocol`** depth=`deep` — do not spawn unbounded explore fleets for ordinary recon.

When filling the checklist, keep the copied note as the working artifact; re-open `references/s0-s18-checklist.md` only if the copy is missing sections.

## Hard constraints

- Cite-or-omit; no invented APIs/IDs
- Draft recon notes ≠ accepted design law
- Prefer progressive disclosure over whole-tree dumps

## Handoffs

| Need | Use |
|------|-----|
| Expand / tracks before recon | `guide-research` |
| Full graded multi-pass note | `research-protocol` |
| Docs/API corroboration | `research-docs` |
| After gate → design | `guide-design` |
| After gate → plan/implement | `implementation-plan` → verify → execute |
| Brownfield standards derive (consumes S12b) | `author-standards` (`derive`) |
| Full Toolbelt ladder | **`implementation-happy-path`** |

## References

- Read `references/s0-s18-checklist.md` **when** starting or recovering S0–S16 steps
- SoT: Toolbelt `docs/templates/codebase-reconnaissance.md`
- Theme: Toolbelt `docs/research/reports/theme-1-codebase-research-for-agents.md`
