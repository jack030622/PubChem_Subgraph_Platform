# T012 Assay-selection task and pilot decision brief

Status: todo
Owner: unassigned
Dependencies: T000

## Goal and deliverables

Create a reviewable decision brief for the first assay-selection virtual-screening experiment. Start from [the shared literature brief](../docs/research/assay-selection-brief.md) and the accepted ADR 0002. Keep the current phase-1/phase-2 contract intact while evaluating whether a low-label target-AID pilot should be added or prioritized. This is suitable for the local-notebook agent and can run independently of T001 implementation on the GPU server.

## Acceptance criteria

- Compare at least two concrete task definitions: current known-assay phase-1/phase-2 retrieval/GBA and a target-assay low-label source-selection pilot. State query, available labels, output, candidate pool, and decision value for each.
- Ground the comparison in AssayMatch, MetaHeta, and Assay2Mol with precise paper sections/figures/tables. Distinguish published results from inferences and project hypotheses.
- Draft a bounded PubChem AID eligibility and outcome policy, split/label-access diagram, required metadata, and failure modes without downloading the full corpus or launching training.
- Specify baseline selectors, fixed downstream predictor, matched budgets, primary metrics, and ablations that isolate assay selection from vocabulary, candidate retrieval, GBA, and graph effects.
- Write unresolved choices as explicit recommendations for the researcher/mentor. Do not mark a new scientific protocol accepted or edit ADR 0002 until a decision is made.

## Evidence

Not started. Record source links/sections, any bounded data inspection, branch/commit, checks, feasibility limits, and the resulting decision brief before marking done.
