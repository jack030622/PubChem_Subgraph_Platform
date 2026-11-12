# Working across GPU-server and local-notebook agents

This repository is the common source of truth for both Codex agents. `AGENTS.md`, the specifications, ADRs, task files, and committed configs travel with Git. Notion and slides are reading and meeting aids; a decision that changes an executable protocol must also be recorded here. Machine-local files, credentials, datasets, indices, and checkpoints do not travel with Git.

## One task, one branch, one owner

1. In each environment, inspect `git status --short --branch` and `git fetch origin` before starting. Read `AGENTS.md`, `README.md`, the relevant specs, and the task file. Update a clean `main` with `git pull --ff-only` before creating a branch. If the checkout is dirty, preserve it and resolve ownership before switching or pulling.
2. Use a separate checkout or worktree and a task branch such as `agent/gpu/T001-contracts` or `agent/local/T012-assay-selection`. The branch name is an example, not a required remote branch. Do not have both agents write the same checkout, branch, or task simultaneously.
3. Claim the task in its task file with `Status: in_progress`, an owner/environment, and branch name. Keep the backlog index synchronized. Before changing a shared specification or ADR, check whether the other agent is editing it and agree who integrates that change.
4. Commit bounded changes on the task branch with the task ID in the message. Push or open a PR only when authorized. No agent should routinely push to `main`, force-push, reset, clean, or amend another agent's commit.
5. At handoff, record branch and commit SHA, touched files, validation commands and results, artifact IDs/hashes, unresolved decisions, and the next action in the task evidence. The integrating agent reviews the diff, resolves conflicts deliberately, and runs relevant checks before merging.

`T001` is the first implementation task and can remain on the GPU-server agent's branch. `T012` is an independent literature-to-protocol design task for the local-notebook agent. T012 may propose changes to T001's pilot definition, but the two agents must not concurrently edit the same T001 file or freeze conflicting protocols. A proposed change stays a proposal until recorded in an ADR and reflected in the specs/tasks.

## Portable environments and artifacts

- Use Python >=3.10 for the platform and a separate Python 3.7 environment for legacy GS-Meta. Do not install into or modify the PCBA baseline checkout. The baseline tag and commit are in `manifests/baselines/pcba_handoff.json`.
- Never commit absolute host paths, tokens, `.env`, raw PubChem data, large matrices, indices, or checkpoints. Use explicit config parameters or documented environment variables for local paths.
- For any data or model result shared across machines, record source snapshot, content checksum, standardization/config/code versions, fit scope, split and label access, and completion manifest. A path existing only on one machine is not reproducible evidence.
- Neither agent should infer that a task is complete from a status label alone. Read its evidence and rerun the smallest relevant verification after integration.

## Current scientific boundary

The accepted direction in ADR 0002 is reusable BRICS/SSM representation and assay-conditioned retrieval with Morgan as a matched baseline; phase 1 masks known molecule–known assay observations, phase 2 holds out molecules on known assays, and phase 3 new-assay transfer is deferred. The [assay-selection meeting brief](research/assay-selection-brief.md) considers a low-label target-assay screening pilot in light of recent papers. It does not override ADR 0002 or the evaluation specification without a new recorded decision.
