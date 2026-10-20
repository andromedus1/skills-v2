---
title: LLM ideation diversity — homogenization, mode collapse, recall limits, diversity-raising techniques and how coverage is measured
provenance: agent-synthesis
updated: 2026-10-20
campaign: solution-space-decomposition
facet: llm-ideation-diversity
summary: >
  Within-specialist brief. Measured evidence that LLM-generated or LLM-assisted idea pools are less
  diverse than independent human pools, chiefly at the collective/across-sample level and across
  model families; alignment-linked mode collapse; recall (not encoding) limits on long-tail items;
  and an authoring-versus-judging asymmetry in which omissions resist review. Techniques with
  measured diversity gains (multi-step "generate then make different" chain-of-thought, ordinary
  personas, verbalized sampling, in-context regeneration, explicit dimension/approach elicitation,
  lens-anchored multi-agent setups) are separated from advocated or qualitatively evaluated ones,
  and null/negative results (seeding, similarity feedback, hybrid select, temperature, standard
  debate, celebrity personas, creativity system prompts) are reported. Diversity/coverage metrics
  (embedding dispersion, dedup-threshold unique counts, capture-recapture estimates, exhaustion
  curves, category-combination counts, learned equivalence classes, human ratings) and their
  validity limits are catalogued.
---

# LLM ideation diversity

## Scope and evidence key

This brief covers evidence on large language models (LLMs) generating alternative ideas or
approaches: how much diversity they produce, why it is limited, which interventions change it,
and how diversity and coverage are measured. Evidence levels used below:

- **measured** — an experiment or benchmark reports a quantitative effect;
- **measured (qualitative)** — user-study perceptions or interviews only;
- **designed/advocated** — a method is proposed or argued for without a reported effect on diversity or coverage;
- **null/negative** — a tested intervention produced no gain or a loss.

Most sources are arXiv preprints. Peer-reviewed venues as stated on the fetched pages: Science
Advances [doshi-hauser-genai-collective-diversity-2024]{302}; Creativity & Cognition 2024
[anderson-llm-homogenization-ideation-2024]{303}; ACM Collective Intelligence 2025
[ashkinaze-ai-ideas-collective-diversity-2024]{304}; ICLR 2024 [padmakumar-he-cowriting-diversity-2023]{305};
NeurIPS 2025 Datasets & Benchmarks [artificial-hivemind-homogeneity-2025]{307}; ICML 2023
[kandpal-long-tail-knowledge-2022]{319}; EMNLP 2024 [liang-multi-agent-debate-divergent-2023]{316};
EMNLP Findings 2025 [kambhatla-persona-lexical-diversity-2025]{313}; AACL 2025
[shaib-text-diversity-measurement-2024]{322}; Nature Human Behaviour, read only through an
institute summary page [meincke-chatgpt-brainstorm-diversity-2025]{301} `{confidence: snippet-thin}`.
Several sources were engaged at abstract depth only; their attestations record this
(`substrate_confidence: search-summary`) and claims resting on them are marked.

## 1. The phenomenon: LLM idea pools are narrower, mostly at the collective level

**Unassisted LLM pools versus pooled independent humans (measured).** With GPT-4 generating
college-product ideas, mean within-pool cosine similarity ranged from 0.255 to 0.432 across 35
prompting strategies against 0.243 for an aggregated pool of separate students' ideas; the base
prompt scored 0.377 [meincke-prompting-idea-variance-2024]{300}. The authors note their human
pool aggregated independent individuals, which "gives an edge to the human innovators"
[meincke-prompting-idea-variance-2024]{300}. Across 22 LLMs on three standardized divergent-thinking
tests, population-level response variability was far lower for LLMs than humans (e.g., Alternate
Uses 0.459 vs 0.738, effect size 2.2), "even after controlling for response structure", while
individual LLM originality scores were similar to or slightly above humans on two of three tests
[wenger-kenett-creative-homogeneity-llms-2025]{306}. In an LLM research-ideation agent, 4000 seed
ideas per topic yielded only 200 non-duplicates at a 0.8 embedding-similarity threshold, with the
non-duplicate rate falling batch over batch until accumulated unique ideas plateaued
[si-llm-research-ideation-2024]{318}. NoveltyBench reports frontier models producing roughly 1.8–2.9
functionally distinct answers out of 10 samples, fewer than small models in the same families and
fewer than human writers [noveltybench-humanlike-diversity-2025]{310}.

