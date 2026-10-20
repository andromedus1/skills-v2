---
source_handle: liu-agreement-not-quality-coding-2026
fetched: 2026-10-20
source_url: https://arxiv.org/pdf/2607.28890
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: arXiv PDF (32 pp.), text extracted with PyMuPDF; abstract, introduction, results patterns, discussion excerpt, limitations and conclusion read; tables partly read
---

# Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth

## Source structure and scope
Alex Liu, Lief Esbenshade, Michael Xiao, Victor Tian (University of Washington), Zachary Zhang, Kevin He
(Colleague AI), Min Sun (University of Washington). arXiv 2607.28890 preprint (no venue printed). Five LLM
systems and three trained human coders independently applied a 72-item hierarchical, multi-label codebook to
2,560 educator messages; one independent domain expert judged 855 pairwise comparisons of code sets blind to
source.

## Anchored details
- **Abstract:** evaluations of LLM coding "almost universally measure model performance as agreement with human coders, a
  practice that presumes human coding is the standard to approximate". "Human-LLM agreement (mean Jaccard 0.30) falls well
  below human-human agreement (0.52) ... yet the blind verifier preferred human and LLM coding at indistinguishable rates
  (51.5% vs. 48.5%, p = 0.537)"; "For several substantive codes, human consensus encoded shared bias that the verifier
  rejected in favor of the LLM interpretation. Agreement-based evaluation is therefore insufficient for automation decisions".
- **Introduction:** "When humans disagree, deviation from any one human coder cannot distinguish an LLM that codes poorly from
  an LLM that codes differently but well. When humans agree, their consensus may still reflect shared interpretive bias rather
  than validity". Moderate human–LLM agreement "can certify shared error".
- **Results, Pattern 2:** e.g. ELA Skills Development (human–human 0.48) endorsed 61% when an LLM applied it vs 30% when a human
  did; "two coders can reliably agree while both under-applying a code."
- **Results, Pattern 3:** "Inquiry and Deep Questions (H-L = 0.15) shows human endorsement of 23% versus LLM endorsement of 65%.
  The low agreement reflects LLMs applying the code where humans do not, yet the verifier judges the LLM application appropriate
  far more often than the human omission. This pattern appears across 12 codes."
- **Results, Pattern 4:** codes where LLMs over-apply and the verifier rejects them (e.g. Tiered Scaffolding 86% human vs 27% LLM
  endorsement) "require recognizing pedagogical intent not explicitly stated in the text."
- **Discussion:** supports a shift "from agreement-as-quality to disagreement-as-information"; "triangulation with independent
  quality assessment is necessary."
- **Limitations:** single codebook and dataset; "the verification relies on a single independent verifier ... a different expert
  might endorse the human coders' interpretation, so the divergence findings demonstrate that divergence is possible rather than
  that human coding is systematically wrong"; models are a capability snapshot; temperature zero.
