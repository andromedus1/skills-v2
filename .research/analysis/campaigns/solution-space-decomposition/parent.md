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
  hold, while "nothing new in the last pass" measurably fails in screening. Models detected planted
  omissions far less often than planted wrong inclusions. No attested source gives a validated rule for
  when to stop challenging a sample and begin depth research; the synthesis offers an escalation
  trigger as an inference. Structured generators are advocated more than measured.
key_findings:
  - Unaided human generation recovers roughly 30–50% of later-recognised objectives or alternatives, and omitted items are about as important as found ones; language-model narrowing is measured as similarity and category coverage, not as this recovery fraction.
  - Upfront examples, similarity feedback and standard multi-agent debate narrowed sets where tested; voting over independent responses did not; exposure to AI ideas narrowed collective diversity in one study and widened it in a dynamic multi-generation pool in another (the widening study at search-summary depth). Independent generation before discussion is a prescription, with pooling demonstrated in one case whose reference was the pooled union.
  - Measured second-pass gains come from stating the first pass is incomplete with a numeric target, or showing prior items with an instruction to differ; more time does not help.
  - No attested source validates a completeness estimator for families of methods or approaches; capture–recapture needs at least two passes, incidence estimators need replicated sampling units, abundance estimators need frequency counts from a sample, and screening tests need a random sample of the remainder; estimates are frame-relative and are not certification.
  - In screening, the baseline-rate and 50-consecutive-misses heuristics each missed the 95% recall target in about 39% of runs, and median thematic-saturation stopping points left part of the observed themes unseen; applying this to "the last challenge pass added nothing" is a transfer.
  - Models detected planted omissions far less often than planted wrong inclusions and judged presented candidates much more accurately than they authored full sets; one abstract-level study found human testers detecting more commission than omission faults.
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
{inferred: absence} Evidence levels: **advocated** (including designed
procedures), **demonstrated**, **measured**; "mixed" marks measured results that disagree.
Reduced-depth sources are marked.

**Terms used in §5.** The consumer is a methodology-review process with four steps: a *domain map* of
approach families; a *charter sample* (the comparison sample drawn from the map for depth comparison);
a *completeness challenge* (an independent pass, the *challenger*, that looks for families the sample
or map misses); and *per-facet research briefs* for depth research. The sample's *author* drafts it;
the *operator* is the person who adjudicates the review's decisions.

## 1. Why samples authored from recall are incomplete

- Unaided human generation recovers roughly 30–50% of later-recognised objectives
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
  [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}. In factual recall, rare items lag encoding
  [calderon-recall-bottleneck-factuality-2026]{320}, and models author sets less accurately than they
  judge membership [judging-not-enumerating-omissions-2026]{321}; both study facts and predicates, not
  approach families. `extends`
- People judging a presented structure under-weight what it leaves out: laypeople and experienced
  mechanics shown a pruned fault tree assigned far too little probability to its "all other" branch
  [fischhoff-slovic-lichtenstein-fault-trees-1978]{464}. This concerns reviewers of a given
  decomposition, not generators judging their own lists.
- Blind spots at the level of whole families recur through vocabulary mismatch
  [mahdabi-prior-art-query-2011]{254}, a single channel or seed set
  [erana-finlayson-neural-patent-landscaping-2024]{253} [wohlin-hybrid-search-snowballing-2022]{160},
  and staying within one's own domain [franke-poetz-schreier-analogous-markets-2014]{273}.

## 2. Generation strategies and their evidence

