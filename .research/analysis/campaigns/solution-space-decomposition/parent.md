---
title: "Solution-space decomposition: generating genuinely different approaches and checking a sample's completeness"
provenance: agent-synthesis
updated: 2026-10-20
summary: >-
  Campaign synthesis over eight facets (design-space methods, decision-option generation,
  analogous-domain search, LLM ideation diversity, search completeness, coverage estimation,
  taxonomy construction, landscape mapping). Unaided human generation recovers roughly a third to
  a half of later-recognised objectives or alternatives and narrows toward familiar examples and a
  person's dominant category; language-model generation, measured differently, converges on the same
  modes across independent draws and across models. Remedies with measured support in their tested
  settings are an objectives- or purpose-first generation key, a second pass that states the first is
  incomplete and sets a target, generation that sees prior items and is told to differ, and abstraction
  at a workable level for distant retrieval; independent generation before group discussion is a
  prescription, with pooling demonstrated in one case;
  upfront examples, similarity feedback and standard multi-agent debate narrowed sets in the studies
  that tested them. No attested source validates a completeness estimator for families of methods or
  approaches; completeness signals are relative to a declared frame, each estimator has its own input
  and independence assumptions, and a model-based lower bound applies only where those assumptions
  hold, while "nothing new in the last pass" measurably fails in screening. Omissions are detected
  far less often than wrong inclusions. Structured generators are advocated more than measured.
key_findings:
  - Unaided human generation recovers roughly 30–50% of later-recognised objectives or alternatives, and omitted items are about as important as found ones; language-model narrowing is measured as similarity and category coverage, not as this recovery fraction.
  - Upfront examples, similarity feedback and standard multi-agent debate narrowed sets where tested (voting over independent responses did not, and AI-example exposure widened collective diversity in one dynamic setting); independent generation pooled before discussion widened the set in one case.
  - Measured second-pass gains come from stating the first pass is incomplete with a numeric target, or showing prior items with an instruction to differ; more time does not help.
  - No attested source validates a completeness estimator for families of methods or approaches; capture–recapture needs at least two passes, incidence estimators need replicated sampling units, abundance estimators need frequency counts from a sample, and screening tests need a random sample of the remainder; estimates are frame-relative and are not certification.
  - Stopping when the last pass added nothing missed recall targets in about 39% of screening runs; saturation stopping points left part of the observed themes unseen.
  - Reviewers and models detect omissions far less often than wrong inclusions, but judge presented candidates much more accurately than they author full sets.
  - Fields distinguish a different approach from a variation by the abstraction level of divergence, a different value on a declared dimension, or non-equivalence under a declared relation; every such test depends on the frame chosen.
---

# Solution-space decomposition

## Question, scope and evidence

**Question.** What systematic strategies decompose a solution space into genuinely different
approaches rather than variations authored from recall, and how can a sample of approaches be
checked for completeness before depth research, including stopping rules and coverage estimates?

**Scope.** Eight specialist facets, composed through two cluster syntheses (generation;
completeness). Most generation evidence is from student or crowd lab studies and from preprints on
language models; most completeness evidence is from evidence synthesis, ecology, software inspection
and testing, and classification research. Transfer to kinds of methods or approaches is analogical
throughout: no attested source tests these techniques on samples of approaches to a methodology.
{inferred: absence across all eight facets} Evidence levels: **advocated**, **demonstrated**,
**measured**; reduced-depth sources are marked.

## 1. Why samples authored from recall are incomplete

- Unaided generation recovers roughly 30–50% of later-recognised objectives
  [bond-carlson-keeney-improving-objectives-2010]{453}; decision makers "identify less than half of
  their alternatives", with overlooked alternatives of the same average quality
  [siebert-keeney-alternatives-2015]{450} {confidence: abstract-only}.
- Omissions concentrate in categories the generator never entered — "breadth of thinking was
  insufficient" [bond-carlson-keeney-improving-objectives-2010]{453}.
