"""End-to-end test of tools/check_contracts.py against a throwaway git repo."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "tools" / "check_contracts.py"


def _git(cwd, *args):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


def _write(repo: Path, version: str, phases: list[str], log: list[dict]):
    (repo / "contracts").mkdir(exist_ok=True)
    (repo / "contracts" / "scdd.json").write_text(json.dumps({
        "id": "scdd", "version": version, "status": "Proposed", "title": "t", "summary": "s",
        "body": {"phases": phases}, "changelog": log}))


def _repo(tmp_path: Path) -> Path:
    _git(tmp_path, "init", "-q", "-b", "main")
    _git(tmp_path, "config", "user.email", "t@example.invalid")
    _git(tmp_path, "config", "user.name", "t")
    _write(tmp_path, "0.1", ["DEFINE"], [{"version": "0.1", "date": "2026-10-20", "change": "a", "pr": "1"}])
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "base")
    return tmp_path


def _run(repo: Path, base: str):
    return subprocess.run([sys.executable, str(TOOL), "--base", base, "--root", str(repo)],
                          cwd=repo, capture_output=True, text=True)


def test_cli_fails_when_contract_changes_without_version_bump(tmp_path):
    repo = _repo(tmp_path)
    _write(repo, "0.1", ["DEFINE", "VERIFY"], [{"version": "0.1", "date": "2026-10-20", "change": "a", "pr": "1"}])
    result = _run(repo, "main")
    assert result.returncode == 1
    assert "version" in result.stdout


def test_cli_passes_when_version_and_changelog_are_raised(tmp_path):
    repo = _repo(tmp_path)
    _write(repo, "0.2", ["DEFINE", "VERIFY"], [{"version": "0.1", "date": "2026-10-20", "change": "a", "pr": "1"},
                                                {"version": "0.2", "date": "2026-10-21", "change": "b", "pr": "2"}])
    result = _run(repo, "main")
    assert result.returncode == 0, result.stdout + result.stderr


def test_cli_treats_missing_base_ref_as_empty_catalogue(tmp_path):
    repo = _repo(tmp_path)
    result = _run(repo, "does-not-exist")
    assert result.returncode == 0, result.stdout + result.stderr
