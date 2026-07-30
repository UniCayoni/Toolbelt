---
title: "Theme 6 — Plan pocket (integrated report)"
status: accepted
theme: theme-6-plan
created: 2026-07-29
updated: 2026-07-29
accepted: 2026-07-29
acceptance_scope: method_guidance_t6_plan
accepted_by: human (Jonathan)
authors: [integrator]
depth: deep
stop_reason: low_return_plus_one
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-6-plan/campaign-brief.md
  - docs/research/notes/theme-6-plan/t6-track-synthesis.md
  - docs/research/notes/theme-6-plan/t6-w3-plus1-residual.md
  - docs/research/notes/theme-6-plan/t6-gap-closure-lean.md
  - docs/research/reports/theme-5-design-pocket.md
  - docs/templates/plan-minimal.md
supersedes: null
---

# Theme 6 — Plan pocket (integrated report)

**Status:** **accepted** (method guidance) — 2026-07-29.  
**Acceptance scope:** Plan pocket method guidance + elevation decisions 1–12.  
**Elevated:** skill `implementation-plan` (2026-07-29).  
**§ Durable GAPs** lean-closed in [`t6-gap-closure-lean.md`](../notes/theme-6-plan/t6-gap-closure-lean.md) — no further deep fleet.

**Using `research-protocol`** · integrator merge — grades from gatherer notes; no invented citations.

**Campaign stop:** `low_return_plus_one` (W2 diminishing returns → W3 residual → stop).

**Pocket scope:** everything Toolbelt will own about **planning** (write plans agents can follow; design→task decomposition; 1..N agent execution shape). Not Design re-litigation; not Implement craft; not Superpowers git/TDD/PR law.

### Elevation decisions (accepted 2026-07-29)

| # | Decision |
|---|----------|
| 1 | **Hybrid density** — intent-contract + checkable tasks; binding interfaces/signatures/expected outputs in-plan; **no** mandatory full impl-code dumps |
| 2 | **`serial_implement_review` default** for shared-checkout coding; parallel only when independence + exclusive file ownership (or worktrees) are stated in the plan |
| 3 | **Done-when + runnable command + expected signal** default; GWT optional when behavior is user/story-shaped |
| 4 | **Verify required; TDD ceremony optional** — not Plan grammar |
| 5 | **Plan pocket owns light pre-exec checks (V1–V8)**; full validating-plans / TDD auditor / issue packaging deferred |
| 6 | **Adopt T0–T3 paste guidance** (no invented numeric budgets) |
| 7 | **Durable plans under `docs/plans/`** for non-trivial work; trivial one-file tweaks may stay chat-ephemeral |
| 8 | **Toolbelt mix nesting** — chapters from design sections; tasks = coherent reviewable units (not 2–5 min law); optional story/phase labels |
| 9 | **Status vocab:** `ready` · `in_progress` · `blocked` (`intent-gap` / `verify-fail` / `needs-human`) · `done`; HALT ≡ `blocked`+`intent-gap` |
| 10 | **Skill-only guidance** for “plan before implement when non-trivial” — not a hard always-on rule; intelligent exceptions for trivial diffs |
| 11 | **Accept** this report as Plan method guidance |
| 12 | **Elevated** — skill `implementation-plan` + checklist; template `docs/templates/plan-minimal.md` (active); house `docs/plans/` |
| — | **Superpowers** = structure inventory only; do **not** import git/worktree/TDD/PR as Plan SoT (same stance as Design) |
| — | Gap closes: no numeric paste SoT; markdown field freeze not JSON SoT; optional `[P]`/parallel-safe marker; ignore validating-plans upstream refs; skip BMAD live-example hunt |

**Shipped template:** [`docs/templates/plan-minimal.md`](../templates/plan-minimal.md).

---

## 1. Executive summary

