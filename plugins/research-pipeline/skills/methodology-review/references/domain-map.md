# Domain map

The domain map is the shared view of a reviewed topic. The charter sample, research
facets and coverage report all reference it. It is made of two artifacts with
different owners, so research stays free of project framing and decisions never
rewrite research.

## Contents

- [Alternative space (research-owned)](#alternative-space-research-owned)
- [Project mapping (loop-record-owned)](#project-mapping-loop-record-owned)
- [Building the map](#building-the-map)
- [Reuse, refresh and programs](#reuse-refresh-and-programs)

## Alternative space (research-owned)

Commission it through `research-pipeline:scout` in domain-map mode. The result is a
landscape brief, optionally with a vocabulary capture, under Agentic Research's
`.research/analysis/` map. Ask for these sections:

| Section | Content |
|---|---|
| Jobs and outcomes | What practitioners in the field are trying to achieve, in the field's terms |
| Decision dimensions | The independent choices along which approaches differ, with each dimension's values |
| Approach families | Genuinely different approaches, each described natively: its concepts, workflow, configuration and intended context, with representative instances |
| Scenarios | Common situations, including adverse and correction paths, that separate the families |
| Evidence by level | Per family: designed or advocated, documented, demonstrated, or independently measured |
| Open questions | What sources could not settle, and known evidence absences |
| Vocabulary | Terms that differ across communities for the same concept, to widen later searches |

Describe the topic generically. Never send private project content to public
searches or services. A family is "genuinely different" when it takes a different
value on at least one decision dimension that matters to the jobs. A variant within
one family is not a new family.

## Project mapping (loop-record-owned)

Record this in the review's loop record, never in research:

- in-scope jobs and decisions, with the map dimensions each decision touches;
- where the current method sits on each dimension;
- the sample: chosen families and representatives, a simpler baseline when relevant,
  and excluded families with reasons;
- coverage status per family: compared, excluded by the operator, or unexamined,
  updated as research returns;
- transfer and proposals, which are drawn from verified comparisons but belong here
  (see [review-record.md](review-record.md#transfer-and-proposals)).

## Building the map

1. Check `.research/analysis/` and the knowledge index for a current map covering the
   topic. Reuse it when its scope and freshness fit.
2. Otherwise commission scout with search vectors that reach beyond the current
   method's vocabulary, including adjacent fields solving the same job.
3. Read the result and draft the project mapping. Then run the skill's
   [sample checkpoint](../SKILL.md#sample-checkpoint-before-depth-research).

The specific decomposition strategies to apply at each step are in the
[surfacing-alternatives primer](../../../docs/surfacing-alternatives.md).

## Reuse, refresh and programs

- **Versioning.** The alternative space follows Agentic Research's correction,
  reversal and refresh rules. A refresh supersedes a prior map and keeps it as
  history. Record which map version the sample drew from in the loop record.
- **Refresh triggers.** A family the challenge or operator adds; an expiring
  `temporal_contract`; material change in the field; or a re-run whose
  what-changed baseline names the area. Refresh only the named gap.
- **Programs.** A component-then-suite program maps once at the root, covering the
  whole suite without presupposing component boundaries. Children draw their samples
  from the shared map, and their project mappings cite it, so results compare against
  one alternative space. A child commissions deeper research only where its own
  decisions need it, and extends the shared map through a refresh rather than a
  private copy.
- **Re-runs.** A re-run reuses the predecessor's map under the same freshness
  rules, and its report notes which map version each round used.
