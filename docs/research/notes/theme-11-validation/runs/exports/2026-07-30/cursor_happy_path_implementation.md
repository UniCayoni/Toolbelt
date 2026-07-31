# Happy path implementation
_Exported on 7/30/2026 at 22:21:53 PDT from Cursor (3.13.25)_

---

**User**

@h1-implementation-happy-path.md (1-34) 

---

**Cursor**

I'll run the H1 handoff: read the claim card and `implementation-happy-path`, then do Part A (and B/C if appropriate) and write the run note.

Using `implementation-happy-path` for H1 orchestration. Pulling the checklist and a sample run log for format.

Classifying Part A as a bug (off-by-one fix), then running Parts B and C and writing the run log.

Using `implementation-happy-path`. Run log: `docs/research/notes/theme-11-validation/runs/H1-20260730.md` — **PASS**.

### Part A — classifier + stages

```text
Ask type: bug
Entry skill / skip notes:
  Entry: reproduce-bug (prove-first) → systematic-debug.
  Design SKIP documented (pure bug-fix / clear repro).
  Return to implementation-plan if design wrong.
  Research: N/A unless fixture unfamiliar.
  ADR / Plan / Execute: N/A on bug entry (unless returned to plan).
```

```text
Happy-path Progress:
- [x] 0 Classified ask → bug
- [ ] 1 Research — N/A (or light codebase-recon)
- [ ] 2 Design — SKIP documented
- [ ] 3 draft-adr — N/A
- [ ] 4–7 Plan/Execute — N/A unless returned to plan
- [ ] 8 Debug branch (primary) — reproduce-bug → systematic-debug
- [ ] 9 Stop / human handoff
```

Workers = **one pocket**. No implementation; no pocket spines pasted.

### Part B — small feature fix

Routes through the Toolbelt ladder: research (as needed) → `design-process` → (optional `draft-adr`) → `implementation-plan` → `implementation-plan-verify` → execute / execute-subagents → execute-verify → debug branch if needed → stop. No foreign workflow.

### Part C — ADR only

Ask type authoring → `draft-adr`. Full feature ladder not mandatory.