| Strategy | Evidence | Key limit |
|---|---|---|
| Objectives or purpose as the generation key | Measured: more and better alternatives [siebert-keeney-alternatives-2015]{450} {confidence: abstract-only}; purpose-fixed, mechanism-diverse retrieval beat keyword and random [hope-analogy-mining-purpose-mechanism-2017]{414} | Students, personal decisions; one 38-worker crowd study |
| Independent generation, then pooled union | Advocated (prescribed) [bond-carlson-keeney-improving-objectives-2010]{453}; demonstrated in one case where executives listed on average 36% of a 39-objective aggregate built from their pooled lists [bond-carlson-keeney-objectives-2008]{452} | "More complete than any one" holds by construction against a pooled reference, and says nothing about families every lister missed {inferred: aggregate}; a different model alone does not establish independent coverage [artificial-hivemind-homogeneity-2025]{307}, while distinct cues to one model raised coverage [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312} |
| Second pass with "first lists are incomplete" and a numeric target | Measured: +2.77 to +4.87 items, with no quality loss in the successful arms [bond-carlson-keeney-improving-objectives-2010]{453} | Objectives, one MBA population |
| See prior items, instruction to differ (LLM) | Measured: lowest similarity [meincke-prompting-idea-variance-2024]{300}; human-level distinctness [noveltybench-humanlike-diversity-2025]{310} | Caveats on model version; gains vanish as pools deplete |
| Distinct cue per draw (ordinary personas; persistent agent lenses) | Measured in single studies: personas raised between-session spread [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}; lens-anchored debate gained 26.2% semantic diversity over homogeneous debate, which itself fell below single-agent generation; a comparison with single-agent generation is not attested {inferred: absence} [creative-mad-debate-diversity-2026]{317} | One model or one preprint each; celebrity personas were mixed [meincke-prompting-idea-variance-2024]{300} |
| Categories as a second pass | Mixed: +30% self-generated in a second pass, but confounded with the second opportunity, and no reliable gain over a motivated deeper review [bond-carlson-keeney-improving-objectives-2010]{453} | Upfront categories did not reduce misses [bond-carlson-keeney-improving-objectives-2010]{453} |
| Abstraction for distant retrieval (compare two analogs; concrete constraint schemas) | Measured: 21% → 45% transfer [gick-holyoak-schema-induction-1983]{416}; relevant yet distant inspirations [kittur-scaling-analogical-innovation-2019]{415} | A review reports Zahner et al. finding that too-abstract framing lowers fit, and that the right balance is unclear [vasconcelos-crilly-inspiration-fixation-2016]{418} |
| Distant or analogous-domain sources | Mixed: novelty up and usability down [franke-poetz-schreier-analogous-markets-2014]{273}; contradictory lab results [chan-fu-analogy-distance-commonness-2011]{403} [fu-near-far-analogy-2013]{404} | No sweet spot was located in the attested sources {inferred: absence} |
| Morphological fields, design spaces (dimensions × values) | Advocated/demonstrated [ritchey-gma-general-method]{100} [shaw-petre-design-spaces-2024]{110} | Complete only within chosen dimensions [ritchey-psm-gma-2006]{263} |
| TRIZ, QOC, set-based design, strategy tables | Mixed or advocated [vargas-hernandez-triz-experiment-2012]{105} [buckingham-shum-dr-hypermedia-2005]{108} [toche-set-based-design-review-2020]{109} [usfws-usgs-sdm-developing-alternatives-2011]{458} | No coverage comparison in the attested sources {inferred: absence} |
| Taxonomy construction with ending conditions | Advocated (designed) [nickerson-taxonomy-development-method-2013]{200} | No attested test against later-found objects [szopinski-taxonomy-evaluation-criteria-2020]{202} {inferred: absence} |

