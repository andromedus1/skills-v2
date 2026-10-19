---
source_handle: upstream-work-conventions
fetched: 2026-10-19
source_url: https://github.com/nklisch/skills/blob/638867b65e35057518865e0ece29e980468b0a94/.work/CONVENTIONS.md
provenance: source-direct
substrate_confidence: source-direct
acquisition: local Git object via the upstream remote (git show 638867b6:.work/CONVENTIONS.md, frontmatter and first sections); release summary 638867b6:.work/releases/workbench-0.17.1.md
---

# nklisch/skills own .work/CONVENTIONS.md at 638867b6

## Anchored passages

- Frontmatter: `owner: workbench`, `workbench_version: 0.26.11`,
  `completed_items: discard`, `review_weight: standard`,
  `simplification_posture: balanced`, `autonomy: collaborative`,
  `commit_posture: feature`, `release_gates: [channel-parity,
  metadata-integrity]`.
- "## Overbuilding calibration" — "Likely overbuilding: Duplicated
  host-specific workflow prose, generic registries or adapters, receipts and
  counters, exhaustive validators, and compatibility shims for project-owned
  surfaces—especially guards without a named threat or capability."
  "Justified complexity: Channel-parity adapters and checks, deterministic
  structural validation, and machinery protecting a real invariant, external
  consumer, or documented failure."
- "## Review approach": "Prefer adaptive, coherent implementation reviews
  across features or deliveries when context reuse and integration
  visibility outweigh delayed feedback."
- Delivery: "Completed items are **discarded** after verification; git
  history is the audit trail."
- Release workbench-0.17.1 verification: "Channel parity passed";
  "the bump script advances them and the dogfood Workbench stamp together".
