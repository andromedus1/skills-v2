---
title: "Cluster synthesis — generation: producing genuinely different approaches"
provenance: agent-synthesis
updated: 2026-10-20
summary: >-
  Cross-specialist synthesis over four facets (design-space methods, decision-option generation,
  analogous-domain search, LLM ideation diversity) on how to generate a set of genuinely different
  approaches rather than variations of one. Unaided generation recovers roughly a third to a half of
  later-recognised items, and LLM generation narrows mainly across independent draws and across
  models. Exposure to examples or consensus narrows sets; independent generation before exposure,
  then pooling, widens them. Measured gains come from a second pass that states the first is
  incomplete, conditioning on prior output with an instruction to differ, objectives or purpose as
  stimuli, and abstraction at a workable level for distant retrieval. Structured generators
  (morphological fields, QOC, set-based design, strategy tables) are advocated or demonstrated, not
  measured against unstructured generation, and the effect of domain distance is mixed.
key_findings:
  - Unaided generation of objectives and alternatives recovers roughly 30–50% of later-recognised items, and omitted items are about as important as generated ones.
  - LLM idea pools are narrower mainly across independent draws and across models; a single session's list can look varied while repeated draws return the same modes.
  - Showing examples or consensus narrows the set (more misses with upfront examples; fixation; lower diversity under debate and similarity feedback), while independent generation pooled before discussion yields a more complete set.
  - Measured gains come from a second pass with a warning and a numeric target, from generation that sees prior items and is told to differ, from distinct per-draw cues, and from objectives or purpose used as stimuli.
  - The fields test "different approach" by the abstraction level at which ideas diverge (principle versus embodiment), a different value on a declared dimension, or non-equivalence under a declared relation.
  - Structured generators lack controlled evidence of better coverage; the one reported matrix-size result was negative, TRIZ results are mixed, and the effect of domain distance on novelty and quality is contradictory.
---

# Generation cluster: producing genuinely different approaches

## Scope and inputs

This synthesis composes four within-specialist briefs of the `solution-space-decomposition`
campaign: design-space and morphological methods, decision-analysis option generation,
analogous-domain search, and LLM ideation diversity. It asks how each field generates a set of
genuinely different approaches, what measurably widens or narrows that set, and how the fields tell a
different approach from a variation. Evidence levels follow the specialist briefs: **advocated**,
**demonstrated**, **measured**; abstract-level and press-release sources are marked.

## 1. The baseline: unaided generation is incomplete, and narrows in characteristic ways

- **People.** Across three lab studies, participants "consistently omitted nearly half of the
  objectives that they later identified as personally relevant", and omitted objectives were "almost
  as important" as generated ones [bond-carlson-keeney-objectives-2008]{452}; a reanalysis put
  first-attempt yield at "30% to 50%" [bond-carlson-keeney-improving-objectives-2010]{453}. For
  alternatives, decision makers "identify less than half of their alternatives", and overlooked
  alternatives were of the same average quality [siebert-keeney-alternatives-2015]{450} {confidence:
  abstract-only}; the Bayreuth release reports 37% unaided recall against a master list
  [siebert-keeney-press-2015]{451}.
- **Narrowness, not only shallowness.** Self-generated items concentrated in each person's top
  category of the reference list — "breadth of thinking was insufficient"
  [bond-carlson-keeney-improving-objectives-2010]{453}.
- **Fixation.** Designers shown examples "tended to repeat key features" even when told not to (Jansson
  and Smith, as reported) [crilly-cardoso-fixation-2017]{114}; a flawed example reduced non-redundant
  ideas among engineering faculty, who believed it had helped
  [linsey-design-fixation-faculty-2010]{417}. Unaided analogical retrieval is surface-bound: about 30%
  applied a prior analogy spontaneously versus about 75% with a hint
  [gick-holyoak-schema-induction-1983]{416}.
