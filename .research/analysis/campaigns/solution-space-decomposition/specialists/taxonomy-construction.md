---
title: Taxonomy construction — how classification schemes decompose a domain and decide when they are complete
provenance: agent-synthesis
updated: 2026-10-20
summary: Methods for building taxonomies, typologies and faceted classifications of a domain's objects, what they treat as "genuinely different", and the completeness (ending) conditions they prescribe. Covers the Nickerson–Varshney–Muntermann iterative method, Bailey's conceptual/empirical typology construction (cite-through), logical division and MECE, facet analysis, the four epistemic routes to forming classes, explanatory typologies, morphological fields, and participant-sorting methods (concept mapping, card sorting). Ending conditions are designed and advocated, not validated; measured evidence exists for the reliability of classifying objects into a fixed scheme and for the stability of sort-derived groupings, but not for whether a scheme's dimensions are complete.
key_findings:
  - The IS taxonomy method defines a taxonomy as dimensions of mutually exclusive, collectively exhaustive characteristics, chosen by a purpose-derived meta-characteristic, built through alternating empirical-to-conceptual and conceptual-to-empirical iterations until objective and subjective ending conditions hold. Its authors say the meta-characteristic critically shapes the result and that the same meta-characteristic can yield different taxonomies.
  - The objective ending conditions are mostly stability checks on the last iteration (no new or merged dimensions, no merged or split objects, every characteristic populated, unique cells). They test convergence on the objects examined, not coverage of unexamined ones; the authors give no evidence that meeting them signals completeness.
  - Surveys of practice find ending conditions rarely stated (17% of journal taxonomies) and, when stated, often asserted without detail (16 of 38) or selectively dropped, including dropping mutual exclusivity for readability.
  - Classification sources treat MECE as an ideal that working schemes rarely meet. Exhaustivity is usually secured with a residual "other" class, not by showing coverage; exclusivity is fragile when more than one basis of division is mixed.
  - Measured reliability concerns assigning objects to an existing scheme. Defect-classification kappas of 0.66–0.82 have been reported, but in another study raters disagreed 43% of the time while nearly all of them (97%) still gave each item exactly one category. A feeling that categories don't overlap is therefore not evidence that raters agree.
  - Sorting-based methods (card sorting, concept mapping) have measured cross-study stability of item groupings (Mantel r 0.61–0.93; 63–93% navigation-scheme agreement) and a sample-size curve (r 0.90 with full-sample similarity at 15 sorters). Where the dendrogram is cut, and how many clusters to keep, is left to judgement.
  - Knowledge-organization critiques hold that the choice of dimensions, the similarity measure and the epistemic route (logical division, phenetic similarity, genealogy, purpose) each change the resulting classes, and that no neutral or single correct classification exists.
---

# Taxonomy construction: decomposing a domain into classes and deciding completeness

## Scope

This facet asks how classification-scheme methods break a domain of objects (here, approaches
to a problem) into categories that are different in kind rather than variants, and what they
offer for judging whether a scheme, or a sample classified by it, is complete. Sources span
information-systems taxonomy research, knowledge organization (library and information
science), social-science typology, software-engineering classification reliability studies,
and user-research sorting methods.

## Methods and how each generates or checks alternatives

### 1. Iterative taxonomy development (Nickerson, Varshney & Muntermann)

- **Definition and the "different" test.** A taxonomy is a set of dimensions, each with at
  least two characteristics that are mutually exclusive and collectively exhaustive, "such
  that each object under consideration has one and only one" characteristic per dimension
  [nickerson-taxonomy-development-method-2013]{200}. Two objects differ when they fall in
  different cells (combinations of characteristics); one objective ending condition requires
  every cell to be unique [nickerson-taxonomy-development-method-2013]{200}.
- **Relevance filter.** A meta-characteristic, derived from the taxonomy's purpose and
  intended users, is fixed first; "Each characteristic should be a logical consequence of the
  meta-characteristic", which guards against "naïve empiricism"
  [nickerson-taxonomy-development-method-2013]{200}. A characteristic "that has the same value
  for all or nearly all objects is of no use", even if it follows from the meta-characteristic
  [nickerson-taxonomy-development-method-2013]{200}.
