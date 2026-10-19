---
source_handle: llm-critics-catch-bugs
fetched: 2026-10-18
source_url: https://arxiv.org/abs/2407.00215
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "partial: abstract, sections 1, 2.1-2.2, 3.1, 3.3, 3.4, 3.6, 5 (arXiv HTML v1); figure values not read off the plots"
---

# LLM Critics Help Catch LLM Bugs

## Source structure and scope
Nat McAleese, Rai (Michael Pokorny), Juan Felipe Cerón Uribe, Evgenia Nitishinskaya, Maja
Trębacz, Jan Leike (OpenAI). arXiv 2407.00215 v1, 28 Jun 2024 (cs.SE). Read via arXiv HTML.
Trains "CriticGPT" with RLHF to critique model-written code from real assistant tasks; compares
model critiques, human contractor critiques and human+model teams on code with human-inserted bugs
and on human-detected (naturally occurring) bugs. Many headline results are presented as figures;
only numbers stated in text are recorded.

## Anchored details
- **Abstract:** "On code containing naturally occurring LLM errors model-written critiques are preferred
  over human critiques in 63% of cases, and human evaluation finds that models catch more bugs than human
  contractors paid for code review." Also:

  > Critics can have limitations of their own, including hallucinated bugs that could mislead humans into making mistakes they might have otherwise avoided, but human-machine teams of critics and contractors catch similar numbers of bugs to LLM critics while hallucinating less than LLMs alone.

- **Section 2.1:** contractors had "a median of five years experience with Python (self-reported)" and took
  "a median of around fifty minutes per example to write their critique".
- **Section 3.1:** both LLM critics (prompted ChatGPT and CriticGPT) caught "many more bugs than the human
  annotators" on inserted bugs; the human cohort "does not represent the best possible human performance;
  however it is representative of the set of contractors used for ChatGPT."
- **Section 3.3:** "Human+CriticGPT teams write substantially more comprehensive critiques than humans
  alone"; "the rate of nitpicks and hallucinated bugs is much higher for models than for humans"; teams
  "fall somewhere in the middle". Figure 6 caption: "Human-machine teams do not increase comprehensiveness"
  relative to the model alone.
- **Section 3.4:** "the probability of catching a bug increases with the number of claims that a critique
  makes", and models that hallucinate more also catch more bugs — framed as a precision/recall tradeoff
  whose right balance "is not obvious".
- **Section 3.6, "LLM critics generalize beyond code":** a CriticGPT critique was sampled for "a large subset of all
  ChatGPT training data that had been rated as "flawless" by a first human annotator"; "In cases where the sampled
  critique identified a problem we asked humans to review the completion with access to the critique." Then:

  > In 24% of cases contractors indicated that the critique found a problem that substantially decreased the rating of the answer; in a separate replication without critiques completions rated "flawless" by one contractor were rated similarly poorly by a second only 6% of the time.

- **Section 5, "Discussion & Limitations":** "the distribution of inserted bugs is quite different from the
  distribution of natural LLM errors"; code snippets "are typically quite short" with "no multi-file support
  and no repository navigation"; nitpick and hallucination rates remain "quite high" in absolute terms;
  critics "may introduce new" biases.
