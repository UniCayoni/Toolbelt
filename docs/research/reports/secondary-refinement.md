# Secondary refinement report

Date: 2026-07-28  
Priorities: `docs/research/SECONDARY_PRIORITIES.md`  
Notes: `docs/research/notes/secondary/`

## Verdict

Highest-impact gaps that unblock templates and skill elevation were closed or narrowed with primary E1 evidence. Templates updated. Ready to elevate **five** Cursor skills (plus soft rule / optional hard hook) after your review — **full SKILL.md bodies not written yet**.

## Closed / narrowed

| Gap ID | Outcome | Evidence |
|--------|---------|----------|
| T1-Yang (SWE-agent ACI) | **Closed** as primary | arXiv:2405.15793v3 PDF extract + abstract API |
| T2-G6 / O5 (Codex AGENTS.md) | **Closed** | developers.openai.com/codex/guides/agents-md — 32 KiB default, discovery order |
| T3-G12 (WTD testing docs) | **Closed** | writethedocs.org/guide/tools/testing/ |
| T2-O1 / O2 (spans / dual payload) | **Closed as local convention** [E4] | chunk_id+grade required; spans optional; JSON claims optional |
| T3-O2 (conflict-log schema) | **Closed as local convention** [E4] | fields in `claim-citation.md` |
| T3-G8 (RFC 2119) | **Closed** | rfc-editor.org/rfc/rfc2119 |
| T2-G10 (PROV) | **Closed brief** | W3C PROV-DM/O |
| T3-G15 (Spectral/Schemathesis) | **Narrowed** | Schemathesis + Spectral READMEs |
| T1 soft vs hard gate | **Recommended close** [E4] | soft skill/rule default; hook optional |
| Explore mandatory? | **Recommended = not mandatory** [E4] | large-repo recommend only |
| FAIR4RS / Lamprecht | **Closed** [E1] | via [Secondary elevation](53b8f1ee-f441-4380-ac21-5dec3213799b) note §3.6 |

## Still open / deferred

- T2-G1 portable evidence-span standard
- T3-O1 ecosystem known-issues URL catalog
- T2-O3 GreyMatter public `/llms.txt` product decision
- “Enough comprehension” metric beyond checklist
- Codex `project_doc_max_bytes` combined vs per-file wording (`OPEN`)
- Full SWE-agent §5 ablation transcription
- Conflict-log storage format (YAML vs table vs JSONL) when skills elevate

## Subagent merge

Coordinator integrated notes from [Secondary P0](9693d283-4bc1-482d-b1fd-02256120c863), [Secondary P1](b13e49ba-eb79-4d1a-b05c-53911017f1d2), and [Secondary elevation](53b8f1ee-f441-4380-ac21-5dec3213799b). Elevation note restored after write race; P1 note kept as subagent body; P0 canonical + merge addenda.

## Template diffs applied

- `agents-md-skeleton.md` — 32 KiB / nesting / Codex discovery note
- `claim-citation.md` — citation defaults + conflict-log YAML + PROV pointer
- `documentation-research.md` — RFC 2119 on D3; WTD/Spectral/Schemathesis on D12; conflict-log link D13
- `codebase-reconnaissance.md` — ACI lens on S8; Explore recommended on S9; soft/hard elevation note on S16
- `research-note.md` — optional PROV Method row

## Elevation preview

See `reports/cursor-elevation-map.md`. Proposed skills: `research-codebase-recon`, `research-docs`, `research-protocol`, `author-agents-md`, `research-draft-adr`.

## Next step (your call)

1. Approve elevation → write SKILL.md under future `grey-matter/` (or workspace `.cursor/skills/` for trial)
2. Or further gap rounds (PC papers, Cursor changelog, known-issues catalogs)
3. Or resume GreyMatter plugin priming/stub