- **Generation moves.** Empirical-to-conceptual (E2C) passes take a subset of objects (random,
  systematic or convenience sample), identify discriminating characteristics and group them
  into dimensions. Conceptual-to-empirical (C2E) passes deduce dimensions from the
  researcher's knowledge, then check whether real objects occupy every characteristic
  [nickerson-taxonomy-development-method-2013]{200}. Little data plus strong domain knowledge
  favours C2E; the reverse favours E2C; with little of either, the researcher should study the
  domain first. Switching approach in later iterations is advised "to view the taxonomy from a
  different perspective" [nickerson-taxonomy-development-method-2013]{200}.
- **Ending conditions.** The fundamental objective condition is the MECE definition itself.
  There are eight more: all objects or a representative sample examined; no object merged or
  split in the last iteration; at least one object under every characteristic; no new
  dimensions or characteristics in the last iteration; none merged or split in the last
  iteration; and unique dimensions, characteristics and cells
  [nickerson-taxonomy-development-method-2013]{200}. The subjective conditions are concise,
  robust, comprehensive, extendible and explanatory. Comprehensiveness has two readings: all
  objects classifiable, or all dimensions identified. A "seven plus or minus two" dimension
  count is suggested as an objective proxy for conciseness
  [nickerson-taxonomy-development-method-2013]{200}.
- **Evidence level: designed and advocated, with one demonstration.** The worked example
  (mobile applications) used only two objective conditions "for simplicity". It took six
  iterations over 15 applications drawn as convenience samples from two literature sources,
  and stopped when an iteration added no dimension; the result "appears to be comprehensive"
  [nickerson-taxonomy-development-method-2013]{200}. The authors list the subjective conditions
  only as necessary conditions for usefulness and say that the only sufficient condition they
  can give ("useful if others use it") is tautological
  [nickerson-taxonomy-development-method-2013]{200}.
- **Gaps as signals.** Empty cells ("voids") are read as opportunities for new objects
  [nickerson-taxonomy-development-method-2013]{200}. Empty characteristics, by contrast,
  violate the "every characteristic populated" condition and must be filled or removed
  [nickerson-taxonomy-development-method-2013]{200}.

### 2. Conceptual typology and empirical taxonomy (Bailey, cite-through)

Nickerson et al. attribute to Bailey (1994) a split between typologies (conceptually or
deductively derived) and taxonomies (empirically derived, e.g. by cluster analysis). They also
attribute two conceptual construction moves to him: *substruction* (start from one type and
add dimensions until a satisfactorily complete typology results) and *reduction* (start from
an extensive typology and eliminate dimensions until it is parsimonious). Bailey's three-level
model runs conceptual-to-empirical or the reverse
[nickerson-taxonomy-development-method-2013]{200}. Nickerson et al. also attribute to Bailey a
list of typology weaknesses: lack of mutual exclusivity and collective exhaustivity, lack of
parsimony, static structure, arbitrary or ad hoc criteria, and description without explanation
[nickerson-taxonomy-development-method-2013]{200}. Bailey's text was not fetched; these points
are held at the cite-through level.

### 3. Logical division and MECE

- Toohey's four rules of division are: exclusivity relative to the basis; joint coextension
  with the divided class (exhaustivity); "only one basis" per division step; and division into
  proximate species. Rules I–II together are the "JEPD" condition
  [fricke-logical-division-2016]{204}. Mixing bases (age, family role and occupation in one
  array) can produce classes that are exclusive only as "a somewhat fragile arrangement" that a
  new case can break [fricke-logical-division-2016]{204}.
- In empirical domains "it is hard to have such certainty" about exclusivity or exhaustivity.
  The standard remedies are binary division (B / not-B) or a residual "everything else" class
  [fricke-logical-division-2016]{204}. Division works best for artificial kinds devised for a
  purpose. It "failed" for biological species, whose members share "some, but not all, of a
  manifold of characteristics" [fricke-logical-division-2016]{204}.
