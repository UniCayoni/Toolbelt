# Toolbelt packs

| Pack | Status | Surfaces |
|------|--------|----------|
| **Research** | shipped | `codebase-recon`, `docs-research`, `research-protocol`, `author-agents-md`, `draft-adr`, `author-cursor-surfaces` |
| **Design** | shipped (Theme 5 accept) | `design-process`, `technical-design`, `creative-systems-design`, `creative-narrative-design`, `creative-world-character-design`; rule `draft-is-not-sot` (includes draft design ≠ accepted). **UX (T5C) deferred** |
| **Plan** | shipped (Theme 6 accept + elevate) | `implementation-plan` (+ wire to `implementation-plan-verify`); template `docs/templates/plan-minimal.md`; house path `docs/plans/`; rule `draft-is-not-sot` (draft plans ≠ law). See `docs/research/reports/theme-6-plan-pocket.md` |
| **Execute** | shipped (Theme 7 accept + elevate) | `implementation-execute`, `implementation-execute-subagents` (+ wire to `implementation-execute-verify` + Debug handoffs); consumes `docs/plans/` + Theme 6 Plan law. See `docs/research/reports/theme-7-execute-pocket.md` |
| **Verify gates** | shipped (Theme 8 accept + elevate) | `implementation-plan-verify`, `implementation-execute-verify`; wired from Plan/Execute/-subagents. **Not** Debug/PR. See `docs/research/reports/theme-8-verify-gates.md` |
| **Debug / investigate** | shipped (Theme 9 accept + elevate) | `systematic-debug`, `reproduce-bug`; template `docs/templates/repro-light.md`; wired from Execute / -subagents / execute-verify. **Not** Theme 8 Verify. See `docs/research/reports/theme-9-debug-pocket.md` |
| **Happy path** | shipped (Theme 10 accept + elevate) | `implementation-happy-path`; template `docs/templates/happy-path.md`; orchestrates pockets (compose only). See `docs/research/reports/theme-10-happy-path.md` |
| **Validation / E0 smokes** | shipped (Theme 11 accept; no new elevation) | P0 E0 smokes 18/18 PASS. Evidence `docs/research/notes/theme-11-validation/runs/`. See `docs/research/reports/theme-11-validation.md` |
| PR / workflow | stub | Phase 2 (listed in Theme 9 parks) |

Keep new rules **intelligent / opt-in** by default except thin always-on (draft≠SoT). Elevate further surfaces only after accepted research. UX skills wait on [`docs/research/notes/theme-5-design/t5c-ux-placeholder.md`](../research/notes/theme-5-design/t5c-ux-placeholder.md).
