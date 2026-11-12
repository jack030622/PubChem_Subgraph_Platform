# T011 Assay-conditioned retrieval and cluster evaluation

Status: todo
Owner: unassigned
Dependencies: T004, T005, T007

## Goal and deliverables

Link shared BRICS components to assay-specific SSM patterns for candidate reranking. Test whether this improves evidence retrieval, GBA, and structural-cluster utility across multiple AIDs. Implement only the evidence links needed to audit retrieved observations; graph propagation is an optional separately ablated variant.

## Acceptance criteria

- Register candidate retrieval and assay-specific reranking scores, feature/label budgets, fit splits, and all source versions. Explain how SSM patterns map to BRICS components and how unmapped patterns are handled.
- Compare Morgan-only, BRICS-only, SSM-only, and hybrid methods on identical phase-1 and phase-2 splits; include global-only and reranking-only ablations.
- Report top-k held-out active enrichment/hit rate, GBA AP/coverage, scaffold diversity, feature coverage, and latency with per-AID results and uncertainty.
- Compare global structural clusters at matched coverage/budgets and report stability plus held-out assay outcome consistency; test any cluster-based candidate restriction against exact full-corpus recall and lost active chemotypes.
- Verify no evaluation outcome enters global clusters, SSM selection, graph evidence, reranking, or GBA; preserve traceable observation IDs and abstention reasons.
- Quantify component reuse, feature coverage, and retrieval gains across the pilot AIDs. Do not claim predictive transfer to entirely unseen AIDs without the deferred phase-3 protocol. Do not claim chemical/biological meaning based on visual clustering alone; document interpretable motifs and independent evidence for their association.

## Evidence

Not started. Add validation commands, per-assay results, artifact IDs, ablations, costs, and limitations before marking done.
