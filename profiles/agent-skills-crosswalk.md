# Agent Skills Crosswalk

Agent Skills formats such as `SKILL.md` describe reusable agent procedures. Work IQ Open Format adds typed frontmatter, provenance, and cross-bundle linking so skills can be validated and governed alongside other work concepts.

| Work IQ Open Format field/object | Agent Skills mapping | What Agent Skills covers | What this profile adds |
| --- | --- | --- | --- |
| Skill Markdown document | `SKILL.md` body | Human-readable execution guidance | Required frontmatter and schema validation |
| `inputs` / `outputs` | Skill prerequisites and outcomes | Operational instructions | Typed, reusable metadata for indexing |
| `approval_rules` | Safety notes | Informal guardrails | Structured approval and access controls |
| `related_concepts` | Linked references | Optional references | Stable graph links into a broader work bundle |
| `canonical_summary` | Summary section | Human orientation | Retrieval-aware summarization semantics |
