---
title: Design-space and morphological methods for generating genuinely different alternatives
provenance: agent-synthesis
updated: 2026-10-20
summary: >-
  How general morphological analysis, morphological matrices, TRIZ, QOC/Design Space Analysis,
  set-based concurrent engineering, software design spaces and objective-driven alternative
  generation construct an option space, keep alternatives from collapsing into variations of one
  idea, and prune; what completeness signals they offer (full-field coverage, consistency-reduced
  solution space, abstraction-weighted variety, master-list recall, capture-recapture style
  estimates); and how thin the measured evidence is relative to the advocated benefits.
---

# Design-space and morphological methods for generating genuinely different alternatives

**Facet:** design-space and morphological methods (campaign `solution-space-decomposition`).
**Question this facet answers:** how each method constructs a space of alternatives, how it guards
against "variations of one idea", how it prunes, and what evidence (if any) shows it improves
coverage or novelty over unstructured generation.

**Evidence-level legend used below.**
*Advocated* = described or claimed by the method's developers or proponents, without comparative data.
*Demonstrated* = shown working in cases, applications or descriptive studies, without a controlled
comparison. *Measured* = a controlled or quasi-controlled comparison against a baseline, with reported
numbers.

## 1. Methods: construction, anti-collapse mechanism, pruning, evidence

### 1.1 General morphological analysis (Zwicky; Ritchey) — parameters × values, then cross-consistency

**Construction.** The analyst identifies the parameters (dimensions) of the problem complex and gives
each a range of discrete values; the morphological field (the "Zwicky box") is the Cartesian product,
and each configuration takes one value per parameter [ritchey-gma-general-method]{100}. Parameters of
different kinds (technical, financial, political, ethical) may be mixed in one field
[ritchey-gma-general-method]{100}. Fields grow fast: Zwicky's 1947 propulsion morphology had 6
parameters and 576 configurations; a typical 6–10 parameter field has 50,000–5,000,000
[ritchey-psm-gma-2006]{101}; the Swedish shelter study's 10-parameter field exceeded 500,000
[ritchey-gma-general-method]{100}.

**How it resists variations-of-one-idea.** Alternatives are not authored one by one; they are
positions in an explicitly enumerated product space, so two configurations differ by construction in
at least one parameter value. Ritchey notes that by hand "it is fairly easy ... to identify and mark out
a few dozen realistic policy configurations", whereas the field contains far more
[ritchey-gma-general-method]{100} — the method's premise is that hand-picked configurations
under-sample the field {inferred: extends}. Zwicky's framing, as quoted by Ritchey, is "totality research" that "in an
unbiased way attempts to derive all the solutions of any given problem"
[ritchey-gma-general-method]{100}.

**Pruning — cross-consistency assessment (CCA).** Every pair of values across parameters is judged for
mutual consistency (no causality or direction); any configuration containing an inconsistent pair is
removed [ritchey-gma-general-method]{100}. Inconsistency types: logical contradiction, empirical
implausibility, and normative constraint — with normative exclusions deferred or "clearly designated as
such" so that "what is possible" is examined before "what is ... desirable"
[ritchey-gma-general-method]{100} [ritchey-psm-gma-2006]{101}. The scaling argument: configurations
grow exponentially with parameters while pairwise judgements grow quadratically, so a 100,000
configuration field needs "no more than a few hundred pair-wise evaluations"
[ritchey-gma-general-method]{100}. Claimed reduction is "up to 90 or even 99%"; in the EPR strategy
field 34,560 configurations reduced to 480 [ritchey-psm-gma-2006]{101}.

**A coverage criterion for sampling the field.** Where the field is a scenario field (hard to prune
because today's implausible may be tomorrow's fact), Ritchey's group chose eight configurations that
"together ... covered all of the parameter states in the scenario field ('full field coverage')"
[ritchey-psm-gma-2006]{101}. This is a stated, checkable completeness rule for a *sample* drawn from a
morphological space: every value of every parameter appears in at least one sampled configuration.

**Classification use.** Johansen defines parameters with "an exhaustive set of possible states or
values", applies CCA, and derives "an all-encompassing and mutually exclusive set of scenario classes"
(six classes for Norwegian external security challenges) [johansen-gma-scenario-classes-2018]{102}
{confidence: abstract-only}.

