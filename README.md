# PubChem Subgraph Platform

Research infrastructure for SSM/BRICS subgraph vocabularies, versioned PubChem molecule data, similarity retrieval, guilt-by-association prediction, and GS-Meta structural-prior ablations.

## Current state

Scaffold and specifications only. Ingestion, mining, search, prediction, and training are not implemented. No PubChem download or new training has been launched. The existing PCBA repository remains a read-only baseline.

## Start here

1. Read [agent rules](AGENTS.md) and [architecture](docs/architecture.md).
2. Review [data contracts](docs/specifications/data_contracts.md), [pipeline specifications](docs/specifications/pipelines.md), and [evaluation protocol](docs/specifications/evaluation.md).
3. Select a ready task from the [backlog](tasks/README.md).
4. Preserve [baseline identities](manifests/baselines/pcba_handoff.json).

## Development

Create a new Python >=3.10 environment. Do not install into baseline environments.

```sh
python3.10 -m venv .venv
.venv/bin/python -m pip install -e .
psp --help
psp --version
.venv/bin/python scripts/validate_scaffold.py
```

Only CLI help/version is implemented. The scaffold runtime is standard-library only; packaging uses setuptools. Runtime dependencies and a lock file are selected during implementation. `.env.example` documents future runner paths; the scaffold does not load `.env` automatically.

## Layout

- `src/pubchem_subgraph_platform/`: shared platform modules and CLI.
- `integrations/`: isolated SSM and GS-Meta adapters.
- `configs/`: versioned design templates, not runnable pipelines yet.
- `schemas/` and `manifests/`: artifact contracts and compact provenance.
- `experiments/`: retrieval, GBA, and structural-prior protocols.
- `tasks/`: task dependencies, acceptance criteria, and evidence.
- `tests/`: bounded fixtures, contract tests, and integration tests added with implementation.
- `reports/`: compact measured summaries only.

The first milestone is a fixed small BRICS/Morgan corpus, exact retrieval, and GBA. Reuse these features in GS-Meta without waiting for full PubChem scale. Expansion requires measured time, memory, storage, and retrieval quality. See [sources](docs/sources.md) for historical results and limitations.

No project license has been selected. Review licensing and preserve attribution before importing upstream code. Large data, indices, matrices, and checkpoints belong outside Git and outside baseline directories.
