---
source_handle: martinsson-bonde-mm-combinatorics-2025
fetched: 2026-10-20
source_url: https://www.cambridge.org/core/journals/ai-edam/article/managing-combinatorial-design-challenges-using-flexibility-and-pathfinding-algorithms/16FD0638E21D476AAECA4B81C1BE7F35
provenance: source-direct
substrate_confidence: source-direct
---

# Managing combinatorial design challenges using flexibility and pathfinding algorithms (Martinsson Bonde et al. 2025)

## Source structure and scope
Julian Martinsson Bonde, Iñigo Alonso Fernández, Michael Kokkolaras, Johan Malmqvist, Massimo Panarotto,
Ola Isaksson (Chalmers; McGill; Politecnico di Milano). AI EDAM 39, e16, 1–16 (2025), doi
10.1017/S0890060425100048, open access (CC BY-NC). PDF read via text extraction: abstract, introduction,
"Exploring large discrete design spaces" related-work section, conclusion. Proposes MOTAC, a
shortest-path method over morphological matrices; automotive (steer-by-wire) case study.

## Anchored details
- **Abstract:** "Morphological matrices (MMs) have traditionally been used to generate concepts by
  combining different means. However, exploring the vast design space resulting from the combinatorial
  explosion of large MMs is challenging. Additionally, all alternative means are not necessarily
  compatible with each other."
- **Introduction:** early in design "expert opinion is required to identify promising configurations.
  However, exploring vast discrete design spaces through expert opinion alone makes it difficult to ensure
  that all promising configurations have been considered." MMs "list all functions that are necessary to
  fulfill the main function, together with all considered means"; one means per function yields a
  candidate.
- **Introduction (as reported):** Almefelt (2005) MM with eight functions and up to 22 means per function
  → "a theoretical maximum of about 54.9 billion possible combinations. Such a vast number of combinations
  cannot possibly be considered manually." "the traditional MM is used to support concept generation, but
  not evaluation ... the traditional method contains no mechanism to assist in identifying the most
  promising solutions."
- **Related work:** "combinatorial explosion often makes it challenging to consider all possible
  combinations in the MM. Thus, high-performing combinations can remain undiscovered." Motte & Bjärnemo
  (2013) classify reduction approaches as "automatic or semi-automatic exploration and reduction through
  heuristics" (as reported). Ulrich et al. say infeasible means should be excluded, "Yet clarity regarding
  the feasibility of design alternatives is not always evident in the early phases". Pahl et al. suggest
  identifying incompatible pairings of means; "These methods do not require the use of software ... but
  their impact on the number of possible combinations is small." Experiments by Smith et al. (2012) with
  engineering students "suggest that large MMs, especially those with many functions relative to the
  number of means, can result in lower-quality concepts" — so for manual use "it can be beneficial to
  restrict the decomposition of functions and keep them at a high level" (as reported). Ölvander et al.
  (2009, Tabu search) and Tiwari et al. (2009, genetic algorithm) attach models to means and encode
  incompatibilities as optimization constraints.
- **Conclusion:** pathfinding requires alternatives in the MM "to be quantifiable".
