---
id: feature-version-matcher-shape
kind: feature
stage: drafting
tags: [agentic-research, citations, lint]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Close version-number matcher shape gaps in the citation lint

## Brief

The `version-number` pattern in the ARD citation lint
(`plugins/agentic-research/ard-core/kernel/lint-citations.py:76`) has shape gaps
that the QVC-S/METH-001 experiment surfaced and `feature-ar-fork-citation-matcher`
left out of scope (that feature shipped tier suppression and token-aware
cited-line suppression, variant B; corpus version flags 174 → 60).

- **Recall:** case-insensitive `Version N` (e.g. `Version 3`) and dotless `vN`
  (e.g. `v2`) are not matched. Every experiment variant missed them.
- **Precision:** residual noise under variant B is mostly section refs (`§4.2`),
  arXiv IDs (`2310.06825`), percentages, decimal statistics and model names
  (heuristic triage, synthetic fixtures; not field measurement).

Close both sides without regressing the anchor rules: a newly matched form must
still be suppressible by the same tier and token-aware cited-line anchors
(`_version_core`, the attestation-body token check at `:439-454`), and new
precision exclusions must not hide plausible fabricated version claims. Ship
labeled positive and negative conformance fixtures for each new form and each
exclusion so the suite can tell variants apart, and report corpus flag counts
before and after.

The fork owns `agentic-research` (operator decision 2026-10-19, recorded in
`feature-claude-methodology-repeat`), so the kernel lint is editable here.
Recall additions raise the flag count while exclusions lower it; the design
must state the net trade and its fixture evidence.

## Simplification opportunity

The suppression-policy header comment (`lint-citations.py:28-38`) and any
prose caveat that lists unmatched or noisy version shapes should shrink to
match the new behavior rather than grow. No other deletions identified; the
`scripts/lint-citations.py` shim forwards to the kernel and needs no change.
