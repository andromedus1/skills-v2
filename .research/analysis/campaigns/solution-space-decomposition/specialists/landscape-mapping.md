---
title: Landscape mapping methods — how practitioner and research traditions bound, cluster, de-blind and coverage-check a solution landscape
provenance: agent-synthesis
updated: 2026-10-20
campaign: solution-space-decomposition
facet: landscape-mapping
summary: >
  Within-specialist brief. Compares how patent landscape reports (WIPO guidelines, RIPL reporting
  standard, automated seed-expansion landscaping), systematic mapping studies in software
  engineering (Petersen keywording, known-set / quasi-gold-standard search validation, hybrid
  snowballing), general morphological analysis and scenario methods, technology roadmapping,
  technology intelligence / horizon scanning, and competitive / analogous-market search define
  landscape boundaries, organise items into families, guard against blind spots (vocabulary
  mismatch, single-source and single-domain search, seed dependence) and check coverage. Most of
  the field's moves are advocated in guidelines; measured evidence exists mainly for search
  recall against a known set, for the low overlap of independent maps or reviews of the same
  topic, and for the novelty gain of drawing on analogous domains. No tradition reports a
  validated completeness estimate for the set of families (as opposed to items within known
  families).
---

# Landscape mapping methods

## Scope, source classes and evidence key

This brief covers practitioner and research methods for mapping a technology or solution
landscape: patent landscape reports, systematic mapping studies in software engineering (SE),
morphological and scenario methods, technology roadmapping, technology intelligence and horizon
scanning, and competitive / analogous-market search. For each it asks how the method (a) sets the
landscape's boundary, (b) organises it into families or clusters, (c) guards against blind spots,
and (d) validates coverage, and what evidence supports each move.

Source classes are mixed and are marked per claim where the attestation does not carry them:
intergovernmental guideline (WIPO), consensus reporting guideline (RIPL), practitioner overviews by
method developers (Ritchey, Phaal), conference/journal methods papers, participant-observer case
studies, controlled experiments, and abstract-only records. Evidence levels:

- **advocated** — recommended in a guideline or by a method's developer without a reported test;
- **demonstrated** — shown in one or a few worked cases or case studies without a controlled
  comparison;
- **measured** — a study reports a quantitative comparison or validation.

## 1. Patent landscape reports

**Boundary.** The WIPO guidelines treat scoping as the first, stakeholder-agreed step: a landscape
on any topic could include hundreds of thousands of documents ("trying to boil the ocean"), so a
scope agreed by all stakeholders sets focus and tells readers the analysis constraints; scope
should state what is out of scope, plus countries, period, family-reduction method and whether
non-patent literature is included [wipo-plr-guidelines-trippe-2015]{250}. The same guidelines
note that "in any given technical area there are likely to be many different approaches", and
recommend that large topics be limited "to a handful of the most important technical approaches"
[wipo-plr-guidelines-trippe-2015]{250} — i.e. the boundary is deliberately narrowed to selected
families rather than drawn around the whole approach space. The RIPL consensus definition, by
contrast, says a landscape "seeks to encompass an entire population of relevant data, rather than
a random sample drawn from that population" [smith-ripl-statement-2018]{251}. Evidence level:
advocated.

