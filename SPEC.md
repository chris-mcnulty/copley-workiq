# Copley Specification

**Specification version: `0.1.0-draft.2` — public proposal for review**  
**Revision date: October 13, 2026**  
**Format baseline: Open Knowledge Format (OKF) v0.2**

## 1. Status, purpose, and boundaries

Copley is a thin, portable profile for trustworthy work knowledge, not a competing ontology, a retrieval platform, or an agent runtime. It connects three layers: pointers to authoritative sources; curated, topic-centered knowledge with accountable ownership and review; and a machine-readable contract for both. Its purpose is to make provenance, currentness, review, and limits visible before someone or something relies on retrieved knowledge.

This document is a draft specification, not an executable script, ratified standard, released implementation, or endorsement by Microsoft or any other platform provider. Requirements describe proposed conformance. No existing code, connector, graph export, or prototype is asserted to implement this revision.

Original evidence remains authoritative for factual claims. Curated Markdown is the canonical curated representation, not a replacement source of truth. Passing validation or receiving human approval does not guarantee factual correctness. A signed agreement and an unapproved draft are not interchangeable evidence; popularity and recency cannot decide which governs.

A concept represents a topic, process, policy, person, system, or other unit of knowledge. It MAY combine multiple sources; every contributing source receives the same provenance and protection checks. One document producing one draft is an explicitly limited bootstrap mode, not the fundamental data model.

Core requires no Microsoft service, Replit project, database, model, RDF engine, or SHACL installation. A separate prototype may demonstrate this contract without becoming part of it. Autonomous actions, arbitrary computation execution, legal interpretation, and enterprise-wide discovery are not Core requirements.

The public non-code repository contains specifications, schemas, documentation, and wholly synthetic fixtures. Real source material, tenant-derived knowledge, credentials, private URLs, and commercial implementation details MUST remain outside it and outside public application assets. This revision supplies no executable validator or application.

## 2. Terminology and independent conformance axes

**MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** express requirements, prohibitions, recommendations, discouraged practice, and permission within the stated scope.

A **bundle** is a portable directory of related knowledge. A **source pointer** identifies evidence without reproducing its raw bytes. A **concept revision** comprises exact metadata, body, and captured source observations. A **producer** authors revisions; a **consumer** reads them; a **publisher** exposes reviewed revisions to an intended audience. **Quarantine** means enforceable restricted storage or removal from an unsafe delivery path, not a warning or hidden navigation.

Implementations MUST report three separate axes:

1. **OKF base:** assessed against OKF v0.2, with its deliberately permissive reading rules.
2. **Copley Core static:** assessed against this version, identifying producer/consumer role and `draft` or `publication` validation mode. Publication mode checks prerequisite structure, not permission to publish.
3. **Runtime assurance:** assessed for a deployment, requesting identity, revision, source set, and observation time, including approval authenticity, source freshness, and authorization.

Each check reports `pass`, `fail`, or `unknown`. Unperformed or unavailable checks are unknown, not pass. Static success is never a live trust badge. A type-only OKF concept remains readable even when it cannot satisfy Copley production requirements.

`AgentProfile` and `SemanticExport` are reserved extension names, not claimable conformance tiers in draft.2. Basic agent documentation is available in Core; a future AgentProfile would specify interoperability tests. SemanticExport would define graph mappings and SHACL shapes. Neither graph tooling nor SHACL is required for Core validation or Core CI.

## 3. Portable layout and canonical storage

A draft.2 bundle uses this deliberately small layout:

```text
bundle/
  copley.yaml
  index.md
  sources/
    renewal-guide.json
    approval-policy.json
  concepts/
    customer-renewal.md
    approval-policy.md
```

`copley.yaml` is the canonical manifest. Source filenames MUST be `<id>.json`; IDs use lowercase alphanumeric segments separated by hyphens. Concepts use `concepts/<slug>.md` with the same slug syntax. `index` and `log` are reserved and cannot be concept slugs. This flat Copley layout is a profile restriction, not a restriction on ordinary OKF hierarchies. Moving a concept preserves its stable identity and repairs affected links.

The root `index.md` is required for produced Copley bundles. Its only permitted frontmatter is `okf_version: "0.2"`; bundle metadata belongs in the manifest. Additional reserved `index.md` or `log.md` files follow OKF rules: nested indexes and logs have no frontmatter. Every other Markdown file within the knowledge bundle is an OKF concept. Repository documentation and agent instruction files therefore belong outside the bundle unless explicitly authored as concepts.

