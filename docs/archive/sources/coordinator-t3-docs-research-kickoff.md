# Coordinator notes — Theme 3 docs research kickoff

Date: 2026-07-27  
Agent: parent coordinator  

## PROTOCOL update [E0]

`PROTOCOL.md` E3 row updated: community/forums/issues are first-class for **limitation discovery**, but still cannot alone lock design — corroborate with E0/E1.

## Write the Docs — Docs as Code [E1]

- Docs as Code = write docs with same tools as code: issue trackers, Git, plain-text markup, code reviews, automated tests. [E1: https://www.writethedocs.org/guide/docs-as-code/ — accessed 2026-07-27]
- Benefits claimed: writers integrate with dev; developers draft docs; **block merging** features without docs. [E1: same]

## Documentation drift [E2/E3]

- Drift = divergence between written docs and actual product/code when docs not updated with development. [E2/E3: Docsie glossary — secondary; corroborate]
- Docs-as-code co-location + PR checklists + CI checks recommended to catch drift; docs-as-code alone does not prevent drift. [E2: Sourcegraph blog on docs-as-code — https://sourcegraph.com/blog/documentation-as-code — accessed 2026-07-27]
- AI risk: agents treat docs as ground truth and may “update” docs to match inferences — defense is verify claims against code. [E2: same Sourcegraph]

## Tools / practices (E3 until verified personally)

- Staleguard, sync-docs, etc. claim deterministic/heuristic doc↔code checks — treat as product claims [E3] until GreyMatter E0 validation.

## GitHub Issues search [E1]

- Improved/semantic issue search GA announced 2026-04-02; meaning-based find + hybrid; API `search_type=semantic|hybrid`. [E1: https://github.blog/changelog/2026-04-02-improved-search-for-github-issues-is-now-generally-available/]
- Filtering/search how-to URL 404’d this pass — **GAP** for classic qualifier docs page; OPEN refetch.

## Alexandria software_engineering [E2]

- Winteringham: incomplete/outdated/unclear API docs → misuse risk; release notes often neglected. [E2: *Software Testing with Generative AI*]
- Osmani: for new/obscure frameworks AI may use outdated APIs — fall back on documentation and feed docs into context; cross-reference AI output with official docs. [E2: *Beyond Vibe Coding*]

## Gaps

- Primary academic “documentation bitrot” paper not fetched this kickoff.
- GitHub official filtering-issues page 404 this pass.
