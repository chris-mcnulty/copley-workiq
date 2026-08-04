# MCP Crosswalk

The Model Context Protocol (MCP) standardizes runtime access to resources, prompts, and tools. Work IQ Open Format adds durable, versioned documentation about the work and agent context behind those runtime interfaces.

| Work IQ Open Format field/object | MCP mapping | What MCP covers | What this profile adds |
| --- | --- | --- | --- |
| Agent record | MCP server or resource documentation | Runtime resources and tools | Lifecycle, ownership, trust, and approval metadata |
| Skills | MCP prompts or documented workflows | Prompt and tool exposure | Stable governance and validation for skill records |
| Tools / MCP endpoints | MCP tools and resources | Invocation contracts | Memory boundaries, safety rules, and attestation context |
| `evaluation_questions` | No direct MCP field | N/A | Retrieval evaluation prompts for bundle quality |
| `exclusion_rules` | No direct MCP field | N/A | Indexing and suppression guidance for brokers and agents |