**Evidence level: advocated / demonstrated.** Ritchey reports over 100 computer-aided projects and an
audit-trail claim [ritchey-gma-general-method]{100}, but no controlled comparison against unstructured
generation in either fetched text. He reports trials where identical fields went to different groups for
CCA and that comparing divergent assessments revealed "the effects of group composition", without
reporting the results [ritchey-gma-general-method]{100}. He also states that GMA "has been written about
and discussed far more than it has actually been used in 'real' client-based projects"
[ritchey-psm-gma-2006]{101}.

### 1.2 Morphological matrix / chart (engineering design) — functions × means

**Construction.** A functional decomposition lists the functions needed for the main function; each row
lists means achieving that function; a concept is one means per function
[martinsson-bonde-mm-combinatorics-2025]{103}. Daly et al. summarise it as "Listing properties and
functions ... and multiple options for achieving each, then forming combinations"
[daly-design-heuristics-2012]{104}.

**Pruning and its limits.** Combinatorics explode: Almefelt's eight functions with up to 22 means gave
about 54.9 billion combinations, which "cannot possibly be considered manually"; "high-performing
combinations can remain undiscovered" [martinsson-bonde-mm-combinatorics-2025]{103}. Reduction routes
are heuristic reduction or (semi-)automatic exploration (Tabu search, genetic algorithms, pathfinding),
the latter requiring that means be quantifiable [martinsson-bonde-mm-combinatorics-2025]{103}. The
traditional matrix supports generation, "but not evaluation" [martinsson-bonde-mm-combinatorics-2025]{103}.

**Evidence level: demonstrated, with one reported negative measured finding.** As reported by Martinsson
Bonde et al., Smith et al. (2012) found with engineering students that large matrices, "especially those
with many functions relative to the number of means, can result in lower-quality concepts", which
motivates keeping functional decomposition at a high level for manual use
[martinsson-bonde-mm-combinatorics-2025]{103}.

### 1.3 TRIZ — contradictions, inventive principles, ideality

**Construction.** As described in the TRIZ experiment paper: Altshuller abstracted patterns from
patents; the portion "used most frequently by instructors" is the contradiction matrix, which frames a problem as a conflict between
two of 39 engineering characteristics and points to up to four of 40 inventive principles
[vargas-hernandez-triz-experiment-2012]{105}. The space is therefore not a product of problem
dimensions but a *catalogue of solution-transformation types* indexed by the contradiction
{inferred: divergence from §1.1}.

**How it resists variations-of-one-idea.** Principles push toward solution types the designer would not
reach from the current concept; Howard et al. (as reported) found principles "encouraged the designers
to find less obvious ideas" [vargas-hernandez-triz-experiment-2012]{105}. Daly et al., however, class
TRIZ with SCAMPER and SIT as methods that apply "modifications to existing concepts", aimed at
refinements "in the implementation phase" [daly-design-heuristics-2012]{104}.

**Evidence level: measured, mixed and small-sample.** The three-site experiment (traffic-light
redesign, short lecture-plus-handout treatment) reported novelty gains at UTEP (0.241→0.560, p=0.0004)
and Maryland (0.095→0.186, p=0.0145) but not Penn State (0.683→0.651, p=0.5786); variety rose at UTEP
(1.61→4.20) and marginally elsewhere with no significance test; quantity did not differ significantly
[vargas-hernandez-triz-experiment-2012]{105}. One UTEP arm had 9 participants, and the paper's text on
which session was assessed is internally inconsistent [vargas-hernandez-triz-experiment-2012]{105}. The
authors conclude TRIZ "improves some of the metrics while worsening others" and that outcomes depend on
subject, task and setting [vargas-hernandez-triz-experiment-2012]{105}. Borgianni et al. (TRIZ
researchers) state "the reliability of the Contradiction Matrix is often questioned", that TRIZ "has not
been developed following the standard procedures of scientific validation", and that IPs' usefulness
"is overwhelmingly more addressed in the literature than their limitations are"
[borgianni-triz-inventive-principles-2021]{106}. Their analysis of 161 TRIZ-solved problems could not
establish a deterministic contradiction→principle mapping (p of randomness 5.3%), and found
domain-specific "favourite IPs" [borgianni-triz-inventive-principles-2021]{106}.

### 1.4 QOC / Design Space Analysis (MacLean, Young, Bellotti, Moran) — questions × options × criteria

