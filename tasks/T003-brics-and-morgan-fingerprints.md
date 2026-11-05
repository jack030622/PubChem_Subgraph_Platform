# T003 BRICS and Morgan fingerprints

Status: todo
Owner: unassigned
Dependencies: T001, T002, T006

## Goal and deliverables

Implement training-scoped BRICS vocabulary and a Morgan comparator with immutable binary encodings.

## Acceptance criteria

- Freeze component IDs, vocabulary ordering, toolkit and representation policy.
- Test attachment labels, empty/all-OOV molecules and canonical reparse behavior.
- Separate fit/transform; queries cannot append columns.
- Record Morgan parameters/collision semantics separately from interpretable BRICS component IDs.
- Measure vocabulary size, nonzeros per molecule and OOV/coverage on frozen pilot splits.

## Evidence

Not started. Add validation commands, outcomes, artifact IDs, and limitations before marking done.
