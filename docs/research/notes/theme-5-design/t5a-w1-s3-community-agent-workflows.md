---
title: "T5A-W1-S3 — Community agent workflows (Superpowers + AgDR)"
status: draft
theme: theme-5-design
track: T5A
wave: 1
slice: T5A-S3
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-t5a-s3]
supersedes: null
---

# T5A-W1-S3 — Community agent workflows (structure inventory)

## 1. Scope

- Question / goal: What structured steps do high-signal community agent workflows use for design-before-code (brainstorm → options/tradeoffs → approval → plan), and what is Agent Decision Record (AgDR) structure?
- In scope: Structure inventory of Superpowers `brainstorming` + `writing-plans` (local skill files); AgDR (repo SPEC/template + blog); optional AATF-style decision-audit specs if fetched — all as discovery / comparison material.
- Out of scope: Treating Superpowers or AgDR as Toolbelt Design SoT; merging Superpowers git/PR/worktree/commit policies into Toolbelt recommendations; re-litigating ADR/MADR FACTS (owned by T5A-S1); locking product process from E3 alone.
- Comprehension / research goal type (if code): other (community process inventory)

**Hard framing:** This note is **structure inventory only** — not product law. `draft` ≠ accepted Design SoT.

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Read (local Superpowers skills); WebFetch (AgDR README/SPEC/template/decide command, me2resh blog, AATF SPEC); WebSearch (AATF discovery); Glob (skill paths) |
| Corpora / URLs searched | Local: Superpowers skill paths below. Remote: https://github.com/me2resh/agent-decision-record ; https://raw.githubusercontent.com/me2resh/agent-decision-record/main/README.md ; https://raw.githubusercontent.com/me2resh/agent-decision-record/main/SPEC.md ; https://raw.githubusercontent.com/me2resh/agent-decision-record/main/agdr-template.md ; https://raw.githubusercontent.com/me2resh/agent-decision-record/main/commands/decide.md ; https://me2resh.com/blog/agent-decision-records ; https://raw.githubusercontent.com/wdh107/agent-audit-trail/main/SPEC.md ; https://github.com/wdh107/agent-audit-trail |
| Queries (exact) | Glob `**/superpowers/**/skills/brainstorming/SKILL.md`; Glob `**/superpowers/**/skills/writing-plans/SKILL.md`; WebSearch `AATF agent audit trail framework specification agent decisions` |
| What was *not* searched | Alexandria corpora; Theme 2 ADR primaries (S1); Cursor Plan Mode vendor docs (W3); Superpowers upstream git history / marketplace popularity metrics; ApexYard; IETF draft-sharif full normative merge (discovered via search only — not treated as AgDR sibling SoT); other agent workflow repos beyond named inventory |
| Depth | deep |
| Waves / stop_reason | wave: 1; slice: T5A-S3; stop_reason: slice inventory complete for named MUST sources + optional AATF fetch; residual community workflows deferred to W2/W3 if integrator opens them |
| Provenance (optional PROV) | Entity←local Superpowers cache + AgDR/AATF remote docs; Activity=T5A-S3 gather; Agent=cursor-grok gatherer |

**Using `research-protocol`; depth: deep; wave: 1; slice: T5A-S3.**

### Exact local paths observed

| Skill | Path |
|-------|------|
| brainstorming | `C:\Users\Jonyc\.cursor\plugins\cache\cursor-public\superpowers\d884ae04edebef577e82ff7c4e143debd0bbec99\skills\brainstorming\SKILL.md` |
| writing-plans | `C:\Users\Jonyc\.cursor\plugins\cache\cursor-public\superpowers\d884ae04edebef577e82ff7c4e143debd0bbec99\skills\writing-plans\SKILL.md` |

Cache commit dir: `d884ae04edebef577e82ff7c4e143debd0bbec99` (observed via path; not independently verified as upstream SHA meaning).

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Slice is a named community inventory, not workspace recon |
| Scope boundary | Named Superpowers skills + AgDR primary URLs + optional AATF SPEC only |

