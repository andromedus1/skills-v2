---
title: Analogous-domain search for genuinely different approaches
provenance: agent-synthesis
updated: 2026-10-20
summary: >-
  Within-specialist brief on finding different solution approaches by searching distant or analogous
  domains: broadcast search and solver distance, analogous-market search, design-by-analogy with near
  vs far sources, problem abstraction as a retrieval key (functional models, WordTrees, purpose-mechanism
  schemas, multi-analog schema induction, LLM-generated analogies), and design fixation as the cause of
  variations-of-one-idea. Measured effects of distance are mixed and partly contradictory: distant
  sources raise novelty and variance in some studies and lower novelty and quality in others; several
  report a too-near/too-far band, and one large field study finds an inverse distance–creativity
  relation. The more consistent measured findings concern the retrieval step: unaided retrieval is
  surface-bound, problem abstraction and comparison across multiple analogs improve far retrieval, and
  retrieval that is diverse in mechanism while staying close in purpose beats both keyword-similar and
  random stimuli in one controlled test.
---

# Analogous-domain search for genuinely different approaches

## Scope

This facet covers how searching outside a problem's home domain is used to surface approaches that are
different in kind rather than variants of a familiar one, and what the measured evidence says about it.
Four strands are covered: (1) broadcast search and solver distance in open innovation contests;
(2) analogous-market search; (3) design-by-analogy (DbA) in engineering design, including near vs far
sources and problem re-representation as a retrieval key; and (4) design fixation as a cause of
variations-of-one-idea. Evidence levels used below: **advocated** (method proposed, rationale argued),
**demonstrated** (case study or illustration, no comparison condition), **measured** (controlled
experiment or statistical observational study with a comparison).

## 1. Why home-domain search yields variations of one idea

**Fixation on examples (measured, mostly student lab studies).** Jansson and Smith's student designers,
shown pictures of existing solutions, "tended to repeat key features" of them, and did so "even when
participants received instructions to avoid repeating particular features", as reported by
[crilly-cardoso-fixation-2017]{419} and [vasconcelos-crilly-inspiration-fixation-2016]{418}. In
engineering design faculty, a deliberately flawed example reduced the number of non-redundant ideas
(control > fixation, t = 2.94, p < 0.02), increased reuse of the example's features, and raised the share
of gas-engine designs [linsey-design-fixation-faculty-2010]{417}. More-common examples narrowed breadth
of search relative to less-common examples (d = −0.61) and to no examples (d = −1.03)
[chan-fu-analogy-distance-commonness-2011]{403}.

**Instructions and self-perception do not reliably correct it (measured, mixed).** Telling participants
to diverge from examples "did not decrease the participants' conformity" (Smith et al. 1993, as reported),
and the review judges research "equivocal on the benefits of constraining instructions"
[vasconcelos-crilly-inspiration-fixation-2016]{418}. The fixated faculty group tended to believe the
example had helped them; the authors conclude "participant perceptions are not an accurate tool for
evaluating design methods" [linsey-design-fixation-faculty-2010]{417}.

**Retrieval is surface-bound (measured in lab; restated in reviews).** With a hint to use a prior
analogous story about 75% solved Duncker's radiation problem by convergence, but without a hint only
about 30% did, so "only a third or less" of those who could apply the analogy spontaneously noticed it
[gick-holyoak-schema-induction-1983]{416}. The same surface-similarity bias — favouring "'near,' or
within-domain, analogs" over structurally similar far ones — is the stated premise of the computational
and crowd work in [kittur-scaling-analogical-innovation-2019]{415} and
[hope-analogy-mining-purpose-mechanism-2017]{414}. Without guidance, people "select domains to search
based on surface similarity to the problem's domain" [kittur-scaling-analogical-innovation-2019]{415}.
In market search, managers "tend to stay within their own market context"
[franke-poetz-schreier-analogous-markets-2014]{402}.

**Concrete artefacts narrow reach (measured, in vivo, one team).** In a professional medical-plastics
team, talk around physical prototypes produced significantly fewer between-domain analogies than talk
around ideas or sketches (χ²(2) = 19.26, p < .001) [christensen-schunn-analogical-distance-2007]{406}.

