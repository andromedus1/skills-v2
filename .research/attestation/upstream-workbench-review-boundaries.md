---
source_handle: upstream-workbench-review-boundaries
fetched: 2026-10-19
source_url: https://github.com/nklisch/skills/blob/638867b65e35057518865e0ece29e980468b0a94/plugins/workbench/skills/work/references/review-boundaries.md
provenance: source-direct
substrate_confidence: source-direct
acquisition: local Git object via the upstream remote (100 lines, read in full)
---

# Workbench review boundaries and timing reference

## Anchored passages

- "Implementation units and review targets need not match."
- Design review: "A separate design review is optional. Align the approach
  with the user once for the current run: no separate pass, focused review of
  selected decisions, or a broader design review." "Never infer design review
  merely from a design heading or a high implementation review weight."
- "Prefer shared reviews when context reuse and integration visibility
  outweigh delayed feedback. Split or review earlier when hidden coupling,
  high consequence, growing uncertainty, or reviewer context limits would make
  a larger pass weaker."
- "A shared pass satisfies the included items' review obligation without
  duplicate per-item passes." "At `standard`, do not send each corrected
  feature through review again."
- "No new batch object, status, receipt, or coordination feature is needed
  just to remember a review." "Never mark a feature done while its required
  review remains deferred."
- Conventions should be "ordinary convention prose, not new frontmatter
  fields or numeric quotas".