- Examples anchor: designers repeated example features even when told not to (Jansson and Smith, as
  reported) [crilly-cardoso-fixation-2017]{114}; upfront examples increased misses
  [bond-carlson-keeney-improving-objectives-2010]{453}; unaided analogical retrieval is surface-bound
  [gick-holyoak-schema-induction-1983]{416}.
- Language models narrow collectively and across models: population-level variability far below
  humans [wenger-kenett-creative-homogeneity-llms-2025]{306}; 71–82% average similarity between
  different models' responses [artificial-hivemind-homogeneity-2025]{307}; independent sessions cover
  far fewer category combinations than independent humans
  [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}. Recall of rare items lags encoding
  [calderon-recall-bottleneck-factuality-2026]{320}.
- Generators overrate their own completeness: laypeople and mechanics under-weighted what a pruned
  fault tree omitted [fischhoff-slovic-lichtenstein-fault-trees-1978]{464}.
- Blind spots at the level of whole families recur through vocabulary mismatch
  [mahdabi-prior-art-query-2011]{254}, a single channel or seed set
  [erana-finlayson-neural-patent-landscaping-2024]{253} [wohlin-hybrid-search-snowballing-2022]{160},
  and staying within one's own domain [franke-poetz-schreier-analogous-markets-2014]{273}.

## 2. Generation strategies and their evidence

| Strategy | Evidence | Key limit |
|---|---|---|
| Objectives or purpose as the generation key | Measured: more and better alternatives [siebert-keeney-alternatives-2015]{450} {confidence: abstract-only}; purpose-fixed, mechanism-diverse retrieval beat keyword and random [hope-analogy-mining-purpose-mechanism-2017]{414} | Students, personal decisions; one small crowd study |
| Independent generation, then pooled union | Demonstrated: aggregate list "much more complete" [bond-carlson-keeney-objectives-2008]{452} | One case; changing model identity alone does not establish independent coverage, since different models' responses were highly similar [artificial-hivemind-homogeneity-2025]{307}, while distinct cues to one model raised coverage [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312} |
| Second pass with "first lists are incomplete" and a numeric target | Measured: +2.77 to +4.87 items, no quality loss [bond-carlson-keeney-improving-objectives-2010]{453} | Objectives, MBA population |
| See prior items, instruction to differ (LLM) | Measured: lowest similarity [meincke-prompting-idea-variance-2024]{300}; human-level distinctness [noveltybench-humanlike-diversity-2025]{310} | Caveats on model version; gains vanish as pools deplete |
| Distinct cue per draw (ordinary personas, fixed agent lenses) | Measured in single studies [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312} [creative-mad-debate-diversity-2026]{317} | One model or one preprint each |
| Categories as a second pass | Measured: +30% self-generated in a second pass [bond-carlson-keeney-improving-objectives-2010]{453} | The category effect cannot be separated from the second opportunity itself, and categories added no reliable gain over a motivated deeper review; upfront categories did not reduce misses [bond-carlson-keeney-improving-objectives-2010]{453} |
| Abstraction for distant retrieval (compare two analogs; concrete constraint schemas) | Measured: 21% → 45% transfer [gick-holyoak-schema-induction-1983]{416}; relevant yet distant inspirations [kittur-scaling-analogical-innovation-2019]{415} | A review reports Zahner et al. finding that too-abstract framing lowers fit, and that the right balance is unclear [vasconcelos-crilly-inspiration-fixation-2016]{418} |
| Distant or analogous-domain sources | Mixed: novelty up and usability down [franke-poetz-schreier-analogous-markets-2014]{273}; contradictory lab results [chan-fu-analogy-distance-commonness-2011]{403} [fu-near-far-analogy-2013]{404} | No locatable sweet spot |
| Morphological fields, design spaces (dimensions × values) | Advocated/demonstrated [ritchey-gma-general-method]{100} [shaw-petre-design-spaces-2024]{110} | Complete only within chosen dimensions [ritchey-psm-gma-2006]{263} |
| TRIZ, QOC, set-based design, strategy tables | Mixed or advocated [vargas-hernandez-triz-experiment-2012]{105} [buckingham-shum-dr-hypermedia-2005]{108} [toche-set-based-design-review-2020]{109} [usfws-usgs-sdm-developing-alternatives-2011]{458} | No coverage comparison |
| Taxonomy construction with ending conditions | Designed [nickerson-taxonomy-development-method-2013]{200} | Never tested against later-found objects |

