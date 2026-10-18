---
id: feature-methodology-review-decomposition
kind: feature
stage: review
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
scale question to the surrounding methodology review. Andrew subsequently authorized
implementation by asking to keep going on methodology-review, including the selector,
child-to-parent reporting and resume/stop rules. Publication and installation remain
outside this feature's scope.

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
judgments within that direction. The follow-up instruction authorizes implementing
the design and completing its validation and review.

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

## Implementation notes

- Execution: inline, one owner for the cohesive skill/reference contract. No
  exploratory or implementation fan-out is needed.
- Review weight: standard (default); one independent Claude feature review, then
  accepted corrections and host verification without a second review.
- Added the selector and linked review-decomposition reference, including child
  input/result fields, parent integration, shared root rounds and resume rules.
- Extended the existing record writing aid and aligned process/readme descriptions.
  Retained the public skill, Codex metadata, ARD ownership and existing exit outcomes.
- Validation: checkpoint forward tests and structural checks passed as recorded
  below. Independent standard feature review is next. These tests do not constitute
  a full live-project research and delivery pilot.
- Simplification: replaced the implicit landscape/component-study suggestion with
  explicit selection; no extra public skills, tracker schemas or research machinery.


## Verification evidence — 2026-10-18

Executed four isolated checkpoint scenarios on both Codex (native fresh-context
agent) and Claude Sonnet/high (peeragent fresh process). Each received only the
skill, directly linked references and the fixture requests below; no expected
answers, implementation design or prior test results. Neither ran external research,
changed project policy or bootstrapped a work substrate. This is forward execution
of the skill at bounded checkpoints, not a complete delegated research/adoption loop.

| Case | Observed Codex behavior | Observed Claude behavior |
| --- | --- | --- |
| 01: indivisible choice, broad evidence | Focused, unsplit; evidence requests remain research dimensions | Focused, unsplit; assessment not yet run |
| 02: independent methods, nested coordinated comparison | Program; coordinated customer-learning node with focused selection/interpretation children; other focused children | Initial run called the two comparisons lenses rather than explicit child assessments. Clarified that coordinated children may share one policy decision. A new process rerunning the unchanged input produced MR-001.1a/.1b child assessments feeding one MR-001.1 decision, under the program root. |
| 03: two clean children, incompatible recommendations | Parent cannot close; conflicting retention requirements; round 2 still in progress | Parent cannot close; conflict provisional pending fresh whole-scope assessment; 1 complete round, round 2 open |
| 04: resume with pending remedy and retained major risk | Preserved round 5, workflow-A pilot authority and deferred METH-002; no unnecessary split or repeated approval | Preserved the same limits, authorization and risk; no reset, no clean outcome and no repeated approval |

Case 04's shape differed (coordinated versus program) on an underspecified existing
cut. Both preserved the required authority, evidence and root-round invariants;
shape labels were not graded as fixed answers. Pre-assessment checkpoint status
also differed; neither host invented a completed assessment.

Claude initial job: `20261018T220102Z-c199627f`, terminal success. Targeted case-02
job after the clarification: `20261018T220427Z-2d8b9b6c`, terminal success. The driver
read the generated state files, including the targeted nested child table and
parent integration sequence; process success alone was not treated as correctness.
Codex forward worker: `/root/methodology_forward_codex`, completed; all four state
artifacts inspected. Temporary fixture outputs were outside the repository and are
not shipped. Exact requests and output fingerprints follow for reproducibility.

Structural verification after the clarification:

- `uv run --no-project --with PyYAML python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py plugins/research-pipeline/skills/methodology-review` — pass.
- `uv run --no-project --with PyYAML sh plugins/research-pipeline/scripts/tests/skill-portability.test.sh` — pass, including affected portable skill/Codex metadata shape.
- Local relative file targets resolve; main skill 281 lines, decomposition reference
  135, record reference 157; host-only dispatch names absent — pass.
- `git diff --check` — pass. No executable, hook, manifest, dependency or version
  changes requiring unrelated runtime suites. There is no repository CI configured.

### Forward-test requests and output fingerprints

#### case-01

