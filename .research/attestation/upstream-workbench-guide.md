---
source_handle: upstream-workbench-guide
fetched: 2026-10-19
source_url: https://github.com/nklisch/skills/blob/638867b65e35057518865e0ece29e980468b0a94/docs/workbench-guide.md
provenance: source-direct
substrate_confidence: source-direct
acquisition: local Git object via the upstream remote (git show 638867b6:docs/workbench-guide.md; 824 lines, read in full)
---

# Workbench Guide (docs/workbench-guide.md at 638867b6)

## Structure and scope

User-facing how-to for adopting Workbench and steering it: install, setup,
plain-language requests, design contracts, pattern maintenance, commit
posture, execution posture, model assignment, autonomy/simplification/review
weights, research, scan, ledger maintenance, custom validator, release gates.

## Anchored passages

- Coexistence: "Workbench and `agile-workflow` use mutually exclusive
  `.work/` schemas — do not run both as workflow owners in one repository.
  Workbench's `setup` consolidates an existing agile-workflow substrate".
  The guide calls agile-workflow "the maintenance-mode alternative".
- Activation: stateful skills are "installed but inactive"; "Repository
  detection, drift, or another skill's recommendation is not consent."
  "Workbench has no session hook."
- Overbuilding calibration: a "concise, user-confirmed `## Overbuilding
  calibration` in `.work/CONVENTIONS.md`: project context, likely
  overbuilding, justified complexity, optionally where cost is felt, and
  reasons to revisit it. Every design and review applies this lens".
- Core defaults table: `autonomy` (collaborative/adaptive/autonomous);
  `review_weight` (none/light/standard/thorough/maximum; standard = "exactly
  one proportionate pass ... corrections are verified, not re-reviewed");
  `simplification_posture` (hygiene/balanced/structural);
  `completed_items` (summarize/discard).
- Design contracts: "The work item is the contract between design, review,
  and implementation"; dense contracts may use
  `.work/attachments/<item-id>/contract.md`; "Attachments are always deleted
  when their owning item completes".
- Commit before handing back: "The default last repository-writing action is
  a commit"; "Reviewers inspect named commits rather than a working tree";
  "Local commits do not authorize publishing."
- Execution: "With no execution preference, Workbench keeps design,
  implementation, corrections, and supporting discovery inline"; values
  `inline`, `inline-first`, `adaptive`, `orchestrated`.
- Models: "Before any task requiring multiple sub-agents, the agent discovers
  available models and aligns models and thinking levels with you in chat";
  optional `.work/MODEL-NOTES.md`; "No model rankings are seeded during
  setup."
- Review: "Review is not verification"; "Review cannot expand scope";
  reviewers "also flag overbuilding relative to the project's actual type and
  risks"; "If you request an independent or cross-model reviewer and none is
  reachable, the agent asks how to proceed."
- Review boundaries: "Small implementation units can share a larger
  review-and-fix pass"; "A shared pass replaces per-feature passes rather
  than adding to them."
- Research: bundled provider rigor dial "`floor` ..., `standard` adds a
  semantic source-support pass, `full` adds an isolated check ..., and
  `adaptive` chooses proportionately".
- Ledger: "Splitting an item does not reduce its commitment"; custom
  `validator_command` in conventions frontmatter.
- Release gates: opt-in `release_gates` names select scan lenses; "Only
  unresolved findings that materially violate the project's stated
  expectation block release completion."
- Knowledge index: optional `.knowledge/index-exclusions.txt` of
  repository-relative prefixes.
