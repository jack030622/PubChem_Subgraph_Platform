# Source provenance

- [PCBA handoff tag](https://github.com/jack030622/pcba_project/tree/pcba-research-handoff-20261005): commit `6492777c42d93d8b9978bb5d93d14d197a614332`.
- [Project handoff](https://github.com/jack030622/pcba_project/blob/pcba-research-handoff-20261005/docs/PROJECT_HANDOFF.md).
- [GS Meta baseline](https://github.com/jack030622/pcba_project/blob/pcba-research-handoff-20261005/docs/GS_META_BASELINE.md).
- [Notion PCBA research](https://app.notion.com/p/3ed74d6fa028809dbc70d145a474c2e2), consulted in the preceding design conversation; last edited 2026-10-02.

SSM results are selected development CV, not final outer holdout. Exact DiSC-2 retained zero pairs. GS-Meta reproduced SIDER 10-shot using best-test selection. The separate seed-0 checkpoint is not the checkpoint behind the 10-seed aggregate; its same-seed discrepancy remains unresolved.

Notion motivates structural priors, retrieval, and GBA. The 10-million molecule and 1-million component figures are illustrative. Collaborator Rust/SSM-BRICS availability and licensing require verification.

Implementation references: [RDKit BRICS](https://www.rdkit.org/docs/source/rdkit.Chem.BRICS.html), [PubChem downloads](https://pubchem.ncbi.nlm.nih.gov/docs/downloads), and [SubDyve](https://proceedings.iclr.cc/paper_files/paper/2026/hash/02cf868040aa0f0a1e1121cf255fdcfb-Abstract-Conference.html). SubDyve already combines SSM fingerprints, molecular similarity networks, and activity propagation; compare it when claiming method novelty. Verify concrete resource formats and current access rules during implementation.

Assay-selection literature for the next research discussion: [AssayMatch](https://arxiv.org/html/2511.16087), [MetaHeta](https://arxiv.org/html/2610.07079), and [Assay2Mol](https://aclanthology.org/2025.emnlp-main.1390.pdf). See [the meeting brief](research/assay-selection-brief.md) for their different inputs, outputs, evidence, and the proposed pilot question.

Historical local baseline: `/data/project/jack030622/pcba_project`. Put machine-specific runtime paths in untracked environment configuration; never write into this baseline.
