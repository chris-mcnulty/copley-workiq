# Work IQ Open Format

Work IQ Open Format is an open-source specification for packaging trustworthy work intelligence as plain-text, Git-native bundles that agents and people can read, validate, explain, update, and share. It solves a common gap in retrieval systems: agents can often retrieve knowledge, but they cannot reliably tell whether it is current, correct, or safe to act on. This format layers a governed, human-readable, machine-validatable profile on top of existing standards that already work, using Google's Open Knowledge Format (OKF) as the base bundle model, JSON Schema and SHACL for validation, and optional RDF / JSON-LD / DCAT / PROV export for graph interoperability. Work IQ Open Format augments brokered retrieval layers such as Microsoft's Work IQ rather than replacing them.

## Conformance tiers

- **Core Bundle** — manifest + concept documents with required frontmatter, JSON Schema valid.
- **Agent Profile** — Core Bundle plus agent documentation objects (records, capabilities, skills, tools/MCP endpoints, memory scope, safety rules).
- **Semantic Export** — Agent Profile plus SHACL-valid RDF/JSON-LD/DCAT/PROV export.

Teams **MUST** be able to adopt Core Bundle without standing up RDF or SHACL infrastructure.

## Repository map

- `SPEC.md` — normative specification skeleton
- `GOVERNANCE.md` — project governance, states, working groups, and release process
- `CONTRIBUTING.md` — contribution workflow, validator usage, and PR checklist
- `CODE_OF_CONDUCT.md` — Contributor Covenant v2.1
- `schemas/` — JSON Schema definitions for the manifest and object types
- `shacl/` — SHACL shapes for semantic validation
- `profiles/` — crosswalks to OKF, DCAT/PROV, MCP, OASF, and Agent Skills
- `examples/` — example bundles and starter artifacts
- `validators/` — local validator, requirements, and conformance fixtures
- `docs/` — onboarding, authoring, governance, and adoption guidance

## Quickstart

Start with the complete minimal Core Bundle in [`examples/fictional-company/`](examples/fictional-company/). Then:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r validators/requirements.txt
python validators/validate.py --root examples/fictional-company
```

The example shows how to define a `workiq.yaml` manifest and concept documents with trust and lifecycle metadata. Specification and documentation text in this repository is intended to be licensed under **CC-BY-4.0**, while code-like assets under `schemas/`, `shacl/`, and `validators/` are covered by **Apache-2.0**. **TODO:** maintainers should confirm the final dual-license policy before the first stable release.
