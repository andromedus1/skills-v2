---
id: feature-model-notes
kind: feature
stage: drafting
tags: [agile-workflow, process]
parent: null
depends_on: [feature-upstream-sync-2026-10]
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Evidence-graded local model notes

## Brief

Add a pruned, evidence-graded .work/MODEL-NOTES.md recording which models did well on which tasks in this repo, reconciled with the fork's models.md patch so the two do not duplicate. Decided by Andrew 2026-10-19 — see `feature-upstream-learnings-2026-10`,
"Operator decisions"; research: `.research/analysis/briefs/upstream-learnings-2026-10-landscape.md`.

## Simplification opportunity

May let the fork's models.md patch shrink to defaults while local experience lives in MODEL-NOTES.

## Design decisions
- **Reshape (Andrew, 2026-10-19): Workbench-style.** `models.md` (fork patch) and
  `research-pipeline/docs/model-selection-pattern.md` become tendency-based with
  runtime discovery; concrete model IDs resolve only through peeragent's alias
  table; add `.work/MODEL-NOTES.md` under Workbench's evidence rules
  (`plugins/workbench/skills/work/references/model-notes.md`), seeded with
  qualified observations from this session; record Andrew's standing model lineup
  once; no staleness trigger; minimal external research (current effort levels
  per host only).