- **LLMs: collective and cross-model narrowing.** Population-level response variability was far lower
  for LLMs than humans while individual originality was similar [wenger-kenett-creative-homogeneity-llms-2025]{306};
  responses from different models had average pairwise similarity of 71–82%
  [artificial-hivemind-homogeneity-2025]{307}; a single GPT-4o session explored categories at nearly
  the human rate, but independent first ideas across sessions covered far fewer combinations
  [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}. Each OLMo 2 post-training stage reduced
  diversity [noveltybench-humanlike-diversity-2025]{310}.
- **Recall, not only knowledge.** Frontier models encode most benchmark facts but recall rare ones
  less often (63.3% versus 84.6% for popular facts in one model)
  [calderon-recall-bottleneck-factuality-2026]{320}; models judge set membership far better than they
  author the set, and the dominant authoring error is omission
  [judging-not-enumerating-omissions-2026]{321}. These sources study facts and predicates, not approach
  families; transfer is an analogy (LLM specialist, marked `extends`).
- **Generators misjudge their own completeness.** Laypeople and experienced mechanics alike
  under-weighted what a pruned fault tree left out [fischhoff-slovic-lichtenstein-fault-trees-1978]{464};
  self-perception of fixation was inaccurate [linsey-design-fixation-faculty-2010]{417}.

## 2. What narrows a set, and what widens it

### 2.1 Exposure before generation narrows; independence then pooling widens

Four facets converge on one ordering effect.

- Upfront examples increased misses (10.8 versus 7.9), consistent with part-list cueing
  [bond-carlson-keeney-improving-objectives-2010]{453}; more examples did not raise distant analogies
  (Dahl and Moreau, as reported) [vasconcelos-crilly-inspiration-fixation-2016]{418}.
- In LLMs, telling the model the similarity of existing ideas produced the least diverse pool, and
  "40 sessions then groups pick the best 10" was worse than the base prompt
  [meincke-prompting-idea-variance-2024]{117}; standard multi-agent debate lowered diversity across
  runs below single-agent generation, even with heterogeneous model families
  [creative-mad-debate-diversity-2026]{317}.
- Pooling independent lists before discussion widened the set: each of 12 executives listed on
  average 36% of 39 objectives, and "the aggregated list ... was a much more complete set"
  [bond-carlson-keeney-objectives-2008]{452}. The prescription is independent generation first,
  because "communication may redirect individuals' from their own ideas"
  [bond-carlson-keeney-improving-objectives-2010]{453}. Distinct per-agent "cognitive lenses" with each
  agent seeing only its most distant peers recovered about 26% of semantic diversity
  [creative-mad-debate-diversity-2026]{317}.
- Pooling helps only if generators draw from different regions: different prompting strategies'
  early ideas overlapped little [meincke-prompting-idea-variance-2024]{117}, while different models
  overlapped heavily [artificial-hivemind-homogeneity-2025]{307}.

### 2.2 Measured second-pass and conditioning techniques

- **Warning plus target.** A second pass with a warning that people list under half and that missed
  items matter added 2.77 items (87% added any) versus 0.55 for a plain review; adding "at least three /
  six / nine" added 3.08 / 3.90 / 4.87, with no quality loss in the successful arms
  [bond-carlson-keeney-improving-objectives-2010]{453}. More time or a week of rumination did not close
  the gap [bond-carlson-keeney-objectives-2008]{452} [siebert-keeney-press-2015]{451}.
- **See prior items, then differ.** Meincke et al.'s chain-of-thought prompt (list, then revise so that
  "No two ideas should be the same") gave the lowest similarity of any prompt, with caveats on model
  version and an advantage that vanished after about 750–800 ideas
  [meincke-prompting-idea-variance-2024]{300}; in-context regeneration — show prior outputs and ask for a
  different one — reached human-level distinctness for three frontier models
  [noveltybench-humanlike-diversity-2025]{310}; verbalized sampling reported 1.6–2.1x semantic diversity,
  measured only by its proposing authors [verbalized-sampling-mode-collapse-2025]{311}.