An OKF concept ID remains its bundle-relative path without `.md`. `copley.stable_id` is a separate absolute URI preserving logical identity across renames. IDs MUST NOT be reused for unrelated knowledge. Root-relative Markdown links begin `/`; other internal links resolve from the containing directory. Consumers MUST prevent traversal outside the authorized bundle. Draft readers expose broken links; publication blocks unresolved links essential to interpreting claims.

The canonical curated representation is Markdown plus frontmatter, the manifest, and pointer records. Storage may be a filesystem or a controlled document service. Operational databases MAY store jobs, schedules, cursors, locks, mappings, and supplemental audit records, but MUST NOT be the only persistent home of curated content or portable provenance.

In the optional SharePoint profile, ordinary document libraries hold these files. A wiki-style UI renders them; classic Wiki Page Libraries are not required. SharePoint columns and optional modern Site Pages are explicitly derived, one-way projections with an authoritative writer and reconciliation, never a second editable truth. Postgres is an optional operational store, not a required Core dependency.

## 4. Manifest contract

Validate parsed `copley.yaml` against `#/$defs/manifest` in the companion schema. Required fields are:

| Field | Meaning |
| --- | --- |
| `spec_version`, `okf_version` | Exactly `0.1.0-draft.2` and `0.2`; independent of bundle version. |
| `id`, `title`, `version` | Stable absolute bundle URI, non-empty display title, and bundle SemVer. |
| `license` | Non-empty declared terms identifier/reference, or `null` when unstated. Null grants nothing. |
| `maintainers` | Non-empty array of accountable identifiers; identity strings are not authentication. |
| `profile` | Exactly `Core` in this revision. |
| `schemas` | Pinned manifest/source/concept definition identifiers shown below. |
| `default_language` | BCP 47 language tag; schema checks shape, semantic validation checks validity. |
| `sensitivity` | `{model, default_label}`: absolute policy-model URI and non-empty label. |
| `validation` | `{mode: draft}` or `{mode: publication}` selecting static checks. |

The `schemas` values are `urn:copley:schema:0.1.0-draft.2#/$defs/manifest`, `urn:copley:schema:0.1.0-draft.2#/$defs/source`, and `urn:copley:schema:0.1.0-draft.2#/$defs/concept`, keyed respectively by `manifest`, `source`, and `concept`. Publication mode additionally applies the publication definitions in Section 12; changing a schema reference cannot bypass them.

These URNs identify locally pinned definitions, not downloadable endpoints. Validators MUST resolve them from an explicitly trusted local registry and MUST NOT fetch or execute arbitrary schema references from bundle metadata. Additional validation policies may be documented, but cannot weaken Core requirements.

Sensitivity labels and declared audiences describe intent, not enforced permissions. Bundle terms do not relicense cited sources. Before redistribution, maintainers MUST establish applicable rights and license terms independently. Specification licensing remains pending under Section 15.

## 5. Source pointer catalog and captured evidence

Each `sources/<id>.json` validates against `#/$defs/source`. Required fields are `id`, `uri`, `system`, `owner`, `identity`, `retrieved_at`, and `access_rights`, plus at least one actual `version` or `content_sha256`. Unobserved catalog candidates remain staged outside a valid Core bundle until these observations are available. They MUST be reported as incomplete/unknown, not presented as Core-valid or populated with invented stamps. Restricted draft production remains available once sources are genuinely observed; ownership and concept-review gaps may remain explicit.

- `id` is the unique bundle-local citation key; `uri` is an absolute canonical evidence URI.
- `system` names the originating system without requiring a registered vendor vocabulary.
- `identity` is an absolute origin-scoped identity URI, stable across ordinary URL changes. A URI is a name, not a command or network-access instruction.
- `owner` is an accountable identifier, or `null` when genuinely unassigned in a draft. Invented owners are prohibited.
- `retrieved_at` is the time the observation was actually obtained, not generation or verification time.
- `version` is an opaque provider revision token, when available; optional `version_kind` names its provider-defined kind, such as `etag`. Preserve and compare tokens without reinterpretation. `content_sha256` hashes original retrieved bytes, not extracted text. Publication requires the hash plus the provider revision token when available; it does not universally require an ETag. Reports distinguish `hash-and-version` from `hash-only` evidence. Hash-only publication requires a trusted provider-capability determination that no token is available; missing or unknown token availability cannot silently qualify as hash-only assurance.
- `access_rights` contains `policy_uri`, an absolute policy reference, and `audience`, an array of intended audience identifiers. An empty array means the audience is not established and blocks publication.

