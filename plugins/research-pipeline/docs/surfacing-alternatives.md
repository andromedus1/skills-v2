---
description: "Thinking primer — 10 researched moves for surfacing genuinely different approaches and checking a sample of approaches for completeness"
type: primer
updated: 2026-10-20
---

# Surfacing Alternatives

A practical toolkit for producing a set of genuinely different approaches to a problem, not
variations of the first one that came to mind, and for judging how complete that set is before
depth research is spent on it. There are 10 moves in three phases: Frame, Generate and Check.

**How to use this:** Read before building a domain map, drawing a comparison sample, challenging a
sample for missing families, or writing per-facet research briefs. This is the
[methodology-review](../skills/methodology-review/SKILL.md) skill's front end, and it applies to any
step that must enumerate alternatives. Apply the moves that fit the step; the
[step table](#where-each-move-applies) says which.

**Grounding.** The moves distil the Agentic Research campaign
`.research/analysis/campaigns/solution-space-decomposition/` (2026-10-20, full rigor). It drew on
eight fields: design-space methods, decision analysis, analogy research, LLM ideation, evidence
synthesis, species-richness estimation, classification and landscape mapping. Each move states its
evidence level. **Measured** means a controlled or quantified comparison exists; **advocated** means
the practice is recommended without one. Most evidence comes from lab studies, crowds and preprints,
and none of it tests these moves on samples of methodology alternatives specifically. Treat the
moves as well-grounded defaults, not guarantees. Citations live in the campaign's `parent.md`, not
here.

**The Incompleteness Principle:** An unaided first list recovers roughly a third to a half of the
alternatives its author later recognises as relevant. The missed ones are about as good as the
found ones, and the author does not notice the gap. **Assume your first list is incomplete, and
check it with something other than your own sense of completeness.**

---

## The Moves

### Frame — decide what "different" means before generating

#### 1. Lead with Purpose
Generate from jobs, outcomes and objectives, not from the solution you already have.

**Why:** Objectives used as stimuli produced more and better alternatives than unaided generation.
Retrieval that held the purpose fixed and varied the mechanism beat both keyword-similar and random
inspiration. Starting from the current method anchors every later idea to it. *(measured; key study
read at abstract depth)*
**How:** Write down what the method is *for*: its jobs, the outcomes that matter and the
constraints that are really fixed. For each objective, ask "what approach would serve this one best?"
Derive the decision dimensions from that purpose, and keep only dimensions on which candidate
approaches actually differ.
**Example:** Reviewing a knowledge-retrieval method. Don't start from "alternatives to our vector
store". Start from the jobs: find a known fact, discover an unknown connection, keep answers current.
Each job pulls in different approach families: lookup, graph traversal, active refresh.

#### 2. Declare the Frame
State the dimensions, the rule for "same family", and the generators you used.

**Why:** Every field that counts kinds finds the count relative to its frame:
- the dimensions chosen;
- the threshold for merging near-duplicates;
- the process that generated the candidates.

A morphological field is "complete" only within its own parameters. Two independent mappings of
one topic overlapped little and classified differently. *(measured)*
**How:** First decide the map's scope. Landscape practice differs between covering the whole
population and narrowing to the handful of most important approaches. Then record three things. The
**dimensions** and their values. The **identity rule**: two
candidates are different families when they diverge at the principle level, or take a different
value on a declared dimension. The **generators**: which searches, people or prompts produced
candidates. Every later completeness statement is "relative to this frame".
**Example:** "Families differ on knowledge representation (graph / vector / document / relational)
or on update model (batch / incremental / on-read). Two tools that share both values are one
family."

#### 3. Test the Level of Difference
Different approaches diverge at the principle level, not in embodiment or detail.

**Why:** Measured breadth in ideation research weights differences by abstraction level: physical
principle, then working principle, then embodiment, then detail. Lists that look varied often differ
only in embodiment. Selecting approaches by how often they are proposed keeps the commonest ones.
*(designed metric; selection effect described in one study)*
**How:** For each pair of candidates, finish the sentence "this approach achieves the job by ___".
If both answers are the same, the candidates are one family. Favour a few clearly distinct families
over many near-duplicates. A university release reports this preference held in a paper-title
task, so for approaches it is a transfer, not a tested rule.
**Example:** "Remove ice", "melt ice", "prevent formation" and "prevent adhesion" are four principles.
Three brands of ice scraper are one.

---

### Generate — widen the set

#### 4. Generate Before You Look
Produce candidates independently before seeing examples, prior lists or anyone else's answers.

**Why:** In an objectives experiment, showing examples upfront *increased* misses, and designers
repeated example features even when told not to. In language models, three things reduced diversity:
telling the model how similar its ideas already were, picking the best from pooled sessions, and
standard multi-agent debate. Voting over independent answers did not reduce it. Independent lists
pooled *before* discussion were much more complete than any single contributor's. *(measured in the
tested conditions; the pooling result is one case; one study found exposure to AI ideas widened
collective diversity, so exposure is not narrowing in general)*
**How:** Have each generator (a person, an agent or a search) list on its own first. Then take the
de-duplicated union. Show existing samples or templates only afterwards, as a second-pass check.
**Example:** The completeness challenger lists the families it expects for the domain *before* it is
shown the review's sample, then compares the two.

