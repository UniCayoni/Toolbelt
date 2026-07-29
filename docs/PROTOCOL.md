# Toolbelt Research Protocol

Status: active  
Created: 2026-07-27  
Updated: 2026-07-29 (depth modes: normal vs deep; migrated from GreyMatter → Toolbelt)  
Purpose: Rules for how agents research and how research is written so claims stay evidence-backed.

## Non-negotiables

1. **No unsupported claims.** If it is not backed by a cited source or a recorded local observation, label it `UNVERIFIED` or omit it.
2. **Cite every non-trivial claim.** Prefer primary sources (official docs, papers, repo READMEs, tool schemas) over secondary summaries.
3. **Separate observation from interpretation.** Use explicit labels (below).
4. **Prefer absence over invention.** If coverage is weak, say so and list what was searched.
5. **Record method.** Every research note must state tools used, queries, date, and corpora/URLs.

## Evidence grades

| Grade | Meaning | Allowed use |
|-------|---------|-------------|
| **E0 — Local observation** | Directly observed in this environment (file exists, command output, MCP payload) | Hard fact for this machine/session |
| **E1 — Primary source** | Official docs, standards, peer-reviewed paper, canonical repo docs | Strong claim |
| **E2 — Secondary synthesis** | Book chapter, reputable guide summarizing primaries | Soft claim; prefer linking back to primary |
| **E3 — Community report** | Forums, blogs, GitHub issues, anecdotes | Hypothesis / caveat only. **Exception for docs research:** E3 is a first-class *discovery* channel for limitations/bugs/outdated behavior, but still cannot alone lock design — corroborate with E0/E1 when possible. |
| **E4 — Inference** | Logical conclusion from E0–E2 | Must state premises |
| **U — Unverified** | Plausible but not evidenced in this pass | Must not drive design locks |

## Claim labels (required in notes)

- `FACT` — graded E0–E2
- `CLAIM` — graded E3 or contested E2
- `INFERENCE` — graded E4 with premises listed
- `GAP` — searched; not found / weak coverage
- `OPEN` — needs follow-up research

## Citation format

Inline:

```text
[E1: Cursor Hooks docs — https://cursor.com/docs/hooks.md — accessed 2026-07-27]
```

For Alexandria RAG chunks:

```text
[E2: Alexandria corpus=`ai_llm_agents` source=`<source_rel_path>` chunk_id=`<id if available>` query=`"..."`]
```

For local commands/files:

```text
[E0: path=`d:\GreyMatter\...` or command=`...` observed 2026-07-27]
```

## Depth modes (normal vs deep)

**Default: `normal`.** Escalate to **`deep`** only when the user asks for deep/theme research, or the goal is a durable multi-surface integrated report / method redesign.

| Mode | Shape | Stop |
|------|-------|------|
| **normal** | One gatherer or short sequential pass; one Method note or graded checklist | Question covered or GAPs listed |
| **deep** | Parallel gatherers by domain; waves (primary SoT → corroboration → residual GAPs); integrator merges | **Diminishing returns** — stop when new notes only restate FACTS, residuals need undocumented runtime, or budget is exhausted |

Full procedure + caveats: `docs/templates/research-depth-modes.md` (skill `research-protocol` → `references/research-depth-modes.md`).

Deep reports remain `draft`/`proposed` until accepted — not design law.

## Note file schema (source agents)

Each parallel researcher writes **notes only** (not the final integrated report) to:

`docs/research/notes/theme-{1|2}/<agent-id>.md`

Required sections:

1. Scope
2. Method (tools, queries, date)
3. Findings (bullets with claim labels + citations)
4. Contradictions / conflicts found
5. Gaps
6. Candidate patterns for templates (still cited)
7. Source list (deduped)

## Integration rules

The integrator:

- Merges notes; does not invent new facts
- Resolves conflicts by preferring higher evidence grade; records remaining conflicts
- Produces theme reports + cross-cutting templates
- Marks anything still `U` or `OPEN` explicitly

## Out of scope for this protocol

- Locking host-product libraries or MVP feature scope (e.g. Brain/RAG stack)
- Inventing product APIs from stubs (e.g. grey-matter plugin scaffold ≠ live Brain)