1. **Fresh agents need self-contained plans.** Subagents do not inherit chat; plans (or per-task packets) must carry Goal, Constraints/do-not, files/interfaces, out-of-scope, and runnable verify. [T6A; T6C; W2-RAG]
2. **Design → plan is a gate + decompose stack.** Consume approved Decision / constraints / interfaces / success criteria / section IDs; do not reopen ADR options. Decompose: WBS coverage → vertical INVEST slices → SPIDR when oversized → SMART tasks with files/deps/AC. [T6B; W3 residual; Theme 5]
3. **Compose for 1..N agents as spine + packets.** Controller-readable plan + per-task handoff (objective, I/O, boundaries, path refs). Default shared-checkout coding: **serial implement + review**; parallel only when independence + exclusive writes or worktree isolation. [T6C; W2-EXEC] **Accepted #2.**
4. **Community grammar converges; density decided hybrid.** Superpowers / Spec Kit / OpenSpec / BMAD share constraints, file maps, checkable units, verify/AC, anti-placeholder/halt. Toolbelt: hybrid (accepted #1). Stars = E3 discovery only. [T6D; W2-GAP]
5. **Paste budget stays principle-only (T0–T3).** No numeric quota. [W2-RAG; W3; accepted #6]
6. **Skill elevated:** `implementation-plan` (+ checklist / plan-minimal / `docs/plans/`).

---

## 2. Sources merged

| Wave | Notes |
|------|-------|
| Framing | `campaign-brief.md`, `t6-coordinator-pin.md` |
| W1 | `t6a-w1-…`, `t6b-w1-…`, `t6c-w1-…`, `t6d-w1-…` |
| W2 | `t6-w2-rag-schema-paste-link.md`, `t6-w2-gap-community-templates.md`, `t6-w2-exec-shape-serial-parallel.md` |
| W3 / +1 | `t6-w3-plus1-residual.md` (`stop_reason: low_return_plus_one`) |
| Synth | `t6-track-synthesis.md` (+ §4.8 residual addendum) |
| Gap close | `t6-gap-closure-lean.md` (`stop_reason: no_further_research_needed`) |

Subagents: `cursor-grok-4.5-high-fast`. Corpora: Alexandria `ai_llm_agents` + `software_engineering` (W2; diminishing returns; trading/path-planning false friends rejected).

---

## 3. Multi-source FACT cluster

| # | Claim (compressed) | Tracks |
|---|-------------------|--------|
| 1 | Fresh subagents = clean context; parent/plan must brief | T6A, T6C, W2-RAG |
| 2 | Goal + Context/files + Constraints + Done-when/verify | T6A, W2-RAG, T6D |
| 3 | Name files/interfaces; out-of-scope; checkable verify | T6A, T6C, T6D |
| 4 | Design/ADR = what/why; Plan = sequenced checkable work | T6B, T6D, brief |
| 5 | WBS → vertical → SPIDR → SMART/AC | T6B, W2-RAG |
| 6 | Parallel research OK; unconstrained parallel coding weaker | T6C, W2-EXEC |
| 7 | Parallel writers need exclusive files and/or worktrees | W2-EXEC, T6C |
| 8 | Review/verify gates are first-class | T6A/C, W2-EXEC, T6D |
| 9 | Community plan cluster shares grammar atoms (stars≠SoT) | T6D, W2-GAP |
| 10 | No E1 numeric paste budget; no portable schema SoT | T6A, W2-RAG, W3 |

Full citations live in gatherer notes + `t6-track-synthesis.md` §4.2 / §4.7.

---

## 4. Design → plan handoff

**Consume:** approved section IDs; Decision (restate or path+§); Constraints/NFRs; success criteria → Done-when; interfaces/contracts; sub-design boundaries as plan chapters; design/ADR paths as T1 locators. [W3 §4.3]

**Do not consume as law:** unresolved options matrices; draft/proposed Design; inventing gaps instead of `blocked`+`intent-gap`. [`draft-is-not-sot`; accepted #9]

**Decompose method:** design sections → WBS parents (100% coverage of approved scope) → vertical INVEST slices → Cohn SPIDR (incl. Spike) when oversized/unknown → Wake SMART tasks with file map, deps, acceptance. [T6B]

---

## 5. Plan method spine (accepted guidance)

| # | Section | Intent |
|---|---------|--------|
| 0 | Preconditions | Approved design/ADR linked; no option reopen |
| 1 | Plan header | Goal; decided stack; Always·Block If·Never; out-of-scope |
| 2 | Coverage map | design-section / FR → work packages (100%) |
| 3 | File / Code Map | Paths + exclusive-write ownership for any parallel tranche |
| 4 | Scaling shape | Simple flat SMART; complex → chapter per sub-design |
| 5 | Task units | Files; Interfaces; deps; Done-when + verify command + expected signal; GWT optional; no TBD; no mandatory code dumps |
| 6 | Execution spine | `serial_implement_review` default; optional parallel-safe; review gates; escalate via status vocab |
| 7 | Handoff packets | Spine + per-task packet for fresh contexts |
| 8 | Paste/link | T0–T3 (accepted #6) |
| 9 | Self-review / validate | V1–V8 light Plan checks (accepted #5) |
| 10 | Non-imports | No mandatory TDD/git/worktree/PR as Plan grammar |

House path: `docs/plans/YYYY-MM-DD-<slug>-plan.md` (non-trivial). Template: `docs/templates/plan-minimal.md` (active).

---

## 6. Conflicts resolved / remaining

| Topic | Resolution |
|-------|------------|
| Plan body density | **Accepted hybrid** (#1) |
| Serial vs parallel | **Accepted scoped default** (#2) |
| TDD-in-plan | **Accepted optional** (#4) |
| validating-plans home | **Accepted Plan owns V1–V8 light** (#5); upstream skill ignored |
| Paste tiers | **Accepted T0–T3** (#6) |
| Plan retention | **Accepted durable `docs/plans/`** (#7) |
| Nesting / status vocab | **Accepted Toolbelt mix + thin status** (#8–9) |
| Hard “always plan” rule | **Accepted skill-only guidance** (#10) |

---

## 7. Community inventory (E3 discovery → E1 structure)

| Rank | System | Plan-writing signal |
|------|--------|---------------------|
| 1 | obra/superpowers `writing-plans` | Densest zero-context plan skill |
| 2 | github/spec-kit plan + tasks | Tech plan vs story-phased tasks; `[P]` / `[USn]`; tests optional |
| 3 | Fission-AI/OpenSpec | proposal→specs→design→tasks |
| 4 | BMAD-METHOD | epics/stories + build-auto Always/Block If/Never + HALT |
| 5 | validating-plans (registry) | Plan QA companion; deep refs GAP — **ignored for SoT** |

Shared atoms retained; Superpowers execution/git/TDD packaging **not** Plan SoT.

---

## 8. Elevation status

| Candidate | Type | Status |
|-----------|------|--------|
| `implementation-plan` | skill | **Shipped** |
| Plan checklist | `skills/implementation-plan/references/` | **Shipped** |
| `plan-minimal` template | `docs/templates/plan-minimal.md` | **Active** |
| Intent-contract fragment | in template | Included (Always/Block If/Never) |
| Thin always-plan rule | rule | **Not elevated** (skill-only #10) |
| Plan-adjacent validate (V1–V8) | in skill/checklist | **Shipped** (light) |
| Entry-flow compose skill | skill | Later |

---

## 9. Durable GAPs — lean-closed

| Former GAP | Close |
|------------|-------|
| Numeric paste budget | T0–T3 only; no fake numbers |
| Portable JSON schema SoT | Markdown field freeze in gap-closure + plan-minimal; JSON later if needed |
| Vendor `[P]` token | Optional `parallel-safe` / `[P]` when #2 criteria met |
| validating-plans refs 404 | Ignore upstream; keep V1–V8 |
| Live BMAD epics examples | Skip |

Optional future: E0 trial measuring paste tiers on a real change — not required for #12.

---

## 10. Highest-value E1 shortlist

Anthropic: context engineering; building effective agents; multi-agent research; Agent Skills progressive disclosure.  
Claude Code: best practices; sub-agents; agent teams.  
Cursor: subagents; plan mode; multi-agent independent steps.  
OpenAI Codex: Goal/Context/Constraints/Done-when.  
SE method: Wake INVEST/SMART; Cohn SPIDR; Nygard ADR.  
GitHub structure: Superpowers writing-plans; Spec Kit templates; BMAD build-auto; OpenSpec schema.

Paths/URLs: `t6-track-synthesis.md` §4.7.

---

## 11. Acceptance checklist

- [x] Accept this report as Plan **method guidance**
- [x] Decide P0 density + serial default + verify grammar + TDD-in-plan
- [x] Decide paste T0–T3; Plan owns V1–V8; plan file house path
- [x] Gap triage: no further deep research needed
- [x] Elevate via `author-cursor-surfaces` — skill `implementation-plan` shipped
