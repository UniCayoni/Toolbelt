---
title: "Author standards checklist (modes)"
status: active
aligned_with:
  - docs/research/reports/theme-16-host-standards.md
  - docs/research/notes/theme-18-recon-history/campaign-brief.md
created: 2026-08-02
updated: 2026-08-03
---

# Author standards — checklist

Authority: Theme 16 accepted; history feedstock Theme 18 (S12b). Used by skill **`author-standards`**.  
Copy into a host note for multi-mode jobs; do not edit this SoT as the deliverable.

## 0 — Mode

| Field | Value |
|-------|-------|
| Mode | `principles` \| `standards` \| `derive` \| `bind-check` |
| Host profile path(s) |  |
| Status until human accepts | `draft` / `proposed` |

## 1 — principles

- [ ] Intent + tone recorded  
- [ ] Short named principles (not lint rules)  
- [ ] Conflict guidance noted (host-authored)  
- [ ] AGENTS.md gets a **pointer**, not a dump  
- [ ] Human accept before treating as SoT  

## 2 — standards

- [ ] Scope (langs/paths) explicit  
- [ ] v1 types chosen; parked types not smuggled in as law  
- [ ] Rules checkable (example + exception + how-to-check)  
- [ ] Enforcement pointer (tooling) is host-owned, not Toolbelt ceremony  
- [ ] Evolution / deprecate slot present  
- [ ] Human accept before treating as SoT  

## 3 — derive (brownfield)

- [ ] Ran / will run `research-codebase-recon` (as-needed) **with S12b** (history/recency)  
- [ ] Prefer existing lint/formatter configs as high-confidence signals  
- [ ] Recency window: default **12 months**, or host override (date / months / years)  
- [ ] On pattern **conflict**: default propose lean = **most recent non-one-off** (Theme 18 L2)  
- [ ] One-offs demoted (singleton / contradicts config / not in hot paths) — do not auto-win  
- [ ] Light hot-path/churn only as support; blame honors `.git-blame-ignore-revs` if present  
- [ ] Quarantine legacy dirs; log dual-era conflicts in recon S12b table  
- [ ] Emit **proposed** candidates only — never silent promote  
- [ ] Human accept → then merge into standards/principles profiles  

## 4 — bind-check (light)

- [ ] Profile paths discoverable from AGENTS or agreed host path  
- [ ] Plan Done-when / constraints can reference standards when present  
- [ ] Execute respects profiles when present; skip when absent  
- [ ] Closeout optional criterion can reference profiles  
- [ ] Do not invent Cursor AGENTS vs Team/Project precedence (product GAP)  

## 5 — Anti-patterns

- Toolbelt-universal coding law  
- Always-on standards rule  
- Auto-promote derive  
- Conflating principles with lint rules  
- Renaming `implementation-closeout` in this skill  
