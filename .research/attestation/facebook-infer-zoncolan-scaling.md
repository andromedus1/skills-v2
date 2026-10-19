---
source_handle: facebook-infer-zoncolan-scaling
fetched: 2026-10-18
source_url: https://6826.csail.mit.edu/2020/papers/facebook-infer-cacm.pdf
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "full-text (9-page CACM PDF, text extracted; figures read only through captions and text)"
---

# Scaling Static Analyses at Facebook

## Source structure and scope
Dino Distefano, Manuel Fähndrich, Francesco Logozzo, Peter W. O'Hearn. Communications of the ACM, vol. 62,
no. 8, August 2019, pp. 62 onward, DOI 10.1145/3338112 (as printed on the fetched PDF, a copy hosted on an
MIT course page). Contributed article reporting organizational experience deploying two interprocedural
analyzers: Infer (mobile and backend C++) and Zoncolan (Hack security taint analysis). Evidence is the
authors' deployment metrics (fix rates, action rates, counts of fixes) and narrative; the batch vs diff-time
comparison is a before/after deployment change, not a controlled experiment.

## Anchored details
- **"Key insights" box:** "Static analyses should strike a balance between missed bugs (false negatives) and
  un-actioned reports (false positives)." "A “diff time” deployment, where issues are given to developers
  promptly as part of code review, is important to catching bugs early and getting high fix rates."
- **"People and deployments":**

  > Later, we recount a striking situation where the diff time deployment saw a 70% fix rate, where a more traditional “offline” or “batch” deployment (where bug lists are presented to engineers, outside their workflow) saw a 0% fix rate.

- **"Actioned reports and missed bugs" (definitions):** "a false positive is one that cannot happen" (a true
  positive is a report of a bug that can happen in some run "whether or not it will happen in practice").
  False positives "tend to lead to apathy toward reported alarms". "fewer false positives often (though not
  always) implies more false negatives". The false positive rate "is challenging to measure for a large,
  rapidly changing codebase", so "we don’t make claims about their rates and pay more attention to the action
  rate and the (observed) missed bugs." "At diff time an action is an update to the diff that removes a static
  analysis report." Zoncolan's "action rate" is "above 80%" with "about 11 “missed bugs.”"
- **"Human factors" (Infer's first deployment was nightly batch):**

  > We assigned 20–30 issues to developers, and almost none of them were acted on. We had worked hard to get the false positive rate down to what we thought was less than 20%, and yet the fix rate—the proportion of reported issues that developers resolved—was near zero.

  Then, at diff time: "the fix rate rocketed to over 70%. The same program analysis, with same false positive
  rate, had much greater impact when deployed at diff time." Developers' explanations: the "mental effort of
  context switch" (in review "mental context already swapped in"; "if a bot were to run for an hour or more on
  a diff it could be too late to participate effectively") and "relevance" (a comment on the diff that
  introduces an issue has "a pretty good (but not perfect) chance" of reaching the right person).
- **"Impact" (Infer):** "Since 2014, Facebook’s developers have resolved over 100,000 issues flagged by Infer.
  The majority of Infer’s impact comes from the diff-time deployment". RacerD's "fix rate for the concurrency
  analysis to March 2018 was roughly 50%, lower than for the previous general diff analysis"; developers
  "appreciate the reports because concurrency errors are difficult to debug", which the authors present as
  "balancing action rates and bug severity".
- **"Funneled deployment" (Zoncolan):** a master analysis exposes all alarms to security engineers via a
  triage dashboard; false-positive alarms are filed back to the tool team, who "refine the tool to improve the
  precision". Promotion to diff analysis "involves improving the signal by filtering the output"; "circa 1/3 of
  the Zoncolan categories are enabled for diff analysis." "For categories with very high signal, Zoncolan acts
  as a security bot: it bypasses the security on-call and instead comments directly on the diff." Lower-signal
  diff issues go to the on-call queue; others fall through to the master analysis.
- **Zoncolan results:** "43.3% of the severe security bugs are detected via Zoncolan"; "211 severe issues are
  prevented at diff-time, versus 122 detected on master"; "the ratio of Zoncolan actioned bugs to be close to
  80%."

## Reference-list entries (recorded for acquisition grounding)
- **"Impact" (RacerD paragraph):** "See Blackshear et al.2 for more discussion on fix rates."
- **References, entry 2:** "Blackshear, S., Gorogiannis, N., Sergey, I. and O'Hearn, P. Racerd: Compositional
  static race detection. In Proceedings of OOPSLA, 2018."
