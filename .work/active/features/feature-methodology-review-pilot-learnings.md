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

**Start condition: met (2026-10-20).** The pilot completed both rounds and
closed. All findings are below. Andrew gated the component and suite rollout on
this revision, and plans to address it in a separate session.

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

**Research execution (added 2026-10-19, mid-pilot; F15–F17 are agentic-research)**

- **F15. The discipline inlining costs a lot.** The verbatim discipline bundle
  plus role brief was inlined into 9 dispatches: a large fixed cost. Consider a
  read-the-file handshake with a content-hash echo.
- **F16. One specialist cited short handles.** It produced 160 broken chains,
  which lint caught. The specialist role brief should state the full-handle
  citation form; dispatches that stated it had no breaks.
- **F17. Lint depends on the working directory.** Lint resolves `source_path`
  relative to the working directory, which gives false `unreachable-source`
  findings when run from `.research/`.
- **F18. Proposal ownership is blurry.** The research parent's "candidate
  transfer" column overlaps the review's step-4 findings, which reinforces F7.
  Decide which artifact owns proposals.

**Findings, assessment and verification (added 2026-10-19, end of round 1)**

- **F19. The order of assessment and the operator's decision packet is
  unspecified.** Should host draft findings be independently assessed *before*
  the operator sees the packet? The pilot did so and benefited (see F22). Make
  it explicit.
- **F20. No bundled assessor brief template.** The pilot host wrote it from
  scratch, from `review-record.md#assessment-report`.
- **F21 (M, agentic-research). The orchestrator's rigor table contradicts its
  own reachability rule.** The table shows `evaluate` only at `full`. The rule
  says `evaluate` "re-enters the floor of any cross-specialist synthesis". The
  host followed the table, skipped `evaluate` and closed early. The round-1
  cross-model assessor caught it.
- **F22 (positive). Independent assessment improved the packet.** The fresh
  cross-model assessor withdrew one host-proposed major finding (KMR-03) and
  downgraded another (KMR-02), each with exact project-text evidence. The
  layering of the review's assessment over the research gates worked.
- **F23 (M). An under-specified commission caused verification churn.** The
  commission did not require a decision-relevance section: evidence per
  decision, the adopt-if-an-alternative-wins conditional, and the next evidence.
  `evaluate` then failed for that reason. Adding the section created new claim
  surface, and qualifier drift needed two further gate passes (about 3 extra
  verifier runs). The commission packet (F9) should require that section from
  the first draft, explicitly non-recommending (see F7/F18).

**Delivery and round 2 (added 2026-10-20)**

- **F24 (agentic-research). No option to delegate a single facet.** The
  orchestrator's light path (one facet) requires authoring inline. After a
  long session the host had to delegate one specialist to protect its
  context. Add a "single delegated specialist" option (same discipline
  inlining and gates; no cross-synthesis, so `evaluate` stays unreachable).
- **F25 (positive, plus one gap). Operator decision handling worked.** The
  rules held: a decision authorizes only what it answers, a retained major
  blocks a clean exit, and adoption is not implementation. The gap: when the
  operator declines the measurement path that an assessor's recommendation
  depended on, the skill does not prompt the host to re-present the dependent
  findings. Here, KMR-03 depended on EX-1 measurement, and the host
  re-presented it manually.
- **F26. No rule for bundling remedies.** `research-handoff` defaults to one
  item per finding. The pilot bundled three authorized lifecycle remedies into
  one `[prose]` delivery item. State that authorized remedies may be bundled
  by delivery surface.
- **F27 (M, agentic-research). The lint passes bare citations silently.** A
  brief with 207 bare `{N}` citations, without `[handle]`, linted as "0
  resolved · 0 broken", which is a clean-looking result that checked nothing.
  Flag bare numeric citations, or resolve them through `references.md`.
- **Round-2 outcome:** "Stopped with retained risks". The operator retained
  major KMR-01. Four remedies were verified, and one new minor finding
  emerged. The exit ranking handled a retained major plus pending minor work
  coherently.

## Pilot performance against intent (2026-10-20)

This section is the operator-facing assessment from the end of the Knowledge
pilot. The intent sources are:

- the skill's description;
- Andrew's intended jobs (`idea-blueprint-methodology-pilot`): review domain
  methods over time, cover the whole suite and each component, and pair with
  scout to surface alternatives and improvements;
- the rollout record: compare methods, workflows, assumptions and evidence
  with products, projects and research, with Andrew adjudicating;
- the October 12 research-depth question.

