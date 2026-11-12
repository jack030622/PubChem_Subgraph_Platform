# T010 Measured scale expansion

Status: todo
Owner: unassigned
Dependencies: T005, T007, T011

## Goal and deliverables

Expand shared vocabulary, clustering, candidate retrieval, assay reranking, and evidence update only after pilot profiling; introduce approximation/distribution when measurements justify it.

## Acceptance criteria

- Register hardware and storage budgets before each 100k/1m/larger run.
- Measure throughput, RSS, disk, index size, recall, cluster coverage/stability, assay reranking time, and latency; compare against pilot predictions.
- Bound component matching/candidate costs and avoid all-pairs materialization.
- Document snapshot/index update, failure recovery and OOV policy.
- Use an ADR for any new service/distributed/approximate backend and include quality evidence.

## Evidence

Not started. Add validation commands, outcomes, artifact IDs, and limitations before marking done.
