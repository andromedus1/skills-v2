---
id: feature-qvc-minor-remedies-doc-review
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

# QVC minor remedies — doc-review

## Brief
Checkpoint for the parent feature's unit covering "doc-review".

## Implementation
See `feature-qvc-minor-remedies` § Implementation Units (doc-review).

## Completion evidence (2026-10-19)
- `plugins/research-pipeline/skills/doc-review/SKILL.md` retargeted to `.work`
  (353 → 326 lines): foundation_docs + index discovery with
  `${PLUGIN_ROOT:-${CLAUDE_PLUGIN_ROOT}}`; checks 2b foundation-vs-active-work,
  2c research refs exist, 2d done-item claims; MCP/BigQuery/TypeScript and
  roadmap/phase checks removed; mechanical-only autofix with "Operator decisions
  needed"; report fields `Baseline`, `Iteration: N of 5`, `Capped`, residual
  counts, "Fixes Applied"; gate-docs boundary line.
- Verification: forbidden-term grep clean (only phase-section headings and the
  deliberate legacy-roadmap line); skill-portability ok; doc-review
  `agents/openai.yaml` needs no change.
- Worker dry run (not fresh-context) on this repo: 2a Medium/Low
  (`docs/designs/knowledge-graph-v2.md` holds implementation units; ownership
  statement triplicated); 2b Info pending roll-forward (AGENTS.md /
  project-navigation vs `feature-ar-fork-citation-matcher`); 2c, 2d clean.
- Discrepancies from design: description edited (removed false blocking-brief
  claim); loop exits on zero *mechanical* Critical/High, operator Critical/High
  stay as blocking residuals; `Baseline` = invocation state + "Fixes Applied";
  noise guards added after the dry run. A fresh-context dry run is owed at
  feature review.
