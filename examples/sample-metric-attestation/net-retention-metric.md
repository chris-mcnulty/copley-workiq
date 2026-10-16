---
id: workiq.metric.net-retention
type: Metric
title: Net Revenue Retention
description: Approved computation for evaluating recurring revenue retention.
status: current
owner: team:finance-operations
sources:
  - id: warehouse-query-nrr
    resource: sql/net_retention.sql
    author: team:finance-operations
    last_modified: 2026-07-11
last_verified: 2026-07-25
stale_after: 2026-10-15
tags: [metric, finance, retention]
relationships:
  informs_processes: [workiq.process.customer-renewal]
attestation:
  reviewer: human:finance-controller
  approved_at: 2026-07-25T16:00:00Z
  evidence:
    - approved query hash:sha256:example
    - dashboard snapshot retained in finance evidence archive
decision_log:
  - decision: Approved as the standard retention metric for renewal planning.
    date: 2026-07-25
    by: council:revenue-operations
canonical_summary: Approved metric definition for net revenue retention used in renewal planning.
evaluation_questions:
  - Can a reviewer identify the approved query and signoff?
  - Is the freshness window still valid for quarterly planning?
---

# Net Revenue Retention

This metric concept demonstrates how to capture an attested computation with evidence and reviewer signoff in frontmatter.
