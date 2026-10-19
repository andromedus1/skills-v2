---
id: feature-upstream-sync-2026-10
kind: feature
stage: drafting
tags: [upstream, agile-workflow, ux-ui-design]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Sync upstream-owned plugins to nklisch/skills 638867b6

## Brief

Bring agile-workflow (0.16.16), ux-ui-design (1.0.0, breaking), prose-craft, code-audit, Workbench (tree only, stays disabled) and small manifest touches up to upstream; update research-pipeline feature/epic-design and any other fork callers to the ux-ui concierge; preserve documented fork patches (models.md, bump-version guard and test); skip upstream's Workbench-only bump test group and Antigravity manifests; correct the catalog's peeragent description and update Claude's peeragent install to 0.8.3. Smoke-check UI triggers on both hosts. Decided by Andrew 2026-10-19 — see `feature-upstream-learnings-2026-10`,
"Operator decisions"; research: `.research/analysis/briefs/upstream-learnings-2026-10-landscape.md`.

## Simplification opportunity

ux-ui-design 1.0.0 removes ~10k lines of pipeline skills; drop fork callers to retired skills rather than shimming them.