Optional `title`, `verified`, `last_verified`, and `stale_after` support display and source-review history. `verified` uses OKF event syntax. If `last_verified` is supplied, it MUST equal the latest recorded source verification instant, never the retrieval time. Historical source verification does not attest that a later observation is reviewed. On any new observation, consumers MUST distinguish historical verification from current evidence; no stamp establishes access or factual truth. `stale_after`, when present, is an absolute source-review deadline.

Pointers contain no wholesale source copy. Authorized extraction caches, if needed, remain outside the portable bundle, protected and retained under deployment policy. Summaries and citations are still sensitive derived content.

A concept cites catalog entries using ordinary OKF `sources[].id` plus `sources[].resource`. Each `resource` MUST equal the matching pointer's `uri` exactly; no undocumented URL normalization is assumed. Each ID occurs once within a concept. Every claim footnote label used for evidence resolves through that ID, not an array position.

`copley.source_versions` captures observations used for that particular revision. It maps source IDs to `{identity, retrieved_at, version?, version_kind?, content_sha256?, pointer_snapshot?}`, requiring at least one version or hash per supplied entry. Drafts MAY leave the map incomplete, including empty, but MUST expose the gap. Publication requires exactly the cited source-ID set, an original-byte hash, the provider version token when available and any recorded kind, and a complete `pointer_snapshot` in every entry.

`pointer_snapshot` is an immutable copy of the complete reviewed source pointer record, including its URI, owner, system, access policy, audience, and any extensions. It contains metadata, not source bytes. Its ID MUST match the map key; flat observation fields MUST equal the corresponding embedded fields. At capture, it MUST equal the selected catalog record. The concept's revision digest binds the entire snapshot, so later catalog edits cannot silently change the authority or protection metadata underlying approval.

Catalog observations may advance; reviewed snapshots MUST remain immutable. Runtime checks compare current identity, URI, revision stamps, source review deadlines, authority, and protection metadata against the reviewed snapshot. Changes to those fields require renewed review; merely advancing `retrieved_at` with otherwise unchanged evidence does not. Extending or removing a pointer's `stale_after` cannot cancel the captured deadline: the original reviewed deadline continues to apply until renewed review. An unsupported authority extension yields unknown assurance rather than being ignored. Updating a pointer cannot reapprove an old concept. Catalog verification and concept approval are separate operations.

## 6. Concept metadata and OKF compatibility

Concepts are UTF-8 Markdown with YAML frontmatter and a non-empty body. Copley producers require the following fields; ordinary OKF readers retain their less restrictive behavior.

| Field | Draft.2 requirement |
| --- | --- |
| `type`, `title`, `description` | Non-empty strings; type vocabulary remains open. |
| `status` | Explicit OKF value: `draft`, `stable`, or `deprecated`. |
| `sources` | Non-empty array of catalog citations with `id` and `resource`. |
| `generated` | `{by, at}` for the current production event. |
| `tags` | Array of unique non-empty strings; empty is valid. |
| `copley` | Required extension object described below. |
| `verified` | Optional historical verification mapping or non-empty event array. |
| `stale_after` | Optional proposed deadline in drafts; required before publication. |

Required `copley` fields are `spec_version`, `stable_id`, `owner`, `source_versions`, and `relationships`. Version is exactly `0.1.0-draft.2`; stable ID is an absolute URI unique within the bundle and the deployment's export scope. Owner may be `null` only while publication is blocked. Relationships is an array, possibly empty; each entry is `{relation, target}` where the relation is a non-empty local vocabulary string and target is another concept's stable ID **within this bundle**. External references use normal Markdown links or OKF resource fields, not an ambiguous relationship target.

