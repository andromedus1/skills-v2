---
source_handle: erana-finlayson-neural-patent-landscaping-2024
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2407.08001
provenance: source-direct
substrate_confidence: source-direct
source_class: research preprint (arXiv 2407.08001v1, 10 Jul 2024), empirical ML evaluation
---

# Automated Neural Patent Landscaping in the Small Data Regime (Islam Erana and Finlayson, 2024)

## Source structure and scope
Tisa Islam Erana and Mark A. Finlayson, Florida International University. 11-page arXiv
preprint. Reviews prior automated patent landscaping systems, builds a labelled AI-patent
dataset with "hard" examples near the landscape boundary via active learning, and compares
models. Engagement depth: full text extracted; abstract, §1, §2 (related work), §3 (data),
Table 4 results and §8 limitations read.

## Anchored details
- **Abstract / §1:** "Patent landscaping is the process of identifying all patents related to a
  particular technological area"; constructing landscapes is "intensely laborious and
  expensive". Landscaping differs from classification "because a standardized patent class
  scheme may not contain classes or distinctions relevant to a particular patent landscaping
  question or need." Inclusion judgements need rare specialised expertise.
- **§1:** prior systems (Abood and Feltenberger 2018; Choi et al. 2019) "were trained only on
  'easy' examples found via keyword search or patent family expansion; as a consequence, they
  do not work well on 'hard' examples near the landscape boundary."
- **§2, cited-by-this-source description of Abood and Feltenberger (2018, Artificial
  Intelligence and Law 26:103-125):** ~1,000 expert-curated "seed" patents; "Level 1" set =
  patents sharing CPC codes with or cited by seeds; "Level 2" adds family members; anything
  outside L2 is an "anti-seed" negative; a wide-and-deep LSTM classifier is applied to L2;
  reported F1 above 0.95 on four topics (browser, operating system, video codec, machine
  learning). The authors state that "if a patent that does not share a CPC code, citation, or
  family link with one of the seed patents, it will never be included in the landscape",
  which is "potentially problematic for broad landscapes covering many CPC codes, or
  landscapes that include many patents (where citation networks are unlikely to be
  exhaustive)."
- **§2 (cited-through):** Choi et al. (2019) generated negatives by re-running the human
  experts' keyword searches and taking returned-but-excluded patents; reported F1 0.62-0.89.
- **§3:** hypothesis that "especially for a large technology domain, the seeds would not
  necessarily be near the boundary, and anti-seeds would almost certainly be far from it";
  2,020 USPTO-examiner-annotated AI seeds plus 56,093 anti-seeds; active learning (SVM) used to
  surface boundary examples, yielding 395 hard positives and 754 hard negatives (Table 1).
- **Table 4:** the Abood and Feltenberger architecture scored F1 0.77 average on easy examples
  but 0.60 on hard examples (0.39 on hard-negative holdout); the best models reached about
  0.67-0.69 on hard examples versus 0.91-0.93 on easy ones.
- **§7 (Citation networks):** removing 1-hot citation features from the A&F architecture
  "actually improved performance".
- **§8 Limitations:** a single domain (AI) studied; unclear generalisation to more specific
  landscape topics; citation network information "did not improve the results as much as
  expected, which is counter-intuitive."
