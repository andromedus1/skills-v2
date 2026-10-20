---
source_handle: verbalized-sampling-mode-collapse-2025
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2510.01171
provenance: source-direct
substrate_confidence: source-direct
---

# Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity

## Source structure and scope
Jiayi Zhang, Simon Yu, Derek Chong, Anthony Sicilia, Michael R. Tomz, Christopher D. Manning, Weiyan
Shi; arXiv 2510.01171, v4 revised 2026-07-15. Abstract and HTML full text read (via extraction);
appendix experiments not audited line by line. Preprint.

## Anchored details
- **Abstract, thesis:** post-training alignment "often reduces LLM diversity, leading to ... mode
  collapse"; authors identify "typicality bias in preference data, whereby annotators systematically
  favor familiar text" as a data-level driver.
- **Typicality-bias estimate (HelpSteer):** alpha-hat = 0.57 +/- 0.07 (Llama-3.1-405B reference) and
  0.65 +/- 0.07 (GLM-4.5 reference), p < 10^-14.
- **Method:** prompt the model to verbalize a distribution over a set of responses, e.g. "Generate 5
  jokes about coffee and their corresponding probabilities"; variants VS-Standard, VS-CoT, VS-Multi
  (multi-turn "5 more with probabilities"). Baselines: direct, CoT, sequence (list in one call), multi-turn.
- **Diversity tuning:** diversity can be adjusted by asking for responses "with probabilities below
  {threshold}".
- **Measures:** semantic diversity = 1 - mean pairwise cosine similarity (OpenAI text-embedding-3-small,
  negatives clipped); ROUGE-L lexical; human Likert ratings; for open-ended QA, coverage-N and KL
  divergence to a reference distribution.
- **Results:** creative writing diversity "1.6-2.1x over direct prompting" (abstract); human-rated
  diversity VS-Standard 2.39/3.06/3.01 vs direct 1.90/2.74/1.83 (poem/story/joke); synthetic-data
  downstream math accuracy 32.8% baseline to 37.5% (VS-Multi).
- **Claims:** "without sacrificing factual accuracy and safety" (abstract; appendices E.6, E.9);
  "more capable models benefit more" — larger models' gains 1.5–2x those of smaller models.
- **Limitations:** extra calls per response set; dependence on model scale/capability; verbalized
  probabilities imperfectly calibrated (KL 0.12 from estimated pre-training distributions).
