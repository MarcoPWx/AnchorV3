"""The contract catalogue and its version rule (B-013, B-014).

A contract is one JSON file in contracts/<id>.json. It changes only through a PR, and any change to
its substance must raise its version (MAJOR.MINOR, e.g. 0.1 -> 0.2) and add a changelog entry for
the new version. A contract is never deleted; its status becomes Superseded, so every decision that
cites `id@version` stays traceable.

check_versions(base, head) is pure: CI gives it the catalogue on the PR's base branch and on its
head, and fails the PR on any problem it returns.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

STATUSES = ("Proposed", "Accepted", "Superseded", "Rejected")
REQUIRED = ("id", "version", "status", "title", "summary", "body", "changelog")
_VERSION = re.compile(r"^\d+\.\d+$")
# Fields that are bookkeeping about a change, not the substance of the contract.
_NOT_SUBSTANCE = ("version", "changelog")


def _vkey(version: str) -> tuple[int, int]:
    major, minor = version.split(".")
    return int(major), int(minor)


def validate(contract: dict) -> list[str]:
    """Problems with one contract on its own (shape, version format, status, changelog head)."""
    cid = contract.get("id", "?")
    problems = [f"{cid}: missing field {f}" for f in REQUIRED if f not in contract]
    version = str(contract.get("version", ""))
    if not _VERSION.match(version):
        problems.append(f"{cid}: version {version!r} must look like 0.1 (MAJOR.MINOR)")
    if contract.get("status") not in STATUSES:
        problems.append(f"{cid}: status {contract.get('status')!r} must be one of {', '.join(STATUSES)}")
    log = contract.get("changelog") or []
    if not log:
        problems.append(f"{cid}: changelog is empty")
    elif str(log[-1].get("version")) != version:
        problems.append(f"{cid}: changelog has no entry for version {version} (last entry is {log[-1].get('version')})")
    return problems


def _substance(contract: dict) -> dict:
    return {k: v for k, v in contract.items() if k not in _NOT_SUBSTANCE}


def check_versions(base: dict[str, dict], head: dict[str, dict]) -> list[str]:
    """Problems when going from the base catalogue to the head catalogue of a PR."""
    problems: list[str] = []
    for cid, contract in head.items():
        problems.extend(validate(contract))
        old = base.get(cid)
        if old is None or not _VERSION.match(str(contract.get("version", ""))):
            continue
        new_v, old_v = _vkey(contract["version"]), _vkey(old["version"])
        if new_v < old_v:
            problems.append(f"{cid}: version went down from {old['version']} to {contract['version']}")
        elif new_v == old_v and _substance(contract) != _substance(old):
            problems.append(f"{cid}: changed but version is still {contract['version']}; raise the version "
                            f"and add a changelog entry")
    for cid in base:
        if cid not in head:
            problems.append(f"{cid}: contract was removed; keep it and set status Superseded instead")
    return problems


def load_catalogue(folder: Path) -> dict[str, dict]:
    """Read contracts/<id>.json; the filename must equal the contract's id."""
    catalogue: dict[str, dict] = {}
    for path in sorted(Path(folder).glob("*.json")):
        contract = json.loads(path.read_text(encoding="utf-8"))
        if contract.get("id") != path.stem:
            raise ValueError(f"{path.name}: id {contract.get('id')!r} does not match the filename")
        catalogue[path.stem] = contract
    return catalogue
