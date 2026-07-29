# Coordinator notes — Theme 2 provenance (Alexandria software_engineering)

Date: 2026-07-27  
Agent: parent coordinator  
Method: `rag_query` corpus `software_engineering`  
Query: `research software engineering documentation provenance reproducibility decision records writing practices`

## Findings

- **FACT [E2]** Research software engineering triad: **open science**, **reproducible research**, **sustainable software** — related but distinct (open ≠ reproducible). [Irving et al. *Research Software Engineering with Python*]
- **FACT [E2]** **Code provenance** for computational results should archive: (1) analysis scripts/notebooks, (2) detailed software environment, (3) ordered data-processing steps for each key result. [same, Ch. Tracking Provenance]
- **FACT [E2]** Environment capture examples: `pip freeze`, `conda env export` → `environment.yml` committed with repo. [same]
- **FACT [E2]** Long-term: exact re-runability decays; **inspectability** (what was run; important decisions) is the enduring goal. [same]
- **FACT [E2]** ADRs (architectural decision records) appear as architecture practice artifact in software architecture metrics literature (index mention). [Ciceri et al. *Software Architecture Metrics* — thin hit; prefer primary ADR sources in integrator pass]
- **INFERENCE [E4]** Agent research docs should record method/environment/steps (provenance triad) so later agents can inspect without re-assuming. Premises: RSE provenance chapter.

## Gaps

- **GAP**: FAIR for research software described as still evolving in the book’s framing — check Lamprecht et al. 2020 primary if locking FAIR claims.
- **GAP**: Full MADR/ADR template not retrieved this query — OPEN for t2b/t2c agents or integrator.

## Source list

- Irving, Hertweck, Johnston, Ostblom, Wickham, Wilson — Research Software Engineering with Python
- Ciceri et al. — Software Architecture Metrics (ADR mention only)
