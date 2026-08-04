# OKF Profile Crosswalk

Work IQ Open Format uses OKF as the base bundle packaging model and adds trust, lifecycle, and retrieval-aware conventions that OKF does not standardize by itself.

| Work IQ Open Format field/object | OKF alignment | What OKF covers | What this profile adds |
| --- | --- | --- | --- |
| `workiq.yaml` manifest | OKF bundle manifest pattern | Bundle packaging, file-based distribution | Conformance profile, sensitivity model, validation rules |
| Concept Markdown + frontmatter | OKF content object in bundle | Plain-text bundled artifacts | Required trust metadata and common work-object fields |
| `sources`, `generated`, `verified` | Related provenance metadata | General descriptive metadata | Reviewability, freshness, and agent-safe use rules |
| `canonical_summary`, `synonyms`, `chunking_strategy` | No direct OKF requirement | N/A | Retrieval-aware behavior for indexing and explanation |
| Agent records and skills | Optional bundle artifacts | Storage of files in the bundle | Shared structure for agent discovery and operation |
| Conformance tiers | Profile-level convention | N/A | Incremental adoption path from Core Bundle to Semantic Export |
