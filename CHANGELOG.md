# Changelog

All notable changes use a release-oriented record here. This repository follows
[Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.2] - 2026-07-30

- Add a least-privilege, signed-tag, draft-first release pipeline that verifies all downloaded
  assets and release notes before one-time stable publication and requires immutable releases.
- Install an exact checksummed GitHub CLI before credentialed release commands and use a dedicated
  settings-read secret for the pre-publication immutability gate.
- Disable shared dependency caching in the release-artifact build job.
- Require the verified release-tag target to be contained in protected `main` history and defer
  isolated project-version parsing until after signature verification.
- Pin every third-party GitHub Action to a full commit SHA, add grouped weekly Dependabot updates
  for `uv` and GitHub Actions, and add scoped security, contribution, issue, and pull-request
  guidance.
- Add repository-policy regressions for action provenance, token permissions, draft publication,
  dependency monitoring, private-reporting guidance, and the disposable-app self-test.
- Require the signed tag to equal the authoritative project version and limit release notes to
  that version's nonempty changelog section.
- Upgrade the development-only pytest requirement and lock from 8.4.2 to 9.0.3; no runtime or
  scientific Python package dependency was added, and the existing Pyodide and Plotly browser
  dependencies are unchanged.
- Preserve the generic arithmetic demonstration, scientific-scope prompts, privacy behavior, and
  user-facing app behavior unchanged.

## [0.1.1] - 2026-07-30

- Constrain the two-column grid and resize Plotly after the results panel becomes visible so the
  template remains contained at a 390 px viewport.
- Add a browser regression for horizontal overflow and release the exact hosted template state
  under an annotated tag. No scientific method or formula changed.

## [0.1.0] - 2026-07-29

- Initial generic template with locked Python, deterministic browser staging, a Web Worker
  runtime, accessible UI and exports, privacy guardrails, documentation prompts, and test
  scaffolding.
- Includes only a conspicuously replaceable arithmetic demonstration; no scientific method is
  implemented.
