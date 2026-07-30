---
name: author-agents-md
description: >-
  Draft or update portable AGENTS.md from the Toolbelt skeleton with progressive
  disclosure and size budgets. Use when bootstrapping agent instructions, nesting
  monorepo guidance, aligning build/test/do-not commands, or the user asks for
  AGENTS.md / Claude CLAUDE.md agent instruction files. Explicit / invoke.
disable-model-invocation: true
---

# Author AGENTS.md

Announce once: **Using `author-agents-md`**.

Explicit skill (`/author-agents-md`). Writes durable repo guidance — not a forever skill substitute for the file itself.

## Instructions

1. Read `references/agents-md-skeleton.md` **when** creating or restructuring an `AGENTS.md`. Read `references/doc-layers.md` **when** choosing among `llms.txt` / `AGENTS.md` / rules / ADRs (do not conflate `llms.txt` with repo agent config).
2. Prefer editing/creating root or nested `AGENTS.md` over dumping everything into Cursor rules.
3. **Budgets:** Keep guidance concise. OpenAI Codex default combined instruction budget is **32 KiB** (`project_doc_max_bytes`); nest/split or raise the knob when hitting caps. Cursor nested `AGENTS.md` also applies closer-path precedence — vendor merge semantics differ; do not assume identical behavior.
4. Include copy-pasteable install/build/test/lint; short layout pointers; do-not boundaries; security/secrets. Prefer links to deeper docs over growth.
5. Optional: Claude `CLAUDE.md` with `@AGENTS.md`; Cursor `.mdc` adapters only when needed.
6. After repeated agent mistakes, update the nearest `AGENTS.md` rather than only chatting a fix.

## Output

- Working tree `AGENTS.md` (and nested overrides if justified)
- Do not invent project commands — verify with E0 (package scripts / Makefile / README) or leave `GAP`

## Handoffs

| Need | Use |
|------|-----|
| Cursor skills/rules/commands | `author-cursor-surfaces` |
| Architecture Decision | `draft-adr` |
| Verify install/build/test claims | `codebase-recon` (E0) |

## References

- Read `references/agents-md-skeleton.md` **when** creating or restructuring an `AGENTS.md`
- Read `references/doc-layers.md` **when** choosing among `llms.txt` / `AGENTS.md` / rules / ADRs
- SoT: Toolbelt `docs/templates/agents-md-skeleton.md`
