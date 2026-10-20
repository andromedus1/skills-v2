---
id: feature-methodology-review-pilot-learnings-primer
kind: story
stage: done
tags: [methodology-review, research-pipeline, prose]
parent: feature-methodology-review-pilot-learnings
depends_on: [feature-methodology-review-pilot-learnings-strategy-research]
release_binding: null
gate_origin: null
created: 2026-10-20
updated: 2026-10-20
---

# Surfacing-alternatives primer

## Brief
Distills the strategy-research campaign into `plugins/research-pipeline/docs/surfacing-alternatives.md`.

## Implementation
See the parent feature's Implementation Units, Unit 2.

## Implementation notes (2026-10-20)

Wrote `plugins/research-pipeline/docs/surfacing-alternatives.md`: 10 moves in three phases (Frame,
Generate, Check), a per-step table and guardrails.

**Grounding:**
- Every move traces to the verified campaign `solution-space-decomposition` (parent §1–§5).
- Each move carries its evidence level (measured, advocated or mixed) and transfer caveats.
- The docs tier carries no `[handle]{N}` citations; the primer points at the campaign parent instead.

**Alignment with the gates:** the primer was revised after each verification round so it matches the
final verified text. In particular:
- independent (blind) generation before exposure;
- the split primary signal (absent from the map versus on the map but unsampled);
- held-out known families;
- triggers matched to their remedies (map refresh, sample revision, stronger challenge);
- no statistical estimate for review challenge passes;
- the abstract-level and secondary-report qualifiers.

**Verification:** the relative-link check is clean, and the knowledge index regenerates with 0 errors
and 0 warnings.
