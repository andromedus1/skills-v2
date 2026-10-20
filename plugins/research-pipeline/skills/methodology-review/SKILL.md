---
name: methodology-review
description: >
  Compare a project's methods, workflows and assumptions with relevant products,
  projects and research. Map the domain's alternative approaches, challenge the
  sample for missing families, assess a whole project or selected component,
  decompose broader reviews into useful component reviews, re-run closed reviews
  over time, and iterate through operator decisions and fresh assessment. Use for
  methodological assessment or comparison with prior art, not ordinary code review
  or documentation consistency checks.
---

# Methodology Review

Assess whether the project's approach serves its intended outcomes against external
alternatives and common scenarios; current architecture and procedures are
hypotheses, not criteria every alternative must meet.

This skill owns comparison framing and the operator-adjudicated loop.
`agentic-research:research-orchestrator` owns grounded research, registration,
source records, refresh and verification; nothing here replaces or copies that
stack. Read the [build process](../../docs/build-process.md) and
[research composition](../../docs/research-composition.md). Without Agentic
Research, report the missing prerequisite and stop; never invent a substitute.

## Scope and authority

Accept a project, component, workflow or review record; with none, use the active
project's instructions, asking only if the boundary is unclear. Discover components;
assume no domain, folder count, stack, product list or deep pass for each.

Invocation authorizes only investigation and review artifacts. The operator decides
changes to the project's methods, requirements, contracts, architecture, code or
operating policy; routine research choices and corrections to the review's own
analysis are the agent's. Reuse prior explicit authorization and settled answers
within their stated scope.

