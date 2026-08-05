---
title: "Secondary P0 — SWE-agent ACI, Codex AGENTS.md, WTD testing"
status: draft
created: 2026-07-28
aligned_with: docs/research/SECONDARY_PRIORITIES.md
---

# Method

Primary fetches (coordinator): arXiv API abstract + local PDF extract (later removed from tree; cite https://arxiv.org/abs/2405.15793); OpenAI Codex AGENTS.md guide; Write the Docs testing page. Alexandria `ai_llm_agents` for Huyen/Dibia adjacent ACI/tool design. WebFetch of ar5iv/HTML conversion failed; PDF was extracted with pypdf during the pass.

# Findings

## 1. SWE-agent ACI (Yang et al. 2024) — closes T1-Yang primary gap (partial)

**Source:** Yang et al., *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering*, arXiv:2405.15793v3 (2024-11-11). [E1] PDF local extract + Atom summary.

**FACT [E1]:** ACI = commands available to the LM **plus** how environment state is communicated back; also history/context management into a single LM input.

**FACT [E1]:** Four design principles (paper §2):

1. Actions simple / few options / concise docs
2. Actions compact & efficient (high-order ops in few turns)
3. Feedback informative but concise
4. Guardrails mitigate error propagation (e.g. syntax check on edit)

**FACT [E1]:** SWE-agent ACI components include search/navigation, file viewer, file editor, context management; ReAct thought+command loop; special search commands (`find_file`, etc.); built atop Linux shell but prefers small LM-friendly action set over raw shell for core SE ops.

**FACT [E1]:** Empirically, tailored ACI >> default Linux shell baseline on SWE-bench Lite (+10.7 pp in their ablation).

**CLAIM [E2]:** Huyen / Dibia summarize navigate/search/view/edit and “read before write / grep before edit” workflows — consistent with ACI tool surface, not a substitute for the paper. Alexandria chunks cited in coordinator pass.

**INFERENCE [E4] for GreyMatter S6–S9 / S16:** Treat recon as **using an ACI-shaped tool surface** (locate → view → then edit), with concise feedback and optional hard guardrails later via hooks — not as “bash freedom.” Soft skill encodes the workflow; hook encodes deny/ask if desired.

**Remaining GAP:** Full §5 ablation tables / exact command names beyond extract pages not transcribed into notes; demo site swe-agent.com not fetched this pass.

## 2. Codex AGENTS.md — closes T2-G6 / O5

**Source:** https://developers.openai.com/codex/guides/agents-md (accessed 2026-07-28). [E1]

**FACT [E1] Discovery order:**

1. Global: `CODEX_HOME` (default `~/.codex`) — `AGENTS.override.md` else `AGENTS.md` (first non-empty only)
2. Project: walk root → cwd; per directory `AGENTS.override.md` then `AGENTS.md` then `project_doc_fallback_filenames`; at most one file per directory
3. Merge: root→cwd concatenation; closer files appear later (override earlier)

**FACT [E1]:** Combined size capped by `project_doc_max_bytes` (**32 KiB default**); raise limit or nest/split when hitting cap. Example config raises to 65536.

**FACT [E1]:** Empty files skipped; rebuild on each run / TUI session start.

**INFERENCE [E4] for `agents-md-skeleton`:** Budget root file well under 32 KiB; progressive disclosure via nested dirs; note Cursor separately supports nested AGENTS.md (Cursor rules docs) — do not assume identical merge semantics across vendors.

## 3. Write the Docs — Testing your documentation — closes T3-G12

**Source:** https://www.writethedocs.org/guide/tools/testing/ (accessed 2026-07-28). [E1]

**FACT [E1]:** Recommend CI on each commit for docs. Categories:

- **Build errors** (tool exit code; Sphinx nitpicky / Jekyll strict)
- **Link testing** (Sphinx `linkcheck`, HTMLProofer, site crawlers)
- **Style/lint** (Vale + style packs incl. MS/Google style implementations)

**INFERENCE [E4] for D12:** When verifying docs for GreyMatter research, prefer executable checks in this order when available: build → linkcheck → example/doctest/contract → prose lint. WTD page does **not** deeply cover doctest/OpenAPI; those remain from Theme 3 other E1 (doctest, Schemathesis).

# Subagent / coordinator merge notes

- Coordinator also fetched live HTML for Codex AGENTS.md guide (2026-07-28) — corroborates `llms-full.txt` discovery + 32 KiB default. [E1]
- **OPEN (from P0 subagent):** `project_doc_max_bytes` wording in official Codex dump conflicts (combined stop vs per-file read). Prefer **combined 32 KiB** guidance for templates until OpenAI clarifies.
- **GAP:** WTD testing page omits doctest/screenshot/API contract testing — keep other E1s for those D12 modalities.

# Template deltas (candidate)

| Artifact | Change |
|----------|--------|
| `codebase-reconnaissance` | Cite ACI principles under S8–S9; keep soft gate at S16 |
| `agents-md-skeleton` | Explicit 32 KiB Codex default budget note; nesting advice |
| `documentation-research` D12 | Add WTD CI categories as checklist |
