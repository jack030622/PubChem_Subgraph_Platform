# Assay-selection meeting brief

Status: proposal for discussion, not an adopted protocol. This brief lets agents in both environments work from the same literature context without requiring access to Notion or the presentation. The accepted scope remains [ADR 0002](../decisions/0002-reusable-vocabulary-and-retrieval.md).

## Task → prior approach → limit → our question

Practical task under discussion: for a target assay or protein query, select useful prior assay evidence from a large database before ranking candidate molecules for virtual screening. The query type, target-label budget, candidate pool, endpoint, and evaluation split are not yet fixed.

| Paper | Query and output | What it establishes | Boundary for this project |
| --- | --- | --- | --- |
| [AssayMatch](https://arxiv.org/html/2511.16087) (2025 preprint) | New assay description, no test-assay labels → source assays for training | TRAK-derived assay-to-assay utility can tune description embeddings; ChEMBL IC50 study reports better AULC than base embeddings in 9/12 model–target combinations | It already studies prospective assay selection. Its selector does not use the target test assay's molecular contents; a structural selector must show extra predictive utility, not just semantic similarity. The test assays are within selected targets, not a general new-protein benchmark. |
| [MetaHeta](https://arxiv.org/html/2610.07079) (2026 preprint) | Target assay with 4/8/16/32 observed molecules plus related auxiliary assays → continuous activity distribution | Assay heterogeneity can hurt broad meta-learning; conditioning on related auxiliary data helps few-shot prediction on FS-Mol and retrospective compound prioritization | Relatedness already uses target identity, homology, description similarity, and in one controlled setting molecular Tanimoto ordering. Its real-data description rule is a heuristic; test whether the proposed structure-aware selection improves transfer at matched label and predictor budgets. It is not a k=0 evaluation. |
| [Assay2Mol](https://aclanthology.org/2025.emnlp-main.1390.pdf) (EMNLP 2025) | Protein/phenotype text → PubChem BioAssay retrieval/filtering → generated SMILES | PubChem assay retrieval, LLM relevance checks, and counterscreen interpretation can guide computational molecule design; irrelevant assay context may be harmful | The output is molecule generation, not ranking a fixed candidate set. Its docking-based evaluations are not wet-lab hit rates or a direct baseline for candidate activity prediction. |

Proposed question: **Does an assay selector that combines text/target metadata with assay-specific SSM patterns and a shared BRICS vocabulary choose source evidence that improves held-out candidate hit ranking, under the same candidate and label budgets as text and Morgan baselines?** This is a hypothesis to test, not an established advantage. Separate assay selection, molecular candidate retrieval, activity prediction/GBA, and any graph propagation in ablations. A `k=0` target has no target-label-fitted SSM; use only source-assay SSM and permitted unlabeled/metadata features there. Target-assay SSM adaptation belongs to a declared `k>0` setting.

## Decisions required before changing the protocol

1. Is the query an existing AID with protocol text, or a protein target without its own assay? These correspond to different retrieval constraints and baselines.
2. Is the primary target-label budget zero, or 4/8/16 observations? Keep zero-shot and few-shot results separate.
3. Is the output binary hit ranking among fixed candidates or a continuous IC50/pIC50 estimate? Assay endpoint, qualifiers, units, and outcome policy must match the claim.
4. Which PubChem AID family and candidate pool form a bounded first pilot? Identify primary/confirmatory/counterscreen relationships and how repeated measurements are handled.
5. Which selection baselines and metrics make the added structure signal falsifiable? At minimum compare all-data, random, metadata/target rules, text embeddings, Morgan, BRICS, SSM, and hybrid at matched budgets; report per-assay AP and early enrichment as appropriate, coverage, and retrieval cost.
6. How are AIDs/campaigns, molecule identities/scaffolds, and observed outcomes held out? Unknown database entries are not ground truth; evaluate on observed results hidden from all fitting and selection paths.

The meeting-slide draft is in the shared Google presentation; its claims should be checked against these primary paper links. A low-label target-AID candidate-ranking pilot is a **suggested first experiment** because it makes auxiliary assay selection and hit utility measurable. It does not replace phase 1/2 or launch phase 3 until a decision updates the ADR, evaluation spec, and task dependencies.