Measured null or negative: a week of rumination for objectives [bond-carlson-keeney-objectives-2008]{452},
and more time for alternatives as reported by the university release [siebert-keeney-press-2015]{451};
upfront examples [bond-carlson-keeney-improving-objectives-2010]{453}; similarity feedback and
select-the-best pooling [meincke-prompting-idea-variance-2024]{300}; standard multi-agent debate,
including heterogeneous models, while judge-based voting over independent responses did not lower
diversity [creative-mad-debate-diversity-2026]{317}; temperature
[deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}. Exposure to AI ideas narrowed collective
diversity when writers received AI story ideas [doshi-hauser-genai-collective-diversity-2024]{302}, but
widened it in a dynamic multi-generation pool [ashkinaze-ai-ideas-collective-diversity-2024]{304}
{confidence: search-summary}. A reported student study associated larger morphological matrices with
lower-quality concepts [martinsson-bonde-mm-combinatorics-2025]{103}. Further advocated moves:
building an alternative around the best consequence for each objective, then hybrids
[usfws-usgs-sdm-developing-alternatives-2011]{458}; separating the person who abstracts a problem from
the person who searches [kittur-scaling-analogical-innovation-2019]{415}.

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
  the attested corpus. {inferred: absence} Search practice measures item recall against a known or
  pooled set [zhang-qgs-search-2011]{258} [sampson-relative-recall-2006]{163}, with a quasi-gold-standard
  stopping band of 70–80% that applies to items, not families [zhang-qgs-search-2011]{258}. Richness
  and coverage estimators have measured evaluations in their own settings: ecological subsampling and
  simulation [chao-sufficient-sampling-2009]{352} [chao-hill-numbers-rarefaction-2014]{351}, fuzzing
  against true path richness [bohme-stads-species-discovery-2018]{359} and inspections against known true
  defect counts [briand-capture-recapture-inspections-2000]{362}; vocabulary applications report model fit
  rather than a known total [efron-thisted-shakespeare-unseen-1976]{355}.
- **Frame-relativity.** Estimates are relative to the generating process
  [kornish-ulrich-opportunity-spaces-2011]{361} [meincke-prompting-idea-variance-2024]{300}, the
  identity threshold [kornish-ulrich-opportunity-spaces-2011]{361}, the declared dimensions
  [ritchey-psm-gma-2006]{263} and the known set [cochrane-handbook-ch4-searching-2025]{151}. A held-out
  known set guards against circularity [hausner-objective-search-strategy-2012]{164}, and re-finding
  items the team did not know in advance is the informative signal
  [cochrane-handbook-ch4-searching-2025]{151}.
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
  Whether capture–recapture is usable for judging closeness to a total is itself contested
  [kastner-cmr-stopping-rule-2009]{166} [rucker-boosting-capture-recapture-2011]{168} {confidence:
  abstract}.
- **What small samples support.** Sample coverage — the share of total abundance or incidence
  probability belonging to observed kinds, not the share of kinds observed — is estimable when the number
  of missing kinds is not [chao-hill-numbers-rarefaction-2014]{351}; it is computed from the same
  singleton and doubleton counts, so it shares their sampling assumptions
  [chao-colwell-chao2-inequality-2017]{350}. In one review, missed papers would have added three new
  categories [kitchenham-slr-repeatability-2011]{375}, so new items opening new categories is a signal
  of missing kinds measured in one case.
- **Stopping rules that fail or are untested.** In screening, the baseline-rate heuristic missed the 95% recall target in
  39.67% of runs and the 50-consecutive-misses heuristic in 39% [callaghan-statistical-stopping-2020]{170};
  median coverage at thematic-saturation stopping points was 78–82% of observed themes
  [guest-thematic-saturation-method-2020]{173}; several taxonomy ending conditions check stability over
  the last iteration, alongside MECE, sample and populated-cell conditions, and the method's
  demonstration used a selected two [nickerson-taxonomy-development-method-2013]{200}. Reading these as
  evidence about a quiet challenge pass is a transfer. `extends` Reliable screening stopping
  reports confidence across a range of recall targets rather than one verdict
  [callaghan-stopping-recommendations-2024]{171}.
- **Diversity-seeking and estimation pull apart.** A diversity-seeking pass produces singletons by
  design, removing the repetition the estimators assume [van-rijnsoever-saturation-simulation-2017]{358}
  [chao-colwell-chao2-inequality-2017]{350}. {inferred: tension}
- **Detecting absence.** Models detected planted over-inclusions "6-7x more often than planted
  omissions" and judged presented candidates much more accurately than they authored the set, in
  one-shot settings with a reference [judging-not-enumerating-omissions-2026]{321}; placeholders marking
  where content was removed raised omission detection by 35.7% on a surface benchmark
  [fu-absencebench-omission-2025]{365}; human testers detected more commission than omission faults in one
  experiment [aguilar-fault-type-code-review-2025]{370} {confidence: abstract-only}. Disagreement between
  passes is partly classification: 23–24% retrieval overlap alongside kappa 0.66–0.82 classification
  agreement [el-emam-defect-classification-repeatability-1998]{372}.
