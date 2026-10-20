---
title: "Cluster synthesis — completeness: judging whether a set of kinds is complete"
provenance: agent-synthesis
updated: 2026-10-20
summary: >-
  Cross-specialist synthesis over four facets (search completeness, coverage estimation, taxonomy
  construction, landscape mapping) on how a sample of approaches or kinds can be checked for
  completeness before depth work. Across the fields, completeness of the process, recall of items
  against a known set, and completeness of the set of kinds or families are distinct quantities.
  For families of methods or approaches, only the first two have measured practice in the attested
  corpus; richness estimators are evaluated in their own settings (species, words, code paths,
  defects). Every estimate is relative to a frame (the generating process, the identity threshold for a
  kind, the chosen dimensions, the known set), and each estimator has its own inputs: two or more
  captures for capture–recapture, replicated units for incidence data, frequency counts for abundance
  data, or a random sample of the remainder for screening tests. "No new items in the
  last run" rules measurably fail or are unvalidated. Omissions are detected markedly less often
  than wrong inclusions by humans and models, and disagreement between passes is partly
  classification rather than retrieval.
key_findings:
  - No attested source validates a completeness estimate for families of methods or approaches; measured practice there covers item recall against a known or pooled set, while richness estimators are evaluated for species, words, code paths and defects.
  - Chao-type estimators give lower bounds under heterogeneous detection; sample coverage (share of abundance or incidence probability already represented, not share of kinds) is more robustly estimable than the number of missing kinds.
  - Every completeness figure is conditional on the generating process, the identity threshold that merges near-duplicates, the rank counted and the frame of dimensions or known items.
  - Estimator inputs differ: capture–recapture needs two or more captures treated as independent, incidence estimators replicated units, abundance estimators frequency counts, screening tests a random sample of the remainder; few occasions widen intervals, and inspection studies advise against fewer than four inspectors unless shown to work in a particular environment.
  - Stopping when the last run added nothing missed recall targets in about 39% of screening runs and left 18–22% of observed themes unseen at qualitative stopping points.
  - Missing items can mean missing categories; independent maps of one topic overlap little, and part of their disagreement is classification, not retrieval.
  - Omission detection is a weaker capability than commission detection for humans and models; marking where content is absent recovered much of the gap in one benchmark.
---

# Completeness cluster: judging whether a set of kinds is complete

## Scope and inputs

This synthesis composes four within-specialist briefs of the `solution-space-decomposition`
campaign: search completeness in evidence synthesis, coverage estimation for samples of kinds,
taxonomy construction, and landscape mapping. It asks what each field treats as a completeness
signal for a set of approaches or kinds, what that signal assumes, and how strong its evidence is.
Evidence levels follow the specialist briefs: **advocated** (proposed or recommended without a test
against truth), **demonstrated** (worked cases, no ground truth), **measured** (quantified against a
known or reconstructed truth, in simulation, benchmarks or experiments). Claims rest on the
attestations cited; abstract-level sources are marked where the specialist marked them.

## 1. Three different completeness quantities

The fields keep apart three things that a single word "complete" can conflate:

1. **Process completeness** — whether the search or construction process is fully reported and
   reproducible. PRISMA-S governs this, and contains no item for how complete the retrieved set is
   [prisma-s-rethlefsen-2021]{150}; the RIPL landscape checklist likewise requires search terms,
   sources, counts and limitations, but "does not extend to recommendations regarding methodologies"
   [smith-ripl-statement-2018]{251}.
2. **Item recall against a reference set** — how much of a known, pooled or held-out set a search
   retrieves. This is where measured practice is concentrated: relative recall across Cochrane
   reviews [sampson-relative-recall-2006]{163}, quasi-gold-standard sensitivity with a 70–80%
   stopping band [zhang-qgs-search-2011]{258}, 83% sensitivity against hand-searched journals in
   horizon scanning [varela-lema-emerging-tech-search-2012]{270} {confidence: abstract}.
3. **Completeness of the set of kinds or families** — whether every distinct kind of approach is
   represented. The landscape-mapping specialist found no attested tradition that reports a
   validated estimator for this quantity, as opposed to recall of items within known families
   [zhang-qgs-search-2011]{258} [wipo-plr-guidelines-trippe-2015]{250} [ritchey-psm-gma-2006]{263}
   {inferred: convergence}. The taxonomy specialist found no taxonomy ending condition tested against
   objects found later [nickerson-taxonomy-development-method-2013]{200}
   [szopinski-taxonomy-evaluation-criteria-2020]{202}.