**Construction.** Design Space Analysis produces "a design space rather than a single artifact";
Questions "highlight key issues", Options are "answers" to Questions, Criteria argue for or against
Options, and "Options may spawn off consequent Questions"
[naverlabs-design-space-analysis-qoc]{107}. The space is a tree of decision questions, each with an
explicit option set and explicit evaluation criteria.

**How it resists variations-of-one-idea.** It requires, per question, that alternatives be stated as
competing answers to the *same* question and assessed against shared criteria — making it visible when
"options" are in fact one option with different details {extends}. Learning QOC requires "unbundling" ideas that
were "bundled together when they were initially expressed" and classifying each as Question, Option or
Criterion [buckingham-shum-dr-hypermedia-2005]{108}.

**Pruning.** Criteria assessments (positive/negative links) rank options per question
[naverlabs-design-space-analysis-qoc]{107}. DSA "does not make any specific claims about what
information should be included" — it structures whatever options the designers or other methods supply
[naverlabs-design-space-analysis-qoc]{107}. It therefore has no internal generator of options and no
completeness criterion {inferred: divergence — QOC organises and evaluates an option set; it does not
itself produce one}.

**Evidence level: advocated / demonstrated, with a negative usability record.** A 1994 survey by its
co-developers "found comparatively weak evidence regarding usability and utility"; intrusiveness and
cognitive overhead were obstacles to adoption, and the field saw a "decline in activity"
[buckingham-shum-dr-hypermedia-2005]{108}. The same authors caution that a modelling template "may
constrain the kinds of options one considers" [buckingham-shum-dr-hypermedia-2005]{108}.

### 1.5 Set-based concurrent engineering (Toyota; Sobek, Ward & Liker) — sets kept open, narrowed by intersection

**Construction and pruning.** As synthesised by Toche et al. from Sobek, Ward & Liker (1999): (1) map
the design space — define feasible regions, "explore trade-offs by designing multiple alternatives",
communicate sets; (2) integrate by intersection — look for intersections of feasible sets, impose
minimum constraint, seek robustness; (3) establish feasibility before commitment — "narrow sets
gradually while increasing detail", stay within sets once committed [toche-set-based-design-review-2020]{109}.
Specialty groups analyse their own option sets independently and then intersect them, as opposed to
point-based design that "focuses on one solution at a time and progressively refines it"
[toche-set-based-design-review-2020]{109}.

**How it resists variations-of-one-idea.** It delays convergence: participants "bring sets of
possibilities ... and juxtapose them to find an intersection of feasibility rather than successively
criticizing and modifying a single option" [toche-set-based-design-review-2020]{109}. It also offers a
*sizing* rule rather than a completeness rule {inferred: extends}: Ward & Sobek (2014, as reported) compute how many
alternatives to carry from the probability of each concept failing, focusing breadth where risk is high
[toche-set-based-design-review-2020]{109}.

**Evidence level: demonstrated (case and survey), with simulation support; low theoretical maturity.**
The review finds SBD research "predominantly qualitative and inductive", mostly case studies, with
"relatively low theoretical development"; industry implementation maturity is "no more than an
introductory level" [toche-set-based-design-review-2020]{109}. Liker et al.'s supplier survey (as
reported) found set-based communication more prevalent among Japanese suppliers but noted its indicator
list "is not exhaustive"; Shahan & Seepersad's simulations favoured set-based exchange but only on
serialised processes [toche-set-based-design-review-2020]{109}. The review also records the cost side:
carrying multiple alternatives "long into the development process could be detrimental"
[toche-set-based-design-review-2020]{109}.

### 1.6 Software design spaces and design-space exploration

**Construction.** Shaw's definition: "a discrete Cartesian space in which the dimensions correspond to
design decisions, the values on each dimension are the choices ... and points in the space correspond
to complete design solutions" [shaw-petre-design-spaces-2024]{110}. Examples: Lane's user-interface
spaces (25 functional dimensions of 3–5 alternatives; 19 structural dimensions of 2–7) built by
interviewing designers of six systems; the "Boxology" of six architecture-style classes; Römer &
Mattern's 14-dimension comparison of 15 sensor-network implementations [shaw-petre-design-spaces-2024]{110}.
Dimension dependencies are added as correlation/inter-dependency rules (Baum et al.; Penders et al.)
[shaw-petre-design-spaces-2024]{110} — the software analogue of CCA {inferred: convergence}.

