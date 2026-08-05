---
title: "Theme 24 — Wave 1 integrator synthesis v2 (quality-first)"
status: accepted
theme: theme-24-author-learning
created: 2026-08-05
updated: 2026-08-05
accepted: 2026-08-05
accepted_by: human (Jonathan)
depth: deep
authors: [integrator-v2]
stop_reason: diminishing_returns_plus_2
supersedes: docs/research/notes/theme-24-author-learning/w1-integrator-synthesis.md
aligned_with:
  - docs/research/notes/theme-24-author-learning/campaign-brief.md
  - docs/research/notes/theme-24-author-learning/deep-campaign-board.md
  - docs/research/notes/theme-24-author-learning/t24c-e0-host-author-surfaces.md
  - docs/research/notes/theme-24-author-learning/t24d-cursor-affordances.md
  - docs/research/notes/theme-24-author-learning/t24f-rag-standard-quality.md
  - docs/research/notes/theme-24-author-learning/t24f-web-guideline-quality.md
  - docs/research/notes/theme-24-author-learning/t24g-rag-continual-learning.md
  - docs/research/notes/theme-24-author-learning/t24g-web-continual-learning.md
  - docs/research/notes/theme-24-author-learning/t24g-github-learning-loops.md
  - docs/PROTOCOL.md
---

# Theme 24 — Wave 1 integrator synthesis v2

**Using `research-protocol`**. Depth: **deep**. Merge of W1 notes **re-weighed** for Toolbelt ideals. **Draft ≠ law.**

**Toolbelt weigh order (this pass):** intent of the surface → evidence quality → draft≠SoT / human accept as last gate → anti-ceremony as *discipline* (skip when no evidence). **Ease is a side effect, never the deciding factor.**

v1 (`w1-integrator-synthesis.md`) is **denied for elevate lean** — kept for audit. W2 gatherer fleets still **skipped** (`diminishing_returns_plus_2`); this is a second **integrator** pass, not new primary search.

---

## 1. Did W1 gatherer tracks follow that train of thought?

Honest meta-audit of *how* notes were gathered / what they emphasized — not a rewrite of their FACTs.

| Track | Aligned with quality-first? | Drift / note |
|-------|----------------------------|--------------|
| **T24F-RAG / T24F-web** | **Strong** | Asked what makes guidelines *good*; keep/reject signals; checkability; Google change process. Primary feedstock for Toolbelt lean. |
| **T24C-E0** | **Strong on fences** | Correctly mapped derive→proposed→accept, no auto-promote. Mild drift: implications labeled skill as “router/harvester” (ease/compose framing) without centering the quality gate as the job. |
| **T24D-docs** | **Mostly strong** | Explicit Skills + refuse Memories/alwaysApply/stop auto-write = control for quality. “Soft nudge” hook language can be read as UX ease — reframe as evidence-warranted prompt only. |
| **T24G-RAG** | **Strong** | Propose→validate→HITL→embed; documentation as organizational memory; automation amplifies, does not replace judgment. |
| **T24G-web** | **Mixed → usable** | Correctly separated human-gated SRE/SASE from auto-promote agent papers. Risk if integrator copies paper *convenience* loops; v1 under-weighted validate-before-promote. |
| **T24G-gh** | **Mixed — comparator ease bias** | Correct stage/proposed pattern. Over-salient Apply/Skip / act-by-default (divad12) as UX shapes. Quality bars present but quieter: SkillOpt held-out gate, MeowKit frequency≥3, OneResearchClaw regression — **v2 elevates these over click-to-accept UX**. |

`INFERENCE` [E4] W1 **evidence** is usable; v1 **lean packaging** drifted toward comparator ease (router + soft closeout + human click as main quality). Premises: §1 table; v1 role/triggers wording; T24G-gh frequency/held-out FACTs underused in v1.

---

## 2. Wave 1 status (unchanged facts)

Same seven notes as v1; W2 fleets still skipped. Retained GAPs unchanged (EBSE thin; IDE Memories; ISO paywall; closeout harvest hook absent until elevate).

---

## 3. Convergent lean v2 (proposed for human)

### Intent (must lead)

`author-learning` exists so a **host workspace** only keeps learnings that survive **Toolbelt-grade evidence and guideline-quality tests**, then become **proposed** feedstock for existing author paths. Human accept is the **last** gate, not the **only** gate. It does **not** exist to make updating skills/standards *easier*; any ease is a side effect of a clean method.

### Surface

