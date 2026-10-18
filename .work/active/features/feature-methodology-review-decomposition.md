---
id: feature-methodology-review-decomposition
kind: feature
stage: implementing
tags: [methodology-review, research-pipeline]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-18
updated: 2026-10-18
research_refs: [research-package-boundary]
---

# Adaptive decomposition for the whole methodology review

## Brief

Extend methodology-review so it can map a topic into reviewable decisions, choose
an appropriate execution shape, and apply the same comparison/adjudication/
reassessment cycle within component scopes before assessing the whole. Each scope
commissions its own proportionate Agentic Research engagement when evidence is
needed. Review decomposition and research decomposition remain distinct.

Andrew confirmed: "Whole review, with adaptive research inside each part."
This promotes idea-methodology-research-depth and extends its original research-
scale question to the surrounding methodology review. Current work is the concrete
design proposal; it does not implement, publish or install the skill change.

## Strategic decisions

- The repeated pattern covers the whole review, not just research fan-out.
- Agentic Research retains research decomposition, attestations, synthesis and
  verification. Pipeline owns the methodological comparison and operator loop.
- Preserve the existing single entrypoint, durable record, operator decisions,
  fresh reassessment and explicit exit outcomes.
- The prior package assessment informs this design; package merger, dependency
  installation and resolver repairs are outside this feature.

## Scope and sizing

Medium, cohesive extension of the existing methodology-review controller and
linked writing aids. Genuine orchestration and authority-boundary decisions make
this feature-design work rather than a prose-only rewrite. No new package,
research schema, tracker or delivery state machine is proposed. No unfinished
prerequisite blocks design; the initial methodology-review feature is archived.

## Simplification opportunity

One entrypoint and one repeated review protocol replace implicit, scattered
choices about review size. Reuse the existing records and engine. Avoid separate
light/deep/program skills, a fixed hierarchy of folder reviews, duplicated research
verification, or one work item per analytical facet.

## Acceptance

- Decompose decisions before selecting a review execution shape.
- Distinguish one coupled decision, several facets of one decision, and independently
  adjudicable component decisions.
- Repeat the review protocol where useful without automatic exhaustive recursion.
- Specify child inputs/outputs, parent integration, authority, stopping and resume.
- Keep research shape and verification rigor independent of review topology.
- Preserve pending/retained risks; child completion cannot imply parent convergence.
- Validate with representative scenarios and portable skill checks before delivery.

## Design decisions

The directional pass is complete: Andrew selected whole-review decomposition with
adaptive research within each part. Remaining choices below are reversible design
judgments within that direction. No implementation authorization is inferred from
the design discussion; `implementing` records design readiness in the substrate.

- Keep one public `methodology-review` entrypoint; infer the shape from the mapped
  questions and dependencies, while honoring an explicit operator choice that
  fits the charter. Explain the choice and material limitations.
- Use three descriptive shapes, not three skill versions: focused review,
  coordinated review, and review program. Each runs the same review protocol.
- Choose review boundaries from decisions, assumptions and common scenarios.
  Folder structure is a discovery aid, not the decomposition rule.
- Review structure, research structure and verification rigor are separate choices.
  A focused methodology review can require a substantial research campaign.
- Keep operational coordination in the existing review record/work substrate;
  keep research analysis and source verification in the existing ARD substrate.

## Grounding and scope probe

Read the current skill, review-record reference, research composition, package
assessment, orchestrator and ARD decomposition contract. The relevant source area
is bounded; direct reading was sufficient and no exploration agent was needed.
The existing skill already supplies chartering, operator adjudication, stable
findings, separate research commissioning and fresh full-scope reassessment.
These are retained contracts, not new capabilities claimed by this feature.

No application UI or new library/API is involved. No code pattern from the local
patterns catalog needs expansion. The new contract is prompt-driven review
orchestration, so its interfaces are explicit Markdown fields and role briefs,
not invented TypeScript types or a machine-readable schema.

## Architectural choice

| Approach | Benefit | Cost | Decision |
| --- | --- | --- | --- |
| One adaptive entrypoint and repeated review protocol | Preserves discoverability and shares authority/exit behavior | Requires a clear decomposition step and parent integration | Selected |
| Separate focused/deep/program review skills | Explicit manual selection | Requires users to choose before discovery; risks drift among versions | Do not introduce |
| Research decomposition alone | Small instruction change | Leaves review decisions, child results and whole-scope reassessment uncoordinated | Does not satisfy Andrew's selected scope |

The repeated unit is: charter → map/decompose → obtain evidence → compare →
adjudicate → reassess. Children inherit applicable constraints and contribute to
their parent's question. The parent evaluates interactions and the original
outcomes; it does not merely concatenate child reports or average their verdicts.