- **No attested stopping rule for families.** None of the eight facets reports a validated rule for
  deciding that a sample of approach families is complete enough to stop challenging it. {inferred:
  absence} Recommendation 10 below offers an escalation trigger as an inference, not a tested rule.

## 5. Adoption recommendations for the consuming primer

These map findings onto the consumer's four steps. Each is conditional on the cited evidence and on
transfer to approaches being analogical; none is shown in the attested sources for methodology
reviews specifically. `extends`

**Domain map.**
1. Start from jobs, outcomes and objectives, and use them as the generation key; derive decision
   dimensions from that purpose and admit only discriminating ones
   [siebert-keeney-alternatives-2015]{450} {confidence: abstract-only}
   [nickerson-taxonomy-development-method-2013]{200}.
2. Use several independent retrieval routes with vocabulary expansion, and at least one adjacent-field
   route at a workable abstraction (purpose fixed, mechanism varied; compare two analogs)
   [zhang-qgs-search-2011]{258} [mahdabi-prior-art-query-2011]{254}
   [hope-analogy-mining-purpose-mechanism-2017]{414} [gick-holyoak-schema-induction-1983]{416}. Decide
   the map's scope explicitly: landscape traditions differ on covering "an entire population"
   [smith-ripl-statement-2018]{251} versus "a handful of the most important technical approaches"
   [wipo-plr-guidelines-trippe-2015]{250}.
3. State the frame explicitly — dimensions, identity rule for "same family", generators used — because
   every completeness claim is relative to it [kornish-ulrich-opportunity-spaces-2011]{361}
   [ritchey-psm-gma-2006]{263}. Keep a held-out set of known families (for example, families named in
   prior reviews) out of map-building, to check the map against later
   [hausner-objective-search-strategy-2012]{164}.

**Charter sample.**
4. Draw so that every value of each declared dimension appears at least once ("full field coverage",
   which covers parameter values, not all configurations) [ritchey-psm-gma-2006]{263}. A university
   release reports that, in a paper-title task, a few clearly distinguishable alternatives scored better
   than many similar ones [siebert-novices-press-2016]{454}; that is a secondary report from another task,
   and it sits in tension with objectives-based generation raising the number of alternatives
   [siebert-keeney-alternatives-2015]{450} {confidence: abstract-only}, so favouring distinct families over
   near-duplicates is a transfer, not a tested rule. Do not select by how often a family is proposed,
   which keeps the commonest [naik-div-se-diversity-of-thought-2023]{314}.
5. Name a different family by divergence at the principle level or on a declared dimension, not by
   surface features [sorensen-ideation-metrics-axioms-2026]{113}.

**Completeness challenge.** The order matters: steps (a) and (b) are independent of the sample;
steps (c) and (d) use it.
6. (a) Have the challenger enumerate families independently, before seeing the sample or the map's
   candidate list. Upfront examples increased misses in an objectives experiment, and independent
   generation before discussion is the prescribed order [bond-carlson-keeney-improving-objectives-2010]{453};
   whether a challenger is anchored by the sample it challenges is untested (see Open questions).
   `extends`
7. (b) Give the challenger distinct cues from the sample's author (different purpose framings, perspectives or
   adjacent fields), and push it with a second pass that states first lists are typically incomplete and
   sets a numeric target [bond-carlson-keeney-improving-objectives-2010]{453}. A different model alone
   does not establish independent coverage [artificial-hivemind-homogeneity-2025]{307}, while distinct cues
   raised coverage within one model [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}; which
   persona type helps is mixed [meincke-prompting-idea-variance-2024]{300}.
