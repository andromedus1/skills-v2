---
id: feature-qvc-minor-remedies
kind: feature
stage: drafting
tags: [methodology-review, research-pipeline, cleanup]
parent: null
depends_on: [feature-qvc-review-receipts]
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# QVC minor remedies: citation gate, doc-review, consolidation, hygiene

## Brief

Fork-only bundle of minor QVC findings accepted by Andrew on 2026-10-19 — see
`feature-claude-methodology-repeat`, "Operator decisions — round 1 packet".
Depends on `feature-qvc-review-receipts` because consolidation touches the same
review-reuse text.

1. **Citation gate tidy-up** (QVC-S/METH-002, QVC-S/METH-003, gate-citations
   incidentals): run the gate with `--exit-code-on` matching its blocking
   policy while keeping the JSON-validity check; one reporting line for
   `campaign_unbound` and `substrate_confidence_omitted` counts (warn-only, no
   items); fix status lists, example paths and the version-advisory caveat.
   The canonical kernel stays unchanged.
2. **doc-review state and scope** (QVC-E/METH-003, QVC-E/METH-004): add
   baseline, iteration and capped fields to its report; limit autonomous fixes
   to mechanical classes and route foundation-doc contradictions to the
   operator; retarget checks that assume the retired roadmap pattern.
3. **Consolidate duplicate rules** (QVC-E/METH-002, QVC-R/METH-004): one
   canonical fork statement of the completion-evidence and review-reuse rules
   with one-line local pointers; drop `research-composition` restatements; weigh
   choices by burden on domain methodology reviews (operator criterion).
4. **Repo hygiene** (QVC incidentals): declare PyYAML for tests; branch guard
   in `bump-version.sh`; fix stale "Cross-Model Advisory Review policy" and
   `peer-review` references in RP feature/epic-design; document the
   `models.md` fork patch in `docs/project-navigation.md`.

Out of scope: matcher changes (QVC-S/METH-001 awaits its experiment), upstream
agile-workflow edits, and new review passes.

## Simplification opportunity

Item 3 is itself a simplification; prefer deleting restatements over rewording them.