Measured null or negative: a week of rumination for objectives [bond-carlson-keeney-objectives-2008]{452},
and more time for alternatives as reported by the university release [siebert-keeney-press-2015]{451}; upfront examples [bond-carlson-keeney-improving-objectives-2010]{453};
similarity feedback and select-the-best pooling [meincke-prompting-idea-variance-2024]{300}; standard
multi-agent debate, including heterogeneous models, while judge-based voting over independent responses
did not lower diversity [creative-mad-debate-diversity-2026]{317} (in a dynamic multi-generation pool,
high exposure to AI ideas instead increased collective diversity
[ashkinaze-ai-ideas-collective-diversity-2024]{304} {confidence: search-summary}); temperature
[deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}. A reported student study associated larger
morphological matrices with lower-quality concepts [martinsson-bonde-mm-combinatorics-2025]{103}.

## 3. What counts as a different approach

- A divergence at a higher abstraction level — principle rather than embodiment or detail
  [sorensen-ideation-metrics-axioms-2026]{113}.
- A different value on a declared, purpose-relevant, discriminating dimension
  [ritchey-gma-general-method]{100} [nickerson-taxonomy-development-method-2013]{200}.
- Non-equivalence under a declared equivalence relation [kang-dse-equivalence-2010]{111}
  {confidence: abstract-only}; a different mechanism for the same purpose
  [hope-analogy-mining-purpose-mechanism-2017]{414}.

Each test depends on a chosen frame: the meta-characteristic "impacts critically the resulting
taxonomy" [nickerson-taxonomy-development-method-2013]{200}, classification routes yield different
classes for the same objects [hjorland-classification-2017]{205}, and a kind count depends on the
identity threshold that merges near-duplicates [kornish-ulrich-opportunity-spaces-2011]{361}.

## 4. Completeness signals and stopping

- **No validated estimator for the completeness of families of methods or approaches** was found in
  the attested corpus; landscape, taxonomy and design-space practice measures item recall against a
  known or pooled set [zhang-qgs-search-2011]{258} [sampson-relative-recall-2006]{163}. Richness and
  coverage estimators do have measured evaluations in their own settings: ecological subsampling and
  simulation [chao-sufficient-sampling-2009]{352} [chao-hill-numbers-rarefaction-2014]{351}, fuzzing
  against true path richness [bohme-stads-species-discovery-2018]{359} and inspections against seeded
  defects [briand-capture-recapture-inspections-2000]{362}; vocabulary applications report model fit
  rather than a known total [efron-thisted-shakespeare-unseen-1976]{355}.
- **Frame-relativity.** Estimates are relative to the generating process
  [kornish-ulrich-opportunity-spaces-2011]{361} [meincke-prompting-idea-variance-2024]{300}, the
  identity threshold [kornish-ulrich-opportunity-spaces-2011]{361}, the declared dimensions
  [ritchey-psm-gma-2006]{263} and the known set [cochrane-handbook-ch4-searching-2025]{151}.