**Organising into families.** WIPO describes four ways to populate technology categories:
classification codes; one search strategy per category (works best when categories are clearly
distinct); categories created "on the fly" while manually reviewing documents, naming a new
category "when the analyst comes across a new approach", often followed by a second
reclassification pass; and semi- or fully-automated ML/semantic grouping. It recommends that
categories "ideally" come from subject-matter-expert input on "an industry standard view", because
examiner-assigned classification codes rarely match market categories ("it is a happy accident when
they align") and differ across offices in system and granularity [wipo-plr-guidelines-trippe-2015]{250}.
An analyst must also decide and state whether a document may sit in several categories
[wipo-plr-guidelines-trippe-2015]{250}. Evidence level: advocated, illustrated with worked
examples (e.g. a solar-cooking landscape segmented by heating technique then component).

**Blind-spot guards.** Three guards recur:

- *Vocabulary.* WIPO's "reverse engineering" search starts from a few on-target hits, mines them
  for classification codes, indexing and inventor terms, re-searches, and repeats "until no
  additional search items are identified, and the analyst feels they have conducted a thorough
  search" [wipo-plr-guidelines-trippe-2015]{250}. Its Atazanavir example shows the same compound
  under different names at filing and later [wipo-plr-guidelines-trippe-2015]{250}. In
  prior-art retrieval research, patent drafters are reported to "purposely use many vague terms
  and expression and non-standard terminology", and IPC classes are used to expand queries
  specifically to "address the vocabulary mismatch" [mahdabi-prior-art-query-2011]{254}.
- *Classification as a vocabulary-independent channel.* WIPO's model terms of reference require
  reports to show "the effect of including different patent classification systems like CPC and FI
  in order to improve recall in comparison to purely IPC based searches", plus citation analysis
  and supplementary keyword searches, with "Numerical evidence" [wipo-plr-guidelines-trippe-2015]{250}.
- *Expert and searcher involvement* for technical fields such as life sciences
  [wipo-plr-guidelines-trippe-2015]{250}.

**Coverage validation.** WIPO sets a working target of recall above 90% with precision above 70%,
prioritising recall for overview landscapes, and says major statistical findings "should always be
validated" [wipo-plr-guidelines-trippe-2015]{250}; the passages read do not state how the recall
figure is to be established (an unspecified measurement step). The stopping rule for query
expansion is saturation of new search terms and codes plus analyst judgement
[wipo-plr-guidelines-trippe-2015]{250}. Evidence level: advocated.

**Evidence on practice.** A systematic review of 81 published life-sciences patent landscapes
found mean compliance of 64% with a 20-item reporting checklist; "Just eight articles (9.9%)
reported all methodological items that would enable replication and validation"
[smith-ripl-statement-2018]{251}; "Just one article (1.4%) reported that patent selection was
blindly reproduced, and 24% of articles list the patents included" [smith-patent-landscape-reporting-thesis-2018]{252}.
The resulting RIPL checklist requires reporting of search terms, databases, dates, selection
criteria, counts at each selection stage and limitations [smith-ripl-statement-2018]{251}, but it
"does not extend to recommendations regarding methodologies" [smith-ripl-statement-2018]{251} and
contains no item requiring a measured recall or completeness estimate (inferred from the checklist
as recorded in the attestation). Evidence level: measured (for reporting deficits).

**Automated landscaping (seed expansion).** In the Abood and Feltenberger approach as described by
Erana and Finlayson, about 1,000 expert-curated seed patents are expanded by shared CPC codes,
citations and family links; anything outside that expansion is treated as a negative
[erana-finlayson-neural-patent-landscaping-2024]{253}. They point out a structural blind spot: a
patent sharing no CPC code, citation or family link with a seed "will never be included in the
landscape", which is problematic for broad landscapes [erana-finlayson-neural-patent-landscaping-2024]{253}.
When boundary-near ("hard") examples were labelled via active learning, the earlier architecture's
F1 fell from 0.77 on easy examples to 0.60 on hard ones, and the best models reached roughly
0.67-0.69 on hard examples versus 0.91-0.93 on easy ones [erana-finlayson-neural-patent-landscaping-2024]{253}.
Evidence level: measured, in one domain (AI patents).

## 2. Systematic mapping studies (software engineering)

**Boundary.** Petersen et al. define a systematic map as "a defined method to build a
classification scheme and structure a software engineering field", whose category frequencies show
"the coverage of the research field" [petersen-systematic-mapping-2008]{255}. They deliberately did
not restrict by outcome or study design because doing so could leave "the map incomplete", and argue
that restricting to rigorous empirical studies biases the picture of an area because some
sub-areas are easier to study empirically [petersen-systematic-mapping-2008]{255}.

**Organising into families (keywording).** Reviewers read abstracts for keywords and concepts
reflecting each paper's contribution and context, combine keywords across papers into categories
"representative of the underlying population", and cluster them into facets; the scheme "evolves
while doing the data extraction, like adding new categories or merging and splitting existing
categories", with a short rationale recorded per placement [petersen-systematic-mapping-2008]{255}.
Topic and contribution facets are derived bottom-up from keywords, while the research-type facet is
adopted from an existing generic classification [petersen-systematic-mapping-2008]{255}. Felderer
and Carver recommend that sub-field maps extend classification schemes from baseline studies so
results can be compared [felderer-carver-sms-security-2018]{257}. Petersen et al. warn that
abstracts "are often misleading and lack important information" and recommend reading deeper where
classification is unclear [petersen-systematic-mapping-2008]{255}. Evidence level: demonstrated
(one worked map), not tested against alternatives.

**Blind-spot guards.** Guidance combines automated database search, manual venue search and
backward/forward snowballing to "achieve a good level of coverage", uses broad strings to avoid
"premature elimination", and enumerates synonyms [felderer-carver-sms-security-2018]{257}. Zhang et
al.'s case studies show the vocabulary failure concretely: early SLRs that called themselves
"survey" were missed until synonyms were added (quasi-sensitivity 65% to 85%), and a published
review's string missed terms actually used in its target literature [zhang-qgs-search-2011]{258}.
In Kitchenham et al.'s repeatability study, two novices' strings omitted "regression testing" and
their only overlap with an expert review was three regression-testing papers
[kitchenham-slr-repeatability-2011]{260}.

**Coverage validation and stopping.**

- *Known set / quasi-gold standard (QGS).* "An essential basis for the subjective assessment of
  completeness is comparison of the search results against a known set of papers"; if the string
  misses known-set papers it must be modified [felderer-carver-sms-security-2018]{257}. Zhang et al.
  make this quantitative: build the QGS by manual search of selected venues and period, compute
  quasi-sensitivity (QGS papers retrieved / QGS size), and stop refinement at a 70-80% threshold
  (e.g. stop if >= 80%), adjusted for "diversity of subject, scope of research questions, and the
  scattering of the descriptive keywords" [zhang-qgs-search-2011]{258}. In their two cases, combined
  manual+automated search found 38 SLRs versus 22 manual-only and 28 automated-only; a re-run of a
  published SLR's search found it had captured only 36% (59/164) of the papers the systematic
  process found, and one venue contributing 7% of the QGS had no paper in the original
  [zhang-qgs-search-2011]{258}. Evidence level: measured in two non-randomly chosen case studies;
  quasi-sensitivity is recall relative to the QGS venues and period only
  [zhang-qgs-search-2011]{258}.
- *Diminishing returns as a stopping signal.* In Zhang et al.'s second case, further string
  refinement gave "very slim" gains while irrelevant hits rose "dramatically", which ended
  refinement at 73% [zhang-qgs-search-2011]{258}.
- *Iterative snowballing to no-new-items.* A hybrid of database start set plus iterative backward
  and forward snowballing found 43 relevant papers where the original SLR listed 33; only 20 were
  common to both [wohlin-hybrid-search-snowballing-2022]{261}. Cheaper variants found 23-38, and
  performance was "highly dependent on the start set"; "When having a round with few articles ...
  we risk that the procedure stops early" [wohlin-hybrid-search-snowballing-2022]{261}. Evidence
  level: measured, single replication.
- *Borderline transparency.* Wild cards (a reviewer may carry forward an article that failed the
  score threshold) and a published list of borderline articles expose near-boundary judgements
  [wohlin-hybrid-search-snowballing-2022]{261}. Evidence level: demonstrated (one wild card ended
  among included articles).

**Reliability evidence (measured, partly abstract-level).** Two independent published mapping
studies of software product line testing differed in "quite a number" of included papers and in
how papers were classified; "their reliability cannot simply be taken for granted"
[wohlin-mapping-reliability-2013]{259} {confidence: abstract}. Two independent novice SLRs of unit
testing shared only 6 of 32 papers and found only 3 of an expert review's 21; 8 of 10
relevant papers the expert review missed would have added three new framework classes and filled
three empty cells [kitchenham-slr-repeatability-2011]{260}. Practice also varies by guideline:
mapping studies commonly combine several guideline families because "the most frequently followed
guidelines are not sufficient alone" [petersen-mapping-guidelines-update-2015]{256} {confidence: abstract}.

## 3. Morphological analysis and scenario methods

**Generating the space.** General morphological analysis (GMA) defines the problem's parameters
(dimensions), assigns each a range of values, and treats every combination as a formally possible
configuration; heterogeneous dimensions (technical, financial, political, ethical) can be mixed
[ritchey-gma-general-method]{262}. Cross-consistency assessment (CCA) then judges every pair of
values for logical or empirical compatibility (normative judgements deferred), removing all
configurations containing an incompatible pair; pair-wise judgements grow quadratically while
configurations grow multiplicatively [ritchey-gma-general-method]{262}. Ritchey reports fields of
6-10 variables holding 50,000 to 5,000,000 formal configurations, typically reduced by up to 90-99%
[ritchey-psm-gma-2006]{263}.

**Coverage claim and its limits.** Zwicky's "totality research" is said to derive all solutions in
an "unbiased way", helping discover configurations "overlooked by other - less systematic -
methods" [ritchey-gma-general-method]{262}. The coverage is total only relative to the chosen
parameters and values: "the output of a morphological analysis is no better than the quality of its
input" [ritchey-psm-gma-2006]{263}. The claimed check on input quality is that "poorly defined
parameters and incomplete ranges of conditions are immediately revealed" during CCA
[ritchey-psm-gma-2006]{263}; no procedure for testing whether a needed dimension is missing is
described in the GMA text [ritchey-gma-general-method]{262} {inferred: absence noted across both
Ritchey sources}. For scenario fields, Ritchey selected eight configurations that "covered all of the
parameter states in the scenario field ('full field coverage')" [ritchey-psm-gma-2006]{263} — a
sample-coverage criterion defined over the dimension values, not over outcomes. Method developers
also note that GMA "has been written about and discussed far more than it has actually been used"
and "requires strong, experienced facilitation" [ritchey-psm-gma-2006]{263}. Evidence level:
advocated and demonstrated in consulting cases by the method's developer; trials giving identical
fields to different groups are mentioned without reported results [ritchey-gma-general-method]{262}.

**Scenario technique families.** A review of the scenario literature catalogued "eight categories
of techniques that include a total of 23 variations" [bishop-hines-collins-scenario-techniques-2007]{264}
{confidence: abstract}. On effectiveness, a critical synthesis argues the widely used intuitive-logics
method and its augmentations are designed to serve understanding and "challenging conventional
thinking", but (except one multi-attribute value augmentation) not decision-making
[wright-bradfield-cairns-intuitive-logics-2013]{265} {confidence: abstract}. An experiment with 252
graduate management students reported that scenario planning "reduces the framing bias" and improves
decision quality relative to traditional strategic-planning tools [meissner-wulf-scenario-framing-2013]{266}
{confidence: abstract}. Neither speaks to whether scenarios cover the space of alternatives.

## 4. Technology roadmapping

Roadmapping frames the landscape as a multi-layered, time-based chart that represents both
demand ("market pull") and supply ("technology push") views [phaal-roadmapping-overview-2020]{267}.
In workshop forms such as S-Plan, a wall chart is used "to share perspectives across the full scope
of the topic of interest, to create a 'strategic landscape'" within which "landmarks" are identified
[phaal-roadmapping-overview-2020]{267}. The guard against blind spots is participant diversity and
openness: lessons from a review of 78 sector roadmapping initiatives include "a spirit of openness
... to encourage new participants and thinking" [phaal-roadmapping-overview-2020]{267}. The method's
developer notes the claimed benefit is often the consensus-building process, while "a healthy strategy
process should also challenge this consensus, as Motorola did with a requirement to include a
'minority report'" [phaal-roadmapping-overview-2020]{267}. Evidence level: advocated and demonstrated
(case studies, practice lessons); no coverage measurement reported.

## 5. Technology intelligence, scouting and horizon scanning

Strategic-foresight frameworks group intelligence methods into market-oriented (e.g. lead-user and
lead-market analysis, competitor analysis), technology-oriented (technology scouting, publication,
patent and conference analysis, S-curves, Delphi) and integrating methods (roadmapping, scenarios);
integrating methods are "discussed as a powerful means to overcome the barriers between market and
technology perspective" [rohrbeck-strategic-foresight-dt-2007]{268}. The rationale is detecting "weak
signals in their periphery" [rohrbeck-strategic-foresight-dt-2007]{268}. That paper reports no
coverage measurement and notes that no consistent framework of actors, methods and systems existed
[rohrbeck-strategic-foresight-dt-2007]{268}. Evidence level: advocated plus one company case.

Health-technology horizon scanning offers measured coverage checks:

- A PubMed strategy for emerging technologies was validated against hand-searching of six key
  research journals and eight high-impact surgery journals: 29 of 35 relevant technologies were found within two years of publication (83%
  sensitivity) [varela-lema-emerging-tech-search-2012]{270} {confidence: abstract}.
- A national horizon-scanning centre scored its 35 routine sources on eight criteria led by
  coverage, quality and efficiency, and recommended dropping seven [smith-cook-packer-horizon-sources-2010]{269}
  {confidence: abstract}.
- About 47% of references in 22 emerging-technology reports were grey literature (manufacturers,
  regulators, trial registries), and searchers are advised to go beyond MEDLINE and Embase; only 41%
  of reports fully described their search [farrah-grey-literature-horizon-scanning-2019]{271}.

## 6. Competitive analysis and analogous-domain search

Competitor analysis has documented systematic blind spots: decision makers "typically have specific
'blind spots' when they consider the contingent decisions of competitors", offered as explanations
for overcapacity, entry failures and acquisition premiums [zajac-bazerman-competitor-blindspots-1991]{272}
{confidence: abstract}. On adjacent domains, a symmetric field experiment (213 problem solvers from
roofing, carpentry and inline skating, sharing a safety-gear comfort problem) found that solutions
from analogous-market solvers were substantially more novel but had lower potential for immediate use,
with the novelty effect about two-thirds of the lead-user effect and strongest in the upper tail
[franke-poetz-schreier-analogous-markets-2014]{273}. The authors note managers "tend to stay within
their own market context" when searching [franke-poetz-schreier-analogous-markets-2014]{273}. They
identified analogous markets by a criterion set (shared analogous problem, delineated markets,
comparable importance, sampling access) applied after secondary research, a 20-interview pilot and 30 expert interviews
[franke-poetz-schreier-analogous-markets-2014]{273}. Evidence level: measured, one context, hand-picked
markets.

## Cross-method synthesis (in the field's own terms)

| Concern | Move | Where | Evidence level |
|---|---|---|---|
| Boundary | Stakeholder-agreed scope with explicit out-of-scope list | Patent landscapes [wipo-plr-guidelines-trippe-2015]{250} | advocated |
| Boundary | Do not filter by method or outcome when the goal is overview | Mapping [petersen-systematic-mapping-2008]{255} | advocated |
| Families | Bottom-up keywording into facets; scheme evolves during extraction | Mapping [petersen-systematic-mapping-2008]{255} | demonstrated |
| Families | Expert/industry categories preferred over examiner classification | Patent landscapes [wipo-plr-guidelines-trippe-2015]{250} | advocated |
| Families | Parameters x values, consistency-pruned | GMA [ritchey-gma-general-method]{262} | demonstrated |
| Vocabulary | Mine hits for terms/codes; iterate to no new terms | Patent landscapes [wipo-plr-guidelines-trippe-2015]{250} | advocated |
| Vocabulary | Classification-code expansion of queries | Prior-art IR [mahdabi-prior-art-query-2011]{254} | measured (recall ~0.5-0.6, no ablation read) |
| Single-channel | Combine database, manual, snowballing | Mapping [felderer-carver-sms-security-2018]{257}; [wohlin-hybrid-search-snowballing-2022]{261} | measured (one replication) |
| Single-domain | Draw on analogous markets | Ideation [franke-poetz-schreier-analogous-markets-2014]{273} | measured (one context) |
| Coverage | Recall against known set / QGS with threshold | Mapping [zhang-qgs-search-2011]{258}; horizon scanning [varela-lema-emerging-tech-search-2012]{270} | measured |
| Coverage | Saturation of new terms or new items | [wipo-plr-guidelines-trippe-2015]{250}; [wohlin-hybrid-search-snowballing-2022]{261} | advocated / demonstrated |
| Coverage | Sample covers every dimension value ("full field coverage") | GMA scenarios [ritchey-psm-gma-2006]{263} | demonstrated |
| Reliability | Independent repetition and overlap comparison | [kitchenham-slr-repeatability-2011]{260}; [wohlin-mapping-reliability-2013]{259} | measured |

{inferred: aggregate — the table is composed from the attestations cited in each row; the
"measured" label for classification expansion reflects reported recall levels only, as no
with/without-classification comparison was read in the source.}

## Disconfirming analysis

Searched across attested sources for evidence that these methods do *not* deliver coverage, or give
illusory completeness:

- **Independent maps of the same topic disagree.** Two published mapping studies differed in
  included papers and classification [wohlin-mapping-reliability-2013]{259} {confidence: abstract};
  two novice SLRs shared 6 of 32 papers and an expert review missed papers that would have added
  framework classes [kitchenham-slr-repeatability-2011]{260}; an SLR and its replication shared 20 of
  56 distinct papers [wohlin-hybrid-search-snowballing-2022]{261} {inferred: aggregate — 33 + 43 - 20
  = 56 distinct}. A single map is therefore not evidence of a complete family set, and a
  classification produced by one team may not be reproduced by another.
- **Known-set recall can be satisfied while families are missing.** QGS quasi-sensitivity measures
  recall only against the QGS venues and period [zhang-qgs-search-2011]{258}, and the known set is
  often drawn from personal knowledge or a prior review [felderer-carver-sms-security-2018]{257}; a
  family absent from the known set cannot lower the score {inferred: tension between the measurement
  definition and the coverage claim}. The CSCW venue example shows a whole source cluster can be absent
  from a published review [zhang-qgs-search-2011]{258}.
- **Seed-based expansion is closed to unlinked regions.** Seed/anti-seed landscaping cannot include
  patents unconnected to the seeds, and performance drops on boundary cases
  [erana-finlayson-neural-patent-landscaping-2024]{253}; snowballing output depends on the start set
  and can stop early [wohlin-hybrid-search-snowballing-2022]{261}.
- **Saturation stopping relies on judgement.** WIPO's stopping rule includes that the analyst "feels"
  the search is thorough [wipo-plr-guidelines-trippe-2015]{250}; Zhang et al. stopped one case at 73%
  because returns diminished — inside their 70-80% band but below the 80% used in their worked stopping rule [zhang-qgs-search-2011]{258}.
- **Morphological "totality" is conditional on the parameter set**, which is chosen by the group and
  not itself tested for completeness [ritchey-psm-gma-2006]{263}; the claim of unbiased derivation of
  all solutions [ritchey-gma-general-method]{262} is the developer's advocacy without reported
  comparative tests.
- **Reporting rarely makes coverage checkable.** Only 9.9% of patent-landscape articles reported all
  replication-relevant methods [smith-ripl-statement-2018]{251}, and 41% of horizon-scanning reports
  fully described their search [farrah-grey-literature-horizon-scanning-2019]{271}.
- **Adjacent-domain search trades usefulness for novelty** [franke-poetz-schreier-analogous-markets-2014]{273};
  and the distance effect is confounded with sample differences in that study
  [franke-poetz-schreier-analogous-markets-2014]{273}.
- **Consensus processes can suppress dissent.** Roadmapping's process benefit is consensus, which the
  method's developer says should be challenged (e.g. a minority report) [phaal-roadmapping-overview-2020]{267}.
- Searched for, but not found in attested sources: any controlled test showing that keywording,
  morphological fields, roadmap layers or scouting networks find *more distinct families* than an
  unstructured expert list. The closest measured comparisons are of item recall
  [zhang-qgs-search-2011]{258} and of solution novelty [franke-poetz-schreier-analogous-markets-2014]{273}.

## Contradictions

- **Whole population vs selected families.** RIPL defines a landscape as seeking "an entire population
  of relevant data" [smith-ripl-statement-2018]{251}; WIPO advises limiting large topics "to a handful of
  the most important technical approaches" [wipo-plr-guidelines-trippe-2015]{250}. Relationship:
  `tension` — RIPL's completeness is over documents within a defined scope; WIPO's narrowing is over
  which approach families enter scope. Both stand as stated.
- **Where categories should come from.** Petersen et al. derive topic categories bottom-up from the
  papers' own keywords so the scheme reflects "the underlying population"
  [petersen-systematic-mapping-2008]{255}; WIPO prefers subject-matter-expert, industry-standard
  categories over data-derived classification codes [wipo-plr-guidelines-trippe-2015]{250}; Felderer
  and Carver recommend reusing baseline schemes [felderer-carver-sms-security-2018]{257}. Relationship:
  `tension` (different purposes: field structure vs client usability vs comparability). Not resolved
  here.
- **Does search strategy change conclusions?** Wohlin et al. report, citing Jalali and Wohlin (2012),
  that database search and backward snowballing yielded mostly the same papers and similar
  conclusions [wohlin-hybrid-search-snowballing-2022]{261}; Kitchenham et al. found missing papers
  "can have a substantial impact on conclusions", while noting an earlier case of theirs with little
  change, possibly because it was a mapping study [kitchenham-slr-repeatability-2011]{260}.
  Relationship: `qualifies` — sensitivity of conclusions appears to depend on study type and on
  whether the missed items fall into new categories.
- **Recall thresholds.** WIPO's working target is recall above 90% [wipo-plr-guidelines-trippe-2015]{250};
  Zhang et al. propose 70-80% quasi-sensitivity as acceptable [zhang-qgs-search-2011]{258}.
  Relationship: `incommensurable` as stated — WIPO's figure is unanchored to a measurement procedure in
  the passages read, while Zhang's is relative to a constrained known set.

## Transfer-relevant observations

Stated in the source fields' own terms, without project recommendations:

- Landscape traditions separate *within-family recall* (measurable against a known set, a QGS, or a
  hand-searched reference) from *family-set completeness*, for which none of the attested traditions
  reports a validated estimator {inferred: convergence across [zhang-qgs-search-2011]{258},
  [wipo-plr-guidelines-trippe-2015]{250}, [ritchey-psm-gma-2006]{263}}.
- The measured signals that do exist for "something is missing" are: recall against an independently
  built known set [zhang-qgs-search-2011]{258}; overlap between independent repetitions
  [kitchenham-slr-repeatability-2011]{260}; whether additional items fall into new categories or empty
  cells rather than existing ones [kitchenham-slr-repeatability-2011]{260}; and yield of new items per
  snowballing or query iteration [wohlin-hybrid-search-snowballing-2022]{261}.
- Known sources of family-level blind spots in these fields are vocabulary mismatch
  [mahdabi-prior-art-query-2011]{254}, single search channel or venue set [zhang-qgs-search-2011]{258},
  seed/start-set dependence [erana-finlayson-neural-patent-landscaping-2024]{253}, staying within one's
  own market or domain [franke-poetz-schreier-analogous-markets-2014]{273}, reliance on bibliographic
  databases for emerging items [farrah-grey-literature-horizon-scanning-2019]{271}, and classification
  schemes built for another purpose [wipo-plr-guidelines-trippe-2015]{250}.
- Structured generators (morphological fields, roadmap layers, mapping facets) make the dimensions
  explicit and therefore auditable, but their completeness is bounded by the dimensions chosen
  [ritchey-psm-gma-2006]{263}; "full field coverage" is one stated criterion for drawing a small sample
  from such a field [ritchey-psm-gma-2006]{263}.
- Reporting standards in these fields (RIPL, mapping guidelines) ask for search strings, sources,
  selection counts and limitations rather than a single completeness number
  [smith-ripl-statement-2018]{251}; [felderer-carver-sms-security-2018]{257}.

## Revisit if

- The full text of Wohlin et al. (2013) becomes readable: its four conjectures and per-paper overlap
  figures may supply mapping-specific reliability guidance [wohlin-mapping-reliability-2013]{259}.
- A study is found that measures family-level (category-level) completeness of a landscape against an
  independent reference, or tests whether a structured generator yields more distinct families than an
  unstructured expert list.
- Abood and Feltenberger (2018) or Choi et al. (2019) are read directly, revising the seed-expansion
  account currently cited through [erana-finlayson-neural-patent-landscaping-2024]{253}.
- Bishop, Hines and Collins (2007) or Wright, Bradfield and Cairns (2013) are read in full, which could
  change the abstract-level characterisation of scenario methods.
- Evidence emerges on how often WIPO-style recall targets are actually measured in practice, and how.

## Gaps and acquisition notes

- Abstract-only engagement for: [wohlin-mapping-reliability-2013]{259} (full-text PDF returned 403 /
  Cloudflare challenge), [petersen-mapping-guidelines-update-2015]{256} (closed access),
  [bishop-hines-collins-scenario-techniques-2007]{264}, [wright-bradfield-cairns-intuitive-logics-2013]{265},
  [meissner-wulf-scenario-framing-2013]{266}, [zajac-bazerman-competitor-blindspots-1991]{272},
  [smith-cook-packer-horizon-sources-2010]{269}, [varela-lema-emerging-tech-search-2012]{270}.
- Jeppesen and Lakhani (2010) on problem-solver marginality is cited by Franke et al. as related
  evidence that distant solvers contribute disjunctive knowledge
  [franke-poetz-schreier-analogous-markets-2014]{273}; it was not read (Harvard repository PDF
  returned an empty file and then HTTP 429).
