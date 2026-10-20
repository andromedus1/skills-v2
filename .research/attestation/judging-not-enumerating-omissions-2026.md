---
source_handle: judging-not-enumerating-omissions-2026
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2608.01000
provenance: source-direct
substrate_confidence: source-direct
---

# Judging Is Not Enumerating: Silent Omissions in LLM-Authored Acceptable Sets

## Source structure and scope
Wenhui Chen, Jianlin Chen, Ziyao Lin, Peiji Long, Chi Man Vong; arXiv 2608.01000 v1 (2026-08-02), preprint.
Abstract and HTML full text read via extraction.

## Anchored details
- **Protocol:** same model weights used to judge membership of one presented candidate (pointwise bit) versus to
  author the whole acceptable set (autoregressive emission with learned stopping). Four reference constructions:
  algorithmic string predicates, algorithmic numeric predicates (complete truth), HumanEval+/MBPP+ test suites,
  WordNet synsets (explicitly incomplete).
- **Gap (abstract):** "models judge whether a candidate belongs far better than they author the set itself"; on the
  algorithmic construction the gap is roughly +0.29 to +0.34 F1 "over a 24x parameter range and does not close";
  models judging code at F1 0.74–0.90 author suites admitting only 19–42% of oracle-correct solutions.
- **Control:** asked to emit the predicate rather than its extension, models reach F1 about 0.99 — "The failure is
  not missing knowledge or an inability to specify, but an inability to materialise the region a specification induces."
- **Omission asymmetry:** "The dominant error is omission, which resists audit: an over-inclusion is a token a
  reviewer can challenge, a missing member an absence whose discovery is the authoring problem itself. Models detect
  planted over-inclusions 6-7x more often than planted omissions"; a production deployment of 43,227 items "fails
  omission-first at 10:1". Observation 2: "Omission is witness-blind to local review".
- **Reasoning:** with test-time reasoning, the algorithmic gap closes for GPT-5.1 (+0.259 to +0.008) — "reasoning
  closes it, where a rule can be executed" — but "on test suites the escape is unreliable" (Opus gap +0.274 to
  +0.096; GPT-5.1 no improvement).
- **Limitations:** headline scope is one-shot greedy authoring without test-time reasoning; complete-truth lists are
  15 words; gating/repair need known-correct references.
