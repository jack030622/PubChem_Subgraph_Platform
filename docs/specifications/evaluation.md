# Evaluation protocol

Register dataset snapshot, task, split hash, fit scope, retrieval corpus, label masks, metrics, selection policy, seeds, and resource budget before each experiment.

| Task | Holdout unit | Allowed evidence |
| --- | --- | --- |
| New molecule to known assay (first milestone) | identity groups followed by scaffold split | training molecules and observed labels |
| Missing edge | molecule-assay edges | only other explicitly available edges |
| New assay few-shot | task split with support/query episodes | meta-training labels and held-out task support labels |

Do not pool these tasks. Deduplicate before splitting. Prevent hidden labels and duplicate test structures from re-entering via PubChem. For few-shot tasks, declare molecule overlap; use a molecule-disjoint variant for claims about both new tasks and new molecules.

Strict inductive vocabulary/IDF fitting uses training structures only. Frozen external unlabeled vocabulary is a separate setting with provenance and overlap audit. Including evaluation structures in corpus fitting is transductive; report it explicitly. Held-out query labels are never permitted.

## Metrics

Report AP, ROC-AUC where defined, class prevalence, counts, per-assay and macro results. AP is average precision, not trapezoidal PR-AUC. Explain undefined metrics. Select k, thresholds, weights, calibration, vocabulary settings, and lambda on validation only. Freeze them for test.

GBA reports coverage and covered-population metrics with counts; never silently drop abstentions. Any fallback needs a specified training-only prior and separate full-population metrics. Assess calibration with reliability summaries and Brier score when using probabilities.

Retrieval reports recall-at-k against exact search with identical eligibility, metric, and tie policy, plus query p50/p95, memory, storage, and build time. Retrieval agreement is not biological prediction quality.

## GS Meta tracks

Paper-protocol: original SIDER split, 2-way 10-shot, seeds 0-9, 2,000 steps, evaluation every 100, best-test selection. The historical 83.9388 +/- 0.1620 percent population-SD result belongs only here.

Primary improvement: validation-selected checkpoints/hyperparameters and one-time test. Rerun original GS-Meta under this protocol. Match encoder, selector, molecule-property edges, edge budget, episodes, seeds, and training budget. Report per-seed paired differences and uncertainty.

Variants: original, Morgan, BRICS, SSM, SSM-to-BRICS, shuffled prior. Reproducibly shuffle molecule assignment and document degree/sparsity effects; avoid topology confounds. Prior-only and molecule-only comparisons are secondary.

## Required gates

Check identity/scaffold disjointness, label-access masks, fit scope, immutable transform, version compatibility, prior-disabled parity, absence of primary-track test selection, and complete split/config/source/environment provenance.