Optional draft fields `copley.bundle_context`, `copley.review`, `copley.last_verified`, `copley.retrieval`, `copley.agent`, and `copley.sensitivity_label` are defined below. The sensitivity override MUST be interpreted through the manifest's model; it is not declassification authority. Unknown metadata MUST remain readable and be preserved during round trips, including inside namespaced objects. Unsupported requirements yield unknown assurance, not invented compliance.

Actor strings in `generated`, `verified`, and citation `author` follow OKF: `human:<id>`, `process:<id>`, or `<producer>/<version>`. Generators are not verifiers merely because they produced content. `verified: {by, at}` MUST be interpreted as a one-element array without discarding history. Producer attribution MUST reflect the actual producer; legacy `agent:` notation is not a new valid actor class.

Optional OKF fields such as `resource`, `usage_window`, and source credibility signals retain their meanings. Copley's catalog citations deliberately narrow `sources[].resource` to concrete absolute URIs; this does not invalidate broader OKF resources or scope descriptors for ordinary readers. Adoption counts cannot outrank source authority.

All Copley timestamps are RFC 3339 date-time strings with uppercase `T` and explicit `Z` or numeric timezone offset. Dates without times are invalid. Quote YAML timestamps. At or after `stale_after`, a revision is stale; the field is not a TTL. Missing OKF status defaults to stable for base interpretation only; Copley producers write it explicitly, and no fallback implies approval.

## 7. Work objects, agent documentation, and retrieval hints

Open type labels can describe people and roles; teams and organizational units; processes and workflows; content and datasets; systems, applications, APIs, and tools; meetings, decisions, actions, and commitments; metrics, computations, objectives, and policies. Labels such as `Person`, `Team`, `Process`, `System`, `Decision`, `Metric`, and `Policy` are conventions, not an enforced ontology. A relationship vocabulary may use `governed_by`, `uses_system`, or `owned_by`, but local meaning MUST be documented. Presence of edges does not establish a working graph integration.

An agent may be documented as a concept with `copley.agent`. If supplied, it requires `capabilities` (string array), `skills` (URI array), `tools` (array of `{id, resource, protocol?}`), `memory` (`{scope, retention}` descriptive strings), and `safety` (`{access_policy, approval_policy}` policy URIs). Optional `discovery` is an array of `{standard, resource}` references. Empty capability, skill, and tool arrays are permitted when accurate. These fields document boundaries; they do not grant authority, call endpoints, load skills, or prove MCP, A2A, or OASF interoperability.

Knowledge Markdown is not interchangeable with `AGENTS.md`, `SKILL.md`, or platform instruction files. Consumers MUST NOT auto-load instructions because a concept links to them. Explicitly trusted instruction repositories and their independent execution policies remain separate from factual authority.

Optional `copley.retrieval` restores retrieval-aware documentation without prescribing a search engine:

- `canonical_summary`: concise preferred description, protected like the body.
- `synonyms`: alternative phrases; `related_concepts`: in-bundle stable IDs.
- `chunking_strategy`: descriptive strategy name, such as `heading-aware`.
- `embedding_scope`: `none` or `approved-content-only`; not an embedding implementation.
- `exclusion_rules`: non-executable descriptions of material to exclude.
- `evaluation_questions`: questions for testing grounding, retrieval, and abstention.

These are optional hints, not executable policies or promises about proprietary retrieval behavior. Consumers MUST disclose supported hints and test their implementation. Unknown hints MUST NOT weaken protection. Indexes, chunks, embeddings, and evaluation answers inherit source-derived restrictions. Draft content MUST NOT enter an approved-content index merely because an embedding hint is present.

For `Attested Computation`, retain OKF's separate computation concept, required `runtime`, sanctioned computation, parameter declarations, executor, and deterministic attester model. Definition verification and per-run attestation remain distinct. Core does not execute computations, invent numeric results, or permit arbitrary code from referenced resources. A future execution implementation needs an independent reviewed security boundary and upstream contract tests.

## 8. Revision binding and human review

Each `copley.review` event contains `decision` (`approved` or `rejected`), `by` (human actor), `at` (timestamp), and `revision_sha256` (64 lowercase hexadecimal characters). Events are append-only exported evidence. They are not cryptographic signatures or proof that the named person acted.

