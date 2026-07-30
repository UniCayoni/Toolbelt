---
title: "Author Cursor surfaces — full Toolbelt inventory audit"
status: superseded
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
aligned_with:
  - docs/templates/author-cursor-surfaces.md
  - docs/research/reports/theme-4-cursor-plugin-components.md
supersedes: null
---

# Author Cursor surfaces — Toolbelt inventory audit

**Superseded by** [`author-surfaces-full-plugin-audit.md`](./author-surfaces-full-plugin-audit.md) (complete component matrix).

**Using `author-cursor-surfaces`**.

## 0 — Outcome & mode

| Field | Value |
|-------|-------|
| Outcome | Audit all Toolbelt plugin skills/rules for Theme 4 reinforce consistency after Theme 8 elevation |
| Mode | **migrate** (conform existing surfaces) + light **author** patches |
| Target | Toolbelt plugin |
| Status | **superseded** — see full plugin audit |

## 1 — Inventory

| Kind | Count | Notes |
|------|------:|-------|
| Skills | 16 | All `name` == folder |
| Rules | 4 | 2 always-on (thin), 2 intelligent |
| Commands | 0 | OK — prefer skills |
| Hooks | 0 | OK — soft gates only |

### Slash-only (`disable-model-invocation: true`) — intentional

| Skill | OK? |
|-------|-----|
| `author-cursor-surfaces` | yes |
| `author-agents-md` | yes |
| `draft-adr` | yes |

All other skills discoverable (no DMI) — matches Plan/Execute/Verify companions.

### Rules

| Rule | alwaysApply | Thin? |
|------|-------------|-------|
| `draft-is-not-sot` | true | yes |
| `research-protocol-grades` | true | yes |
| `research-before-write` | false | yes |
| `research-skill-coexistence` | false | yes |

## 2 — Gaps found (pre-patch)

| Severity | Surface | Gap |
|----------|---------|-----|
| P1 | `codebase-recon`, `docs-research`, `draft-adr`, `author-cursor-surfaces` | Refs listed without **“Read X when Y”** gate wording |
| P1 | `implementation-execute-subagents` | No local `references/`; checklist pointer not “read when”; thin vs Execute pattern |
| P2 | Research/design skills | No uniform **Handoffs** table (Plan/Execute/Verify have them) |
| P2 | `design-process` | Domain handoff OK; post-gate ladder should name plan-verify explicitly (spine already updated) |
| OK | All skills | Announce Using; name==folder; budgets &lt;500 lines |
| OK | Verify companions | Reinforced in prior note |

## 3 — Patches applied this pass

- P1 **read-when** on `codebase-recon`, `docs-research`, `draft-adr`, `author-cursor-surfaces`, `research-protocol`, `author-agents-md`
- P1 **subagents** References → shared Execute / execute-verify checklists (no `..` paths)
- P2 **Handoffs** tables on recon, docs-research, draft-adr, author-*, research-protocol, design-process, technical + creative design skills (ladder → plan-verify)
- Rule `research-skill-coexistence`: elevate/revise surfaces → `author-cursor-surfaces`
- Sync to local plugin done; Reload once more for this pass

## 4 — Deferred (not blocking)

- Full description rewrites for every creative skill (already short + pushy enough)
- Adding `references/` directory under `-subagents` (pointing at Execute checklist is enough)
- Marketplace review (`review-plugin-submission`)
- Hooks

## 5 — Verify

- [x] Audit complete
- [ ] Patches synced + Reload (after this pass)
- [ ] Human accepts audit note / remaining P2 as OK-to-defer
