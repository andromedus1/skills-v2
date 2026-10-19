---
name: doc-review
description: >
  Review core planning documents for consistency, completeness, and alignment. Uses cascading
  passes: system-level first, then system + each module. Verifies docs match code and the
  .work substrate: active-item decisions, cited research, and delivered files. Writes report to disk.
  Run after major design changes, before starting a new epic, or at quality checkpoints.
  Use when user says "review docs", "check consistency", "audit planning docs", or "are our docs up to date".
---

# Doc Review

You audit a project's foundation and planning documents for consistency, completeness, and
alignment with each other, with the `.work/` substrate, and with the codebase. You find the
drift between what was decided and what is documented.

**You follow the build process at `${PLUGIN_ROOT:-${CLAUDE_PLUGIN_ROOT}}/docs/build-process.md`.** Read it before starting.

Boundary: `agile-workflow:gate-docs` checks one release bundle's changes for drift;
doc-review audits the whole corpus regardless of what changed.

## Arguments

- No arguments: full cascading review (system-level + each module)
- Module name (e.g. `brief`): system-level + that module only
- `--system-only`: system-level docs only, skip module passes

## Model Assignment

Per [model-selection-pattern.md](../../docs/model-selection-pattern.md):

- **Reviewer (this skill's main loop)** — Orchestration at the host quality-first tier with high reasoning. Runs in parent context.
- **Cascading review passes** — Parallel worker at the balanced host-native tier with medium reasoning. Spawned one per pass (system-level + one per module) in Phase 2.

Cross-doc consistency judgment sits in the quality-first orchestrator, which must catch subtle contradictions. Each pass is scoped to one doc set and parallelizable, where the balanced host-native tier is sufficient.

---

## Phase 1: Discover Documents

**Step 1: Record the baseline.** Note `git rev-parse HEAD` and whether the working tree
has uncommitted changes (list their paths). This is the report's `Baseline`.

**Step 2: Find foundation docs.**

1. If `.work/CONVENTIONS.md` declares `foundation_docs:`, every listed path is system-level.
2. Read `docs/knowledge-index.yaml` (detail in `docs/knowledge-index-detail.yaml`) and add
   every entry that is not a research artifact (research types below, or paths under
   `.research/`). If no index exists, flag **Info**: "No knowledge index. Using directory
   scan. Consider running `research-pipeline:knowledge-index`."
3. Always include root instruction files (`AGENTS.md`, `CLAUDE.md`, `.claude/CLAUDE.md`).
4. Fallback when neither source exists: `docs/VISION.md`, `docs/SPEC.md`,
   `docs/ARCHITECTURE.md`, `docs/architecture/`, `docs/*/architecture/`.

A legacy roadmap-style file is reviewed as an ordinary foundation doc; delivery state is
read from `.work/`, not from docs. Briefs and research artifacts are not audited for
structure here — `research-pipeline:knowledge-index` lint and the citation gate own that.

**Step 3: Load the substrate.** If `.work/` exists, list active items with
`.work/bin/work-view --kind <epic|feature|story> --paths` (or glob `.work/active/`), and
done items with `--scope archive --paths` plus active items at `stage: done`. No `.work/`
→ skip checks 2b–2d and flag **Info**.

**Step 4: Discover modules dynamically.** A module is a unit with its own planning docs:
non-system `north-star` index entries, `docs/*/architecture/` sets, or package/plugin
directories carrying their own docs. Each discovered module gets its own pass. No
hardcoded module list.

**Step 5: Verify frontmatter compliance** on discovered docs under `docs/` (exempt:
instruction files, READMEs, plugin-shipped docs, and `.work/` items, whose schema the
substrate owns):

```yaml
---
description: One-line summary
type: <a type research-pipeline:knowledge-index accepts>
updated: YYYY-MM-DD
research_method: /brief | /research | /deep-research | /research-program | hand-written | migrated
---
```

- No frontmatter, or missing `description`, `type` or `updated` → **Medium** (the index
  falls back to inference). `updated` more than a year old → **Low**.
- `research_method` missing on research types (`brief`, `campaign-parent`,
  `campaign-report`, `program-parent`, `program-report`) → **Low**; backfill `migrated`
  if the origin is unknown. Informational only for other types.

**Present the inventory:** "Found N system-level docs, M module docs across K modules,
A active and D done work items. Frontmatter compliance: X/total. Running cascading review."

---

## Phase 2: Cascading Review Passes

Launch each pass as a parallel host-native sub-agent at medium reasoning.

### Pass 1: System-Level Consistency

**Scope:** system-level docs plus the substrate items loaded in Step 3.

#### 2a. Document ownership
- Content in the wrong doc? (Architecture in the vision; delivery status, decomposition
  or task lists in foundation docs — those belong in `.work/` items)
- Duplicated content across docs?
- Missing content? (Decision made but not documented)

#### 2b. Foundation vs active work
For each active, not-done item's recorded decisions (`## Design decisions`,
`## Architectural choice`, operator-decision notes), check whether a foundation doc
asserts the opposite.
- Direct contradiction with an item at `implementing` or `review` → **High**; with a
  `drafting` item, or an indirect/partial conflict → **Medium**.
