# Agent rules

These rules apply throughout this repository. Explicit user instructions take precedence. Preserve unrelated user changes.

Both GPU-server and local-notebook agents follow this file. The shared checkout protocol is in [docs/agent-workflow.md](docs/agent-workflow.md); machine-local paths and credentials are not project defaults.

## Boundaries

- Develop the new platform here. Treat `pcba_project`, archived worktrees, baseline artifacts, source data, and their environments as read-only.
- Pin baseline source to `pcba-research-handoff-20261005`, commit `6492777c42d93d8b9978bb5d93d14d197a614332`. Read that revision when porting; a dirty working tree is not the baseline.
- Never clean, reset, change permissions, switch branches, install packages, or write outputs inside baseline repositories or archives.
- Routine local implementation and relevant checks need no additional confirmation. Do not push, publish, change remote settings, send messages, or launch paid jobs unless authorized.
- Do not start full-corpus downloads or long training as incidental validation. Use bounded fixtures and task-specific resource budgets.
- Do not delegate to sub-agents unless explicitly requested by the user or task. If authorized, assign disjoint ownership and validate integration.
- Work on a task-specific branch in each environment. Claim one task in its task file before implementation; do not edit files owned by the other active agent without coordinating the handoff. Never share a writable checkout or push directly to `main` as routine agent work.
- Fetch before starting, inspect the worktree before switching or integrating, and do not reset, clean, force-push, or overwrite another agent's commits. Record a branch, commit, validation, and open questions at handoff.

## Workflow

1. Read README, applicable specifications, and task dependencies; inspect Git status.
2. Mark the selected task `in_progress` before substantive implementation.
3. Deliver the task's complete behavior. Empty modules are not completed pipelines.
4. Run meaningful checks for changed behavior, including leakage, version compatibility, restart safety, and parity where applicable.
5. Record commands, results, artifact identities, and limitations in the task evidence. Mark `done` only when acceptance criteria pass.
6. Update the specification and an ADR for changes to scientific protocols or shared contracts. Never silently change a split or metric.
7. Treat the assay-selection meeting brief as a proposal. Do not silently replace the accepted research direction or phase-1/phase-2 evaluation order before a recorded decision.

## Data and research correctness

- Preserve raw records, snapshot IDs, checksums, and standardization versions. Distinguish PubChem CID/SID from internal molecule IDs.
- Missing, inconclusive, and conflicting labels are not automatically inactive. Preserve observations before aggregation.
- Fit supervised vocabularies, IDF, selection, calibration, and thresholds only within the registered protocol's training/validation scope. Never fit on query/test labels or held-out task labels.
- Keep global structural clusters label-free. Record whether the structural corpus is strictly inductive or transductive; never describe held-out outcomes as unknown ground truth.
- Separate global candidate search, assay-specific reranking, graph evidence, and GBA in ablations. Compare methods at matched candidate and label budgets; preserve exact-search recall when clusters restrict candidates.
- Separate structural component IDs from vocabulary-local feature indices. Reject fingerprint, vocabulary, standardization, and index mismatches.
- Store predictions separately from observations. Never turn inferred labels into evidence automatically.
- Freeze feature order and record seeds, config/source hashes, dependencies, and fit scope. Define invalid, empty, and OOV behavior.
- AP means average precision, not trapezoidal PR-AUC. Development CV is not final holdout evaluation.

## Integrations and artifacts

- Isolate Python 3.7 GS-Meta from the platform environment. Exchange versioned artifacts; do not import from mutable baseline paths.
- Implement new prior code here, never in archived GS-Meta. Verify prior-disabled adjacency and prediction parity before ablations.
- Control encoder, task selector, molecule-property edges, edge budget, episode schedule, and training budget. Separate best-test paper comparisons from validation-selected one-time-test results; compare matched seeds.
- Import upstream code only after license review, with source revision and attribution. Collaborator Rust/SSM-BRICS code is pending integration, not an existing capability.
- Commit code, configs, schemas, manifests, and compact reports only. Keep large artifacts outside Git and baseline paths.
- Shared runtime configs use explicit parameters or documented environment variables, not machine-specific absolute paths.
- Use staged writes, checksum verification, and atomic completion manifests. Partial output is not a complete artifact.
- New resumable training checkpoints include model, optimizer, scheduler, RNG, and sampler state. Historical weights do not support exact resume.