- **Distinct cues per draw.** Ordinary everyday personas raised between-session spread 2.6x and, with
  chain-of-thought, exceeded human category-combination coverage in one model and domain
  [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}.
- **Categories: timing matters.** A category-structured second pass raised the self-generated set by
  over 30%, while upfront categories yielded "more specific (but not more complete) sets"
  [bond-carlson-keeney-improving-objectives-2010]{453}.

### 2.3 Objectives or purpose as the generation key

- Using objectives as stimuli "enhances both the number and quality of created alternatives" across
  four studies [siebert-keeney-alternatives-2015]{450} {confidence: abstract-only}; the release reports
  objective-first students finding twice as many alternatives [siebert-keeney-press-2015]{451}.
- In analogy retrieval, holding purpose fixed while diversifying mechanism gave a 46% good-idea rate
  versus 37% for random and 30% for keyword-similar inspirations (38 workers, wide intervals)
  [hope-analogy-mining-purpose-mechanism-2017]{414}.
- The SDM module builds alternatives from the best consequence for each conflicting objective, then
  hybrids, and asks for alternatives whose outcomes are "discrete from each other"
  [usfws-usgs-sdm-developing-alternatives-2011]{458} (advocated).

### 2.4 Abstraction and distance

- **Abstraction at a workable level aids far retrieval.** Comparing two analogs raised unprompted
  transfer from 21% to 45%, while single-analog summaries and diagrams did not
  [gick-holyoak-schema-induction-1983]{416}; concrete constraint schemas gave relevant but still
  distant inspirations [kittur-scaling-analogical-innovation-2019]{415}; problems framed "too
  abstract" yield alternatives less likely to fit (Zahner et al., as reported)
  [vasconcelos-crilly-inspiration-fixation-2016]{418}.
- **Distance effects are mixed.** Far examples raised novelty versus near in one study
  [chan-fu-analogy-distance-commonness-2011]{403} and lowered novelty and quality in another
  [fu-near-far-analogy-2013]{404}; source distance related inversely to shortlisting across 707
  concepts [chan-dow-schunn-distant-inspiration-2015]{405}; analogous-market solvers were more novel but
  less immediately usable [franke-poetz-schreier-analogous-markets-2014]{273}; solver distance had a
  small positive association in one contest study [jeppesen-lakhani-marginality-broadcast-search-2010]{400}
  and no main effect in a follow-up [acar-van-den-ende-knowledge-distance-2016]{401}.
- **Random is not analogous.** Random inspirations gave diversity "but not relevance"
  [hope-analogy-mining-purpose-mechanism-2017]{414}; temperature raised diversity only slightly while
  producing nonsense [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}.

### 2.5 Structured generators: advocated more than measured

- General morphological analysis enumerates the product of declared parameters and prunes by
  cross-consistency [ritchey-gma-general-method]{100}; no controlled comparison against unstructured
  generation was found, and its developer notes it is "written about and discussed far more than it has
  actually been used" [ritchey-psm-gma-2006]{101}.
- Larger morphological matrices with many functions relative to means were associated with
  lower-quality concepts (Smith et al., as reported) [martinsson-bonde-mm-combinatorics-2025]{103}.
- TRIZ raised novelty at two of three sites and not the third [vargas-hernandez-triz-experiment-2012]{105};
  its contradiction matrix's reliability "is often questioned" [borgianni-triz-inventive-principles-2021]{106}.
- QOC's co-developers found "comparatively weak evidence regarding usability and utility"
  [buckingham-shum-dr-hypermedia-2005]{108}; set-based design research is "predominantly qualitative"
  [toche-set-based-design-review-2020]{109}; strategy tables and value-focused brainstorming are
  prescribed without attested controlled tests [usfws-usgs-sdm-developing-alternatives-2011]{458}
  [keeney-value-focused-brainstorming-2012]{455} {confidence: abstract-only}.
- LLM-generated dimensions (Luminate) have qualitative evaluation only, and the authors note
  "dimensional reasoning does not happen naturally" even for experts
  [luminate-design-space-generation-2023]{118}.

