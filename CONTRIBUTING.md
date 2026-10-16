# Contributing

Thank you for contributing to Work IQ Open Format.

## Propose changes

1. Search for an existing issue or open a new one describing the problem or proposal.
2. Keep pull requests focused and link related issues.
3. Update examples, schemas, SHACL shapes, or docs when your change affects them.
4. Mark open design choices with `TODO:` rather than inventing unresolved policy.

## Run the validator locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r validators/requirements.txt
python validators/validate.py --root examples
python validators/validate.py --root validators/conformance-tests/passing
python validators/validate.py --root validators/conformance-tests/failing --expect-fail
```

## Add examples

- Prefer small, realistic, plain-text examples.
- Every new or changed bundle **SHOULD** include a `workiq.yaml` manifest.
- Keep examples Git-native and tool-agnostic.
- If you add semantic export files, ensure they pass SHACL validation.

## Pull request checklist

- [ ] Change is scoped to the issue or proposal
- [ ] New or changed bundles pass JSON Schema validation in CI
- [ ] New or changed semantic exports pass SHACL validation in CI when present
- [ ] Examples and crosswalks are updated when required
- [ ] Open questions are marked with `TODO:` where needed
