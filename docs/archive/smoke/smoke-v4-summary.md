---
title: "Smoke v4 — coexistence stress + auto-fire determination"
status: draft
created: 2026-07-28
---

# Smoke v4 results

**Using `superpowers:verification-before-completion`** — fresh E0 verify before pass claims (see Method).

## Method

| Item | Value |
|------|-------|
| Date | 2026-07-28 |
| Coexistence staging | Superpowers `using-superpowers` → GreyMatter `codebase-recon` → write → Superpowers `verification-before-completion` |
| Artifact | Root `CONTRIBUTING.md` (outside `docs/research/`) |
| Verify command | Python path-exists + markdown link target check on CONTRIBUTING |
| Verify result | `VERIFY_EXIT 0`; all `./` links LINK_OK [E0] |
| Coexistence rule | Updated to allow Superpowers **process** + GreyMatter **templates/grades** |

## A. Coexistence stress — determination

| Criterion | Evidence | Score |
|-----------|----------|-------|
| Superpowers process invoked | Announced `using-superpowers`; later `verification-before-completion` with fresh verify | Met |
| GreyMatter owns research artifact | `v4-recon-before-contributing.md` with grades; CONTRIBUTING points at PROTOCOL/AGENTS | Met |
| No invented merged git workflow | CONTRIBUTING defers to AGENTS.md; no Superpowers git policy copied | Met |
| Templates/approaches followed | as-needed recon; E0-only links; draft notes | Met |

**Coexistence: PASS** (no longer partial). Staging model works when Superpowers = process, GreyMatter = research artifacts.

## B. Auto-fire probe — determination

| Probe | What happened | Interpretation |
|-------|---------------|----------------|
| Primary write (`CONTRIBUTING.md`) | Recon note **before** write | Behavior correct for `research-before-write` |
| Was recon *unprompted*? | Human asked for coexistence + auto-fire smoke; plan named recon for coexistence staging | **Contaminated** — cannot claim pure Cursor auto-inject |
| Micro-edit (smoke-v4 marker) | One-line edit on **known** file; **no** full re-recon | Matches skill “tiny known-file / as-needed skip” — correct, not a fail |
| Silent auto-fire without any test framing | Not isolated (same session already loaded rules) | **Still cannot prove** product auto-attach |

**Auto-fire (v4 same-session):** contaminated → treated as GAP pending cold start.

### Update — cold start v4b (2026-07-28)

Human-run fresh chat scored in `smoke-v4b-coldstart-score.md`:

- Inspected before write; used `research-before-write.mdc` + `codebase-recon` **without those names in the user prompt**
- Also staged Superpowers `using-superpowers`
- `HEALTH.md` present [E0]

**Auto-fire (product / unnamed select): PASS.** Coexistence reconfirmed PASS.

## Overall

| Surface | Was | Now |
|---------|-----|-----|
| Coexistence | Partial | **PASS** |
| Auto-fire (unnamed select) | GAP | **PASS** (v4b cold start) |
| Auto-fire (behavioral path) | unproven | **PASS** |

## Artifacts

- `.cursor/rules/research-skill-coexistence.mdc` (staging model updated)
- Working notes under `archive/` (`v4-*.md`)
- `CONTRIBUTING.md`, `HEALTH.md`
- `smoke-v4b-coldstart-score.md`
