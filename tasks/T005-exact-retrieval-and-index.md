# T005 Exact retrieval and index

Status: todo
Owner: unassigned
Dependencies: T003

## Goal and deliverables

Implement exact sparse search and a versioned inverted index on a frozen eligible corpus.

## Acceptance criteria

- Exact binary Jaccard and deterministic tie-breaking match hand-computed fixtures.
- Empty vectors, self/identity exclusions, fewer-than-k matches, and version mismatch are handled explicitly.
- Indexed retrieval matches the oracle if exact; any candidate limits have measured recall-at-k.
- Record build time, index bytes, peak memory, query p50/p95, and query sampling.
- Index updates are immutable and restart-safe.

## Evidence

Not started. Add validation commands, outcomes, artifact IDs, and limitations before marking done.
