---
id: feature-methodology-review-pilot-learnings
kind: feature
stage: review
tags: [methodology-review, research-pipeline]
parent: null
depends_on: [feature-agentic-research-pilot-fixes]
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-20
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

**Operator direction, Andrew, 2026-10-20 (end of pilot):**

- **Surfacing alternatives is the key step.** Improve it substantially. It is
  the lead objective of this revision, ahead of the other edit priorities.
- **Research strategies for breaking down alternatives.** This means
  systematic ways to decompose a solution space into genuinely different
  approaches, so that the review's sample is complete rather than authored
  from recall. Treat this as a **research question for the revision itself**,
  commissioned through Agentic Research. The plugin may already hold part of
  the answer in its primers. Attach the relevant primers to methodology-review,
  as other research-pipeline skills attach `first-principles.md` and
  `system-design.md` (for example feature-design, epic-design, architecture
  and ideate). Candidate primers to evaluate:
  - `docs/first-principles.md`: Open/decompose moves, such as Decompose to
    Fundamentals and Question Deeply, and Challenge moves, such as Invert and
    Seek Falsification;
  - `docs/oblique-strategies.md`: lateral moves for when the sample is stuck
    or over-constrained;
  - `docs/system-design.md`;
  - `docs/brief-first-principles-frameworks.md`;
  - `docs/first-principles-architecture.md`.

  Decide which moves apply at which step: domain map, charter sample,
  sample-completeness check, and per-facet research briefs.
- **Thoroughness over efficiency.** Andrew always prefers thoroughness. High
  agent cost is acceptable. F12/F31 are reframed accordingly: show cost as
  information for the operator, not as a budget cap, and never trade coverage
  or verification depth for cost. F31's reuse across a program is still
  wanted, for consistency and comparability rather than for savings.

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
| Effort visibility (operator preference: thoroughness over efficiency) | **Partly met** | About 20 agent dispatches plus resumes for one component. The cost is acceptable to Andrew, but it was not shown up front (F12). Thoroughness should not be reduced to save cost |

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
- **F31. Program-scale reuse.** For component-then-suite programs, the skill
  should plan a shared domain map and shared research across children, so
  children compare against one consistent alternative space. Per-child
  research then deepens where a child's decisions need it. The goal is
  consistency and comparability, not savings. Andrew prefers thoroughness over
  efficiency, so no per-child budget caps.

**Suggested edit priorities for the skill revision:**

1. **Surfacing alternatives: the lead objective (Andrew).**
   - A domain-map front end with a sample-completeness check (F11, F14).
   - Research strategies for decomposing the alternative space, commissioned
     as research for this revision.
   - Primers attached to the skill (`first-principles.md`,
     `oblique-strategies.md`, and others as evaluated).
   - Pair this with F28's evidence-feasibility triage and F31's shared map
     across children.
2. **Cost and effort visibility as information, not a cap** (F12). Andrew
   prefers thoroughness over efficiency.
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

## Design decisions

Captured from the `--only-questions` pass with Andrew on 2026-10-20. Treat these
as fixed inputs for feature-design.

1. **Domain map: step 0 of methodology-review, with split ownership.** A new
   step 0 commissions the map through `research-pipeline:scout` →
   `agentic-research:research-orchestrator`, with a structured domain-map
   output. The two halves are owned separately:
   - **External alternative space** (research-owned): approach families
     described in their own terms, evidence by level and open questions. It is a
     versioned, refreshable `.research/` artifact that a component-then-suite
     program can reuse (F31).
   - **Project mapping** (loop-record-owned): jobs, decisions, the charter
     sample drawn from the map, and coverage against it.

   This split also settles F7/F18. Project transfer and proposals belong to the
   loop record, not to research. No second research engine and no new skill.
2. **Sample completeness: an independent challenge, then an operator gate.**
   Before any depth specialists launch:
   - A fresh-context pass (cross-model where available) applies the
     decomposition strategies to the map and sample to find missing approach
     families.
   - An operator checkpoint then shows the map, the sample, the gaps, the F28
     evidence-feasibility triage, and the expected dispatch count and effort
     (F12, as information, not a cap).
3. **Coverage gaps against the map are report-only.** Unexamined approach
   families that bear on in-scope decisions are listed in the assessment report
   and the exit report. They never block a "Clean within reviewed scope" exit.
