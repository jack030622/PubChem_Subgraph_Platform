# T001 Executable contracts and configuration

Status: todo
Owner: unassigned
Dependencies: T000

## Goal and deliverables

Implement strict configuration and table/manifest validators. Select and lock core dependencies in a new environment.

## Acceptance criteria

- Validate JSON Schema and reject incomplete manifests, invalid paths, unknown configuration fields, and unresolved runtime values.
- Validate molecule, observation, component, fingerprint, split, and prediction records against the documented contract.
- Reject baseline output roots using resolved paths, including symlinks.
- Test missing-label semantics, incompatible versions, invalid counts, and malformed IDs.
- Document and lock compatible RDKit, sparse storage, Parquet and analysis dependencies; do not alter legacy environments.

## Evidence

Not started. Add validation commands, outcomes, artifact IDs, and limitations before marking done.
