---
title: "T23A — Toolbelt toolbox inventory"
status: draft
theme: theme-23-host-playbook
depth: deep
created: 2026-08-04
updated: 2026-08-04
authors: [t23a-gatherer]
supersedes: null
---

# T23A — Toolbelt toolbox inventory

## 1. Scope

- Question / goal: Inventory **all live** Toolbelt surfaces (skills, rules, host-facing templates, packs grouping) as feedstock for a future host adoption playbook — intent, good-for, limits, typical next/handoff.
- In scope: `skills/*/SKILL.md`, `rules/*.mdc`, host-copy templates under `docs/templates/`, pack rows in `docs/packs/README.md`, plugin identity in `.cursor-plugin/plugin.json`.
- Out of scope: Elevating `docs/host-playbook.md`; editing `skills/`; Theme 24 learn-back; contributor CI / Phase 2 ceremony; grey-matter; inventing APIs or unlisted surfaces; treating this draft as law.
- Comprehension / research goal type: reuse (operator feedstock) + adaptive (map current toolbox).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-04 |
| Tools used | Read (skill `research-protocol` + note template); Glob (`skills/*/SKILL.md`, `rules/*.mdc`, `docs/templates/**`); Shell (PowerShell extract of skill FM/sections; template first lines; counts); Grep (thin-section checks); Read (`docs/packs/README.md`, `docs/templates/README.md`, `.cursor-plugin/plugin.json`, campaign brief) |
| Corpora / URLs searched | None (E0 local only) |
| Queries (exact) | Glob skills/rules/templates; dump/extract all SKILL.md; dump all rules; list template intros |
| What was *not* searched | Historical renamed IDs as current law; Theme reports for surface intent (except packs README pointers); plugin install paths outside workspace; marketplace; agent transcripts; `references/` bodies beyond SKILL front doors; web/RAG; host project catalogs outside Toolbelt |
| Depth | deep |
| Waves / stop_reason | Wave 1 gatherer T23A; `stop_reason`: all live `SKILL.md` (26) + `rules/*.mdc` (4) + templates README + packs README read; diminishing returns on re-reading reference checklists |
| Provenance (optional PROV) | Entity←workspace paths below; Activity=T23A inventory; Agent=Cursor gatherer |

