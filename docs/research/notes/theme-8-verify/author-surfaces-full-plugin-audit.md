---
title: "Author Cursor surfaces — full Toolbelt plugin audit"
status: accepted
theme: theme-4-cursor-plugins
created: 2026-07-30
updated: 2026-07-30
accepted: 2026-07-30
accepted_by: human (Jonathan)
authors: [coordinator]
aligned_with:
  - docs/templates/author-cursor-surfaces.md
  - docs/research/reports/theme-4-cursor-plugin-components.md
  - docs/research/reports/theme-8-verify-gates.md
supersedes: docs/research/notes/theme-8-verify/author-surfaces-inventory-audit.md
---

# Full Toolbelt plugin surface audit

**Using `author-cursor-surfaces`**.

Authority: Theme 4 accepted + checklist §3–§5. E0 inventory 2026-07-30 (repo `d:\Toolbelt` + sync target `~/.cursor/plugins/local/toolbelt`).

**Status:** **accepted** 2026-07-30 — optional findings closed with Theme-style leans (thin surfaces; quality/focus over ceremony).

## 0 — Outcome & mode

| Field | Value |
|-------|-------|
| Outcome | Complete inventory + Theme 4 reinforce audit of every Cursor plugin surface Toolbelt ships |
| Mode | **migrate** (conform) — audit first; patches called out |
| Target | Toolbelt plugin (repo + local sync) |
| Status | **accepted** |

## 1 — Component matrix (Theme 4 catalog)

| Component | Theme 4 path | Present? | Count / notes |
|-----------|--------------|----------|---------------|
| Manifest | `.cursor-plugin/plugin.json` | **yes** | `name=toolbelt`, `displayName=Toolbelt`, version `0.1.0`, description includes Verify |
| Skills | `skills/<name>/SKILL.md` | **yes** | **16** |
| Rules | `rules/*.mdc` | **yes** | **4** (2 always-on, 2 intelligent) |
| Agents | `agents/` | **no** | Intentional — T4L GAP (no Task isolation via plugin agents) |
| Commands | `commands/` | **no** | Intentional — slash workflows use skills + DMI where needed |
| Hooks | `hooks/hooks.json` | **no** | Intentional — soft gates only (ADR soft explore-before-edit) |
| MCP | `mcp.json` / manifest mcpServers | **no** | Intentional — Brain/RAG is grey-matter, not Toolbelt |
| Root `SKILL.md` | (single-skill plugin) | **no** | Correct — multi-skill under `skills/` |
| Marketplace multi-plugin | `.cursor-plugin/marketplace.json` | **no** | Single-plugin repo — OK |
| Packaged `AGENTS.md` | — | **no** | Correct — T4N plugins don’t ship AGENTS.md |

**Sync parity (E0):** repo skills 16 = local 16; rules 4 = 4; no orphan folders either side after last sync.

## 2 — Skills (per-surface Theme 4 §3)

Common: all `name` == folder; all announce `Using …`; all bodies &lt;500 lines; all `description` ≤1024 chars (Spec cold-start budget).

| Skill | DMI (slash) | Refs | Handoffs | Read-when | Pack | Notes |
|-------|:-----------:|:----:|:--------:|:---------:|------|-------|
| `codebase-recon` | | 1 | yes | yes | Research | OK |
| `docs-research` | | 1 | yes | yes | Research | OK |
| `research-protocol` | | 4 | yes | yes | Research | OK |
| `author-agents-md` | **yes** | 2 | yes | yes | Research | Slash intentional |
| `draft-adr` | **yes** | 1 | yes | yes | Research | Slash intentional |
| `author-cursor-surfaces` | **yes** | 1 | yes | yes | Research | Slash intentional |
| `design-process` | | 1 | yes | yes | Design | OK |
| `technical-design` | | 1 | yes | yes | Design | OK |
| `creative-systems-design` | | 1 | yes | yes | Design | OK |
| `creative-narrative-design` | | 1 | yes | yes | Design | OK |
| `creative-world-character-design` | | 1 | yes | yes | Design | OK |
| `implementation-plan` | | 2 | yes | yes | Plan | OK |
| `implementation-plan-verify` | | 1 | yes | yes | Verify | Theme 8 |
| `implementation-execute` | | 1 | yes | yes | Execute | OK |
| `implementation-execute-subagents` | | **0** | yes | yes* | Execute | *refs via sibling skills — OK pattern; no local `references/` |
| `implementation-execute-verify` | | 3 | yes | yes | Verify | Theme 8 |

