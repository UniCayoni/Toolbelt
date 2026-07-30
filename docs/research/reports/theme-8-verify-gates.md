---
title: "Theme 8 — Verify gates (integrated report)"
status: accepted
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
accepted: 2026-07-30
acceptance_scope: method_guidance_t8_verify_gates
accepted_by: human (Jonathan)
authors: [integrator]
depth: deep
stop_reason: low_return_plus_one
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-8-verify/campaign-brief.md
  - docs/research/notes/theme-8-verify/t8-track-synthesis.md
  - docs/research/notes/theme-8-verify/t8-w3-plus1-residual.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/research/reports/theme-7-execute-pocket.md
  - skills/implementation-plan-verify/SKILL.md
  - skills/implementation-execute-verify/SKILL.md
supersedes: null
---

# Theme 8 — Verify gates (integrated report)

**Status:** **accepted** (method guidance) — 2026-07-30.  
**Elevated:** `implementation-plan-verify` + `implementation-execute-verify` (+ Plan/Execute/-subagents wire).  
**Campaign stop:** `low_return_plus_one`.

**Using `research-protocol`** · integrator merge.

**Scope:** Theme 8 is **not** the Debug/PR pocket. It is the **missing verification extension** of the shipped **Plan** and **Execute** pockets. Lean: **quality, readability, Toolbelt focus** — ease is a side effect. Debug/PR remains a later stub pack.

Standalone Toolbelt (inspire; **do not depend** on Superpowers / OpenSpec / Spec Kit / BMAD).

### Elevation decisions (accepted 2026-07-30)

| # | Decision |
|---|----------|
| D1 | Surface **C**: companions **`implementation-plan-verify`** + **`implementation-execute-verify`** |
| D2 | **Hybrid orchestration** — Plan/Execute/-subagents orchestrate; companions hold gates/rubrics |
| D3 | **Skill-only** — no always-on verify rule |
| D4 | Theme naming: **Verify gates** (Plan/Execute extensions, not Debug) |
| D5–D13 | Plan-verify: explicit phase; Reality‖Drift‖Coverage/Actionability; park TDD auditor; severity + PASS trio; fix-plan-not-code; hard ambiguity → intent-gap; light taxonomy + FR→task/DAG; verification table when non-trivial; Spec Kit grammar only |
| D14–D21 | Execute-verify: iron law; post-green review (non-trivial + EOP); fresh when required; Evidence+Faithfulness+Readability/coherence; EOP light converge (incl. unrequested); signal≠intent; Theme 7 HITL; **N=2 frozen** |
| FC-G1 | Thin rubric Evidence / Faithfulness / Readability-coherence |
| FC-SEV | **Dual-lane** severity + crosswalk |
| FC-AMB | Hard vs soft ambiguity tables |
| FC-G2 | Shared `non_trivial` = DUR/MF/IF/DEP/FLAG/SUB; trivial skip; **EOP review+converge always on durable plans** |
| FC-T8B-2 | Converge **EOP-only** |
| FC-APPEND | `## Convergence` + `### Task C###`; append-only; global max `C*` |
| FC-G3 | Companion description triggers (as shipped in SKILL frontmatter) |
| FC-LAYOUT | Companions elevated; orchestrators wired; packs updated |
| FC-PARKS | TDD auditor, council, CLI deps, Copilot PR, SHA-as-SoT, fat Quality, Debug design |
| — | Gaps/minors: recommended leans accepted (quality/readability/Toolbelt focus) — NT4 prose `review-required`; G4 bounce/warn if durable plan never plan-verified |

---

## 1. Executive summary

1. Plan had Done-when + light V1–V8; Execute had Done-when run + N=2 + critical review. Missing: graded **plan-validate** and **post-green + converge** execute-verify.  
2. Community atoms extracted; no runtime dependency.  
3. Elevated two thin companions; Debug/PR untouched.  
4. Quality lean: faithfulness, evidence, readability.

---

## 2. Sources merged

Notes under `docs/research/notes/theme-8-verify/` (pass1–3, W1–W2, PLUS1, synth). Input law: Theme 6 + Theme 7 accepted reports. Subagents: `cursor-grok-4.5-high-fast`.

---

## 3. Method spine (accepted)

```text
0. Design accepted → implementation-plan (V1–V8 light)
1. implementation-plan-verify → PASS* → Meta ready
2. Fresh context recommended → implementation-execute
3. Per task: critical review → implement → Done-when Verify (N=2)
4. When non_trivial: implementation-execute-verify post-green (fresh)
5. End of durable plan: execute-verify EOP review + light converge
6. Escalate Theme 7: intent-gap | verify-fail | needs-human | major-deviation
```

---

## 4. Boundaries

| Theme 8 owns | Plan still owns | Execute still owns | Later (not Theme 8) |
|--------------|-----------------|--------------------|---------------------|
| Graded plan-validate companion | Authoring, V1–V8 light, grammar | Task loop, N=2, HITL, subagents | Debug / PR / workflow pack |
| Post-green + EOP converge companion | Meta status vocab | Signal verify run | Copilot PR skills, git ceremony |
| Thin rubrics + thresholds | Durable `docs/plans/` | Major-deviation checklist | Fat Quality / council / TDD auditor |

---

## 5. Elevation status

| Surface | Status |
|---------|--------|
| `implementation-plan-verify` | **Shipped** |
| `implementation-execute-verify` | **Shipped** |
| Plan / Execute / -subagents wire | **Shipped** |
| `plan-minimal` plan-verify + execute-verify notes | **Updated** |
| Always-on verify rule | **Rejected** |
| Shared `implementation-verify` | **Rejected** |
| Debug/PR pack | **Out of scope** |

---

## 6. Acceptance checklist

- [x] Human accepts this report as Theme 8 method guidance  
- [x] Elevation decisions (recommended leans; quality/readability/Toolbelt focus)  
- [x] Elevate companions + wire orchestrators + update packs  
- [x] Theme 4 reinforce via **`author-cursor-surfaces`** (retroactive — see `docs/research/notes/theme-8-verify/author-surfaces-t8-verify.md`)  
- [ ] Sync local plugin + Reload Window (operator)
