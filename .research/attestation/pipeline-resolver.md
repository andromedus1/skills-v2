---
source_handle: pipeline-resolver
fetched: 2026-10-18
source_path: plugins/research-pipeline/scripts/resolve-agentic-research.sh
provenance: source-direct
substrate_confidence: source-direct
---

# Companion-plugin resolver

## Structure and behavior

The shell script resolves an explicit `AGENTIC_RESEARCH_PLUGIN_ROOT` first,
then a sibling `agentic-research` directory, then configured and default Claude
and Codex cache roots. `is_agentic_root` checks for a citation-linter file and
Claude manifest; it does not parse the manifest version or an activation registry.
An invalid explicit root fails immediately. Missing companions produce an error
and an installation/environment-variable instruction.

## Anchored passages

In the `for root in $search_roots` loop, `find` results pass through
`LC_ALL=C sort | tail -n 1`. Later matching search roots overwrite `match`.
This is lexical path selection. The script has no semantic-version comparison
or declared compatibility-range check. The explicit-root and sibling branches
exit before this fallback, so the fallback does not describe every invocation.

The machine observation record preserves the script hash at fetch time. Git
baseline 15893074 contains the inspected implementation.
