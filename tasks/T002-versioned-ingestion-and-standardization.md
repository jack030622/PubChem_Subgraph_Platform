# T002 Versioned ingestion and standardization

Status: todo
Owner: unassigned
Dependencies: T001

## Goal and deliverables

Build a bounded reproducible PubChem assay pilot with raw provenance, molecule identity, assay metadata/readouts, and restart-safe shards.

## Acceptance criteria

- Verify current PubChem source formats/access guidance and register a concrete snapshot plus sampling policy.
- Choose and document salt, charge, tautomer, stereo, isotope and sanitization policies.
- Retain raw records, SID/CID mappings, AID metadata, readout type/unit/qualifier, and source mappings; deterministic identity survives reruns.
- Report parse failures and deduplication; do not silently discard records.
- Interrupted shard resume matches an uninterrupted fixture run; reject input/config mismatch.
- Record pilot throughput, peak RSS, storage, worker count, and source checksums.

## Evidence

Not started. Add validation commands, outcomes, artifact IDs, and limitations before marking done.