- The item's own scope rolls that doc forward → **Info** ("pending roll-forward by <id>").
- Otherwise always an operator decision: either the doc or the item is wrong, and only
  the operator can say which.

#### 2c. Research refs exist
For each active item, every `research_refs:` entry and every research path its body
cites as evidence (`.research/…`, `docs/research/…`, briefs) must resolve on disk. Path
patterns, placeholders and mentions of legacy locations are not citations.
- Missing → **High**. If the item is tagged `[needs-brief]` or `[needs-research]` at
  `drafting`, the research is expected but unwritten → **Info**.
- If the target moved (one unambiguous match by filename, or `git log --follow`), the
  fix is a mechanical path update.

#### 2d. Done-item claims
For each done item (archive or `stage: done`), files its implementation notes or
"Files"/"Delivered" sections name as delivered must exist. Resolve plugin- or
package-relative paths first; alternatives the item merely discussed are not claims.
- Renamed per `git log --follow` → **Info** (the record was true when written).
- Deleted with a later commit or item explaining the removal → clean.
- Missing with no explanation → **Critical**, operator decision (reopen, or record the
  removal). Never edit done or archived items autonomously.

#### 2e. Decision consistency
- Locked decisions stated the same in every doc?
- Architecture matches the vision's domain model?
- Open questions: resolved in one doc but still open in another?

#### 2f. Cross-reference integrity
- Every doc-to-doc reference and link target exists? (Use Glob to verify)
- Knowledge index matches actual docs on disk? (If index exists)
- "Related docs" sections current?

#### 2g. Schema consistency
- Interfaces, data schemas and field specs identical everywhere they appear?
- Frontmatter field specs identical where defined?

#### 2h. Staleness
- Old file paths after reorganization?
- Old identifiers after renaming (skills, item ids, section numbers)?
- "Deferred" items that are now implemented?
- References to renamed or superseded tools or concepts?

**What is NOT staleness (do not flag):** concrete deployment values (project IDs, bucket
names, endpoints), module names in examples, version numbers matching what is deployed.

#### 2i. Provenance summary (research_method)

Aggregate `research_method` across research-type docs. For each value, count docs and report
the latest `updated` date. Identify the highest-fidelity tool used in the corpus (precedence:
`/research-program` > `/deep-research` > `/research` > `/brief` > `hand-written`/`migrated`).
Docs produced by a lower tool and `updated` before the latest higher-tool doc are **refresh
candidates**: list the top 10 by tag overlap with recent higher-tier seeds. Informational,
not a finding. Skip the section when there are none.

### Pass 2+: System + Module (one pass per discovered module)

- **Vision:** module vision aligns with the system vision and cites system principles correctly.
- **Architecture:** module architecture matches what system docs say about it, including
  cross-cutting systems it participates in.
- **Work:** module scope matches active epics/features touching it; nothing the module
  doc calls in scope is contradicted by an item decision (same severity rule as 2b).
- **Internal:** scope, interface and capability tables agree; field specs match the
  system-level spec.

---

## Phase 3: Compile Report & Write to Disk

Collect all pass findings. Deduplicate. Classify by severity:

| Severity | Meaning | Examples |
|----------|---------|---------|
| **Critical** | Active contradiction, or a delivery claim false on disk | Two foundation docs assert opposite decisions. A done item's delivered file is missing with no explanation. |
| **High** | Content that could mislead a builder | Foundation doc contradicts an in-flight item's decision. An active item's research ref is missing. Required link target missing. |
| **Medium** | Stale content that is technically wrong | Old path or identifier. Deferred item now implemented. Missing frontmatter. |
| **Low** | Minor inconsistency | Missing related-docs entry. Typo in an interface. |
| **Info** | Observation | No knowledge index. Orphaned doc. Expected-but-unwritten research on a drafting item. |

Mark each Critical/High finding **mechanical** (fixable without judgment: broken or stale
references, moved paths, link targets, frontmatter fields, index regeneration) or
**operator** (any contradiction between docs, or between a doc and an item decision; any
false done-item claim).

**Write the report to disk:** `doc-review-report.md` in the project root.

```markdown
# Doc Review Report

**Project:** {project name}
**Date:** {date}
**Baseline:** {commit}{ + uncommitted: paths, if any}
**Iteration:** {N} of 5
**Capped:** {yes|no}
**Documents reviewed:** {count} ({system} system + {module} module); work items: {active} active, {done} done
**Passes run:** {count} (1 system + {N} module passes)
**Issues found:** {count by severity}; residual Critical/High: {c}/{h} ({k} need operator decision)

## Operator decisions needed
| # | Severity | Files / items | Conflict | Options |
|---|----------|---------------|----------|---------|

## Pass 1: System-Level

### Critical ({n})
#### {Issue title}
**Files:** {file1} vs {file2 or item id}
**What:** {description}
**Class:** mechanical | operator
**Fix:** {what should change where, or "operator decision #k"}

### High ({n})
...

## Pass 2: System + {Module Name}
...

## Work-Item Checks
| Item | Check | Reference | Exists / consistent? | Finding |
|------|-------|-----------|----------------------|---------|
| {id} | 2b / 2c / 2d | {decision, path or ref} | Yes/No | {severity + title, or clean} |

## Fixes Applied
- {iteration}: {path} — {mechanical change}

## Clean Areas
- {What is consistent — give credit}

## Provenance Summary
| research_method | Docs | Latest updated |
|-----------------|------|----------------|
| {value or (missing)} | {n} | {date} |

### Refresh Candidates
| Slug | research_method | Updated | Note |
|------|-----------------|---------|------|
```

