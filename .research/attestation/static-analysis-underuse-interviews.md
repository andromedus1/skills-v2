---
source_handle: static-analysis-underuse-interviews
fetched: 2026-10-18
source_url: https://people.cs.gmu.edu/~johnsonb/docs/icse2013.pdf
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "full-text (10-page author PDF, text extracted; Figure 1 bar chart read as extracted numbers)"
---

# Why Don't Software Developers Use Static Analysis Tools to Find Bugs?

## Source structure and scope
Brittany Johnson, Yoonki Song, Emerson Murphy-Hill (North Carolina State University) and Robert Bowdidge
(Google), as printed on the fetched author PDF. The venue is not printed on the fetched PDF. The reference
list of the separately fetched Sadowski et al. 2018 CACM article attributes it to the Proceedings of the 35th
International Conference on Software Engineering, 2013. A qualitative interview study: semi-structured
interviews of 40-60 minutes with 20 participants (16 professional developers at a large company and 4 graduate
students with industry experience; 3 to 25 years of experience), including an "Interactive Interview" using a
tool on code and a participatory-design part. Counts are participants raising a theme, not measured behavior.

## Anchored details
- **Abstract:** "although all of our participants felt that use is beneficial, false positives and the way in
  which the warnings are presented, among other things, are barriers to use."
- **Section III.A "Participants":** 20 participants; "Sixteen of our participants are professional developers
  at a large company and 4 are graduate students at North Carolina State University with previous industry
  experience."
- **Section III.F (coded example, Tool Output):** Jason: "like I mentioned with FlexLint it gives you so many
  warnings and sifting through them is so, arduous that whenever I just look at it I’m like ehhh forget this."
  (Supporting Teamwork) John: "The only reason I like the batch results is to communicate, broadcast to the team
  a sense of progress or lack of progress."
- **Section IV.A "Tool Output":** "Out of the 20 people we interviewed, 14 people expressed the negative impacts
  of poorly presented output." "Some of our participants felt, however, that false positives and large volumes
  of warnings would be less burdensome if the way the output is presented was more user-friendly and intuitive."
- **Section IV.A "Customizability":** "For 17 of our participants, customizability is important". On
  suppression:

  > A common problem expressed by most of the participants is the inability to temporarily ignore or suppress certain warnings.

  "not all developers are comfortable with turning warnings completely off. Matt, for example, is afraid that he
  may not remember to turn it back on." Jordan "would prefer that static analysis tools offered a way of
  recording his judgement about that warning", for example "this warning isn’t a problem now, but may be in the
  future if the following conditions are met".
- **Section IV.A "Result Understandability":** "Nineteen of our 20 participants, felt that many static analysis
  tools do not present their results in a way that gives enough information for them to assess what the problem
  is, why it is a problem and what they should be doing differently." James on Eclipse Python plug-ins: "I find
  that the information they provide is not very useful, so I tend to ignore them." The "most frequently mentioned
  difficulty" was lack of or poorly implemented quick fixes.
- **Section IV.B "Workflow Integration":** "Nineteen of the 20 developers we interviewed expressed the importance
  of workflow integration". Lee: having to open another perspective "is a guarantee that unmotivated people will
  not do it"; Jason: "if it disrupts your flow, you’re not gonna use it."
