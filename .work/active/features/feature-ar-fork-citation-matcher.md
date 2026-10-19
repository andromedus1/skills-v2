---
id: feature-ar-fork-citation-matcher
kind: feature
stage: drafting
tags: [agentic-research, methodology-review]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Fork-owned agentic-research: anchor-aware version-number matcher

## Brief

Andrew decided on 2026-10-19 that the fork owns `agentic-research` going forward
(see `feature-claude-methodology-repeat`, "Operator decisions — follow-ups").
First change: QVC-S/METH-001's version-number matcher in
`plugins/agentic-research/ard-core/kernel/lint-citations.py`.

- Suppress version-number advisories in `source-direct` attestations (tier
  suppression, matching CATALOGS §3 "without an in-corpus anchor").
- On analytical lines with resolved citations, suppress only when a cited
  attestation contains the matched version token (experiment variant B).
- Add positive and negative conformance fixtures that distinguish current,
  blanket-citation and token-aware behavior (modeled on the scratch experiment's
  labeled fixtures; see the controller's experiment section).
- Roll forward ownership statements in `AGENTS.md` and
  `docs/project-navigation.md`; keep catalogs/docs consistent with the kernel.

Evidence: scratch experiment (fixture precision 0.40 → 0.84, recall 0.90 →
0.80; real-corpus flags 174 → 60, with 112 attestation flags removed and no
observed recall loss). Synthetic fixtures; not field measurement.

Out of scope: matcher-shape changes (case-insensitive `version`, dotless `vN`,
section refs, arXiv IDs) unless design shows they are cheap and tested; other
kernel rules.

## Simplification opportunity

The gate-citations version-advisory caveat prose may shrink once the matcher
stops flagging attestation metadata.
