---
source_handle: github-stale-review-dismissal
fetched: 2026-10-18
source_url: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "partial: section 'Require pull request reviews before merging' read in full; other branch-protection sections skimmed"
---

# GitHub Docs: About protected branches

## Source structure and scope
GitHub product documentation describing branch protection settings. It documents optional, configurable
platform behavior (designed capability), not evidence about review effectiveness. No page date recorded.

## Anchored details
- **"Require pull request reviews before merging", stale approvals:**

  > Optionally, you can choose to dismiss stale pull request approvals when commits are pushed that affect the diff in the pull request.

  "GitHub records the state of the diff at the point when a pull request is approved. This state represents the set
  of changes that the reviewer approved." If the diff changes (new pushes, "Update branch", or a related pull request
  merged into the target branch), "the approving review is dismissed as stale, and the pull request cannot be merged
  until someone approves the work again."
- **Same section, most recent reviewable push:** "Optionally, you can require that the most recent reviewable push must
  be approved by someone other than the person who pushed it." This lets the "last reviewer" check "that the latest set
  of changes incorporates feedback from other reviews, and does not add new, unreviewed content."
- **Same section, the documented tradeoff:**

  > For complex pull requests that require many reviews, requiring an approval from someone other than the last person to push can be a compromise that avoids the need to dismiss all stale reviews

  and: "If you are concerned about pull requests being "hijacked" (where unapproved content is added to approved pull
  requests), it is safer to dismiss stale reviews."
- **Same section, note:** with either setting, "approving reviews will be dismissed as stale if the merge base introduces
  new changes after the review was submitted."
