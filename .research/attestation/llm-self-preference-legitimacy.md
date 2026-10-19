---
source_handle: llm-self-preference-legitimacy
fetched: 2026-10-18
source_url: https://arxiv.org/abs/2504.03846
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "partial: abstract, sections 2.1, 3.1, 3.2, 5.1, 5.2 and Appendix H limitations (arXiv HTML v3)"
---

# Do LLM Evaluators Prefer Themselves for a Reason?

## Source structure and scope
Wei-Lin Chen, Zhepei Wei, Xinyu Zhu (University of Virginia), Shi Feng (George Washington
University), Yu Meng (University of Virginia). arXiv 2504.03846 v3, 12 Dec 2025 (comments:
"Added LMArena experiments"). Read via arXiv HTML. Uses verifiable benchmarks with ground truth
(MATH500, MMLU, MBPP+ for code) and pairwise judging with order swapping, across Llama, Qwen,
Gemma, Mistral, Phi, GPT and DeepSeek families. Self-preference is measured strictly as a judge
favouring its exact own output.

## Anchored details
- **Abstract:** prior studies "relied primarily on subjective tasks" lacking ground truth; this
  study separates "harmful self-preference (favoring objectively worse responses) from legitimate
  self-preference (favoring genuinely superior ones)". Findings as stated:

  > (1) While stronger models exhibit greater self-preference, much of this preference aligns with objectively superior performance, indicating stronger models prefer themselves mostly legitimately.

  > (2) Harmful self-preference persists when evaluator models err as generators, and stronger models display more pronounced harmful self-preference bias when they do err.

  (3) generating a long chain of thought before the verdict "effectively reduce[s] the harmful
  self-preference."
- **Section 2.1:** every pair is judged twice with response order swapped to mitigate position bias.
- **Section 3.1:** task accuracy and judge accuracy correlate (Pearson r of 0.795, 0.708 and 0.899
  for MATH500, MMLU and MBPP+); "in code generation, models that produce correct code are better at
  identifying bugs and errors in peer code."
- **Section 3.2:** on MATH500, "Qwen-2.5-70B and Llama-3-70B achieve LSPR of 96.57 and 95.16"
  (legitimate self-preference ratio).
- **Section 5.1, "Harmful Self-Preference in LLM Evaluators":** harmful self-preference propensity
  (HSPP) is the tendency to prefer its own incorrect output over a correct alternative.

  > Notably, the most performant model, Qwen2.5-72B, exhibits an HSPP of 86 on MATH500 and 73 on MMLU, significantly higher than its overall SPR ( Figure 3 ) of 55 and 52 , respectively.

  On MBPP+ the correlation is weaker, but large models show HSPP "ranging from approximately 50 to 75",
  above overall SPR "which remains below 40". The authors summarise: "as models become more capable,
  they are also more confident in their own responses, even when they are wrong."
- **Section 5.2:** no-reasoning judging "exhibits the highest HSPP"; CoT lowers it and long-CoT
  reasoning models achieve "the lowest HSPP across all models".
- **Appendix H, "Limitations":** other biases (length, order, style) are out of scope; "a more relaxed
  definition may include preference toward outputs from models within the same family", which the
  study does not measure.