The ecological estimators of Section 3 are the closest formal treatment of the third quantity;
their validity for kinds of methods or approaches is untested in the attested sources
[chao-colwell-chao2-inequality-2017]{350} {inferred: absence across the coverage-estimation sources}.

## 2. Completeness signals and their evidential status

| Signal | What it reports | Main assumption or limit | Evidence |
|---|---|---|---|
| Known-item check | Share of known key items found | Biased toward what is already known [cochrane-handbook-ch4-searching-2025]{151} | advocated |
| Relative recall / pooled recall | A route's share of the union of routes | Capped by the union; "actual recall could be close to zero" [sampson-relative-recall-2006]{163} | measured (relative) |
| Held-out known set | Recall on items withheld from strategy-building | Needs prior comprehensive reviews [hausner-objective-search-strategy-2012]{164} | demonstrated |
| Quasi-gold standard | Recall against a manually searched venue set | Relative to those venues and period [zhang-qgs-search-2011]{258} | measured (two cases) |
| Capture–recapture | Estimated number missing, with interval | Independent passes; model choice swings estimates [kastner-cmr-horizon-2007]{165} [rucker-boosting-capture-recapture-2011]{168} | demonstrated; sensitivity measured |
| Chao1/Chao2 (f1/f2) | Lower bound on the total number of kinds | Exact only under homogeneous detection [chao-colwell-chao2-inequality-2017]{350} | measured (ecology; inspections; screening simulation) |
| Good–Turing sample coverage | Share of the population already represented | Not a count of missing kinds [chao-hill-numbers-rarefaction-2014]{351} | measured |
| Hypergeometric stopping test | "Recall ≥ target" at a confidence level | Random sample of the unseen remainder [callaghan-statistical-stopping-2020]{170} | measured |
| "No new items in N" / baseline rate | Run of non-yield | Ignores the size of the remainder [callaghan-statistical-stopping-2020]{170} | measured (often fails) |
| Thematic saturation metric | New themes per run relative to a base | "No guarantee" [guest-thematic-saturation-method-2020]{173} | measured retrospectively |
| Taxonomy ending conditions | MECE; all or a representative sample of objects examined; populated characteristics; unique cells; no change in the last iteration | None tested against later-found objects; the demonstration used a selected two [nickerson-taxonomy-development-method-2013]{200} | designed |
| Full field coverage | Sample covers every value of every dimension | Relative to the chosen dimensions [ritchey-psm-gma-2006]{263} | demonstrated |
| Agreement across independent character sets (Whewell) | Robustness of class boundaries | Stated as a maxim [hjorland-classification-2017]{205} | advocated |
| Overlap between independent repetitions | Low overlap signals unseen items | Disagreement is partly classification [kitchenham-slr-repeatability-2011]{260} [el-emam-defect-classification-repeatability-1998]{372} | measured |
| New items fall into new categories | Missing items imply missing kinds | Shown in one review [kitchenham-slr-repeatability-2011]{260} | measured (one case) |

{inferred: aggregate — rows are composed from the cited attestations; evidence labels follow the
specialist briefs.}

## 3. Convergent findings

### 3.1 Every completeness figure is relative to a frame

Four facets independently reach the same conclusion: a completeness figure is meaningful only
relative to a frame that the estimate itself cannot validate.

- **Generating process.** Idea-space estimates are "the total number of ideas" reachable by one
  process, and "Different processes would result in different sizes"
  [kornish-ulrich-opportunity-spaces-2011]{361}; applied to GPT-4 idea pools they estimate "only the
  possible number of unique ideas that can be found with a particular technique"
  [meincke-prompting-idea-variance-2024]{363}. In fuzzing, claims hold "w.r.t. that fuzzer", and
  unreachable kinds are missed entirely [bohme-stads-species-discovery-2018]{359}.
- **Identity threshold.** Kornish and Ulrich's count depends on 50% or 70% rater-agreement cutoffs
  they call "arbitrary" [kornish-ulrich-opportunity-spaces-2011]{361}; higher ranks saturate before
  lower ones [gotelli-colwell-quantifying-biodiversity-2001]{353}.
