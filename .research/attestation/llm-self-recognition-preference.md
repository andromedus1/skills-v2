---
source_handle: llm-self-recognition-preference
fetched: 2026-10-18
source_url: https://arxiv.org/abs/2404.13076
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "partial: abstract, sections 1, 2.4, 3.1-3.4, 5.1, 5.2 (arXiv HTML v1)"
---

# LLM Evaluators Recognize and Favor Their Own Generations

## Source structure and scope
Arjun Panickssery (MATS), Samuel R. Bowman (New York University; Anthropic, PBC),
Shi Feng (New York University). arXiv 2404.13076 v1, 15 Apr 2024. Read via arXiv HTML:
abstract, introduction, out-of-the-box measurements, fine-tuning correlation and
confounder controls, discussion and limitations. Tasks are news summarization only
(XSUM and CNN/DailyMail, 1,000 articles each); evaluators are GPT-3.5 Turbo, GPT-4
and Llama 2. Self-preference is measured against other LLMs' and human-written summaries.

## Anchored details
- **Abstract:** self-preference is defined as "where an LLM evaluator scores its own outputs
  higher than others' while human annotators consider them of equal quality." The authors
  report that out of the box "LLMs such as GPT-4 and Llama 2 have non-trivial accuracy at
  distinguishing themselves from other LLMs and humans", and that fine-tuning reveals "a
  linear correlation between self-recognition capability and the strength of self-preference bias".
- **Section 1, contributions:** "On two summarization tasks, LLMs (GPT-3.5 Turbo, GPT-4, and
  Llama 2) disproportionately favor summaries written by themselves over those by other LLMs
  and from humans."
- **Section 2.4, "Out-of-the-Box Self-Preference":** in the pairwise setting the
  self-preference scores of each pair of evaluator models add up to more than one (the
  section's numeric symbol did not survive text extraction; section 5.2 restates it as "the
  sum of self-preference scores of a pair of LLMs exceeds one"), and "All models
  show the greatest self-preference against the human summary." In the individual (Likert)
  setting, "Llama doesn't give very different scores to the different sources, while GPT-4 and
  GPT-3.5 show signs of self-preference."
- **Section 3.4, "Controlling for Confounders":** models fine-tuned on unrelated tasks (length,
  vowel count, readability, constant and random answers) fall on the same linear trend.
  Prompt-only evidence: when source labels were reversed, GPT-4 and GPT-3.5 "show a preference
  for the summary labeled as being their own generation" on XSUM; "In the CNN dataset or the
  Llama evaluator, no clear difference is shown from label reversal."
- **Section 5.1:** the authors suggest that if self-preference proves pervasive,
  "countermeasures such as authorship obfuscation should be incorporated into standard
  prompting practice", and note risk where "similar LLMs are use as both optimizer and reward
  model".
- **Section 5.2, "Limitations and Future Work":**

  > Despite the use of a diverse set of control tasks, our experiments can only provide evidence towards the causal hypothesis without fully validating it.

  On ground-truth quality: "Self-preference can be justifiable if the LLM's generation is
  indeed higher quality than the alternative"; controlling for this "would require controlling
  for generation quality when measuring self-preference using groundtruth annotation", which the
  study offers only indirect evidence for (pairwise self-preference sums exceeding one).
