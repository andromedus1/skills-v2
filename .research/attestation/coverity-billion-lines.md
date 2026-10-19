---
source_handle: coverity-billion-lines
fetched: 2026-10-18
source_url: https://6826.csail.mit.edu/2019/papers/coverity.pdf
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "full-text (10-page CACM PDF, text extracted; sidebars and tables read as extracted text)"
---

# A Few Billion Lines of Code Later: Using Static Analysis to Find Bugs in the Real World

## Source structure and scope
Al Bessey, Ken Block, Ben Chelf, Andy Chou, Bryan Fulton, Seth Hallem, Charles Henri-Gros, Asya Kamsky,
Scott McPeak (current or former Coverity employees) and Dawson Engler (Stanford; technical advisor to
Coverity), per the author notes. Communications of the ACM, vol. 53, no. 2, February 2010, pp. 66 onward (as
printed on the fetched PDF, a copy hosted on an MIT course page). An experience report on commercializing a
research bug-finding tool; claims are the vendor's accumulated experience and anecdotes from customer trials,
not measured studies.

## Anchored details
- **Section "False Positives":**

  > False positives do matter. In our experience, more than 30% easily cause problems. People ignore the tool. True bugs get lost in the false. A vicious cycle starts where low trust causes complex bugs to be labeled false positives, leading to yet lower trust.

  Continues: "We have seen this cycle triggered even for true errors. If people don’t understand an error, they
  label it false." The authors "initially thought false positives could be eliminated through technology.
  Because of this dynamic we no longer think so."
- **Same section, the vendor target:** "We aim for below 20% for “stable” checkers. When forced to choose
  between more bugs or fewer false positives we typically choose the latter."
- **Same section, not all false positives are equal:** "The initial reports matter inordinately; if the first N
  reports are false positives (N = 3?), people tend to utter variants on “This tool sucks.”" Also: "A stupid
  false positive implies the tool is stupid."
- **Passage on trial-meeting utterances (preceding "How to handle cluelessness"):** after examples of
  programmers rejecting true reports, "a not-understood bug report is commonly labeled a false positive, rather
  than spurring the programmer to delve deeper. The result? We have completely abandoned some analyses that
  might generate difficult-to-understand reports."
- **Usage of the term (early section on the research context):** the article glosses false positives as
  "false-error messages (false positives)" and states the ideal as finding "the maximum number of serious true
  errors with the minimum number of false reports". No numeric definition of how the 20% or 30% figures are
  measured is given in the passages read.