- **Chosen dimensions.** Morphological "totality" is "no better than the quality of its input"
  [ritchey-psm-gma-2006]{263}; the taxonomy meta-characteristic "impacts critically the resulting
  taxonomy" [nickerson-taxonomy-development-method-2013]{200}, and classification routes (logical
  division, similarity, genealogy, purpose) can yield different classes for the same objects
  [hjorland-classification-2017]{205}.
- **Known set.** Known-item and relative-recall checks cannot detect items every route missed
  [cochrane-handbook-ch4-searching-2025]{151} [sampson-relative-recall-2006]{163}; a family absent
  from the quasi-gold standard cannot lower its score [zhang-qgs-search-2011]{258} {inferred: tension
  noted by the landscape specialist}.

### 3.2 Each estimator has its own inputs and independence assumptions

Capture–recapture needs at least two searches treated as captures
[cochrane-handbook-ch4-searching-2025]{151}; incidence estimators need replicated sampling units and
abundance estimators frequency counts of individuals from one sample
[chao-colwell-chao2-inequality-2017]{350} [chao-hill-numbers-rarefaction-2014]{351}; the screening
stopping test needs a random sample of the unseen remainder [callaghan-statistical-stopping-2020]{170}.
Overlap estimators read items found once versus twice and assume passes behave like independent
captures [bron-chao-estimator-tar-2024]{169}. Webster and Kemp's design, as Bron et al. describe it,
uses independent searchers as the passes [bron-chao-estimator-tar-2024]{169}. Few passes give wide
intervals and underestimates: a Chao2 of 36.3 from 12 units carried a 95% interval of 29.1 to 68.8
[chao-colwell-chao2-inequality-2017]{350}, inspection estimates "ought not be used with less than 4
inspectors unless shown to work in a particular environment", while other capture–recapture models
could overestimate severely or fail to produce an estimate [briand-capture-recapture-inspections-2000]{362}, and singleton methods underestimate at
1–5% sampling fractions [schmitz-rahmann-richness-estimation-review-2025]{357} {confidence:
extractor-level}. Adaptive samplers bias estimates downward
[bohme-residual-risk-greybox-2021]{360}.

### 3.3 "Nothing new in the last run" is not evidence of completeness

- In technology-assisted screening, stopping after 50 consecutive irrelevant items or at a baseline
  rate missed the 95% recall target in about 39% of runs [callaghan-statistical-stopping-2020]{170};
  the 5th-percentile recall of the consecutive-miss rule fell to 53%
  [callaghan-stopping-recommendations-2024]{171}.
- At the typical thematic-saturation stopping point, median coverage of the full dataset's themes
  was 78–82%, and the authors state that meeting the thresholds is "no guarantee"
  [guest-thematic-saturation-method-2020]{173}. Code saturation (9 interviews) arrived before meaning
  saturation (16–24) [hennink-code-meaning-saturation-2017]{174}.
- Several taxonomy ending conditions are stability checks over the last iteration, alongside MECE,
  representative-sample and populated-cell conditions; the method's own demonstration used a selected
  two conditions and stopped after one no-change iteration over a convenience sample, and none is
  tested against later-found objects [nickerson-taxonomy-development-method-2013]{200}.
- Snowballing can stop early after a thin round and depends on its start set
  [wohlin-hybrid-search-snowballing-2022]{160}; seed expansion cannot reach regions with no link to
  the seeds [erana-finlayson-neural-patent-landscaping-2024]{253}.

The measured alternative in screening is a hypothesis test on a random sample of the remainder, which
reached its stated confidence at the cost of extra screening; the 2024 consensus asks for confidence
across a range of recall targets rather than one verdict
[callaghan-statistical-stopping-2020]{170} [callaghan-stopping-recommendations-2024]{171}.

### 3.4 Missing items can mean missing kinds, and independent maps disagree

Two independent novice reviews shared 6 of 32 papers, and papers an expert review missed "would have
had an impact ... by adding three new categories to the framework"
[kitchenham-slr-repeatability-2011]{375}. Two mapping studies of one topic differed in included
papers and in classification [wohlin-mapping-reliability-2013]{161} {confidence: abstract}; an SLR and
its replication shared 20 papers [wohlin-hybrid-search-snowballing-2022]{160}. Disagreement has two
separable parts: in inspections only 23–24% of defects were found by both inspectors, while
classification agreement on the shared defects was kappa 0.66–0.82
[el-emam-defect-classification-repeatability-1998]{372}; with trained students, classification
discrepancy averaged 43% even though 97% of responses gave exactly one category
[falessi-odc-feasibility-2006]{209}. Matching duplicates across passes is itself a classification
step that needed consolidation by two people [briand-capture-recapture-inspections-2000]{362}.

