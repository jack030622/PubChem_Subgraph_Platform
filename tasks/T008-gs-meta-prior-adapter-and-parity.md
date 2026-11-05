# T008 GS Meta prior adapter and parity

Status: todo
Owner: unassigned
Dependencies: T003, T006

## Goal and deliverables

Create an isolated pinned GS-Meta integration and structural adjacency injection.

## Acceptance criteria

- Document a reproducible separate Python 3.7 environment and license/source provenance.
- Verify imported molecule ordering, vocabulary/index identities and label masks.
- With lambda=0 compare adjacency and predictions against the unchanged reference on a frozen fixture; record tolerances and evidence.
- Mix pre-top-k scores for nonzero lambda while preserving masks, topology policy and edge budget.
- Preserve encoder, selector and molecule-property behavior.
- New resumable checkpoints capture optimizer/scheduler/RNG/sampler state.

## Evidence

Not started. Add validation commands, outcomes, artifact IDs, and limitations before marking done.