**Cross-model homogeneity (measured).** Responses from different models to the same open-ended
query had average pairwise embedding similarity of 71%–82%, and top response clusters drew on ~8
different models each [artificial-hivemind-homogeneity-2025]{307}. Wenger and Kenett find LLM
responses "much more similar to other LLM responses than human responses are to each other"
[wenger-kenett-creative-homogeneity-llms-2025]{306}. The Artificial Hivemind authors caution that
"model ensembles may not yield true diversity when their constituents share overlapping alignment
and training priors" [artificial-hivemind-homogeneity-2025]{307}.

**Human-with-LLM pools: individual gain, collective narrowing (measured).** Writers given up to five GPT-4
story ideas were rated 8.1% more novel and 9.0% more useful, but their stories were more similar
to each other — "writers are individually better off, but collectively a narrower scope of novel
content is produced" [doshi-hauser-genai-collective-diversity-2024]{302}. ChatGPT users' ideas were
less divergent from the group-average embedding than those of users of an Oblique Strategies card
deck (d = .47), with no difference in within-user diversity and with ChatGPT users covering more
categories individually [anderson-llm-homogenization-ideation-2024]{303}. The Nature Human
Behaviour study is reported as finding significant diversity reduction in 37 of 45 comparisons
across five experiments [meincke-chatgpt-brainstorm-diversity-2025]{301} `{confidence: snippet-thin}`.
Co-writing with InstructGPT, but not base GPT-3, reduced cross-author diversity, attributed to the
model-contributed text [padmakumar-he-cowriting-diversity-2023]{305} `{confidence: search-summary}`.

**Within-session versus across-sample.** Deng, Brucks and Toubia find a single GPT-4o session
explores categories at nearly the same rate as a single human (12.46 vs 12.68 categories over 10
ideas), whereas independent first ideas across sessions cover far fewer categories and
combinations than independent humans (T_comb 5.88 vs 9.17)
[deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}. Anderson et al. likewise find the
effect at group level, not individual level [anderson-llm-homogenization-ideation-2024]{303}.
`{inferred: convergence}` Across these sources the measured shortfall is concentrated in what
repeated, independent LLM draws jointly cover, rather than in how varied one session's own list looks.

## 2. Proposed mechanisms and their evidence level

| Mechanism | Evidence | Level |
|---|---|---|
| Alignment / preference tuning narrows outputs | RLHF reduced per-input and across-input diversity relative to SFT [kirk-rlhf-generalisation-diversity-2023]{308}; each OLMo 2 post-training stage reduced diversity, sharply at DPO [noveltybench-humanlike-diversity-2025]{310}; InstructGPT but not GPT-3 reduced co-writing diversity [padmakumar-he-cowriting-diversity-2023]{305}; base models beat aligned forms on randomness and creative originality [west-potts-base-vs-aligned-creativity-2025]{309} `{confidence: search-summary}` | measured |
| Typicality bias in preference data (annotators favour familiar text) | Bias parameter estimated at 0.57–0.65 on HelpSteer, p < 10^-14 [verbalized-sampling-mode-collapse-2025]{311} | measured (one dataset) + theoretical |
| Fixation — early outputs constrain later ones | Within-session category accumulation slopes; CoT changes the slope in LLMs but not humans [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}; "Degeneration-of-Thought" in self-reflection [liang-multi-agent-debate-divergent-2023]{316} | measured (inferred from slopes / disagreement rates) |
| Knowledge aggregation — one model is one "unified distribution", not a population with partitioned knowledge | Low across-session category coverage; ordinary personas raise between-session spread [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312} | measured (one model, one domain) |
| Recall rather than knowledge limits long-tail coverage | QA accuracy tracks pre-training document count [kandpal-long-tail-knowledge-2022]{319} `{confidence: search-summary}`; frontier models encode 95–98% of benchmark facts but recall of rare facts lags (Gemini-3-Pro 63.3% vs 84.6% for popular facts) [calderon-recall-bottleneck-factuality-2026]{320} | measured (factual QA) |
| Enumeration is weaker than judgment | Same models judge set membership far better than they author the set; the dominant error is omission [judging-not-enumerating-omissions-2026]{321} | measured (predicate sets, test suites, WordNet) |