**Using `research-protocol`**. Depth: **deep**. Draft ≠ law.

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | systematic |
| Why this mode | Campaign requires complete live-surface matrix |
| Scope boundary | Included: `d:\Toolbelt\skills\`, `rules\`, `docs\templates\`, `docs\packs\README.md`, `.cursor-plugin\plugin.json`. Excluded: editing surfaces; Theme 23 elevate; Theme 24 |

## 4. Findings — pack grouping

`FACT` [E0] Packs table groups shipped surfaces by pocket (Research, Design, Plan, Execute, Verify gates, Debug, Routers/pocket entry, Happy path, Closeout, Host standards, Validation smokes, Contributor/GitHub). [E0: `docs/packs/README.md`]

| Pack (from packs README) | Status (as stated) | Surfaces (as stated) |
|--------------------------|--------------------|----------------------|
| Research | shipped | recon, docs, protocol, guide-research, author-agents-md, draft-adr, author-cursor-surfaces, author-standards |
| Design | shipped (Theme 5); UX T5C deferred | guide-design, design-* ×4; rule draft-is-not-sot |
| Plan | shipped | implementation-plan (+ plan-verify); template plan-minimal; docs/plans/ |
| Execute | shipped | implementation-execute, -subagents (+ execute-verify) |
| Verify gates | shipped | plan-verify, execute-verify (not Debug/PR) |
| Debug / investigate | shipped | debug-systematic, debug-reproduce; repro-light |
| Routers / pocket entry | shipped | guide-* + guide-meta (not always-on); standards resolve if-present |
| Happy path | shipped | implementation-happy-path; happy-path.md |
| Closeout readiness | shipped | implementation-closeout; closeout templates (ceremony Phase 2) |
| Host standards | shipped | author-standards, guide-standards, catalog/module templates, standards-resolve-gate |
| Validation / E0 smokes | shipped | Theme 11 evidence path (no new elevation) |
| Contributor / GitHub | shipped (docs) | CONTRIBUTING + PR template; CI automation Phase 2 |

`FACT` [E0] Packs README: keep new rules intelligent/opt-in by default except thin always-on (draft≠SoT); UX skills wait on T5C placeholder. [E0: `docs/packs/README.md` L18]

`FACT` [E0] Plugin `displayName` Toolbelt v0.1.0 describes research→closeout + guide-meta + standards + happy-path; “Not a Brain/RAG product.” [E0: `.cursor-plugin/plugin.json`]

---

## 4b. Primary artifact — surface matrix

Columns: **id** | **kind** | **pocket/pack** | **intent** | **good-for** | **limits** | **typical next/handoff**

Counts: **26 skills**, **4 rules**, **24 templates** (excl. README). [E0: Shell count 2026-08-04]

### Guides / meta

| id | kind | pocket/pack | intent | good-for | limits | typical next/handoff |
|----|------|-------------|--------|----------|--------|----------------------|
| guide-meta | skill | Routers / meta | Global front door: classify fuzzy/cold-start → name **exactly one** next surface | “Which skill?”, “where do I start?”, mixed multi-pocket asks | Not always-on; not pocket spine; not PIPELINE planner; **host onboarding playbook content out of scope** (separate when elevated) [E0: `skills/guide-meta/SKILL.md`] | One of: guide-*, happy-path, author-standards, author-cursor-surfaces, closeout, or named leaf |
| guide-research | skill | Research / routers | Expand/atomize fuzzy research; tracks; enough-to-start gate | Theme/campaign before gather; unclear tracks | Not graded notes; not S0–S18/D0–D14 rewrite; skip ordinary single-note lookup [E0: `skills/guide-research/SKILL.md`] | research-protocol / recon / docs; later guide-design |
| guide-design | skill | Design / routers | Design-before-implement spine + HITL gate | Non-trivial design; options/tradeoffs before code | UX/UI deferred T5C; domain depth → design-* leaves [E0: `skills/guide-design/SKILL.md`] | design-* → ADR → guide-implementation / plan |
| guide-implementation | skill | Routers / Impl | Classify → wire plan over plan/verify/execute leaves | Unclear which Impl skill; after design accept | Not writing plans/executing; not guide-meta [E0: `skills/guide-implementation/SKILL.md`] | plan → plan-verify → execute (±subagents) → execute-verify; or guide-debug |
| guide-debug | skill | Routers / Debug | Classify prove vs fix; wire debug leaves | After Execute N=2; which debug skill | Not Theme 9 spine restatement; not PR/CI [E0: `skills/guide-debug/SKILL.md`] | debug-reproduce and/or debug-systematic |
| guide-standards | skill | Host standards / routers | Resolve which host modules to load (pointers only) | Accepted catalog present; selective load | Compose-only; no-op if empty shelf; not authoring [E0: `skills/guide-standards/SKILL.md`] | Load pointed modules; author-standards if creating feedstock |
| implementation-happy-path | skill | Happy path | Orchestrate end-to-end feature ladder via pocket guides | Full feature pipeline / cold-start ladder | Not single-pocket wire; not worker-only skill; not trivial one-file [E0: `skills/implementation-happy-path/SKILL.md`] | guide-meta if unclear; else chain guide-* + optional closeout |

### Research

| id | kind | pocket/pack | intent | good-for | limits | typical next/handoff |
|----|------|-------------|--------|----------|--------|----------------------|
| research-protocol | skill | Research | Method-envelope notes; grades; deep waves | Claim-bearing write-ups; integrate gatherers; deep campaigns | Checklist smokes may skip full note; draft≠law [E0: `skills/research-protocol/SKILL.md`] | guide-research (expand); recon/docs; after accept → guide-design / plan |
| research-codebase-recon | skill | Research | S0–S16 workspace recon before impl/arch docs | Unfamiliar repo; explore-before-edit; S12b for derive | Do not invent APIs; skip trivial scoped edits; deep multi-subsystem → protocol [E0: `skills/research-codebase-recon/SKILL.md`] | protocol / docs / guide-design / plan / author-standards derive |
| research-docs | skill | Research | D0–D14 docs research + docs↔code | API/behavior from docs; version pin; limitations | Prefer corroboration; cite-or-omit [E0: `skills/research-docs/SKILL.md`] | protocol; recon; draft-adr; design/plan |
| research-draft-adr | skill | Research | House ADR after design/research lock | Locking choices; rejecting alternatives | Explicit/invoke; `GAP`: no dedicated `## When to use` section in SKILL (intent mainly in description) [E0: `skills/research-draft-adr/SKILL.md`] | After accept → plan + plan-verify |