- **Inputs and assumptions differ by estimator.** Capture–recapture needs at least two searches,
  treated as independent captures [cochrane-handbook-ch4-searching-2025]{151}
  [bron-chao-estimator-tar-2024]{169}; incidence estimators need replicated sampling units, and
  abundance estimators need frequency counts of individuals from a sample
  [chao-colwell-chao2-inequality-2017]{350} [chao-hill-numbers-rarefaction-2014]{351}; the screening
  stopping test needs a random sample of the unseen remainder [callaghan-statistical-stopping-2020]{170}.
  Chao-type estimates are lower bounds under heterogeneous detection
  [chao-colwell-chao2-inequality-2017]{350}; other capture–recapture models can overestimate severely
  or fail to produce an estimate, and inspection studies advise against fewer than four inspectors
  "unless shown to work in a particular environment" [briand-capture-recapture-inspections-2000]{362}.
- **What small samples support.** Sample coverage, the share of total abundance or incidence
  probability belonging to observed kinds rather than the share of kinds observed, is estimable when
  the number of missing kinds is not [chao-hill-numbers-rarefaction-2014]{351}; Kitchenham et al. found missed papers "adding three new
  categories" [kitchenham-slr-repeatability-2011]{375}, so new items opening new categories is a
  measured signal of missing kinds.
- **Stopping rules that fail.** "No new items in N" missed the 95% recall target in about 39% of
  screening runs [callaghan-statistical-stopping-2020]{170}; median coverage at thematic-saturation
  stopping points was 78–82% of observed themes [guest-thematic-saturation-method-2020]{173}; several
  taxonomy ending conditions check stability over the last iteration, alongside MECE, sample and
  populated-cell conditions, and the method's demonstration used a selected two; none is tested
  against later-found objects [nickerson-taxonomy-development-method-2013]{200}.
  Certification-style reporting gives confidence across a range of targets
  [callaghan-stopping-recommendations-2024]{171}.
- **Diversity-seeking and estimation pull apart.** A diversity-seeking pass produces singletons by
  design, removing the repetition the estimators assume [van-rijnsoever-saturation-simulation-2017]{358}
  [chao-colwell-chao2-inequality-2017]{350} (coverage-estimation specialist, marked inferred).
- **Detecting absence.** Planted over-inclusions were detected "6-7x more often than planted omissions"
  [judging-not-enumerating-omissions-2026]{321}; placeholders marking where content was removed raised
  omission detection by 35.7% on a surface benchmark [fu-absencebench-omission-2025]{365}; judging
  presented candidates is much more accurate than authoring the set
  [judging-not-enumerating-omissions-2026]{321}. Disagreement between passes is partly classification:
  23–24% retrieval overlap alongside kappa 0.66–0.82 classification agreement
  [el-emam-defect-classification-repeatability-1998]{372}.

## 5. Adoption recommendations for the consuming primer

These map findings onto the consumer's four steps. Each is conditional on the cited evidence and on
transfer to approaches being analogical; none is shown in the attested sources for methodology
reviews specifically.

**Domain map.**
1. Start from jobs, outcomes and objectives, and use them as the generation key; derive decision
   dimensions from that purpose and admit only discriminating ones
   [siebert-keeney-alternatives-2015]{450} {confidence: abstract-only}
   [nickerson-taxonomy-development-method-2013]{200}.
2. Use several independent retrieval routes with vocabulary expansion, and at least one adjacent-field
   route at a workable abstraction (purpose fixed, mechanism varied; compare two analogs)
   [zhang-qgs-search-2011]{258} [mahdabi-prior-art-query-2011]{254}
   [hope-analogy-mining-purpose-mechanism-2017]{414} [gick-holyoak-schema-induction-1983]{416}.
3. State the frame explicitly — dimensions, identity rule for "same family", generators used — because
   every completeness claim is relative to it [kornish-ulrich-opportunity-spaces-2011]{361}
   [ritchey-psm-gma-2006]{263}.

**Charter sample.**
4. Draw so that every value of each declared dimension appears at least once ("full field coverage",
   which covers parameter values, not all configurations) [ritchey-psm-gma-2006]{263}. A university
   release reports that, in a paper-title task, a few clearly distinguishable alternatives scored better
   than many similar ones [siebert-novices-press-2016]{454}; that is a secondary report from another
   task, so favouring distinct families over near-duplicates is a transfer, not a tested rule; do not select by how often a family is proposed, which keeps the
   commonest [naik-div-se-diversity-of-thought-2023]{314}.
