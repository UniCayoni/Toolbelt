---
name: author-cursor-surfaces
description: >-
  Author or compose Cursor plugin surfaces (skills, rules, commands, hooks) to
  Toolbelt Theme 4 standards. Optionally scaffold with Cursor built-ins
  (/create-skill, /migrate-to-skills, /create-subagent) then reinforce. Use when
  writing new skills, thin rules, slash commands, hooks, weaving existing
  Toolbelt skills into a workflow skill, or packing surfaces for an outcome.
  Explicit / invoke. Not a review/audit skill.
disable-model-invocation: true
---

# Author Cursor surfaces

Announce once: **Using `author-cursor-surfaces`**.

Explicit skill (`/author-cursor-surfaces`). **Author / compose** — not marketplace review.

## When to use

- Create or revise **skills**, **rules**, **commands**, or **hooks** for Toolbelt or a host plugin/project
- **Compose** existing skills/rules into a new skill for a workflow outcome
- Migrate long always-on rules or slash prompts into skills with correct frontmatter
- User asks to write Cursor plugin components “the Toolbelt way”

## Authority

- Accepted Theme 4: Toolbelt `docs/research/reports/theme-4-cursor-plugin-components.md`
- Working checklist: `references/author-cursor-surfaces.md` (SoT: `docs/templates/author-cursor-surfaces.md`)
- Grades / draft≠SoT: always-apply Toolbelt rules still bind

## Caveats (do not skip)

1. **Slash-like** — this skill is explicit `/` only; do not auto-run mid-feature work.
2. **Thin always-on rules** — long workflows belong in skills, not `alwaysApply: true`.
3. **No plugin `agents/` for Task isolation** — use runtime Subagent/Task (or `/create-subagent` for `.cursor/agents/`) until Cursor documents plugin-agent wire-up (Theme 4 GAP).
4. **Built-ins optional** — `/create-skill` etc. are scaffolds; if unavailable, author from Theme 4 alone. Never treat scaffold output as finished SoT.
5. **Draft until human accepts** — new surfaces stay draft/proposed; `draft-is-not-sot`.
6. **Standalone** — Toolbelt owns Cursor-surface standards. Do not invent merged third-party git/PR policy as Toolbelt law.
7. **Not a review skill** — do not substitute for create-plugin `review-plugin-submission` / template validators.

## Instructions

1. **Clarify outcome** with the user (purpose, triggers, where it lives: Toolbelt plugin vs host `.cursor/` vs personal skills).
2. **Copy** `references/author-cursor-surfaces.md` into a host note path **when** the job is multi-step or compose-heavy; otherwise keep the checklist mental and write artifacts directly.
3. **Choose surface** using the Theme 4 table in the checklist (§1). Prefer skill over always-on rule for multi-step work.
4. **Optional scaffold (when available):**
   - New skill → suggest/use `/create-skill`
   - Dynamic rules / user-workspace slash commands → `/migrate-to-skills` when appropriate
   - Runtime subagent → `/create-subagent` (runtime path only)
   - Record scaffold used or `GAP` if missing; continue either way.
5. **Toolbelt reinforce (required):** Apply checklist §3 — pushy descriptions, `name`==folder, conditional `references/`, correct `disable-model-invocation`, thin rules, known hook events only. Align with existing Toolbelt skill style (`announce Using …`, note output paths, cite-or-omit where research-related).
6. **Compose mode:** Map outcome steps → existing skills/rules (checklist §4). Write an **orchestration** skill that invokes/links them; do **not** paste large bodies from other skills.
7. **Write files** to the agreed paths (e.g. Toolbelt `skills/<name>/SKILL.md`, `rules/*.mdc`). Keep paths relative; no `..` traversal in plugin manifests.
8. **Host playbook drift (Toolbelt plugin):** If you changed skills/rules/host-facing templates, update `docs/host-playbook.md` and/or `docs/host-playbook-catalog.md` per checklist §5 (Theme 23). Live `SKILL.md` wins on conflict.
9. **Verify** per checklist §6 (Reload/Customize/`/` smoke as applicable). For Toolbelt plugin edits: refresh SoT refs if templates changed, then `sync-toolbelt-local-plugin.py` + Reload.
10. Stop at **draft** unless the human accepts the surface as SoT.

## Output

- New/updated skill and/or rule and/or command and/or hooks files
- Optional filled checklist note under host `docs/research/notes/` (or user path)
- Brief summary: surface chosen, scaffold used, compose map, verify status

## Handoffs

| Need | Use |
|------|-----|
| AGENTS.md house docs | `author-agents-md` |
| Decision record | `research-draft-adr` |
| Unknown Cursor API facts | `research-docs` / `research-protocol` |
| Marketplace audit | create-plugin `review-plugin-submission` (not this skill) |

## References

- Read `references/author-cursor-surfaces.md` **when** authoring, composing, or migrating Cursor surfaces (checklist §0–§7)
- SoT template: Toolbelt `docs/templates/author-cursor-surfaces.md`
- Theme 4 (accepted): Toolbelt `docs/research/reports/theme-4-cursor-plugin-components.md`
- Related Toolbelt skills: `author-agents-md`, `research-draft-adr`, `research-protocol`
