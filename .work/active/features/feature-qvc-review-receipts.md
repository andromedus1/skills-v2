---
id: feature-qvc-review-receipts
kind: feature
stage: done
tags: [methodology-review, research-pipeline, review]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Review receipts that make covering-review reuse checkable

## Brief

Operative remedy for QVC-R/METH-002 (alias QVC-E/METH-005), accepted by Andrew
on 2026-10-19 — see `feature-claude-methodology-repeat`, "Operator decisions —
round 1 packet". Research origin:
`.research/analysis/campaigns/qvc-review-evidence/parent.md` (covering-review
reuse is a policy choice; recording what a review covered makes reuse
checkable).

Fork-only change to `.work/CONVENTIONS.md` and `research-pipeline`
`quality-checkpoint` §2: a review receipt records the reviewed `base..head`,
reviewer class and path, weight, findings, accepted-fix verification, and a
one-line coverage classification for each post-review change to a consequential
file (covered by the pass / covered by verification of a named finding /
uncovered → normal delivery). "Stale" means a post-review change with no
classification.

Out of scope: any added review pass; mandatory re-review; changes to upstream
agile-workflow templates.

## Simplification opportunity

Replace the current author-judged "materially uncovered" prose with the receipt
field where possible, rather than adding a parallel rule.

## Design decisions

- **Applies to (Andrew, 2026-10-19):** feature and epic review records in
  skills-v2 — the independent-review boundary where reuse decisions matter.
  Standalone-story inline reviews keep the existing record.
- **Legacy items (Andrew, 2026-10-19):** prospective requirement. When
  quality-checkpoint meets an earlier review without a receipt it may reconstruct
  the range from git and must label it `reconstructed`; if reconstruction is
  impossible, the evidence is missing (existing rule).
- Receipt placement (judgment): a fork block appended directly after the
  upstream `## Review (date)` record, so the upstream template stays untouched.
- Post-review classification granularity (judgment): one line per commit that
  touches a consequential path, naming its files — commits are the unit git can
  enumerate mechanically.

## Architectural choice

Options considered: (A) a convention-defined receipt block plus a git-enumerated
post-review change list, consumed by quality-checkpoint; (B) A plus a helper
script that prints the receipt skeleton and the change list; (C) A plus a test
that fails when a done feature lacks a receipt. B and C add mechanism the
operator criterion favours, but both add files outside the authorized scope
(`.work/CONVENTIONS.md` and quality-checkpoint §2), and C would need a cutoff for
legacy items. Choose **A**, keeping the enumeration mechanical by specifying one
exact `git log` command, so "stale" becomes checkable without a new tool. B/C stay
available if round-2 assessment finds receipts unreliable in practice.

The receipt replaces the author-judged "materially uncovered" bridge with an
explicit per-commit classification. It keeps the QVE rule that a changed hash
alone does not force another pass: a post-review commit is acceptable when it is
classified as covered by the pass or as a verified fix of a named finding;
unclassified consequential commits make the evidence stale; `uncovered` routes
through normal delivery. No review pass is added.

## Implementation Units

### Unit 1 (trickiest): repository receipt convention

**File**: `.work/CONVENTIONS.md` — replace the second paragraph under "Release
mapping" (the "Use `agile-workflow:review`…" paragraph) with a `### Review
receipts` subsection.

Contract (exact shape the implementer writes):

```markdown
### Review receipts

Feature and epic review records carry a receipt directly after the
`## Review (YYYY-MM-DD)` block written by `agile-workflow:review`:

**Receipt**
- Reviewed: `<base>..<head>` — product scope, with any excluded paths
- Reviewer: <model/class> via <peeragent job id | fresh-context sub-agent>; independent: yes|no
- Weight: <none|light|standard|thorough|maximum> (source: caller|convention|default)
- Findings: blockers N, important N, nits N, rejected N
- Accepted-fix verification: <commit(s)> verified by <who/how> | none required

At closure, list every later commit that touches a consequential path:

**Post-review changes** (`<head>..<closure>`)
- `<sha>` <subject> (<files>) — covered-by-pass | fix-of:<finding> verified <how> | uncovered → <item id>

