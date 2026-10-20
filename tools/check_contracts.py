#!/usr/bin/env python3
"""CI adapter: compare contracts/ on the PR's base ref with the working tree (B-014).

    python tools/check_contracts.py --base origin/main

Exits 1 and prints one line per problem when a contract changed without a version bump, a version
went down, a changelog entry is missing, or a contract was removed. A base ref that does not exist
(e.g. the very first PR) counts as an empty catalogue.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from anchor import contracts  # noqa: E402


def base_catalogue(root: Path, ref: str) -> dict[str, dict]:
    listed = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "contracts/"],
                            cwd=root, capture_output=True, text=True)
    if listed.returncode != 0:
        return {}
    catalogue: dict[str, dict] = {}
    for name in listed.stdout.split():
        if not name.endswith(".json"):
            continue
        blob = subprocess.run(["git", "show", f"{ref}:{name}"], cwd=root, capture_output=True,
                              text=True, check=True)
        contract = json.loads(blob.stdout)
        catalogue[contract.get("id", Path(name).stem)] = contract
    return catalogue


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", required=True, help="git ref of the PR's base branch, e.g. origin/main")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    args = ap.parse_args(argv)
    root = Path(args.root)
    head = contracts.load_catalogue(root / "contracts")
    problems = contracts.check_versions(base_catalogue(root, args.base), head)
    for p in problems:
        print("PROBLEM", p)
    print(f"{len(head)} kontrakt(er), {len(problems)} problem(er)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
