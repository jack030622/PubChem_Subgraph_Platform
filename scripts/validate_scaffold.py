"""Check scaffold consistency without external packages or data downloads.

This is not a JSON Schema validator or a scientific correctness test.
"""
import ast
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    required = ["README.md", "AGENTS.md", "pyproject.toml", "docs/architecture.md",
                "docs/specifications/data_contracts.md", "docs/specifications/pipelines.md",
                "docs/specifications/evaluation.md", "tasks/README.md",
                "schemas/artifact_manifest.schema.json"]
    for name in required:
        if not (ROOT / name).is_file():
            raise ValueError("Missing required file: " + name)
    for path in ROOT.rglob("*.json"):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        json.loads(path.read_text())
    for path in (ROOT / "src").rglob("*.py"):
        ast.parse(path.read_text(), filename=str(path))
    tasks = {}
    for path in sorted((ROOT / "tasks").glob("T[0-9]*.md")):
        content = path.read_text()
        tid = path.name.split("-", 1)[0]
        if tid in tasks:
            raise ValueError("Duplicate task: " + tid)
        status = re.search(r"^Status: (.+)$", content, re.M).group(1)
        if status not in {"todo", "in_progress", "blocked", "done"}:
            raise ValueError("Invalid status: " + tid)
        dependencies = re.search(r"^Dependencies: (.+)$", content, re.M).group(1)
        tasks[tid] = [] if dependencies == "none" else dependencies.split(", ")
    visited, active = set(), set()
    def visit(tid):
        if tid not in tasks or tid in active:
            raise ValueError("Missing or cyclic task: " + tid)
        if tid in visited:
            return
        active.add(tid)
        for dep in tasks[tid]:
            visit(dep)
        active.remove(tid)
        visited.add(tid)
    for tid in tasks:
        visit(tid)
    for path in ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            destination = target.split("#", 1)[0]
            if not (path.parent / destination).exists():
                raise ValueError("Broken link in {}: {}".format(path, target))
    baseline = json.loads((ROOT / "manifests/baselines/pcba_handoff.json").read_text())
    if baseline["commit"] != "6492777c42d93d8b9978bb5d93d14d197a614332":
        raise ValueError("Baseline commit changed")
    for option in ("--help", "--version"):
        result = subprocess.run(
            [sys.executable, "-B", "-m", "pubchem_subgraph_platform.cli", option],
            cwd=str(ROOT / "src"), check=True, stdout=subprocess.PIPE,
            universal_newlines=True,
        )
        if "psp" not in result.stdout:
            raise ValueError("CLI did not produce expected output")
    print("Scaffold checks passed: JSON, Python syntax, local links, task DAG, baseline pin, CLI.")


if __name__ == "__main__":
    main()
