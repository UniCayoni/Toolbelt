---
title: "Theme 5 — Design pocket (integrated report)"
status: accepted
theme: theme-5-design
created: 2026-07-29
updated: 2026-07-29
accepted: 2026-07-29
acceptance_scope: method_guidance_t5a_t5b_t5d
accepted_by: human (Jonathan)
authors: [integrator]
depth: deep
stop_reason: tracks_complete_t5a_t5b_t5d
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/research/notes/theme-5-design/t5a-track-synthesis.md
  - docs/research/notes/theme-5-design/t5b-track-synthesis.md
  - docs/research/notes/theme-5-design/t5d-track-synthesis.md
  - docs/research/notes/theme-5-design/t5c-ux-placeholder.md
supersedes: null
---

# Theme 5 — Design pocket (integrated report)

**Status:** **accepted** (method guidance) — 2026-07-29.  
**Acceptance scope:** T5A + T5B + T5D as Design method guidance / elevation authority.  
**Deferred (non-acceptance):** T5C UX/UI — [`t5c-ux-placeholder.md`](../notes/theme-5-design/t5c-ux-placeholder.md).  
**§7–§8 GAP/OPEN** remain non-locks unless closed later.

**Active tracks merged:** T5A, T5B, T5D (each `stop_reason: low_return_plus_one`).

**Using `research-protocol`** · integrator merge only — no new facts.

### Elevation decisions (accepted 2026-07-29)

| # | Decision |
|---|----------|
| 1 | Accept all of T5A+T5B+T5D as method guidance |
| 2 | Elevate: design-process, design-technical, creative skills (split), draft≠accepted rule; **no UX skill** |
| 3 | Creative **split**: systems / narrative / world-character |
| 4 | ADR house: `docs/adr/NNNN-slug.md`; status `proposed\|accepted\|deprecated\|superseded`; require **Considered Options** (+ pros/cons) before Decision |
| 5 | Toolbelt Design skills **do not reference Superpowers**; Toolbelt process spine stands alone |
| — | UX skipped until T5C readiness gate |

---

## 1. Executive summary

1. **Design is multi-type.** Technical architecture, creative systems, and (later) UX must not share one mega-skill. [campaign brief; track syntheses]
2. **Shared spine (T5A):** criteria → options/tradeoffs → critique → **human decide** → record (ADR/MADR) → HITL before implement. Keep lanes: human methods / agent orchestration / decision capture. [T5A]
3. **Technical design (T5B):** Dependency Rule + modularity principles; ADR on architectural significance; monolith vs microservices both sides; clean/standards contested as constraints not SoT. [T5B]
4. **Creative design (T5D):** Plural methods — MDA/systems loops, plural narrative topologies, world/character consistency bibles; TTRPG ≠ VG law; agent critique via HITL/producer–critic (no invented creative AgDR). [T5D]
5. **T5C deferred** until UX RAG or queryable corpus readiness. [placeholder]
6. **Do not elevate Design skills** until this report is accepted.

---

## 2. Sources merged

| Track | Synthesis | stop_reason |
|-------|-----------|-------------|
| T5A | `notes/theme-5-design/t5a-track-synthesis.md` | `low_return_plus_one` |
| T5B | `notes/theme-5-design/t5b-track-synthesis.md` | `low_return_plus_one` |
| T5D | `notes/theme-5-design/t5d-track-synthesis.md` | `low_return_plus_one` |
| T5C | placeholder only | deferred |

Gatherer trees under `docs/research/notes/theme-5-design/` (pins, W1–W3). Subagents: `cursor-grok-4.5-high-fast`.

---

## 3. Cross-track process spine (T5A)

| Step | Role |
|------|------|
| Frame + constraints | Human-owned; AI may help |
| Criteria before solutions | Human refine |
| Alternatives + tradeoffs | Matrix / 2–3 approaches |
| Critique | Human amends AI analysis |
| Decide | **Human accountable** |
| Record | ADR/MADR (AI may draft; human owns) |
| Gate | HITL before implementation |

- ADR/MADR: Nygard core + Fowler/MADR options atoms; Theme 2 reuse; draft/proposed ≠ SoT.  
- Cursor Plan Mode: plan→review→build; **≠** ADR options matrix.  
- Superpowers/AgDR: E3 structure inventory only — do not merge git/PR policies; AgDR single-author lineage.

---

## 4. Technical design (T5B)

| Topic | Takeaway |
|-------|----------|
| Modularity | Dependency Rule; ADP/SDP/SAP; REP/CCP/CRP; Hexagonal/Onion E1 |
| Patterns | GoF vocabulary ≠ whole-app architecture |
| Deploy shape | Monolith-first vs microservices — cite both; ADR when structure choice |
| ADR triggers | Significance axes (Nygard/AWS) + multi-option/undocumented |
| Clean/standards | Contested schools — constraints, not architecture SoT |
| Agents | Plan-first; human owns architecture decisions |

---

## 5. Creative & game systems (T5D)

| Topic | Takeaway |
|-------|----------|
| Systems | MDA E1 + Sellers/Schell/Zubek/Adams plural loops; not code CA |
| Narrative | Plural topologies; bind beats to state where supported |
| World/character | Bible structure; consistency; TTRPG vs VG distinct |
| Critique | HITL + producer–critic; no creative AgDR invented |
| GUR/GDD | GUR methods E2; GDD templates E3 discovery only |

---

## 6. Deferred — T5C

Re-open when UX corpus ingested with good probes, or queryable site corpus documented, or human waives web/E1-first deep. Integrator invents **no** UX FACTS here.

---

## 7. Conflicts retained

| Conflict | Handling |
|----------|----------|
| ADR status vocab / folder paths | OPEN — project meta-decision |
| Clean Code schools | Cite both; no winner |
| Monolith vs microservices | Cite both; criteria + ADR |
| HITL design-time vs per-decision | OPEN — layers may differ |
| Story method plurality | No single SoT |

---

## 8. GAP / OPEN (non-locks)

- T5C entire track deferred  
- E0 Plan Mode UX; agent-native ADR schema  
- Windows service/desktop design (non-P0)  
- Creative AgDR / machine beat↔state schema  
- Classical ATAM / non-AI design baselines thin  

---

## 9. Toolbelt implications (accepted elevation 2026-07-29)

Elevated via `author-cursor-surfaces` after accept:

| Surface | Track | Path |
|---------|-------|------|
| `design-process` | T5A | `skills/design-process/` |
| `design-technical` | T5B | `skills/design-technical/` |
| `design-systems` | T5D | `skills/design-systems/` |
| `design-narrative` | T5D | `skills/design-narrative/` |
| `design-world-character` | T5D | `skills/design-world-character/` |
| House ADR + `research-draft-adr` | cross | `docs/adr/`; options required |
| `draft-is-not-sot` rule | cross | includes draft design / proposed ADR |
| UX skill | T5C | **Not elevated** |

**Hard reject (retained):** one mega-skill claiming all design types. Superpowers not referenced in Design skills.

---

## 10. Method (integrator)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Depth | deep |
| Inputs | T5A/B/D track syntheses + campaign brief + T5C placeholder |
| New facts | **none** |
| Campaign stop | Active tracks complete; T5C deferred does not block |
| Next | Human accept (full / facts-only / slice) → elevation |
