---
source_handle: google-review-speed-lgtm
fetched: 2026-10-18
source_url: https://google.github.io/eng-practices/review/reviewer/speed.html
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "full-text (pages: reviewer/speed.html; reviewer/looking-for.html 'Every Line' section; eng-practices index)"
---

# Google Engineering Practices: Speed of Code Reviews (and "Every Line" exceptions)

## Source structure and scope
Public pages of "Google Engineering Practices Documentation" (google.github.io/eng-practices), which the
index page describes as documents that "represent our collective experience of various best practices";
licensed CC-By 3.0. No page dates were shown. These are documented guidance for reviewers, not measurements.
Also read: https://google.github.io/eng-practices/review/reviewer/looking-for.html (section "Every Line",
"Exceptions") and the index https://google.github.io/eng-practices/ (terminology: CL = changelist; LGTM =
"Looks Good to Me", what a reviewer says when approving).

## Anchored details
- **speed.html, "Why Should Code Reviews Be Fast?":** "At Google, we optimize for the speed at which a team of
  developers can produce a product together, as opposed to optimizing for the speed at which an individual developer
  can write code." When reviews are slow, work is "delayed by days, weeks, or months as each CL waits for review and
  re-review."
- **speed.html, "LGTM With Comments":**

  > In order to speed up code reviews, there are certain situations in which a reviewer should give LGTM/Approval even though they are also leaving unresolved comments on the CL.

  Conditions (at least one): "The reviewer is confident that the developer will appropriately address all the
  reviewer's remaining comments."; "The comments don't have to be addressed by the developer."; "The suggestions are
  minor, e.g. sort imports, fix a nearby typo, apply a suggested fix, remove an unused dep, etc." Also: "The reviewer
  should specify which of these options they intend, if it is not otherwise clear."
- **looking-for.html, "Every Line" / "Exceptions":** a reviewer on a multi-reviewer CL may be asked to review only
  certain files or "only certain aspects of the CL, such as the high-level design, privacy or security implications";
  "In these cases, note in a comment which parts you reviewed."