## 2. Methods that search distant or analogous domains

### 2.1 Broadcast search and solver distance (measured, observational)

Broadcast search posts a problem openly and lets external solvers self-select. Across 166 InnoCentive
science challenges from 26 firms' R&D labs, 49 were solved (29.5%); solved problems drew more than twice
as many submissions as unsolved ones (16.8 vs 7.0) [jeppesen-lakhani-marginality-broadcast-search-2010]{400}.
Winning was positively associated with the solver's self-assessed distance from the problem field, but the
effect is modest: odds of winning up 3.3% per scale step, significant only at the 10% level
[jeppesen-lakhani-marginality-broadcast-search-2010]{400}. The authors' mechanism is diversity of
"perspectives and heuristics": "what matters is to be different and relevant", and the odds of a solve
"increase with each additional solver who arrives with a different analytical toolkit"
[jeppesen-lakhani-marginality-broadcast-search-2010]{400}. One challenge received four winning solutions
"with differing scientific mechanisms" from an aerospace physicist, an agribusiness owner, a transdermal
drug-delivery specialist and an industrial scientist [jeppesen-lakhani-marginality-broadcast-search-2010]{400}
— an illustration that independent distant solvers can return different approach families to one problem.

A follow-up on the same platform found **no main effect** of knowledge distance (OR 0.99, p > .25); distance
helped only for solvers with high effort and focused (low-variation) search, and hurt when both effort and
variation were high, while insiders did best with high-variation recombination
[acar-van-den-ende-knowledge-distance-2016]{401}.

### 2.2 Analogous-market search (measured, one field experiment)

Franke, Poetz and Schreier ran a symmetric experiment with 213 solvers from roofing, carpentry and inline
skating, three markets sharing the analogous problem of safety-gear comfort; solutions from
analogous-market solvers "show lower potential for immediate use" but "substantially higher levels of
novelty", with the effect strongest "in the upper tail of the novelty distribution"
[franke-poetz-schreier-analogous-markets-2014]{402}. Analogous markets were selected by explicit criteria
(shared analogous problem, delineated markets, comparable importance, accessible sampling) after secondary
research and expert interviews — the markets were hand-picked
[franke-poetz-schreier-analogous-markets-2014]{402}.

### 2.3 Problem abstraction as the retrieval key

These methods re-describe the problem in domain-neutral terms so that sources from other domains match it.

| Method | How it generates alternatives | Evidence level |
|---|---|---|
| WordTree: verbs from functions/customer needs re-represented by hypernyms/troponyms (team + WordNet), problem statements written from domain-specific to general, a second team ideates without seeing the original problem [linsey-wordtree-method-2008]{411} | Unusual verb senses point to "distant but analogous domains" (e.g. "fold" → sailing) [linsey-wordtree-method-2008]{411} | demonstrated (one case study); authors state "Much more evaluation ... needs to be completed" [linsey-wordtree-method-2008]{411} |
| Functional-basis vector search over patents [murphy-function-based-analogy-search-2014]{412} | Patents indexed by function verbs, so retrieval ignores solution domain; returns "very near-field ... to far-field cross-domain analogies" [murphy-function-based-analogy-search-2014]{412} | demonstrated (two case studies) |
| Same search in a controlled experiment [fu-functional-analogy-search-2015]{413} | Patents retrieved from functional descriptions shown mid-ideation | measured: novelty above control only for the all-functions query; no change in quantity; quality not measured; n = 17 per group [fu-functional-analogy-search-2015]{413} |
| Purpose–mechanism schemas, cluster by purpose then diversify by mechanism (MAX-MIN selection) [hope-analogy-mining-purpose-mechanism-2017]{414} | Near-purpose, far-mechanism inspirations, chosen to be mutually dissimilar | measured: good-idea rate 46% vs 37% random vs 30% TF-IDF (k = 2); wide CIs; 38 crowd workers [hope-analogy-mining-purpose-mechanism-2017]{414} |
| Crowd schema pipelines: separate people abstract, search and apply; two-stage "suggest three types of experts" domain search; constraint-level schemas [kittur-scaling-analogical-innovation-2019]{415} | Abstract schemas lead searchers to distant expert domains (contortionists, Japanese aesthetics) instead of near ones (electricians) | measured in the authors' separate studies, summarised without sample sizes; "several unsuccessful" configurations not reported [kittur-scaling-analogical-innovation-2019]{415} |
| Schema induction by comparing two analogs [gick-holyoak-schema-induction-1983]{416} | Describing similarities of two analogs yields an abstract schema that later cues far retrieval | measured: unprompted transfer 45% with two analogs vs 21% with one; single-analog summaries, principle statements or diagrams alone "None ... achieved a notable degree of sucess" [gick-holyoak-schema-induction-1983]{416} |
| LLM-generated cross-domain analogies with a stakeholder/context/goal/obstacle prompt [ding-llm-cross-domain-analogies-2023]{420} | Holds goal and obstacle fixed, varies stakeholder and context to set distance | measured without a no-analogy control: median helpfulness 4/5, ~80% led to observable reformulation; up to ~25% potentially harmful [ding-llm-cross-domain-analogies-2023]{420} |
| TRIZ contradiction matrix: problem restated as a conflict of generic parameters, mapped to inventive principles abstracted from patents [vargas-hernandez-triz-experiment-2012]{422} | Generic principle catalogue as a cross-domain lookup | measured, mixed: novelty up at two of three sites, not the third [vargas-hernandez-triz-experiment-2012]{422}; matrix reliability "often questioned" [borgianni-triz-inventive-principles-2021]{423} |

