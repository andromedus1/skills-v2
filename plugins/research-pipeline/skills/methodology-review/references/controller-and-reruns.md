# Controller and re-runs

Use this reference when minting an Agile Workflow controller for a review, or when
repeating a closed review. The skill's [Scope and authority](../SKILL.md#scope-and-authority)
and [Re-run](../SKILL.md#re-run-and-longitudinal-review) sections own the rules; this file holds
the skeleton and the detailed re-run steps and fields.

## Contents

- [Agile Workflow controller](#agile-workflow-controller)
- [Re-run and longitudinal review](#re-run-and-longitudinal-review)
- [Re-run record](#re-run-record)

## Agile Workflow controller

Mint the controller directly, not through `agile-workflow:scope`, whose next step
routes to design. The `methodology-review-controller` tag routes the item back to this
skill and keeps it out of design, implementation and release binding. Add a topic tag
such as `methodology-review` only alongside it, never instead of it. The controller
stays at `drafting` while the review is open. On exit, move it to `done` under the
project's retention conventions.

```markdown
---
id: methodology-review-<scope-slug>
kind: feature
stage: drafting
tags: [methodology-review-controller]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Methodology review: <scope>

## Charter
<step 1 fields; (operator) answers with dates; baseline>

## Domain map
<alternative-space path and version; project mapping; sample; exclusions>

## Sample checkpoint
<challenge report link; operator response; expected effort>

## Commission packets
<one per review unit, or links>

## Rounds and assessments
<round count and limit; dated assessor reports; coverage; effort>

## Findings and decisions
<finding records; decision packets; actual operator responses>

## Delivery
<handoff items, revisions and evidence>

## Next step
<the next unfulfilled step, or the exit outcome>
```

Child review items in a program use the same skeleton, with `parent` linking the
root controller.

## Re-run and longitudinal review

Repeat a closed review under a revised skill, after time passes or after the method
changes by opening a new review linked to its predecessor; never reopen the closed
record.

- Give it a new review ID and record, linked to the predecessor's record and final
  assessment.
- Carry predecessor finding IDs forward as prior IDs; a persisting finding keeps its
  identity and new findings get new IDs.
- Start a fresh round count; the predecessor's limit and count do not carry over.
- Reuse its research and domain map under the engine's freshness rules, refreshing
  only named stale or missing coverage.
- Record a what-changed baseline: project revisions, skill version, decisions and
  delivery since, and expiring research.
- Compare outcomes with the predecessor in the report: operator corrections to the
  sample, effort, verification churn, decision yield and assessor withdrawals. This
  is evidence about the review method, not a verdict on the project.

## Re-run record

A re-run's record carries the predecessor's record and final-assessment links, the
mapping from prior finding IDs to current ones, a fresh round count, the reused
research and map versions with their freshness, and a what-changed baseline. Its
report compares outcomes with the predecessor's: operator corrections to the sample,
effort, verification churn, decision yield and assessor withdrawals. The closed
predecessor record is never edited, except to add a forward link.
