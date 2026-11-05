# Baseline and artifact boundaries

Status: accepted for initial scaffold.

Use tagged PCBA as a read-only reference. Build shared chemistry/vocabulary/retrieval/GBA here and isolate legacy GS-Meta. Exchange immutable artifacts instead of importing mutable baseline paths.

Supervised fitting stays within allowed training partitions. Predictions and observations are separate. Best-test and validation-selected results are separate protocols. This supports independent platform and prior experiments, at the cost of explicit manifests and parity checks. Runtime dependencies and scaling infrastructure follow pilot measurements.