Consequential paths: `plugins/*/skills/`, `plugins/*/docs/`, `plugins/*/ard-core/`,
`plugins/*/hooks/`, plugin manifests, `AGENTS.md`, `.claude/CLAUDE.md`,
`.work/CONVENTIONS.md`, `README.md`. Enumerate with
`git log --format='%h %s' <head>..<closure> -- <paths>`. An enumerated commit
without a line makes the evidence stale; `uncovered` routes through normal
delivery and review. A changed hash alone does not require another pass.
Standalone-story inline reviews keep the existing record.
```

**Implementation notes**: keep the surrounding no-CI / feature-boundary
sentences; remove the now-redundant "Record the reviewed scope, actual outcome
and correction verification" sentence (the receipt replaces it); keep "Missing,
failed or stale required evidence is not a pass…".

**Acceptance criteria**:
- [ ] The subsection defines all five receipt fields, the post-review line
      format, the consequential path set, the enumeration command and the stale
      rule, in ≤ 35 lines.
- [ ] The enumeration command runs as written in this repo (verified on a real
      range) and its output maps one-to-one to classification lines.
- [ ] No duplicated restatement of the receipt contract elsewhere in CONVENTIONS.

### Unit 2: quality-checkpoint consumes receipts

**File**: `plugins/research-pipeline/skills/quality-checkpoint/SKILL.md` §2
"Reconcile delivery-review evidence" (generic for all adopting projects).

Replace the second and third paragraphs with text that:
- names the covering-review evidence as a receipt: reviewed `base..head`,
  reviewer path/class and independence, weight, finding counts and accepted-fix
  verification, using the project's convention when it defines one;
- enumerates commits after the reviewed head that touch the project's
  consequential paths and requires each to be classified (covered by the pass /
  verified fix of a named finding / uncovered → normal delivery); an unclassified
  commit makes that evidence stale; an uncovered contract routes to delivery;
- for a review without a receipt: reconstruct the range from git and label it
  `reconstructed`, or record the evidence as missing;
- keeps: a changed hash alone does not require another pass; never describe the
  original reviewer as approving later corrections; resume from existing
  receipts; missing required review blocks readiness.

**Acceptance criteria**:
- [ ] §2 net length does not grow by more than ~6 lines; the "materially
      uncovered" judgment sentence is replaced, not supplemented.
- [ ] Frontmatter unchanged (name/description only); skill-portability test passes.
- [ ] Generic wording: no skills-v2-specific paths in the skill.

### Unit 3: forward verification (both host shapes)

No new repository files. Run three scenarios against the changed text, once with
a fresh-context Claude sub-agent and once with Codex via peeragent, giving each
only the two changed files and a scenario packet:
1. **covered_fix** — review receipt `A..B`; later commit touches a skill and is
   classified `fix-of:I-1 verified`; expect evidence current.
2. **unclassified** — a later commit touching `plugins/x/skills/` with no line;
   expect stale → not a pass.
3. **legacy** — review record without receipt, range recoverable from git;
   expect `reconstructed` label, or missing if not recoverable.

Record actual outcomes in this item. Also dogfood: this feature's own review
record carries the new receipt.

## Implementation Order

1. Unit 1 — defines the contract Unit 2 consumes.
2. Unit 2.
3. Unit 3 verification, then feature review (standard weight, Codex reviewer).

## Testing

- Structural: `plugins/research-pipeline/scripts/tests/skill-portability.test.sh`
  (with PyYAML available) passes.
- Behavioral: Unit 3 scenarios on both hosts; the enumeration command run on a
  real range (e.g. QVE's `c1827823..a2f03eaa`, which should list `6419b3bc`).
- No child stories: single-stride, tightly coupled prose change.

## Risks

- **Receipt ceremony skipped in practice** (reader compliance again): the
  receipt is still prose-enforced. — **Fallback**: round-2 assessment checks
  whether this feature's own review produced a valid receipt; if receipts prove
  unreliable, scope option B/C.
- **Path list drift** as plugins add new instruction locations. — **Fallback**:
  the list lives in one place (CONVENTIONS) and errs broad.
- **Interaction with `feature-qvc-minor-remedies` consolidation**, which will
  touch the same paragraphs. — Sequenced by `depends_on`; consolidation must
  keep the receipt subsection as the canonical statement.
- **Least sure**: whether reviewers reliably record the exact reviewed head when
  a review spans uncommitted fixes. Mitigation: the receipt's `head` must be a
  commit; reviews of dirty trees record the base commit plus "working tree" and
  are classified at closure.

## Implementation notes
- Execution capability: inline, host (Claude Opus); two-file cohesive prose
  contract change, no coordination needed.
- Review weight: standard (default; no caller or project override).
- Files changed: `.work/CONVENTIONS.md` (new `### Review receipts` subsection;
  removed the superseded "Record the reviewed scope…" sentence);
  `plugins/research-pipeline/skills/quality-checkpoint/SKILL.md` §2 (receipt
  consumption, enumeration/classification, reconstruction rule).
