---
id: skill.renewal-summary
type: Skill
title: Renewal Summary Skill
description: Reusable skill for preparing a concise renewal status summary.
status: current
owner: team:customer-success
sources:
  - id: renewal-summary-template
    resource: templates/renewal-summary.md
    author: team:customer-success
    last_modified: 2026-07-10
last_verified: 2026-07-24
stale_after: 2026-10-24
tags: [skill, renewal, summary]
relationships:
  used_by_agents: [agent:renewal-assistant]
inputs:
  - account metadata
  - renewal date
  - risk indicators
outputs:
  - summary brief
preconditions:
  - account metadata is accessible
approval_rules:
  - human review required before customer-facing reuse
---

# Renewal Summary Skill

This skill produces a short, evidence-linked renewal summary for internal review.
