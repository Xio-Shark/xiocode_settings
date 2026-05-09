---
name: database-design
description: "Use when choosing a database or designing schemas, indexes, ORM strategy, or migrations."
---

# Database Design

## Overview

Use this skill for practical database decisions around storage engine, schema shape, indexing, and migration safety.

## Rules

- Choose the database and ORM from workload, deployment, and team constraints.
- Model relationships and indexes from the access pattern, not just entity diagrams.
- Keep migrations safe and reversible when possible.
- Treat query plans and N+1 risks as design concerns, not post-launch surprises.

## When to use

- database selection
- schema design
- indexing strategy
- ORM choice
- migration planning

## Workflow

1. Clarify data model, scale, and deployment environment.
2. Choose the database and ORM that fit the actual system.
3. Design schema, relationships, and constraints.
4. Add indexes from query shape and performance risk.
5. Plan migrations and operational safety.

## Focus points

- schema normalization vs denormalization
- query-driven indexes
- transaction and consistency needs
- migration safety
- avoiding obvious query anti-patterns
