---
name: scout
description: >
  Map prior art before project definition or scope expansion. Retains the familiar breadth-first
  pipeline entrypoint and delegates grounded acquisition, synthesis, and verification to
  agentic-research:research-orchestrator.
---

# Scout

Scout answers “what already exists, and what should we investigate next?” It
does not choose a technology, define the product, or replace deeper research.

Read `${CLAUDE_PLUGIN_ROOT}/docs/research-composition.md`, project intent, and
the knowledge index. Define several genuinely distinct prior-art search vectors
and state which project decision the landscape will inform.

Invoke `agentic-research:research-orchestrator` with:

- `intent: prior-art-landscape`;
- a proposed breadth-survey/landscape `output_kind`;
- the project constraints and north-star context;
- the decision-relevance hypothesis; and
- any existing landscape as a refresh input.

The orchestrator owns dials, decomposition, source acquisition, attestations,
the landscape brief under the current `.research/analysis/` map, and all
verification. Preserve Scout's neutrality in the seed: surface representative
adjacent products, open-source projects, academic or standards work, recurring
patterns, failures, and research gaps without selecting a winner.

## Domain-map mode

When `methodology-review` (or another caller) asks for a domain map, propose
`output_kind: [landscape-brief, vocab-capture]` and request the section shape in
[domain-map.md](../methodology-review/references/domain-map.md): jobs and outcomes,
decision dimensions, approach families in their own terms, scenarios, evidence by
level and open questions. Describe the topic generically; project specifics stay
with the caller. Search vectors must reach beyond the caller's current approach and
vocabulary, including adjacent fields solving the same job. The result is an
ordinary landscape brief that later reviews may reuse or refresh. The caller, not
Scout, draws the sample from it.

After completion, index the landscape and return concise recommendations for
subsequent research. When called from `ideate`, pass the artifact back as input;
do not let Scout define project scope itself.