#### 5. Vary the Cue, Not the Copy
Give each generator a different starting point, because same-prior generators converge.

**Why:** Different language models answered open questions with 71–82% average similarity, so
swapping models alone does not establish independent coverage. LLM pools also narrow mostly *across*
independent draws. Distinct per-draw cues (ordinary everyday personas, a fixed lens per agent)
measurably widened coverage, and a higher temperature barely helped. Judge a new generator by what it
adds, not by its name. *(measured in single studies)*
**How:** Assign each pass a different framing: a different stakeholder, a different objective as
the key, a different adjacent field, or a different decision dimension to lead with. Pair this with
oblique-strategies' **Borrow Eyes**.
**Example:** Three challenger passes lead with "the cheapest workable approach", "how a
librarian would do this" and "approaches that drop our assumed constraint".

#### 6. Search Adjacent Fields at a Workable Level
Abstract the problem enough to reach other fields, but no further.

**Why:** Unaided retrieval is surface-bound: about 30% of people spontaneously used an available
analogy, against about 75% with a hint. Comparing two analogs roughly doubled far transfer, and
concrete constraint statements found relevant yet distant sources. Statements that are too abstract
produce ideas that don't fit. The effect of domain distance itself is mixed: distant sources can be
more novel but less usable, and no reliable sweet spot is known. *(measured; distance effects
contradictory)*
**How:** Restate the job as a domain-neutral function ("keep a set of claims current as sources
change"). Search for fields that solve that function, and compare at least two of them before
settling on an approach. Collect each field's vocabulary for the same concept; vocabulary mismatch
is a recurring cause of missed families. Pair this with oblique-strategies' **Steal From a
Stranger**.
**Example:** "Keeping claims current" reaches cache invalidation, journal retraction tracking and
pharmacovigilance. These are three fields with different update models.

#### 7. Push the Second Pass
After a first list, run a second pass that says the first is incomplete and sets a target.

**Why:** A plain "anything else?" added almost nothing (+0.55 items). A warning that first lists
usually capture under half, plus "add at least N more", added roughly 3 to 5 items with no quality
loss. Extra time or rumination did not help. For language models, showing the prior items with an
instruction to make the next one different gave the largest diversity gains. A category-structured
second pass also added items, but that design cannot separate the categories from the extra pass
itself, and categories added nothing reliable over the warning. *(measured; objectives, MBA
population; LLM benchmarks)*
**How:** Second pass: "Most first lists miss half the relevant options, and the missed ones matter
as much. Add at least five families not yet listed, each different at the principle level." If you
use categories, offer them in the second pass, not upfront; upfront categories did not reduce misses.
**Example:** After eight families, the second pass surfaces "do nothing / manual curation" as a
baseline, and a market-mechanism family that no one had listed.

---

### Check — judge completeness without overclaiming

#### 8. Judge, Don't Re-Enumerate
Ask the checker to judge presented candidates and to look at visible gaps. Don't ask it to recall
everything again.

**Why:** In one-shot tests against a reference, models judged set membership far more accurately
than they authored sets, and they detected planted wrong inclusions 6–7x more often than planted
omissions. Marking *where* content was removed raised omission detection substantially for surface
deletions with both documents available. People judging a decomposition they were shown
underweighted what it left out, experts included. *(measured; transfer to missing approach families
untested)*
**How:** Do this *after* the checker's independent list from move 4 is recorded. Give it the
candidates from the map and the other passes, plus the dimension grid with empty cells shown, and
ask: "Which of these belong? Which empty combinations are real families?" Never accept "looks
complete" as a finding. Judging the map's own candidates can only find gaps between the sample and
the map. It cannot find families the map is missing. That job belongs to move 4's blind list and to
held-out families (move 9).
**Example:** A dimension grid shows no candidate with an "on-read" update model and a "graph"
representation. The checker is asked whether that combination exists in practice.

#### 9. Report Coverage, Not Completeness
Say what the independent passes found and how far they agreed, relative to the frame.

**Why:** No attested source validates a completeness estimator for families of methods or
approaches. Statistical estimators work in their own fields (ecology, fuzzing, software inspection),
but each has its own sampling assumptions. Capture–recapture needs independent passes, and inspection
studies advise against fewer than four unless they are shown to work. A review challenge has one
author sample and one or two deliberately varied passes. That falls short of those assumptions, so no
statistical estimate is supported. Sample coverage is no exception, because it comes from the same
counts. When new items open *new categories*, that is a measured sign of missing
kinds. Disagreement between passes is partly classification (merged or split families), not only
retrieval. *(measured in other domains; transfer to approaches untested)*
**How:** First apply move 3 to the checker's *blind* list (move 4), so variations aren't counted as
families. Then lead with the primary signal, in two parts:
- **(i) families absent from the map**, and whether they open new dimensions or empty cells;
- **(ii) families on the map but left out of the sample**, and whether each carries a dimension value
  the sample doesn't cover. Exclusions the sample made on purpose are not gaps.

Note whether each addition came from the unforced pass or the targeted second pass (move 7). Then
report:
- the overlap between the blind list and the sample;
- held-out known families absent from the map (keep a few known families, such as ones named in
  prior reviews, out of map-building, then check the map against them);
- new families added per pass;
- naming and merging decisions, kept separate from retrieval gaps;
- the frame from move 2.

Give the observed count, never an estimated total. A statistical estimate isn't available here for
three reasons: the sample is a purposive draw rather than a random capture, there are only two or
three passes, and models with shared training priors may correlate them.
**Example:** "Challenger and author overlapped on 6 of 9 families. The challenger's 3 extra families
filled two empty cells and added one new dimension (governance model). That is evidence the frame
was incomplete, so refresh the map."

#### 10. Distrust "Nothing New"
A pass that adds nothing is not evidence that nothing is missing.

**Why:** In screening, stopping after 50 irrelevant items in a row, or at a baseline rate, each
missed the recall target in about 39% of runs. At typical saturation stopping points, a median 18–22%
of the observed themes were still unseen. Several taxonomy ending conditions check only the last
iteration. No attested rule says when a sample of approach families is complete enough. *(measured in
other domains; transfer to a quiet challenge pass is an inference)*
**How:** Match each trigger to its remedy.
- **Refresh the map** and re-challenge the affected decisions when there are part (i) families, or
  held-out known families absent from the map.
- **Revise the sample** when there are part (ii) families with an uncovered dimension value.
- **Strengthen the challenge** (more distinct cues, another targeted pass) when the challenger itself
  misses held-out families. A quiet challenge that also misses known families is weak evidence.

Otherwise, moving to depth research is the operator's judgement, made on the coverage statement
(move 9), not on a quiet last pass. When depth research later reports a new category, treat it as a trigger to
refresh the map. Pair this with first-principles' **Seek Falsification**: look for the family that
would break your frame.

---

## Where each move applies

| Step | Lead moves | Pair with |
|------|------------|-----------|
| Domain map | 1 Lead with Purpose, 2 Declare the Frame, 6 Search Adjacent Fields | first-principles *Decompose to Fundamentals*, *Question Deeply* (explore alternatives); oblique *Question the Question* |
| Charter sample | 3 Test the Level of Difference, 2 Declare the Frame; cover every value of each declared dimension at least once ("full field coverage") | first-principles *Apply Multiple Lenses* |
| Completeness challenge | 4 Generate Before You Look, 5 Vary the Cue, 7 Push the Second Pass, 8 Judge, Don't Re-Enumerate, 9 Report Coverage, 10 Distrust "Nothing New" | first-principles *Seek Falsification*, *Invert the Problem*; oblique *Borrow Eyes* |
| Per-facet research briefs | 6 Search Adjacent Fields (vocabulary), 9 Report Coverage (do new sources open new categories?); ask for maximum variation and disconfirming cases | first-principles *Doubt What You Know* |

**The rhythm:** Frame → Generate → Check, then back to Frame when Check finds a new dimension. A
family the check adds goes back into the map as a refresh, never as an untracked note.

---

## Guardrails

### Illusory Totality
Treating a complete enumeration of *your* dimensions as a complete enumeration of the space.
**Antidote:** Every completeness statement names its frame (move 2). Look for a family that needs a
dimension you don't have.

### Variations Dressed as Families
A long list that differs only in embodiment. **Antidote:** Apply the principle-level test (move 3);
prefer few distinct families to many similar ones.

### Consensus Collapse
Debate, shared examples or one model family pull every pass to the same modes. **Antidote:** Keep
passes independent until the union (move 4). Vary cues, not copies (move 5).

### Too Far to Use
Distant analogies that are novel but don't fit the job. **Antidote:** Abstract to a workable level
and compare two analogs (move 6). Judge fit to the declared jobs before adding a family.

### Self-Certified Completeness
The author, or a checker that saw the author's list first, declares the sample complete.
**Antidote:** The check generates independently, judges presented candidates, and reports coverage
(moves 4, 8, 9).

### Analysis Paralysis
Enumerating forever. **Antidote:** The goal is a sample fit for the decision, not the whole
space. Stop when the agreed checks have run and their findings are dispositioned (move 10), and
report what remains unexamined.

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [First Principles](first-principles.md) | Depth within a frame: decompose, challenge, synthesize, verify |
| [Oblique Strategies](oblique-strategies.md) | Lateral moves for when a list is stuck or over-constrained |
| [Methodology review](../skills/methodology-review/SKILL.md) | The consuming skill (domain map, sample checkpoint, commission packet) |
| Campaign `solution-space-decomposition` | Evidence for every move: `.research/analysis/campaigns/solution-space-decomposition/parent.md` |