## 3. Telling a different approach from a variation

- **Abstraction level of divergence.** Ideas are placed on a genealogy tree (physical principle →
  working principle → embodiment → detail); "An idea could achieve the objective by ____" names the
  principle level, and differences at higher levels weigh more
  [sorensen-ideation-metrics-axioms-2026]{113}.
- **Declared dimensions.** Two configurations differ by construction in at least one parameter value
  [ritchey-gma-general-method]{100}; design spaces are "discrete Cartesian" spaces of design decisions
  [shaw-petre-design-spaces-2024]{110}.
- **Declared equivalence.** Symmetry-breaking predicates stop an engine sampling "multiple equivalent
  design candidates" [kang-dse-equivalence-2010]{111} {confidence: abstract-only}; NoveltyBench counts
  learned functional-equivalence classes [noveltybench-humanlike-diversity-2025]{310}.
- **Purpose versus mechanism.** Retrieval held purpose fixed and varied mechanism
  [hope-analogy-mining-purpose-mechanism-2017]{414}; contest winners for one problem used "differing
  scientific mechanisms" [jeppesen-lakhani-marginality-broadcast-search-2010]{400}.
- **Measured breadth is category-count based** — distinct categories or option-tree limbs accessed
  [delmissier-option-generation-ideation-2015]{459} [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312},
  and conclusions depend on the categorization scheme [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}.

## 4. Quantity, quality and distinctness

More options lowered mean quality in two problems while raising the best option's quality
[delmissier-option-generation-ideation-2015]{459}; number of options tracked set divergence and maximum
originality but not mean originality, and related negatively to feasibility
[schweizer-creative-option-generation-2016]{460}. The 2016 release reports that "a set of few but clearly
distinguishable alternatives scored better than a set of many but mutually similar alternatives"
[siebert-novices-press-2016]{454}. Frequency-based selection of approaches keeps the commonest ones
[naik-div-se-diversity-of-thought-2023]{314}.

## Contradictions

| Relationship | Positions |
|---|---|
| `contradicts` | Far-field examples raised novelty versus near [chan-fu-analogy-distance-commonness-2011]{403}; far stimuli lowered maximum novelty and quality [fu-near-far-analogy-2013]{404}. Fu et al. reconcile them post hoc by mapping both stimulus sets onto one similarity structure. |
| `tension` | Analogous-market solvers more novel [franke-poetz-schreier-analogous-markets-2014]{273} versus an inverse distance–shortlisting relation [chan-dow-schunn-distant-inspiration-2015]{405}; outcome constructs differ. |
| `qualifies` | Categories help as a second pass but not upfront [bond-carlson-keeney-improving-objectives-2010]{453}. |
| `qualifies` | Celebrity or "creative entrepreneur" personas modestly helped in one study [meincke-prompting-idea-variance-2024]{300}; ordinary personas beat them in another [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}. |
| `incommensurable` | LLMs below pooled humans even with the best prompt [meincke-prompting-idea-variance-2024]{300} [wenger-kenett-creative-homogeneity-llms-2025]{306} versus persona-plus-CoT and in-context regeneration matching or exceeding humans [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312} [noveltybench-humanlike-diversity-2025]{310}; metrics, domains and models differ. |
| `qualifies` | More options lower mean quality and can worsen expert choices (Johnson and Raab, as reported) [delmissier-option-generation-ideation-2015]{459} versus raising best-option quality [schweizer-creative-option-generation-2016]{460}; mean versus max, and populations differ. |
| `tension` | Few distinct alternatives beat many similar ones [siebert-novices-press-2016]{454} versus objectives-stimulated generation raising both number and quality [siebert-keeney-alternatives-2015]{450} {confidence: abstract-only}. |
| `tension` | Fixation as "premature closure" [daly-design-heuristics-2012]{104} versus fixation as sometimes neutral or time-saving [crilly-cardoso-fixation-2017]{114}. |
| `tension` | Exposure to AI ideas narrowed collective diversity [doshi-hauser-genai-collective-diversity-2024]{302} versus increased it in a dynamic multi-generation pool [ashkinaze-ai-ideas-collective-diversity-2024]{304} {confidence: search-summary}. |

