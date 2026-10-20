---
id: story-lint-substrate-confidence-enum
kind: story
stage: done
tags: [agentic-research]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-20
updated: 2026-10-20
---

# Lint: unknown substrate_confidence values and inline comments read as full-depth

## Brief

The agentic-research citation lint has two silent passes that overstate how deeply a source was engaged:

- **Unknown values count as full text.** An unknown `substrate_confidence` value (for example `abstract`, `abstract-only`, `fetched-page-extract`, `partial`) resolves as source-direct `resolved`.
- **Inline comments break the value.** An inline YAML comment after the value is read as part of the value, so the value is no longer recognised.

This is the same silent-pass class as F27.

**Where it was found.** While dogfooding the `solution-space-decomposition` campaign on 2026-10-20, 24 attestations used nonstandard values and were normalized by hand.

**Fix direction:**
- Treat any value outside the catalog enum as `unspecified` (a reduced-substrate gap), with a warning.
- Strip inline comments in `parse_frontmatter`.
- Add conformance fixtures.
- State the allowed values in the specialist brief.

Scoped 2026-10-20 from backlog `idea-lint-substrate-confidence-enum` at Andrew's direction (housekeeping during the Codex
validation run). It merges via PR. Version bumps and install updates wait until that run ends.

## Implementation (2026-10-20)

**`lint-citations.py`:**
- `parse_frontmatter` reads values through `_scalar`, which strips quotes and a trailing
  ` # comment`. A `#` without a space before it, as in a URL fragment, stays in the value.
- An unrecognised `substrate_confidence` now resolves as `reduced-substrate-attestation`, treated
  like `unspecified`, and is reported as a warning. JSON gains `substrate_confidence_unknown`.

**Conformance:** four new attestation fixtures and check group 1f, bringing the total to 139/139.
The new checks fail against the prior lint.

**Contract text updated:** CATALOGS §2 (the value list and the unknown-value rule); the attestation
schema description (adds `snippet`); and the specialist brief, which now states the allowed values
and forbids inline comments. The fork navigation note also lists the divergence.

**Verification:**
- conformance 139/139;
- lint unit tests 4/4;
- refresh-scan;
- skill-metadata;
- `gen-contract --check` in sync;
- the repo corpus has 0 unknown values.

## Review (2026-10-20, bounded inline; standalone story)

**Lenses:** correctness, regression, tests and docs.

**Correctness:**
- Quoted values containing `#` keep their content.
- Unquoted values only lose a `#` that has whitespace before it, which a valid URL never has.
- The other fields parsed the same way (`source_handle`, `source_url`, `provenance`,
  `acquisition_status`) benefit equally.
- An omitted value keeps its grace-period behaviour.

**Regression:** existing conformance groups are unchanged.

**Verdict:** approve, with no findings.
