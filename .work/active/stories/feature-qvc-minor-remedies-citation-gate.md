---
id: feature-qvc-minor-remedies-citation-gate
kind: story
stage: done
tags: [methodology-review, research-pipeline, cleanup]
parent: feature-qvc-minor-remedies
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# QVC minor remedies — citation-gate

## Brief
Checkpoint for the parent feature's unit covering "citation-gate".

## Implementation
See `feature-qvc-minor-remedies` § Implementation Units (citation-gate).

## Completion evidence (2026-10-19)
- `gate-citations/SKILL.md`: `--exit-code-on medium` with an exit-code/JSON
  interpretation table (JSON validity still mandatory); broken citations taken
  from the lint's `broken_chains` (restated status list removed); stage table maps
  severity only; `Warn-only: campaign_unbound N, substrate_confidence_omitted N`
  output line; `.research/analysis/briefs/<slug>.md` example paths; version caveat
  names arXiv IDs, `§x.y`, "version N", decimals and titles until the matcher
  feature lands.
- Verification (worker): verbatim command on this repo → exit 0, valid JSON,
  0 broken, `Warn-only: campaign_unbound 0, substrate_confidence_omitted 5`;
  scratch fixtures: unresolved handle → exit 1 + valid JSON (high); unreachable
  source → exit 1 (medium); low-only → exit 0; bad flag → exit 2, empty output;
  scripted comparison of skill status prose vs `catalogs.json`: all 7 broken
  statuses covered, none misclassified.
- Discrepancy: also adjusted the "Required fix" text and Execution/evidence line
  (status parenthetical removed; exit code + JSON validity reported).
