# Work IQ Open Format / Copley

This repository contains two layers of material that need to be kept distinct:

- The current root-level draft specification in [`SPEC.md`](SPEC.md) and the root JSON Schema in [`copley.schema.json`](copley.schema.json) are the most recent Copley-oriented specification assets.
- The project’s working bundle examples, JSON Schemas under [`schemas/`](schemas), and validator tooling still reflect the earlier Work IQ-oriented naming and are kept for compatibility and iteration.

The repository is best understood as the Copley specification living alongside the older Work IQ implementation conventions. The root specification is the canonical source for the most up-to-date language, while `schemas/` and `examples/` continue to model the repository’s current validator-backed bundle format.

## Conformance tiers

- **Core Bundle** — manifest + concept documents with required frontmatter, JSON Schema valid.
- **Agent Profile** — Core Bundle plus agent documentation objects (records, capabilities, skills, tools/MCP endpoints, memory scope, safety rules).
- **Semantic Export** — Agent Profile plus SHACL-valid RDF/JSON-LD/DCAT/PROV export.

Teams **MUST** be able to adopt Core Bundle without standing up RDF or SHACL infrastructure.

## Repository map

- `SPEC.md` — current Copley draft specification
- `copley.schema.json` — root-level Copley schema artifact for the draft specification
- `GOVERNANCE.md` — project governance, states, working groups, and release process
- `CONTRIBUTING.md` — contribution workflow, validator usage, and PR checklist
- `CODE_OF_CONDUCT.md` — Contributor Covenant v2.1
- `schemas/` — validator-facing JSON Schema definitions and compatibility artifacts
- `shacl/` — SHACL shapes for semantic validation
- `profiles/` — crosswalks to OKF, DCAT/PROV, MCP, OASF, and Agent Skills
- `examples/` — example bundles and starter artifacts; manifests use `copley.yaml` and accept legacy `workiq.yaml` aliases
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

The bundle manifests in examples are currently named `copley.yaml`; older `workiq.yaml` names continue to be accepted for compatibility. Specification and documentation text in this repository is intended to be licensed under **CC-BY-4.0**, while code-like assets under `schemas/`, `shacl/`, and `validators/` are covered by **Apache-2.0**. **TODO:** maintainers should confirm the final dual-license policy before the first stable release.