Abstraction has a measured limit at both ends. Abstract problem statements promote divergence and concrete
ones convergence, but "if a problem is framed in terms that are too abstract, then alternatives are less
likely to fit the problem requirements" (Zahner et al., as reported) [vasconcelos-crilly-inspiration-fixation-2016]{418}.
Vacuous schemas ("a problem was solved using logical means") predicted poor transfer
[gick-holyoak-schema-induction-1983]{416}. Constraint schemas made concrete ("prevent tipping over") gave
more relevant inspirations "that were still distant" than higher-level ones ("safety")
[kittur-scaling-analogical-innovation-2019]{415}. Ding et al. informally found their structured prompt
balanced distance and usefulness better than prompting for "an abstracted schema"
[ding-llm-cross-domain-analogies-2023]{420}.

### 2.4 Defixation by re-representation (measured, small n)

Giving fixated faculty a functional description, analogies (some found with WordTree), a list of energy
sources and a back-of-envelope calculation reduced fixation "but it did not completely eliminate it": the
control group still produced the most concepts, while the defixation group "employed a greater diversity of
energy-based solutions" [linsey-design-fixation-faculty-2010]{417}. Group sizes were 9–12.

## 3. Does distance help? The measured record

| Study | Setting | Distance effect | Level |
|---|---|---|---|
| [chan-fu-analogy-distance-commonness-2011]{403} | 153 students, patent examples | Far vs near: novelty up (d = 0.56), quality variance up, about one fewer concept; neither near nor far differed from no-example control on novelty | measured |
| [fu-near-far-analogy-2013]{404} | 72 students, same problem | Far worse than near on max novelty (d = −0.82) and quality (d = −0.76); far rated less relevant; "too near" and "too far" | measured |
| [chan-dow-schunn-distant-inspiration-2015]{405} | 707 OpenIDEO concepts, 12 challenges | Each unit of source distance −0.33 to −0.40 log-odds of shortlisting; far-citing concepts converge on no-citation rate | measured (observational) |
| [chan-schunn-far-analogy-in-vivo-2014]{407} | One professional team | Far analogies followed by more incremental, not larger, conceptual moves; concept rate rose | measured (N = 1 team) |
| [christensen-schunn-analogical-distance-2007]{406} | One professional team | 55% within / 45% between domain; between-domain analogies mainly explained, within-domain mainly identified problems | measured (N = 1 team) |
| [srinivasan-stimuli-ideation-iced-2017]{408} | 105 students, 226 concepts, a week | "no significant correlations" between proximity and novelty or quality | measured |
| [srinivasan-analogical-distance-ideation-2018]{409} | Same dataset | Abstract: novelty rises and quality falls with distance; nearer classes used more | measured (abstract only read) |
| [keshwani-casakin-bio-vs-engineering-analogies-2024]{410} | 26 student teams | Biological > within-domain on novelty; biological ≈ cross-domain; biological chosen most | measured |
| [franke-poetz-schreier-analogous-markets-2014]{402} | 213 solvers, 3 markets | Novelty up, immediate usefulness down | measured |
| [jeppesen-lakhani-marginality-broadcast-search-2010]{400} | 166 contests | Small positive association with winning (p < .10) | measured (observational, self-selected) |
| [acar-van-den-ende-knowledge-distance-2016]{401} | 218 solutions | No main effect; depends on effort × search variation | measured (observational) |
| [hope-analogy-mining-purpose-mechanism-2017]{414} | 38 workers | Diverse-but-relevant beats relevant-homogeneous and random | measured |