### Design

| id | kind | pocket/pack | intent | good-for | limits | typical next/handoff |
|----|------|-------------|--------|----------|--------|----------------------|
| design-technical | skill | Design | Code architecture / boundaries / stack criteria at design-time | Modularity, services, feature shape before code | Not lint pack; not UX; not MDA-as-Clean-Architecture [E0: `skills/design-technical/SKILL.md`] | guide-design spine; draft-adr; plan |
| design-systems | skill | Design | Game/creative *systems* (MDA-class et al.) | Loops, economies, tuning | Not story/world/UX/engines-as-law [E0: `skills/design-systems/SKILL.md`] | guide-design; technical/ADR; plan |
| design-narrative | skill | Design | Storylines/quests/interactive narrative | Plot/quest/branching ↔ gameplay | Not world bible; not systems balance; not UX [E0: `skills/design-narrative/SKILL.md`] | guide-design; systems/world; plan |
| design-world-character | skill | Design | World bibles + characters/consistency | Setting, cast, continuity | Not quests; not combat systems; not UX [E0: `skills/design-world-character/SKILL.md`] | guide-design; narrative/systems; plan |

### Plan

| id | kind | pocket/pack | intent | good-for | limits | typical next/handoff |
|----|------|-------------|--------|----------|--------|----------------------|
| implementation-plan | skill | Plan | Hybrid agent plans: checkable tasks, Done-when, T0–T3 | Durable plans for fresh agents after approved design | No planning from draft design as law; no mandatory TDD/PR ceremony [E0: `skills/implementation-plan/SKILL.md`] | **implementation-plan-verify** → ready → execute |
| plan-minimal.md | template | Plan | Host-copy plan shape under `docs/plans/` | Durable plan artifacts | Working notes must copy out, not edit template in place [E0: `docs/templates/README.md` Rules; `docs/templates/plan-minimal.md`] | plan-verify |

### Execute

| id | kind | pocket/pack | intent | good-for | limits | typical next/handoff |
|----|------|-------------|--------|----------|--------|----------------------|
| implementation-execute | skill | Execute | Approved-plan task loop; Done-when; N=2 | Multi-file/multi-task from written plan | No inventing outside plan; not plan write; not Debug method [E0: `skills/implementation-execute/SKILL.md`] | execute-verify; on fail after N=2 → debug leaves / guide-debug |
| implementation-execute-subagents | skill | Execute | Controller + fresh implementers per task | Multi-task; keep parent short | Not for single tiny task; needs approved plan [E0: `skills/implementation-execute-subagents/SKILL.md`] | Same as execute → execute-verify / debug |

### Verify

| id | kind | pocket/pack | intent | good-for | limits | typical next/handoff |
|----|------|-------------|--------|----------|--------|----------------------|
| implementation-plan-verify | skill | Verify gates | Pre-exec plan validate (PASS / NOTES / NEEDS REVISION) | Before Meta ready / execute | Not execute-verify; not Debug; not inventing design intent [E0: `skills/implementation-plan-verify/SKILL.md`] | PASS* → execute; else rewrite plan / human |
| implementation-execute-verify | skill | Verify gates | Evidence iron law; post-green; EOP light converge | After green tasks / end-of-plan | No silent Goal rewrite; not PR/Debug pack [E0: `skills/implementation-execute-verify/SKILL.md`] | Convergence tasks → execute; unclear Critical → debug |

