# Decisions

## 2026-07-29 — Functional Python core and browser worker

Python is the calculation source of truth. The static UI sends strict JSON to a restartable
Web Worker running exact-version Pyodide. This prevents Python initialization and calculation
from blocking the main UI thread.

## 2026-07-29 — Generated, verified browser stage

The installed locked app and optional external packages are staged from a TOML manifest.
Generated files are ignored. File, package, and aggregate hashes are verified before Python is
loaded, avoiding a manually synchronized JavaScript file list.

## 2026-07-29 — No live shared UI dependency

The repository is a creation-time template, not a runtime framework. Initialized apps may evolve
independently without a shared component release becoming an application availability risk.

## 2026-07-29 — Strict client-side privacy boundary

There is no backend, telemetry, persistence, cookie, or input-bearing URL. Static CDN requests do
not include user input.

## 2026-07-30 — Fail-closed repository and release governance

Third-party GitHub Actions are content-addressed by full commit SHA and receive grouped,
review-only Dependabot proposals. Ordinary CI and the disposable-app self-test have explicit
read-only contents permission; Pages and release jobs receive only their required writes.

A release requires a GitHub-verified signed annotated tag and enabled repository release
immutability. The tag must equal `v` plus the authoritative project version. The workflow builds
and checksums all assets before release creation, extracts a nonempty release body from only that
version's changelog section, transfers the complete bundle to a separate publishing job, creates a
draft stable release, downloads and compares every draft asset and its release body, and publishes
only after exact verification. Credentialed release commands use an exact checksummed GitHub CLI;
the pre-publication immutability query uses a dedicated settings-read Actions secret. A failed run
leaves an inspectable draft rather than an incompletely published release. Published tags and
assets are never rewritten or promoted between lifecycle states. The signed tag is bound to the
event commit and protected `main` history before isolated project-version parsing or other
repository code execution.

Private vulnerability reporting is the disclosure path. Public issue forms explicitly exclude
credentials, restricted data, sensitive user values, and protected health information.

## New decision record

AUTHOR ACTION REQUIRED: append dated decisions that change scientific meaning, runtime,
dependencies, validation, privacy, exports, accessibility, or maintenance. Do not silently
rewrite historical decisions.
