# Implementation backlog

Task files are the source of truth for status and evidence. Keep this index synchronized. Status values: todo, in_progress, blocked, done. A task is ready when its dependencies are done; begin with T001. Use [the task template](TEMPLATE.md) for additions.

| Task | Deliverable | Dependencies | Status |
| --- | --- | --- | --- |
| [T000](T000-repository-foundation.md) | Repository foundation | none | done |
| [T001](T001-executable-contracts-and-configuration.md) | Executable contracts and configuration | T000 | todo |
| [T002](T002-versioned-ingestion-and-standardization.md) | Versioned ingestion and standardization | T001 | todo |
| [T003](T003-brics-and-morgan-fingerprints.md) | BRICS and Morgan fingerprints | T001, T002, T006 | todo |
| [T004](T004-ssm-and-hybrid-vocabulary-adapters.md) | SSM and hybrid vocabulary adapters | T003, T006 | todo |
| [T005](T005-exact-retrieval-and-index.md) | Exact retrieval and index | T003 | todo |
| [T006](T006-split-and-leakage-enforcement.md) | Split and leakage enforcement | T001, T002 | todo |
| [T007](T007-gba-pilot-evaluation.md) | GBA pilot evaluation | T005, T006 | todo |
| [T008](T008-gs-meta-prior-adapter-and-parity.md) | GS Meta prior adapter and parity | T003, T006 | todo |
| [T009](T009-controlled-structural-prior-ablations.md) | Controlled structural prior ablations | T008, T007 | todo |
| [T010](T010-measured-scale-expansion.md) | Measured scale expansion | T005, T007 | todo |

The first platform milestone is T001-T003 plus T005-T007. T008 can follow T003/T006 without waiting for PubChem scale. SSM/hybrid ablations additionally require T004. T010 is a measured expansion, not permission to launch an unbounded download or training job.

Task changes must record acceptance evidence. Planned dependencies, licenses, snapshots and budgets remain explicit unresolved implementation work. No scientific experiment is complete at scaffold creation.
