"""Tests for the contract catalogue and its version check (B-014).

A contract changes only through a PR, and a change must raise its version (0.1 -> 0.2) and add a
changelog entry for the new version. A contract is never deleted; it is marked Superseded (B-013).
"""
from __future__ import annotations

import copy
import json

import pytest

from anchor import contracts


def _contract(version="0.1", body=None, changelog=None, status="Proposed"):
    return {
        "id": "scdd",
        "version": version,
        "status": status,
        "title": "SCDD-faserne",
        "summary": "Hvad Anchor lover i hver fase.",
        "body": body if body is not None else {"phases": ["DEFINE", "VERIFY", "PROMOTE", "GOVERN"]},
        "changelog": changelog if changelog is not None else [
            {"version": "0.1", "date": "2026-10-20", "change": "Første version", "pr": "PR 1"}
        ],
    }


def test_check_unchanged_contract_has_no_problems():
    c = _contract()
    assert contracts.check_versions({"scdd": c}, {"scdd": copy.deepcopy(c)}) == []


def test_check_changed_body_without_version_bump_fails():
    base = _contract()
    head = _contract(body={"phases": ["DEFINE", "VERIFY", "PROMOTE", "GOVERN", "NY"]})
    problems = contracts.check_versions({"scdd": base}, {"scdd": head})
    assert any("scdd" in p and "version" in p for p in problems)


def test_check_bump_with_changelog_entry_passes():
    base = _contract()
    head = _contract(version="0.2", body={"phases": ["DEFINE", "VERIFY"]}, changelog=[
        {"version": "0.1", "date": "2026-10-20", "change": "Første version", "pr": "PR 1"},
        {"version": "0.2", "date": "2026-10-21", "change": "To faser fjernet", "pr": "PR 7"},
    ])
    assert contracts.check_versions({"scdd": base}, {"scdd": head}) == []


def test_check_bumped_version_without_changelog_entry_fails():
    base = _contract()
    head = _contract(version="0.2", body={"phases": ["DEFINE"]})
    problems = contracts.check_versions({"scdd": base}, {"scdd": head})
    assert any("changelog" in p for p in problems)


def test_check_version_going_down_fails():
    base = _contract(version="0.2", changelog=[
        {"version": "0.1", "date": "2026-10-20", "change": "a", "pr": "PR 1"},
        {"version": "0.2", "date": "2026-10-21", "change": "b", "pr": "PR 2"},
    ])
    head = _contract(version="0.1")
    problems = contracts.check_versions({"scdd": base}, {"scdd": head})
    assert any("down" in p or "ned" in p for p in problems)


def test_check_removed_contract_fails_and_asks_for_superseded():
    problems = contracts.check_versions({"scdd": _contract()}, {})
    assert any("scdd" in p and "Superseded" in p for p in problems)


def test_validate_rejects_malformed_version_and_unknown_status():
    problems = contracts.validate(_contract(version="v1", status="Maybe"))
    assert any("version" in p for p in problems)
    assert any("status" in p for p in problems)


def test_load_catalogue_requires_filename_to_match_id(tmp_path):
    (tmp_path / "andet.json").write_text(json.dumps(_contract()))
    with pytest.raises(ValueError):
        contracts.load_catalogue(tmp_path)


def test_repo_catalogue_is_valid():
    """The real contracts/ folder must pass validation on every commit."""
    from pathlib import Path

    root = Path(__file__).resolve().parent.parent / "contracts"
    catalogue = contracts.load_catalogue(root)
    assert catalogue, "contracts/ must hold at least one contract"
    for c in catalogue.values():
        assert contracts.validate(c) == []