For publication, `copley.bundle_context` MUST contain a small immutable context snapshot with `bundle_id`, `spec_version`, `okf_version`, `profile`, `schemas`, `sensitivity`, and `license`. Drafts MAY omit it. `bundle_id` MUST equal the current manifest's `id`; the other standard fields MUST exactly equal their corresponding current manifest values. The nested schemas and sensitivity objects are compared as complete JSON values, not selected subfields. Validate its shape against `#/$defs/bundleContext`.

This context stays inside ordinary candidate metadata, so the existing digest automatically binds identity, version pins, classification model/default label, schema pins, and license. Publication and mediated assurance MUST check current-manifest equality; any mismatch blocks reliance pending a new reviewed candidate. Unrelated manifest display text or bundle release-version changes alone do not invalidate unchanged context. Unknown policy extensions require explicit supported handling or unknown assurance. Runtime checks MUST NOT silently replace either `bundle_context` or pointer snapshots in an approved revision.

Compute the candidate digest as follows:

1. Parse frontmatter into JSON-compatible data. Reject duplicate mapping keys, YAML tags and aliases, implicit timestamp objects, non-finite numbers, and values outside RFC 8785's supported data model.
2. Remove top-level `verified`, `copley.review`, and `copley.last_verified`. Retain all other metadata, including unknown extensions and captured source snapshots.
3. Take the body immediately after the closing frontmatter delimiter's line ending. Normalize CRLF and CR to LF; preserve all other whitespace.
4. Construct `{ "metadata": <remaining mapping>, "body": <normalized body> }`, serialize using RFC 8785 JSON Canonicalization Scheme, and hash its UTF-8 bytes with SHA-256.

The digest appears only in excluded review evidence, never inside its own input. A reviewer approves final candidate metadata, including proposed stable status, assigned owner, source snapshots, and deadline. That candidate remains physically restricted until publication. Changing body, source observations, owner, expiry, or any other bound field changes the digest and requires new approval. Appending verification or review evidence does not.

If present, `copley.last_verified` is a derived convenience value: the latest `verified.at` whose human actor and instant match an approved review event for the current candidate digest. It MUST be omitted when no such event exists. It neither overrides a later rejection nor controls freshness. Generation MUST NOT manufacture verification events or dates to satisfy a schema.

Human corrections create a new explicit revision and remain durable. Regeneration MUST NOT silently overwrite those corrections or reuse their approval. Implementations SHOULD show a reviewable diff and retain provenance for both versions.

## 9. Lifecycle and currentness

New generation creates a restricted `draft`. Historical events may be retained, but never displayed as current sign-off without matching revision evidence. Reviewers resolve material conflicts or explicitly scope uncertainty before approving affected claims.

Publication requires assigned concept and source owners, complete hashed source snapshots with available version tokens and bound pointer metadata and bundle context, non-empty declared audiences, stable candidate status, an unexpired deadline, and current authenticated human approval. The publisher MUST verify reviewer identity and eligibility under deployment policy; a `human:` string alone establishes neither.

For the candidate digest, the latest decision is the greatest `at` instant. Conflicting tied decisions or indeterminate ordering block publication. The latest decision must be approval and have a human `verified` event with identical actor and instant. Exported evidence MUST be authenticated or re-established under the receiving deployment's policy before reliance; imported strings cannot self-authorize.

Immediately before publication commit, recheck candidate digest, manifest policy/schema pins, source identity, stamps, reviewed pointer authority/protection metadata, availability, and authorization boundaries. All recorded tokens and hashes must agree with current observations; a provider version-token change requires review even if bytes match. A newly available token changes the required evidence level and must be captured in a new reviewed candidate. Hash-only assurance requires a fresh, authorized retrieval and hash of the original source bytes; inability to retrieve or establish current bytes is unknown and withholds consumption. A stored hash alone is not a freshness check. Concurrent changes invalidate approval for the changed candidate. No atomic transaction across source and target is assumed.

A source change creates a new restricted draft for review, not an automatic update to an approved concept. Reaching either an applicable source deadline or the concept deadline requires review, even without detected source changes. Extending a concept deadline changes its digest. Deletion, confirmed access revocation, or an identity mismatch blocks current consumption; restoration does not automatically restore approval.

Runtime validity is separate from OKF status: `fresh`, `stale`, `unknown`, or `blocked`. Fresh requires all applicable checks to pass at the stated observation time. Known drift or expiry is stale; missing evidence is unknown; denied access, invalid approval, or unsafe delivery is blocked. Multiple conditions may coexist; deny/block takes precedence over a freshness label. None creates a fourth OKF status value.

