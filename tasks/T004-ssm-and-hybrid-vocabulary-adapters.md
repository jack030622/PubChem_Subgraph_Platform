# T004 SSM and hybrid vocabulary adapters

Status: todo
Owner: unassigned
Dependencies: T003, T006

## Goal and deliverables

Port the required pinned SSM behavior and implement assay-scoped selection linked to the shared BRICS component registry. Preserve cross-assay reuse provenance rather than assuming a single supervised universal vocabulary.

## Acceptance criteria

- Review upstream/collaborator licenses and record code provenance before importing.
- Preserve strict count checks and probability metric parity tolerance 1e-7 where applicable to baseline comparisons.
- Mine training partitions/tasks only; retain per-assay scores, label budgets, and selection provenance.
- Quantify shared components across AIDs, vocabulary coverage on new molecules, and mapping stability under resampling. Compare BRICS-only, SSM-only, and hybrid representations at matched feature budgets.
- Report unmapped/cross-fragment candidates; bounded unions remain a separate variant.
- Do not assume useful DiSC-2 pairs from the historical zero-pair result.
- If Rust code becomes available, prove parity before benchmarking or enabling it.

## Evidence

Not started. Add validation commands, outcomes, artifact IDs, and limitations before marking done.