```text
# Request
Use methodology-review to plan the next checkpoint for one decision: whether this team should replace its manual verification step with an automated gate. The policy is indivisible for this team. Evidence is needed about coverage, false negatives, recovery and operator burden. Those are evidence dimensions, not independently changeable policies. The operator has authorized investigation only, with mixed scope and standard research verification. No research has been performed yet. Record the review shape, useful boundaries, evidence requests and next step. Do not run the research in this checkpoint.
```

codex output SHA-256: `aab28948b3eb62a2a0c5c41f2134196b8e5e4c8e58095b4cc1f00c3db64cbcc9`.

claude output SHA-256: `13c2499a7eb2740c705fa4a86f3045f2cb94c1ddd29170bd9ac4511b3c5bc665`.

#### case-02

```text
# Request
Use methodology-review to organize a review of this project's approach to customer learning, release planning and knowledge capture. Each has a separate owner, a separately changeable policy and its own rollout schedule. The shared outcome is learning reliably without slowing delivery. Within customer learning, interview selection and interpretation need separate comparisons before one coordinated learning-policy decision. Release planning is one bounded choice. Knowledge capture has current evidence ready to reuse. Investigation is authorized; project changes are not. Mixed scope and standard research verification are agreed. There is no .work directory or other established tracker. Record the first checkpoint and how component results will be used. Do not run research or create a delivery substrate during this checkpoint.
```

codex output SHA-256: `4360450fadbfee8e2bf27c987c8f68ff0b49b2a754c453571b3685efd3cc61d1`.

claude output SHA-256: `a59bdc9e944f16d41af658ca9aba52244cb53b5d81477ebfaccea18a4d0face6`.

claude-targeted output SHA-256: `66eeb67a55e43f5ecd06a30921a4661d7124a7bc28f93595587dfba37f315e33`.

#### case-03

```text
# Request
Resume methodology review R3 from the supplied state and component reports. Both child assessors reported clean. Can the parent close? Record the next checkpoint using the existing evidence. Do not perform new research or implementation.

# Existing state
Root: R3. Baseline: fixture-v1. Completed root rounds: 1; in-progress root round: 2; shared limit: 5.
Charter: choose a response-record handling method that stays within storage constraints and supports correction of interpretation errors for a month. Two related policy components were assessed separately. No operator decisions authorize applying either recommendation yet. The supplied reports are current verified fixture evidence, but there has been no fresh parent assessment of their combined effects.

# Child R3-A report
Scope: storage burden. Current baseline fixture-v1. Assessor reports clean within child scope. Recommends deleting every raw response after 24 hours. The provided measurements support the storage benefit. No parent interaction assessment was performed.

# Child R3-B report
Scope: correction of interpretation errors. Current baseline fixture-v1. Assessor reports clean within child scope. Recommends re-reading raw responses during correction requests up to 30 days after receipt. The provided process trial supports this correction method. No parent interaction assessment was performed.
```

codex output SHA-256: `f1cc6cb722cbcafa17be418ab31c1c864305cbadabd2813667fcbb883b3c0bd8`.

claude output SHA-256: `094b9d92e6b74c8c6f8da127849e9a9f8d3545a80fbd4e65b117bad3bba6e0b5`.

#### case-04

```text
# Request
Resume methodology review R4 and record the next checkpoint. You may split the existing validation question into performance and recovery questions if useful. Continue within the already authorized pilot; do not ask to approve it again. This checkpoint is investigation/coordination only, not the implementation itself.

# Existing state
Root R4; baseline fixture-v1; four complete root assessment rounds; fifth round in progress; shared limit five. Only a documentation typo changed since the previous checkpoint.
Coverage includes delivery validation and evidence retention. Validation child R4-A has a finished, verified research engagement. Its proposed remedy is not applied yet. The operator authorized a pilot in workflow A only; the delivery item remains pending. The research completion did not contain a methodology assessor report. Retention child R4-B has finding METH-002, a supported major risk, explicitly deferred by the operator with no remedy authorized. The operator has not elected to end the root review. Existing criteria and research settings remain valid. A newly split child would have no prior local history.
```

codex output SHA-256: `e12d26838cd48d889092ad8572d1002210ae0ce632c8e4dd9ddc60c1841f456a`.

claude output SHA-256: `f81a3bb6cec0543a9673e88f7c4337016f79f8634498f0a6f9356c5d6872a238`.