The same-field review reads the record as "good support" for a band "neither too near nor too far",
while noting that "research has only offered general suggestions for what this distance is"
[vasconcelos-crilly-inspiration-fixation-2016]{418}. Fu et al. say their sweet spot "is dependent upon and
specific to the patents and design problem" [fu-near-far-analogy-2013]{404}. A survey of data-driven DbA
records distance as the most-studied factor and summarises the trade-off as more novelty with fewer ideas
and lower quality at greater distance [jiang-data-driven-design-by-analogy-2021]{421}.

## 4. Failure modes and limits

- **Too-far sources produce unusable or shallow inferences.** Far stimuli were judged less relevant and
  lowered quality [fu-near-far-analogy-2013]{404}; Chan, Dow and Schunn note far sources may require sifting
  "many samples of far sources to find 'hidden gems'" [chan-dow-schunn-distant-inspiration-2015]{405}.
  Engineers preferred biological analogies yet mapped cross-domain engineering ones more effectively
  [keshwani-casakin-bio-vs-engineering-analogies-2024]{410}. LLM analogical concepts in a team setting
  scored high on novelty but low on feasibility (Zhu et al., as reported)
  [ding-llm-cross-domain-analogies-2023]{420}.
- **Random sampling is not analogous search.** Fu et al. say their findings "directly challenge the random
  inspiration methods" [fu-near-far-analogy-2013]{404}; random inspirations gave diversity "but not
  relevance" [hope-analogy-mining-purpose-mechanism-2017]{414}.
- **Keyword/surface retrieval returns the home domain.** TF-IDF inspirations were "relevant, but also likely
  to be redundant and homogeneous" [hope-analogy-mining-purpose-mechanism-2017]{414}; embeddings, LSI and LDA
  "excel at detecting surface similarity" but miss relational similarity [kittur-scaling-analogical-innovation-2019]{415}.
- **Cost.** Far sources cost about one concept in timed ideation
  [chan-fu-analogy-distance-commonness-2011]{403}; Fu et al. attribute a null effect on quantity to the
  cognitive load of abstracting and transferring [fu-functional-analogy-search-2015]{413}.
- **Timing.** Distant stimuli helped more after work had begun, near ones before (Tseng et al., as reported)
  [vasconcelos-crilly-inspiration-fixation-2016]{418}.
- **More examples are not more coverage.** More examples did not raise the number of distant analogies
  (Dahl & Moreau, as reported) and several examples may further inhibit creativity (Sio et al., as reported)
  [vasconcelos-crilly-inspiration-fixation-2016]{418}.
- **Selection and self-report in field data.** Contest findings depend on solver self-selection — "those that
  assessed themselves to be very 'far' may never have participated" — and on seekers that may prefer
  out-of-field solutions after failing internally [jeppesen-lakhani-marginality-broadcast-search-2010]{400};
  distance there is self-reported [acar-van-den-ende-knowledge-distance-2016]{401}.
- **Evaluation and benchmarks are thin.** Few data-driven DbA studies evaluate generated ideas, and the lack
  of gold-standard benchmarks "makes it impossible to directly compare different DbA methods"
  [jiang-data-driven-design-by-analogy-2021]{421}. A researcher's a priori usefulness judgments of LLM
  analogies did not correlate with users' in-task helpfulness ratings (r = −0.03, p = 0.69)
  [ding-llm-cross-domain-analogies-2023]{420}.