4. **Strategy research produces a new primer.** Commission an Agentic Research
   engagement on systematic ways to decompose a solution space into genuinely
   different approaches; set its dials at kickoff and favor thoroughness.
   Distill the result into a new primer doc under `plugins/research-pipeline/docs/`,
   following the precedent of `brief-first-principles-frameworks.md` →
   `first-principles.md`. Attach the new primer, `first-principles.md` and
   `oblique-strategies.md` to specific methodology-review steps: domain map,
   charter sample, completeness challenge and per-facet briefs.
5. **The Agentic Research fixes become a sibling feature with their own PR.**
   F8, F15, F16, F17, F21, F24 and F27 move to a separate `agentic-research`
   feature, drained in the same run. Land F21 (rigor table vs `evaluate`
   reachability) and F27 (bare-citation lint) before the strategy research runs,
   because both affect that engagement's gates.
6. **F4 is fixed with a fork-patched tag route.** Agile-workflow gains a
   documented fork patch: items tagged `methodology-review` route to
   `research-pipeline:methodology-review`, mirroring the existing `[research]` →
   research-orchestrator route. Autopilot and the design family then hand the
   controller to that skill instead of designing it. methodology-review mints
   its controller directly from a bundled body skeleton, not through
   `agile-workflow:scope` (F5, F6).

**Out of scope for this drain:** the validation plan (repeating the Knowledge
review under the revised skill) runs in project-blueprint, after merge, and only
when Andrew places that project in scope.


## Design-time refinements (autopilot judgment, 2026-10-20)

- **Decision 6, refined: the route tag is `methodology-review-controller`, not
  `methodology-review`.** This repo, and adopters, use `methodology-review` as a
  topic tag on ordinary work about the skill, including this feature and its
  stories. A route on that tag would hand those items to the review skill. A
  dedicated controller tag keeps "route this item to methodology-review"
  separate from "this item is about methodology-review". The skill's controller
  definition changes from "tagged `methodology-review` without `research`" to
  "tagged `methodology-review-controller`".
- **Controllers stay in `work-view --ready`.** The `[scan]` exclusion is
  compiled into the `work-view` binary. Patching it means a fork binary change
  plus a rebuild, which is out of proportion here. Routing at the skill level
  delivers the operative fix: no design, implement or release skill acts on a
  controller.

## Architectural choice

Three shapes were considered:

- **A. Revise methodology-review in place (chosen).** Add a step 0 domain map,
  built by `scout` in a structured domain-map mode. Scout uses the existing
  `survey-landscape` intent and `landscape-brief` + `vocab-capture` output
  kinds, so the map is an ordinary refreshable landscape brief under
  `.research/analysis/`. The project-side mapping (jobs, decisions, the sample
  drawn from the map, coverage) lives in the loop record. Deep templates move to
  directly linked references: the domain map, the commission packet and the
  assessor briefs.
- **B. A separate domain-map skill.** Rejected by design decision 1. It adds a
  skill to maintain, for a step only reviews use.
- **C. A new `domain-map` output kind in Agentic Research.** Rejected. It would
  extend ARD's inventory to serve a pipeline concern, and `landscape-brief`
  with `vocab-capture` already carries the shape. Required sections are a
  commissioning request, not an engine change.

**Machinery forecast.** A adds no new state owner:

- The map lives in the existing research tier.
- The project mapping lives in the existing loop record.
- The completeness challenge is one more fresh-context dispatch, using the same
  pattern as the step-6 assessor.
- The F4 fork patch adds routing rows only, with no binary or `work-view`
  change. Consequence: `work-view --ready` still lists a controller, but no
  design or implement skill will act on it.

**Trickiest unit: the strategy research and primer (S1, S2).** Their content is
unknown until the research returns, and the lead objective depends on them. They
are therefore commissioned first and run alongside the skill-core and routing
stories. The skill-core story leaves explicit seams (step 0, the
sample-completeness checkpoint, facet briefs) that S5 fills from the primer.

## Implementation Units

### Unit 1 (S1): Strategy research engagement

**Story:** `feature-methodology-review-pilot-learnings-strategy-research`, a
`[research]` story with `research_dials`.

The question: what systematic strategies decompose a solution space into
genuinely different approaches? And how can a sample of approaches be checked
for completeness before depth research, including stopping rules and coverage
estimates?

Declared facets (`mixed` scope authority, so more may emerge):

1. Design-space and morphological methods, for example general morphological
   analysis, TRIZ, design-rationale QOC and set-based design.
2. Systematic-review search strategy and completeness, for example search
   saturation, capture–recapture, citation chasing and PRISMA-S.
