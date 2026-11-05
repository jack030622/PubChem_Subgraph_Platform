# T004 SSM and hybrid vocabulary adapters

Status: todo
Owner: unassigned
Dependencies: T003, T006

## Goal and deliverables

Port the required pinned SSM behavior and implement assay-scoped selection plus SSM-to-BRICS mapping.

## Acceptance criteria

- Review upstream/collaborator licenses and record code provenance before importing.
- Preserve strict count checks and probability metric parity tolerance 1e-7 where applicable to baseline comparisons.
- Mine training partitions/tasks only; retain per-assay scores and selection budgets.
- Report unmapped/cross-fragment candidates; bounded unions remain a separate variant.
- Do not assume useful DiSC-2 pairs from the historical zero-pair result.
- If Rust code becomes available, prove parity before benchmarking or enabling it.

## Evidence

Not started. Add validation commands, outcomes, artifact IDs, and limitations before marking done.
