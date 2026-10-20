---
id: idea-rp-orphan-conformance-fixtures
created: 2026-10-19
updated: 2026-10-19
tags: [research-pipeline, cleanup]
---

# Remove orphaned conformance fixtures under research-pipeline

`plugins/research-pipeline/scripts/conformance/` (10 tracked files: `analysis/`,
`attestation/`, `briefs/`) has no runner, README or reference anywhere in the repo.
It is an older subset of `plugins/agentic-research/ard-core/kernel/conformance/`,
last touched by `88775f35` ("refactor: remove duplicate ARD implementation"),
which appears to have left the fixtures behind. Found while implementing
`feature-version-matcher-shape`. Confirm nothing external consumes it, then delete.