`extends` The recall and enumeration sources study facts, predicate extensions and test suites, not
approach families; their transfer to enumerating solution approaches is an analogy, not a measured result.

## 3. Techniques that change diversity or coverage

### 3.1 Multi-step "generate many, then make them different" (chain-of-thought)

- Meincke et al.'s CoT prompt — list 100 short titles, then revise them to be "different and bold"
  so "No two ideas should be the same", then describe — gave the lowest similarity of any prompt
  (0.255 vs base 0.377) and a larger estimated unique-idea space (~4700 vs ~3700)
  [meincke-prompting-idea-variance-2024]{300}. **Measured**, with caveats recorded in the source: the CoT
  pool was generated by a different model version (gpt4-1106-preview) than most strategies
  (gpt4-0314), ~15% of runs where the model skipped the revision step were removed, and the CoT
  advantage disappeared after ~750–800 ideas [meincke-prompting-idea-variance-2024]{300}.
- Deng et al. independently report CoT raising LLM category-combination coverage (bootstrap T_comb
  39.15 → 55.49) and reducing fixation, but not restoring across-session knowledge partitioning
  [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}. **Measured**.

### 3.2 Personas

- **Mixed/conditional.** In Meincke et al., celebrity and "creative entrepreneur" personas ranged from
  modest gains (Creative Entrepreneur 0.348, Steve Jobs 0.368 vs base 0.377) to worse-than-base
  variants (e.g., several "Novel Modifier" variants at 0.38–0.41) [meincke-prompting-idea-variance-2024]{300}.
- Deng et al. find ordinary everyday personas outperform "creative entrepreneur" personas (T_comb 56.97
  vs 50.40; human 59.66), acting as "diverse sampling cues" that raise between-session spread 2.6x —
  but they increase within-session fixation; ordinary personas plus CoT produced the highest coverage,
  exceeding humans (aggregate T_comb 248 vs 197) [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}. **Measured**, single model and domain.
- Persona prompting raised lexical diversity of synthetic text, but fine-grained persona detail added
  little beyond specifying a length cutoff [kambhatla-persona-lexical-diversity-2025]{313}
  `{confidence: search-summary}`. **Measured (lexical only)**.
- "More creative" system prompts slightly raised individual LLM creativity but left population-level
  variability far below humans [wenger-kenett-creative-homogeneity-llms-2025]{306}. **Null for population diversity**.

### 3.3 Distribution-level prompting: verbalized sampling and in-context regeneration