Before research, resolve one durable root loop record: in Agile Workflow, a matching
controller item, or one minted directly (not via `agile-workflow:scope`) from the
[controller skeleton](references/review-record.md#agile-workflow-controller), tagged
`methodology-review-controller` without a `research` tag or `research_dials`
(separately commissioned research items own their engagements, whose completion never
closes it; the tag routes the item here, never to design or implementation); else an
established decision tracker, never mixing trackers; else root `methodology-review-state.md` with existing
planning frontmatter, never under `.research/` and without bootstrapping `.work/`.
Give concurrent reviews named sections; never overwrite another. The record holds
operator decisions, delivery links and dated full-scope assessments; research
comparisons and verification stay in Agentic Research's artifact map, linked from
it. Never rewrite a completed research report to reflect decisions or implementation
status. Consult [review-record.md](references/review-record.md) when first recording the
charter, findings or decisions (existing schemas, no new ARD tier).

## 0. Map the domain

Before chartering comparisons, build or reuse a **domain map**, the structured view of
the reviewed topic that the sample, research facets and coverage report all reference
([domain-map.md](references/domain-map.md)). Its halves have different owners:

- **Alternative space** (research-owned): jobs and outcomes, decision dimensions,
  approach families in their own terms, scenarios, evidence by level and open
  questions. Commission it through `research-pipeline:scout` in domain-map mode,
  describing the topic generically; it is a refreshable landscape brief, never edited
  to reflect decisions.
- **Project mapping** (loop-record-owned): in-scope jobs and decisions, where the
  current method sits in the space, and the sample drawn from it.

Reuse a current map that covers the topic, such as a parent's, sibling's or
predecessor's, refreshing it only for a named coverage or freshness gap. A program maps
once at the root for every child.

## 1. Set a review charter

Read project intent, instructions, knowledge navigation, existing research, delivery
state and other reviews whose scope overlaps. Record the fields below. Ask the operator
only the **(operator)** fields not already settled; the host determines the rest from
evidence and records its basis.

- **(operator)** Users, jobs, outcomes, constraints and the decisions this review may
  change.
- **(operator)** Scope, project-wide or component-only coverage and deliberate
  exclusions; the host records the baseline revision/digests.
- Assumptions, disputed requirements and evidence that could change them; operator
  constraints versus inherited design choices. The operator confirms disputed ones.
- Overlapping reviews: a settled decision is a constraint; a pending one is an input
  this review neither re-adjudicates nor absorbs. Link it and exclude or depend on its
  scope; ask only if the overlap changes what this review may decide.
- Scenarios and criteria: outcome quality, evidence, uncertainty, human effort,
  correction/learning, operating burden and applicability.
- A sample of genuinely different approaches drawn from the map's families, with a
  simpler baseline when relevant; explain each consequential exclusion. Never author
  the sample from recall.
- Evidence feasibility for each decision: literature-settleable, experiment-needed or
  mixed, using existing research (a documented evidence absence counts). Propose an
  experiment track early for experiment-needed decisions rather than expecting
  sources to settle them.
- Expected effort: anticipated engagements and dispatches, fresh assessments and
  rounds. This is information for the operator, never a cap or a reason to trim
  coverage or verification depth.
- **(operator)** Confirmed research settings, completion criteria and round limit: propose mixed
  scope authority and standard verification unless context differs (the
  orchestrator settles its dials); default to at most five complete root assessment
  rounds including the first, changeable by the operator.
- Required research and delivery checks, owners and establishing evidence, then
  their actual outcomes and assessed inputs; missing reports or successful worker
  execution alone never satisfy a check
  ([build process §Completion](../../docs/build-process.md#completion)). Keep each
  owner's correction rules and limits; add no common retry loop.

Do not re-ask settled kickoff questions; expose material ambiguity before dependent
work. A suite landscape or pilot may help set boundaries but is never mandatory.

## 2. Map decisions and select the review shape

Map decisions, assumptions, shared constraints and scenarios before choosing a
shape. Alongside the domain's own decision dimensions, include **discovery**: what the
current method omits or underexplores relative to the map. Start unsplit; split only when distinct comparisons would improve a decision,
never for folder counts, topic breadth, research volume or distinct evidence domains
alone.

- **Focused review:** one bounded decision; no child reviews.
- **Coordinated review:** distinct methodological subquestions feed one combined
  operator decision and parent reassessment.
- **Review program:** independently adjudicable components with their own change
  schedules; each child also has its own decision and child-scope reassessment,
  within the root's shared rounds and limit.

These are shapes of one skill, not versions. Explain the chosen shape and coverage
limits; honor an explicit operator choice that fits the charter, surfacing a
consequential mismatch before dependent work. Each child repeats charter → map →
evidence → comparison in its smaller scope. Persist the cut, rationale, exclusions
and dependencies. Routine decomposition within authorized scope needs no new blanket
approval; changed scope or constraints do. For a split, uncertain boundary or
resumed multi-part review, first read
[review-decomposition.md](references/review-decomposition.md).

## Sample checkpoint (before depth research)

Before commissioning comparisons:

1. Compare the sample with the map and name the unsampled families and why.
2. Have a fresh-context assessor, with the project's cross-model preference when
   available, challenge the map and sample for missing families or framings using the
   [completeness-challenge brief](references/assessor-briefs.md#completeness-challenge).
   Its proposals are evidence. Add a missing family by refreshing the map through
   scout, never from host recall.
3. Present the operator with the map, sample, exclusions, challenge results,
   evidence-feasibility triage and expected effort; record the actual response.

Repeat the challenge only when the map or sample changes materially. Until the
operator responds, this is a checkpoint awaiting a decision; no depth research starts.

## 3. Research and compare

Per review unit, name the evidence gap and the decision a finding could change.
Reuse sufficient current research under the engine's source/refresh rules; use
`research-pipeline:scout` for missing landscape coverage, not every round.
Commission comparisons via `agentic-research:research-orchestrator` with a
[commission packet](references/commission-packet.md): charter fields, map and sample,
evidence levels, scenarios, default dials and a required non-recommending
decision-relevance section. Every dispatch references the packet by path rather than
restating it; the engine discovers facets. Research owns comparisons in each
alternative's own terms and their evidence; the loop record owns coverage mapping,
transfer and proposals. If the operator widens scope mid-review, record a new baseline
and extend a running engagement only within its registered scope authority; otherwise
commission a linked new engagement. Review
shape sets neither research shape nor rigor (a focused review may need a large
campaign). `research-pipeline:research-program` is for separately commissioned
engagements and their dependencies, not for review children as such. Preserve
confirmed settings within their agreed scope.

Ask the research to:

- Describe alternatives in their own categories, including other configurations,
  deliberately omitted work and capabilities beyond our inventory, leaving their
  mapping onto ours to the loop record; a longer feature list is not a better method.
- Compare the same user job under stated constraints, noting audience, scale and
  purpose differences; a documentation gap is unknown unless absence is evidenced,
  and advertised capability is not execution evidence.
- Trace representative scenarios through acquisition, interpretation, evaluation,
  human judgment, action and correction as applicable to the domain, including failure/contrary cases and
  maintenance cost.
- Separate designed, documented, demonstrated and independently measured behavior;
  propose decisive experiments where sources cannot settle a consequential choice,
  never inferring successful operation from coherent documents.
- Seek evidence against both the current approach and proposed replacements,
  keeping useful guarantees while making their benefit and burden testable.

Never send private project content to public searches or external services. Source
acquisition is research; paid trials, deployments and resource-consuming
experiments need their own authorized scope.

## 4. Produce findings and a decision packet

Finish the engagement's required verification before calling recommendations
verified. Seed it with sample bias, comparability, source support and criteria
favoring the current design; under adversarial-read rigor these are lenses for that
orchestrator-owned pass, not a second verification stack. A clean exit still needs
the step 6 assessment, even at floor rigor; one pass serves both only if its actual
scope and structured result satisfy both. Refresh the project's existing knowledge
index after new research artifacts; never bootstrap one elsewhere.

Before anything reaches the operator: check each draft finding against the current
artifact text it relies on and drop or correct any misreading; then have the fresh
assessor of [step 6](#6-fresh-reassessment-and-exit) assess the draft findings with the
[assessment brief](references/assessor-briefs.md#assessment); then present the packet
with the assessor's withdrawals and downgrades.

Deduplicate findings under [stable IDs](references/review-record.md#finding-record)
and separate methodological findings from incidental doc/code defects. A **major**
finding has evidence of a material threat to an agreed outcome or consequential
decision: an invalid method, missing necessary capability, unjustified burden or
decision-blocking uncertainty; state its consequence and uncertainty. A plausible
alternative, extra feature or stylistic preference is not major by itself; missing
evidence can require an experiment without showing the method is wrong.

For each finding, present the source-grounded observation, affected outcome,
strongest counterargument, plausible choices (including retention), recommended next
action, tradeoffs, deciding evidence and exactly which project change or experiment
each choice authorizes. Present one manageable
[decision batch](references/review-record.md#decision-packet), unresolved major
findings first; keep smaller observations without letting them drive the loop. A
split review [integrates](references/review-decomposition.md#integrate-at-the-parent)
child results before claiming a parent outcome.

## 5. Operator adjudication and authorized action

Ask the operator to accept, modify, reject or defer a proposal, or request more
evidence; record the actual response, rationale, selected scope and authorized next
action. Changed criteria or scope get a new recorded baseline without silently
erasing earlier-scope findings.

- Silence, elapsed time and a pending asynchronous question are not approval.
- A decision authorizes only what it answers: a partial answer covers only its
  portion, and a decision on one finding grants nothing for later findings or
  changes. Meanwhile continue independent or authorized work.
- Agreeing with a diagnosis or direction does not authorize implementing it.
  Distinguish adoption only, further research, filing work and applying a specified
  change; ask only where that authorization is missing.
- To file research-derived work on explicit request, invoke
  `agentic-research:research-handoff` with the source artifact, authorized finding
  IDs, exact decisions and destination, honoring its confirmation contract. First
  check the loop record and existing items for the same review/finding IDs, even
  under a refreshed research slug, and reuse matches.
- Before emitted work reaches design, implementation or autopilot, align its
  operative brief and acceptance scope with the actual decision and add the stable
  IDs, exact authorized next action, a backlink to the loop-record decision and the
  research-origin link; a broader original proposal may stay only as labeled
  background. Link the item from the loop record. These are work-side edits; never
  alter research to match a decision.
- Deliver authorized changes through the project's workflow, bypassing none of its
  design, implementation, testing, review or deployment requirements, and record the
  resulting revision and evidence. If delivery happens elsewhere or later,
  checkpoint as awaiting change and resume when its evidence exists.

When the operator declines or changes a path that other findings or recommendations
depended on, such as a measurement, an experiment or another remedy, re-present those
dependent findings on the changed basis in the same batch. Authorized remedies sharing a
delivery surface may be bundled into one delivery item that keeps each finding ID and
its exact authorization.

Rejecting or deferring neither falsifies a proposal's evidence nor verifies a
remedy; record the retained risk, rationale and any revisit trigger. Do not re-ask
on an unchanged baseline; reopen only for materially new evidence, changed
constraints or an explicit operator request. Correct a false finding when evidence
warrants, however popular its proposal.

## 6. Fresh reassessment and exit

After an authorized change or deciding research, reassess the **whole agreed review
scope**, including cross-component consequences, regressions and new major findings.
A component-only charter stays component-only; a full-project charter must not
shrink to edited files. Reuse sufficient current sources, refresh affected claims
through the orchestrator, and restart discovery only for a named coverage or
freshness gap.

Use a fresh-context assessor, with the project's cross-model preference when
available. Supply the charter, current project evidence, source-grounded comparisons
and exact operator decisions; never prescribe a verdict. It assesses current methods
against the charter as well as earlier remedies, reporting each finding status
([assessment report](references/review-record.md#assessment-report)). Store its
dated report in the loop record with the research and delivery evidence it consumed.
A finding resting on an external claim absent from verified research stays
provisional, and justifies no change, until the orchestrator verifies the claim; a
consequential provisional concern blocks a clean exit. With no changes required, an
already independent initial assessment can be the exit report. A parent assessor
also weighs child assessments, coverage and baselines for combined effects; all
children passing is insufficient.

The assessment reports coverage against the domain map: families compared, excluded
by the operator with reasons, and unexamined. Unexamined families bearing on an
in-scope decision are listed in the assessment and exit report but do not by
themselves block a clean exit. It also reports actual effort beside the charter
estimate.

Read the exit from that assessment, not the author's confidence or a targeted grep;
a bounded review never proves universal quality. When several outcomes apply, report
every finding's status; the highest-ranked outcome is primary.

| Rank | Outcome | Condition → next action |
|---|---|---|
| 1 on explicit operator stop | **Stopped with retained risks** (**Incomplete** if none) | Operator stops or retains/defers a material issue → list those findings and revisit conditions; dispositioned, not clean. |
| 2 | **Awaiting decision** | A choice needed for progress is unanswered → present the decision packet and checkpoint; no dependent changes. |
| 3 | **Awaiting change or evidence** | An accepted direction lacks a verified remedy, or an authorized experiment/delivery is pending → link the owner/item/evidence needed; not resolved. |
| 4 | **Incomplete** | Required coverage/verification is unavailable, the round limit is reached, or an unchanged round would add no evidence or authorized progress → report the limitation and concrete next step; never manufacture convergence. |
| 5 | **Clean within reviewed scope** | Fresh full-scope assessment of the current baseline: zero unresolved major findings, counting retained/deferred ones, and all required checks pass → report minor observations and coverage limits. |

A root round ends when a fresh parent assessment evaluates the whole charter from
available verified comparisons, returned child checkpoints and explicit coverage
gaps; it counts even if its outcome is pending or incomplete. Persist the count,
baseline and pending checkpoints. Children share the limit; creating, splitting,
re-cutting, reshaping or resuming a review never grants another allowance or resets
the count. Never repeat an unchanged round, lower severities or silently exclude
scope to meet the exit bar, or widen the research question indefinitely. At the
limit with clean conditions unmet, report Incomplete or the more specific
awaiting/stopped outcome, never clean; only the operator can extend the limit.
Paused or waiting portions do not block unrelated authorized work.

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

## Resume and report

To resume, use the supplied record path, else the matching active
`methodology-review` item or root `methodology-review-state.md`; follow a child
record's root backlink before dispatch; recover a closed review's record through
retention conventions; if several match, ask which scope. Read the current revision
and linked research, reconcile intervening changes with the last charter, preserve
decisions and finding IDs, and identify the next unfulfilled step. Never infer
approval from an item's presence or its research engagement's completion. Split
reviews follow the [resume rules](references/review-decomposition.md#rounds-stopping-and-resume).

Report the assessed scope/baseline, approaches sampled and map coverage, expected
versus actual effort, major findings by status,
operator decisions, authorized changes and verification, unresolved risks and exact
exit reason, linking research outputs and the operational record. Keep the result
usable without an implementation or a tracked work substrate.
