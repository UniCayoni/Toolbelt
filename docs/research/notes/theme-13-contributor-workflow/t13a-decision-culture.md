---
title: "Theme 13 T13A — Toolbelt decision culture (normal)"
status: draft
theme: theme-13-contributor-workflow
track: T13A
created: 2026-07-31
updated: 2026-07-31
authors: [coordinator]
depth: normal
aligned_with:
  - docs/research/notes/theme-13-contributor-workflow/campaign-brief.md
  - docs/PROTOCOL.md
  - docs/packs/README.md
supersedes: null
---

# T13A — Toolbelt decision culture (E0 inventory)

**Using `research-protocol`**; depth: **normal**.  
**Using `research-codebase-recon`** (as-needed) for layout/packs pointers only.

**Status:** `draft`. Not contributor SoT. Feeds T13B/C/D after more evidence.

---

## 1. Scope

- **Question:** What self-imposed standards and historical leans already govern how Toolbelt accepts design/feature/method changes?
- **In:** PROTOCOL, always-on rules, packs Phase 2 parks, theme accept→elevate pattern, surface authoring, naming, validation culture, happy-path stop before PR.
- **Out:** External OSS CONTRIBUTING comparison (T13B); elevating CONTRIBUTING.md this pass; deep fleets.

---

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-31 |
| Tools used | Read PROTOCOL, `draft-is-not-sot`, packs README, Theme 5/9/10/12 reports (elevation tables), `author-cursor-surfaces` caveats, CHANGELOG rename table; Grep Phase 2 / CONTRIBUTING |
| Corpora / URLs | Local Toolbelt only (E0) |
| Queries (exact) | `CONTRIBUTING\|pull_request_template\|Phase 2\|PR / workflow` under repo |
| What was *not* searched | External GitHub community health files; live GitHub Settings; other orgs’ private contribution policies |
| Depth | normal |
| stop_reason | E0 culture map sufficient for T13A; external patterns deferred to T13B |

---

## 3. Findings — authority ladder

- `FACT` [E0] Research Protocol requires cite-or-omit, claim labels (FACT/CLAIM/INFERENCE/GAP/OPEN), evidence grades E0–E4/U, Method recording, and forbids U/uncorroborated E3 as design locks. [E0: `docs/PROTOCOL.md`]
- `FACT` [E0] Always-on rule `draft-is-not-sot`: `draft`/`proposed` research, designs, plans, and proposed ADRs are **not** accepted law; prefer `accepted` research/ADRs and E0+E1 facts. [E0: `rules/draft-is-not-sot.mdc`]
- `FACT` [E0] Always-on rule `research-protocol-grades` binds grades/labels in sessions (companion to PROTOCOL). [E0: `rules/research-protocol-grades.mdc` present in packs/README framing]
- `INFERENCE` [E4] For contributors, “mergeable” method/design work must clear **human accept** (or equivalent accepted ADR/report), not merely open a PR with draft notes. Premises: draft≠SoT [E0]; theme reports use `accepted_by: human` [E0 Theme 5/9/10/12].

---

## 4. Findings — change pipeline (how Toolbelt actually evolved)

Observed recurring pattern across Themes 5–12 (E0 from accepted reports + packs):

```text
scope / research-scope (when complex)
  → research (normal or deep) — draft notes
  → integrate draft report
  → human accept (facts / method / elevation decisions)
  → elevate via author-cursor-surfaces (skills/rules/templates)
  → refresh-skill-references + sync-toolbelt-local-plugin + Reload
  → optional E0 smokes (Theme 11 culture)
  → stop / hand human  (PR/CI = Phase 2 stub — not owned by happy-path)
```

- `FACT` [E0] Packs list **PR / workflow** as **stub / Phase 2**; Research→Happy-path shipped. Elevate further surfaces only after accepted research. [E0: `docs/packs/README.md`]
- `FACT` [E0] Theme 10 D7: PR/CI remains Phase 2 stub; ladder ends at stop/human handoff. [E0: `docs/research/reports/theme-10-happy-path.md`]
- `FACT` [E0] Theme 9 parks PR/CI/Bugbot mega-pack as Phase 2 list-only — not Debug pocket law. [E0: `docs/research/reports/theme-9-debug-pocket.md`]
- `FACT` [E0] Theme 5: do not elevate Design skills until report accepted; elevation via `author-cursor-surfaces` after accept; ADR house + Considered Options required. [E0: theme-5 report elevation section]
- `FACT` [E0] `author-cursor-surfaces`: new surfaces stay draft until human accepts; prefer skill over fat always-on rules; compose don’t paste; standalone — do not invent merged third-party git/PR policy as Toolbelt law. [E0: `skills/author-cursor-surfaces/SKILL.md` caveats]
- `FACT` [E0] Theme 12: companion `research-scope` for expand/atomize/tracks; enough-to-start = agent proposes + human accepts; no scoping spine inside `research-protocol`. [E0: theme-12 report D3/D6/D8]
- `FACT` [E0] Theme 11: P0 surfaces validated with claim-card E0 smokes (18/18); no mandatory elevation from that campaign. [E0: theme-11 report / packs]
- `GAP` No root `CONTRIBUTING.md`, `.github/pull_request_template.md`, or `CODEOWNERS` found in live tree this pass. Searched: Grep CONTRIBUTING / pull_request_template. Result: archive smoke mentions only; packs stub only. [E0: Grep 2026-07-31]