- MECE as used in consulting is a grouping principle attributed to Barbara Minto (McKinsey,
  late 1960s), with Ranganathan's canons of exhaustiveness and exclusiveness as antecedents
  [wikipedia-mece-principle]{214}. A practitioner critique argues that the canonical "increase
  revenues / cut costs" split is collectively exhaustive but not mutually exclusive. On this
  argument, forcing true exclusivity requires adding a hybrid branch that "re-tangled" the
  split, so the author proposes "independent and collectively exhaustive" (ICE) instead
  [chevallier-mece-vs-ice-2012]{213}. The same sources note that MECE excludes deliberate
  redundancy [chevallier-mece-vs-ice-2012]{213} [wikipedia-mece-principle]{214}. Evidence
  level: argument and worked example; no data.

### 4. Facet analysis (Ranganathan, Classification Research Group)

- Facet analysis sorts a field's terms "into homogeneous, mutually exclusive facets, each
  derived from single characteristic of division" (Vickery, quoted). Ranganathan's PMEST
  categories, or Vickery's thirteen, serve as candidate facet types, and subjects are
  synthesised by combining facet values rather than enumerated
  [hjorland-facet-analysis-2013]{203}. Construction steps are: define the field (which entities
  and which aspects interest the user group); formulate facets from "a representative range of
  material"; then structure each facet hierarchically. The structuring step is claimed to
  "indicate gaps in the system" [hjorland-facet-analysis-2013]{203}. A faceted scheme can be
  read as several division trees applied to the same class at once
  [fricke-logical-division-2016]{204}.
- **Evidence level: advocated; sparse and mixed comparative data.** In the Cranfield I test
  reported by Vickery, faceted retrieval scored 73.8% against 75.6–82.0% for UDC, alphabetical
  and Uniterm indexing (83% in a supplementary test) [hjorland-facet-analysis-2013]{203}.
  Hjørland finds discussion of limitations "rare" in the facet literature
  [hjorland-facet-analysis-2013]{203}. He calls its "main weaknesses" a lack of empirical basis
  and speculative ordering, and questions whether new subjects can always be expressed as
  combinations of pre-set categories [hjorland-facet-analysis-2013]{203}.

### 5. Four epistemic routes to forming classes

Hjørland distinguishes four routes. Rationalist logical division works downward from a basis of
division. Empiricist grouping by overall similarity is phenetics or numerical taxonomy, which
"maximize[s] homogeneity within classes and heterogeneity between classes". The other two are
historicist or genealogical classification by common ancestry, and pragmatic or critical
classification by purpose [hjorland-classification-2017]{205}. These routes can yield
different classes for the same objects. For example, numerical taxonomy and phylogenetic
methods disagree on birds and reptiles [hjorland-classification-2017]{205}. Mayr is quoted as
saying that downward division by single characters "actually produces identification schemes
rather than classifications" [hjorland-classification-2017]{205}. Whewell's test for
"natural" systems, also quoted, is that "the arrangement obtained from one set of characters
coincides with the arrangement obtained from another set" [hjorland-classification-2017]{205}.
That is a convergence check across independent character sets.

### 6. Explanatory typologies and ideal types

Typologies built from Weberian ideal types differ from "simple classification systems" that
order phenomena "into mutually exclusive and exhaustive categories"
[allen-explanatory-typologies-ib]{206}. Theory underpins the types, and the types need not be
mutually exclusive on every dimension [allen-explanatory-typologies-ib]{206}. The prescribed
steps are: clarify concepts; justify why the chosen dimensions are the important ones; model
and operationalize the types without assigning real cases "as if it were a category"; confront
the types with evidence; and re-assess afterwards [allen-explanatory-typologies-ib]{206}. For
choosing concepts there is "no specific method other than a mixture of prior knowledge and
guidance from theory" (attributed to Bailey) [allen-explanatory-typologies-ib]{206}.
Configurational analysis (fuzzy-set QCA) is cited as a way to surface "theoretically neglected
configurations" [allen-explanatory-typologies-ib]{206}. Evidence level: argued from published
exemplars, with no comparative evaluation.

### 7. Morphological fields as typologies

