# Scaffold validation

Validated on 2026-10-06 (Asia/Seoul). Scope: repository foundation T000, not research pipeline implementation.

## Results

- `python -B scripts/validate_scaffold.py`: passed JSON parsing, Python syntax, relative Markdown links, task dependency graph, baseline commit pin, and source CLI smoke checks.
- Built and installed `pubchem-subgraph-platform` 0.1.0 into an isolated temporary Python 3.10 environment using pip. Wheel build and installation passed.
- Installed `psp --help`, `psp --version`, and package import: passed; version 0.1.0.
- JSON Schema Draft 2020-12 metaschema validation: passed using jsonschema 4.26.0.
- A complete synthetic fingerprint manifest was accepted. Eleven invalid variants were rejected: five absolute/traversal/nonportable paths, empty complete-artifact shards, null split/vocabulary/standardization identifiers, and malformed commit/config hashes.
- Baseline tag resolved to `6492777c42d93d8b9978bb5d93d14d197a614332`; upstream submodule commits match the baseline manifest.
- The baseline checkout retained its pre-existing modified SSM submodule status. No baseline files, environments, or artifacts were modified by this work.

## Reproduction and limits

From the repository root, run `python -B scripts/validate_scaffold.py` with Python >=3.10. In a separate environment, `python -m pip install .` followed by `psp --help` and `psp --version` exercises packaging. Schema smoke validation used a temporary jsonschema installation; runtime schema validation and maintained contract tests belong to T001.

The initial sandboxed package installation could not reach the registry; the approved retry completed in the isolated temporary environment. No dependencies were installed into the baseline environment. Build outputs are ignored by Git.

Configuration files are templates, and chemistry policy, dataset snapshot, dependency lock, and license decisions remain open tasks. No scientific pipeline, PubChem download, model training, or GitHub Actions execution is claimed. The local main branch and origin are configured; no commit or push has been made.
