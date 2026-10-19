---
source_handle: llm-judge-panel-poll
fetched: 2026-10-18
source_url: https://arxiv.org/abs/2404.18796
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "partial: abstract, sections 1-3.1, 4.1-4.5, 5 (arXiv HTML v2)"
---

# Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models

## Source structure and scope
Pat Verga, Sebastian Hofstätter, Sophia Althammer, Yixuan Su, Aleksandra Piktus, Arkady
Arkhangorodsky, Minjie Xu, Naomi White, Patrick Lewis (Cohere). arXiv 2404.18796 v2, 1 May 2024.
Read via arXiv HTML. A Panel of LLM evaluators (PoLL) of three models from three families
(Command R, Claude Haiku, GPT-3.5) is compared with single judges, including GPT-4, on KILT
single-hop QA (NQ, TriviaQA, HotPotQA), multi-hop QA (Bamboogle, HotPotQA) and Chatbot Arena Hard.
Human annotations / Arena rankings are the reference. Note the authors work at Cohere, whose model
is one panel member.

## Anchored details
- **Abstract:** "using a PoLL composed of a larger number of smaller models outperforms a single large
  judge, exhibits less intra-model bias due to its composition of disjoint model families, and does so
  while being over seven times less expensive."
- **Section 2, PoLL score:** "each evaluator model independently scores a given model output"; scores
  are pooled by a voting function (max voting for binary QA judgements, average pooling for 1-5 Arena scores; section 3.1).
- **Section 4.1, Table 1 (Cohen's kappa vs human judgements, single-hop QA):** PoLL 0.763 / 0.906 /
  0.867 on NQ / TQA / HPQA; GPT-4 0.627 / 0.841 / 0.830; Haiku 0.749 / 0.894 / 0.873. "overall, PoLL has
  the strongest correlation across various tasks, while GPT-4 is one of the weaker evaluators on this
  particular task setup". (On HPQA, Haiku's 0.873 exceeds PoLL's 0.867.)
- **Section 4.2, Table 2 (vs Chatbot Arena ranking):** PoLL Pearson 0.917, Kendall tau 0.778; GPT-4
  0.817 / 0.667.
- **Section 4.3:** GPT-4 improved with prompt changes; the authors hypothesise it was "over-reasoning"
  on what is essentially fuzzy string matching against a gold reference.
- **Section 4.4, "Judge Bias and Consistency":** PoLL had the smallest spread of accuracy deltas versus
  humans ("standard deviation of 2.2"; GPT-3.5 6.1), and

  > We also see in Figure 4 that the highest positive delta for each individual model being scored occurs when it is judged by itself.

  On Arena Hard, the GPT-4 judge ranked another GPT-4 variant second rather than its actual fourth place.
- **Section 4.5:** the three-model panel is "seven to eight times less expensive than running a single
  GPT-4 judge" at the prices stated at the time of writing.
- **Section 5, limitations:** "we investigated only three evaluator settings and a limited number of
  judges and panel compositions"; applicability to "math or reasoning evaluations" is left to future
  work, as is panel selection.
