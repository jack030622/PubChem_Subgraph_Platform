# Data contracts

Contract version 0.1 specifies logical records. Executable table validation is T001. IDs are opaque strings unless specified otherwise.

| Record | Required fields and invariants |
| --- | --- |
| molecule | molecule_id, canonical_structure, standardization_version, structure_hash; identity includes policy and collision checks |
| source_mapping | source, snapshot_id, source_record_id, CID/SID if available, molecule_id, raw_record_ref; many-to-one mappings permitted |
| standardization_failure | snapshot_id, source_record_id, stage, reason; no silent row loss |
| assay | assay_id/AID, depositor, protocol/outcome method, stated target if any, assay type, source snapshot; target mapping is not interchangeable with assay identity |
| assay_observation | observation_id, molecule_id, assay_id, SID/source_record_ref, snapshot_id, original outcome; preserve conflicting measurements |
| assay_readout | observation_id, readout name/type, raw value, relation, unit, concentration/condition when available; retain source semantics |
| split | split_id, molecule/task/edge membership, identity grouping version, seeds, source hash, label-access policy |
| component | component_id, canonical representation, representation kind, identity policy, provenance |
| vocabulary | vocabulary_id, ordered component IDs, fit_scope, applicable split_id, algorithm/config hash, source artifact IDs, toolkit versions |
| assay_selection | assay_id, component_id, score, method, fit split; retain provenance across union |
| fingerprint | molecule_id, vocabulary_id, standardization_version, encoding, sorted unique indices, optional counts, OOV statistics |
| index | index_id, fingerprint artifact ID, metric, candidate policy, eligible corpus, build configuration |
| cluster_assignment | molecule_id, cluster_id, representation/index version, algorithm/config hash; global clusters must be label-free |
| evidence_link | source/target entity IDs, relation type, observed-vs-derived flag, artifact version, source record references; predictions cannot be observed links |

## Chemistry and labels

Standardization declares sanitization, mixtures/salts, charge, tautomers, stereochemistry, isotopes, and toolkit version. Preserve raw structures. Group duplicate structures before splitting and keep all merged source references.

Outcomes: active, inactive, inconclusive, unspecified, probe. Probe remains a distinct source outcome and joins the binary active class only under an explicit view policy. An unmeasured label is absent, not inactive. Binary views use a versioned eligibility/aggregation policy. Preserve endpoint context and source units where present; distinct assays are not interchangeable properties.

The same molecule may have several readouts in one AID and several AIDs linked to one target. Preserve each result with its AID, units, qualifiers, and conditions. Cross-assay aggregation is a separately versioned policy, not an implicit merge.

## Feature identity

Component IDs hash the canonical structural representation plus its policy, with collision verification. Feature indices are local to a vocabulary version. Binary encoding means presence; count encoding requires an explicit occurrence rule. Unique BRICS decomposition output is not an occurrence count. Attachment labels, leaf/non-leaf settings, and decomposition-vs-substructure matching are part of the representation contract.

Define empty-empty similarity as zero. Empty/all-OOV vectors provide no positive evidence; invalid encoding is a separate failure. Reject nonfinite/negative counts and version mismatches before scoring. Query transform never extends the vocabulary.

Global structural components and cluster membership use no assay labels. Assay-specific SSM selections store their fit split and label budget. Reranking records both candidate-index and assay-selection versions. Molecule identity uses canonical structure, not a similarity fingerprint or cluster ID.

## Predictions

Required fields: prediction_id, query molecule ID, assay ID, nullable score, score_kind, status, model/config version, index ID, observation snapshot, evidence neighbor IDs, observed label references, similarities, effective weight sum, cluster/search and reranking versions, and timestamp.

Statuses: ok, insufficient_evidence, invalid_structure, incompatible_artifact. Store predictions separately from observations. Uncalibrated weighted votes are scores, not validated probabilities.

## Artifact lifecycle

Data-bearing stages use `schemas/artifact_manifest.schema.json`. Record input IDs, SHA-256 hashes, relative shard paths, row counts, source commit, environment identity, config hash, seed when applicable, and fit scope. Reject absolute paths and parent traversal. Write shards in staging, verify them, then atomically publish a complete manifest. Consumers require complete status and compatible versions. Resume only when inputs/config match. Updates create immutable versions; incremental indices identify their parent and eligible corpus.
