---
id: story-rp-orphan-conformance-fixtures
kind: story
stage: implementing
tags: [research-pipeline, cleanup]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-20
updated: 2026-10-20
---

# Remove orphaned research-pipeline conformance fixtures

## Brief

`plugins/research-pipeline/scripts/conformance/` (10 tracked files: `analysis/`,
`attestation/`, `briefs/`) has no runner, README or reference anywhere in the repo.
It is an older subset of `plugins/agentic-research/ard-core/kernel/conformance/`,
last touched by `88775f35` ("refactor: remove duplicate ARD implementation"),
which appears to have left the fixtures behind. Found while implementing
`feature-version-matcher-shape`. Confirm nothing external consumes it, then delete.

Scoped 2026-10-20 from backlog `idea-rp-orphan-conformance-fixtures` at Andrew's direction (housekeeping during the Codex
validation run). It merges via PR. Version bumps and install updates wait until that run ends.