General morphological analysis treats each combination of one value per parameter as a
configuration (a cell). Cross-consistency assessment removes logically or empirically
incompatible pairs [ritchey-gma-general-method]{215}. Two of its practices carry over to
classification: cells play the same role as taxonomy cells, and a sample of configurations can
be chosen to cover all parameter states ("full field coverage")
[ritchey-psm-gma-2006]{216} {inferred: convergence}. The method's authors claim that poorly
defined parameters and incomplete value ranges are "immediately revealed" during consistency
assessment. This "garbage detection" claim is advocated, not measured
[ritchey-psm-gma-2006]{216} [ritchey-gma-general-method]{215}. (Morphological analysis itself
is the subject of a sibling facet.)

### 8. Participant sorting: concept mapping and card sorting

- In group concept mapping, participants brainstorm statements on a focus prompt and each
  participant sorts and rates them. Multidimensional scaling and cluster analysis then produce
  the map. How many clusters to keep is a judgement, not a prescribed rule
  [trochim-concept-mapping-kb]{212}.
- **Measured stability.** Six open card sorts (140 participants, two domains) gave Mantel
  correlations between studies of 0.609–0.930 and 90.9–96.5% similarity of base clusters.
  Navigation schemes cut at the elbow agreed 63.2–92.7%
  [katsanos-card-sort-cross-study-reliability-2019]{210}. Where to cut the dendrogram "greatly
  affects the final navigation scheme", and "two people can produce different content
  structures" from the same dendrogram [katsanos-card-sort-cross-study-reliability-2019]{210}.
  Nielsen reports Tullis and Wood's resampling of 168 sorters: correlation with the
  full-sample similarity was 0.75 at 5 sorters, 0.90 at 15, 0.95 at 30 and 0.98 at 60
  [nielsen-card-sort-sample-size-2004]{211}. {confidence: fetched-page-extract — the Tullis &
  Wood paper itself was not read}

## What counts as "genuinely different"

- **Difference on a purpose-relevant, discriminating dimension.** In the taxonomy literature,
  objects differ in kind when they occupy different characteristics of a dimension that follows
  from the meta-characteristic. Dimensions that do not discriminate are excluded
  [nickerson-taxonomy-development-method-2013]{200}. Facet analysis likewise requires each facet
  to come from a "single characteristic of division" [hjorland-facet-analysis-2013]{203}, and
  logical division requires one basis per step [fricke-logical-division-2016]{204}.
- **Natural vs artificial classes.** Mill, as quoted, holds that a classification is natural
  when its groups support more and more important general propositions, and artificial when
  they track an incidental trait, such as Linnaeus's stamen counts
  [hjorland-facet-analysis-2013]{203}. Bailey is quoted as saying that "a classification is no
  better than the dimensions or variables on which it is based"
  [nickerson-taxonomy-development-method-2013]{200}.
- **Monothetic vs polythetic membership.** Classical classes are defined by necessary and
  sufficient features. Polythetic and prototype classes need only a minimum number of a broader
  feature set, so no single feature is shared by all members [hjorland-classification-2017]{205}.
  Under polythetic membership, two items can belong to one family without sharing any single
  defining feature. A MECE check on single features can then split or merge such families
  {inferred: divergence} [hjorland-classification-2017]{205} [fricke-logical-division-2016]{204}.
- **Theory-linked difference.** In explanatory typologies, types differ because a theory
  predicts different outcomes from their configurations, not merely because attributes differ
  [allen-explanatory-typologies-ib]{206}.

## Completeness signals and their evidential status