**How it resists variations-of-one-idea.** Design spaces "help designers to check for coverage by
prompting them to consider alternatives systematically within the space"
[shaw-petre-design-spaces-2024]{110}. In automated DSE, Kang, Jackson & Schulte take a user-defined
notion of equivalence and generate symmetry-breaking predicates so the engine "does not sample multiple
equivalent design candidates" [kang-dse-equivalence-2010]{111} {confidence: abstract-only} — an explicit
mechanism for refusing near-duplicates.

**Limits stated by the field.** Design spaces are "helpful—but incomplete"; dimension choice is
"highly dependent on context" and changes as understanding evolves; comparing *existing* designs is
"less subject to the risk of oversimplification ... because the current set of designs is known"
[shaw-petre-design-spaces-2024]{110}. A hierarchical representation "tends to encourage making decisions
in the order embedded in the hierarchy"; designers "satisfice" and the systematic-search model is
"vastly oversimplified" (Brooks, as reported) [shaw-petre-design-spaces-2024]{110}. Practitioners report
choosing familiar solutions; "Since it is rarely possible to explore all the possible alternatives,
prior experiences are the primary source of information" [borowa-architectural-rationales-2023]{112}.

**Evidence level: demonstrated (curated examples), one statistical validation reported second-hand.**
The sampler is explicitly "not a comprehensive survey, let alone a systematic review"; Lane's
recommendation rules were reported as statistically validated against subjects' designs
[shaw-petre-design-spaces-2024]{110}.

### 1.7 Objective-driven alternative generation (decision analysis; Siebert & Keeney)

**Construction.** Decision makers' articulated objectives are used as stimuli for the
alternative-creation process [siebert-keeney-alternatives-2015]{115} {confidence: abstract-only}; the
Bayreuth release describes a master list of objectives combined with instructions to use them in the
search [siebert-keeney-press-2015]{116}.

**Evidence level: measured.** Across five studies of personally important decisions, decision makers
"identify less than half of their alternatives" and "the average quality of the overlooked alternatives
is the same as those identified"; using objectives "enhances both the number and quality of created
alternatives" with high significance [siebert-keeney-alternatives-2015]{115}. The Bayreuth release
reports, for an internship decision, unaided recall of 37% of the alternatives later judged relevant
against a master list; only 44% had considered their eventual top-rated option; a master list of
objectives plus instructions raised alternatives considered by 53%; and more time was not a substitute
[siebert-keeney-press-2015]{116}.

**Completeness signal.** Recall against a master list compiled independently of the respondent is the
measure that made the incompleteness visible [siebert-keeney-press-2015]{116} {inferred: aggregate}.

### 1.8 Contrast: heuristic transformation methods (Design Heuristics, SCAMPER, SIT)

Design Heuristics are "cognitive prompts" for moving through concept space; they "help an individual
build upon that idea to create endless variations" [daly-design-heuristics-2012]{104}. These methods
take an existing concept as input, which is the opposite of the morphological stance of enumerating a
space before any concept exists {inferred: divergence}. In Daly et al.'s protocol study, "in no cases did
the participants follow the prescribed procedure" of any listed ideation method, and a participant who
varied one functional dimension "did not capture the multidimensional aspect of morphological analysis"
[daly-design-heuristics-2012]{104}.

### 1.9 LLM-mediated morphological generation (reused attestations)

Luminate has an LLM generate categorical dimensions and values, then randomly selects one value per
dimension as a requirement for each response — a morphological field instantiated by a model
[luminate-design-space-generation-2023]{118}. Its evaluation reports no quantitative diversity or
coverage measure, and the authors note "dimensional reasoning does not happen naturally" even for
experts [luminate-design-space-generation-2023]{118}.

## 2. Operationalising "genuinely different": what the field measures

- **Abstraction-level hierarchy.** Shah, Smith & Vargas-Hernandez (2003), as restated by Sorensen et
  al., define variety as "a measure of the explored solution space"; ideas sit on a genealogy tree
  (physical principle → working principle → embodiment → detail) and differences at higher levels are
  weighted more (10/6/3/1) [sorensen-ideation-metrics-axioms-2026]{113}. Sorensen et al.'s OPED tree
  makes the "principle" level explicit: "An idea could achieve the objective by ____", e.g. remove ice /
  melt ice / prevent formation / prevent adhesion, versus embodiments such as "ice scraper"
  [sorensen-ideation-metrics-axioms-2026]{113}. Two ideas under one principle are, on this view,
  variations; two principles are different approaches {inferred: convergence with §1.1's
  parameter-value distinction}.
