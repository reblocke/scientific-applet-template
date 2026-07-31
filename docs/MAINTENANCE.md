# Maintenance

## Status

Template status: active engineering scaffold, version 0.1.1.

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

Use a reviewed pull request. After the exact merge commit is verified, create a signed, annotated
semantic-version tag. The release workflow verifies the signature, reruns the full suite under
read-only contents permission, and builds the deterministic source archive, browser-stage manifest,
and SHA-256 checksums before a release exists. A separate job with narrowly scoped contents-write
permission requires repository release immutability, creates a draft prerelease with every asset,
downloads and compares the draft assets, then publishes only the verified draft.
The tag must equal `v` plus the authoritative project version, and the public release body contains
only that version's nonempty changelog section.

If the workflow fails after draft creation, retain the draft for inspection. Repair the workflow
and create a new tag only after the failure is understood; never move a published tag or replace a
published asset. Promote a prerelease only after hosted Pages and portfolio-level validation are
complete, and confirm that the administrative promotion does not change its tag or assets.

Repository settings must retain read-only default workflow permissions, protect `main` and `v*`
tags, enable private vulnerability reporting and Dependabot security updates, and enable immutable
releases before the next tag is created.

## Deprecation

AUTHOR ACTION REQUIRED: define how users will be warned, how long the hosted app will remain
available, and where a successor is documented. Do not silently redirect or delete an old URL.
