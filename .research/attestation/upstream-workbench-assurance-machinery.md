---
source_handle: upstream-workbench-assurance-machinery
fetched: 2026-10-19
source_url: https://github.com/nklisch/skills/blob/638867b65e35057518865e0ece29e980468b0a94/plugins/workbench/skills/work/references/assurance-machinery.md
provenance: source-direct
substrate_confidence: source-direct
acquisition: local Git object via the upstream remote (73 lines, read in full); commit messages 7a963fc9 and 1160aed2
---

# Workbench assurance-machinery reference (machinery forecast)

## Anchored passages

- "Treat machinery for correctness, accounting, verification, state
  management, and determinism as a costed design choice, not an automatic
  mark of rigor."
- Forecast trigger: a component "that owns changing state, publishes results
  others read, records history, recovers from failure, or keeps unfinished
  work alive across calls"; not "for routine local choices inside an accepted
  authority chain".
- Method: "Show the user the minimum coherent chain and the proposed chain in
  plain language"; "Keep the forecast conversational. Do not create an
  artifact, fixed packet, or new gate for it".
- Be skeptical of: "parallel ledgers, receipts, status files, caches, or
  indexes that require reconciliation with the thing they describe";
  "bespoke validators and test harnesses built mainly to police
  agent-generated bookkeeping rather than user-visible behavior or a real
  external contract"; "issue-specific rules promoted into universal
  constraints, migrations, and lifecycle states after one failure".
- Earned when "reproducibility, financial or regulatory traceability, data
  integrity, concurrency, irreversible effects, or a genuine external
  contract requires them". "This lens never waives correctness".
- 1160aed2 (2026-09-25): "Make the machinery forecast a proactive design
  step" — "one user action and the failure to prevent, three questions, the
  simplest working chain beside the proposed one, and a recommendation".
