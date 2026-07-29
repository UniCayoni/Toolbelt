# Coordinator notes — Theme 1/2 web primaries (llms.txt, AGENTS.md)

Date: 2026-07-27  
Agent: parent coordinator  
Method: WebSearch + WebFetch of primary pages  
Protocol: `docs/research/PROTOCOL.md`

## Findings

### llms.txt

- **FACT [E1]** Spec at https://llmstxt.org/ (accessed 2026-07-27): Markdown file at `/llms.txt` providing curated LLM-oriented index (background, guidance, links to detailed markdown). Designed to be human- and LLM-readable and programmatically parseable.
- **FACT [E1]** Required/ordered structure: H1 title; optional blockquote description; optional details; zero or more H2 sections with markdown link lists `[name](url)` optional `: notes`; special H2 `Optional` for skippable links when context is short.
- **FACT [E1]** Also proposes clean `.md` twins of useful HTML pages (append `.md` to URL).
- **FACT [E1]** Distinct from `robots.txt` (access policy) and `sitemap.xml` (exhaustive index); llms.txt is curated for inference-time assistance.
- **FACT [E1]** Guidance: concise language; brief link descriptions; expand to context file and test models can answer from it.

### AGENTS.md

- **FACT [E1]** Canonical site https://agents.md/ (accessed 2026-07-27 via search synthesis + agentsmd repo): open Markdown format — “README for agents” for build/test/conventions; complements human README.
- **FACT [E1]** No required schema/fields — standard Markdown; agents parse text. [agents.md FAQ / community spec materials]
- **FACT [E1]** Place at repo root; nested `AGENTS.md` in packages — nearest file takes precedence (progressive disclosure by path).
- **FACT [E1]** Stewardship claimed under Agentic AI Foundation / Linux Foundation (per agents.md site messaging — verify on https://agents.md/ if needed for legal claims).
- **CLAIM [E3]** Complementary to llms.txt: AGENTS.md = how to work *in this repo*; llms.txt = where to find accurate *dependency/docs* indexes. [secondary writeups; treat as CLAIM until primary says so]

### Diátaxis

- **GAP**: Direct fetch of https://diataxis.fr/ timed out this session. **OPEN**: refetch for official four-mode model (tutorials/how-to/explanation/reference).

## Gaps

- Full AGENTS.md “v1.1” frontmatter proposal is GitHub issue discussion — not ratified as required; mark as CLAIM/OPEN if used. [https://github.com/agentsmd/agents.md/issues/135]

## Source list

- https://llmstxt.org/
- https://agents.md/
- https://github.com/agentsmd/agents.md
- https://github.com/agentsmd/agents.md/issues/135
