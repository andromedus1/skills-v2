---
id: story-bootstrap-project-knowledge-index
kind: story
stage: review
tags: [prose, knowledge-index, research-pipeline]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-18
updated: 2026-10-18
---

# Bootstrap this repository's generated knowledge index

## Brief

Andrew requested the missing knowledge navigator while clarifying that the
Workbench-oriented foundation documents are inherited upstream references and
that methodology-review should remain local for iteration. The existing generator
finds 13 documents but omits them from its outputs because they lack frontmatter.

Add indexing metadata to those documents, preserve their bodies, and add a short
fork navigation guide pointing to the current authorities and plugin entrypoints.
Generate all three knowledge-index layers with the existing Research Pipeline
generator. Keep this work local; no publication, version bump, installed-cache
change, or methodology-review behavior change is commissioned.

## Acceptance

- All existing documents under docs/ and the new navigation guide appear in the
  generated index with useful descriptions and summaries.
- Navigation distinguishes upstream references and deprecated material from the
  fork's current instructions without rewriting inherited document bodies.
- The guide links to Research Pipeline, Agentic Research, methodology-review,
  and the work substrate; plugin internals remain owned by their source docs.
- Generated files pass lint and the navigator fits the session hook's size budget.
- SessionStart discovery works from the repository and a nested directory.

## Simplification opportunity

Use the existing generator and hook. Add source metadata and links instead of
introducing a second indexer, copying plugin documentation, or hand-maintaining
generated files.

## Delivery

- Execution: inline; one cohesive documentation and generation task.
- Review: standard bounded standalone-story review, without an independent reviewer.
- Dependencies: none; scope does not alter the methodology-review feature.

## Implementation notes

- Added source frontmatter to all 13 existing docs and a high-priority
  docs/project-navigation.md linking the fork's authorities and plugin entrypoints.
- Preserved all 13 original document bodies byte for byte, including example dates.
- Marked the deprecated Workflow guide and obsolete in-tree npm publishing research
  as historical. Labeled inherited foundations as upstream context; research metadata
  does not claim a new external-source verification.
- Generated docs/knowledge-index-nav.yaml, docs/knowledge-index.yaml and
  docs/knowledge-index-detail.yaml using the existing generator in an isolated
  PyYAML environment. No generator, hook or skill behavior changed.
- Execution capability: inline host; mechanical metadata and bounded prose scope.
- Review weight: standard standalone-story lane, as recorded at scope time.
- Tests added/removed: none; direct corpus checks and existing hook tests cover the
  generated outputs and session integration without duplicating implementation.
- Simplification: retained the existing generation and hook paths; linked plugin
  authorities instead of copying their contracts or adding scan-root configuration.
- Design discrepancies: none. The existing generator indexes docs and research,
  not every plugin tree; the navigation guide makes that coverage explicit.
- Adjacent work: no additional work items created.

## Verification

- Generation: 14 documents, 8 planning / 4 research / 2 historical; zero lint errors
  and warnings. Navigator approximately 2 KB, below the 9,800-byte hook threshold.
- Corpus parity: every docs/**/*.md appears once in the full index and has a detail
  entry; the fork guide is the sole explicitly high-priority navigation entry.
- Every new Markdown link and emitted relationship target resolves.
- Compared original bodies against scope commit 0aa97f3e; all 13 are unchanged.
- Repository and installed Codex-cache navigator scripts both emit this navigator
  from the repo root and a nested plugin directory, within the full output budget.
- Existing session-context hook suite passes; Git whitespace check passes.
- Hook scripts were exercised directly. No fresh live model session or external
  research refresh is claimed by this story.