## 4. Findings

### 4.1 Superpowers `brainstorming` — design-before-code steps

- `FACT` [E0] Local skill file exists at the path above; YAML name `brainstorming`; description requires use before creative/implementation work. [E0: local path — accessed 2026-07-29]
- `CLAIM` [E3] Same content is a community Cursor plugin skill (Superpowers), not Toolbelt protocol. Grade E3 for community status; do not lock Design law from it alone. Premises for dual grade: (1) E0 file contents observed; (2) plugin cache under `cursor-public/superpowers`. [E3: Superpowers community plugin — local cache observation]
- `FACT` [E0] Hard gate: do not invoke implementation skills, write code, scaffold, or take implementation action until a design is presented and the user has approved it. [E0: brainstorming/SKILL.md HARD-GATE — accessed 2026-07-29]
- `FACT` [E0] Ordered checklist (must complete in order): (1) Explore project context; (2) Offer visual companion just-in-time (not upfront); (3) Ask clarifying questions (one at a time); (4) Propose 2–3 approaches with trade-offs and a recommendation; (5) Present design in sections, get approval after each section; (6) Write design doc to `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md` and commit; (7) Spec self-review; (8) User reviews written spec; (9) Transition by invoking `writing-plans`. [E0: brainstorming/SKILL.md Checklist — accessed 2026-07-29]
- `FACT` [E0] Process flow terminal state is invoking `writing-plans` only — not other implementation skills. [E0: brainstorming/SKILL.md Process Flow / After the Design — accessed 2026-07-29]
- `FACT` [E0] Approaches step explicitly requires 2–3 approaches with trade-offs; lead with recommended option and why. [E0: brainstorming/SKILL.md Exploring approaches — accessed 2026-07-29]
- `FACT` [E0] Dual approval gates: conversational section approval, then written-spec review gate before plans. [E0: brainstorming/SKILL.md Presenting the design + User Review Gate — accessed 2026-07-29]
- `FACT` [E0] Spec self-review checks: placeholder scan, internal consistency, scope check, ambiguity check. [E0: brainstorming/SKILL.md Spec Self-Review — accessed 2026-07-29]
- `OPEN` Superpowers visual companion (`skills/brainstorming/visual-companion.md`) referenced but not read in this slice. Follow-up: only if visual HITL structure becomes a residual GAP.

**Inventory map (structure only — not Toolbelt recommendation):**

```text
context → clarify (1Q/msg) → 2–3 options+tradeoffs → sectional design approval
  → write spec → self-review → user spec approval → writing-plans
```

### 4.2 Superpowers `writing-plans` — plan structure after approval

- `FACT` [E0] Local skill file exists at the path above; description: use when you have a spec/requirements for a multi-step task, before touching code. [E0: writing-plans/SKILL.md — accessed 2026-07-29]
- `CLAIM` [E3] Community skill status same dual-grade framing as brainstorming. [E3: Superpowers community plugin]
- `FACT` [E0] Save plans to `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md` (user prefs may override). [E0: writing-plans/SKILL.md — accessed 2026-07-29]
- `FACT` [E0] Required plan header fields: Feature title; agentic-worker note pointing to `subagent-driven-development` or `executing-plans`; Goal; Architecture; Tech Stack; Global Constraints. [E0: writing-plans/SKILL.md Plan Document Header — accessed 2026-07-29]
- `FACT` [E0] Before tasks: map files to create/modify and responsibilities (decomposition lock-in). [E0: writing-plans/SKILL.md File Structure — accessed 2026-07-29]
- `FACT` [E0] Task structure includes Files (Create/Modify/Test paths), Interfaces (Consumes/Produces), then checkbox steps typically: failing test → run fail → minimal impl → run pass → commit. [E0: writing-plans/SKILL.md Task Structure — accessed 2026-07-29]
- `FACT` [E0] Self-review after plan: spec coverage, placeholder scan, type consistency. [E0: writing-plans/SKILL.md Self-Review — accessed 2026-07-29]
- `FACT` [E0] Execution handoff offers Subagent-Driven vs Inline Execution — **inventory only**; not imported as Toolbelt git/PR/worktree policy. [E0: writing-plans/SKILL.md Execution Handoff — accessed 2026-07-29]
- `GAP` This slice does **not** extract or recommend Superpowers commit cadence, worktree creation (`using-git-worktrees`), or PR policies. Searched: named skill bodies only. Result: those policies appear as adjacent skill references; deliberately omitted from Toolbelt implications per hard rules.

