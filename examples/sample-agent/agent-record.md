---
id: agent:renewal-assistant
type: Agent
title: Renewal Assistant
description: Agent record for preparing renewal briefs and routing approvals.
status: current
owner: team:customer-success
sources:
  - id: agent-runbook
    resource: runbooks/renewal-assistant.md
    author: team:customer-success
    last_modified: 2026-07-18
last_verified: 2026-07-24
stale_after: 2026-10-24
tags: [agent, renewal, approvals]
relationships:
  supports_processes: [workiq.process.customer-renewal]
  uses_skills: [skill.renewal-summary]
capabilities:
  - summarize renewal context
  - identify missing approval inputs
skills:
  - skill.renewal-summary
tools:
  - name: Renewal CRM Lookup
    kind: mcp-tool
    endpoint: mcp://renewals/crm-lookup
    mcp_resource: renewals.crm.lookup
discovery:
  a2a: renewal-assistant
  oasf_taxonomy: workflow-assistant
memory_scope:
  retention: session-only unless explicitly attached to a bundle update
  boundary: may retain task context but not copy restricted source documents into long-term memory
safety_rules:
  - Require human review before sending external communications.
  - Refuse actions that change commercial terms without approval.
approval_rules:
  - Finance approval is required for non-standard pricing.
---

# Renewal Assistant

The Renewal Assistant helps prepare internal renewal briefs and checks that the required humans have reviewed the package before action.
