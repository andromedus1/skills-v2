---
id: feature-methodology-review-codex-pilot-revision
kind: feature
stage: drafting
tags: [methodology-review, research-pipeline, prose]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-26
---

# Methodology-review: revision from the Codex Knowledge pilot

## Brief

The Codex-driven repeat of the Knowledge methodology review (project-blueprint,
research-pipeline 0.6.0 / Agentic Research 0.10.0) closed **Stopped with retained
risks** after 24 dispatches and one root round, with modest incremental decision
yield. Its handoff names five candidate skill changes with behavioral acceptance
tests. This feature adjudicates them against current text, separates skill gaps
from host mistakes and ARD-owned source problems, delivers a small revision with
forward-scenario regression checks, and writes a bounded next-pilot plan in a
different domain. The goal is decision usefulness and proportional execution, not
family count, defect count or a Clean verdict.

Evidence (read-only, private checkout):
`~/dev/project-blueprint/data-knowledge-blueprint/.work/review-evidence/knowledge-methodology-review-2026-10-20-codex/`
— `skills-v2-handoff.md`, `pilot-lessons.md`, `pilot-log.md` (P01–P27),
`round1-lead-adjudication.md`, `round1-assessment-clarification.md`,
`predecessor-sample-crosswalk.md`.

Non-goals: restarting or editing the Knowledge review or its decisions, running
EX-1/EX-9, inspecting other Blueprint components, launching the next pilot,
publishing a plugin version, or copying ARD discipline into research-pipeline.

## Simplification opportunity

Prefer sharpening existing rules over new artifacts or gates. The sample
checkpoint's unconditional "absent from the map → refresh" remedy is replaced by a
decision-tied one, which removes an implied refresh/re-challenge loop rather than
adding a budget. No new mandatory report, schema field or verification layer.

## History

Created 2026-10-19 as `idea-blueprint-methodology-pilot`: Andrew's intended jobs
(domain-method review over time, suite and component review, scout pairing) and the
decision to pilot on project-blueprint's Knowledge component first. The first
pilot's findings were delivered by `feature-methodology-review-pilot-learnings`
(research-pipeline 0.6.0). The item stayed parked as the home for the Codex
repeat's findings; this feature files them.
