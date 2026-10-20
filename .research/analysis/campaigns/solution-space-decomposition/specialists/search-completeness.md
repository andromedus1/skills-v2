---
title: Search completeness and stopping signals in evidence synthesis
provenance: agent-synthesis
updated: 2026-10-20
summary: Evidence-synthesis and qualitative-research methods for deciding when a set of retrieved items is complete enough to stop. Covers multi-strategy search, citation chasing, known-item and relative-recall benchmarks, capture-recapture, statistical stopping for screening, and saturation. Most rules are advocated rather than validated, several measurably fail, and most completeness estimators depend on overlap between independent passes.
key_findings:
  - Reporting standards (PRISMA-S) cover how complete the search report is, not how complete the retrieved set is; the main guidance says objective stopping is hard and little evaluated.
  - Supplementary strategies (snowballing, citation tracking, expert contact, specialist sources) often find items that database search missed, but the added yield varies widely with topic, and the evidence comes mostly from weak designs.
  - Relative recall and known-item checks only measure against what the combined passes already found. They can look high even when true recall is low.
  - Capture-recapture gives a number-missed estimate from overlap between passes. It assumes independent passes, and estimates swing with model choice; under heterogeneity Chao's estimator is a lower bound.
  - In screening, stopping after N consecutive irrelevant items or at a baseline rate missed the 95% recall target in about 39% of runs. Hypothesis-test criteria achieved their stated confidence at a cost in extra screening.
  - Saturation is a judgement about unobserved items. Measured stopping points still leave a fraction of eventual themes unseen, and code-level saturation arrives before meaning-level saturation.
---

# Search completeness and stopping signals in evidence synthesis

## Scope and engagement depth

This brief covers methods from systematic review, information retrieval for evidence synthesis, technology-assisted review (TAR) and qualitative research. These methods are used to (a) widen a search beyond one retrieval route and (b) judge whether the retrieved set is complete enough to stop. It records what signal each method reports, what that signal assumes, and how strong the evidence is. Evidence levels are marked as **designed/advocated** (proposed or recommended, not tested against truth), **demonstrated** (applied to cases, without ground truth or with weak designs) or **measured** (performance quantified against a known or reconstructed truth).

Engagement depth varies. Full texts were read for PRISMA-S, the Cochrane Handbook chapter, both Cooper/Booth guidance reviews, Hirt et al., Bramer et al., Sampson et al., Hausner et al., Kastner 2007, Bron et al., both Callaghan papers, Saunders et al. and Guest et al. Several sources were read at abstract level only, and their attestations say so: Greenhalgh and Peacock, Ogilvie et al., Horsley et al., Kastner 2009, Stelfox et al., Rücker et al., Hennink and Kaiser, Francis et al., Malterud et al. and Cooper's metrics review. Hennink et al. 2017 was read as its abstract plus a summarising fetch of the body. {confidence: abstract-level for those sources}

## Methods and the completeness signal each reports

### 1. Reporting the search process (no completeness estimate)

PRISMA-S has 16 items: databases, registries, browsing, citation searching, contacts, other methods, full strategies, limits, filters, prior work, updates, dates, peer review, total records and deduplication. Its stated aim is to verify that "each component of a search is completely reported and therefore reproducible" [prisma-s-rethlefsen-2021]{150}. It contains no item for estimating how complete the retrieved set is, and the words "saturation" and "stop" do not appear in it [prisma-s-rethlefsen-2021]{150}. It does require declaring non-reproducible methods "even if it may not be fully replicable", plus per-source record counts, so readers can see which sources contributed [prisma-s-rethlefsen-2021]{150}. *Evidence level: designed (Delphi consensus); it governs reporting, not effectiveness.*

A review of nine guidance documents found that only one gave guidance on when to stop searching [cooper-search-process-guidance-2018]{152}. A systematic review of 50 search-effectiveness studies found six metrics (sensitivity, specificity, precision, accuracy, number needed to read, yield) and one method (capture-recapture), with "no consensus on appropriate use" [cooper-search-effectiveness-metrics-2018]{153}.

### 2. Multi-strategy search (generating candidates from different retrieval routes)

Cochrane makes it mandatory to "capture as many studies as possible" and rates searching other reviews and grey literature as highly desirable [cochrane-handbook-ch4-searching-2025]{151}. The evidence on why one route is not enough is measured, but it mostly comes from single reviews:

