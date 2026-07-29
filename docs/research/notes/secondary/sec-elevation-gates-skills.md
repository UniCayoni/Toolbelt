# Secondary note — elevation gates (skills / rules / hooks / subagents)

Status: notes only (not integrated report)  
Date: 2026-07-27  
Agent: sec-elevation-gates-skills  
Authority: `docs/research/PROTOCOL.md`

## 1. Scope

Decide (with evidence) how GreyMatter should elevate research templates into Cursor surfaces:

1. Re-fetch Cursor docs for Skills, Rules, Hooks, Subagents — what each is for (E1).
2. Map Theme templates → recommended surface(s).
3. Soft vs hard explore-before-edit (T1 OPEN / T1-OPEN gate): skills/rules = soft; hooks = hard — cite Claude + Cursor.
4. Whether investigation should default to Explore subagent (recommended vs mandatory).
5. Propose skill `name` + `description` (agentskills.io “Use when…” style) for each recommended skill — descriptions only; **no** full `SKILL.md` bodies.
6. FAIR4RS / Lamprecht if fetchable in ≤2 fetches; else GAP.

**Out of scope this note:** full skill files, plugin stub, locking MVP feature scope.

## 2. Method

| Item | Detail |
|------|--------|
| Tools | WebFetch (Cursor docs ×4; Claude Code best practices; agentskills.io specification; Lamprecht PDF + FAIR4RS PDF via search/fetch); Read (PROTOCOL, SECONDARY_PRIORITIES, Theme 1 report/OPEN items, t1b note, templates README); Grep (local research corpus) |
| Queries / URLs | `https://cursor.com/docs/skills.md`; `…/rules.md`; `…/hooks.md`; `…/subagents.md`; `https://code.claude.com/docs/en/best-practices`; `https://agentskills.io/specification`; Lamprecht 2020 + FAIR4RS v1.0 PDFs |
| Date | 2026-07-27 |
| Local context | `docs/research/templates/*`, Theme 1 implications §7, `SECONDARY_PRIORITIES.md` P1 T1-OPEN gate |
| Not used | Alexandria RAG this pass; no E0 Cursor product UI inspection |

## 3. Findings

### 3.1 Cursor surfaces — what each is for (E1)

