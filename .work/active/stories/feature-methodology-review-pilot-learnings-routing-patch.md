---
id: feature-methodology-review-pilot-learnings-routing-patch
kind: story
stage: done
tags: [methodology-review, agile-workflow]
parent: feature-methodology-review-pilot-learnings
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-20
updated: 2026-10-20
---

# Agile-workflow tag route for methodology-review controllers

## Brief
Fixes F4 with a documented fork patch (design decision 6). Items tagged `methodology-review-controller` route to `research-pipeline:methodology-review`, never into the design or implement families, and never bind to a release.

## Implementation
See the parent feature's Implementation Units, Unit 4.

## Implementation notes (2026-10-20)

- **Agile-workflow fork patch.** The `[methodology-review-controller]` route is
  added in four places:
  - an autopilot routing row (awaiting operator, not a blocker);
  - a feature-design misroute guard;
  - an implement-orchestrator skip;
  - a release-deploy never-bind rule.
- **Research-pipeline.** feature-design gains the route and misroute guard.
  epic-design is unchanged, because controllers are features.
- **Documentation.** The tag convention is in `.work/CONVENTIONS.md`, and the
  fork-patch record is in `docs/project-navigation.md`.
- **Verification.** These tests pass: `convert-content-integrity`,
  `agent-metadata`, `convert-install-routing`, `test_prompt_context` and
  research-pipeline `skill-portability`.