- Across 58 reviews, 16% of included references were found in only one database. A four-database combination reached 98.3% overall recall, measured against the reviews' own included references. The authors estimate that 60% of published reviews do not retrieve 95% of available relevant references [bramer-database-combinations-2017]{162}.
- In one review of complex evidence, 30% of 495 sources came from the protocol-defined search, 51% from snowballing and 24% from personal knowledge or contacts [greenhalgh-peacock-snowball-audit-2005]{156}.
- In one review of a social intervention, only 4 of 69 relevant studies were in a first-line health database. About half came from a specialist transport database, and seven were found by chance [ogilvie-finding-evidence-2005]{157}.

Booth separates two strategies. Adding more databases is "to search for more of the same". Purposive diversification moves "to different, more productive lines of inquiry", for example by seeking negative or disconfirming cases and maximum variation [booth-qes-searching-2016]{155}. *Evidence level for the diversification moves: advocated.*

### 3. Citation chasing (backward, forward, iterated snowballing)

Backward tracking follows a seed's references. Forward tracking follows papers that cite it. Iterations reuse newly found items as seeds [hirt-citation-tracking-scoping-2022]{158}. Of 45 studies that assessed benefit, 43 found added value. The authors themselves warn that this ratio is inflated by publication bias. Most studies ran only one round [hirt-citation-tracking-scoping-2022]{158}. A Cochrane methodology review found added yield ranging from 2.5% to 42.7%, from studies "at high risk of bias". Its conclusion is that the hard part is recognising which situations need the method [horsley-reference-list-checking-2011]{159}. Reported cases of no added value include forward citation tracking on 40 included papers that found one new eligible paper [hirt-citation-tracking-scoping-2022]{158}.

In software engineering, a hybrid design (database start set, then iterated backward and forward snowballing) found 43 studies against 33 in the original review. Snowballing performance is "highly dependent on the start set", and a round with few articles risks the procedure stopping early [wohlin-hybrid-search-snowballing-2022]{160}. *Evidence level: demonstrated, in single replications or weak comparative designs.*

### 4. Benchmark checks: known items, relative recall, quasi-gold standards

- **Known-item check.** Test whether the search finds key publications or studies included in similar reviews. Cochrane warns: "It is not enough ... for the strategy to find only those records", because that may show "the strategy is biased towards known studies". The more informative signal comes when citation searching or reference checking finds items the search had already retrieved "but that the team did not necessarily know about in advance" [cochrane-handbook-ch4-searching-2025]{151}. *Advocated.*
- **Relative recall.** The share of the pooled relevant set from all routes that one route retrieves [sampson-relative-recall-2006]{163}. Across 105 Cochrane reviews it produced filter recall figures of 0.91–0.98, consistent with earlier hand-search benchmarks. Its stated ceiling: it "is only as good as the sum of the individual searches", and "The relative recall of one system may be high, yet the actual recall could be close to zero" [sampson-relative-recall-2006]{163}. Bramer et al.'s recall figures use this pooled denominator and leave out items found by non-database methods [bramer-database-combinations-2017]{162}. *Measured, but only against a pooled denominator.*
- **Held-out quasi-gold standard.** Items included in prior reviews are split two-thirds for building the strategy and one-third for validating it, and the strategy must retrieve the held-out set [hausner-objective-search-strategy-2012]{164}. In the worked example, the 13-item validation set "was also completely identified" [hausner-objective-search-strategy-2012]{164}. *Demonstrated on one example.*

### 5. Capture-recapture (estimating how many items are missing)

Each retrieval route is treated as a capture occasion. The pattern of overlap among routes is used to estimate how many items no route found. Cochrane notes that this needs at least two searches. It describes Kastner's iterative search-estimate-decide approach as warranting further investigation [cochrane-handbook-ch4-searching-2025]{151}.

