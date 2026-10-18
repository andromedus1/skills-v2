---
id: story-bootstrap-project-knowledge-index
kind: story
stage: implementing
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