- Verbalized sampling asks for k responses with verbalized probabilities (optionally "below
  {threshold}") and reports 1.6–2.1x semantic diversity over direct prompting in creative writing,
  human-rated diversity gains, coverage gains on open-ended QA, and no loss of factual accuracy or
  safety; gains are larger for more capable models [verbalized-sampling-mode-collapse-2025]{311}.
  **Measured by the proposing authors; preprint.** Verbalized probabilities are imperfectly calibrated
  (KL 0.12) [verbalized-sampling-mode-collapse-2025]{311}.
- In-context regeneration — show prior outputs and ask for a different one — was the most effective of
  four strategies on NoveltyBench, reaching human-level distinctness for three frontier models;
  resampling, paraphrased prompts and a "novel answer" system prompt were weaker
  [noveltybench-humanlike-diversity-2025]{310}. **Measured.**
- `{inferred: convergence}` Meincke's CoT, verbalized sampling's "sequence"/list baselines and
  in-context regeneration share one feature: later items are generated with earlier items visible and
  an explicit instruction to differ.

### 3.4 Explicit dimensions and approach elicitation

- **Dimension-structured generation (designed; qualitative evaluation).** Luminate has the LLM propose
  categorical dimensions and values for a prompt, then samples value combinations as generation
  requirements [luminate-design-space-generation-2023]{315}. Its 14-writer study reports perceived
  usefulness and dimension accuracy, but no quantitative measure of diversity or coverage, and the
  authors note "even experts can have difficulties answering the dimensions that characterize the
  problem space" [luminate-design-space-generation-2023]{315}.
- **Dimensions as a measurement frame (measured).** Deng et al. measure diversity by coding ideas on three
  pre-specified dimensions and counting distinct categories and combinations; they note conclusions
  depend on the categorization scheme [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}.
- **Approach elicitation (measured on accuracy, not coverage).** DIV-SE asks the model to name
  approaches (5 per call, 100 calls), keeps the most frequent 3–5, pairs them with model-suggested
  personas, and ensembles them; it beat temperature-sampled self-consistency at equal cost on
  reasoning benchmarks, arguing token-level stochasticity "does not always ensure diverse and
  independent solution approaches" [naik-div-se-diversity-of-thought-2023]{314}. Gains were negligible
  for a weaker open model [naik-div-se-diversity-of-thought-2023]{314}. Selection by frequency keeps the
  most commonly proposed approaches, which is the opposite of seeking long-tail approaches
  [naik-div-se-diversity-of-thought-2023]{314}.

### 3.5 Multiple agents

- Two-sided debate counters "Degeneration-of-Thought" on tasks with correct answers (e.g., 37.0% vs
  27.5% for self-reflection on counter-intuitive arithmetic); moderate rather than maximal
  disagreement worked best, and LLM judges may favour debaters of their own model family
  [liang-multi-agent-debate-divergent-2023]{316}. **Measured (accuracy).**
- **Negative for diversity:** standard multi-agent debate lowered semantic and lexical diversity across
  independent runs below single-agent generation, while judge-based voting over independent responses
  did not — "isolating debate dynamics as the primary driver"; convergence pressure persisted with
  heterogeneous model families [creative-mad-debate-diversity-2026]{317}. Anchoring each agent to a
  persistent distinct "cognitive lens" and restricting each agent's view to its most distant peers
  recovered ~26% semantic diversity with near-parity quality [creative-mad-debate-diversity-2026]{317}.
  **Measured; single preprint.**

### 3.6 Interventions with null or negative measured effects

- Telling GPT-4 the cosine similarity of existing ideas produced the least diverse pool (0.432);
  hybrid "40 sessions then groups pick the best 10" scored 0.393, worse than the base prompt; HBR and
  design-thinking article prompts were also worse than base [meincke-prompting-idea-variance-2024]{300}.
- Seeding LLM sessions with human first ideas "does not improve downstream idea diversity at all"
  [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}.
- Higher temperature gave "only slight improvement ... while often producing nonsensical answers"
  [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}; min-p at temperature 2.0 still left 61.2% of
  response pairs above 0.8 similarity [artificial-hivemind-homogeneity-2025]{307}.
- Meincke et al. state that "prompt crafting does not always have a significant effect"
  [meincke-prompting-idea-variance-2024]{300}.

### 3.7 Thinking/reasoning and retrieval for recall-limited coverage

- Thinking recovered 40–65% of encoded-but-not-directly-recalled facts and helped rare facts more than
  popular ones, but recovered only 5–20% of non-encoded facts [calderon-recall-bottleneck-factuality-2026]{320}.
- Test-time reasoning closed the authoring-judging gap on executable predicates for one model but was
  unreliable on test-suite authoring [judging-not-enumerating-omissions-2026]{321}.
- Retrieval augmentation reduced dependence on pre-training frequency for long-tail QA
  [kandpal-long-tail-knowledge-2022]{319} `{confidence: search-summary}`.

## 4. How diversity and coverage are measured

| Measure | Used by | Known limits stated in sources |
|---|---|---|
| Mean pairwise embedding cosine similarity / dispersion | [meincke-prompting-idea-variance-2024]{300} (Universal Sentence Encoder); [doshi-hauser-genai-collective-diversity-2024]{302}; [artificial-hivemind-homogeneity-2025]{307}; [verbalized-sampling-mode-collapse-2025]{311} | Results can change "dramatically" with the embedding model; link to human-judged similarity unestablished [meincke-prompting-idea-variance-2024]{300}; may lack expressiveness for creative variation [artificial-hivemind-homogeneity-2025]{307}; can overweight paraphrase [noveltybench-humanlike-diversity-2025]{310} |
| Distance from group-centroid embedding (group vs individual) | [anderson-llm-homogenization-ideation-2024]{303} (MiniLM; 61–65% agreement with human categorization) | Moderate agreement with human coding |
| Unique-idea count via similarity threshold (0.8) | [meincke-prompting-idea-variance-2024]{300}; [si-llm-research-ideation-2024]{318} | Threshold set "by testing" / "manual inspection" |
| Capture-recapture-style estimate of total unique ideas | [meincke-prompting-idea-variance-2024]{300}, which attributes the method to Kornish & Ulrich | Estimates only the space reachable "with a particular technique", not the true idea space [meincke-prompting-idea-variance-2024]{300} |
| Exhaustion / saturation curve (similarity of each new idea to all prior; non-duplicate share per batch) | [meincke-prompting-idea-variance-2024]{300}; [si-llm-research-ideation-2024]{318} | Technique-relative; differences between strategies vanish as the pool depletes [meincke-prompting-idea-variance-2024]{300} |
| Category and category-combination counts on pre-specified dimensions | [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}; flexibility categories in [anderson-llm-homogenization-ideation-2024]{303} | Depends on the categorization scheme [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312} |
| Learned functional-equivalence classes (distinct_k) and quality-weighted utility | [noveltybench-humanlike-diversity-2025]{310} | Classifier 79% accuracy; whether users want diversity is context-dependent |
| Human ratings of diversity | [verbalized-sampling-mode-collapse-2025]{311}; [creative-mad-debate-diversity-2026]{317} | Scale; Meincke et al. note rating pools of 100 ideas "does not scale well" [meincke-prompting-idea-variance-2024]{300} |
| Lexical metrics (compression ratio, n-gram self-repetition, Self-BLEU, BERTScore) | [shaib-text-diversity-measurement-2024]{322} `{confidence: search-summary}` | Low mutual correlation — report several |
| Coverage of a reference answer distribution (coverage-N, KL) | [verbalized-sampling-mode-collapse-2025]{311} | Requires a reference distribution |
| Authoring F1 vs judging F1 against complete truth | [judging-not-enumerating-omissions-2026]{321} | Requires complete or executable ground truth |

**Completeness and stopping signals present in this literature.** Two signals are used to say a
generation process has run out: a falling share of non-duplicates per batch with a plateau in
accumulated uniques [si-llm-research-ideation-2024]{318}, and convergence of new-idea similarity curves
plus a capture-recapture estimate of reachable uniques [meincke-prompting-idea-variance-2024]{300}.
Both are explicitly technique-relative: they estimate the reservoir of one generator, not the true
space [meincke-prompting-idea-variance-2024]{300}. Whether pooling generators adds coverage is a
matter of overlap and marginal additions: Meincke et al. report small overlap between different
prompting strategies' early ideas [meincke-prompting-idea-variance-2024]{300}, while cross-model average
similarity is high, so model identity alone establishes neither independent coverage nor zero additional
discoveries; overlap and marginal additions are what to assess [artificial-hivemind-homogeneity-2025]{307}.

**Omission resists audit.** Models "detect planted over-inclusions 6-7x more often than planted
omissions", and a production deployment "fails omission-first at 10:1"; "Omission is witness-blind
to local review" because "a missing member [is] an absence whose discovery is the authoring problem
itself" [judging-not-enumerating-omissions-2026]{321}. At the same time, judging a presented candidate
is much more accurate than authoring the set [judging-not-enumerating-omissions-2026]{321}, and recall
failures in generation largely disappear in verification for reverse questions
[calderon-recall-bottleneck-factuality-2026]{320}.

## Disconfirming analysis

Searches across the attested sources for evidence against each load-bearing claim:

- **"LLM ideation is less diverse."** Disconfirming or qualifying evidence found: (a) individual-level
  diversity is not lower — Anderson et al. find no within-user difference and broader category coverage
  per ChatGPT user [anderson-llm-homogenization-ideation-2024]{303}, and Deng et al. find near-identical
  within-session exploration [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}; (b) exposing people to
  AI ideas *increased* collective idea diversity in a dynamic 800+ participant experiment ("AI made ideas
  different, not better") [ashkinaze-ai-ideas-collective-diversity-2024]{304} `{confidence: search-summary}`;
  (c) with persona + CoT prompting an LLM exceeded human category-combination coverage
  [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}, and in-context regeneration reached human-level
  distinctness [noveltybench-humanlike-diversity-2025]{310}; (d) LLM research ideas were rated *more novel*
  than experts' individually [si-llm-research-ideation-2024]{318}. Outcome: the claim holds for default,
  independent sampling and for population-level measures; it does not hold as a fixed property under all
  prompting regimes or at the individual-idea level.
- **"Chain-of-thought increases diversity."** Supported by two independent groups
  [meincke-prompting-idea-variance-2024]{300} [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}.
  Weakening evidence: in Meincke et al. the CoT pool used a different model version than the baseline,
  failing runs were excluded, and the advantage vanished by ~750–800 ideas [meincke-prompting-idea-variance-2024]{300};
  in Deng et al. CoT did not restore across-session partitioning and had no effect in humans
  [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}.
- **"Personas increase diversity."** Weakened: celebrity personas gave inconsistent results and some
  persona variants were worse than base [meincke-prompting-idea-variance-2024]{300}; creativity system prompts did
  not close the population gap [wenger-kenett-creative-homogeneity-llms-2025]{306}; fine-grained persona detail
  adds little lexically [kambhatla-persona-lexical-diversity-2025]{313} `{confidence: search-summary}`. Supported only
  for ordinary personas in one single-model study [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}.
- **"Multiple agents increase diversity."** Directly disconfirmed for standard debate, which lowered
  across-run diversity, including with heterogeneous model families [creative-mad-debate-diversity-2026]{317};
  model ensembles are cautioned against as a diversity source [artificial-hivemind-homogeneity-2025]{307}.
  Debate's documented benefit is accuracy on correct-answer tasks [liang-multi-agent-debate-divergent-2023]{316}.
- **"Verbalized sampling improves diversity without cost."** No independent replication was found among
  attested sources; evidence comes from the proposing authors [verbalized-sampling-mode-collapse-2025]{311}.
- **"Explicit dimension enumeration improves coverage."** No attested source measures a coverage gain from
  LLM-generated dimensions; Luminate's evidence is qualitative and its authors flag dimension generation
  as hard [luminate-design-space-generation-2023]{315}. Pre-specified dimensions are used as a *measurement*
  frame, not tested as a *generation* intervention, in Deng et al. [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}.
- **"Saturation signals completeness."** Disconfirmed as stated: saturation estimates are relative to the
  generating technique [meincke-prompting-idea-variance-2024]{300}; Si et al.'s plateau of ~200 uniques reflects the
  generator's repetition, not the size of the research-idea space [si-llm-research-ideation-2024]{318} `extends`.
- **"A reviewer pass catches what an author missed."** Weakened for omissions: planted omissions are
  detected far less often than planted over-inclusions [judging-not-enumerating-omissions-2026]{321}; LLM judges
  correlate poorly with humans on similar-quality open-ended responses [artificial-hivemind-homogeneity-2025]{307}
  and the best LLM pairwise idea ranker agreed with expert reviewers 53.3% of the time against 56.1% human inter-reviewer agreement [si-llm-research-ideation-2024]{318}.
  Supporting: judging presented candidates is much more accurate than authoring [judging-not-enumerating-omissions-2026]{321}.

## Contradictions

| Claim | Position A | Position B | Relationship |
|---|---|---|---|
| Effect of AI on collective idea diversity | Exposure to AI ideas narrowed collective diversity [doshi-hauser-genai-collective-diversity-2024]{302} [anderson-llm-homogenization-ideation-2024]{303} [meincke-chatgpt-brainstorm-diversity-2025]{301} | High AI exposure increased collective diversity and its rate of change [ashkinaze-ai-ideas-collective-diversity-2024]{304} | `tension` — designs differ (direct assistance vs viewing example ideas in an evolving, multi-generation pool); not a shared frame for adjudication |
| Which personas help | Celebrity/"creative entrepreneur" personas modestly improved diversity over base (e.g., Creative Entrepreneur 0.348 vs 0.377) [meincke-prompting-idea-variance-2024]{300} | Ordinary personas beat "creative entrepreneur" personas; the latter were the weaker cue [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312} | `qualifies` — Deng et al. did not test against Meincke's metric or model; both find some persona effect, disagreeing on which type |
| Whether LLMs can match human diversity by prompting | Even the best prompt (CoT) came "close" to but below pooled humans [meincke-prompting-idea-variance-2024]{300}; creativity prompts left population variability far below humans [wenger-kenett-creative-homogeneity-llms-2025]{306} | Persona + CoT exceeded humans [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}; in-context regeneration matched or exceeded humans [noveltybench-humanlike-diversity-2025]{310} | `incommensurable` — different metrics (embedding similarity vs category combinations vs learned equivalence classes), domains and models |
| Model scale and diversity | Larger models within a family often less diverse [noveltybench-humanlike-diversity-2025]{310}; benchmark capability correlates with worse randomness/creativity [west-potts-base-vs-aligned-creativity-2025]{309} | More capable models benefit more from verbalized sampling [verbalized-sampling-mode-collapse-2025]{311}; DIV-SE gains require instruction-following capability [naik-div-se-diversity-of-thought-2023]{314} | `qualifies` — default-output diversity vs responsiveness to a diversity-eliciting prompt are different quantities |

## Transfer-relevant observations

Stated in the field's own terms; no project recommendations.

- `{inferred: convergence}` The measured deficit is in what independent draws jointly cover
  [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312} [anderson-llm-homogenization-ideation-2024]{303}
  [wenger-kenett-creative-homogeneity-llms-2025]{306}; a single list can look varied while repeated or
  cross-model generation returns the same modes [artificial-hivemind-homogeneity-2025]{307}.
- Interventions with measured gains share explicit conditioning on what has already been generated plus an
  instruction to differ (CoT revision step, in-context regeneration, verbalized sets)
  [meincke-prompting-idea-variance-2024]{300} [noveltybench-humanlike-diversity-2025]{310}
  [verbalized-sampling-mode-collapse-2025]{311}, or distinct sampling cues per draw (ordinary personas,
  persistent per-agent lenses) [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}
  [creative-mad-debate-diversity-2026]{317}. `{inferred: aggregate}`
- Interventions that add exposure to consensus — similarity feedback, selecting the best from pooled
  sessions, unrestricted debate — measured as neutral or harmful to diversity
  [meincke-prompting-idea-variance-2024]{300} [creative-mad-debate-diversity-2026]{317}. `{inferred: aggregate}`
- Saturation and capture-recapture counts in this literature are estimates of a generator's reachable
  reservoir, explicitly not of the true space [meincke-prompting-idea-variance-2024]{300}.
- Diversity metrics disagree with one another and with human judgments to a degree the sources
  themselves flag [meincke-prompting-idea-variance-2024]{300} [shaib-text-diversity-measurement-2024]{322}
  [noveltybench-humanlike-diversity-2025]{310}; category-based coverage depends on the categorization scheme
  [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}.
- Diversity and quality are separable outcomes; several sources measure only diversity
  [meincke-prompting-idea-variance-2024]{300} [deng-brucks-toubia-llm-idea-diversity-barriers-2026]{312}, and
  frequency-based selection of approaches keeps the commonest ones [naik-div-se-diversity-of-thought-2023]{314}.
- For enumeration tasks, membership judgment of presented candidates is more accurate than authoring
  the full set, but omissions are rarely detected by local review [judging-not-enumerating-omissions-2026]{321};
  generation-time recall of long-tail items lags encoding and is partly recoverable by thinking
  [calderon-recall-bottleneck-factuality-2026]{320}. Whether this transfers from facts and predicates to
  approach families is untested `extends`.
- LLM judges are weak at ranking open-ended ideas against human preferences
  [si-llm-research-ideation-2024]{318} [artificial-hivemind-homogeneity-2025]{307}, and may prefer outputs of
  their own model family [liang-multi-agent-debate-divergent-2023]{316}.

## Revisit if

- An independent replication of verbalized sampling or in-context regeneration on ideation/approach
  enumeration (not creative writing) reports effects on coverage of a known reference set.
- A study measures whether LLM-generated dimensions (Luminate-style) increase coverage of a reference
  set of approaches versus unstructured listing.
- The full Nature Human Behaviour article (Meincke, Nave, Terwiesch 2025) becomes readable — its
  diversity metrics and any mitigation tests would firm up or revise §1 and §3.
- Omission-detection results [judging-not-enumerating-omissions-2026]{321} are extended to open-ended
  approach families or to reviewers given a structured checklist of dimensions.
- New model generations report reversed alignment-diversity trends (e.g., post-training explicitly
  optimizing for diversity).
- Capture-recapture or species-richness estimators are validated against a known-complete idea or approach space.

## Revisions

- **2026-10-20 — correction (lead, after adversarial-read).** The categorical "pooling helps only if" restriction is replaced by an overlap and marginal-addition criterion.
- **2026-10-20 — correction (adversarial re-check).** The marginal-addition clause is restated unambiguously (R6).
