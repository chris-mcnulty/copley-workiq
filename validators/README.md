# Validators

The validator checks every bundle under a root directory by:

1. loading each `workiq.yaml` manifest
2. validating it against `schemas/workiq-bundle.schema.json`
3. loading Markdown frontmatter files in the bundle
4. validating frontmatter against the matching schema
5. validating RDF / Turtle exports with SHACL when a bundle declares them in `exports`

## Local usage

```bash
pip install -r validators/requirements.txt
python validators/validate.py --root examples
python validators/validate.py --root validators/conformance-tests/passing
python validators/validate.py --root validators/conformance-tests/failing --expect-fail
```

The `--expect-fail` flag is intended for intentionally failing conformance fixtures.