### Decomposition before shape selection

Add a light orientation step between chartering and substantive research:

1. State the outcome and decisions this review could change. Read existing intent,
   prior findings, current methods and available evidence before proposing work.
2. Map the consequential methodological questions, assumptions and shared
   constraints. Identify which conclusions depend on other conclusions.
3. Try an unsplit review first. If useful distinctions would be lost, compare
   alternative cuts by decisions, end-to-end scenarios or components. Persist
   the chosen cut, its rationale and what it may omit. No fixed candidate quota
   is imposed on this operational step; ARD retains its own research requirements.
4. Select a shape using the table below. If a consequential boundary is unknown,
   commission a small bounded discovery engagement or ask the operator about
   intent; do not launch an exhaustive review to discover its own scope.
5. Revisit the cut only when new evidence or an authorized scope change warrants
   it. Preserve stable finding identities and map old coverage to the new cut.

| Shape | Selection rule | Execution |
| --- | --- | --- |
| Focused review | One bounded decision; separate child assessments would add little | Run the protocol inline for that scope |
| Coordinated review | Distinct methodological subquestions deserve their own comparisons but share an outcome and coordinated decision | Run bounded child assessments, then integrate evidence, conflicts and interactions at the parent |
| Review program | Components have independently adjudicable decisions, different evidence needs or distinct change/reassessment cycles | Coordinate child review loops and their dependencies; reassess the program's shared outcomes |

Apply the selection again inside a child only if a smaller review boundary adds
decision value. Do not force all children to the same shape or depth. Every split
must reduce scope and name the child's contribution. Shared questions have one
owner and referenced results, not duplicate child reviews. Keep tightly coupled
or mutually dependent choices together rather than manufacturing a dependency cycle.

### Child contract and parent integration — trickiest unit

Use these fields in the existing record body or delegated brief:

| Field | Contract |
| --- | --- |
| Review identity | Stable root and child IDs; parent reference and covered questions |
| Purpose | Child decision/question, affected outcome and contribution to parent |
| Charter | Baseline; included/excluded scope; inherited constraints; applicable criteria/scenarios |
| Coordination | Inputs and dependencies; shared-question owner; scope/round limits; next checkpoint |
| Authority | Investigation and recommendation scope; exact inherited decisions; changes still require applicable operator authorization |
| Research requests | Evidence gaps, decision relevance and references to independently registered engagements |
| Returned assessment | Coverage; stable findings; source/research references; uncertainty; contrary evidence; cross-boundary implications; existing exit outcome and unresolved obligations |

The parent must reconcile overlapping findings without erasing identities,
surface conflicts and incompatible recommendations, and test cross-component
scenarios. Any cross-source analytical synthesis goes through Agentic Research;
the parent operational assessment consumes verified results and records decisions.
A child summary is not a new source attestation. New external claims raised by
the parent remain provisional until the engine verifies them.

A child can finish its investigation while its parent awaits decisions, changes
or integration evidence. A child cannot authorize a project-wide change on behalf
of the root. Batch related operator decisions where their scope permits; do not
create repeated approval prompts for previously settled decisions.

### Research within every review unit

Before commissioning research, name the unresolved evidence question and what
finding would change the unit's decision. Reuse current, verified research where
sufficient. The engine chooses bounded versus decomposed research for one
engagement; separately commissioned decisions may use research-program coordination.
Scout fills landscape gaps. Review depth never mechanically sets research depth
or rigor. Preserve the engine's registration, kickoff, decomposition, citations,
verification and handoff rules by invocation, not copying them into this skill.

### Stopping, authority and resume

- Retain the existing root limit of five complete assessment rounds unless the
  operator sets another limit. Allocate child work within the root round/checkpoint;
  spawning or re-cutting a child does not grant a fresh five-round allowance.
- Stop splitting when it adds no distinct decision, the scope no longer shrinks,
  evidence is sufficient, or the agreed limits are reached. Surface remaining
  coverage as incomplete/awaiting evidence using the existing outcomes.
- Scope expansion and changes to consequential constraints return to the operator.
  Routine splitting inside an agreed review boundary does not create a new
  project-change authorization or require repeated blanket confirmation.
- Root clean exit still requires fresh assessment of the entire agreed scope,
  including interactions and retained/deferred major risks. Child clean exits do
  not substitute. A fresh pass may cover both levels when its actual inputs and
  recorded coverage satisfy both; avoid duplicating equivalent review passes.
- Resume from recorded baselines, coverage, child assessments, research references,
  actual decisions and pending obligations. Refresh affected evidence; do not
  repeat completed discovery merely because another context resumed the review.

## Implementation Units

### Unit 1: Review selection and repeated protocol