A mediated runtime claiming assurance checks the requested revision, matching approval, stable status, deadlines, current source observations, and authorization. Failure or unknown required evidence withholds the current answer. Historical copies may remain accessible only to explicitly authorized reviewers in restricted storage, not as a last-known-good current response.

## 10. Authorization and safe operation

The derived audience MUST be no broader than the effective intersection of access established for **all** contributing sources. Same tenant, site, library, or generator identity does not establish alignment. Summarization is not declassification. Metadata, titles, footnotes, summaries, and search snippets require protection too.

For Copley-mediated requests, check the requesting identity's current source and artifact access before returning any protected content. Unavailable or insufficiently fresh evidence is unknown assurance and requires withholding. Cached grants cannot override detected revocations. Provider behavior and propagation limits MUST be disclosed.

Direct file reads, downloads, and other agents bypass mediated reauthorization. Enable these paths only inside enforced, aligned storage boundaries. Deployments MUST define and test ACL synchronization, quarantine, and invalidation for files, pages, search indexes, and caches. Removing an index entry or changing status is not a security control. Already downloaded copies cannot be recalled; instantaneous revocation propagation MUST NOT be claimed.

Declare detection, authorization propagation, and cache/index removal lag, including unknown bounds. If required boundaries cannot be met, withhold the affected path rather than rely on warnings. Separate draft and approved audiences through enforceable permissions, not labels.

Source text is untrusted data. Embedded instructions MUST NOT change policy, invoke tools, disclose unrelated information, or select publication targets. Sanitize Markdown, reject active content and unsafe links, and prevent automatic remote resource loading. A schema-valid URI is not safe to fetch: network operations require explicitly allowed schemes, origins, redirects, credentials, and private-network boundaries.

Producers MUST declare extraction support and reject failed, empty, unsupported, or encrypted inputs clearly. They MUST exclude generated targets and projections using stable identifiers to prevent feedback loops. Use retry-safe writes, durable checkpoints, per-concept concurrency control, and deduplication covering source identity/version and generation configuration. Repeated jobs cannot duplicate logical concepts or approvals.

Enumerate every page in a selected scope. Partial listings do not prove deletion; affected assurance becomes unknown and destructive cleanup requires confirmed evidence. Prepare and validate content before updating the index. Consumers validate referenced revisions independently; mixed multi-file states are unavailable, not silently current. Crashes leave recoverable state rather than overwriting newer work.

Deployments MUST document processors, data residency, extraction caches, retention, exports, and backups. Only approved providers and locations receive protected content. Logs avoid source text, credentials, and unnecessarily identifying URLs.

## 11. Optional SharePoint implementation profile

A reference interaction uses delegated Entra sign-in; accessible-site search with explicit site-URL fallback; source library/document selection; and selection or permitted creation of an ordinary target library. Discovery is not authorization proof. Access MUST be verified for selected resources, including the intended derived audience.

Implementers MUST validate current Microsoft Graph permissions and consent requirements per operation. Reading, searching, and library creation are distinct capabilities. If creation is unavailable, select an existing authorized target or stop; do not request blanket full control as a workaround. Core does not require SharePoint Embedded or app-only tenant enumeration.

TXT, Markdown, DOCX, and text-based PDF are suggested bootstrap extraction formats, not compulsory Core parsers. OCR and complex layouts are explicitly declared capabilities. Manual generation is sufficient; unattended schedules require separately reviewed identity, consent, token lifecycle, and reconciliation. A delegated interactive session implies no indefinite background authority.

Native search or Microsoft Copilot ingestion requires explicit compatibility testing for the actual product and path, including authorization, citations, metadata interpretation, freshness, and removal. File presence does not establish ingestion or respect for Copley review state. Existing Microsoft governance is complementary; Copley does not claim to replace it or supply untested integration.

## 12. Machine schema and validation interface

`copley.schema.json` is a non-executable JSON Schema Draft 2020-12 artifact with `$id` `urn:copley:schema:0.1.0-draft.2`. It allows additional object properties to preserve extensions. Validators MUST enable `format` assertions as well as ordinary schema keywords; format annotations alone are insufficient.

