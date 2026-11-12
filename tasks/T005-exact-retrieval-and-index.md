# T005 Exact retrieval and index

Status: todo
Owner: unassigned
Dependencies: T003

## Goal and deliverables

Implement exact sparse search and a versioned inverted index on a frozen eligible corpus. Establish label-free BRICS/Morgan structural clusters as a baseline for navigation and candidate selection.

## Acceptance criteria

- Exact binary Jaccard and deterministic tie-breaking match hand-computed fixtures.
- Empty vectors, self/identity exclusions, fewer-than-k matches, and version mismatch are handled explicitly.
- Indexed retrieval matches the oracle if exact; any candidate limits have measured recall-at-k.
- Version global label-free clusters; report coverage and stability, and assess held-out assay outcome consistency without fitting clusters on those outcomes.
- If cluster membership restricts candidates, report lost full-corpus neighbors and active chemotypes.
- Record build time, index bytes, peak memory, query p50/p95, and query sampling.
- Index updates are immutable and restart-safe.

## Evidence

Not started. Add validation commands, outcomes, artifact IDs, and limitations before marking done.