Files:
- `plugins/research-pipeline/skills/methodology-review/SKILL.md`
- `plugins/research-pipeline/skills/methodology-review/references/review-decomposition.md` (new)

Keep the main skill as entrypoint and authority/exit contract. Add the orientation
and selection step, link the reference directly, and put the decision table,
child/parent contract and bounded recursion guidance in that reference. Target
under 300 lines for the skill and under 200 for the reference. Preserve portable
frontmatter and existing Codex metadata unless the trigger description needs a
specific clarification; retain one public skill and implicit invocation policy.

Acceptance: the same instruction set handles all three shapes; a child has a
bounded purpose and explicit contribution; the parent assesses interactions;
research mechanics remain delegated; current authority and exit guarantees remain.

### Unit 2: Durable coordination and discovery

Files:
- `plugins/research-pipeline/skills/methodology-review/references/review-record.md`
- `plugins/research-pipeline/docs/research-composition.md`
- `plugins/research-pipeline/docs/build-process.md`
- `plugins/research-pipeline/README.md`

Extend the record writing aid with parent/child coverage, chosen shape/rationale,
shared-question ownership, root round/checkpoint and unresolved obligations. These
are body fields, not new frontmatter, tiers or stages. Small coordinated reviews
use named sections in one controller. If independently scheduled program reviews
need separate work items, those items own their operational state; the root links
them and does not duplicate their stages. The standalone fallback uses linked
sections in the existing `methodology-review-state.md`, without bootstrapping `.work/`.
Keep research commissioning items distinct from review controllers.

Update process descriptions to explain adaptive whole-review decomposition and
link to the single contract. Do not duplicate its decision table across docs.
Acceptance: interruptions and re-cutting preserve coverage, decisions and findings;
work/research ownership remains unambiguous in both substrate and standalone use.

### Unit 3: Behavioral evidence and portable validation

Use scenario prompts in the implementation record and capture observed decisions
and artifacts there. Avoid tests that merely assert phrases exist in SKILL.md.
Use the existing portability/metadata validators for structural contracts. Record
host/model and whether a case was executed or only inspected; a design walkthrough
does not establish runtime agent behavior.

## Implementation order and testing

Implement Unit 1 first, especially the child/parent contract, then Unit 2 and
scenario evaluation. One owner can deliver this cohesive change; no child delivery
stories or parallel implementation are warranted. The review nodes described by
the feature are runtime review scopes, not delivery stories for implementing it.

| Scenario | Required observable behavior |
| --- | --- |
| One narrow methodological choice | Focused review, no manufactured children |
| One coupled choice needing broad evidence | Focused review may commission deep research; research breadth alone does not create a review program |
| Several facets sharing a project outcome | Explain the cut; run bounded child assessments; parent evaluates interactions |
| Independently changeable project methods | Program with explicit dependencies and mixed child shapes, not one fixed depth everywhere |
| Children individually pass but recommendations conflict | Parent records unresolved interaction and cannot report clean convergence |
| Child completes research while remedy remains pending | Review stays awaiting decision/change; research completion cannot close it |
| Interrupted review with existing decisions | Resume without repeating adjudication or resetting round allowance |
| Excessive decomposition or ambiguous scope | Stop splitting; explain the uncovered question and use bounded discovery/clarification |
| Project without `.work/` | Use the existing fallback record and research contract; create no delivery substrate |

During implementation, run `scripts/tests/skill-portability.test.sh` from the
Research Pipeline plugin with PyYAML available, the available skill validator,
local-link checks and affected Claude/Codex metadata checks. Evaluate representative
behavior in fresh contexts on both hosts before claiming cross-host behavior.
Use proportionate independent feature review, then correct and verify accepted
findings. Regenerate knowledge discovery after work/document changes. Publication,
cache updates and version bumps remain outside scope.

## Risks and pre-mortem

- Highest uncertainty: a plausible decomposition can hide cross-component effects.
  Test the conflicting-children case first; if integration cannot explain the
  conflict, collapse coupled nodes into a coordinated review.
- Recursive ceremony can exceed its value. Start unsplit, require a distinct
  contribution, reuse evidence and share root limits; do not infer fan-out from
  topic size or folder counts.
- A reviewer could confuse verified research with an approved change. Keep the
  existing evidence/decision/remedy dimensions and separate commissioning items.
- Review-level decomposition might drift into a second research engine. Constrain
  it to methodological questions, decisions and coordination; invoke ARD for
  research facets, source acquisition, synthesis and verification.

## Design status

Design complete; implementation not started. No plugin source, manifest, installed
cache or research artifact changed in this design pass. The open empirical question
is whether the decomposition guidance selects useful boundaries in real cases;
the behavioral cases above are the next evidence to obtain.