### 3.5 Recurring causes of missing families

Across landscape and search practice, the named causes of whole families going missing are:
vocabulary mismatch [mahdabi-prior-art-query-2011]{254} [zhang-qgs-search-2011]{258}; a single search
channel or venue set [zhang-qgs-search-2011]{258} [ogilvie-finding-evidence-2005]{157} {confidence:
abstract}; seed or start-set dependence [erana-finlayson-neural-patent-landscaping-2024]{253}
[wohlin-hybrid-search-snowballing-2022]{160}; staying within one's own market or domain
[franke-poetz-schreier-analogous-markets-2014]{273}; and classification schemes built for another
purpose [wipo-plr-guidelines-trippe-2015]{250}. Diversification moves — maximum variation and
disconfirming or negative cases rather than "more of the same" — are advocated for samples of kinds
in qualitative synthesis [booth-qes-searching-2016]{155}.

## 4. Detecting what is missing

- **Omission is the weaker capability.** Models detected planted over-inclusions "6-7x more often
  than planted omissions" [judging-not-enumerating-omissions-2026]{366}. On AbsenceBench,
  Claude-3.7-Sonnet reached 69.6% F1 at identifying removed content and model averages ranged from
  71.2% down to 14.7%; reasoning added 7.9%, while placeholders
  marking where content was removed added 35.7% [fu-absencebench-omission-2025]{365}. The benchmark
  covers surface omission only, and its authors expect semantic absences to be harder
  [fu-absencebench-omission-2025]{365}. Human testers detected more commission than omission faults in
  one experiment [aguilar-fault-type-code-review-2025]{370} {confidence: abstract}.
- **Structured review helps conditionally.** Defect-class scenarios beat ad hoc and checklist reading
  in the original experiment, while checklists were no better than ad hoc
  [porter-votta-basili-detection-methods-1995]{368}; perspective-based reading's distinct perspectives
  did not find different defects [regnell-pbr-perspectives-different-2000]{367}; and two- and
  four-person inspections did not differ [inspection-team-size-experiment]{371}.
- **Agreement is not correctness.** Two coders "can reliably agree while both under-applying a code"
  [liu-agreement-not-quality-coding-2026]{377} (single verifier).

## Contradictions

| Relationship | Positions |
|---|---|
| `tension` | Diversity-seeking sampling is advocated for samples of kinds [booth-qes-searching-2016]{155} and reaches every code in fewer steps, but "only yields between 1 and 3 observations per code" [van-rijnsoever-saturation-simulation-2017]{358}; frequency-count estimators read singletons as evidence of unseen kinds and assume random sampling [chao-colwell-chao2-inequality-2017]{350}. A diversity-seeking pass produces singletons by design, so its f1/f2 lose their random-sampling meaning (coverage-estimation specialist, marked inferred there). |
| `tension` | Perspective-based reading aims to minimise overlap between reviewers [regnell-pbr-perspectives-different-2000]{367}; capture–recapture needs overlap and independence [briand-capture-recapture-inspections-2000]{362}. |
| `tension` | RIPL defines a landscape as covering "an entire population of relevant data" [smith-ripl-statement-2018]{251}; WIPO advises narrowing large topics "to a handful of the most important technical approaches" [wipo-plr-guidelines-trippe-2015]{250}. |
| `incommensurable` | WIPO's recall target above 90% is not tied to a measurement procedure in the passages read [wipo-plr-guidelines-trippe-2015]{250}; Zhang's 70–80% band is relative to a constrained known set [zhang-qgs-search-2011]{258}. |
| `tension` | Capture–recapture presented as usable for judging closeness to the total [kastner-cmr-stopping-rule-2009]{166} {confidence: abstract} versus model choice producing estimates "varying markedly" [rucker-boosting-capture-recapture-2011]{168} {confidence: abstract}. |
| `qualifies` | Mills's claim that inductive and faceted routes give "remarkably similar" results is unsupported per Hjørland, who holds the routes produce different classifications [hjorland-facet-analysis-2013]{203}. |
| `tension` | Checklists no better than ad hoc reading [porter-votta-basili-detection-methods-1995]{368} versus PBR teams less effective than checklists [ciolkowski-pbr-meta-analysis-2009]{369} {confidence: abstract}; different outcome levels and comparators. |