| Signal | Source | What it checks | Evidence status |
|---|---|---|---|
| No new dimension or characteristic in the last iteration | [nickerson-taxonomy-development-method-2013]{200} | Convergence on the objects examined so far | Designed; never validated against later-found objects |
| Every characteristic has at least one object; unique cells | [nickerson-taxonomy-development-method-2013]{200} | Internal fit of scheme to sample | Designed; often waived for conceptually derived characteristics [szopinski-taxonomy-evaluation-criteria-2020]{202} |
| Comprehensive: all objects classifiable / all dimensions identified | [nickerson-taxonomy-development-method-2013]{200} | Coverage (two distinct senses) | Subjective judgement |
| Residual "other / not elsewhere classified" class | [fricke-logical-division-2016]{204} [bowker-star-sorting-things-out-1999]{207} | Guarantees formal exhaustivity | A technical device; does not show coverage |
| Agreement between independent character sets (Whewell) | [hjorland-classification-2017]{205} | Robustness of class boundaries | Stated as a maxim |
| Inter-rater agreement when classifying objects | [el-emam-defect-classification-repeatability-1998]{208} [falessi-odc-feasibility-2006]{209} | Repeatability of assignment to fixed classes | Measured; varies with rater training |
| Cross-study agreement of sort-derived groupings | [katsanos-card-sort-cross-study-reliability-2019]{210} | Stability of groupings across samples of sorters | Measured (two domains) |
| Users classify new objects with the scheme | [szopinski-taxonomy-evaluation-criteria-2020]{202} | Applicability and coverage on fresh objects | Advocated guideline |
| Re-evaluation after new objects appear | [szopinski-taxonomy-evaluation-criteria-2020]{202} | Robustness over time | Advocated guideline |

The "no new dimensions in the last iteration" rule has the same structure as saturation
stopping rules in qualitative analysis. There, a threshold on new information after a run of
observations still carries "no guarantee that saturation is in fact reached"
[guest-thematic-saturation-method-2020]{217} [nickerson-taxonomy-development-method-2013]{200}
{inferred: convergence}. In the Nickerson demonstration the run was a single iteration of three
applications [nickerson-taxonomy-development-method-2013]{200}.

## Practice and reliability evidence

- **Adoption, not efficacy.** Of 24 journal taxonomy articles (2013–2018), 58% cited no
  development method and 17% followed Nickerson et al. Ending conditions were stated in 17%,
  all of them Nickerson-based; 54% were not evaluated; 13% involved intended users; 46%
  examined no real objects [losser-taxonomy-research-assessment-2019]{201}. In a larger corpus,
  201 articles built a taxonomy and 63 evaluated one. Of the 38 evaluating articles that used
  Nickerson et al.'s method, 16 stated that they applied the ending conditions "without giving
  any further detail" [szopinski-taxonomy-evaluation-criteria-2020]{202}. Some articles excluded
  the "representative sample" condition, or the "every characteristic populated" condition. One
  excluded mutual exclusivity "with a more readable and less complex taxonomy" as the reason
  [szopinski-taxonomy-evaluation-criteria-2020]{202}. Evaluation criteria were heterogeneous:
  43 criteria across 54 articles, about half used once
  [szopinski-taxonomy-evaluation-criteria-2020]{202}.
- **Assignment reliability.** An ODC-derived defect scheme reached kappa 0.66 and 0.82 on real
  inspection data. Merging two confusable classes ("Data" and "Assignment") raised the lower
  kappa to 0.73 [el-emam-defect-classification-repeatability-1998]{208}. With 110 trained
  students classifying seeded defects, the most frequent category accounted for 69% of
  answers, and 97% of responses assigned exactly one category. Yet discrepancy between raters
  averaged 43%, falling from 60% to 17% as training increased. Several category pairs were
  "strongly affine" [falessi-odc-feasibility-2006]{209}. These studies measure whether raters
  agree on a fixed scheme. They do not measure whether the scheme's classes are complete
  {inferred: aggregate}.

## Failure modes and limits

- **MECE as an unmet ideal.** "No real-world working classification system that we have looked
  at meets these simple requirements and we doubt that any ever could." Schemes mix
  contradictory principles; exclusivity fails under ambivalent membership; completeness can be
  traded away [bowker-star-sorting-things-out-1999]{207}. Raters' single-category assignments
  (97%) sat alongside 43% inter-rater discrepancy, so how exclusive the categories feel did not
  track agreement on membership [falessi-odc-feasibility-2006]{209} {inferred: divergence}.
- **Exhaustivity by construction.** A residual class makes a division exhaustive by
  definition [fricke-logical-division-2016]{204}. The ICD deliberately distributes "not
  elsewhere classified" throughout rather than as a top-level class, so uncertainty does not
  pile up in one place [bowker-star-sorting-things-out-1999]{207}. A formally exhaustive scheme
  can therefore hide unrecognised families inside residual classes {inferred: aggregate}.
