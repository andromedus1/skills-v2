---
id: feature-model-notes
kind: feature
stage: review
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

## Implementation (2026-10-19)
Standing lineup confirmed by Andrew (recorded in `.work/CONVENTIONS.md`
`## Model lineup`). Minimal-churn choice: `models.md` is upstream-owned, so instead
of rewriting it a short fork note sets the resolution order (peeragent alias
table + runtime discovery → operator lineup → MODEL-NOTES; upstream names are
dated examples), keeping future syncs cheap. `model-selection-pattern.md` was
already role-based; it gains a "Resolving concrete models" section with the
durable tendencies. `.work/MODEL-NOTES.md` added under Workbench's evidence rules
(no frontmatter, qualified, pruned; not indexed), seeded with six observations from
2026-10-19 and two working-guidance lines. Fork patch documented in
`docs/project-navigation.md`. No staleness trigger; no external research needed
(effort levels per host come from the peeragent skill).

## Implementation notes
- Execution capability: host inline. Review weight: standard (default).
- Files: `plugins/agile-workflow/skills/principles/references/models.md` (fork
  note, 7 lines); `plugins/research-pipeline/docs/model-selection-pattern.md`;
  `.work/CONVENTIONS.md`; `.work/MODEL-NOTES.md`; `docs/project-navigation.md`.
- Verification: RP portability ok; models.md diff vs upstream = Kimi/Pi patch +
  the fork note only.
- Discrepancy from the reshape decision: models.md is not rewritten wholesale
  (fork note instead) to limit upstream-sync drift — consistent with the new
  overbuilding calibration.