8. (c) Then compare the challenger's pre-exposure list with the sample. Overlap and additions are
   computed from that list only, so exposure does not inflate them. (d) Separately, present candidate
   families from the map for membership judgement, which models did more accurately than enumeration in
   one-shot settings with a reference [judging-not-enumerating-omissions-2026]{321}, and make absences
   visible, for example empty cells in the dimension grid; placeholder gains were measured for surface
   deletions with both documents available [fu-absencebench-omission-2025]{365}
   [nickerson-taxonomy-development-method-2013]{200}. Judging map candidates can only reveal gaps between
   the sample and the map, not families the map itself lacks; reviewers of a presented structure
   under-weight what it omits [fischhoff-slovic-lichtenstein-fault-trees-1978]{464}.
9. Report a descriptive, frame-relative coverage statement rather than "complete". The primary signal
   comes from the challenger's pre-exposure list, counted after the family-versus-variation adjudication
   of recommendation 5, in two parts: (i) families **absent from the map**, and whether they open new
   dimensions [kitchenham-slr-repeatability-2011]{375} or empty cells [nickerson-taxonomy-development-method-2013]{200}; (ii) families **on the map but not
   sampled**, and whether each carries a dimension value the sample does not cover (intended exclusions
   under recommendation 4 are expected and are not gaps). Record whether each addition came from the
   unforced or the targeted pass of recommendation 7. Report alongside: the adjudicated observed union;
   overlap between the pre-exposure list and the sample; held-out known families absent from the map
   [hausner-objective-search-strategy-2012]{164}; new families per pass
   [wohlin-hybrid-search-snowballing-2022]{160}; classification-boundary decisions; and the frame. Keep the
   observed count distinct from any estimated total. No model-based estimate, including sample coverage,
   is supported for these passes, because the sample is a purposive draw from the map rather than a
   capture, there are only two or three occasions where inspection guidance advises four or more unless shown to work
   in a particular environment
   [briand-capture-recapture-inspections-2000]{362}, and shared model priors may correlate the passes
   [artificial-hivemind-homogeneity-2025]{307}, against the independence capture–recapture assumes
   [bron-chao-estimator-tar-2024]{169}. {inferred: aggregate} Avoid "nothing new in the last pass" as a
   completeness claim [callaghan-statistical-stopping-2020]{170}.
10. Match each trigger to its remedy. Families absent from the map (part (i)), or held-out known
    families absent from the map, trigger a **map refresh** and a re-challenge of the affected decisions.
    On-map families carrying an uncovered dimension value (part (ii)) trigger a **sample revision**. If
    the held-out families are also used to test the challenger, a challenger that misses held-out
    families gives a quiet result that is weak evidence of completeness, and the remedy is a **stronger challenge** (more distinct cues, another
    targeted pass), not a map refresh. Proceeding to depth research is otherwise a judgement by the review's
    operator, informed by the coverage statement, since no attested rule decides it. Run any re-challenge or
    stronger challenge as a fresh pass under recommendations 6–8, not by the already-exposed challenger.
    Under recommendation 4's full field coverage, part (ii) fires only when the draw missed a value or
    adjudication reclassified a family; and because full field coverage covers single values, not
    combinations, part (ii) cannot flag a family distinguished only by an uncovered combination. `extends`
11. Separate retrieval gaps from classification disagreements (merged or split families) when passes
    disagree [el-emam-defect-classification-repeatability-1998]{372}
    [briand-capture-recapture-inspections-2000]{362}.

**Per-facet research briefs.**
12. Ask each facet to seek maximum variation and disconfirming cases rather than "more of the same"
    [booth-qes-searching-2016]{155}, to record vocabulary differences, and to report whether new sources
    open new categories [kitchenham-slr-repeatability-2011]{375}. A reported new category feeds back as
    a map refresh and a re-challenge of the decisions it touches. `extends`

## Contradictions