- Kastner et al. treated four databases as captures and fitted log-linear (Poisson) models. They estimated 1,838 articles (95% CI 1,749–1,955), of which 1,246 had been found (68%). The proposed rule is to stop once the known count falls within the estimate's confidence interval. The method rests on "k independent samples", the authors call for "cutpoints" that have not yet been defined, and they flag the result as needing caution [kastner-cmr-horizon-2007]{165}. At full-text level the same four databases provided 81% of the estimated total [kastner-cmr-stopping-rule-2009]{166}.
- A surgical review estimated 3 missed articles (95% CI 0–6), with the database search providing 93% [stelfox-cmr-surgery-2013]{167}.
- Model choice is a known weak point. On two reviews, manually selected models estimated 82 and 140 missing articles. Automatically selected models estimated 127 and 188 (95% CIs 52–128 vs 86–186, and 116–168 vs 159–223). The authors attribute the instability to "variable selection and overfitting" [rucker-boosting-capture-recapture-2011]{168}.
- Chao's estimator uses only items found once (f1) and items found twice (f2). Many singletons relative to doubletons indicate many items are still unseen. When capture probabilities vary across items, it "provides a lower bound". "Contagion", where one capture changes the chance of the next, violates its assumptions [bron-chao-estimator-tar-2024]{169}. Bron et al. attribute to Webster and Kemp (2013) a design in which "multiple reviewers conduct independent searches" so that their overlaps can feed this estimate [bron-chao-estimator-tar-2024]{169}. In TAR simulations, point-estimate ("optimistic") criteria tended to underestimate the number of relevant documents [bron-chao-estimator-tar-2024]{169}.

*Evidence level: demonstrated in single-review applications with no external truth (Kastner, Stelfox). Measured in simulation for TAR (Bron). Sensitivity to model choice is measured (Rücker).*

### 6. Statistical stopping rules for screening (TAR)

Bron et al. divide stopping rules into **heuristic** rules, which "do not offer strong guarantees besides the results of the criterion on known datasets", and **certification** rules, which carry a formal statistical guarantee [bron-chao-estimator-tar-2024]{169}. They attribute two methods to Cormack and Grossman (2016). The *Target* method randomly samples until 10 relevant items are found, then stops once all 10 are rediscovered, and claims at least 70% recall. The *Knee* method stops at a slope change in the recall curve [bron-chao-estimator-tar-2024]{169}.

Measured failures of heuristic rules:

- Stopping at a baseline inclusion rate missed the 95% recall target in 39.67% of runs, and the most common work saving was 0% [callaghan-statistical-stopping-2020]{170}.
- Stopping after 50 consecutive irrelevant items missed it in 39% of runs [callaghan-statistical-stopping-2020]{170}. In another evaluation the 5th-percentile recall of that rule was as low as 53% [callaghan-stopping-recommendations-2024]{171}.
- The underlying reason given: recall depends on how many unseen items remain, not only on the relevant rate among them. "Even a perfect estimator of the proportion of unseen documents that are relevant is insufficient on its own" [callaghan-statistical-stopping-2020]{170}.

The proposed alternative samples the unseen remainder and tests the null hypothesis "recall < target" with a hypergeometric test. Ranked quasi-sampling missed the target in 0.95% of runs and saved 17% of work [callaghan-statistical-stopping-2020]{170}. The 2024 consensus asks for several things [callaghan-stopping-recommendations-2024]{171}:

- reporting whether a recall target and confidence level were pre-set
- reporting "confidence levels across a range of recall targets"
- reporting the recall implications even when stopping for pragmatic reasons
- accepting that "any reliable stopping criteria will require that more records are screened than the minimum"

*Evidence level: measured on benchmark datasets. The 2024 paper notes that reliability in simulation "may ... be dependent on the specific experimental setup, or even be achieved by over-optimising" [callaghan-stopping-recommendations-2024]{171}.*

### 7. Saturation (qualitative research and qualitative evidence synthesis)

Saturation stops when "further data collection and/or analysis are unnecessary". It has at least four forms: theoretical, inductive thematic, a priori thematic and data saturation, each saturating something different [saunders-saturation-models-2018]{172}. As Saunders et al. quote, Glaser and Strauss's original form deliberately seeks "groups that stretch diversity of data as far as possible" before declaring saturation [saunders-saturation-models-2018]{172}. Operational versions:

