---
id: story-fix-doc-review-archive-path
kind: story
stage: review
tags: [bug, research-pipeline]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# doc-review archive recovery path pluralizes `story` as `storys`

## Symptom
QVC round-2 assessment (QVC/METH-001, minor): doc-review check 2d's recovery
template `git show <git_ref>:.work/active/<kind>s/<id>.md` fails for archived
stories. Reproduced: `git show 8bec851e:.work/active/storys/story-research-package-boundary.md`
→ `fatal: path ... does not exist`; the `stories` path recovers the body.

## Root cause
The template derives the active directory by appending `s` to `kind`, but the
substrate's story directory is the irregular plural `stories`.

## Fix approach
Name the directory explicitly: `<dir>` is `epics`, `features` or `stories` for the
stub's `kind`. No other behavior changes.

## Regression test
`plugins/research-pipeline/scripts/tests/skill-portability.test.sh` fails if
doc-review's SKILL contains `<kind>s/` (failed before the fix, passes after).

## Implementation notes
- Execution capability: host inline; one-line prose correction plus a guard.
- Files changed: `plugins/research-pipeline/skills/doc-review/SKILL.md` (2d);
  `plugins/research-pipeline/scripts/tests/skill-portability.test.sh`.
- Four-step confirmation: (1) new check failed before the fix (rc=1) and passes
  after; (2) RP portability ok, AR metadata ok; (3) applying the corrected rule
  to all 7 archived stubs in this repo recovers every body (3 stories, 4
  features); (4) the reported symptom (archived story unrecoverable) is gone.
- Adjacent issues parked: none.