### Debug

| id | kind | pocket/pack | intent | good-for | limits | typical next/handoff |
|----|------|-------------|--------|----------|--------|----------------------|
| debug-reproduce | skill | Debug | Never-fix: prove bug + light 8-field dossier | Prove/minimize/flaky before patch | Does **not** implement fixes [E0: `skills/debug-reproduce/SKILL.md`] | **debug-systematic** |
| debug-systematic | skill | Debug | Reproduce → falsify → minimal fix → same repro; cycles=3 | Bugs/regressions; after Execute N=2 | Not Theme 8 verify; not PR; prefer reproduce first when prove-only [E0: `skills/debug-systematic/SKILL.md`] | guide-debug / execute-verify / plan if design wrong |
| repro-light.md | template | Debug | Light repro dossier fields | Host `docs/repro/` or `REPRO.md` | Theme 9; used by debug-reproduce [E0: `docs/templates/repro-light.md`] | debug-systematic |

### Closeout

| id | kind | pocket/pack | intent | good-for | limits | typical next/handoff |
|----|------|-------------|--------|----------|--------|----------------------|
| implementation-closeout | skill | Closeout | Host-owned closeout profile + evidence score | Ship-ready **check**; DoD-style criteria | **Not** commit/push/PR/merge ceremony [E0: `skills/implementation-closeout/SKILL.md`] | Human/host CONTRIBUTING for ceremony |
| closeout-profile.md | template | Closeout | Host-owned criteria profile | Durable DoD | Theme 15; active [E0: `docs/templates/closeout-profile.md`] | closeout checklist / skill |
| closeout-readiness-checklist.md | template | Closeout | Score criteria vs cited evidence | Readiness verdict | Not merge automation [E0: `docs/templates/closeout-readiness-checklist.md`] | Human ship |

### Host standards

| id | kind | pocket/pack | intent | good-for | limits | typical next/handoff |
|----|------|-------------|--------|----------|--------|----------------------|
| author-standards | skill | Host standards | Author principles/standards; derive; light bind-check | Host style/principles feedstock | Not Toolbelt-universal coding law; not always-on standards rule; derive≠accepted [E0: `skills/author-standards/SKILL.md`] | guide-standards apply; AGENTS pointer; plan/execute/closeout bind |
| standards-catalog.md | template | Host standards | Host catalog index | guide-standards + resolve-gate | Lean default path `docs/standards/index.md` (rule) [E0: `docs/templates/standards-catalog.md`; `rules/standards-resolve-gate.mdc`] | modules |
| standards-module.md | template | Host standards | One checkable module | Progressive load | Draft/proposed ≠ law | guide-standards pointers |
| standards-profile.md / principles-profile.md | template | Host standards | Profile shapes for author-standards | Host authoring | Theme 16 active [E0: templates] | catalog index |
| author-standards-checklist.md | template | Host standards | Authoring checklist | Mode checklist | Theme 16/18 [E0: template] | author-standards |
| guide-standards.md | template | Host standards | Router checklist | Skill companion | Theme 19/21 [E0: template] | module paths |

### Authoring

| id | kind | pocket/pack | intent | good-for | limits | typical next/handoff |
|----|------|-------------|--------|----------|--------|----------------------|
| author-cursor-surfaces | skill | Authoring / Research pack | Author skills/rules/commands/hooks per Theme 4 | New/compose Cursor surfaces | Explicit/invoke; not review/audit skill; thin always-on; draft until accept [E0: `skills/author-cursor-surfaces/SKILL.md`] | author-agents-md; research-docs/protocol for API facts |
| author-agents-md | skill | Authoring / Research pack | Portable AGENTS.md from skeleton | Bootstrap agent instructions; budgets | Explicit/invoke; keep short pointers for standards [E0: `skills/author-agents-md/SKILL.md`] | author-cursor-surfaces; author-standards; ADR; recon |
| agents-md-skeleton.md | template | Authoring | AGENTS.md baseline | Portable house ops | Progressive disclosure [E0: `docs/templates/agents-md-skeleton.md`] | author-agents-md |
| author-cursor-surfaces.md | template | Authoring | Theme 4 checklist | Surface authoring | Accepted Theme 4 authority [E0: template] | skill |

