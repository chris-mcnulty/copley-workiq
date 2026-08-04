---
id: workiq.process.customer-renewal
type: Process
title: Customer Renewal Process
description: Standard work pattern for managing renewals across account, delivery, and finance teams.
status: stable
version: 1.0.0
owner: team:customer-success
tags: [renewal, account-management, revenue]
sources:
  - id: crm-renewal-playbook
    resource: docs/renewal-playbook.md
    author: team:customer-success
    last_modified: 2026-07-15
generated:
  by: agent:workiq-curator
  at: 2026-07-20T14:00:00Z
verified:
  - by: human:process-owner
    at: 2026-07-22T09:00:00Z
last_verified: 2026-07-22
stale_after: 2026-10-01
relationships:
  uses_systems: [salesforce, sharepoint, teams]
  produces: [renewal-forecast, account-risk-summary]
  related_skills: [skill.renewal-summary, skill.account-risk-review]
---

# Customer Renewal Process

This process coordinates renewal preparation, risk review, and commercial approval before a customer contract end date.

## Purpose

Keep renewal decisions consistent across account, delivery, and finance teams while preserving an auditable record of the inputs used.

## Main steps

1. Review upcoming renewal dates and account health signals.
2. Prepare a renewal summary and identify risk indicators.
3. Confirm delivery commitments and finance assumptions.
4. Publish the renewal forecast and account risk summary.
