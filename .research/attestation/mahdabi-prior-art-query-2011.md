---
source_handle: mahdabi-prior-art-query-2011
fetched: 2026-10-20
source_url: https://folia.unifr.ch/documents/318549/files/crestani_LNCS_2011.pdf
provenance: source-direct
substrate_confidence: source-direct
source_class: peer-reviewed IR conference paper (repository file name indicates LNCS 2011; venue not read off the document), CLEF-IP 2010 experiments
---

# Building Queries for Prior-art Search (Mahdabi, Keikha, Gerani, Landoni, Crestani)

## Source structure and scope
Parvaz Mahdabi, Mostafa Keikha, Shima Gerani, Monica Landoni, Fabio Crestani (University of
Lugano). 12-page paper; read: abstract, §1 introduction, §2 collection, §3 related work, §4-6
method and parameter results. Automatic query generation from a patent document for prior-art
retrieval on the CLEF-IP 2010 collection.

## Anchored details
- **§1:** "patent retrieval is considered as a recall-oriented application." "the vocabulary
  used in patent applications is very diverse. Writers tend to purposely use many vague terms and
  expression and non-standard terminology in order to avoid narrowing down the scope of their
  invention"; applicants "also develop their own terminologies". Previous work shows the
  effectiveness of incorporating IPC classes; the authors use IPC-class clusters to expand the
  query model, which "will address the vocabulary mismatch since we include words in query which
  are not present in the query topic itself."
- **§4:** retrieved results are filtered to documents sharing at least one IPC class with the
  query patent.
- **§6.3, Tables 1-2 (training set):** recall of generated queries roughly 0.48-0.63 depending on
  field and method (description field best, e.g. LLQM 0.59-0.63; claims 0.48-0.57); beyond about
  100 query terms, adding terms "does not improve the performance anymore".
