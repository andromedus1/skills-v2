---
source_handle: claude-plugin-dependencies
fetched: 2026-10-18
source_url: https://code.claude.com/docs/en/plugins/dependencies
provenance: source-direct
substrate_confidence: source-direct
---

# Plugin dependencies

## Anchored summary

“Declare dependencies” documents automatic same-marketplace dependencies directly
in a plugin manifest, optionally version-constrained. “Bundle plugins for a team”
describes a separate aggregate plugin: “installing it installs every dependency”.

“How a constraint resolves against tags” selects matching plugin-scoped tags. For
relative-path plugins, missing matching tags fall back to marketplace contents;
an incompatible version disables the dependent plugin at load. Local `--plugin-dir`
copies bypass version checks (“Test a plugin and its dependency locally”).

## Structure

Official host documentation, not installed-client testing. HTML read successfully;
publication date not established.

## Revisions

Correction: distinguished direct dependencies from aggregate bundles and recorded
the relative-path load check and local-development exception.