5. Name a different family by divergence at the principle level or on a declared dimension, not by
   surface features [sorensen-ideation-metrics-axioms-2026]{113}.

**Completeness challenge.**
6. Have the challenger enumerate families independently before seeing the sample, then compare —
   upfront examples increased misses in an objectives experiment, and independent generation before
   discussion is the prescribed order [bond-carlson-keeney-improving-objectives-2010]{453}; standard
   multi-agent debate lowered diversity across runs [creative-mad-debate-diversity-2026]{317}.
7. Give the challenger distinct cues from the author (different purpose framings, perspectives or
   adjacent fields): different models' responses were highly similar, so a different model alone does
   not establish independent coverage [artificial-hivemind-homogeneity-2025]{307}, while distinct cues
   raised coverage within one model [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}.
8. Run a second pass that states first lists are typically incomplete and sets a numeric target
   [bond-carlson-keeney-improving-objectives-2010]{453}, and present candidate families from the map
   for membership judgement, which models did more accurately than enumeration in one-shot settings
   with a reference [judging-not-enumerating-omissions-2026]{321}; make absences visible, for example
   empty cells in the dimension grid — placeholder gains were measured for surface deletions with both
   documents available [fu-absencebench-omission-2025]{365}
   [nickerson-taxonomy-development-method-2013]{200}.
9. Report a descriptive, frame-relative coverage statement rather than "complete": the adjudicated
   observed union; families found by the challenger but not the sample; overlap between passes; whether
   new families open new categories or empty cells; classification-boundary decisions; and the frame
   used. Keep that observed count distinct from any estimated total. Apply a named model-based estimate
   only when its sampling assumptions are justified, report its uncertainty and transfer limits, and do
   not assign a statistical bound to deliberately varied challenge passes, whose design conflicts with
   the estimators' assumptions [chao-colwell-chao2-inequality-2017]{350}
   [bron-chao-estimator-tar-2024]{169} [kitchenham-slr-repeatability-2011]{375}. Avoid "nothing new in
   the last pass" as a completeness claim [callaghan-statistical-stopping-2020]{170}.
10. Separate retrieval gaps from classification disagreements (merged or split families) when passes
    disagree [el-emam-defect-classification-repeatability-1998]{372}
    [briand-capture-recapture-inspections-2000]{362}.

**Per-facet research briefs.**
11. Ask each facet to seek maximum variation and disconfirming cases rather than "more of the same"
    [booth-qes-searching-2016]{155}, to record vocabulary differences, and to report whether new sources
    open new categories [kitchenham-slr-repeatability-2011]{375}.

## Contradictions

| Relationship | Positions |
|---|---|
| `contradicts` | Far-field examples raised novelty [chan-fu-analogy-distance-commonness-2011]{403}; far stimuli lowered novelty and quality [fu-near-far-analogy-2013]{404}. |
| `tension` | Diversity-seeking sampling advocated for kinds [booth-qes-searching-2016]{155} versus estimators that need random-like repetition [chao-colwell-chao2-inequality-2017]{350} [van-rijnsoever-saturation-simulation-2017]{358}. |
| `tension` | Perspective-based review minimises reviewer overlap [regnell-pbr-perspectives-different-2000]{367}; capture–recapture needs overlap [briand-capture-recapture-inspections-2000]{362}. |
| `qualifies` | Categories coincided with gains as a second pass, confounded with the second opportunity, and added no reliable gain over a motivated deeper review; upfront they did not reduce misses [bond-carlson-keeney-improving-objectives-2010]{453}. |
| `qualifies` | Generating more options was associated with lower mean option quality and higher best-option quality in some problems, with non-significant direct links to choice quality [delmissier-option-generation-ideation-2015]{459}, and with higher maximum but not mean originality between persons [schweizer-creative-option-generation-2016]{460}; correlational, not causal. |
| `tension` | Morphological "totality research" [ritchey-gma-general-method]{100} versus design spaces as "helpful—but incomplete" [shaw-petre-design-spaces-2024]{110}. |
| `incommensurable` | LLM diversity below humans [wenger-kenett-creative-homogeneity-llms-2025]{306} versus matching or exceeding humans under some prompts [noveltybench-humanlike-diversity-2025]{310}; different metrics and domains. |

