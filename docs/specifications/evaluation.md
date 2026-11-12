# Evaluation protocol

Register dataset snapshot, task, split hash, fit scope, retrieval corpus, label masks, metrics, selection policy, seeds, and resource budget before each experiment.

| Task | Holdout unit | Allowed evidence |
| --- | --- | --- |
| Phase 1: known molecule, known assay | hold out observed molecule-AID edges under an explicit access mask | only other declared observed edges; no copy of the held-out result |
| Phase 2: unseen molecule, known assay | hold out entire molecule identities and structural duplicates; assess scaffold generalization | training molecule labels and a frozen permitted structural corpus |
| Phase 3: known molecule, new assay (deferred) | hold out assay/AID; predeclare zero-shot or a fixed support-label budget | meta-training assay labels and, for few-shot only, support labels |

Do not pool these tasks. Phase 1 validates the workflow and is not evidence of generalization to unseen structures; hide the target edge and all duplicate copies of its outcome. Phase 2 tests the main new-molecule claim. Deduplicate before splitting and prevent hidden labels and duplicate test structures from re-entering via PubChem. Unknown entries are not ground truth: evaluate by masking observed outcomes. For phase 3, declare support size and molecule overlap; use a molecule-disjoint variant for claims about both new tasks and new molecules.

Strict inductive vocabulary/IDF fitting uses training structures only. Frozen external unlabeled vocabulary is a separate setting with provenance and overlap audit. Including evaluation structures in corpus fitting is transductive; report it explicitly. Held-out query labels are never permitted.

A shared structural vocabulary and global clusters may fit only the declared unlabeled corpus. Assay-specific SSM selection and reranking must fit only that assay's allowed training outcomes. If phase 1 uses structures already indexed, report it as a transductive structural setting. Do not use evaluation outcomes for clusters, graph edges, SSM, reranking, thresholds, or model selection.

## Metrics

Report AP, ROC-AUC where defined, class prevalence, counts, per-assay and macro results. AP is average precision, not trapezoidal PR-AUC. Explain undefined metrics. Select k, thresholds, weights, calibration, vocabulary settings, and lambda on validation only. Freeze them for test.

GBA reports coverage and covered-population metrics with counts; never silently drop abstentions. Any fallback needs a specified training-only prior and separate full-population metrics. Assess calibration with reliability summaries and Brier score when using probabilities.

Retrieval reports recall-at-k against exact search with identical eligibility, metric, and tie policy, plus query p50/p95, memory, storage, and build time. Compare global candidate search and assay-conditioned reranking at the same candidate and label budgets. Report held-out active enrichment or hit rate at an explicitly fixed top-k, representation coverage, and scaffold diversity. Global clustering reports stability under resampling or snapshot updates and held-out assay outcome consistency; compare with Morgan at matched coverage/cluster budgets. A plot or retrieval agreement alone is not biological prediction quality.

Ablate Morgan, BRICS, SSM, hybrid mappings, and any graph propagation separately. Check whether gains persist across assays and label budgets, and whether representation/cluster updates preserve old artifact provenance. Search on all clusters or measure recall and lost active chemotypes when restricting to clusters.

## GS Meta tracks

Paper-protocol: original SIDER split, 2-way 10-shot, seeds 0-9, 2,000 steps, evaluation every 100, best-test selection. The historical 83.9388 +/- 0.1620 percent population-SD result belongs only here.

Primary improvement: validation-selected checkpoints/hyperparameters and one-time test. Rerun original GS-Meta under this protocol. Match encoder, selector, molecule-property edges, edge budget, episodes, seeds, and training budget. Report per-seed paired differences and uncertainty.

Variants: original, Morgan, BRICS, SSM, SSM-to-BRICS, shuffled prior. Reproducibly shuffle molecule assignment and document degree/sparsity effects; avoid topology confounds. Prior-only and molecule-only comparisons are secondary.

## Required gates

Check identity/scaffold disjointness, held-out-edge masking, label-access masks, global-versus-assay fit scope, immutable transform, version compatibility, prior-disabled parity, absence of primary-track test selection, and complete split/config/source/environment provenance.
