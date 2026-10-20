---
source_handle: wohlin-hybrid-search-snowballing-2022
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2307.02612
provenance: source-direct
substrate_confidence: source-direct
source_class: peer-reviewed empirical replication (preprint of Information and Software Technology article, DOI 10.1016/j.infsof.2022.106908, as stated on the preprint)
---

# Successful Combination of Database Search and Snowballing for Identification of Primary Studies in Systematic Literature Studies (Wohlin, Kalinowski, Romero Felizardo, Mendes, 2022)

## Source structure and scope
Claes Wohlin (BTH), Marcos Kalinowski (PUC-Rio), Katia Romero Felizardo (UTFPR), Emilia
Mendes (BTH). arXiv 2307.02612 preprint, 30 pages; final version in Information and Software
Technology. Replicates an SLR on industry-academia collaboration (IAC) in SE using a hybrid
search (Scopus start set + iterative backward/forward snowballing) and compares four hybrid
variants. Engagement depth: full text extracted; abstract, related work (§2, Table 2), method
(§3-4), results (§6, Tables 4-5) and conclusions (§8) read.

## Anchored details
- **Abstract / §8:** the hybrid strategy "identified 30% more primary studies and even more
  when focusing only on peer-reviewed articles"; "a strong contender".
- **§6.3, Table 4:** original SLR listed 33, replication 43; "the number of publications
  included by both the original SLR and its replication is 20 articles". The original included
  nine publications not in the replication even after removing four non-peer-reviewed items;
  of these, two were among the replication's "borderline" articles, one was excluded on
  scope advice, one scored zero at abstract level, one was excluded after full text.
- **§6.4, Table 5:** start set + full iterative backward*forward snowballing found 43;
  backward||forward in parallel 23; backward then forward 38; forward then backward 23.
  "their performance is highly dependent on the start set"; "When having a round with few
  articles in backward or forward snowballing, we risk that the procedure stops early."
  Snowballing iterates until a round yields no new included articles (as per Wohlin 2014
  guidelines described in §3.2).
- **§3.2 / §4.2.4 Wild cards and borderline articles:** a wild card lets each reviewer
  nominate an article that failed the score threshold so it is carried forward; borderline
  articles (score of three) are listed separately for transparency so readers can judge them.
  One wild card ended among the included articles.
- **§2, Table 2 (cited-by-this-source summaries of prior studies):** Wohlin et al. attribute
  to Jalali and Wohlin (2012) that database search and backward snowballing yielded mostly the
  same included articles and similar conclusions; to Badampudi et al. (2015) that snowballing
  effectiveness is comparable to database search and "its reliability is highly dependent on
  the creation of a suitable start set"; to Kitchenham et al. (2010) that digital-library
  searches find more than manual searches but possibly of lower quality; to Dieste et al.
  (2009) that "It is not straightforward to optimise a search strategy for retrieving SE
  experiments articles"; and summarise Zhang et al. (2011) QGS as terminating when
  quasi-sensitivity >= 80%.
- **§8:** alternative hybrid strategies save effort "although missing some articles"; choose
  based on start-set characteristics; "Further research into adaptive (in relation to the
  start set) hybrid search strategies is needed."