| Intended | Performance | Evidence |
|---|---|---|
| Treat current architecture as a hypothesis, not a criterion | **Met** | Verifiers repeatedly removed "designed" properties presented as evidence. The final synthesis labels the method undemonstrated throughout |
| Ground comparisons in verified research at the right depth (Oct 12 question) | **Met, at high cost** | A 7-facet campaign, a focused prior-art brief and a scout. Review shape and research shape decoupled cleanly. Verification caught real errors, but churned (F23) |
| Surface alternatives (scout pairing) | **Partly met** | The approach sample was host-authored. Andrew had to add gap discovery and an open scout mid-campaign (F11, F14). Scout acted as a late patch, not a front end |
| Produce decision-useful methodological findings | **Partly met** | Honest null: no alternative was shown better, and the method itself is unproven. Most decision value came from naming experiments and hardening the design. The central evidence gap was predictable at kickoff (prior research had found no economics evidence), but the skill has no step that asks whether sources can settle a decision (F28) |
| Operator-adjudicated loop with exact authority | **Met, a strength** | Decisions authorized only what they answered. A retained major blocked a clean exit. "Need more info" was handled, and agreement never became implementation |
| Fresh independent reassessment | **Met, a strength** | Cross-model assessors withdrew or downgraded host majors, caught a skipped research gate, and verified remedies in round 2 (F22) |
| Close the loop through delivery | **Met** | Decision → research-handoff items → delivered and reviewed → verified in round 2 |
| Component, then suite program (decomposition) | **Untested** | Component-only charter. The decomposition guidance and shared round limit were not exercised |
| Longitudinal re-review over time | **Untested, and the next test** | Andrew plans to repeat the Knowledge review with the revised skill. The skill has no guidance for re-running a closed review under a new skill version or after time passes (F29) |
| Proportionate effort, scalable to 6 components and the suite | **Not met** | About 20 agent dispatches plus resumes for one component, with no cost shown up front (F12). At this cost, a full rollout is impractical without reuse and budgets |

**New findings from this assessment:**

- **F28 (M). No evidence-feasibility triage.** At charter, the skill should
  classify each decision as literature-settleable or experiment-needed, and
  set expectations accordingly. Where prior research already shows an
  evidence absence, it should propose an experiment track early. This review
  spent a large campaign confirming that a key question cannot be settled from
  sources, and the operator then declined the experiment.
- **F29 (M). No re-run or longitudinal-review semantics.** Define how to
  repeat a closed review, either under a revised skill or after time has
  passed:
  - a new review id linked to its predecessor;
  - prior finding ids carried forward as prior IDs;
  - the round limit not inherited;
  - research reused under freshness rules, not re-commissioned;
  - an explicit "what changed since the prior review" baseline;
  - comparison of outcomes across versions as the skill's own validation.
- **F30. No host pre-check of draft findings.** Before the independent
  assessment, the host should verify each draft finding against the current
  artifact text. KMR-03 was a host misreading of the lifecycle; the assessor
  caught it, but a cheap pre-check would have avoided it.
- **F31. Program-scale economics.** For component-then-suite programs, the
  skill should plan a shared domain map and shared research across children,
  with lighter per-child research and an explicit budget per child. Repeating
  a full campaign per component does not scale.

**Suggested edit priorities for the skill revision:**

1. **Domain-map front end with sample-completeness check** (Andrew's
   direction; F11, F14). Pair it with F28's evidence-feasibility triage and
   F31's reuse across children.
2. **Cost and effort visibility with an operator budget** (F12, F31).
3. **Commission-packet template** including a non-recommending
   decision-relevance section, and a clear review/research ownership boundary
   (F7, F9, F10, F18, F23).
4. **Assessment ordering and bundled assessor brief** (F19, F20, F22), plus
   the host pre-check (F30).
5. **Loop-record mechanics** (F4, F5, F6): routing marker, skeleton, direct
   minting.
6. **Re-run and longitudinal semantics** (F29), with re-presentation of
   dependent findings (F25), remedy bundling (F26) and prior pending decisions
   (F1, F2).
7. **Agentic-research fixes, as a separate plugin change:** F8, F15, F16, F17,
   F21, F24, F27.

**Validation plan for the revised skill.** Repeat the Knowledge review under
the revised skill (Andrew's intent). Use it as the skill's own A/B test against
this pilot, comparing:

- whether the sample needed operator correction;
- agent count and cost against the stated budget;
- verification churn;
- the decision yield of the findings;
- whether the assessor withdrew any host findings.

Reuse the existing research under freshness rules. It is TTL-bounded to
2027-01-19/20.

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