## Disconfirming analysis

- *A structured decomposition guarantees a complete set.* Not supported: completeness is relative to
  the frame [ritchey-psm-gma-2006]{263}, and no attested study shows a structured generator finding more
  distinct families than an unstructured expert list (absence across the generation and landscape facets).
- *An independent challenger reliably finds what is missing.* Weakened: omissions are detected far less
  often than commissions [judging-not-enumerating-omissions-2026]{321}; more perspectives did not find
  different defects [regnell-pbr-perspectives-different-2000]{367}; Chao-type estimates are
  lower bounds under heterogeneous detection, with wide intervals from few sampling units
  [chao-colwell-chao2-inequality-2017]{350}. Supported in a weaker form:
  independent lists pooled are more complete than any one [bond-carlson-keeney-objectives-2008]{452}.
- *Incompleteness of the sample matters.* The objectives authors disclaim direct evidence that
  incompleteness degrades decisions [bond-carlson-keeney-objectives-2008]{452}, while overlooked
  alternatives were of equal average quality [siebert-keeney-alternatives-2015]{450} {confidence:
  abstract-only}.
- *Using a language model makes the sample broader.* Disconfirmed for default sampling and standard
  debate [artificial-hivemind-homogeneity-2025]{307} [creative-mad-debate-diversity-2026]{317}; for model
  ensembles the source cautions they "may not" diversify given shared priors, without measuring marginal
  additions [artificial-hivemind-homogeneity-2025]{307};
  supported only under specific prompting regimes [noveltybench-humanlike-diversity-2025]{310}.

## Open questions

- How near-duplicate approaches should be merged before counting families, given that counts depend on
  the identity threshold [kornish-ulrich-opportunity-spaces-2011]{361}.
- Whether omission detection on semantic absences, such as missing approach families, behaves like
  surface omission [fu-absencebench-omission-2025]{365}.
- How problem framing and reformulation change which families are generated; held only through
  cite-through [vasconcelos-crilly-inspiration-fixation-2016]{418}.

## Revisit if

- A study validates any completeness estimator or ending condition against later-found kinds of methods
  or approaches.
- Full texts of Siebert and Keeney (2015) and Gettys et al. (1987) are acquired.
- A controlled study compares structured or model-generated dimensions with unstructured generation on
  coverage of a reference set of approaches.
- Omission-detection evidence for semantic absences appears for humans or models.

## Revisions

- **2026-10-20 — correction (adversarial-read R1–R9).** Positions preserved; claims re-scoped to their
  attestations. Overlap counts are reported descriptively and model-based bounds are applied only under
  justified assumptions (R1). Estimator input requirements are stated per estimator, and the validation
  absence is restricted to families of methods or approaches (R2). The full taxonomy ending conditions
  are restored (R3). The 12-unit worked example was confirmed against the source and the attestation
  extended (R4). The human recovery fraction is separated from LLM findings (R5). The categorical pooling
  restriction is removed (R6). The narrowing claims are limited to the tested conditions, with the
  voting control and the exposure countercase restored (R7). Quantity–quality findings are stated as
  associations (R8). Source-depth, cite-through and conditional qualifiers are restored (R9).
- **2026-10-20 — correction (adversarial re-check).** Per-setting estimator evaluations now cite their own attestations (R2). The ensemble statement is qualified as the source's caution (R6). The independent-first sequencing is labelled a prescription with one demonstration (R7). The categories contradiction row is qualified (R9).
