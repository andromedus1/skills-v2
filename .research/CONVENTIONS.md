---
owner: agentic-research
---

# Research conventions

## Layout

`reference/<corpus>/` holds source records and bibliography; `attestation/` holds
flat source-handle attestations; `analysis/briefs/` holds bounded comparisons.
Create other Agentic Research tiers only when needed. Existing `docs/research/`
remains in place and discoverable; this scaffold does not convert that corpus.

## Frontmatter contracts

Attestations require `source_handle`, `fetched`, `source_url` or `source_path`, and
`provenance: source-direct`. Analytical artifacts require `provenance:
agent-synthesis`; include a title, updated date and summary for knowledge discovery.
Machine observations identify themselves as `generated-listing` in their record.

## Citation rule

`[handle]{N}` resolves through `.research/references.md` to a flat attestation and
then its fetched source. Record the load-bearing detail before citing it. Own
analyses and framework rules are comparison lenses, never source attestations.

## Lifecycle

Research has no delivery-stage progression. Use `status` and `temporal_contract`
when needed, and the canonical correction/reversal/refresh distinction for changes.
Operational decisions and engagement registration belong in the commissioning
work item. Research artifacts do not point back into `.work/`.

## Authoring and enforcement

Use Agentic Research's authoritative
[discipline](../plugins/agentic-research/ard-core/kernel/discipline.md) and
`plugins/agentic-research/ard-core/kernel/lint-citations.py`. Verification depth is
registered per engagement. Keep the discipline and validator in their owning plugin.

## Invariants

Preserve source provenance, explicit uncertainty and contradiction handling.
Research-to-work promotion is operator-confirmed. Migrations are additive and
require operator authorization; new research does not silently recast old artifacts.
