# Maintenance

## Status

Template status: active engineering scaffold, version 0.1.3.

AUTHOR ACTION REQUIRED after initialization: choose and state one maintenance status such as
experimental, active, maintenance-only, archived, or superseded.

## Ownership

Maintainer: Brian Locke (`@reblocke`). Use repository issues and pull requests for public project
coordination.

AUTHOR ACTION REQUIRED: confirm downstream ownership, review responsibilities, and a contact path.

## Dependency updates

Review Pyodide, Plotly, Python, uv, Ruff, pytest, Hypothesis, Playwright, and GitHub Actions
updates deliberately. Dependabot groups weekly `uv` and GitHub Actions updates for review; it
does not authorize automatic merging. Keep each third-party Action pinned to a full commit SHA
with its reviewed version in a comment. For any external scientific core:

1. review its release notes and scientific changes;
2. update the exact package version and artifact checksum;
3. regenerate and review `uv.lock`;
4. run strict JSON, frozen scientific fixtures, staging, Chromium, and WebKit validation;
5. record the adopted core version in docs, UI, and release notes.

## 2026-10-10 maintenance consolidation

Protected `main` is the leading development branch. The security update
([#18](https://github.com/reblocke/scientific-applet-template/pull/18)), Action updates
([#17](https://github.com/reblocke/scientific-applet-template/pull/17)), and development locks
([#16](https://github.com/reblocke/scientific-applet-template/pull/16)) were reviewed and merged
sequentially, retaining their branch and PR histories. Earlier feature branches contain work
already incorporated into `main`; their refs remain available.

The adopted lock contains urllib3 2.8.0, the patched version for
[GHSA-vxq7-64xx-v4gw](https://github.com/urllib3/urllib3/security/advisories/GHSA-vxq7-64xx-v4gw).
GitHub marked Dependabot alert #2 fixed after #18 merged. Distribution metadata was checked
against PyPI, and the Action commit pins were checked against the official release tags.

Fresh engineering checks passed on each reviewed head:

| PR | Reviewed head | CI | Disposable-app self-test |
| --- | --- | --- | --- |
| #18 | `8f276e691797c8253b353ffdf829aced049e4eae` | [run, attempt 2](https://github.com/reblocke/scientific-applet-template/actions/runs/37974993951/attempts/2) | [run, attempt 2](https://github.com/reblocke/scientific-applet-template/actions/runs/37974994149/attempts/2) |
| #17 | `b2c1a7b58cd87651a020dab86d570ae7c29b6064` | [run](https://github.com/reblocke/scientific-applet-template/actions/runs/38115893208) | [run](https://github.com/reblocke/scientific-applet-template/actions/runs/38115893226) |
| #16 | `55ca57954c6742fb1566198ca39b5627851885d7` | [run](https://github.com/reblocke/scientific-applet-template/actions/runs/38116009517) | [run](https://github.com/reblocke/scientific-applet-template/actions/runs/38116009440) |

Local reproduction on each head: `uv sync --locked`, `uv run playwright install chromium webkit`,
`make verify`, `make template-self-test`, and `git diff --check`. These passed formatting, lint,
38 non-browser tests, five Chromium tests, WebKit smoke, and a disposable initialized app's
29 non-browser tests plus Chromium smoke. Staging checks cover manifest hashes, repeatability,
and stale-file removal; browser checks include exports, keyboard access, mobile containment,
worker recovery, and privacy using synthetic inputs.

This is unreleased maintenance work. The project version remains 0.1.3 and the published v0.1.3
tag and assets remain unchanged. The template still implements only its replaceable arithmetic
demonstration; these checks establish no scientific or clinical validity.

## Release

Use a reviewed pull request. After the exact merge commit is verified, create an annotated
semantic-version tag. Before repository code runs, the release workflow binds the local and remote
tag objects and target to the event commit, requires the target to be contained in protected
`main` history, and checks exact project-version agreement. It then reruns the full suite under
read-only contents permission and builds the deterministic source archive, browser-stage manifest,
and SHA-256 checksums before a release exists. A separate job with narrowly scoped contents-write
permission uses an exact checksummed GitHub CLI and the job-scoped GitHub token, creates a draft
stable release with every asset, downloads and compares the draft assets and release body, then
publishes only the verified draft. The workflow immediately requires the published release to
report immutable and verifies every hosted asset. The tag must equal `v` plus the authoritative
project version, and the public release body contains only that version's nonempty changelog
section.

If the workflow fails after draft creation, retain the draft for inspection. Repair the workflow
and create a new tag only after the failure is understood; never move a published tag or replace a
published asset. The draft is the candidate; publish once into the intended stable lifecycle state
after hosted Pages and portfolio-level validation are complete.

Repository settings must retain read-only default workflow permissions, protect `main` and `v*`
tags, enable private vulnerability reporting and Dependabot security updates, and enable immutable
releases before the next tag is created. Release automation does not require a separate
repository-administration credential.

## Deprecation

AUTHOR ACTION REQUIRED: define how users will be warned, how long the hosted app will remain
available, and where a successor is documented. Do not silently redirect or delete an old URL.
