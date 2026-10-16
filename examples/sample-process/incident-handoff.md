---
id: workiq.process.incident-handoff
type: Process
title: Incident Handoff
description: Standard handoff between on-call responders and service owners.
status: current
owner: team:operations
sources:
  - id: incident-runbook
    resource: runbooks/incident-handoff.md
    author: team:operations
    last_modified: 2026-07-12
last_verified: 2026-07-21
stale_after: 2026-09-30
tags: [incident, handoff, operations]
relationships:
  related_processes: [workiq.process.customer-renewal]
  uses_systems: [pagerduty, jira]
inputs:
  - incident summary
  - owner acknowledgment
outputs:
  - resolved handoff record
---

# Incident Handoff

This concept demonstrates a second process document that can be cross-referenced from other bundles and examples.
