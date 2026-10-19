---
source_handle: llm-self-bias-refinement
fetched: 2026-10-18
source_url: https://arxiv.org/abs/2402.11436
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "partial: abstract, sections 1, 4.2, 4.4, 5 (external feedback; model size), conclusion and limitations (arXiv HTML v2)"
---

# Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement

## Source structure and scope
Wenda Xu, Guanglei Zhu, Xuandong Zhao, Liangming Pan, Lei Li, William Yang Wang
(University of California, Santa Barbara; Carnegie Mellon University). arXiv 2402.11436 v2,
18 Jun 2024. Read via arXiv HTML. Models: GPT-4, GPT-3.5, Gemini, LLaMA2, Mixtral and
DeepSeek; tasks: machine translation, constrained text generation (CommonGen) and
mathematical reasoning. Self-bias is quantified with two statistics (bias and distance
skewness) comparing self-evaluation against an external quality measure.

## Anchored details
- **Abstract:** "We find that self-bias is prevalent in all examined LLMs across multiple
  languages and tasks. Our analysis reveals that while the self-refine pipeline improves the
  fluency and understandability of model outputs, it further amplifies self-bias."
- **Section 4.2, "Self-Bias Amplification during Iterative Refinement":** GPT-4 and Gemini show
  some robustness, yet the authors "observe a consistent amplification of self-bias through the
  self-refine pipeline across four language directions". Figure 5 caption: "the rate of LLM's
  self-estimated improvements is much higher than the true coverage improvements".
  A single graduate-student annotator (MQM-style) found that "all three LLMs have not received
  measurable improvements via the self-refine pipeline".
- **Section 1:** "LLMs may favor texts that mirror their style, potentially leading to false
  positive optimization and reduced diversity in text generation."
- **Section 5, "External Feedback Reduces Self-Bias":** the external feedback is InstructScore,
  a reference-based feedback model the authors treat as oracle feedback:

  > Since InstructScore can access reference text to provide feedback, we recognize this external feedback as oracle feedback.

  Result: "external feedback with accurate assessment can significantly lower the model's bias
  at iterative refinement", and "all LLMs with external feedback can elicit their self-correction
  ability with consistent BLEURT improvements at self-refine iterations" (Figure 9, Yoruba-to-English).
- **Section 5, "Larger Model Reduces Self-Bias":** LLaMA2-70B's self-bias "begins to plateau after
  the 5th iteration", while 7B and 13B models continue to amplify it.
- **Limitations:** the study measures a model's bias toward its own output; bias "between
  different LLMs" is left open, including whether an LLM has more bias toward models "within the
  same language model families".
