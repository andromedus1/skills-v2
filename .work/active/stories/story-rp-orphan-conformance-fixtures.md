---
id: story-rp-orphan-conformance-fixtures
kind: story
stage: review
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

## Implementation (2026-10-20)

Removed `plugins/research-pipeline/scripts/conformance/` (10 files).

**Checks before removal:**
- `git grep` finds no reference outside the directory, the backlog note and research artifacts.
- No CI workflow mentions it.
- 9 of the 10 files are byte-identical to `plugins/agentic-research/ard-core/kernel/conformance/`;
  `briefs/brief.md` is an older variant.
- The canonical fixtures and their runner live in agentic-research.

**Verification:** research-pipeline `skill-portability` and `resolve-agentic-research` pass.
