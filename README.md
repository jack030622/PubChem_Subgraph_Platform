# PubChem Subgraph Platform

Research infrastructure for a reusable BRICS/SSM molecular vocabulary, structure-aware clustering, assay-conditioned retrieval, evidence-backed guilt-by-association prediction, and secondary GS-Meta structural-prior ablations.

## Current state

Scaffold and specifications only. Ingestion, mining, search, prediction, and training are not implemented. No PubChem download or new training has been launched. The existing PCBA repository remains a read-only baseline.

## Start here

1. Read [agent rules](AGENTS.md), the [two-agent workflow](docs/agent-workflow.md), [architecture](docs/architecture.md), and the [research-direction decision](docs/decisions/0002-reusable-vocabulary-and-retrieval.md).
2. Review [data contracts](docs/specifications/data_contracts.md), [pipeline specifications](docs/specifications/pipelines.md), and [evaluation protocol](docs/specifications/evaluation.md).
3. Select a ready task from the [backlog](tasks/README.md).
4. Preserve [baseline identities](manifests/baselines/pcba_handoff.json).

The [assay-selection meeting brief](docs/research/assay-selection-brief.md) compares AssayMatch, MetaHeta, and Assay2Mol and records questions still open for discussion. It is not an adopted change to the evaluation protocol. The local-notebook agent can take [T012](tasks/T012-assay-selection-task-framing.md) independently while the GPU-server agent continues implementation work on its own branch.

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

- `src/pubchem_subgraph_platform/`: shared platform modules, including clustering, and CLI.
- `integrations/`: isolated SSM and GS-Meta adapters.
- `configs/`: versioned design templates, not runnable pipelines yet.
- `schemas/` and `manifests/`: artifact contracts and compact provenance.
- `experiments/`: retrieval, GBA, and structural-prior protocols.
- `tasks/`: task dependencies, acceptance criteria, and evidence.
- `tests/`: bounded fixtures, contract tests, and integration tests added with implementation.
- `reports/`: compact measured summaries only.

The first milestone is a fixed small PubChem assay pilot: Morgan/BRICS baselines, label-free structural clustering, exact retrieval, and GBA on held-out observed molecule-assay edges. Next, test new molecules on known assays and compare assay-specific SSM/BRICS reranking with the same baselines. New-assay transfer, large-scale deployment, and GS-Meta prior ablations remain later or parallel work. Expansion requires measured time, memory, storage, and retrieval quality. See [sources](docs/sources.md) for historical results and limitations.

No project license has been selected. Review licensing and preserve attribution before importing upstream code. Large data, indices, matrices, and checkpoints belong outside Git and outside baseline directories.
