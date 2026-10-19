---
source_handle: upstream-workbench-verification-cadence
fetched: 2026-10-19
source_url: https://github.com/nklisch/skills/blob/638867b65e35057518865e0ece29e980468b0a94/plugins/workbench/skills/work/references/verification-cadence.md
provenance: source-direct
substrate_confidence: source-direct
acquisition: local Git object via the upstream remote (153 lines, read in full); commit messages 0606c01f, 95fe1118, 4e17182a
---

# Workbench verification cadence reference

## Anchored passages

- Scope: "when several units, agents, or correction rounds deliver into one
  target. A check runs once, at the cheapest boundary that can catch what it
  protects."
- "Implementers and correction rounds run implementation-loop checks ...
  They do not run the integration gate." "Most verification waits for the
  epic boundary."
- Merges: "re-verify only what the incoming changes can affect"; "Unrelated
  upstream commits do not restart the gate."
- Merge first, gate after: "When several sessions deliver into one repository
  on one machine, they merge into a local integration branch first, and the
  long gates run afterwards on its newest head." "One gate runner per
  repository"; "Green publishes that head to the shared remote"; "Red bisects
  the first-parent merges since the last green"; "An item closes only after a
  green gate on a head that contains its merge." "Ledger-only changes (work
  items and docs) need no gate."
- "A check that cannot fail is not a gate."
- Timing: "Timing is never a unit, merge, or integration check."
- Delegated units: "A delegated implementer, reviewer, or checker never
  deletes a worktree, branch, or build folder it did not create"; returned
  evidence is "the verdict, the commit, and one log path".
- 0606c01f message (2026-10-01) adds: "Design reviews of concurrency protocols
  stop after two rounds unless failures are hangs, crashes or corruption".
