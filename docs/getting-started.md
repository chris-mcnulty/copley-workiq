# Getting Started

The repository is currently split between the Copley draft specification and the working Work IQ bundle examples. The most up-to-date normative language lives in `SPEC.md`, while the example bundles use the validator-backed Git-native layout with a `copley.yaml` manifest.

## Start with Core Bundle

1. Copy the structure in `examples/fictional-company/`.
2. Create a `copley.yaml` manifest.
3. Add one or more Markdown concept documents with YAML frontmatter.
4. Validate locally with the Python validator.

Core Bundle is the recommended first step because it does not require RDF or SHACL infrastructure.

## Add richer profiles later

- Add agent records, capabilities, skills, and tool documentation for **Agent Profile**.
- Add RDF / JSON-LD exports plus SHACL validation for **Semantic Export**.

## Local validation

```bash
pip install -r validators/requirements.txt
python validators/validate.py --root examples/fictional-company
```

## What to model first

Good first concepts include:

- a critical business process
- a trusted metric or attested computation
- a team-owned agent and its approval boundaries

Prefer high-value, reviewable concepts over bulk import.
