---
name: server-management
description: "Use when operating or managing servers."
---

# Server Management

## Overview

Use this skill for practical server operations decisions rather than memorizing commands.

## Rules

- Prefer boring, recoverable operations over clever but fragile setups.
- Monitoring, restart behavior, and rollback paths matter as much as the deploy itself.
- Check process state, logs, resources, and dependencies in that order when troubleshooting.
- Run production services with least privilege and explicit access controls.

## When to use

- process management decisions
- monitoring and alerting setup
- scaling choices
- health-check strategy
- production server troubleshooting

## Workflow

1. Clarify workload type and runtime shape.
2. Choose process/runtime control: systemd, PM2, containers, or orchestration.
3. Define health checks, monitoring, logs, and restart behavior.
4. Review scaling needs only after understanding actual bottlenecks.
5. Keep security, backup, and audit basics in place.

## Focus points

- process lifecycle
- observability
- resource pressure
- scaling strategy
- operational safety