---

## 5. Findings — surface & naming leans (contributor-relevant)

- `FACT` [E0] Domain-first skill ids (`research-*`, `design-*`, `implementation-*`, `debug-*`, `author-*`) documented as breaking renames in CHANGELOG Unreleased; descriptions carry “formerly …”. [E0: `CHANGELOG.md`]
- `FACT` [E0] Theme 4 / author skill: `name` must match folder; thin always-on; relative paths; sync after elevate. [E0: author-cursor-surfaces]
- `FACT` [E0] Intelligent (not always-on) `research-before-write`: soft explore-before-edit via `research-codebase-recon`. [E0: `rules/research-before-write.mdc`]
- `INFERENCE` [E4] Drive-by PRs that add skills without Theme 4 reinforce, accept gate, or domain-first naming will fight repo culture even if CI is green. Premises: author caveats [E0]; packs “elevate after accepted research” [E0]; rename table [E0].

---

## 6. Decision taxonomy (how choices get locked)

| Change type | Historical lean (E0) | Typical gate |
|-------------|----------------------|--------------|
| Method / pocket law | Theme campaign → accepted report → elevate | Human accept + author-cursor-surfaces |
| Architecture / process lock | ADR with Considered Options | `research-draft-adr`; proposed ≠ law until accepted |
| Design options | `design-process` + domain skill + human accept | draft design ≠ SoT |
| Implementation | plan → plan-verify → execute → execute-verify | Meta `ready`; verify companions |
| Bugfix | debug-reproduce / debug-systematic | Evidence; not PR pack |
| Fuzzy multi-surface research | `research-scope` then protocol/recon/docs | Human accept enough-to-start |
| Plugin packaging / marketplace | Theme 4 + create-plugin review (external) | Not invented git/PR law in Toolbelt |
| PR / CI / Bugbot | **Parked Phase 2** | Explicit non-ownership today |

---

## 7. Implications for contributor docs (INFERENCE only — not locks)

- `INFERENCE` [E4] CONTRIBUTING (when written) should **front-load** draft≠SoT, cite-or-omit, accept→elevate, and “PR pack not shipped yet” — or outsiders will treat draft notes as merge criteria. Premises: §3–4 [E0].
- `INFERENCE` [E4] Prefer pointing contributors at **accepted theme reports + packs + author-cursor-surfaces** over re-teaching pocket spines in CONTRIBUTING. Premises: Theme 10 D8 orchestration-only spirit [E0]; author compose mode [E0].
- `INFERENCE` [E4] T13B should look for OSS patterns that match **design-first / proposal / thin templates**, and park heavy CLA/bot stacks under T13D unless E1 shows clear need. Premises: author caveat #6 [E0]; Theme 9/10 Phase 2 parks [E0].

---

## 8. Gaps & OPEN

| ID | Item | Follow-up |
|----|------|-----------|
| G1 | No live CONTRIBUTING / PR template | T13C after T13B |
| G2 | Themes 1–3 reports lack Theme-10-style `accepted` frontmatter (older integrated reports) | Optional packing; don’t block T13 |
| G3 | Comparator shortlist unset | Human pin or T13B Method chooses 3–6 |
| OPEN | Whether contributor path elevates a skill vs docs-only | T13C |

---

## 9. Source list

1. `docs/PROTOCOL.md`
2. `rules/draft-is-not-sot.mdc`
3. `rules/research-before-write.mdc`
4. `docs/packs/README.md`
5. `docs/research/reports/theme-5-design-pocket.md`
6. `docs/research/reports/theme-9-debug-pocket.md`
7. `docs/research/reports/theme-10-happy-path.md`
8. `docs/research/reports/theme-11-validation.md`
9. `docs/research/reports/theme-12-research-scoping.md`
10. `skills/author-cursor-surfaces/SKILL.md`
11. `CHANGELOG.md`
12. Theme 13 [`campaign-brief.md`](./campaign-brief.md) (accepted scope)