| Input | Schema entry point |
| --- | --- |
| Parsed manifest | `#/$defs/manifest` |
| Source pointer JSON | `#/$defs/source` |
| Parsed concept frontmatter | `#/$defs/concept` |
| Publication source prerequisites | `#/$defs/publicationSource` |
| Publication concept prerequisites | `#/$defs/publicationConcept` |
| Reviewed bundle policy context | `#/$defs/bundleContext` |
| `{path, metadata, body}` concept test record | `#/$defs/conceptRecord` |
| Test/transport envelope | Root or `#/$defs/bundle` |

Publication definitions require stronger shapes, including source hashes, complete pointer snapshots and `bundle_context`, assigned owners, stable status, deadline, human verification, and an approval event. Token availability and the validity of a hash-only evidence level are semantic/runtime checks, not conclusions drawn from a missing JSON field. They cannot establish a matching hash, latest decision, real identity, expiry, or live authorization. Publication envelope mode applies these prerequisites to every included source and concept; a mixed draft/history working set uses draft mode and evaluates publication candidates separately.

`copley-example-bundle.json` is a complete synthetic envelope `{manifest, sources, concepts}`. Each concept record contains `path`, parsed `metadata`, and `body`. It is **not** an additional file required inside physical bundles and does not contain an index file. A materializer writes the declared files and generates the root index. Its two concepts and two pointers illustrate multi-source knowledge, in-bundle relationships, missing draft ownership, and absence of fabricated verification. Example URLs are inert fixture identifiers, not live evidence.

A companion validator's interface MUST separate parsing/schema checks, offline semantic checks, and optional live assurance. Reports identify spec version, mode, role, record/path, check name, outcome, observation time where applicable, and actionable diagnostics. Required offline semantic checks include unique source IDs, canonical URIs, identities, concept paths and stable IDs; filename-ID agreement; citation/resource/catalog joins; exact publication snapshot coverage and embedded/flat observation agreement; immutable pointer-snapshot and bundle-context binding plus exact current-manifest context comparisons; available-token capture and declared evidence level; relationship and retrieval-reference resolution; footnote joins; essential links; derived verification values; and revision digest/decision matching.

Offline checks also distinguish a captured snapshot from a newer catalog observation. They MUST NOT edit either to make a test pass. Live freshness checks are separate, explicitly consented connector capabilities. CI SHOULD default to offline synthetic fixtures with no arbitrary URL fetching, production credentials, or real customer data. SHACL is relevant only to a future specified SemanticExport profile.

## 13. Minimum acceptance cases

The following are required test intentions for implementations, not claims of implemented or executed integration tests:

| Case | Expected result |
| --- | --- |
| Type-only OKF, unknown type/key | Read as OKF; preserve extensions; do not claim Copley Core success. |
| Supplied synthetic envelope | Pass draft structure and joins; fail publication prerequisites. |
| Missing resource, malformed datetime/hash, unsupported spec | Fail applicable static check with location. |
| Bare verification mapping versus one-element array | Equivalent interpretation, not automatic approval. |
| Missing or duplicate source ID; mismatched URI | Fail semantic resolution even if JSON Schema accepts it. |
| Multi-source concept with one denied source | Withhold all protected derived content. |
| Pointer advances, reviewed snapshot unchanged | Detect drift; never mutate snapshot or inherit approval. |
| Pointer owner, URI, or access policy changes | Compare bound pointer snapshot; require review, not silent authority replacement. |
| Source deadline extended or removed | Retain captured expiry; require review before changing it. |
| Source token changes; byte hash unchanged | Require review of changed observation. |
| Hash-only source; provider has no token versus unknown availability | Permit the stated evidence level only for established no-token capability; otherwise unknown assurance. |
| Manifest schema pin, sensitivity, or license changes | Compare immutable `bundle_context` with current manifest; mismatch requires review. |
| Expiry with unchanged sources | Stale; no automatic extension or verification. |
| Signed evidence conflicts with popular draft | Surface conflict; resolve authority, not popularity. |
| Candidate/body changes during review | Digest or conditional write fails; renewed review. |
| Forged human string or tied conflicting decisions | Block publication; identity and ordering matter. |
| Source changes around publication commit | Precommit detection blocks; later detection stops mediated serving and triggers remediation. |
| Direct reader after permission change | Test ACL/quarantine behavior and disclose lag; no mediated-assurance claim. |
| Later scan page fails | Unknown completeness; no inferred mass deletion. |
| Retry, partial write, index mismatch | Recover one logical revision; do not serve mixed state. |
| Embedded disclosure/tool instruction | Treat as untrusted evidence text; never execute. |
| Unknown extension or retrieval hint | Preserve; do not infer capability or weaken policy. |