- **Fixed-run rule.** Take an initial sample of 10, then stop after 3 consecutive interviews with no new ideas. In one demonstration the criterion was met for one belief category but not study-wide [francis-data-saturation-2010]{176}.
- **Base / run / threshold metric.** New themes found in a run of 2–3 interviews, divided by the themes in a base of 4–6, against a ≤5% or 0% threshold [guest-thematic-saturation-method-2020]{173}. It does not assume a random sample. The authors state "there is no guarantee that saturation is in fact reached when meeting these thresholds". At the typical stopping point of 6–7 interviews, the median coverage of the full dataset's themes was 78–82% [guest-thematic-saturation-method-2020]{173}.
- **Code versus meaning saturation.** Code saturation came at 9 interviews; meaning saturation needed 16–24 ("heard it all" versus "understand it all") [hennink-code-meaning-saturation-2017]{174}. A systematic review of 23 empirical tests found saturation within 9–17 interviews, mostly in homogeneous samples testing code saturation. Outliers such as multi-country studies and meaning saturation needed more [hennink-kaiser-saturation-review-2022]{175}.
- **Information power.** This replaces saturation with a sample-adequacy judgement based on aim, specificity, theory, dialogue quality and analysis strategy [malterud-information-power-2016]{177}. *Advocated.*
- **In evidence synthesis.** Searching stops when late-found studies "did not add anything new". A "more mechanical" signal is when references to the same studies keep reappearing. The open question remains: "how can a reviewer know that an additional study will not add important insights?" [booth-qes-searching-2016]{155}. Cochrane accepts saturation-based justifications for qualitative evidence [cochrane-handbook-ch4-searching-2025]{151}.

*Evidence level: the saturation metrics are measured retrospectively against the full collected dataset. That dataset is itself a sample, so the 78–82% figure is coverage of observed themes, not of all themes that exist.* {inferred: qualifies}

### Summary table

| Method | Completeness signal reported | Key assumption or limit | Evidence level |
| --- | --- | --- | --- |
| PRISMA-S reporting | Completeness of the search *report* | Says nothing about set completeness [prisma-s-rethlefsen-2021]{150} | Designed |
| Multiple databases | Unique-per-source counts; recall against included set | Denominator is the review's own included set [bramer-database-combinations-2017]{162} | Measured (relative) |
| Citation chasing | Added yield beyond database search | Context-dependent; publication bias in the evidence [hirt-citation-tracking-scoping-2022]{158}; weak designs [horsley-reference-list-checking-2011]{159} | Demonstrated |
| Known-item check | Share of known key items retrieved | Biased toward what is already known [cochrane-handbook-ch4-searching-2025]{151} | Advocated |
| Relative recall | Route's share of the pooled set | Capped by the union of routes [sampson-relative-recall-2006]{163} | Measured (relative) |
| Held-out validation set | Recall on held-out known items | Needs prior comprehensive reviews [hausner-objective-search-strategy-2012]{164} | Demonstrated |
| Capture-recapture | Estimated number missing, with CI | Independence; model choice [kastner-cmr-horizon-2007]{165} [rucker-boosting-capture-recapture-2011]{168} | Demonstrated / measured sensitivity |
| Chao lower bound | Estimate from f1/f2 counts | Lower bound under heterogeneity; no contagion [bron-chao-estimator-tar-2024]{169} | Measured in simulation |
| Hypergeometric stopping test | "Recall ≥ target at confidence level" | Random sample of the unseen remainder [callaghan-statistical-stopping-2020]{170} | Measured |
| Consecutive-miss and baseline heuristics | "No new items in N" | Ignores the size of the remainder [callaghan-statistical-stopping-2020]{170} | Measured (often fails) |
| Thematic saturation metric | % new themes per run relative to base | No guarantee; order effects [guest-thematic-saturation-method-2020]{173} | Measured retrospectively |

## Failure modes and limits

