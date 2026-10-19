---
source_handle: llm-judge-affinity-similarity
fetched: 2026-10-18
source_url: https://arxiv.org/abs/2502.04313
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "partial: abstract, sections 1, 3 (affinity bias), 5 (trend and implications), 7, Appendix B.4-B.6 (arXiv HTML v2); several numeric symbols did not survive text extraction"
---

# Great Models Think Alike and this Undermines AI Oversight

## Source structure and scope
Shashwat Goel, Joschka Strüber, Ilze Amanda Auzina, Karuna K Chandra, Ponnurangam Kumaraguru,
Douwe Kiela, Ameya Prabhu, Matthias Bethge, Jonas Geiping (ELLIS Institute Tübingen, Max Planck
Institute for Intelligent Systems, Tübingen AI Center / University of Tübingen, IIIT Hyderabad,
Contextual AI, Stanford). arXiv 2502.04313 v2, 12 Jun 2025 (comments: "60 pages, 20 figures").
Read via arXiv HTML. Introduces CAPA, a chance-adjusted similarity metric based on overlap in model
mistakes; judge experiments use filtered MMLU-Pro free-form responses with ground truth, nine
open-weight judges from four families, plus an AlpacaEval extension. Several in-text coefficient
values were rendered as math and lost in extraction; only values present as text are recorded here.

## Anchored details
- **Abstract:** "Using CAPA, we first show that LLM-as-a-judge scores favor models similar to the
  judge, generalizing recent self-preference results." Also: "model mistakes are becoming more similar
  with increasing capabilities, pointing to risks from correlated failures."
- **Section 1, item 1 "LLM-as-a-Judge":**

  > It might seem possible to avoid this concern by simply using a different model as the judge.

  The authors ask whether judges show "affinity bias" and find "LM judges indeed assign higher scores
  to models that are more similar to themselves."
- **Section 3, framing:** leaderboards "assume that excluding the judge model from the rankings
  circumvents this problem"; the finding "would indicate that it is not sufficient to just use a
  held-out LM as the judge; one must account for the confounder of similarity."
- **Section 3, motivating example:** "Qwen2.5-72B-Instruct as a judge scores Qwen2.5-7B-Instruct as
  being 71% correct, while the more capable (41% vs 51% MCQ accuracy) Llama-3.1-70B-Instruct is deemed
  less accurate at 67%." Favoritism "extends beyond self- or family- preference to all models that are
  functionally similar."
- **Section 3, Q2 (Table 2):** with accuracy controlled by partial correlation and multiple regression,
  "there is still a significant effect of similarity on judgment scores even for the best judge models";
  "especially for small models" the similarity effect is greater; the coefficient of accuracy "increases
  for more capable judge models".
- **Section 5, "Potential Implications":** the trend "could undermine benefits from using LM juries by
  compromising independence and amplifying collective biases."
- **Appendix B.6:** partial correlations between judge score and similarity, controlling for accuracy,
  are significant and positive for all judges.