| Relationship | Positions |
|---|---|
| `contradicts` | Far-field examples raised novelty [chan-fu-analogy-distance-commonness-2011]{403}; far stimuli lowered novelty and quality [fu-near-far-analogy-2013]{404}. |
| `tension` | Exposure to AI story ideas narrowed collective diversity [doshi-hauser-genai-collective-diversity-2024]{302}; high exposure widened it in a dynamic multi-generation pool [ashkinaze-ai-ideas-collective-diversity-2024]{304} {confidence: search-summary}; designs differ. |
| `tension` | Diversity-seeking sampling advocated for kinds [booth-qes-searching-2016]{155} versus estimators that need random-like repetition [chao-colwell-chao2-inequality-2017]{350} [van-rijnsoever-saturation-simulation-2017]{358}. |
| `tension` | Perspective-based review minimises reviewer overlap [regnell-pbr-perspectives-different-2000]{367}; capture–recapture needs overlap [briand-capture-recapture-inspections-2000]{362}. |
| `tension` | Capture–recapture presented as usable for judging closeness to the total [kastner-cmr-stopping-rule-2009]{166} {confidence: abstract-only} versus estimates varying markedly with model choice [rucker-boosting-capture-recapture-2011]{168} {confidence: abstract-only}. |
| `tension` | A landscape covers "an entire population of relevant data" [smith-ripl-statement-2018]{251} versus narrowing to "a handful of the most important technical approaches" [wipo-plr-guidelines-trippe-2015]{250}. |
| `qualifies` | Ordinary personas beat "creative entrepreneur" personas in one study [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}; celebrity and entrepreneur personas modestly helped in another [meincke-prompting-idea-variance-2024]{300}. |
| `tension` | Few distinct alternatives scored better than many similar ones (university release) [siebert-novices-press-2016]{454} versus objectives raising the number and quality of alternatives [siebert-keeney-alternatives-2015]{450} {confidence: abstract-only}. |
| `qualifies` | Within one source: categories coincided with gains as a second pass, confounded with the second opportunity, and added no reliable gain over a motivated deeper review; upfront they did not reduce misses [bond-carlson-keeney-improving-objectives-2010]{453}. |
| `qualifies` | Generating more options was associated with lower mean option quality, and for time-pressured experts with poorer, less consistent choices (Johnson and Raab, as reported) [delmissier-option-generation-ideation-2015]{459}, versus higher best-option quality in some problems [delmissier-option-generation-ideation-2015]{459} and higher maximum but not mean originality between persons [schweizer-creative-option-generation-2016]{460}; correlational, mean versus max, populations differ. |
| `tension` | Morphological "totality research" [ritchey-gma-general-method]{100} versus design spaces as "helpful—but incomplete" [shaw-petre-design-spaces-2024]{110}. |
| `incommensurable` | LLM diversity below humans [wenger-kenett-creative-homogeneity-llms-2025]{306} versus matching or exceeding humans under some prompts [noveltybench-humanlike-diversity-2025]{310}; different metrics and domains. |

## Disconfirming analysis

- *A structured decomposition guarantees a complete set.* Not supported: completeness is relative to
  the frame [ritchey-psm-gma-2006]{263}, and no attested study shows a structured generator finding more
  distinct families than an unstructured expert list. {inferred: absence}
- *An independent challenger reliably finds what is missing.* Weakened: models detected omissions far
  less often than commissions [judging-not-enumerating-omissions-2026]{321}; more perspectives did not find
  different defects [regnell-pbr-perspectives-different-2000]{367}; Chao-type estimates are lower bounds
  under heterogeneous detection, with wide intervals from few sampling units
  [chao-colwell-chao2-inequality-2017]{350}. The pooling case shows independent lists jointly exceed any
  one list, but against a reference built from those same lists [bond-carlson-keeney-objectives-2008]{452},
  so it says nothing about families every lister missed. {inferred: aggregate}
- *Purpose-first generation is a reliable key.* Supported by one study set at abstract and
  press-release depth [siebert-keeney-alternatives-2015]{450} {confidence: abstract-only} and one 38-worker
  crowd study [hope-analogy-mining-purpose-mechanism-2017]{414}; no contrary result was found in the attested sources. {inferred: absence}
- *A warning-plus-target second pass generalises.* Measured in one MBA population on objectives
  [bond-carlson-keeney-improving-objectives-2010]{453}; untested on approach families.
- *Judging beats enumerating.* Measured for models in one-shot settings with a reference
  [judging-not-enumerating-omissions-2026]{321}; untested for open approach families.