## Disconfirming analysis

- *Structured generators improve coverage over unstructured generation.* Not supported as measured for
  morphological fields, QOC, set-based design or strategy tables; one reported matrix result was
  negative and TRIZ results are mixed (Section 2.5).
- *More reviewers, agents or models widen the set.* Disconfirmed for standard debate and for ensembles of
  models with shared priors [creative-mad-debate-diversity-2026]{317} [artificial-hivemind-homogeneity-2025]{307};
  supported for independently generated lists pooled before discussion, in one demonstrated case
  [bond-carlson-keeney-objectives-2008]{452}.
- *Distant sources yield more different approaches.* Study-specific only (Section 2.4); even the positive
  study found neither near nor far examples beat a no-example control on novelty
  [chan-fu-analogy-distance-commonness-2011]{403}.
- *Incompleteness harms decisions.* The objectives authors disclaim direct evidence
  [bond-carlson-keeney-objectives-2008]{452}; recognition-primed experts act on one plausible option
  [klein-rpd-model-overview]{463}, though Take-the-First held only at high expertise in chess
  [raab-chess-take-the-first-replication-2026]{462}.
- *Explicit dimension enumeration improves coverage.* No attested source measures a coverage gain from
  generated dimensions [luminate-design-space-generation-2023]{118}.

## Transfer-relevant observations

Stated in the source fields' own terms; not recommendations.

- Generation before exposure, then a de-duplicated union, is the prescribed group order
  [bond-carlson-keeney-improving-objectives-2010]{453} [keeney-value-focused-brainstorming-2012]{455}
  {confidence: abstract-only}; consensus exposure measured as neutral or harmful to diversity
  [meincke-prompting-idea-variance-2024]{300} [creative-mad-debate-diversity-2026]{317}.
- Effective second passes state that the first pass is typically incomplete and set a numeric target
  [bond-carlson-keeney-improving-objectives-2010]{453}, or show prior items with an instruction to differ
  [noveltybench-humanlike-diversity-2025]{310}.
- Objectives or purpose serve as generation keys with measured support
  [siebert-keeney-alternatives-2015]{450} {confidence: abstract-only} [hope-analogy-mining-purpose-mechanism-2017]{414}.
- Distinctness is operationalised by abstraction level, declared dimensions or declared equivalence,
  and measured breadth is a category count relative to a scheme [sorensen-ideation-metrics-axioms-2026]{113}
  [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}.
- Separating the person who abstracts a problem from the person who searches is advocated as a fixation
  guard [kittur-scaling-analogical-innovation-2019]{415} [linsey-wordtree-method-2008]{411}.
- Generators' own judgements of completeness and helpfulness are unreliable
  [fischhoff-slovic-lichtenstein-fault-trees-1978]{464} [linsey-design-fixation-faculty-2010]{417}
  [ding-llm-cross-domain-analogies-2023]{420}.

## Open questions carried to the parent

- How problem framing and reformulation (abstract versus concrete statements) changes which families
  are generated; held only through cite-through here [vasconcelos-crilly-inspiration-fixation-2016]{418}.
- Whether a challenger shown the sample it is challenging is anchored by it, as upfront examples
  anchored generators [bond-carlson-keeney-improving-objectives-2010]{453}.

## Revisit if

- Full texts of Siebert and Keeney (2015) and Gettys et al. (1987) are acquired.
- A controlled study compares a structured generator, or LLM-generated dimensions, with unstructured
  generation on coverage of a reference set of approaches.
- Independent replications of verbalized sampling or in-context regeneration on approach enumeration
  report coverage effects.
- A meta-analysis establishes the distance–novelty–quality relation across problems with a common
  distance metric.