### 4.3 AgDR — structure (Y-statement, options table, metadata, triggers)

- `FACT` [E3] AgDR is presented as a Markdown decision-record format for AI-assisted development, with normative `SPEC.md`, templates, JSON Schema, and validator. [E3: me2resh/agent-decision-record README — https://raw.githubusercontent.com/me2resh/agent-decision-record/main/README.md — accessed 2026-07-29]
- `FACT` [E3] File location/naming (normative): `docs/agdr/AgDR-{NNNN}-{slug}.md`; `id` must match `AgDR-{NNNN}` prefix. [E3: SPEC.md §1 — https://raw.githubusercontent.com/me2resh/agent-decision-record/main/SPEC.md — accessed 2026-07-29]
- `FACT` [E3] Required frontmatter fields: `id`, `timestamp` (ISO-8601 with time/tz), `agent`, `model`, `trigger`, `status`. Optional/SHOULD: `session`. Optional/MAY: `supersedes`. [E3: SPEC.md §2 — accessed 2026-07-29]
- `FACT` [E3] `trigger` enum (SPEC): `user-prompt` \| `hook` \| `automation` \| `self-initiated`. [E3: SPEC.md §3 — accessed 2026-07-29]
- `FACT` [E3] `status` enum (SPEC): `proposed` \| `executed` \| `superseded` \| `deprecated`. [E3: SPEC.md §4 — accessed 2026-07-29]
- `FACT` [E3] Y-statement (required blockquote under title): “In the context of **{situation}**, facing **{concern}**, I decided **{decision}** to achieve **{goal}**, accepting **{tradeoff}**.” Every clause must be specific. [E3: SPEC.md §5–§6; blog https://me2resh.com/blog/agent-decision-records — accessed 2026-07-29]
- `FACT` [E3] Required body: title; Y-statement; `## Options Considered` table (≥2 real options with Pros/Cons); `## Decision` with chosen option + specific `because` justification. [E3: SPEC.md §5 — accessed 2026-07-29]
- `FACT` [E3] SHOULD sections when substantive: `## Context`, `## Consequences`, `## Artifacts`. Full vs short templates exist. [E3: SPEC.md §5; agdr-template.md — https://raw.githubusercontent.com/me2resh/agent-decision-record/main/agdr-template.md — accessed 2026-07-29]
- `FACT` [E3] Create-when triggers (situations): compares options; chooses a library; selects a pattern; architecture choice; picks a convention. Don’t create for trivial naming/formatting, following existing convention, or obvious bugfix. [E3: SPEC.md §7; README “When to Create an AgDR” — accessed 2026-07-29]
- `FACT` [E3] Integration inventory (structure only): `/decide` command/skill flow; Cursor MDC rule; Copilot/Windsurf/system prompts; pre-commit warning when architecture-ish files change without AgDR. [E3: README Tools & Integrations; blog “How to Integrate”; commands/decide.md — accessed 2026-07-29]
- `FACT` [E3] Blog positions AgDR as extending ADR for agent workflows (agent metadata, Y-statement, options table, mid-session template). [E3: https://me2resh.com/blog/agent-decision-records — accessed 2026-07-29]
- `CLAIM` [E3] Blog/README claim AgDR “extends” / differs from ADR (author=agent, real-time, required metadata, hook enforcement). Not Toolbelt ADR law; S1 owns ADR FACTS. [E3: README “Key Differences from ADR”; blog — accessed 2026-07-29]
- `INFERENCE` [E4] AgDR’s options table + Decision/Consequences structurally resemble common ADR “alternatives / decision / consequences” sections, with added agent provenance fields and Y-statement. Premises: (1) AgDR SPEC required Options/Decision (+ SHOULD Consequences) [E3 SPEC §5]; (2) AgDR README credits Nygard ADR / MADR / joelparkerhenderson ADR as inspiration [E3 README Credits]; (3) exact ADR field FACTS deferred to T5A-S1. Do not treat this as ADR FACT.

### 4.4 Optional: AATF / agent-audit-trail (fetched — do not lock)

- `FACT` [E3] Fetched AATF SPEC v0.1.0 Draft (2026-06-16) from `wdh107/agent-audit-trail`: JSON Trace → Steps; `reasoning` steps require Decision Record with `input_summary`, `decision`, `reasoning`, `confidence`, required `alternatives_considered[]`, optional assumptions/constraints; hash-chain tamper evidence; step types include `human_input` and `guardrail`. [E3: https://raw.githubusercontent.com/wdh107/agent-audit-trail/main/SPEC.md — accessed 2026-07-29]
- `CLAIM` [E3] AATF targets runtime agent execution audit (JSON, confidence, hash chain), not the same artifact as human-readable Markdown AgDR / design-spec workflow. Discovery only — **do not lock** Toolbelt Design process on AATF. [E3: AATF SPEC Purpose/Scope — accessed 2026-07-29]
- `GAP` IETF `draft-sharif-agent-audit-trail-00` appeared in search results as a separate “Agent Audit Trail” logging draft; not fetched/normalized in this slice beyond discovery. Searched: WebSearch hit. Result: name collision risk with AATF; leave OPEN if needed.

### 4.5 Cross-pattern (inventory synthesis — not law)

- `INFERENCE` [E4] Shared structural pattern across inventoried sources for design-or-decision visibility: **elicit context → enumerate alternatives with tradeoffs → choose with justification → (optional) human gate → record artifact**. Premises: (1) Superpowers checklist steps 1–9 [E0]; (2) AgDR Options/Decision/Y-statement [E3]; (3) AATF Decision + alternatives_considered [E3]. Not a universal SoT.
- `INFERENCE` [E4] Superpowers emphasizes **HITL approval before plan/code**; AgDR emphasizes **decision capture at choice time** (may be mid-implementation); AATF emphasizes **execution-trace audit**. Premises: (1) Superpowers HARD-GATE + dual approval [E0]; (2) AgDR timing “as decisions are made” [E3 README]; (3) AATF Trace/Steps model [E3]. Different jobs — do not merge into one Toolbelt skill blindly.

## 5. Hypothesis log (optional but recommended for code)

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | High-signal community agent design workflows share options→approval→plan scaffolding | revised | Confirmed as **inventory pattern** (E4), not as Toolbelt law |
| H2 | AgDR is a drop-in ADR replacement for Toolbelt | rejected | AgDR is E3 community format; ADR FACTS owned by S1; AgDR adds agent metadata / Y-statement / mid-session triggers |
| H3 | AATF and AgDR are interchangeable | rejected | Different media (JSON runtime trail vs Markdown decision doc) and goals (audit chain vs design decision record) |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| AgDR `trigger` / `status` enums | Blog template snippet: `trigger: user-prompt \| hook \| automation`; `status: proposed \| executed \| superseded` [E3 blog] | SPEC.md: adds `self-initiated`; `status` adds `deprecated` [E3 SPEC §§3–4] | Prefer **SPEC.md** as normative for AgDR structure inventory; note blog/template lag |
| AgDR short template `trigger` placeholder | agdr-template.md short form omits listing `self-initiated` in places | SPEC enum includes `self-initiated` | Prefer SPEC |
| Campaign brief W2 vs pin W1 for Superpowers/AgDR | campaign-brief deep cover lists Superpowers/AgDR under W2 | coordinator pin + this task assign S3 community inventory in W1 | Follow **explicit slice task** (this note); no conflict on evidence content |

## 7. Gaps & OPEN

- `GAP` Adoption / effectiveness evidence for AgDR or Superpowers design gates (beyond author blog claims). Searched: AgDR README “Results From Production Use” (anecdotal E3). Result: no independent E1/E2 corroboration in this slice.
- `GAP` Whether Toolbelt should adopt Y-statement, AgDR frontmatter, or Superpowers dual-approval — deliberately out of scope; needs integrator + human accept after S1/S2.
- `GAP` Superpowers visual companion structure unread.
- `OPEN` Corroborate AgDR vs ADR field overlap with T5A-S1 FACTS (do not invent ADR sections here).
- `OPEN` If W2 needs more community workflows (e.g. other decide skills), run residual gather — stop rule applies at track level.
- `OPEN` IETF draft-sharif vs AATF naming/relationship if audit-trail track expands.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] For T5A spine design, community inventory suggests separating (a) **process gates** (clarify → options → approve → plan) from (b) **decision records** (options table + justification + provenance) from (c) **runtime audit trails** (confidence/hash). Premises: §4.5 inferences.
- `INFERENCE` [E4] Any future Toolbelt Design surface that cites Superpowers should import **step topology only**, not Superpowers paths (`docs/superpowers/...`), commit steps, worktree, or execution-handoff skills. Premises: hard rules for this slice; writing-plans Execution Handoff [E0] deliberately excluded from recommendations.
- `INFERENCE` [E4] AgDR is a candidate **E3 pattern library** for agent-authored decision docs; acceptance would require Protocol-grade corroboration and alignment with S1 ADR/MADR FACTS — not this note.

## 9. Source list (deduped)

1. Superpowers `brainstorming` SKILL.md — `C:\Users\Jonyc\.cursor\plugins\cache\cursor-public\superpowers\d884ae04edebef577e82ff7c4e143debd0bbec99\skills\brainstorming\SKILL.md` (E0 local; E3 community) — accessed 2026-07-29
2. Superpowers `writing-plans` SKILL.md — `C:\Users\Jonyc\.cursor\plugins\cache\cursor-public\superpowers\d884ae04edebef577e82ff7c4e143debd0bbec99\skills\writing-plans\SKILL.md` (E0 local; E3 community) — accessed 2026-07-29
3. me2resh/agent-decision-record README — https://raw.githubusercontent.com/me2resh/agent-decision-record/main/README.md — accessed 2026-07-29
4. AgDR SPEC.md — https://raw.githubusercontent.com/me2resh/agent-decision-record/main/SPEC.md — accessed 2026-07-29
5. AgDR agdr-template.md — https://raw.githubusercontent.com/me2resh/agent-decision-record/main/agdr-template.md — accessed 2026-07-29
6. AgDR commands/decide.md — https://raw.githubusercontent.com/me2resh/agent-decision-record/main/commands/decide.md — accessed 2026-07-29
7. Me2resh blog “Agent Decision Records” — https://me2resh.com/blog/agent-decision-records — accessed 2026-07-29
8. AATF SPEC.md v0.1.0 Draft — https://raw.githubusercontent.com/wdh107/agent-audit-trail/main/SPEC.md — accessed 2026-07-29
9. T5A coordinator pin — `docs/research/notes/theme-5-design/t5a-coordinator-pin.md` (slice assignment context only)
10. Theme 5 campaign brief — `docs/research/notes/theme-5-design/campaign-brief.md` (track framing; draft)