- Tests added/removed: none in-repo (no stable executable interface changed).
  Structural: skill-portability passes (with PyYAML). Behavioral: Unit 3
  forward scenarios on both hosts, below.
- Simplification: the author-judged "materially uncovered" bridge is replaced by
  per-commit classification; the redundant scope-recording sentence removed.
- Discrepancies from design:
  - **Pathspec bug caught in verification.** The designed command with
    directory pathspecs (`'plugins/*/skills/'`) matched nothing; git glob
    pathspecs need a trailing `*`. The convention now gives the exact command
    verbatim, verified on QVE's `c1827823..a2f03eaa` (returns `6419b3bc`) and
    `70348687..a2f03eaa` (returns `6419b3bc`, `4575547d`).
  - Subsection is 45 lines vs the ≤35 target: code fences, the verbatim command
    and the ambiguity fixes below.
  - **Ambiguity fixes from the Claude scenario reader** (all consistent with the
    design's intent): added `other:<item id>` classification (path-wide
    enumeration otherwise makes every receipt stale on a long branch);
    `covered-by-pass` defined as "in the reviewed working tree"; `uncovered`
    readiness also needs the routed item's evidence; reconstruction counts only
    when the old record shows an independent pass at the required weight, with
    head = last product commit before the review record. QC §2 mirrors the
    generic parts. Reader's ambiguity G (QC §2 lacks "stale blocks readiness")
    is already covered by QC §4 line 168.
- Adjacent issues parked: none.

### Unit 3 forward scenarios (2026-10-19)

Same packet (`receipt-scenarios.md`, scratch) to two hosts, reading only the two
changed files; expected outcomes not supplied.

| Scenario | Codex `gpt-6-luna` high (job `20261019T153136Z-177a08ef`) | Claude fresh sub-agent |
| --- | --- | --- |
| 1 covered_fix | current; pass | current; pass |
| 2 unclassified `eee5555` | stale; not pass; classify, route if uncovered | stale; not pass; likely `uncovered → item` |
| 3 legacy, range recoverable | reconstructable; record label before pass | reconstructed; pass rule unclear (ambiguity B) |
| 4 standalone story | rule does not apply | rule does not apply |

Both hosts agree on all outcomes; the run predates the ambiguity fixes, which
address the Claude reader's A–F. No re-run after the fixes (they narrow, not
change, the scenario outcomes).

## Review (2026-10-19)

**Verdict**: Approve with comments (after receiver adjudication; reviewer verdict
was Request changes)

**Blockers**: none remaining. Reviewer blocker accepted and fixed: reconstructed
head defined as "last product commit before the review record" could absorb
post-review corrections into the reviewed range → now the head the reviewer's
report states it assessed, otherwise missing (`7eb12d33`).
**Important**: accepted and fixed in `7eb12d33`: reconstruction required "an
independent pass", conflicting with valid none/light policies → "the review its
effective weight required".
**Nits**: subsection exceeds the ≤35-line criterion — accepted as documented
deviation (verbatim command and code fences); criterion superseded.
**Rejected**: none.

**Notes**: feature substrate review, standard weight, one independent pass; no
re-review per standard. Fix verification by host: diff re-read, `git diff
--check` clean, skill-portability ok (PyYAML via uv; the reviewer's own run was
blocked by network), and the reconstruction rule applied to QVE's real legacy
record (reviewer-stated scope `70348687..13711e20` → head `13711e20`; later
`6419b3bc` classifiable as fix-of I-1/I-2). Forward scenarios predate the final
two wording changes; outcomes for scenarios 1, 2 and 4 are unaffected and
scenario 3 now has a deterministic head.

**Receipt**
- Reviewed: `6669a54a..a27d41d3` — `.work/CONVENTIONS.md`, `plugins/research-pipeline/skills/quality-checkpoint/SKILL.md`; work-record files excluded
- Reviewer: Codex `gpt-6.1-sol` medium via peeragent job `20261019T153332Z-4db66a16`; independent: yes (cross-model; host Claude)
- Weight: standard (source: default)
- Findings: blockers 1, important 1, nits 1, rejected 0
- Accepted-fix verification: `7eb12d33` verified by host (checks in Notes)

**Post-review changes** (`a27d41d3..7eb12d33`)
- `7eb12d33` fix(review receipts): anchor reconstruction on assessed head; honor none/light (.work/CONVENTIONS.md, quality-checkpoint/SKILL.md) — fix-of:blocker-1 and important-1 verified by host checks above
