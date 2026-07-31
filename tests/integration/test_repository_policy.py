from __future__ import annotations

import re
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_ROOT = PROJECT_ROOT / ".github" / "workflows"


def test_makefile_exposes_required_commands() -> None:
    makefile = (PROJECT_ROOT / "Makefile").read_text(encoding="utf-8")

    for target in [
        "stage-web:",
        "fmt:",
        "fmt-check:",
        "lint:",
        "test:",
        "e2e:",
        "verify:",
        "serve:",
        "clean:",
    ]:
        assert target in makefile


def test_ci_and_pages_use_repository_targets() -> None:
    ci = (PROJECT_ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    pages = (PROJECT_ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")

    assert "make fmt-check" in ci
    assert "make lint" in ci
    assert "make test" in ci
    assert "make e2e" in ci
    assert "make e2e-webkit-smoke" in ci
    assert "make stage-web" in pages
    assert "web" in pages


def test_workflows_pin_external_actions_to_full_shas_with_version_comments() -> None:
    use_value_pattern = re.compile(r"^\s*(?:-\s+)?uses:\s+(?P<value>\S+)(?:\s+#.*)?$")
    external_use_pattern = re.compile(
        r"^\s*(?:-\s+)?uses:\s+"
        r"(?P<action>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_./-]+)?)"
        r"@(?P<sha>[0-9a-f]{40})"
        r"\s+#\s+v(?P<version>\d+\.\d+\.\d+)\s*$"
    )
    violations: list[str] = []
    external_uses_count = 0
    workflows = sorted(
        {*WORKFLOW_ROOT.glob("*.yml"), *WORKFLOW_ROOT.glob("*.yaml")},
    )

    for workflow in workflows:
        for line_number, line in enumerate(
            workflow.read_text(encoding="utf-8").splitlines(),
            start=1,
        ):
            if "uses:" not in line:
                continue
            parsed_use = use_value_pattern.fullmatch(line)
            if parsed_use is None:
                violations.append(f"{workflow.name}:{line_number}:{line.strip()}")
                continue
            if parsed_use.group("value").startswith("./"):
                continue
            external_uses_count += 1
            if external_use_pattern.fullmatch(line) is None:
                violations.append(f"{workflow.name}:{line_number}:{line.strip()}")

    assert external_uses_count > 0
    assert violations == []


def test_workflow_permissions_are_explicit_and_least_privilege() -> None:
    ci = (WORKFLOW_ROOT / "ci.yml").read_text(encoding="utf-8")
    pages = (WORKFLOW_ROOT / "pages.yml").read_text(encoding="utf-8")
    release = (WORKFLOW_ROOT / "release.yml").read_text(encoding="utf-8")
    template_self_test = WORKFLOW_ROOT / "template-self-test.yml"

    assert "permissions:\n  contents: read" in ci
    if template_self_test.exists():
        assert "permissions:\n  contents: read" in template_self_test.read_text(encoding="utf-8")
    assert "permissions:\n  contents: read\n  pages: write\n  id-token: write" in pages
    assert "permissions: {}" in release
    assert "verify-and-build:\n    permissions:\n      contents: read" in release
    assert release.count("contents: write") == 1
    assert (
        "publish:\n    needs: verify-and-build\n    permissions:\n      contents: write" in release
    )


def test_release_is_signed_tag_draft_first_and_immutable_fail_closed() -> None:
    release = (WORKFLOW_ROOT / "release.yml").read_text(encoding="utf-8")

    assert 'tomllib.load(open("pyproject.toml", "rb"))["project"]["version"]' in release
    assert 'test "$GITHUB_REF_NAME" = "v${project_version}"' in release
    assert 'git cat-file -t "$GITHUB_REF_NAME"' in release
    assert ".verification.verified" in release
    assert 'gh api "repos/${GITHUB_REPOSITORY}/immutable-releases"' in release
    assert ')" = "true"' in release
    assert "sha256sum --check SHA256SUMS" in release
    assert "actions/upload-artifact@" in release
    assert "actions/download-artifact@" in release
    assert "--draft" in release
    assert "--verify-tag" in release
    assert 'awk -v version="$version"' in release
    assert "--notes-file dist/release-notes.md" in release
    assert "--notes-file CHANGELOG.md" not in release
    assert "gh release download" in release
    assert "diff --recursive --brief dist/assets remote-dist" in release
    assert "--draft=false" in release
    assert "--json isImmutable" in release
    assert (
        release.index("gh release create")
        < release.index("gh release download")
        < release.index("--draft=false")
    )


def test_dependabot_covers_locked_python_and_actions_without_auto_merge() -> None:
    dependabot = (PROJECT_ROOT / ".github" / "dependabot.yml").read_text(encoding="utf-8")

    assert 'package-ecosystem: "uv"' in dependabot
    assert 'package-ecosystem: "github-actions"' in dependabot
    assert dependabot.count('interval: "weekly"') == 2
    assert "python-dependencies:" in dependabot
    assert "github-actions:" in dependabot
    assert "automerge" not in dependabot.lower()


def test_public_coordination_files_preserve_scope_and_private_reporting() -> None:
    security = (PROJECT_ROOT / "SECURITY.md").read_text(encoding="utf-8")
    normalized_security = " ".join(security.lower().split())
    contributing = (PROJECT_ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    issue_config = (PROJECT_ROOT / ".github" / "ISSUE_TEMPLATE" / "config.yml").read_text(
        encoding="utf-8"
    )
    engineering_issue = (
        PROJECT_ROOT / ".github" / "ISSUE_TEMPLATE" / "engineering-bug.yml"
    ).read_text(encoding="utf-8")
    accessibility_issue = (
        PROJECT_ROOT / ".github" / "ISSUE_TEMPLATE" / "accessibility-report.yml"
    ).read_text(encoding="utf-8")
    security_contact = (
        PROJECT_ROOT / ".github" / "ISSUE_TEMPLATE" / "security-contact.yml"
    ).read_text(encoding="utf-8")
    pull_request = (PROJECT_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md").read_text(
        encoding="utf-8"
    )

    assert "/security/advisories/new" in security
    assert "Do not disclose vulnerability details in a public issue" in security
    assert "protected health information" in security.lower()
    assert "synthetic" in security.lower()
    assert "does not establish clinical decision support" in normalized_security
    assert "scientific formula" in contributing.lower()
    assert "private" in contributing.lower()
    assert "blank_issues_enabled: false" in issue_config
    assert "/security/advisories/new" in issue_config
    assert "protected health information" in engineering_issue.lower()
    assert "behavior owned by this repository" in engineering_issue.lower()
    assert "authoritative upstream" in engineering_issue.lower()
    assert "assistive technology" in accessibility_issue.lower()
    assert "protected health information" in accessibility_issue.lower()
    assert "include no vulnerability details" in security_contact.lower()
    assert "protected health information" in security_contact.lower()
    assert "AUTHOR ACTION REQUIRED" in pull_request
    assert "make verify" in pull_request


def test_generated_stage_is_ignored_and_not_tracked() -> None:
    gitignore = (PROJECT_ROOT / ".gitignore").read_text(encoding="utf-8")

    assert "web/assets/py/" in gitignore
    assert (
        subprocess.run(
            ["git", "check-ignore", "web/assets/py/manifest.json"],
            cwd=PROJECT_ROOT,
            check=False,
        ).returncode
        == 0
    )
    assert (
        subprocess.run(
            ["git", "ls-files", "web/assets/py"],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        == ""
    )
