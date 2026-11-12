# T007 GBA pilot evaluation

Status: todo
Owner: unassigned
Dependencies: T005, T006

## Goal and deliverables

Implement observed-label weighted voting with evidence, abstention, and validation-only selection. Establish Morgan and BRICS baselines for phase-1 held-out-edge and phase-2 unseen-molecule evaluation, keeping the results separate.

## Acceptance criteria

- Compute weights using only eligible observed binary labels and declared neighbor policy.
- Zero evidence yields null score and insufficient_evidence.
- Return neighbor provenance; predictions never mutate observations.
- Report AP, ROC-AUC where defined, prevalence, coverage, counts and frozen-threshold metrics.
- Compare BRICS and Morgan with identical splits, candidate/label budgets, and eligibility masks; calibration is validated before probability claims.
- In phase 1 exclude the hidden molecule-AID outcome and duplicates; in phase 2 exclude all held-out molecule identities.
- Report top-k active enrichment or hit rate, scaffold diversity, and abstention/coverage alongside aggregate prediction metrics.

## Evidence

Not started. Add validation commands, outcomes, artifact IDs, and limitations before marking done.
