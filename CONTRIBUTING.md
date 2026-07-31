# Contributing

## Repository scope

This repository begins as a generic, client-side scientific-applet engineering scaffold. While it
is still in template state, it owns no scientific formula or clinical interpretation. After
initialization, its maintainers must name the scientific authority, validation evidence, scope, and
upstream owner for every calculation rather than introducing a formula through UI scaffolding.

Use the public issue forms only for nonsensitive repository engineering and accessibility reports.
Report vulnerabilities through the private process in [SECURITY.md](SECURITY.md). Never place
credentials, protected health information, patient-level data, unpublished restricted data, or
other sensitive values in an issue, pull request, fixture, screenshot, URL, or workflow log.

## Change process

1. Start from the current `main` branch and make one reviewable change.
2. State assumptions, success criteria, silent-failure risks, and verification before editing.
3. Preserve every intentional `AUTHOR ACTION REQUIRED` prompt until an identified authority supplies
   the answer.
4. Keep Python under `src/` as source of truth and regenerate browser Python with `make stage-web`.
5. Keep external scientific packages exact-version and checksum bound.
6. Keep third-party GitHub Actions pinned to full commit SHAs with version comments.
7. Open a pull request and let all required checks complete before merging.

Do not add a backend, telemetry, persistence, cookies, hidden state, input-bearing URLs, or
unowned scientific formulas as conveniences.

## Verification

Restore the locked environment and run the complete documented suite:

```bash
uv sync --locked
uv run playwright install chromium webkit
make verify
git diff --check
git status --short
```

While the repository is still in template state, changes to the initializer, scaffold, or
repository structure must also preserve the `initialize-disposable-app` workflow. Document any
skipped check or warning.

## Release changes

A release change requires a reviewed pull request and a signed, annotated version tag pointing to
the exact reviewed merge commit. The tag must equal `v` plus the authoritative project version,
and that version needs a nonempty changelog section. The tag workflow:

1. verifies the tag and complete test suite with read-only contents permission;
2. builds and checksums all assets before creating a release;
3. transfers the complete bundle to a narrowly write-enabled publishing job;
4. requires repository release immutability;
5. creates a draft prerelease using only the current version's changelog section;
6. downloads and compares every draft asset; and
7. publishes only the verified draft.

If a release job fails after draft creation, leave the release as a draft for inspection. Do not
replace assets or move a tag after publication.
