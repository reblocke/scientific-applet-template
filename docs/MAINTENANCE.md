# Maintenance

## Status

Template status: active engineering scaffold, version 0.1.2.

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
