---
aligned_with: docs/research/reports/theme-2-agent-usable-documentation.md
---

# Claim & citation conventions (agent checklist)

Authority: `docs/research/PROTOCOL.md` + Theme 2 integrated report §§3–4.  
See also: `templates/doc-layers.md`.

## Hard constraints

1. **Cite-or-omit** — No citation → no factual claim.
2. **Never invent** source IDs, URLs, line ranges, APIs, or library names not observed in tools/docs.
3. **Context-only** in grounded research mode — if evidence missing → `GAP` / `insufficient_evidence`, not parametric fill-in.
4. **Draft ≠ truth** — `status: draft|proposed` must not be treated as accepted SoT.
5. Prefer **hedged truth or silence** over confident falsehood.

## Dual citation layer

### Machine layer (for later verification)

```text
corpus=… | source=… | chunk_id=… | path=… | url=… | retrieved_at=YYYY-MM-DD
```

**Defaults (secondary refinement):** Required = grade + locator (`url` \| `path` \| Alexandria `corpus`+`chunk_id` \| E0 observation). Recommended = short quote (≤25 words) on risky paraphrases. Optional = `char_start`/`char_end` when tools supply them — **not** required for integrator merge. Human markdown notes are default; machine `claims[]` JSON is optional (preferred for multi-agent merge).

### Human layer (inline)

```text
[E1: Title — https://… — accessed YYYY-MM-DD]
[E2: Alexandria corpus=`ai_llm_agents` source=`…` chunk_id=`…` query=`…`]
[E0: path=`…` or command=`…` observed YYYY-MM-DD]
```

## Claim object (preferred structured form)

Use in notes or JSON sidecars:

| Field | Required | Values |
|-------|----------|--------|
| `claim_id` | yes | stable id |
| `claim_text` | yes | atomic statement (no pronouns that hide referents) |
| `label` | yes | FACT \| CLAIM \| INFERENCE \| GAP \| OPEN \| U |
| `grade` | yes | E0–E4 \| U |
| `support` | if FACT/CLAIM | list of evidence refs |
| `premises` | if INFERENCE | list of prior claim_ids or citations |
| `status` | yes | supported \| partial \| unsupported \| insufficient_evidence |
| `confidence` | recommended | high \| medium \| low |

## Sources-of-truth precedence

1. E0 local observation / tool output (this session)  
2. E1 primary standards & official docs  
3. E1–E2 peer / canonical literature (with path+chunk)  
4. E2 secondary guides  
5. E3 community — hypothesis only  
6. Model prior / vibes / undated chat — **never SoT** → `U` or omit  

## Conflict protocol

When sources disagree: cite **both**, describe the disagreement, prefer higher grade. Do not silently pick one.

### Conflict log fields (local convention)

```yaml
conflict_id: C-###
recorded_at: YYYY-MM-DD
status: open | resolved | stale_doc | stale_code | needs_human | waived
doc_locator: { url_or_path, version, diataxis_type }
doc_quote: "…"          # recommended
doc_claim: "…"          # atomic DOC_CLAIM
code_locator: { path, symbol_or_route, commit_or_version }
command: "…"            # if E0 runtime
schema_path: "…"        # if OpenAPI/JSON Schema
observation: "…"        # + MATCH|MISSING|RENAMED|AMBIGUOUS|CONTRADICTED
winner: code | schema | doc | unresolved
winner_reason: "…"
evidence_grades: { doc: E1, observation: E0 }
claim_labels: [CONTRADICTED_BY_E0, STALE]
repair_suggestion: update_docs | fix_code | update_schema | unknown
citations: []           # both sides retained
prov_note: ""           # optional light PROV
resolved_at: YYYY-MM-DD
```

Optional PROV vocabulary for Method blocks: Entity / Activity / Agent / wasDerivedFrom / used / wasAttributedTo / wasQuotedFrom / Bundle (W3C PROV-DM/O) — do not require full RDF graphs.

**RFC 2119/8174:** Capitalized MUST/SHOULD (esp. with BCP 14 adoption) weight higher as normative intent; lowercase tutorial “must” ≠ contract; still corroborate via D12; E0 wins on conflict.

## Self-check before marking a note complete

- [ ] Every FACT/CLAIM has support refs  
- [ ] INFERENCEs list premises  
- [ ] GAPs record what was searched  
- [ ] No invented citations/APIs  
- [ ] Faithfulness spot-check: unsupported claims removed or relabeled  
- [ ] Negative rejection used where retrieval/evidence weak  
