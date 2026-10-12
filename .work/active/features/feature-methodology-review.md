---
id: feature-methodology-review
kind: feature
stage: done
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

## Implementation and structural verification — 2026-10-12

Implemented the shared methodology-review skill, focused comparison/decision-record
reference and Codex presentation metadata. Updated the plugin README, root README,
research-composition and build-process entrypoints. Registered the new metadata in
the existing portability test; no new test that mirrors skill wording was added.

Validation passed: skill-creator quick_validate; existing skill-portability test;
Claude/Codex manifest version/discovery and marketplace resolution parity; Codex
presentation/invocation fields; 12 local links across touched documentation; Git
whitespace check. System Python lacked PyYAML, so checks ran in an isolated temporary
venv with PyYAML rather than modifying project dependencies.

An isolated behavioral continuation exercise covers four synthetic nonsoftware
projects. One cross-model feature review follows the standard single-pass policy.
Their outcomes and host dispositions will be recorded below. No release/version bump
or change to installed caches has occurred.

## Behavioral continuation checks — 2026-10-12

A fresh-context native agent used the skill against four isolated synthetic
nonsoftware projects in a temporary directory. It received requests, current process,
checkpoint and completed assessment records, without expected answers. It performed
the next permitted actions rather than reviewing the instructions.

| Case | Observed behavior |
|---|---|
| Editorial, partial approval | Applied only the independent factual-check change. Left the separate source-sharing decision unanswered, and did not claim the applied change independently verified. Preserved round 1/5. |
| Volunteer roster, rejected remedy | Retained weekly updates and the supported major risk, recorded the rejection rationale and revisit trigger, stopped with retained risks. Preserved round 2/5. |
| Planning, exhausted limit | Kept the experiment unauthorized and major finding open, reported awaiting decision at 5/5, required an extension before another assessment. |
| Editorial, supplied clean assessment | Closed clean within the specified scope from the independent full-scope evidence; retained minor observations and excluded live effectiveness. Preserved round 2/5. |

The host compared file digests: only the authorized editorial process and the four
checkpoint records changed; all source requests and assessment snapshots remained
unchanged. Result links resolved. This tests continuation/authority/exit behavior,
not fresh web acquisition or real-world methodological effectiveness. Fresh review
was unavailable inside the offline fixtures and was reported as pending, not invented.

## Review (2026-10-12)

**Independent verdict**: Request changes. Claude reviewed through the installed
peeragent wrapper, job `20261012T140425Z-9cd308a9`, terminal status success. It was
instructed not to delegate back. Effective weight: standard, one independent pass;
the host owns correction and verification without another independent pass.

**Host closure**: Approve after verified inline corrections. No unresolved blockers.
The independent verdict remains the original result; no claim is made that Claude
reviewed or approved the corrected snapshot.

| Accepted finding | Disposition and verification |
|---|---|
| Loop record location/ownership and metadata were underspecified | Fixed inline. Specify a matching Agile Workflow controller separate from research engagements, existing alternate trackers, or a fixed root fallback outside `.research/`. Define assessment storage and discovery, including archived records. The fallback frontmatter passes the existing index validator in schema v1 and v2 modes. |
| Narrowed operator decisions could be lost in research handoff | Fixed inline. Emission receives exact decisions; reconcile operative brief/acceptance before downstream dispatch; preserve review/finding IDs, decision backlink, research origin and reciprocal links; deduplicate across research refreshes. A focused behavioral continuation verified a broad emitted proposal becomes only the authorized two-week newsletter pilot. |

**Additional comments addressed inline**: refresh an existing knowledge index after
research; route comparison challenge lenses through the orchestrator without a second
verification stack; verify new external claims introduced by an assessor; define exit
precedence; expose the skill in the overview and adopter template. No rejected or
deferred findings, and no separate repair items were needed for these prose edits.

The focused post-fix continuation reused the same fresh-context test agent in a new
isolated fixture. It received the current skill, saved review record, synthetic verified
comparison, operator instruction and an already emitted overbroad item. It narrowed
the item, preserved `stage: drafting`, kept the two-workflow review scope and unresolved
finding, recorded awaiting change/evidence at 1/5, and did not implement or emit another
item. Host checks confirmed the research digest was unchanged, the item identities and
links were correct, and no duplicate item was created. This is behavioral verification
of the fix, not another independent feature review or live research validation.

Final checks passed: skill-creator quick_validate; existing plugin portability test;
Claude/Codex manifest parity and both marketplace discovery paths; Codex UI metadata;
five new/changed local Markdown links; standalone record compatibility with the existing
index's v1/v2 schema; targeted handoff continuation checks; and Git whitespace check.
All acceptance criteria are met for local skill authoring. A real-project research
pilot remains a future use of the skill, not evidence claimed by this feature.

No plugin version, installed cache, remote branch or adopter project was changed.