- **Dimension-choice dependence.** The meta-characteristic "impacts critically the resulting
  taxonomy", and "multiple taxonomies may be developed for a domain even when starting with the
  same meta-characteristic" [nickerson-taxonomy-development-method-2013]{200}. Because objects
  have unlimited properties, "any empirical classification is biased in ways that cannot be
  controlled", and similarity is not objective (colour vs shape)
  [hjorland-classification-2017]{205}. "Each standard and each category valorizes some point of
  view and silences another" [bowker-star-sorting-things-out-1999]{207}. Fixed fundamental
  categories may "force a discipline into a particular form, while being blind to other
  categories" [hjorland-facet-analysis-2013]{203}.
- **Judgement throughout.** Choosing the meta-characteristic, the ending conditions, the path,
  the object subsets and the dimensions "all require human judgment"
  [nickerson-taxonomy-development-method-2013]{200}. C2E passes offer "little guidance"
  [nickerson-taxonomy-development-method-2013]{200}. Cluster count and dendrogram cut are
  judgement calls [trochim-concept-mapping-kb]{212}
  [katsanos-card-sort-cross-study-reliability-2019]{210}.
- **Forcing exclusivity can cost insight.** Forcing exclusivity on independent options can
  re-entangle factors that a CE split had separated [chevallier-mece-vs-ice-2012]{213}.
- **Reification.** Ideal types treated as "things", or typologies as natural kinds, are a
  named pitfall [allen-explanatory-typologies-ib]{206} [hjorland-classification-2017]{205}.
- **Single-basis downward division** yields identification keys rather than classifications
  (Mayr, quoted) [hjorland-classification-2017]{205}.

## Disconfirming analysis

- *Does following a taxonomy method improve completeness?* None of the attested sources
  measures the coverage of taxonomies built with versus without a method. The available
  measures are rates of use and of transparent reporting. Articles that followed Nickerson et
  al. described their process transparently, which is an association with reporting, not with
  completeness [losser-taxonomy-research-assessment-2019]{201}. The method's own demonstration
  stops on a one-iteration no-change rule over a convenience sample
  [nickerson-taxonomy-development-method-2013]{200}. Result: no evidence was found for or
  against coverage gains.
- *Do deductive and inductive routes converge on the same classes?* Mills claims an inductive
  approach gave results "remarkably similar" to faceted ones. Hjørland could find no empirical
  evidence for the claim and holds that inductive and deductive principles produce different
  classifications [hjorland-facet-analysis-2013]{203}. The bird/reptile case shows phenetic and
  phylogenetic methods diverging [hjorland-classification-2017]{205}. Result: the convergence
  claim is unsupported; divergence is documented in at least one domain.
- *Are MECE checks reliable?* Coders in the IS review judged 67% of taxonomies MECE and none
  non-MECE, but they based this on the stated characteristics, counting complementary pairs
  and continua as exhaustive [losser-taxonomy-research-assessment-2019]{201}. That is a check
  on form, not on how objects are actually assigned. Assignment studies show agreement varying
  with training [falessi-odc-feasibility-2006]{209}
  [el-emam-defect-classification-repeatability-1998]{208}.
- *Is one sorting study enough?* The cross-study evidence supports stable groupings for
  similar-profile participants in two general-purpose domains
  [katsanos-card-sort-cross-study-reliability-2019]{210}. It does not test heterogeneous or
  expert populations, and agreement on navigation schemes dropped to 63% in one pair
  [katsanos-card-sort-cross-study-reliability-2019]{210}.
- *Did facet analysis improve retrieval?* The one comparative figure reported (Cranfield I)
  places faceted retrieval below the three alternatives tested
  [hjorland-facet-analysis-2013]{203}.

## Contradictions