- **Lab validity.** Fixation and inspiration studies typically use students, about an hour or less, simple
  problems and researcher-rated sketches [vasconcelos-crilly-inspiration-fixation-2016]{418}
  [crilly-cardoso-fixation-2017]{419}.

## Disconfirming analysis

Searched for evidence against each load-bearing claim before stating it:

- *Distant sources yield more novel approaches.* Disconfirming evidence found and reported: lower novelty
  and quality for far stimuli [fu-near-far-analogy-2013]{404}; inverse relation with expert shortlisting
  across 12 challenges [chan-dow-schunn-distant-inspiration-2015]{405}; a null correlation
  [srinivasan-stimuli-ideation-iced-2017]{408}; no main effect of solver distance
  [acar-van-den-ende-knowledge-distance-2016]{401}; far analogies followed by smaller, not larger, conceptual
  moves [chan-schunn-far-analogy-in-vivo-2014]{407}. Even the positive Chan et al. study found neither
  near nor far examples beat the no-example control on novelty [chan-fu-analogy-distance-commonness-2011]{403}.
  The claim is therefore stated only as study-specific, not general.
- *Abstraction improves far retrieval.* Searched for nulls: abstraction devices applied to a single analog
  failed [gick-holyoak-schema-induction-1983]{416}; only one of three functional query levels raised novelty
  [fu-functional-analogy-search-2015]{413}; over-abstraction lowers fit
  [vasconcelos-crilly-inspiration-fixation-2016]{418}. Positive results for schema pipelines are the
  authors' summaries of their own studies, with unreported failures acknowledged
  [kittur-scaling-analogical-innovation-2019]{415}. Supported only in the qualified form "abstraction at a
  suitable level, or derived by comparing several analogs".
- *Fixation explains variations-of-one.* Fixation errors "might be quite rare", feature repetition can save
  time, and narrow deep exploration "might save time" [crilly-cardoso-fixation-2017]{419}; Sio et al. suggest
  fixation may restrict variety while improving quality and novelty (as reported)
  [vasconcelos-crilly-inspiration-fixation-2016]{418}. Chan, Dow and Schunn propose iterative deep search
  near the problem as a route to good ideas [chan-dow-schunn-distant-inspiration-2015]{405}. Fixation is
  therefore treated as one measured cause of narrowed breadth, not as evidence that narrow search is worse.
- *Broadcast search finds different approach families.* The four-mechanism challenge is a single
  illustration; the quantitative distance effect is small and marginal
  [jeppesen-lakhani-marginality-broadcast-search-2010]{400}. No source measured approach-family coverage
  of a contest's submissions.
- *LLM analogies help.* No no-analogy control and one researcher's a priori ratings
  [ding-llm-cross-domain-analogies-2023]{420}; stated as demonstrated helpfulness, not measured gain.

## Contradictions

- **Far sources and novelty** — `contradicts` within a shared frame (same problem, same lab group):
  [chan-fu-analogy-distance-commonness-2011]{403} found far-field examples raised mean and maximum novelty
  vs near; [fu-near-far-analogy-2013]{404} found far stimuli lowered maximum novelty vs near and control.
  Fu et al. reconcile the two by mapping both stimulus sets onto one similarity structure (the 2011 "far"
  lay nearer than the 2013 "near"); that reconciliation is theirs and post hoc.
- **Distance and creative outcome in field data** — `tension`: [franke-poetz-schreier-analogous-markets-2014]{402}
  reports higher novelty from analogous-market solvers; [chan-dow-schunn-distant-inspiration-2015]{405}
  reports an inverse relation between source distance and shortlisting. The outcome constructs differ
  (expert-rated novelty vs shortlisting combining novelty and quality); Chan, Dow and Schunn name this
  difference themselves.
- **Same dataset, different conclusions** — `contradicts`: [srinivasan-stimuli-ideation-iced-2017]{408}
  reports "no significant correlations" between stimulus proximity and novelty or quality;
  [srinivasan-analogical-distance-ideation-2018]{409} (abstract) reports novelty rising and quality falling
  with distance. The analyses were not compared at full text {ambiguous: srinivasan-analogical-distance-ideation-2018 full text not read}.
