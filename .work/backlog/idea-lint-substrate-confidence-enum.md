---
id: idea-lint-substrate-confidence-enum
created: 2026-10-20
updated: 2026-10-20
tags: [agentic-research]
---

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
