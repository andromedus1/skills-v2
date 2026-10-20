# Commission packet

A commission packet carries one review unit's comparison request to
`agentic-research:research-orchestrator`. Write it once, in the loop record or as a
linked section, and reference it by path from the commissioning item and every
dispatch, so charter fields are not restated or drifted per dispatch. The
orchestrator remains authoritative for its kickoff, dials and verification.

## Template

```markdown
### Commission packet — <review-id>/<unit>

- **Decision relevance (yield hypothesis):** <which recorded decision changes if the
  comparison finds what>
- **Domain map:** <path and version of the alternative space>; sampled families and
  representatives; baseline; excluded families with reasons
- **Charter fields:** users, jobs and outcomes; constraints (fixed versus disputed);
  scenarios with adverse and correction paths; criteria
- **Evidence levels:** separate designed, documented, demonstrated and independently
  measured behavior; a documentation gap is unknown, not absence
- **Evidence feasibility:** per decision: literature-settleable, experiment-needed or
  mixed; for experiment-needed ones, ask for the decisive experiment design, not a
  verdict
- **Proposed dials:** intent `calibrate-external`; output_kind
  `[synthesis-brief, questions-list]`; scope authority and rigor proposed per the
  charter (default mixed and standard), for the orchestrator to settle
- **Required output section:** Decision relevance (non-recommending), below
- **Coverage asks:** seek maximum variation and disconfirming cases; record vocabulary
  differences; flag any source that opens a category absent from the domain map
- **Privacy:** no private project content in public searches or external services
```

The defaults fit a comparison that informs, rather than makes, an operator decision.
Change them only when the decision warrants it. For example, a pure landscape gap goes
to scout, and a single bounded question may need only a synthesis brief.

## Required output: Decision relevance

Ask for this section from the first draft. Adding it afterwards creates new claim
surface and verification churn. For each recorded decision, the section states:

- the evidence bearing on it, by level, with citations;
- the conditional: if an alternative is preferred, what would have to hold for
  adopting it to be warranted, and what retaining the current method would need;
- the next evidence that would settle it, such as a source, measurement or
  experiment.

The section is **non-recommending**. It states conditions and evidence, never
"adopt X" or what the project should do. Research owns comparisons in each
alternative's own terms. Transfer to this project and proposals belong to the loop
record ([review-record.md](review-record.md#transfer-and-proposals)).

## Scope changes

If the operator widens scope after commissioning, record a new baseline. Extend the
running engagement only within its registered scope authority. Otherwise commission
a linked new engagement with its own packet. Never stretch a registration silently.
At a program-scale threshold, follow the orchestrator's escalation rather than
widening one fan-out.