### Research / method templates (host-copy working notes)

| id | kind | pocket/pack | intent | good-for | limits | typical next/handoff |
|----|------|-------------|--------|----------|--------|----------------------|
| research-note.md | template | Research | Method-envelope note shape | Full graded notes | Copy out; draft≠law [E0: `docs/templates/README.md`] | research-protocol |
| research-depth-modes.md | template | Research | normal vs deep | Campaign depth choice | PROTOCOL authority [E0: template] | protocol |
| research-campaign-brief.md | template | Research | Campaign brief (guide-research) | Theme scope | Theme 12 [E0: template] | gather skills |
| codebase-reconnaissance.md | template | Research | S0–S18 checklist SoT copy | Recon working note | Skill text says S0–S16; reference file named s0-s18 — naming tension [E0: skill + `docs/templates/codebase-reconnaissance.md`] | `OPEN`: reconcile S16 vs S18 labeling for playbook |
| documentation-research.md | template | Research | D0–D14 | Docs research notes | Copy out | research-docs |
| claim-citation.md | template | Research | Citation shape | Claim audits | PROTOCOL [E0: template] | protocol |
| doc-layers.md | template | Research | Which doc format | Choosing note/ADR/etc. | Reference cheat sheet [E0: template] | authoring/docs |
| adr-minimal.md | template | Research | ADR shape | Decision records | Frontmatter status proposed in template [E0: `docs/templates/adr-minimal.md`] | draft-adr |
| guide-meta.md / guide-debug.md / guide-implementation.md / happy-path.md | template | Guides | Pocket/meta checklists | Skill companions | Not always-on routers [E0: templates] | matching skills |

`GAP`: `docs/templates/README.md` “When agents must use these” table omits several host-facing templates that exist on disk (`plan-minimal`, `happy-path`, `repro-light`, closeout pair, `guide-implementation`). [E0: compare `docs/templates/README.md` vs Glob of `docs/templates/*.md`]

---

## 4c. Rules matrix

| id | kind | pocket/pack | alwaysApply | intent | good-for | limits | typical next/handoff |
|----|------|-------------|-------------|--------|----------|--------|----------------------|
| draft-is-not-sot | rule | Cross-cutting | **true** | Draft/proposed research, design, plans, ADRs ≠ accepted law | Blocks locking architecture/MVP from drafts; UX skills not elevated until T5C [E0: `rules/draft-is-not-sot.mdc`] | Prefer accepted research/ADRs / E0+E1 | N/A ambient |
| research-protocol-grades | rule | Research | **true** | Ambient cite-or-omit + E0–E4/U + labels | Any claim-bearing work; announce Using skill; deep only when asked/multi-surface [E0: `rules/research-protocol-grades.mdc`] | Thin; full Method → research-protocol | research-protocol |
| standards-resolve-gate | rule | Host standards | **true** | If accepted host catalog → guide-standards; else no-op | Selective standards apply without pasting corpora [E0: `rules/standards-resolve-gate.mdc`] | Not Toolbelt coding law; no invent when absent | guide-standards / author-standards |
| research-before-write | rule | Research / Impl soft gate | **false** (intelligent) | Soft explore-before-edit before non-trivial code writes | Unfamiliar areas / large refactors [E0: `rules/research-before-write.mdc`] | Soft only; research notes exempt; hard hooks deferred | research-codebase-recon or human waive |

`FACT` [E0] Always-on rules: 3 (`draft-is-not-sot`, `research-protocol-grades`, `standards-resolve-gate`). Intelligent: 1 (`research-before-write`). [E0: rules frontmatter]

