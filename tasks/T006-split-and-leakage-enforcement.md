# T006 Split and leakage enforcement

Status: todo
Owner: unassigned
Dependencies: T001, T002

## Goal and deliverables

Implement three explicit protocols: phase-1 held-out observed edges for known molecules/AIDs; phase-2 molecule-identity/scaffold holdout for known AIDs; deferred phase-3 new-AID support/query split. Enforce label-access masks for each.

## Acceptance criteria

- Prove required split disjointness after standardization and duplicate grouping.
- Audit external-corpus overlaps and prevent hidden labels from re-entering evidence.
- Enforce vocabulary/IDF fit scope and query immutability.
- Represent phase-1 known-molecule/known-assay, phase-2 unseen-molecule/known-assay, and phase-3 new-assay task policies separately.
- In phase 1 hide every copy of the target outcome, including alternate SID/source mappings; in phase 2 hold out duplicate structures entirely.
- Distinguish a frozen unlabeled structural corpus from outcome-bearing evidence and document transductive structure access.
- Freeze split manifest hashes and test support/query label access.

## Evidence

Not started. Add validation commands, outcomes, artifact IDs, and limitations before marking done.