**DMI policy:** Only authoring/decision slash skills use `disable-model-invocation: true`. Method/workflow skills stay discoverable — **pass**.

## 3 — Rules (Theme 4 §3)

| Rule | alwaysApply | Lines | Desc ≤1024 | Globs | Verdict |
|------|-------------|------:|:----------:|:-----:|---------|
| `draft-is-not-sot.mdc` | true | 16 | yes | no | **Pass** — thin always-on |
| `research-protocol-grades.mdc` | true | 16 | yes (short) | no | **Pass** — thin always-on |
| `research-before-write.mdc` | false | 17 | yes | no | **Pass** — intelligent; optional globs later |
| `research-skill-coexistence.mdc` | false | 21 | yes | no | **Pass** — intelligent; points at `author-cursor-surfaces` for elevation |

No long workflows in always-on rules — **pass**.

## 4 — Non-surface plugin assets (related, not Cursor components)

| Asset | Role | Audit note |
|-------|------|------------|
| `docs/PROTOCOL.md` | Method SoT | Copied into `research-protocol` refs via refresh script |
| `docs/templates/*` | Template SoT | Refresh → skill `references/` |
| `docs/packs/README.md` | Pack index | Should list all shipped packs/skills |
| `docs/plans/`, `docs/adr/` | Host conventions | Not plugin components |
| `scripts/refresh-skill-references.py` | Ref sync | Required after template edits |
| `scripts/sync-toolbelt-local-plugin.py` | Local install | Required after surface edits |
| `README.md` | Human install | **Drift** — still under-lists Verify / Design skills (see §6) |
| `docs/research/**` | Method history | Not loaded as Cursor surfaces |

## 5 — Compose / ladder (expected wiring)

```text
codebase-recon / docs-research / research-protocol
        ↓
design-process (+ technical | creative-*)
        ↓
draft-adr (as needed)
        ↓
implementation-plan → implementation-plan-verify
        ↓
implementation-execute | -subagents → implementation-execute-verify
```

Authoring side-path: `author-cursor-surfaces` · `author-agents-md`.

E0: spine skills handoff tables include plan-verify / execute-verify after Theme 8 + reinforce pass.

## 6 — Findings

| ID | Sev | Finding | Recommendation |
|----|-----|---------|----------------|
| F1 | **P1** | Root `README.md` skills table / verify list omitted Design creatives + Verify companions; layout said “Quality stub” | **Fixed** this pass — README + packs wire notes updated |
| F2 | P2 | `implementation-execute-subagents` has no local `references/` | **Accepted lean: keep** shared Execute / execute-verify checklists — no duplicate `references/` (thin; avoid sprawl) |
| F3 | P2 | Intelligent rules have no `globs` | **Accepted lean: defer** — pushy descriptions sufficient; revisit only if under-trigger observed |
| F4 | P2 | `plugin.json` keywords | **Accepted lean: done enough** — `plan-verify` / `execute-verify` already added; no further keyword pile-on |
| F5 | OK | No agents/commands/hooks/MCP | Aligns with Theme 4 Toolbelt stance |
| F6 | OK | Local sync parity 16/16 + 4/4 | Healthy |
| F7 | OK | Description budgets all ≤1024 | Healthy |
| F8 | Process | Future elevations must use `/author-cursor-surfaces` before treating SoT | Already in coexistence rule |

## 7 — Patches from this audit

| Action | Status |
|--------|--------|
| Full audit note (this file) | written |
| README + packs alignment for Verify/Design | **done** |
| Skill/rule body Theme 4 reinforce | prior inventory pass (2026-07-30) |

## 8 — Verify checklist (§5)

- [x] Paths relative; under plugin layout
- [x] No secrets / `${VAR}` MCP (N/A)
- [x] Sync parity verified E0
- [x] Operator Reload after README sync
- [x] Human accepts this audit + F2–F4 leans

## 8.1 — Optional-item determinations (accepted)

| ID | Determination |
|----|----------------|
| F2 | No local `-subagents` `references/` — shared sibling checklists |
| F3 | No `globs` on intelligent rules unless later E0 under-trigger |
| F4 | Stop keyword expansion; current set is enough |
| — | No agents / commands / hooks / MCP from this audit (Theme 4 stance holds) |

## 9 — Out of scope

- Marketplace `review-plugin-submission`
- Adding hooks/MCP/agents
- Creative skill description rewrites beyond budget (already OK)
- Grey-matter plugin surfaces
