# T001 Executable contracts and configuration

Status: todo
Owner: unassigned
Dependencies: T000

## Goal and deliverables

Before freezing schemas, register a compact pilot protocol: selected AIDs, outcome policy, phase-1/phase-2 label access, permitted structural corpus, and comparison methods. Then implement strict configuration and table/manifest validators. Select and lock core dependencies in a new environment.

## Acceptance criteria

- Validate JSON Schema and reject incomplete manifests, invalid paths, unknown configuration fields, and unresolved runtime values.
- Record a concrete pilot protocol and why the selected AIDs permit phase-1 held-out-edge and phase-2 held-out-molecule evaluation.
- Validate molecule, assay, observation/readout, component, fingerprint, split, cluster-assignment, evidence-link, and prediction records against the documented contract.
- Reject baseline output roots using resolved paths, including symlinks.
- Test missing-label semantics, incompatible versions, invalid counts, and malformed IDs.
- Document and lock compatible RDKit, sparse storage, Parquet and analysis dependencies; do not alter legacy environments.

## Evidence

Not started. Add validation commands, outcomes, artifact IDs, and limitations before marking done.