- *Full field coverage gives an adequate sample.* Demonstrated by its developer only
  [ritchey-psm-gma-2006]{263}; it covers declared values, not unseen dimensions.
- *Incompleteness of the sample matters.* The objectives authors disclaim direct evidence that
  incompleteness degrades decisions [bond-carlson-keeney-objectives-2008]{452}, while overlooked
  alternatives were of equal average quality [siebert-keeney-alternatives-2015]{450} {confidence:
  abstract-only}.
- *Using a language model makes the sample broader.* Disconfirmed for default sampling and standard
  debate [artificial-hivemind-homogeneity-2025]{307} [creative-mad-debate-diversity-2026]{317}; for model
  ensembles the source cautions they "may not" diversify given shared priors, without measuring marginal
  additions [artificial-hivemind-homogeneity-2025]{307}; supported only under specific prompting regimes
  [noveltybench-humanlike-diversity-2025]{310}.

## Open questions

- Whether a challenger shown the sample it is challenging is anchored by it, as upfront examples
  anchored generators [bond-carlson-keeney-improving-objectives-2010]{453}.
- When to stop challenging and begin depth research: no attested rule exists for families of approaches.
- How near-duplicate approaches should be merged before counting families, given that counts depend on
  the identity threshold [kornish-ulrich-opportunity-spaces-2011]{361}.
- Whether omission detection on semantic absences, such as missing approach families, behaves like
  surface omission [fu-absencebench-omission-2025]{365}.
- How problem framing and reformulation change which families are generated; held only through
  cite-through [vasconcelos-crilly-inspiration-fixation-2016]{418}.

## Revisit if

- A study validates any completeness estimator, stopping rule or ending condition against later-found
  kinds of methods or approaches.
- The full text of Siebert and Keeney (2015) is acquired, or the act-generation study that
  [delmissier-option-generation-ideation-2015]{459} cites as Gettys et al. (1987).
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
- **2026-10-20 — correction (adversarial re-check 2).** "Seeded" is replaced by the attested "known true defect counts" (R2).
- **2026-10-20 — correction (evaluate round 1).** Stopping and escalation are addressed as an inferred
  trigger and an open question, with a feedback path from depth facets (C1, C2). The challenge
  sequencing, the primary signal, the held-out known-set signal, the per-pass yield and the statement
  that no estimate is supported for the described passes are added to recommendations 6–10 (H1, C3, H3,
  H5). The fault-tree evidence is reframed (H2). The certification wording is fixed (H4). The pooling
  case is marked circular against its pooled reference (H6). Terms are defined and evidence vocabulary
  normalized (H7). The doshi-hauser exposure finding is restored (X1). The anchoring open question is
  restored and recommendation 6 marked `extends` (X2). The scope, persona, capture–recapture and
  distinct-versus-number tensions are carried (X3, C5). The QGS band is noted as item-level (C4).
  Absence, `extends` and transfer markers replace prose notes (G1–G3, G5, G6). The omission claim rests
  on models, with the human study at abstract depth (G4). Gettys is grounded through a cite-through
  (G7). Duplicate `{N}` numbers were verified to resolve to the same attestation (G8). Dropped
  qualifiers are restored (G9). Positive prescriptions now have disconfirming entries (G10).
- **2026-10-20 — correction (evaluate round 2).** The primary signal is split into absent-from-map and
  on-map-but-unsampled parts, counted after adjudication and tagged by pass, and each escalation
  trigger is matched to its remedy (N1). The reasons no estimate is supported are stated (purposive
  sample, few occasions, correlated priors). Marker form: `extends` replaces `{inferred: extends}`.
  Notes addressed: "on average" restored, lens-debate baseline, heading, Kastner/Rücker confidence
  markers, Johnson and Raab side restored, absence marker, "Prescribed" mapped to advocated, "author"
  clarified.
- **2026-10-20 — correction (evaluate round 3 notes).** Marker prose is trimmed. The depth label on the exposure finding is corrected. The inspector exception is carried into rec 9. An absence marker is added. Empty cells are cited to Nickerson. Re-challenges are fresh passes, and the part (ii) firing conditions and combination limit are stated in rec 10.