- **ODC repeatability** (`qualifies`). El Emam & Wieczorek report "sufficiently high
  repeatability" (kappa 0.66/0.82) with professional inspectors on real defects
  [el-emam-defect-classification-repeatability-1998]{208}. Falessi & Cantone report 43%
  discrepancy among trained students on seeded defects, and cite Henningsson & Wohlin as
  finding subjectivity [falessi-odc-feasibility-2006]{209}. Raters, defects and schemes all
  differ between the two studies.
- **MECE as a requirement** (`incommensurable`). Nickerson et al. make mutually exclusive,
  collectively exhaustive characteristics definitional for a taxonomy
  [nickerson-taxonomy-development-method-2013]{200}. Allen et al. place MECE categories in
  "simple classification systems" and allow ideal-type dimensions that are not mutually
  exclusive [allen-explanatory-typologies-ib]{206}. Chevallier argues for "independent" rather
  than exclusive branches [chevallier-mece-vs-ice-2012]{213}. Each defines a different
  artifact (taxonomy, explanatory typology, problem-decomposition tree), so the positions are
  recorded side by side. {incommensurable: artifact type}
- **Ending conditions as evaluation** (`tension`). In practice the subjective ending conditions
  are often reused to evaluate the finished taxonomy. The same source says design science
  "advocates that a rigorous research process should strictly separate building from
  evaluation" [szopinski-taxonomy-evaluation-criteria-2020]{202}.
- **How many sorters / studies** (`tension`). Nielsen's rationale for larger sorting samples is
  "great variability in different people's mental models"
  [nielsen-card-sort-sample-size-2004]{211}. Katsanos et al. conclude that the multiple-mental-model concern
  "may not be that strong, at least for similar profile participants"
  [katsanos-card-sort-cross-study-reliability-2019]{210}.
- **Inductive–deductive convergence** (`contradicts`). Mills's claim of similarity, as quoted,
  stands against Hjørland's position that the routes produce different classifications
  [hjorland-facet-analysis-2013]{203}.

## Transfer-relevant observations

Stated in the field's own terms, without application recommendations.

- Taxonomy methods put a purpose statement (meta-characteristic) before generation. Candidate
  dimensions are admitted only if they follow from that purpose and discriminate among objects
  [nickerson-taxonomy-development-method-2013]{200}.
- The prescribed way to vary perspective is to alternate passes from objects (E2C) and from
  concepts (C2E) [nickerson-taxonomy-development-method-2013]{200}. In knowledge organization,
  rationalist, empiricist, genealogical and pragmatic routes are distinguished, and they can
  yield different classes for the same objects [hjorland-classification-2017]{205}.
- The completeness signals the field names are of three kinds:
  - stability of the scheme over the last pass;
  - formal coverage, through populated characteristics and residual classes;
  - agreement, between raters, between independent character sets, or across sorting
    studies.

  Only the agreement measures have published reliability data. None of the signals has been
  tested against later discovery of missing classes [nickerson-taxonomy-development-method-2013]{200}
  [szopinski-taxonomy-evaluation-criteria-2020]{202} [katsanos-card-sort-cross-study-reliability-2019]{210}
  {inferred: aggregate}.
- Empty cells in a dimension × characteristic grid are read as candidate unoccupied
  combinations [nickerson-taxonomy-development-method-2013]{200}. In morphological practice,
  configuration samples are chosen to cover every parameter state [ritchey-psm-gma-2006]{216}.
- Reporting guidance asks for explicit justification of which ending conditions were applied
  and to what degree they were met. It also asks for independent classification of objects by
  people outside the build team [szopinski-taxonomy-evaluation-criteria-2020]{202}.

## Revisit if

- Kundisch et al. (2022, "An update for taxonomy designers", BISE) or Nobes & Stadler (2013,
  AOS) are acquired. The first may carry extended-process recommendations and further practice
  statistics. The second reports experiments on how classifier and characteristic choices change
  classifications. Both were blocked in this session (see acquisition candidates).
- A study appears that compares taxonomies built under explicit ending conditions with
  independently found objects (held-out coverage).
- Assignment-reliability or sorting-stability studies appear for expert populations
  classifying methods or approaches, not defects or web content.
- Bailey (1994) or Doty & Glick (1994) primary text is fetched, to replace the cite-through
  claims.