- **Illusory saturation, denominator artefact.** Metrics whose denominator is the full collected dataset "eventually" reach 100% by construction [guest-thematic-saturation-method-2020]{173}. Saturation is "a statement about the unobserved based on the observed", and for disconfirming cases a statement "about the unobserved based on the unobserved" [saunders-saturation-models-2018]{172}.
- **Illusory saturation, level of analysis.** Counting codes saturates earlier than understanding their dimensions [hennink-code-meaning-saturation-2017]{174}. Saunders et al. note that saturation produced by one's own coding cannot independently validate that coding [saunders-saturation-models-2018]{172}.
- **Homogeneity dependence.** Small saturation sample sizes come from homogeneous samples with narrow objectives; heterogeneous designs needed more [hennink-kaiser-saturation-review-2022]{175} [guest-thematic-saturation-method-2020]{173}.
- **Benchmark circularity.** Known-item and relative-recall checks cannot detect items that every route missed [cochrane-handbook-ch4-searching-2025]{151} [sampson-relative-recall-2006]{163}.
- **Dependence between sources and model choice.** Capture-recapture depends on "independent samples" [kastner-cmr-horizon-2007]{165}. Dependence handled through interaction terms makes estimates vary "markedly" [rucker-boosting-capture-recapture-2011]{168}. Heterogeneous catchability turns Chao's estimator into a lower bound [bron-chao-estimator-tar-2024]{169}. Database searches built from one shared strategy are not obviously independent captures. {inferred: extends — no attested source tests that specific dependence}
- **Start-set dependence.** Snowballing yield depends on the seeds and can stop early after a thin round [wohlin-hybrid-search-snowballing-2022]{160}.
- **Judgement disagreement inflating apparent gaps.** In the software-engineering replication, original-only items included ones excluded on scope or quality grounds, not only search misses [wohlin-hybrid-search-snowballing-2022]{160}. Two mapping studies of the same topic differed considerably in included papers and classification [wohlin-mapping-reliability-2013]{161}.
- **Overfitting of stopping rules to benchmark datasets** [callaghan-stopping-recommendations-2024]{171}.

## Disconfirming analysis

- *Claim: supplementary search methods improve coverage.* Disconfirming evidence was sought and found. Westphal et al. and Wright et al. found little or no added value from citation tracking [hirt-citation-tracking-scoping-2022]{158}. Ogilvie et al. found that experts contributed information rather than additional studies [ogilvie-finding-evidence-2005]{157}. Horsley et al. rated the supporting designs as high risk of bias [horsley-reference-list-checking-2011]{159}. The claim holds only as context-dependent: complex, interdisciplinary or poorly indexed topics benefit most [hirt-citation-tracking-scoping-2022]{158}.
- *Claim: capture-recapture can serve as a stopping rule.* The original authors state that cutpoints are undefined and evaluation was retrospective [kastner-cmr-horizon-2007]{165} [kastner-cmr-stopping-rule-2009]{166}. Rücker et al. show estimates that depend heavily on the model [rucker-boosting-capture-recapture-2011]{168}. None of the attested applications compares the estimate with an independently established true total. {inferred: aggregate} The claim stands as **demonstrated, not validated**.
- *Claim: "no new items for N steps" signals completeness.* In TAR this is directly disconfirmed (39% target misses; 53% 5th-percentile recall) [callaghan-statistical-stopping-2020]{170} [callaghan-stopping-recommendations-2024]{171}. In qualitative work, the stopping point left 18–22% of the observed dataset's themes unseen [guest-thematic-saturation-method-2020]{173}. The Francis et al. demonstration did not reach study-wide saturation [francis-data-saturation-2010]{176}.
- *Claim: certification-style rules are reliable.* Their performance is measured only on benchmark collections. The 2024 consensus warns that setup-dependent results may not generalise [callaghan-stopping-recommendations-2024]{171}. Chao-based rules underperformed AUTOSTOP on reliability at high targets [bron-chao-estimator-tar-2024]{169}.
- *Claim: comprehensive searching is the quality marker.* Contested by guidance reviews that say comprehensiveness is "not necessarily a marker of literature search quality" [cooper-search-process-guidance-2018]{152}, and by purposive and theoretical sampling traditions [booth-qes-searching-2016]{155}.

## Contradictions

