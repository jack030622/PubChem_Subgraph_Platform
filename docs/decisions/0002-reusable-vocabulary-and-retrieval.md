# Reusable vocabulary and assay-conditioned retrieval

Status: accepted as the research direction on 2026-11-05. The method and claimed advantages remain hypotheses until evaluated.

The central question is how to link a shared BRICS structural vocabulary with SSM subgraphs selected from individual assays so that a representation can be reused across assays. Compare its retrieval and GBA value with Morgan fingerprints; seek conditions where it is better or complementary rather than presuming a universal replacement.

Separate a label-free global molecular organization from assay-conditioned ranking. Global clusters and candidate indices use frozen structural features. Assay-specific SSM selection uses only the permitted training labels; it may rerank candidates. Observed molecule-assay links, structural links, and component membership provide versioned, inspectable evidence. GBA is a downstream test of the retrieved evidence. Any graph propagation or learned graph model requires a direct ablation against retrieval without it.

Evaluation order: (1) held-out observed edges for molecules and assays already represented in the permitted corpus; (2) entirely held-out molecule identities on known assays, including scaffold-based generalization; (3) new-assay few-shot transfer after its support-label budget is specified. Phase 1 is a feasibility baseline; phase 2 tests the main new-molecule claim. Unknown PubChem entries cannot be scored as ground truth.

The initial method must show an improvement attributable to shared vocabulary, assay-specific adaptation, clustering/search, or their interaction on known AIDs. Reuse of structural components across AIDs is distinct from predicting a previously unseen AID. Compare BRICS alone, SSM alone, Morgan alone, and the hybrid at matched data access and compute. Evaluate retrieval quality, cluster utility, GBA, feature coverage, and cost. GS-Meta prior ablations remain a secondary transfer check. PubChem scale follows measured pilot gains and resource use.

Related work already uses SSM fingerprints, molecular similarity networks, and activity propagation: [SubDyve](https://proceedings.iclr.cc/paper_files/paper/2026/hash/02cf868040aa0f0a1e1121cf255fdcfb-Abstract-Conference.html). This direction must demonstrate its cross-assay vocabulary and retrieval contribution rather than claim novelty for that combination alone.
