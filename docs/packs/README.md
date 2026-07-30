# Toolbelt packs

| Pack | Status | Surfaces |
|------|--------|----------|
| **Research** | shipped | `codebase-recon`, `docs-research`, `research-protocol`, `author-agents-md`, `draft-adr`, `author-cursor-surfaces` |
| **Design** | shipped (Theme 5 accept) | `design-process`, `technical-design`, `creative-systems-design`, `creative-narrative-design`, `creative-world-character-design`; rule `draft-is-not-sot` (includes draft design ≠ accepted). **UX (T5C) deferred** |
| **Plan** | shipped (Theme 6 accept + elevate) | `implementation-plan` (+ wire to `implementation-plan-verify`); template `docs/templates/plan-minimal.md`; house path `docs/plans/`; rule `draft-is-not-sot` (draft plans ≠ law). See `docs/research/reports/theme-6-plan-pocket.md` |
| **Execute** | shipped (Theme 7 accept + elevate) | `implementation-execute`, `implementation-execute-subagents` (+ wire to `implementation-execute-verify`); consumes `docs/plans/` + Theme 6 Plan law. See `docs/research/reports/theme-7-execute-pocket.md` |
| **Verify gates** | shipped (Theme 8 accept + elevate) | `implementation-plan-verify`, `implementation-execute-verify`; wired from Plan/Execute/-subagents. **Not** Debug/PR. See `docs/research/reports/theme-8-verify-gates.md` |
| Debug / PR / workflow | stub | **Separate later pack** — not Theme 8 |

Keep new rules **intelligent / opt-in** by default except thin always-on (draft≠SoT). Elevate further surfaces only after accepted research. UX skills wait on [`docs/research/notes/theme-5-design/t5c-ux-placeholder.md`](../research/notes/theme-5-design/t5c-ux-placeholder.md).
