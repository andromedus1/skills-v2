---
source_handle: upstream-workbench-git-posture
fetched: 2026-10-19
source_url: https://github.com/nklisch/skills/blob/638867b65e35057518865e0ece29e980468b0a94/plugins/workbench/skills/work/references/git-posture.md
provenance: source-direct
substrate_confidence: source-direct
acquisition: local Git object via the upstream remote (122 lines, read in full)
---

# Workbench Git posture reference

## Anchored passages

- "A writing agent hands back committed work. This floor applies to all
  repository writes, including loose edits, design, research, setup, and
  ledger maintenance".
- Postures: `adaptive`, `feature`, `checkpoint`, `batch`, `preserve`;
  missing means `adaptive`.
- "Stronger user and repository Git/contribution rules govern where and how
  commits land. If those rules prevent a commit, disclose the exception".
- "Stage only owned changes"; "Never absorb another actor's edits to make the
  tree look clean." "A local commit never grants permission to push, merge,
  publish, or deploy."
- Preserve items before trimming: "A never-committed item needs an atomic
  commit containing its full pre-trim record ... before changing or removing
  them"; "needs no receipt, archive directory, or schema field".
- Stable review targets: "A distinct design or implementation review uses an
  identified commit or base/head range"; "Do not silently fall back to a
  working-tree review"; uncommitted inspection is "advisory feedback".
  "New commits do not themselves authorize another distinct review pass".
- "Check a merge's result ... before any follow-on step. Never pipe a merge
  into another command".
