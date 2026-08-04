# Adoption Playbook

## Recommended rollout path

Organizations **SHOULD** roll out Work IQ Open Format in stages:

1. **Core Bundle** — capture trusted concepts and processes with required frontmatter.
2. **Agent Profile** — document approved agents, capabilities, tools, and safety boundaries.
3. **Semantic Export** — add RDF / JSON-LD / DCAT / PROV export when graph interoperability becomes valuable.

This sequence keeps early adoption lightweight while preserving a path to deeper interoperability.

## How the format fits existing retrieval

Work IQ Open Format augments an existing brokered-retrieval layer such as Work IQ rather than replacing it. A broker can continue handling permissions, ranking, and source retrieval while this format provides:

- durable bundle packaging
- explicit freshness and verification metadata
- agent-readable safety and approval constraints
- optional semantic export for graph consumers

## Suggested first rollout

- Pick one team-owned process and one attested metric.
- Validate them in CI.
- Train contributors to review `sources`, `verified`, and `stale_after` fields.
- Add agent records only after the team is comfortable maintaining Core Bundle artifacts.

## Success measures

Look for:

- reduced ambiguity about what is authoritative
- faster review of agent-usable knowledge
- clearer ownership and refresh expectations

**TODO:** add a maintainer-approved maturity checklist after the first public pilot.