3. Taxonomy and faceted-classification construction methods.
4. Technology and landscape mapping practice, for example patent landscaping,
   technology scouting and scenario methods.
5. LLM and agent ideation diversity and coverage failures, for example
   homogenization and diversity techniques.

**Decision relevance:** which moves the new primer prescribes at each
methodology-review step (domain map, charter sample, completeness challenge,
facet briefs), and which completeness signal the challenge reports.

**Acceptance:**
- [ ] A campaign exists under
  `.research/analysis/campaigns/solution-space-decomposition/`.
- [ ] Every gate passed at `full` rigor (multi-path, so `adversarial-read` and
  `evaluate` both ran).
- [ ] The engagement record is in the story body.

### Unit 2 (S2): Surfacing-alternatives primer

**File:** `plugins/research-pipeline/docs/surfacing-alternatives.md`, a new
primer. It mirrors the `first-principles.md` shape: preamble, moves, a per-step
workflow, guardrails and related documents. It also has a "Grounding" note
linking the campaign. It contains no `[handle]{N}` citations, because the docs
tier is not a research tier. It states which moves apply at which
methodology-review step, and how it composes with `first-principles.md` (Open
and Challenge) and `oblique-strategies.md` (lateral moves when the sample is
stuck).

**Acceptance:**
- [ ] Every move traces to a finding in the campaign, or is explicitly labeled
  as practice without evidence.
- [ ] The per-step table covers all four steps.
- [ ] It has `knowledge-index` frontmatter consistent with the sibling primers.

### Unit 3 (S3): methodology-review core revision

**Files:** `plugins/research-pipeline/skills/methodology-review/SKILL.md`, new
references `domain-map.md`, `commission-packet.md` and `assessor-briefs.md`,
plus edits to `review-record.md`, `review-decomposition.md`,
`plugins/research-pipeline/skills/scout/SKILL.md` (domain-map mode),
`docs/research-composition.md` (the profile row) and `agents/openai.yaml` if
the description changes.

| Skill area | Change | Findings |
|---|---|---|
| New step 0 | Map the domain. Reuse a current map, or commission one through scout. External alternative space goes to research; project mapping goes to the loop record. | F11, F31 |
| Step 1 | Mark operator-owned kickoff questions apart from host fields. Add a rule for overlapping prior reviews: a pending prior decision is a constraint input, never silently absorbed. Add "discovery" as a decision dimension. Add evidence-feasibility triage per decision, with an early experiment track. Draw the sample from the map. | F1, F2, F14, F28 |
| New Checkpoint M | Map and sample, before any depth research: an independent completeness challenge, then the operator gate showing the map, sample, gaps, triage, and expected dispatch count and effort, as information, never a cap. | F11, F12 |
| Step 3 | A commission packet with default dials (`calibrate-external`; `synthesis-brief` + `questions-list`). The required non-recommending decision-relevance section covers evidence per decision, the adopt-if-an-alternative-wins conditional, and the next evidence. Ownership: research owns comparisons, the loop record owns transfer and proposals. A route for mid-review scope expansion: amend the engagement within its scope authority, else open a new linked engagement. | F7, F9, F10, F13, F18, F23 |
| Step 4 | Host pre-check of each draft finding against current text. Independent assessment happens before the operator packet. The bundled assessor brief. | F19, F20, F22, F30 |
| Step 5 | Re-present dependent findings when the operator declines the path they relied on. Authorized remedies may be bundled by delivery surface. | F25, F26 |
| Step 6 | Coverage gaps against the map are report-only. A tally of actual effort sits beside the estimate. | decision 3, F12 |
| New "Re-run and longitudinal review" section | New review id linked to its predecessor; prior IDs carried forward; no inherited round count; research reused under freshness rules; a what-changed baseline; outcome comparison across versions. | F29 |
| `review-record.md` | The Agile Workflow controller skeleton, minted directly with tag `methodology-review-controller` (not via `scope`). The Transfer field moves to the loop record. Re-run and effort fields. | F4, F5, F6, F7 |
| `review-decomposition.md` | Children share the root map; per-child research deepens only where a child's decisions need it. | F31 |

**Acceptance:**
- [ ] Each F-number above maps to a specific rule in the skill or a reference.
- [ ] SKILL.md stays focused, with deep templates in references.
- [ ] No ARD discipline is copied into the pipeline.
- [ ] skill-portability passes.
- [ ] Every relative link resolves.

### Unit 4 (S4): Agile-workflow routing fork patch (F4)

