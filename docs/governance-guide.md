# Governance Guide

This guide explains how to participate in the project’s governance model.

## Roles

- Maintainers steward releases and conformance definitions.
- Working groups shape proposals in focused domains.
- Contributors improve text, examples, schemas, validators, and interoperability mappings.

## Change flow

1. Start with an issue or proposal.
2. Discuss scope and affected conformance tiers.
3. Submit a pull request with updated examples and validation changes if needed.
4. Merge after review and passing CI.

## Artifact state usage

Use artifact states consistently:

- `draft` for active proposals
- `current` for normative artifacts in active use
- `deprecated` for artifacts with a migration path
- `archived` for retained historical reference only

## Governance records

Maintainers should keep release notes, meeting outcomes, and substantive decisions in the repository so bundle producers can understand why requirements changed.
