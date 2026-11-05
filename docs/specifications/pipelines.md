# Pipeline specifications

The command names below are planned interfaces. The scaffold implements only help and version.

## Ingestion and standardization

`psp ingest` and `psp standardize`: register source URLs, snapshot, inventory, retrieval time, and checksums. Pilot sampling must be reproducible and disclose bias. Support retries and interrupted shards with bounded workers. Emit molecule, mapping, and failure tables without overwriting raw records.

## Vocabulary and fingerprints

`psp vocab fit` and `psp fingerprints encode`: separate fit and transform. Backends are BRICS, training-label SSM, SSM-to-BRICS, and a Morgan comparator. Freeze feature order; record frequency/size limits, coverage, and OOV. Fit IDF on the allowed corpus only.

For multi-assay SSM, select within training partitions/tasks, union structural identities, and preserve per-assay scores with selection budgets. A supervised PubChem-wide vocabulary requires explicit labels and fit scope. Map SSM candidates to containing BRICS fragments under defined attachment semantics. Cross-fragment candidates are initially unmapped; bounded union expansion is a separate experiment. Report mapping multiplicity and failure rates. Rust acceleration requires reference parity before replacement.

## Retrieval

`psp index build` and `psp search`: initial binary metric is intersection/union Jaccard (Tanimoto). Cosine is a comparator; count Tanimoto requires a registered formula. Exact sparse scoring is the oracle. Tie-break by molecule ID. Apply protocol eligibility, self, and duplicate filters consistently.

Use inverted postings, then exact reranking. Candidate truncation/common-fragment pruning/approximate backends require recall-at-k checks against the exact oracle. Return molecule ID, score, shared components, and index version. Fewer than k positive matches is valid. Reject incompatible versions.

## GBA

`psp predict gba`: initial policy is global top-k retrieval followed by assay-label filtering. Declare this explicitly and report lost coverage. Only eligible observed binary labels contribute. Score is sum(weight * label) / sum(weight), with nonnegative similarity weights and frozen k/min-similarity/min-evidence parameters selected on validation.

No effective positive weight or insufficient neighbors produces insufficient_evidence and a null score. Return neighbor evidence and coverage. Calibrate on validation predictions if probability claims are needed. Never feed predictions into the observation table.

## GS Meta prior

The entry point belongs in `integrations/gs_meta/` and its separate environment. Inject between `EdgeUpdateNetwork` and `InductiveGraphConnector.connect_graph` in `TaskRelationNet.forward_inductive`.

For lambda > 0, mix learned pre-top-k sigmoid scores and structural scores: A = TopK((1-lambda) * A_learned + lambda * S). Preserve baseline diagonal masking, directed topology policy, and edge budget. Keep S fixed within an episode unless registered otherwise.

For lambda = 0, execute the unchanged baseline adjacency path including ordering/ties and verify adjacency/prediction parity. Preserve molecule-property edges and label masks. Empty/OOV structure yields zero structural scores and a reported coverage count. Fixed meta-training vocabulary and support-only adaptation are separate variants.

New resumable checkpoints include model, optimizer, scheduler, RNG, sampler, config, and step. Historical state dictionaries remain reference artifacts, not exact-resume checkpoints.
