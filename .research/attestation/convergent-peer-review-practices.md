---
source_handle: convergent-peer-review-practices
fetched: 2026-10-18
source_url: https://users.ece.utexas.edu/~miryung/teaching/EE379K-Spring2014/Papers/Paper%204.pdf
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "full-text (11-page PDF, text extracted; figures not read as images)"
---

# Convergent Contemporary Software Peer Review Practices

## Source structure and scope
The fetched PDF is a course-reading copy hosted on a University of Texas page; its title block is
replaced by a "PAPER 4" header, and it carries the ACM notice "ESEC/FSE '13, August 18 – 26, 2013, Saint
Petersburg, Russia" (printed page numbers run 202-212). The title and authors (Peter C. Rigby and Christian
Bird) are as attributed by citing references in fetched sources (reference [5] of the Czerwonka et al. talk
abstract and reference [33] of the Sadowski et al. Google case study), not read off this PDF; the two references differ on the title wording
("Convergent contemporary software peer review practices" vs "Convergent software peer review
practices"). Observational study of review data from Android, Chromium OS, Bing,
Office, MS SQL and AMD, contrasted with Lucent inspection data and six OSS projects (including Apache,
Linux, KDE). Measures: review interval, number of developers involved, proxy measures of defects
found, and a knowledge-sharing measure.

## Anchored details
- **Abstract:** "many of the characteristics of the review process have independently converged to
  similar values which we think indicate general principles of code review practice."
- **Section 4.2, "Selecting Reviewers":** the optimal number of inspectors "has long been contentious";
  citing Porter et al., the authors write that "two reviewers discovered as many defects as four
  reviewers. The consensus seems to be that two inspectors find an optimal number of defects". They
  label this "Convergent Practice 4: Two reviewers find an optimal number of defects".
- **Section 4.2, own data:** AMD median of 2 reviews; Chrome and Android median of two reviewers;
  Microsoft (Bing, Office, SQL) invited a median of 3, 3 and 4 reviewers, but "the median number of people
  that actually take part in a review (other than the author) is 2." Then:

  > Interestingly, we found that there was only a minimal increase in the number of comments about the change when more reviewers were active and there was no increase in the number of change sets submitted (i.e., the same number of "rounds of reviewing").

  Reviews with many more reviewers arose when "the author or the reviewers will invite additional developers
  after a round of reviewing has taken place", e.g. on concluding "that the change carries a high risk and
  should be reviewed by 'more eyes'."
- **Section 4.3, "Defects vs Discussion":** at Lucent "a median of 3 true defects found per review" plus 4
  false positives per review; "Convergent Practice 5: Review has changed from a defect finding activity to a
  group problem solving activity". At AMD "87% of reviews have no recorded defects", which the authors
  attribute to defects not being recorded rather than not found.
- **Section 7, "Conclusion" (practice list):** "Contemporary review usually involves two reviewers. However, the number of
  reviewers is not fixed and can vary to accommodate other factors, such as the complexity of a change."
- **Abstract, knowledge sharing:** review "increases the number of distinct files a developer knows about by
  66% to 150% depending on the project."
