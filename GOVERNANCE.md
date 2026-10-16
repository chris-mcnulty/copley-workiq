# Governance

This repository covers both the current Copley specification draft and the earlier Work IQ bundle conventions that are still used in validation and examples. The project governance therefore focuses on maintaining coherence between the canonical specification in `SPEC.md` and the validator-facing examples in `examples/` and `schemas/`.

## 1. Maintainers and working groups

- **Maintainers** are responsible for release management, issue triage, and conformance policy.
- **Working groups** may be formed for specification, validation, interoperability, and adoption topics.
- Maintainers **SHOULD** publish working group rosters and decision records in the repository.

## 2. Contribution and change proposals

- Substantive changes to the specification, schemas, SHACL shapes, or conformance definitions **SHOULD** begin with an issue or change proposal.
- Pull requests **MUST** link to their motivating issue when one exists.
- Maintainers **MAY** request working group review for changes that alter conformance behavior or governance rules.

## 3. IPR and licensing expectations

- Contributions are made under the repository licensing terms.
- Code-like assets in `schemas/`, `shacl/`, and `validators/` are intended for Apache-2.0 licensing.
- Specification and documentation assets are intended for CC-BY-4.0 licensing.
- **TODO:** confirm whether a Developer Certificate of Origin, CLA, or equivalent statement is required before 1.0.

## 4. Required repository files

A conforming project repository **SHOULD** include, at minimum:

- `README.md`
- `SPEC.md`
- `GOVERNANCE.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `LICENSE`
- versioned schemas and validators
- examples and conformance fixtures

## 5. Issue and pull request workflow

1. Open or reference an issue for bug fixes, specification clarifications, or feature proposals.
2. Submit a focused pull request.
3. Ensure schema and SHACL validation passes in CI for affected bundles.
4. Obtain maintainer approval before merge.

PRs that change bundle formats, validation behavior, or semantic mappings **SHOULD** include updated examples or fixtures.

## 6. Release cadence

- Draft releases **MAY** be published frequently during early development.
- Current releases **SHOULD** be versioned and accompanied by change notes.
- Deprecated artifacts **SHOULD** remain available with migration guidance.
- Archived artifacts **MUST NOT** be presented as current normative references.

## 7. Artifact states

Project artifacts use these lifecycle states:

- **draft** — under active review and not yet stable for general adoption
- **stable** — reviewed and safe for general adoption, but not necessarily the latest normative version
- **current** — approved for active implementation
- **deprecated** — still readable, but scheduled for replacement or removal
- **archived** — retained for recordkeeping only

## 8. Conformance tiers

- **Core Bundle** — manifest + concept documents with required frontmatter, JSON Schema valid
- **Agent Profile** — Core Bundle plus agent documentation objects
- **Semantic Export** — Agent Profile plus SHACL-valid RDF/JSON-LD/DCAT/PROV export

Core Bundle adoption **MUST NOT** depend on RDF or SHACL infrastructure.