## Disconfirming analysis

- *A structured generator yields a complete set of kinds.* Not supported: morphological completeness
  is relative to the parameters chosen [ritchey-psm-gma-2006]{263}; no attested study shows
  keywording, morphological fields or roadmap layers finding more distinct families than an
  unstructured expert list (absence reported by the landscape specialist)
  [zhang-qgs-search-2011]{258} [franke-poetz-schreier-analogous-markets-2014]{273}.
- *A completeness estimate can certify a sample of approaches.* Not supported for kinds of approaches:
  estimator validity is demonstrated for species, words, code paths, defects and screening, and the
  near-unbiased condition is not shown to hold for approaches
  [chao-colwell-chao2-inequality-2017]{350}; idea-space estimates have no known-truth comparison
  [kornish-ulrich-opportunity-spaces-2011]{361}.
- *More reviewers or perspectives find more missing items.* Mixed: perspectives did not differ
  [regnell-pbr-perspectives-different-2000]{367} and four reviewers were no better than two
  [inspection-team-size-experiment]{371}, while scenario reading raised detection in its original
  experiment [porter-votta-basili-detection-methods-1995]{368}.
- *Comprehensive searching is the quality marker.* Contested by guidance reviews and by purposive
  sampling traditions [cooper-search-process-guidance-2018]{152} [booth-qes-searching-2016]{155}.

## Transfer-relevant observations

Stated in the source fields' own terms; not recommendations.

- The fields report process completeness, item recall and kind completeness separately. Where an
  estimator's assumptions hold, kind counts are reported as model-based estimates with intervals —
  Chao-type values as lower bounds under heterogeneity — conditional on process, identity threshold and
  frame; observed counts are kept distinct from estimated totals
  [chao-colwell-chao2-inequality-2017]{350} [kornish-ulrich-opportunity-spaces-2011]{361}.
- Sample coverage and short-range extrapolation are treated as estimable from small samples, while
  the total number of kinds is not [chao-hill-numbers-rarefaction-2014]{351}
  [orlitsky-suresh-wu-unseen-species-2016]{354}.
- The measured "something is missing" signals are recall against an independently built known set,
  overlap between independent repetitions, whether new items open new categories or empty cells, and
  yield per iteration [kitchenham-slr-repeatability-2011]{375} [zhang-qgs-search-2011]{258}
  [wohlin-hybrid-search-snowballing-2022]{160}.
- Guards against circularity hold the known set out of strategy-building, and count re-finding of
  items the team did not know in advance as the informative signal
  [hausner-objective-search-strategy-2012]{164} [cochrane-handbook-ch4-searching-2025]{151}.
- Making absence visible (placeholders) recovered much of the omission-detection gap in a surface
  benchmark [fu-absencebench-omission-2025]{365}; empty cells in a dimension grid are read as
  candidate unoccupied combinations [nickerson-taxonomy-development-method-2013]{200}.
- Classification disagreement concentrates in a few confusable category pairs and falls with
  definition refinement or training [el-emam-defect-classification-repeatability-1998]{372}
  [falessi-odc-feasibility-2006]{209}.

## Open questions carried to the parent

- How near-duplicate approaches should be merged before counting kinds, given that every count
  depends on the identity threshold [kornish-ulrich-opportunity-spaces-2011]{361}.
- Whether omission detection on semantic absences (missing approaches) behaves like surface omission
  [fu-absencebench-omission-2025]{365}.

## Revisit if

- A study validates a kind-completeness estimator or a taxonomy ending condition against later-found
  kinds or a known total for methods or approaches.
- A controlled test compares a structured generator with an unstructured expert list on the number of
  distinct families found.
- Omission-detection evidence appears for semantic absences, for humans or models.
- Full texts acquired for the abstract-level sources (Wohlin 2013, Kastner 2009, Rücker 2011,
  Ciolkowski 2009) change the strength of the claims that rest on them.

## Revisions

- **2026-10-20 — correction (adversarial-read R1–R4, R9).** Estimator inputs are stated per estimator
  (R2). The validation absence is restricted to families of methods or approaches (R2). The full
  taxonomy ending conditions are restored (R3). Model-based bounds are confined to justified assumptions
  (R1). The 12-unit example is confirmed in the extended attestation (R4). The inspector quotation's
  exception is restored (R9).
