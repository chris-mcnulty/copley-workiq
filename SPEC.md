# Work IQ Open Format Specification

This specification uses the key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** as described in RFC 2119.

## 1. Bundle manifest (`workiq.yaml`)

A Work IQ Open Format bundle **MUST** include a root manifest named `workiq.yaml`.

The manifest **MUST** declare:

- bundle `id`
- bundle `version`
- `license`
- `maintainers`
- `conformance_profile`
- referenced `schemas`
- `default_language`
- `sensitivity_model`
- `validation_rules`

A bundle claiming **Core Bundle** conformance **MUST** provide a manifest and concept documents that validate against the JSON Schemas in `schemas/`.

A bundle claiming **Agent Profile** conformance **MUST** satisfy Core Bundle requirements and **MUST** include agent documentation objects.

A bundle claiming **Semantic Export** conformance **MUST** satisfy Agent Profile requirements and **MUST** provide semantic exports that validate against the SHACL shapes in `shacl/`.

Teams **MUST** be able to adopt Core Bundle without deploying RDF stores, SHACL services, or graph infrastructure.

## 2. Concept documents

Concept documents **MUST** be Markdown files with YAML frontmatter followed by a human-readable Markdown body.

Each concept document **MUST** include the following frontmatter fields:

- `id`
- `type`
- `title`
- `description`
- `status`
- `owner`
- `sources`
- `last_verified`
- `stale_after`
- `tags`
- `relationships`

Profiles and specialized schemas **MAY** introduce additional fields such as `version`, `generated`, `verified`, `access_rights`, or `attestation`, but they **MUST NOT** remove the required core fields.

## 3. Work graph object types

A bundle **MAY** describe work intelligence using these object families:

1. people & roles
2. teams & org units
3. processes & workflows
4. content & datasets
5. systems, apps, APIs & tools
6. meetings, decisions, actions & commitments
7. metrics, computations, OKRs & policies

Each object **SHOULD** use stable identifiers and **SHOULD** explicitly link to related concepts, systems, or evidence.

## 4. Agent documentation objects

Agent documentation objects define agent-operable context. An Agent Profile bundle **SHOULD** include:

- an agent record
- capabilities
- skills
- tools & MCP endpoints
- A2A/OASF-compatible discovery metadata
- memory scope & retention boundaries
- safety, access & approval rules

Agent records **MUST** identify the agent, its owner, status, and approved usage boundaries. Tool references **SHOULD** describe interfaces in a tool-agnostic way, with optional MCP mappings when available.

## 5. Trust & lifecycle metadata

Bundles **MUST** support trust-oriented metadata, including:

- `sources`
- `generated`
- `verified`
- `status`
- `stale_after`
- `access_rights`
- `attestation`
- `decision_log`

Producers **SHOULD** provide enough provenance for a reviewer or agent to explain why a concept is present and whether it is safe to use. Consumers **MUST** treat stale or missing verification metadata according to the bundle’s declared validation rules.

## 6. Retrieval-aware fields

Work IQ Open Format adds retrieval-aware fields as a profile-level innovation. A concept or agent document **MAY** include:

- `canonical_summary`
- `synonyms`
- `related_concepts`
- `chunking_strategy`
- `embedding_scope`
- `exclusion_rules`
- `evaluation_questions`

These fields **SHOULD** help brokered retrieval and agent reasoning systems decide what to index, summarize, suppress, or escalate. They do not replace source citations or human-readable bodies.

## 7. Validation & export

The profile **MUST** support:

- JSON Schema validation for frontmatter and manifests
- SHACL validation for graph exports
- optional RDF / JSON-LD / DCAT / PROV export
- conformance tests and sample bundles

A Core Bundle implementation **MUST NOT** require semantic export support. Semantic exports **MAY** be produced only for selected bundles, provided the bundle’s declared conformance profile remains accurate.

## 8. Open questions

- **TODO:** confirm whether `last_verified` remains mandatory in all examples or can be satisfied by the latest entry in `verified`.
- **TODO:** define versioning expectations for cross-bundle identifiers and imported schemas.
- **TODO:** decide whether the profile should publish an official JSON-LD context in the first public draft.
