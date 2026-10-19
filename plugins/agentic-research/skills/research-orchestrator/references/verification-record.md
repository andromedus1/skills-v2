# Recording research verification

Use this when starting verification, correcting an output or resuming an
engagement. The orchestrator's verification-depth rules and ARD SPEC §7 determine
which gates run and their correction/stop behavior; this writing aid adds no gate,
rigor dial, iteration allowance or research schema.

Keep the record with the engagement: the commissioning item body, a standalone
campaign's existing verification artifacts, or the transcript for standalone light
research. Do not create `.work/` just to record a standalone result. A transcript
that cannot be recovered on resume is missing evidence.

Before checking, record the output paths and assessed revision/digests, effective
rigor (for `adaptive`, the resolved level and why), reachable required gates and any legitimate reachability prune. For each
required gate, retain:

| Field | Meaning |
|---|---|
| Scope and inputs | Output snapshot and evidence visible to this verifier; preserve evaluator isolation |
| Actual result | Verdict/checklist, lint findings, lead spot-check findings, error or not run |
| Evidence | Report or captured output location |
| Correction | Finding, affected claims, remedy and verification still required at that scope |

Do not claim engagement completion while a required result is missing, failed,
stale or unresolved; successful worker exit without its required verdict is not
approval. Read lint's structured findings rather than treating its default zero
exit as a clean bill of health. Report broken chains, thin attestations and advisory
patterns separately. Group advisories by category with representative file/line
examples and retain raw lint output; a dotted version token can be neutral prose,
a source title or a decimal, not necessarily an unsupported factual claim.
Ordinary `1.`/`2.` bibliography numbering is not itself a version-number trigger.
Neither suppressing these warnings nor reaching zero warnings establishes semantic
support; the required semantic checks and lead spot-check still apply.

After a correction, preserve earlier findings/verdicts and identify the changed
claims/inputs. Refresh affected verification according to the orchestrator's gate
rules; record why unaffected evidence still applies. A metadata-only revision does
not by itself invalidate semantic coverage. Do not imply a reviewer assessed text
written afterward. Apply the orchestrator's stop rule (surface a recurring or repeatedly
regressing failure) and keep unresolved gates open; do not silently retry, or treat
interruption/delegation as a fresh engagement.

On resume, restore the last assessed output, applicable gates, returned reports,
corrections and pending next step before commissioning more work. A gate already
satisfied on unchanged inputs needs no duplicate run. Report an explicit unresolved
outcome when required coverage or correction cannot be completed.