| Relationship | Positions retained |
| --- | --- |
| tension | Strong yield from snowballing and contacts in complex reviews [greenhalgh-peacock-snowball-audit-2005]{156} versus near-zero added value from citation tracking in two intervention reviews (chronic depression trials; multiple risk-behaviour interventions) [hirt-citation-tracking-scoping-2022]{158}. The field's own reading is that this depends on context, and Horsley et al. say the situations are hard to recognise in advance [horsley-reference-list-checking-2011]{159}. |
| tension | Capture-recapture presented as usable for judging closeness to the total [kastner-cmr-stopping-rule-2009]{166} [stelfox-cmr-surgery-2013]{167} versus manual model selection giving "large estimates, varying markedly" [rucker-boosting-capture-recapture-2011]{168}. |
| incommensurable | Saturation sample sizes of 6–7 [guest-thematic-saturation-method-2020]{173}, 9–17 [hennink-kaiser-saturation-review-2022]{175} and 16–24 for meaning [hennink-code-meaning-saturation-2017]{174} measure different things (relative new-theme rate, code saturation, meaning saturation) and are not stated in a shared frame. |
| incommensurable | The mandatory "as many studies as possible" standard [cochrane-handbook-ch4-searching-2025]{151} versus purposive or theoretical sampling to saturation, with explicit justification for stopping [booth-qes-searching-2016]{155}. They answer different review purposes (aggregative versus interpretive). |
| qualifies | Bron et al. report that their estimators "work well" in simulation [bron-chao-estimator-tar-2024]{169}; Callaghan et al. 2024 qualify simulation-based reliability claims in general [callaghan-stopping-recommendations-2024]{171}. |

## Transfer-relevant observations

Stated in the source fields' own terms. These are not recommendations.

- The fields keep **process-completeness reporting** (what routes were used, declared even when not reproducible) separate from **set-completeness estimation** (missing-count estimates, recall certification) [prisma-s-rethlefsen-2021]{150} [callaghan-stopping-recommendations-2024]{171}.
- The set-completeness estimators attested in this facet need either **at least two overlapping retrieval passes** (capture–recapture) or a **random sample of the unseen remainder** (statistical stopping tests); a single search pass gives no overlap signal for capture–recapture [cochrane-handbook-ch4-searching-2025]{151} [callaghan-statistical-stopping-2020]{170}. Abundance-based richness estimators in other fields use frequency counts from one sample instead (coverage-estimation facet). {inferred: convergence, scoped to this facet's estimators}
- Overlap-based estimators read the **frequency of items found by exactly one pass versus two** (f1/f2) and assume passes behave like independent captures [bron-chao-estimator-tar-2024]{169}. Webster and Kemp's design, as Bron et al. describe it, uses independent searchers as the passes [bron-chao-estimator-tar-2024]{169}.
- Benchmark checks guard against circularity by using a **held-out** known set [hausner-objective-search-strategy-2012]{164}. A second route that re-finds already retrieved items the team did not know about beforehand counts as a positive signal; re-finding only known items does not [cochrane-handbook-ch4-searching-2025]{151}.
- In qualitative synthesis, completeness of a **sample of kinds** is judged by diversification moves (maximum variation, disconfirming or negative cases, different research traditions) rather than by adding more of the same source [booth-qes-searching-2016]{155} [saunders-saturation-models-2018]{172}.
- Saturation reports in their more disciplined forms state the base, run and threshold (for example "6+2" at ≤5%) and say explicitly that this is no guarantee [guest-thematic-saturation-method-2020]{173}. Certification-style reports give confidence across a range of recall targets rather than one yes/no verdict [callaghan-stopping-recommendations-2024]{171}.
- Disagreement between independent passes comes partly from **inclusion judgement**, not only from retrieval [wohlin-hybrid-search-snowballing-2022]{160} [wohlin-mapping-reliability-2013]{161}. Applied to the replication's peer-reviewed counts (22 and 43, with 20 in common), a two-sample Lincoln-Petersen calculation gives about 47 against an observed union of 45. That calculation is valid only if the two teams applied the same inclusion boundary and searched independently, and the source shows they did not fully share a boundary. {inferred: aggregate — illustrative arithmetic, not reported by the source}

## Revisit if

- A prospective validation compares capture-recapture or Chao-type estimates against an independently established true total for literature searches.
- Delphi-based citation-tracking recommendations announced by Hirt et al. are published.
- Guideline bodies (Cochrane, PRISMA) adopt a reporting item or minimum standard for search-completeness or stopping statements.
- Saturation metrics are validated on samples of *categories of approach* or other non-interview units, or on heterogeneous populations.
- Evaluations of TAR stopping rules across new datasets show certification rules failing their stated confidence.

## Revisions

- **2026-10-20 — correction (lead, after adversarial-read).** The two-pass requirement is scoped to capture–recapture and stopping tests rather than to every estimator.
