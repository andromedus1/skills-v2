---
source_handle: ding-llm-cross-domain-analogies-2023
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2302.12832
provenance: source-direct
substrate_confidence: source-direct
source_class: peer-reviewed conference paper, exploratory evaluation without a no-analogy control (Creativity and Cognition C&C '23; DOI 10.1145/3591196.3593516 read off the PDF)
---

# Fluid Transformers and Creative Analogies: Exploring Large Language Models' Capacity for Augmenting Cross-Domain Analogical Creativity (Ding, Srinivasan, MacNeil & Chan)

## Source structure and scope
Zijian Ding, Arvind Srinivasan (Maryland), Stephen MacNeil (Temple), Joel Chan (Maryland). C&C '23. arXiv
2302.12832, 17 pages. Read: abstract, §1 contributions, §2 related work (LLM analogy), §3 prompt-engineering
explorations, §4 Study 1 (participants, correlation result), §6 discussion and limitations.

## Anchored details
- **Abstract:** "LLM-generated cross-domain analogies were frequently judged as helpful in the context of a problem
  reformulation task (median 4 out of 5 helpfulness rating), and frequently (∼80% of cases) led to observable changes
  in problem formulations"; "upper bound of ∼25% of outputs being rated as potentially harmful, with a majority due to
  potentially upsetting content".
- **§1:** human analogy-making is "highly sensitive to surface similarities, favoring 'near', or within-domain,
  analogs".
- **§2 (as reported):** Zhu et al. integrated 10 LLM analogically generated concepts into a design team's brainstorming;
  "the analogical concepts generally received high novelty scores but low feasibility scores."
- **§3.1 prompt structure:** GPT-3 text-davinci-002, temperature 1; problem split into "stakeholder, context, goal and
  obstacle"; informally this "enabled us to balance the distance (stakeholder and context are different) and usefulness
  (goal and obstacle are similar)" better than an earlier design prompting for "an abstracted schema"; 480 analogies
  across six design problems.
- **§1 / §3.3 results:** one- or few-shot prompts gave outputs where "70% ... were both unique and judged by researcher
  to be potentially useful"; one-shot vs zero-shot ≈80% vs ≈40% potentially useful and less similar to input
  (<0.5 vs >0.7 semantic similarity); few-shot ≈0.3 similarity, ≈67% useful. Duplicates — analogies "so similar to
  previously encountered analogies that it was redundant" — were coded during screening.
- **§4:** Prolific participants (123 enrolled; those not completing round two removed); no statistically significant
  correlation between a priori researcher usefulness judgments and in-use helpfulness ratings (point-biserial −0.0266,
  p = 0.6939), with alternative explanations not excluded.
- **§6:** results "underscore the importance of going beyond simple benchmark-based measures of output 'quality'"; helpfulness
  ratings rose from the first to the second analogy, suggesting some "settling into" the task. Limitations: only one
  run of the one-shot paradigm with one example was used in Study 1; not confident one-shot beats few-shot.
