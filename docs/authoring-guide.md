# Authoring Guide

## Authoring principles

- Keep bundles plain-text and Git-friendly.
- Prefer specific source citations over vague descriptions.
- Record freshness and review expectations in frontmatter.
- Use `TODO:` for open design questions.

## Concept authoring pattern

Each concept file contains:

1. YAML frontmatter validated by JSON Schema
2. a Markdown body that explains the concept for human readers

Recommended body sections:

- purpose
- trigger or usage context
- main steps or interpretation notes
- exceptions or escalation guidance
- linked systems, teams, or evidence

## Retrieval-aware authoring

When useful, add:

- `canonical_summary` for stable retrieval snippets
- `synonyms` for search expansion
- `evaluation_questions` for bundle quality review
- `exclusion_rules` for content that should not be embedded or surfaced automatically

## Agent Profile guidance

Agent records should describe:

- what the agent is allowed to do
- which tools or MCP endpoints it can use
- what memory it may retain
- when approval is required before action