`Iteration` is the number of fix iterations run (0 when the first audit is clean).
`Capped: yes` means the cap was reached with mechanical Critical/High findings still open.
Residual Critical/High counts include operator findings; quality-checkpoint reads them as
blocking regardless of `Capped`.

---

## Phase 4: Present & Auto-Fix Loop

Present the initial report: counts by severity, the top 3 fixes, the operator decisions
list, and which passes found the most.

**No mid-loop confirmation.** Invoking doc-review is consent to fix **mechanical**
Critical and High findings autonomously. It is never consent to resolve a contradiction:
operator findings stay in "Operator decisions needed" and are never edited away, even when
one side looks obviously right. Do not ask between iterations.

### Auto-Fix Loop

Iterate, with a hard cap of **5 iterations**:

1. Fix every mechanical Critical and High finding from the current report.
2. **Dispatch a fresh host-native reviewer at high reasoning to re-run the full review (Phase 2 in full — all system passes + every module pass).** This is a REQUIRED Agent dispatch step, not an optional re-check. Do not re-run "affected" passes only — a fix in one pass can introduce findings in another, and partial re-runs miss those.
3. The dispatched audit Agent compiles a fresh structured report with severity counts and classes.
4. **Exit decision is read from the dispatched audit's structured report.** If it has no mechanical Critical or High findings → loop is done (`Capped: no`); any operator Critical/High remain as residuals. The orchestrator does NOT make the exit call from its own assessment.
5. **Cap hit:** if iteration 5 ends with mechanical Critical or High findings remaining → stop, set `Capped: yes`, and emit: `"Hit max iterations (5). N Critical / M High remain — manual investigation needed."`
6. Otherwise → start another iteration.

Update the report's header fields from the final dispatched audit and continue to Phase 5.

**The loop bar is Critical + High only.** Medium / Low / Info findings are listed in every report but never trigger another iteration and are never auto-fixed.

**Why the loop exists.** Findings cluster: fixing one stale path often turns up two more once the surrounding doc is re-scanned. The loop runs until the corpus has no mechanically fixable C/H left, or signals that it cannot get there autonomously.

### Mandatory: re-audit before exit

The exit condition MUST be confirmed by a fresh full audit pass — NOT by manual grep, spot-check, or "verification." Fixing one finding can introduce another in a different file; manual verification cannot catch what it did not think to look for.

**These do NOT count as a re-audit and MUST NOT trigger exit:**
- Manual grep of the patterns the previous audit flagged
- Spot-check or sampling of the edited files
- The orchestrator's own confidence that fixes were complete
- Reading back changed sections to confirm intent
- Token-economy or session-budget concerns about running another audit

If the prior iteration applied any fix, run a fresh audit. Period.

## Phase 5: Regenerate Knowledge Index

After fixing any issues, **run `research-pipeline:knowledge-index`** to regenerate the index
from frontmatter. The index is fully derived; moves, renames, deletions and frontmatter
changes the loop made are picked up automatically.

Do NOT hand-edit `docs/knowledge-index*.yaml`. If the regenerator's lint surfaces issues,
fix them in the source frontmatter and re-run. Skip this phase if the project does not use
the knowledge index.

---

## When to Run This Skill

- **After major design changes** — new architecture decisions, new modules, restructured docs
- **Before starting a new epic** — verify foundation docs agree with the work about to be designed
- **At quality checkpoints** — first check in `research-pipeline:quality-checkpoint` (docs before code)
- **After `research-pipeline:update-documentation`** — verify automated updates did not introduce inconsistencies
- **When adding a new module** — verify it is integrated with system-level docs

## Anti-Patterns

- **Don't review everything in one flat pass.** Cascading catches module-vs-system drift.
- **Don't just check docs against docs.** Verify against `.work/` and the codebase too (2b–2d).
- **Don't resolve contradictions.** Route them to "Operator decisions needed"; some inconsistencies are intentional and only the operator knows which side is current.
- **Don't edit done or archived items.** They are history; report false claims instead.
- **Don't flag concrete deployment values as staleness.**
- **Don't skip module passes.** Module drift is where the worst issues hide.
- **Don't forget to write the report file.** It is a project artifact that quality-checkpoint consumes.
- **Don't substitute manual verification for a full audit re-run**, and don't skip it for token economy. The audit's independent re-scan is its load-bearing value.
