## Scope

Describe the engineering, scientific, documentation, governance, or maintenance problem addressed.
Name the authoritative upstream repository when a released package owns the affected behavior.

## Risk and release impact

Describe silent-failure risks, privacy/accessibility implications, generated-stage effects, and
whether the change requires a new release.

## Verification

List the exact commands run and their outcomes. Include skipped checks and warnings.

## Checklist

- [ ] Any scientific method or formula change names its authority, independent validation, and
      assumptions; a repository still in template state adds no scientific method.
- [ ] Intentional `AUTHOR ACTION REQUIRED` prompts remain unresolved until an identified authority
      supplies the answer.
- [ ] Public copy stays within validated functionality and does not imply clinical or regulatory
      readiness.
- [ ] Examples and fixtures are synthetic and contain no credentials, sensitive data, or protected
      health information.
- [ ] No backend, telemetry, persistence, cookies, hidden state, or input-bearing URL was added.
- [ ] Generated Python under `web/assets/py/` was produced by `make stage-web`, not edited by hand.
- [ ] Every third-party GitHub Action remains pinned to a full commit SHA with a version comment.
- [ ] `uv sync --locked` and `make verify` pass.
- [ ] A repository still in template state preserves the disposable-app self-test after initializer
      or scaffold changes.
- [ ] README, scope, validation, privacy, decisions, maintenance, citation, and changelog were
      reviewed for synchronization.
