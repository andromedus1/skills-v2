---
id: feature-methodology-review
kind: feature
stage: implementing
tags: [prose, research-pipeline]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-12
updated: 2026-10-12
---

# Reusable methodology review with operator-adjudicated iteration

## Brief

Andrew requested a reusable skill in skills-v2 for comparing a project's methods,
workflows and assumptions with relevant products, projects and research. It should
support whole-project and component review, scout alternative configurations, and
iterate like doc-review until no major findings remain, while Andrew adjudicates
project changes and decisions. The request generalizes an earlier review proposal;
no private project content is part of this package.

The deliverable is `research-pipeline:methodology-review`: portable instructions,
one focused reference for the comparison/decision record, Codex presentation
metadata, and affected plugin/process documentation. No research campaign on an
adopter project, automatic installation, version publication or remote push is
commissioned here.

## Strategic decisions

- Generalize over projects, components, workflows and disciplines; discover the
  scope rather than hard-code a component count, domain or vendor shortlist.
- The agent owns source research and analytical corrections. The operator owns
  project-method changes, adoption, accepted risk and scope changes.
- Compose the existing Scout and Agentic Research workflows; no copied research
  engine, discipline, validator or competing substrate.
- Separate findings, operator decisions and verified remediation. Declined,
  deferred or merely accepted findings do not become resolved by bookkeeping.
- A fresh full-scope methodological assessment must support a clean exit after
  changes. Research coverage is bounded; stopping with decisions/risks outstanding
  must remain distinct from clean completion.
- Scope is authoring and local validation. Packaging uses the current shared skill
  directory in both manifests; version release remains separate.

## Simplification opportunity

Replace bespoke review prompts with one reusable process overlay. Reuse existing
research, delivery, handoff and reviewer routes rather than another loop engine.
Do not change doc-review's separate consistency/autofix contract.

## Acceptance

- Suite/project and single-component use are discoverable through a precise skill
  description; this is not triggered by ordinary code/doc consistency reviews.
- The landscape does not require alternatives to match the project's current
  taxonomy. Common scenarios compare outcomes, evidence and burden fairly.
- Major findings have explicit consequence and supporting evidence; evidence gaps
  can block consequential decisions without being presented as proved defects.
- Operator adjudication is required before project changes, with partial answers,
  prior authorization and no-response behavior explicit.
- Reassessment checks the whole agreed scope and regressions; stable finding IDs,
  evidence pointers and decisions survive resume. No duplicate work emission.
- Clean, awaiting-decision, awaiting-change, stopped-with-risks and incomplete
  outcomes have distinct meanings. A bounded loop cannot silently lower severity,
  shrink scope or count rejected findings as fixed to manufacture convergence.
- Research execution and handoff remain owned by Agentic Research. Existing corpus
  output/refresh conventions and work-state ownership are preserved.
- Validate frontmatter and Codex metadata, plugin discovery/parity, relevant links,
  and realistic loop behavior; receive one independent feature review.

## Outline

1. Entry point: intent/prerequisites, charter, research comparison, decision gate,
   authorized delivery, fresh reassessment, convergence/resume.
2. Reference: reusable comparison/finding/decision/report fields, without defining
   a second research schema.
3. Plugin README, research-composition and build-process routing links.

## Implementation notes

- Execution: inline prose authoring; no production code or hook changes.
- Review weight: standard, one independent pass with host correction/verification.
- The current fork instructions/README override inherited Workbench-centric meta
  docs. Those unrelated existing differences are outside this feature.