- **Solver distance** — `qualifies`: [jeppesen-lakhani-marginality-broadcast-search-2010]{400} finds a positive
  association; [acar-van-den-ende-knowledge-distance-2016]{401}, using the same distance scale on the same
  platform, finds no main effect and a sign that depends on search effort and variation.
- **Designers' choice of far sources** — `tension`: [keshwani-casakin-bio-vs-engineering-analogies-2024]{410}
  found designers chose biological (farthest) analogies most and says this contradicts Ward's
  path-of-least-resistance; [christensen-schunn-analogical-distance-2007]{406} and
  [srinivasan-analogical-distance-ideation-2018]{409} report nearer sources used as much or more.

## Transfer-relevant observations

Stated in the field's own terms; no project recommendations.

- The field separates **retrieval** (finding a distant source) from **mapping** (making it work). Retrieval
  is where measured gains concentrate (abstraction, comparison of analogs, purpose–mechanism search);
  mapping is where distance costs appear (relevance, quality, feasibility) {inferred: convergence}.
- Distance is relative to the stimulus pool and problem, so "near" and "far" are not portable labels
  [fu-near-far-analogy-2013]{404}; studies operationalise it differently (patent-network proximity, LDA
  cosine, self-report, market identity).
- Two retrieval designs embed an explicit diversity criterion: dispersion over mechanism within a fixed
  purpose [hope-analogy-mining-purpose-mechanism-2017]{414}, and a staged step that asks searchers to name types of
  experts who might bring useful perspectives before any search [kittur-scaling-analogical-innovation-2019]{415}.
- Separating the person who abstracts the problem from the person who searches is advocated as a fixation
  guard [kittur-scaling-analogical-innovation-2019]{415}; WordTree likewise has a second team ideate from
  re-representations without the original problem [linsey-wordtree-method-2008]{411}.
- Self-assessment of fixation is unreliable [linsey-design-fixation-faculty-2010]{417}, and a priori
  usefulness ratings did not predict in-use helpfulness [ding-llm-cross-domain-analogies-2023]{420}; these
  bear on any step where the generator also judges its own sample.
- Fixation research measures breadth with category counts (energy domains used; functional categories;
  distinct solution types), not with coverage estimates [linsey-design-fixation-faculty-2010]{417}
  [chan-fu-analogy-distance-commonness-2011]{403}. No source in this facet reports a stopping rule or a
  completeness estimate for analogous search {inferred: aggregate}.
- Independent outside solvers in one contest returned different mechanisms for one problem
  [jeppesen-lakhani-marginality-broadcast-search-2010]{400}; in the authors' framing the yield grows with
  each additional solver bringing a different toolkit, which is an argued mechanism, not a measured curve.

## Revisit if

- Full text of the 2018 Srinivasan et al. JMD paper resolves its divergence from the 2017 ICED analysis.
- A replication or meta-analysis estimates the distance–novelty–quality relation across problems with a
  common distance metric (Sio et al. 2015 is a meta-analysis on examples that was not read).
- Controlled studies test LLM- or retrieval-generated analogies against a no-analogy condition for
  approach-family coverage rather than idea ratings.
- Evidence appears on analogous search with expert or professional searchers at realistic time scales.
- A study measures approach-family coverage of open-contest submissions.

## Gaps and acquisition notes

- Jansson & Smith (1991), *Design fixation*, Design Studies 12(1) — closed access; claims about it are cited
  through [crilly-cardoso-fixation-2017]{419} and [vasconcelos-crilly-inspiration-fixation-2016]{418}.
- Sio, Kotovsky & Cagan (2015), meta-analysis of examples in design — named by
  [vasconcelos-crilly-inspiration-fixation-2016]{418} as the quantitative synthesis; not obtained.
- Linsey, Markman & Wood (2012), WordTree controlled study, JMD 134(4) — named on the IDREEM WordTree page
  and cited by [fu-near-far-analogy-2013]{404}; not obtained, so WordTree is rated demonstrated only.
- Srinivasan et al. (2018) JMD full text — abstract only.
- PNAS full text of [kittur-scaling-analogical-innovation-2019]{415} was read via PMC; the underlying studies
  it summarises (Yu et al.) were not read.