- **Axioms a set-level variety score should satisfy.** Adding a unique idea must raise variety; a new
  idea at a higher level should raise it more; a new idea similar to many existing ones should raise it
  less [sorensen-ideation-metrics-axioms-2026]{113}. The original SVS variety score violates the first
  (removing one idea raised it from 6.54 to 7.1) [sorensen-ideation-metrics-axioms-2026]{113}.
- **Equivalence classes.** Declare what counts as equivalent and sample one representative per class
  [kang-dse-equivalence-2010]{111}.
- **Embedding similarity thresholds.** Treating cosine similarity ≥0.8 as a duplicate, Meincke et al.
  estimate a technique's reachable unique-idea pool by a mark-recapture-style method (base prompt ~3700,
  chain-of-thought ~4700), and show diminishing returns after ~750–800 ideas
  [meincke-prompting-idea-variance-2024]{117}.

## 3. Completeness signals the sources offer, and what each can and cannot show

| Signal | Source | What it shows | What it cannot show |
|---|---|---|---|
| Full field coverage: each parameter value appears in ≥1 sampled configuration | [ritchey-psm-gma-2006]{101} | The sample spans the declared value ranges | Whether the parameters or value ranges are themselves complete |
| CCA-reduced solution space size (e.g. 34,560 → 480) | [ritchey-psm-gma-2006]{101} | How many internally consistent configurations remain | Correctness of pairwise judgements; group-composition effects are acknowledged but unreported [ritchey-gma-general-method]{100} |
| "Garbage detection": ill-defined parameters and "incomplete ranges of conditions" surface during CCA | [ritchey-psm-gma-2006]{101} | Definitional gaps inside the declared field | Missing parameters (claimed, not measured) |
| Abstraction-weighted variety | [sorensen-ideation-metrics-axioms-2026]{113} | Relative spread of a set across principles/embodiments | Absolute adequacy: "the metrics cannot yet be used to say whether a set has 'enough' novelty or variety" |
| Recall against an independent master list | [siebert-keeney-press-2015]{116} | Share of relevant alternatives an unaided generator found | Requires a master list built by other means |
| Capture-recapture style unique-pool estimate | [meincke-prompting-idea-variance-2024]{117} | Saturation of *one technique's* reachable pool | "we cannot estimate the total number of ideas in a space" |

{inferred: aggregate — every signal in the table is relative to a frame fixed by someone (declared
parameters, a genealogy tree, a master list, a generator); none of the fetched sources offers an
absolute completeness measure for an open option space.}

## 4. Failure modes and limits

1. **Dimension selection is the uncontrolled step.** GMA output "is no better than the quality of its
   input" [ritchey-psm-gma-2006]{101}; design-space dimensions are context-dependent and shift with
   understanding [shaw-petre-design-spaces-2024]{110}; even experts struggle to name dimensions
   [luminate-design-space-generation-2023]{118}. A morphological field built from recall inherits the
   recall gaps of its author {inferred: convergence across these three sources}.
2. **Illusory totality.** "Totality research" [ritchey-gma-general-method]{100} is totality *within the
   declared parameters*; Shaw & Petre state design spaces are "helpful—but incomplete"
   [shaw-petre-design-spaces-2024]{110}; Sorensen et al. state a tree "cannot describe the total design
   space. It can only describe the explored space" [sorensen-ideation-metrics-axioms-2026]{113}.
3. **Combinatorial explosion, then arbitrary sampling.** Large fields exceed manual inspection
   [martinsson-bonde-mm-combinatorics-2025]{103} [ritchey-psm-gma-2006]{101}; large matrices with many
   functions relative to means were associated with lower-quality concepts (Smith et al., as reported)
   [martinsson-bonde-mm-combinatorics-2025]{103}.
4. **Scaffold-induced narrowing.** A template or modelling approach "may constrain the kinds of options
   one considers" [buckingham-shum-dr-hypermedia-2005]{108}; hierarchical representations bias decision
   order [shaw-petre-design-spaces-2024]{110}.
5. **Overhead and non-adoption.** QOC carried "cognitive overhead" and weak utility evidence
   [buckingham-shum-dr-hypermedia-2005]{108}; GMA "requires strong, experienced facilitation"
   [ritchey-psm-gma-2006]{101}; designers observed in the lab did not follow any method's procedure
   [daly-design-heuristics-2012]{104}; SBCE adoption is shallow [toche-set-based-design-review-2020]{109}.