---

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Live skill count for playbook catalog is 26 unique `skills/*/SKILL.md` | confirmed | Shell count + Glob (duplicate path separators collapsed) |
| H2 | Host playbook “start here” should center guide-meta + thin always-on rules, not full skill encyclopedia | open (playbook craft = T23B) | guide-meta when-to-use + out-of-scope playbook note [E0: `skills/guide-meta/SKILL.md`] |
| H3 | S0–S16 (skill body) vs S0–S18 (template/reference name) needs playbook-safe wording | open | Grep skill vs template filename |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Recon step range | Skill describes **S0–S16** [`skills/research-codebase-recon/SKILL.md`] | Template/reference named **s0-s18** / codebase-reconnaissance Theme 1 S0–S18 [`docs/templates/README.md`, `docs/templates/codebase-reconnaissance.md`] | Prefer skill front-door for “what agents run”; leave `OPEN` for label reconciliation — do not invent which steps exist without reading checklist body (not fully re-read this pass) |
| Templates index completeness | templates README table | Actual `docs/templates/*.md` set | README incomplete as catalog; packs README + this matrix stronger for host-facing list |

## 7. Gaps & OPEN

- `GAP`: `research-draft-adr` thin on structured When-to-use / Out-of-scope sections (description carries intent).
- `GAP`: templates README not a complete host-template catalog.
- `OPEN`: Playbook path name (campaign lean: `docs/host-playbook.md`) — elevate deferred to T23C.
- `OPEN`: Inventory appendix vs embedded compact catalog in playbook — T23B/C.
- `OPEN`: S16 vs S18 recon labeling for host-facing docs.
- `OPEN`: Per-leaf anti-pattern depth in playbook — many skills have rich anti-patterns; this note summarizes, not exhaustively quotes all.

## 8. Implications for host playbook (INFERENCE only)

Do **not** elevate playbook from this note alone (`draft-is-not-sot`).

1. `INFERENCE` [E4] **Start-here layer** must lead with **`guide-meta`** (cold/fuzzy entry) + **`implementation-happy-path`** (full ladder) + pocket **`guide-*`** (local wire) — not a flat dump of 26 skills. Premises: (1) guide-meta purpose/limits [E0: SKILL]; (2) happy-path vs pocket split [E0: skills + packs].
2. `INFERENCE` [E4] Playbook must explain **three always-on rules** (draft≠SoT, grades, standards gate no-op) so hosts know ambient behavior without mistaking Toolbelt for universal coding law. Premises: rules FM alwaysApply [E0].
3. `INFERENCE` [E4] **Setup / copy-once** section should list host-facing templates: AGENTS skeleton, standards catalog/module/profiles, closeout profile/checklist, plan-minimal, repro-light — with “copy out, don’t edit template” rule. Premises: templates README Rules + active closeout/standards/plan templates [E0].
4. `INFERENCE` [E4] **Appendix catalog** (or linked inventory) should hold leaf skills (research/design/plan/execute/verify/debug/authoring) with good-for/limits/handoff — progressive disclosure. Premises: packs encyclopedia vs router design [E0: packs + guide-* anti always-on meta].
5. `INFERENCE` [E4] Playbook must call out **explicit outs**: UX/UI (T5C deferred), PR/merge/CI ceremony (Phase 2 / host), empty standards shelf = normal silence, draft research/design/plan ≠ law. Premises: packs L18; closeout/execute limits; draft-is-not-sot; guide-standards skip [E0].

## 9. Source list (deduped)

1. `skills/*/SKILL.md` (26) — E0 2026-08-04
2. `rules/draft-is-not-sot.mdc`
3. `rules/research-protocol-grades.mdc`
4. `rules/standards-resolve-gate.mdc`
5. `rules/research-before-write.mdc`
6. `docs/packs/README.md`
7. `docs/templates/README.md` + 24 template files under `docs/templates/`
8. `.cursor-plugin/plugin.json`
9. `docs/research/notes/theme-23-host-playbook/campaign-brief.md` (scope only; accepted brief ≠ playbook elevate)
10. Skill `research-protocol` / `references/research-note.md` (Method shape)
