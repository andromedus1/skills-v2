---
id: feature-methodology-review-pilot-learnings
kind: feature
stage: drafting
tags: [methodology-review, research-pipeline]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Methodology-review: pilot learnings and a domain-map front end

## Brief

This feature revises `research-pipeline:methodology-review`, using findings from
its first real-domain use. That use was the project-blueprint Knowledge pilot,
which began on 2026-10-19 on research-pipeline 0.5.0 (see
`idea-blueprint-methodology-pilot`). The pilot showed two things about the
protocol:

- Its authority, loop and verification rules held up.
- Its coverage depended on the operator. The host wrote the approach sample. The
  operator had to ask, twice, for missing approach families (graph-based gap
  discovery, then an open scout) after five depth specialists had already
  finished.

Agent fan-out cost also stayed invisible to the operator until the agents
launched.

**Lead direction (Andrew, 2026-10-19).** Add a front end that uses Research
Pipeline and Agentic Research to gather context and build a structured conceptual
view of the review topic, a *domain map*, before chartering. Methodology-review
then targets that map rather than a host-authored sample:

- the charter's sample is drawn from the map;
- the research facets are cut against it;
- coverage and exit are measured against it.

The map may also be reusable across related reviews, for example per component
and then for a whole suite.

**Start condition.** Design waits for the pilot's round-1 assessment, so that
findings from the steps not yet exercised are included: findings and decision
packet, adjudication, fresh reassessment and exit. Append those findings below
before feature-design.

## Pilot findings (2026-10-19)

The full log is held in the private pilot project at
`blueprint-suite/review-evidence/2026-10-19-methodology-review-pilot/skill-feedback.md`.
It is optional context, not a prerequisite. The findings are summarized here so
this item stands alone. **(M)** marks material findings.

**Coverage and scale**

- **F11 (M). Sample completeness is unchecked.** §3 says to use scout "for missing
  landscape coverage", but no step tests whether a host-authored sample has gaps
  before depth research is commissioned. This is the problem the domain-map
  direction addresses.
- **F12 (M). Fan-out cost is invisible.** No expected agent count or effort is
  stated at the charter or at Checkpoint A, and there is no operator cap. The
  pilot ran 1 inventory agent and 7 specialists before verification and
  assessment.
- **F13. Mid-review scope expansion has no defined route.** It pushed the
  engagement to the orchestrator's program-scale threshold (7 facets). The seam
  between a review-level scope change and the engagement's decomposition (amend
  it, or start a new engagement) is unspecified.
- **F14. Discovery is missing from the decision prompts.** "Find what is missing
  or underexplored" is not among step 1's decision dimensions, alongside
  representation, maintenance, serving and evaluation.

**Kickoff and charter**

- **F1 (M). Overlapping prior reviews have no rule.** The skill gives no guidance
  for prior reviews whose operator decisions are still pending and overlap this
  review's scope. Is such a decision an input, a constraint, an exclusion, or
  something to absorb?
- **F2. Operator questions are not separated from host fields.** Step 1 lists
  charter contents but does not mark which are operator-owned kickoff questions
  and which the host determines.
- **F3 (positive).** The October 12 research-depth question is resolved: review
  shape sets neither research shape nor rigor, and scout is reserved for
  landscape gaps.

**Loop record**

- **F4 (M). The controller shows up as ready work.** The Agile Workflow
  controller record is a `kind: feature` at `stage: drafting`, so
  `work-view --ready` lists it as ready drafting work. Autopilot or feature-design
  would pick it up. No routing marker or stage convention exists, and
  agile-workflow has no `methodology-review` route. The pilot's workaround was a
  routing note in the item body.
- **F5. Minting the controller via `agile-workflow:scope` is heavyweight.** Its
  "Next" section routes the item to the design family, which reinforces F4.
- **F6. No body skeleton for Agile Workflow.** `review-record.md` gives fields
  but no item-body skeleton for the Agile Workflow case.

**Research commissioning**

- **F7. Project-specific transfer has no stated home.** `review-record.md` places
  comparison rows, including the project-specific "Transfer" field, in research
  artifacts. ARD's substrate test flags project framing that leaks into research.
  The skill should say where coverage mapping and transfer live: the research
  parent or the loop record.
- **F8 (agentic-research). No concurrency rule for the bibliography.** Parallel
  specialists share one append-only numbered `references.md`. The pilot host
  reserved number blocks and merged per-specialist refs files afterwards.
- **F9. No commission packet.** The charter's comparison fields, evidence levels
  and scenarios had to be restated in every dispatch. A methodology-review →
  orchestrator commission packet would cut drift and host effort, and it pairs
  naturally with the domain map.
- **F10. No default dials.** The skill gives no default `intent` or `output_kind`
  for review comparisons. The pilot chose `calibrate-external` with
  `[synthesis-brief, questions-list]`.

## Design questions for feature-design

- Should the domain map be a new Research Pipeline entry point, a step-0 phase of
  methodology-review, or a reuse of scout with a structured output kind (for
  example landscape plus vocabulary capture)? What does Agentic Research own
  versus the pipeline?
- Map shape: jobs and outcomes; decision dimensions; approach families described
  in their own terms; scenarios; known evidence by level; open questions. Is it a
  versioned analytical artifact that can be refreshed?
- How do the charter sample, facet cut, required coverage and exit test reference
  the map? Can a coverage gap against the map block a clean exit?
- How is the map reused across a review program (component → suite) without
  presupposing component boundaries?
- How should F12 be surfaced: as a cost or effort statement with an operator cap
  at the charter and at Checkpoint A?

## Simplification opportunity

- A domain map could replace the host-authored provisional sample and the
  per-dispatch restatement of charter fields (F9, F11).
- Resolving F4 at the routing level may remove the need for body routing notes.
- Do not add a second research engine. Map construction stays with Agentic
  Research under existing dials.