6. **Transformation methods produce variations by design.** Heuristic and TRIZ-style operators modify an
   existing concept [daly-design-heuristics-2012]{104}; the variety they add depends on the starting
   concept {inferred: extends}.
7. **Fixation is the baseline these methods target.** Fixation is "a restricted exploration of the
   design space due to an unconscious bias resulting from prior experiences, knowledge or assumptions";
   exposure to examples led designers to repeat features "even when participants received instructions
   to avoid repeating" them (Jansson & Smith, as reported) [crilly-cardoso-fixation-2017]{114}.
8. **Metric fragility.** Variety and novelty scores correlate with idea quantity; evaluators build
   different trees and the effect on scores is unevaluated [sorensen-ideation-metrics-axioms-2026]{113};
   embedding-similarity results may change "dramatically" with the embedding model
   [meincke-prompting-idea-variance-2024]{117}.

## Disconfirming analysis

For each load-bearing claim I searched the attested sources for evidence against it.

- **"Structured design-space methods improve coverage/novelty over unstructured generation."** No
  attested source reports a controlled comparison of GMA, QOC, or set-based design against unstructured
  generation; the GMA and QOC evidence is practitioner/advocate reporting
  [ritchey-gma-general-method]{100} [ritchey-psm-gma-2006]{101} [naverlabs-design-space-analysis-qoc]{107}.
  The controlled numbers this facet found for a named structured method are TRIZ's, and they are mixed (one of three
  sites null on novelty, variety untested) [vargas-hernandez-triz-experiment-2012]{105}. A reported
  student experiment associates *larger* morphological matrices with *lower* concept quality
  [martinsson-bonde-mm-combinatorics-2025]{103}. Daly et al. state that "little systematic evidence has
  been presented for their usefulness in engineering design" for most listed ideation methods
  [daly-design-heuristics-2012]{104}. Outcome: the claim is **not supported as measured** for the
  morphological/QOC/SBCE family; it is advocated and demonstrated.
- **"Unaided generation misses many alternatives."** Supported by measurement in decision analysis
  [siebert-keeney-alternatives-2015]{115} [siebert-keeney-press-2015]{116} and consistent with the
  fixation literature [crilly-cardoso-fixation-2017]{114}. Disconfirming material found: Crilly &
  Cardoso note fixation errors "might be quite rare", that feature repetition is not always bad, and that
  narrow deep exploration "might save time" [crilly-cardoso-fixation-2017]{114}; most fixation studies
  use students, short tasks, and researcher-rated sketches [crilly-cardoso-fixation-2017]{114}, and the
  Siebert & Keeney samples were students on personal decisions [siebert-keeney-press-2015]{116}.
  Outcome: supported, with a population and task-type qualification.
- **"Cross-consistency assessment prunes the space substantially."** Ritchey reports 90–99% and a
  34,560 → 480 case [ritchey-psm-gma-2006]{101}; Martinsson Bonde et al. state that identifying
  incompatible pairings of means (Pahl et al.) has a "small" impact on the number of combinations
  [martinsson-bonde-mm-combinatorics-2025]{103}. Outcome: contested across contexts (see Contradictions).
- **"A sample can be checked for completeness."** Every completeness signal found is relative to a
  declared frame (§3); Sorensen et al. explicitly disclaim absolute adequacy
  [sorensen-ideation-metrics-axioms-2026]{113} and Meincke et al. explicitly disclaim whole-space
  estimation [meincke-prompting-idea-variance-2024]{117}. Outcome: supported only in the relative sense.
- **"QOC-style structuring helps designers."** Its own developers' 1994 survey found weak evidence
  [buckingham-shum-dr-hypermedia-2005]{108}. Outcome: not supported as measured.

## Contradictions

- **CCA reduction magnitude.** [ritchey-psm-gma-2006]{101}: pairwise consistency typically reduces a
  field "by up to 90 or even 99%". [martinsson-bonde-mm-combinatorics-2025]{103}: identifying
  incompatible pairs of means "do[es] not require ... software ... but their impact on the number of
  possible combinations is small." Relationship: `qualifies` — Ritchey writes about policy/strategy
  fields assessed by expert groups including empirical-implausibility judgements; Martinsson Bonde et al.
  write about engineering function–means matrices pruned on technical incompatibility. Neither source
  measures the other's setting.