| Piece | Lean v2 |
|-------|---------|
| Skill id | **`author-learning`** (author-* pocket) |
| Role | **Quality-gated harvest** — score/filter candidates; **refuse or park** weak ones; emit **proposed** deltas; then **compose** into `author-standards` / `author-agents-md` / `author-cursor-surfaces` (host) / `research-draft-adr`. Not a convenience router; not a new law body. |
| Invocation | Explicit `/` (`disable-model-invocation: true`) — runs when asked or when an evidence-warranted handoff fires; **not** ambient “learning mode” |
| Target | Host/workspace skills + standards/principles/AGENTS — **not** Toolbelt plugin `skills/*` |
| Hard fence | Never auto-accept; draft≠SoT; cite-or-omit; no vibes-as-proposal |

### Loop shape (quality order)

```text
evidence-warranted trigger
  → harvest with locators
  → quality + evidence floor (refuse/park failures HERE)
  → stage only qualified proposals (status: proposed)
  → human accept/reject
  → author-* writes durable host surfaces
```

Comparators **for gates**, not UX fashion: Albada propose→validate→HITL→embed; SRE reviewed actions; SASE coach-approve; SkillOpt held-out / stage-adopt; MeowKit frequency; OneResearchClaw regression + `proposed/`. Apply/Skip UIs are optional presentation — **not** the quality model. Agent memory papers = candidate factories only.

### Triggers (T24A) — evidence-warranted, not soft

| When | Quality framing |
|------|-----------------|
| Explicit `/author-learning` | Human asserts intent to harvest |
| After non-trivial closeout **and** citable friction/lessons exist | Skip when verdict has nothing durable to cite — anti-ceremony as **discipline**, not “don’t bother the user” |
| Other loop ends only if evidence floor is already met | Design at elevate; never always-on |

**Out:** always-on harvest; stop-followup SoT rewrite; “soft” prompts with empty evidence.

### Candidate atoms (T24B) — floor before propose

| Field | Required? | Why |
|-------|-----------|-----|
| Recurring pain / problem | **Yes** | Pattern/guideline quality (T24F) |
| Evidence + locator + label/grade | **Yes** | PROTOCOL; **U / no locator → do not propose** |
| Proposed change type | Yes | principles \| standards \| host-skill \| AGENTS pointer \| ADR |
| Target host path | Yes | Workspace-bound |
| Checkability / strength (DO vs CONSIDER) | Yes for standards/skills that claim rules | T24F |
| Trade-offs + conflict with existing catalog | Yes when catalog/modules exist | Google change process |
| Corroboration / recurrence signal | Prefer; park if single anecdote without strong E0 | MeowKit-style frequency / “pulls weight” — exact N **OPEN** at elevate, direction = quality |
| Status | `proposed` until human | draft≠SoT |

### Quality keep / reject (T24F) — skill’s primary work

**Keep (must earn propose):** goal-tied; pulls weight (not “minimal for ease”); reader-clear; consistent; non-surprising; enforceable or strength-labeled; this/not-that; patterns need problem + consequences; migration note if conflicts.

**Refuse / park (do not hand human a fake choice):** pattern name only; wrong-place complexity; vague success criteria; vibes; auto-accept implication; uncited; conflicts catalog with no migration story.

### Cursor affordances (T24D) — control, not convenience

| Prefer | Avoid |
|--------|--------|
| Explicit host Skill; scaffolds **after** accept | `alwaysApply` learnings dump |
| Thin AGENTS / fence pointers | Memories as standards SoT |
| Hook only if it captures **candidates** or asks when evidence exists | Unconditional followup SoT rewrite; “nudge” without evidence |

### Elevate package (when v2 lean accepted)

1. `skills/author-learning/` + template: **quality gate checklist first**, then candidate schema, then author-* handoffs  
2. Closeout: handoff **only when** harvestable cited friction — not a default soft prompt  
3. Packs / README / CHANGELOG / guide-meta  
4. Smokes: refuse uncited/U; refuse auto-accept; host-path only; quality park path  
5. Sync; human review before commit  

### Explicit outs

- Elevate from v1 lean  
- Auto-accept / act-by-default as Toolbelt law  
- Skill identity = “make standards updates easy”  
- Toolbelt plugin self-modify; playbook rewrite; CI; Brain  
- Locking undocumented Memories / AGENTS precedence  

---

## 4. Human gate

```text
Accept Wave 1 stop + author-learning elevate lean v2?
  intent: quality-gated harvest (ease side-effect only)
  skill: author-learning — filter then propose then author-* compose
  floor: evidence+locator required; U/no locator → no propose
  trigger: explicit + evidence-warranted closeout; no always-on
  out: v1 router/soft framing; auto-accept; plugin self-modify; Memories-as-law
```

**Accepted** 2026-08-05 — elevated; see `docs/research/reports/theme-24-author-learning.md`.
