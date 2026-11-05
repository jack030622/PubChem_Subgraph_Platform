# T007 GBA pilot evaluation

Status: todo
Owner: unassigned
Dependencies: T005, T006

## Goal and deliverables

Implement observed-label weighted voting with evidence, abstention and validation-only selection.

## Acceptance criteria

- Compute weights using only eligible observed binary labels and declared neighbor policy.
- Zero evidence yields null score and insufficient_evidence.
- Return neighbor provenance; predictions never mutate observations.
- Report AP, ROC-AUC where defined, prevalence, coverage, counts and frozen-threshold metrics.
- Compare BRICS and Morgan with identical splits; calibration is validated before probability claims.

## Evidence

Not started. Add validation commands, outcomes, artifact IDs, and limitations before marking done.