- **Is the space "total"?** [ritchey-gma-general-method]{100} (Zwicky as quoted): morphology attempts to
  "derive all the solutions of any given problem". [shaw-petre-design-spaces-2024]{110}: design spaces
  are "helpful—but incomplete"; [sorensen-ideation-metrics-axioms-2026]{113}: a tree "can only describe
  the explored space". Relationship: `tension` — the totality claim is about the product of declared
  parameters; the incompleteness claims are about the space of possibilities beyond any declared frame.
  `{contested: whether a declared parameter set can be treated as complete}`.
- **TRIZ effectiveness.** [vargas-hernandez-triz-experiment-2012]{105}: TRIZ increased novelty and
  variety at two of three sites. [daly-design-heuristics-2012]{104}: "no scientific evidence has been
  collected that documents the use of TRIZ principles by untrained engineers" (2012).
  [borgianni-triz-inventive-principles-2021]{106}: the contradiction matrix's reliability "is often
  questioned"; TRIZ lacks standard scientific validation. Relationship: `tension` — Borgianni et al. cite
  the same group's 2013 journal version as experimental support while also recording validation doubts.
- **Is fixation (narrow exploration) a defect?** [daly-design-heuristics-2012]{104}: fixation is
  "premature closure of the search process". [crilly-cardoso-fixation-2017]{114}: fixation can be
  neutral or beneficial, e.g. deep exploration of a narrow viable set "might save time". Relationship:
  `tension`.

## Transfer-relevant observations

Stated in the field's own terms; no project recommendations.

1. The methods split into three families by what they enumerate: **problem-parameter products**
   (GMA, morphological matrix, Cartesian design spaces, Luminate), **solution-transformation catalogues**
   (TRIZ principles, Design Heuristics, SCAMPER), and **decision structures that organise supplied
   options** (QOC, set-based narrowing) {inferred: aggregate}. Only the first family enumerates before any
   concept exists; the second starts from a concept; the third has no generator of its own.
2. The field's operational test for "different approach" versus "variation" is the **abstraction level
   at which two ideas diverge** — principle/physical-principle versus embodiment/detail
   [sorensen-ideation-metrics-axioms-2026]{113}, or a different value on a declared parameter
   [ritchey-gma-general-method]{100}, or non-equivalence under a declared equivalence relation
   [kang-dse-equivalence-2010]{111}.
3. **Pruning is separated from generation** in GMA and SBCE: consistency (logical, empirical) first,
   normative/desirability later [ritchey-gma-general-method]{100}; feasibility before commitment
   [toche-set-based-design-review-2020]{109}.
4. The one **sample-level coverage rule** stated in the attested sources is full field coverage (every
   parameter value represented at least once) [ritchey-psm-gma-2006]{101}; the one **frame-level
   adequacy check** with measured results is recall against an independently compiled master list
   [siebert-keeney-press-2015]{116}.
5. **Objectives as a generation scaffold** have measured support for raising number and quality of
   alternatives [siebert-keeney-alternatives-2015]{115}; no other generation scaffold attested in this
   facet reports a measured effect on how many relevant alternatives are found.
6. Running **multiple distinct generation strategies and pooling** them reduced between-pool overlap in
   LLM ideation [meincke-prompting-idea-variance-2024]{117}, and Ritchey's group used parallel groups and
   cross-group comparison of consistency judgements [ritchey-psm-gma-2006]{101}
   [ritchey-gma-general-method]{100} {inferred: convergence — independent passes are used to surface
   divergence in both settings}.
7. Every completeness signal found is **frame-relative** (§3); an absolute stopping rule for an open
   option space is not offered by any attested source in this facet.

## Revisit if

- A controlled study comparing GMA/morphological-field generation (or QOC) against unstructured or
  recall-based generation on variety/coverage is found or published.
- Ritchey's unreported multi-group CCA divergence trials, or any inter-rater reliability data for CCA,
  become available.
- The full texts of Siebert & Keeney (2015), Shah et al. (2003), Smith et al. (2012) on matrix size, or
  Ilevbare et al. (2013) on TRIZ in practice are acquired and alter the reported numbers or conditions.
- An absolute (not frame-relative) adequacy measure for idea-set variety is proposed and validated —
  Sorensen et al. list this as open work.
- LLM-generated dimension sets are evaluated for coverage against expert-built fields.
