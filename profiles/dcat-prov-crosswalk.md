# DCAT and PROV Crosswalk

DCAT and PROV help represent catalog and provenance views of a bundle’s contents. Work IQ Open Format adds operational authoring rules, conformance tiers, and retrieval-aware fields that those vocabularies do not define.

| Work IQ Open Format / Copley field/object | DCAT / PROV mapping | What DCAT / PROV covers | What this profile adds |
| --- | --- | --- | --- |
| Bundle manifest | `dcat:Dataset` / `dcat:CatalogRecord` | Dataset discovery and catalog metadata | Conformance claims and bundle-native validation settings |
| Concept document | `dcat:Resource` or domain entity | Resource-level metadata | Required frontmatter shape for work intelligence |
| `sources` | `prov:wasDerivedFrom` | Upstream lineage | Source formatting rules for bundles |
| `generated.by`, `generated.at` | `prov:wasGeneratedBy`, `prov:generatedAtTime` | Generation provenance | Human-readable authoring guidance |
| `verified` / `attestation` | `prov:qualifiedAttribution` / `prov:wasInfluencedBy` | Reviewer and activity modeling | Freshness windows and safe-to-act review signals |
| `stale_after` | No exact standard term | N/A | Operational freshness deadline for retrieval systems |