**Files:**
- `plugins/agile-workflow/skills/autopilot/SKILL.md`: a routing row for
  `[methodology-review-controller]` items at any stage, handed to
  `research-pipeline:methodology-review` to resume. An item awaiting an
  operator decision is reported as *awaiting operator*, not as a defect
  blocker.
- `plugins/agile-workflow/skills/feature-design/SKILL.md` and
  `plugins/research-pipeline/skills/{feature-design,epic-design}/SKILL.md`:
  misroute guards.
- `plugins/agile-workflow/skills/implement-orchestrator/SKILL.md`: an exclusion,
  if it selects implementing items.
- `plugins/agile-workflow/skills/release-deploy/SKILL.md`: controllers never bind
  to a release.
- `.work/CONVENTIONS.md`: the tag convention.
- `docs/project-navigation.md`: a fork-patch record.

**Acceptance:**
- [ ] Every skill that routes drafting, implementing or review items names the
  route or the exclusion.
- [ ] The fork-patch note lists the patched files.
- [ ] Agile-workflow tests pass (`convert-content-integrity`,
  `test_prompt_context`).

### Unit 5 (S5): Primer attachment and strategy-specific steps

**Files:** methodology-review `SKILL.md`, plus `domain-map.md` and
`assessor-briefs.md`. Optionally `scout/SKILL.md`.

Add "Read … for consideration" lines in the established style, plus the moves
applied at step 0, at Checkpoint M's completeness challenge, and in the facet
briefs, as the research supports.

**Acceptance:**
- [ ] The primers are attached at named steps.
- [ ] The completeness challenge brief uses the researched strategies and
  completeness signal.

## Implementation Order

1. **S1 research and S4 routing patch.** Independent, and S1 takes the longest.
2. **S3 skill core.** It needs no research output and leaves seams for S5.
3. **S2 primer**, after S1.
4. **S5 attachment**, after S2 and S3.
5. Feature verification and review, then the PR.

## Testing

- `plugins/research-pipeline/scripts/tests/skill-portability.test.sh` checks
  skill shape and frontmatter.
- A relative-link check over the methodology-review skill, its references and
  the new primer: a scripted check run at verification.
- The agile-workflow tests touched by S4: `convert-content-integrity.test.sh`
  and `hooks/scripts/test_prompt_context.py`.
- Knowledge-index regeneration plus `--lint-only` for the new primer's
  frontmatter.
- Behavioral validation (repeating the Knowledge review in project-blueprint) is
  out of scope for this drain; see design decisions.

## Risks

- **The research yields no decisive strategy set.** **Fallback:** the primer
  states the evidence gaps, uses the strongest supported moves plus the
  existing first-principles and oblique moves, and labels unsupported practice.
- **SKILL.md bloat**, since the skill is already dense. **Fallback:** move the
  templates to references and keep SKILL.md to rules.
- **Fork-patch drift against upstream agile-workflow.** **Fallback:** documented
  in `project-navigation.md`, so it is preserved on sync.
- **Least sure:** whether autopilot should drive controllers at all, as opposed
  to skipping them. The chosen route resumes the controller and stops at the
  operator gates, consistent with decision 6.

## Design questions for feature-design

- **Surfacing alternatives:**
  - Which strategies for decomposing a solution space should the skill
    prescribe? Research it first.
  - Which primers attach, at which steps?
  - How does the operator review the domain map and the sample, so they can add
    approaches before any depth research, rather than mid-campaign as in the
    pilot?
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

## Integrated verification (2026-10-20)

All five child stories are done.

**Tests that passed:**
- research-pipeline `resolve-agentic-research` and `skill-portability`;
- the research-pipeline session-context hook test;
- agentic-research `skill-metadata`;
- agentic-research conformance 132/132 and the lint unit tests;
- agile-workflow `convert-content-integrity`, `agent-metadata`, `convert-install-routing` and
  `test_prompt_context`.

**Other checks:**
- The knowledge index regenerates with 0 errors and 0 warnings.
- The relative-link and anchor check is clean across the methodology-review skill, its references,
  scout and the three primers.
- The research campaign passed every verification gate (see the strategy-research story's record).

**Acceptance coverage:**
- design decisions 1–6 are realized (decision 6 refined to the `methodology-review-controller` tag);
- F1–F31 are traced in the skill-core story's table;
- the primer is grounded in the verified campaign.

The validation plan (repeating the Knowledge review in project-blueprint) remains out of scope.
