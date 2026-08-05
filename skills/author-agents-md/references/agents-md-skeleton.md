# {Project} agent instructions

> Portable baseline (`AGENTS.md`). Keep short; nest per-package files for monorepos.  
> Claude Code: import via `@AGENTS.md` from `CLAUDE.md` or symlink.  
> Evidence: Theme 2 report §2.2; https://agents.md/ — not a mandatory schema.  
> **Size budget:** OpenAI Codex default `project_doc_max_bytes` = **32768 (32 KiB)**. Guide prose treats this as a **combined** stop when concatenating files; another official dump section wording looks per-file — prefer **combined** for templates until clarified (`OPEN`). Raise the knob or nest/split when hitting the cap ([Codex AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md); also `llms-full.txt`).  
> Cursor also supports nested `AGENTS.md` (closer paths take precedence). Prefer progressive disclosure over a mega-root file.  
> Codex discovery (for interop): global `AGENTS.override.md`/`AGENTS.md` → project walk with per-dir override then `AGENTS.md`. Merge semantics differ by vendor — do not assume identical behavior.

## Dev environment / commands

- Install:
- Build:
- Test:
- Lint:

(Use exact, copy-pasteable commands.)

## Layout / architecture pointers

-
-

## Code conventions

- (short, verifiable bullets — not entire style guides)

## Testing / definition of done

-
-

## Boundaries (do-not)

-
-

## Security / secrets

-

## When you change this file

Update after repeated agent mistakes. Prefer progressive disclosure (link deeper docs) over growth past tool budgets.