Deployment tests additionally cover unsupported extraction, correction preservation, source deletion, cache removal, and every enabled ingestion path. Synthetic tests establish bounded behavior, not universal correctness or actual platform compatibility.

## 14. Migration from earlier proposals and October 9 draft

Draft.2 restores the bundle-wide contract while retaining source authority, human review, permission alignment, and portable Markdown. It supersedes the October 9 review text for this proposal; it is not a ratified release or a backward-compatibility guarantee.

| Earlier form or assumption | Draft.2 treatment |
| --- | --- |
| `workiq.yaml` | Rename to `copley.yaml`; import-only alias may warn, never create two authoritative manifests. |
| No manifest or pointer catalog | Add explicit bundle metadata and `sources/<id>.json`; stage unobserved candidates outside valid Core, never fabricate evidence. |
| Unbound or earlier full manifest context | Capture the specified `copley.bundle_context`; remove competing context representations from canonical output. Changed metadata requires a new digest and review. |
| Earlier Markdown pointer proposal | Import pointer metadata into JSON companion records, outside OKF concept typing; preserve original canonical citation URIs. Do not retain two competing pointer routes or copy raw source bytes. |
| Top-level concept `id` / `owner` | Explicitly map logical identity to `copley.stable_id` / `copley.owner`; retain OKF path identity separately. Conflicts require review, not silent precedence. |
| Source `ref` without `resource` | Resolve the actual canonical pointer URI and write `id` plus `resource`; a path rename alone is insufficient. |
| Snapshot `version` or earlier `etag` | Preserve generic opaque `version`; migrate an actual ETag to `version` with `version_kind: etag`. Never fabricate tokens or infer their availability. |
| Bare dates; `agent:` attribution | Obtain justified timezone instants and actual producer/version attribution. Never guess historical verification. |
| Required `last_verified` on new drafts | Omit until supported by recorded events; distinguish source history from current concept approval. |
| Top-level relationships/retrieval fields | Move explicitly into `copley.relationships` / `copley.retrieval`, preserving meaning and resolving stable IDs. |
| One concept per source; universal SHACL CI | Bootstrap mode only; Core is topic-centered and JSON Schema based. |
| Agent/graph integration tiers | Reserved future profiles; documentation or mappings do not prove interoperability. |

Canonical producers MUST NOT emit competing legacy and current identity/owner fields. Importers SHOULD preserve originals in restricted migration history, report unmapped values, and create reviewable drafts. Changed metadata, namespacing, snapshots, or hash rules require recomputation and new approval; existing signatures or digest strings are not assumed compatible. No existing implementation has been validated against this migration.

## 15. Evolution, governance, and source notes

Specification versioning is independent of bundle versions and OKF versions. Future breaking profile changes require explicit migration guidance and fixtures. A proposed maintainer process should review public change proposals, publish decision rationale, and distinguish draft, accepted, and deprecated specification revisions. This is a proposal for governance, not an assertion that a governing body or ratification process already exists.

Open decisions include portable authentication of exported review evidence, deployment-specific reviewer authority, direct-access revocation limits, graph crosswalks, and extension conformance tests. Publication-capable deployments MUST settle and test their relevant authority and protection policies rather than treating these open areas as implicit permission.

Copley's license and contributor/IP terms require maintainer confirmation. OKF's Apache-2.0 license does not automatically license Copley, borrowed schemas, source material, or implementations. Preserve applicable upstream attribution; this draft creates no new license grant.

Public references provide context, not proof of implementation:

- [Open Knowledge Format, v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) — base syntax and semantics; the linked main branch may evolve, so implementations must pin their reviewed baseline.
- [Retrieval Got Solved. Trust Didn't.](https://www.synozur.com/insights/retrieval-got-solved-trust-didnt-meet-copley) — original public framing.
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema) and [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html) — structural validation and deterministic candidate serialization.
- [Work IQ overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/) — complementary platform context, not endorsement or Copley compatibility evidence.
