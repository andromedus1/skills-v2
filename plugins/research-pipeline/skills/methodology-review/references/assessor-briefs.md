# Assessor briefs

Bundled briefs for this skill's two fresh-context passes. Dispatch each to a
fresh-context reviewer, using the project's cross-model preference when available.
Supply the named inputs and never prescribe a verdict. Both briefs tell the assessor
to work directly and never delegate the pass to another agent.

## Contents

- [Completeness challenge](#completeness-challenge)
- [Assessment](#assessment)

## Completeness challenge

Used at the [sample checkpoint](../SKILL.md#sample-checkpoint-before-depth-research),
before any depth research. The inputs are released in stages, because showing a
generator examples first increased misses, and a list made after exposure cannot test
what the exposure hid. Each stage's output is recorded before the next stage's inputs
are given. A re-challenge is always a fresh challenger starting at stage 1, never the
already-exposed one.

Blindness is input isolation, not only prompt staging. Before stage 1, check what the
challenger's environment shows automatically, such as working-tree status and
filenames, memory, instructions and the frame's own values. Remove or isolate anything
that names map or sample families, by whatever mechanism the host has. Keep required
safety and project instructions, and record the cues they still give. If candidate
names stay visible, report the challenge as cued with that limit, never as blind.

**Stage 1, blind.** Give only the charter's jobs, outcomes, constraints and decisions;
the declared frame (dimensions and the rule for "same family"); and the challenger's
cue. The cue must differ from the sample author's, for example a different objective as
the key, a stakeholder's perspective or an adjacent field.

> You are generating approach families for the job described, without seeing anyone
> else's list. Using the moves in the
> [surfacing-alternatives primer](../../../docs/surfacing-alternatives.md) (Lead with
> Purpose, Vary the Cue, Search Adjacent Fields), list genuinely different families.
> They must differ at the principle level or on a declared dimension, not in embodiment.
> For each, give the job it serves and the dimension values that distinguish it. Then
> do a second pass: first lists usually miss half the relevant families, and the missed
> ones matter as much. Add at least five more, marking which pass each came from. Name
> families descriptively, and do not present a family's existence or merits as fact
> without a source. Do this work directly; do not delegate it to another agent.

**Stage 2, compare.** Now give the drafted sample, with its exclusions and their
reasons, and the domain map's alternative space. Leave out the author's reasoning
beyond those reasons.

> Compare your recorded list with the map and the sample. Classify each of your families
> after merging variations: (i) absent from the map; (ii) on the map but not sampled,
> noting whether it carries a dimension value the sample does not cover; (iii) already
> sampled. Flag sampled "families" that are variants of one family, and any exclusion
> whose reason depends on the current method's own design.

**Stage 3, judge.** Now give the dimension grid with its empty cells, and the held-out
known families.

> Judge which empty combinations are real families, and which held-out families your
> list and the map each missed. Judging the map's candidates can only find gaps between
> the sample and the map. Report families absent from the map from your stage 1 list
> and from held-out checks, not from this judgement.

**Output:**
- the stage 1 list, with pass tags;
- the classification into (i), (ii) and (iii), and the merge or split decisions;
- empty-cell judgements;
- held-out families missed by the challenger, and held-out families absent from the map;
- questionable exclusions;
- the coverage statement the primer prescribes, as observed counts with no estimated
  total;
- the remedies the findings point to (map refresh, sample revision or a stronger
  challenge), and whether the sample looks fit to commission. This is advisory; the
  operator decides.

## Assessment

Used for the step-4 assessment of draft findings, before the operator sees the
packet, and for each step-6 round or exit assessment.

**Inputs:**
- the charter and current baseline;
- the domain map and the project mapping's coverage status;
- current project evidence: the actual artifact text cited by each finding;
- verified research comparisons and their gate records;
- the draft findings, or the prior findings with their statuses;
- exact operator decisions and authorized actions;
- the research and delivery evidence consumed.

For a parent assessment, also supply child assessments and coverage.

**Brief:**

> You are a fresh, independent assessor of a methodology review. Assess the current
> methods against the charter, not against the host's conclusions.
>
> 1. For each finding, check the cited project text and research. Report it as
>    supported, uncertain/needs evidence, or withdrawn with an evidence reason.
>    Check its severity against the major-finding definition the skill gives you.
> 2. Report new major findings, regressions and cross-component effects within the
>    agreed scope. Treat any external claim absent from verified research as
>    provisional.
> 3. Report remedy verification for authorized changes, as verified, not resolved,
>    or awaiting evidence.
> 4. Report coverage against the domain map: compared, operator-excluded and
>    unexamined families bearing on in-scope decisions. Unexamined coverage is
>    reported, not converted into a finding by itself.
> 5. Change a severity only on evidence, stating it; never lower one, shrink scope or
>    treat agreement as approval to reach a cleaner exit.
> 6. Carry the exact operator decisions as given. An explicit retain/defer decision on
>    an unchanged basis needs no fresh confirmation; if a new choice is needed for
>    progress, name it and the evidence that makes it new.
>
> Do this work directly; do not delegate it to another agent.

**Output:** a dated report in the
[assessment report](review-record.md#assessment-report) shape, including counts and
IDs, coverage against the map, actual versus expected effort when supplied, and one
exit outcome from the skill with its reason. Exit outcomes apply to round or exit
assessments only. A step-4 pre-packet assessment returns finding statuses only, unless
it covers the whole charter on the current baseline: then it counts as one round and
also returns the exit.
