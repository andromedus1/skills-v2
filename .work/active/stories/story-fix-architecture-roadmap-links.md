---
id: story-fix-architecture-roadmap-links
kind: story
stage: done
tags: [bug, research-pipeline, documentation]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# architecture skill still points at a retired roadmap document

## Symptom
`research-pipeline/skills/architecture/SKILL.md` linked `roadmap.md`, told users to
resolve questions "during roadmapping", and said `/epicize` creates a "phased build
plan" (parked as `idea-architecture-roadmap-links`).

## Root cause
The skill predates the retirement of the roadmap-as-document pattern; `/epicize`
now emits epics into `.work/`.

## Fix approach
Replace the eleven roadmap references with `.work` epics / epic decomposition; drop
the Roadmap row from the generated architecture doc's Related Documents table.

## Regression test
`grep -i roadmap plugins/research-pipeline/skills/architecture/SKILL.md` returns
nothing; RP skill portability passes. (Prose fix; no executable surface.)

## Implementation notes
- Execution capability: host inline. Files: architecture `SKILL.md` only.
- Confirmation: grep clean; portability ok; the template's next-step text now
  matches `epicize`'s behavior.

## Review (2026-10-19)
**Verdict**: Approve — bounded inline standalone-story review; wording only, no
behavior or authority change. No independent reviewer per the standalone lane.