- `FACT` [E1]: **Skills** package domain workflows (instructions + optional scripts/references/assets). Discovered from skill dirs; agent gets skill list and **decides relevance from `description`**; also invocable via `/skill-name`. Progressive disclosure (metadata → body → references). Frontmatter requires `name` + `description`. Dynamic rules / slash commands can migrate to skills; `alwaysApply` / globbed rules are **not** migrated. [E1: Cursor Skills — https://cursor.com/docs/skills.md — accessed 2026-07-27]

- `FACT` [E1]: **Rules** inject persistent prompt-level instructions (project `.mdc`, user, team, or plain `AGENTS.md`). Types: Always Apply / Apply Intelligently (description) / globs / manual `@`. Best for codebase conventions, scoped standards, short always-on guidance; keep under ~500 lines; prefer references over dumping docs. [E1: Cursor Rules — https://cursor.com/docs/rules.md — accessed 2026-07-27]

- `FACT` [E1]: **Hooks** are stdio JSON scripts (or prompt-hooks) on agent lifecycle events; can **observe, block, or modify** behavior. Examples: gate risky ops, scan secrets, control Task/subagent spawn, inject session context. Blocking via `permission: "deny"` / exit code `2` on hooks such as `preToolUse`, `beforeShellExecution`, `beforeReadFile`, `subagentStart`. Default fail-open unless `failClosed: true`. [E1: Cursor Hooks — https://cursor.com/docs/hooks.md — accessed 2026-07-27]

- `FACT` [E1]: **Subagents** are delegated agents with **isolated context**; built-ins include **Explore** (codebase search/analysis; faster model; parallel searches; noisy intermediates stay out of parent), Bash, Browser. Agent uses built-ins **automatically when appropriate**; custom agents live under `.cursor/agents/` with `description` driving Task-tool delegation. Docs contrast: use subagents for long research / parallel / specialized multi-step work; use **skills** for single-purpose repeatable actions. [E1: Cursor Subagents — https://cursor.com/docs/subagents.md — accessed 2026-07-27]

- `FACT` [E1]: Agent Skills description guidance (agentskills.io): `description` must say **what** and **when**; good pattern includes “Use when…”. [E1: Agent Skills Specification — https://agentskills.io/specification — accessed 2026-07-27]

### 3.2 Soft vs hard explore-before-edit (closes T1-OPEN gate directionally)

- `FACT` [E1]: Claude Code: “Explore first, then plan, then code”; plan mode separates exploration from execution. **CLAUDE.md / instructions are advisory**; **hooks are deterministic** and guarantee actions (“Unlike CLAUDE.md instructions which are advisory, hooks are deterministic…”). Use hooks for actions that must happen every time with zero exceptions (e.g. block writes). Use subagents for investigation so reads do not clutter main context. [E1: Claude Code best practices — https://code.claude.com/docs/en/best-practices — accessed 2026-07-27]

- `FACT` [E1]: Cursor skills/rules are **prompt / relevance** mechanisms (agent may ignore relevance misjudgment); Cursor hooks are the **enforcement** surface that can deny tool use. Official hooks docs **do not** ship a default explore-before-edit policy. [E1: Cursor Skills; Rules; Hooks — accessed 2026-07-27] [E0: Theme 1 report GAP — vendors do not mandate explore-before-edit by default — `docs/research/reports/theme-1-codebase-research-for-agents.md`]

- `INFERENCE` [E4]: Premises: (P1) Claude advisory instructions vs deterministic hooks [E1]; (P2) Cursor skills/rules = soft inclusion in context, hooks = hard allow/deny [E1]; (P3) Theme 1 implication #3 already proposed soft guidance vs hard gates [E4 prior]. → **Default GreyMatter elevation: soft explore-before-edit via Skill + optional Always/Intelligent Rule; hard gate only if product chooses enforcement via Hook** (e.g. `preToolUse` matcher on `Write` / `Delete` until a recon artifact exists). Measuring “enough comprehension” before writes remains `OPEN` [Theme 1 T1A].

### 3.3 Explore subagent — recommended vs mandatory

- `FACT` [E1]: Cursor documents Explore as the built-in for codebase search/analysis; Agent uses it **automatically when appropriate**; “You don't need to configure these subagents.” Automatic delegation also considers task complexity/scope. No E1 statement that Explore is required before every edit. [E1: Cursor Subagents — accessed 2026-07-27]

- `FACT` [E1]: Claude recommends subagents for investigation (context hygiene), not as a universal mandatory pre-edit law. [E1: Claude Code best practices — accessed 2026-07-27]

- `INFERENCE` [E4]: Premises: Explore is automatic-when-appropriate + context-isolation rationale [E1]; Theme 1 implication #4 defaults recon to isolated exploration but left mandatory vs recommended `OPEN`. → **Recommend** defaulting broad/unfamiliar recon to Explore (or equivalent Task explore) inside the codebase-reconnaissance skill; **do not** make Explore mandatory for every edit (narrow `@`-file fixes, known paths).

- `OPEN`: Whether GreyMatter ever **mandates** Explore (skill wording “always” / rule / hook denying Write without Task:Explore) — product policy; underspecified by vendor docs. Leave `OPEN` for integrator / product owner.

### 3.4 Template → surface map (elevation table)

| Template / artifact | Primary surface | Secondary / optional | Soft vs hard | Notes |
|---------------------|-----------------|----------------------|--------------|-------|
| `codebase-reconnaissance.md` (S0–S18) | **Skill** | Recommend **Explore** subagent for broad recon; optional Intelligent Rule “before large edits, run recon” | Soft by default | Progressive disclosure: short SKILL + `references/` checklist S0–S18. Hook only if enforcing recon artifact. |
| `documentation-research.md` (D0–D14) | **Skill** | — | Soft | Workflow when researching third-party/product docs. |
| `research-note.md` | **Skill** | Path-scoped Rule on `docs/research/**` reminding PROTOCOL schema | Soft | Method + claim labels; pairs with claim-citation. |
| `claim-citation.md` | **Skill** (can share folder/references with research-note) | Same path Rule as above | Soft | Activation when emitting/checking cited claims. |
| `agents-md-skeleton.md` | **Skill** | Output lands as root/`nested` **AGENTS.md** (Cursor Rules surface) | Soft | Skill creates/updates; durable form is AGENTS.md / rules, not remaining a skill forever. |
| `adr-minimal.md` | **Skill** | Optional Rule when editing `docs/**/adr*` or `decisions/**` | Soft | After research, record decision. |
| PROTOCOL evidence grades (E0–E4 / U + claim labels) | **Always Apply Rule** (or short AGENTS.md section) | Cite from research skills via `@` / references — **not** a standalone skill alone | Soft (context always present) | Needs high availability for any research write-up; skills alone may not fire. |
| Explore-before-edit **enforcement** | **Hook** (`preToolUse` / Write deny until gate) | — | **Hard** | Only if GreyMatter opts into enforcement; not required by Cursor/Claude defaults. |

- `INFERENCE` [E4]: Premises: skills = workflow packages with relevance descriptions [E1]; rules = always/intelligent prompt inject [E1]; long checklists benefit from progressive disclosure [E1 skills]; PROTOCOL grades must apply even when no skill matched. → Map above.

### 3.5 Proposed skill names + descriptions (no bodies)

agentskills.io / Cursor style: what + when (“Use when…”).

| `name` | `description` (proposed) |
|--------|---------------------------|
| `codebase-reconnaissance` | Run GreyMatter S0–S18 codebase/workspace reconnaissance before implementation or docs changes. Use when exploring an unfamiliar repo, mapping architecture, locating symbols/files, or the user asks to investigate before editing. Prefer context-isolated Explore/search; fill the recon checklist; do not invent APIs. |
| `documentation-research` | Research product or third-party documentation with GreyMatter D0–D14 (official docs, forums/issues, docs↔code checks). Use when verifying API behavior from docs, hunting known limitations, or comparing docs to code. |
| `research-note` | Write an evidence-backed research note using the GreyMatter research-note schema (scope, method, graded findings, gaps, sources). Use when documenting investigation results, secondary research, or any claim-bearing research write-up. |
| `claim-citation` | Format and grade claims per GreyMatter claim-citation + PROTOCOL (FACT/CLAIM/INFERENCE/GAP/OPEN; E0–E4/U; inline citation forms). Use when stating non-trivial facts, citing sources, or auditing unsupported assertions in notes/reports. |
| `agents-md-skeleton` | Draft or update portable `AGENTS.md` (and optional vendor adapters) from the GreyMatter agents-md-skeleton. Use when bootstrapping agent instructions, nesting monorepo guidance, or aligning build/test/do-not commands for coding agents. |
| `adr-minimal` | Record a design decision with the GreyMatter minimal ADR template after research. Use when locking an architecture/process choice, rejecting alternatives, or the user asks for an ADR. |

**Not proposed as skills this pass:** PROTOCOL grades alone (→ Always Rule / AGENTS.md); hard explore gate (→ Hook if chosen).

### 3.6 FAIR4RS / Lamprecht (P2 — fetched)

- `FACT` [E1]: Lamprecht et al. 2020, *Towards FAIR principles for research software*, Data Science 3(1):37–59, DOI 10.3233/DS-190026 — summarizes adapting FAIR to software; notes software differs from data (executability, versioning); interoperability hardest; foundational debate before community FAIR4RS. [E1: Lamprecht et al. 2020 PDF — https://www.pure.ed.ac.uk/ws/files/152466725/Towards_FAIR_principles_LAMPRECHT_DOA14102019_VOR_CC_BY.pdf — accessed 2026-07-27]

- `FACT` [E1]: FAIR4RS Principles v1.0 (RDA / ReSA / FORCE11 WG, 2022) are the community-endorsed principles; cite DOI https://doi.org/10.15497/RDA00068; R1.2-style provenance already used in Theme 2 notes. Lamprecht 2020 is cited in FAIR4RS lineage, not a substitute for v1.0 normative text. [E1: FAIR4RS Principles v1.0 — https://www.rd-alliance.org/system/files/FAIR4RS%20principles%20v1.0.pdf — accessed 2026-07-27]

- `INFERENCE` [E4]: For elevation, FAIR4RS/Lamprecht strengthen **research-note / claim-citation / agents-md provenance** wording (method blocks, who/what/when), not a separate Cursor surface. Prefer FAIR4RS v1.0 for normative R-principles; Lamprecht for historical framing.

## 4. Contradictions / conflicts

1. **Skills vs rules for PROTOCOL grades** — Skills only load when relevant; Always Rule always costs tokens. Conflict resolved here by preferring Always Rule (or AGENTS.md) for grades; skills for workflows.
2. **Explore “automatic when appropriate” vs template “default Explore”** — Not contradictory if “default” means skill *recommendation*, not product mandate. Mandatory remains `OPEN`.
3. **Claude plan mode vs Cursor Explore** — Different mechanisms (permission/plan mode vs built-in Explore subagent); shared pattern is explore/isolate then implement — do not conflate product features in skill text.

## 5. Gaps

- `GAP`: No E0 measurement of how often Cursor Agent actually auto-spawns Explore for GreyMatter-sized tasks (would need session telemetry).
- `GAP`: Hook design for “recon artifact exists” (path, schema, failClosed) not specified — only surface recommendation.
- `OPEN`: Hard explore-before-edit hook — adopt or defer (policy).
- `OPEN`: Mandatory vs recommended Explore (see §3.3).
- `OPEN`: Merge `research-note` + `claim-citation` into one skill vs two (descriptions proposed separately for flexibility).
- `GAP`: Team Rules / enforced org rules as distribution channel for GreyMatter — not evaluated this pass.

## 6. Candidate patterns for templates / elevation (still cited)

1. Elevate **workflows** → Skills with agentskills.io descriptions; put long S0–S18 / D0–D14 in `references/`. [E1: Cursor Skills; agentskills.io]
2. Elevate **always-on research discipline** (evidence grades, claim labels) → Always Apply Rule or AGENTS.md section. [E1: Cursor Rules]
3. Elevate **enforcement** → Hooks only. [E1: Cursor Hooks; Claude best practices]
4. Elevate **broad recon execution** → recommend built-in Explore / Task explore inside skill; do not invent a custom Explore clone unless specialization needed. [E1: Cursor Subagents]
5. Soft-first for T1 explore-before-edit; hard only by explicit product choice. [E4 from §3.2]

## 7. Source list (deduped)

| Source | Grade |
|--------|-------|
| https://cursor.com/docs/skills.md | E1 |
| https://cursor.com/docs/rules.md | E1 |
| https://cursor.com/docs/hooks.md | E1 |
| https://cursor.com/docs/subagents.md | E1 |
| https://code.claude.com/docs/en/best-practices | E1 |
| https://agentskills.io/specification | E1 |
| Lamprecht et al. 2020 PDF (Edinburgh Research Explorer / DOI 10.3233/DS-190026) | E1 |
| FAIR4RS Principles v1.0 PDF (RDA; DOI 10.15497/RDA00068) | E1 |
| `docs/research/PROTOCOL.md` | E0 local authority |
| `docs/research/SECONDARY_PRIORITIES.md` | E0 |
| `docs/research/reports/theme-1-codebase-research-for-agents.md` | E0 / prior synthesis |
| `docs/research/notes/theme-1/t1b-web-agent-workspace-patterns.md` | E0 prior note |
| `docs/research/templates/README.md` | E0 |

---

## Elevation table (summary for integrator)

| Artifact | Elevate to |
|----------|------------|
| codebase-reconnaissance (S0–S18) | Skill `codebase-reconnaissance` + recommend Explore (not mandatory) |
| documentation-research (D0–D14) | Skill `documentation-research` |
| research-note | Skill `research-note` |
| claim-citation | Skill `claim-citation` |
| agents-md-skeleton | Skill `agents-md-skeleton` → writes AGENTS.md |
| adr-minimal | Skill `adr-minimal` |
| PROTOCOL evidence grades | Always Apply Rule / AGENTS.md (not skill-only) |
| explore-before-edit soft | Skill + optional Rule |
| explore-before-edit hard | Hook only (opt-in; OPEN) |

**Output path:** `d:\GreyMatter\docs\research\notes\secondary\sec-elevation-gates-skills.md`

---

## Integrator reconciliation (2026-07-28)

Race: coordinator draft briefly overwrote this note; **subagent body restored** as canonical.

**v1 skill-pack fold (product preference, still E4):** Prefer **five** skills — `codebase-recon`, `docs-research`, `research-protocol` (folds research-note + claim-citation + PROTOCOL refs), `author-agents-md`, `draft-adr` — rather than six separate note/citation skills. PROTOCOL grades stay an **Always/short Rule** as this note recommends. Naming in §3.5 remains valid synonyms.

**FAIR4RS / Lamprecht:** Closed as E1 in §3.6 (not GAP).
