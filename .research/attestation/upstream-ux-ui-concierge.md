---
source_handle: upstream-ux-ui-concierge
fetched: 2026-10-19
source_url: https://github.com/nklisch/skills/commit/2e812a1c34279071381fe3395c2e747ef33dc26a
provenance: source-direct
substrate_confidence: source-direct
acquisition: local Git objects via the upstream remote (git show 2e812a1c; 2e812a1c:.work/active/feature-ux-ui-concierge.md; 638867b6:.work/releases/ux-ui-design-1.0.0.md)
---

# ux-ui-design concierge restructure (2e812a1c, release 1.0.0)

## Structure and scope

Commit message, feature item `feature-ux-ui-concierge` (closed by b1360477)
and release summary `.work/releases/ux-ui-design-1.0.0.md` (released
2026-08-25). Plugin diff: 49 files, +1311/−10008.

## Anchored passages

- Message: "Replace the seven pipeline skills (ux-ui-principles, palette,
  components, motion, screens, flows, adopt) with one interview-first
  concierge skill." Reference library "consolidates twenty files into nine";
  "tier ordering, the AGENTS.md auto-installer, pipeline enforcement, and
  fixed option counts are dropped". "agile-workflow callers (scope,
  epic-design, feature-design, ideate) are semantically rewritten".
- Item, risks: "Trigger regression (one description replacing seven)";
  "Users lose old determinism — intentional, major-version-signaled".
  Design revision: "Independent review (Sol, standard weight) returned 4
  material findings; the user redirected twice mid-implementation"; library
  "shrinks 20 → 9 files (~4,700 → ~1,400 lines)".
- Release: "**Breaking:** the
  `/ux-ui-design:{palette,components,motion,screens,flows,adopt}`
  invocations are gone"; "The `.mockups/` layout and tech conventions are
  unchanged"; "agile-workflow 0.16.16 ships the matching caller updates".
  Verification: "Design and implementation each received one independent
  cross-model review at standard weight".
- Evidence of use after release: the record contains delivery verification
  only; no later upstream commit in the range changes the plugin except its
  version bump (3fd8f183).
