---
name: api-patterns
description: "Use when designing an API."
---

# API Patterns

## Overview

Choose API design patterns that fit the actual clients, system constraints, and evolution plan.

## Rules

- Pick API style from context instead of defaulting to REST automatically.
- Keep response formats and error shapes consistent.
- Plan auth, rate limiting, and versioning early for non-trivial APIs.
- Read only the reference material relevant to the current API decision.

## When to use

- choosing REST vs GraphQL vs tRPC
- designing response envelopes and error formats
- planning versioning
- deciding auth or rate limiting patterns

## Workflow

1. Identify API consumers and product constraints.
2. Choose the API style that best fits those consumers.
3. Define response, error, pagination, and versioning rules.
4. Decide authentication and rate limiting strategy.
5. Produce a consistent contract and documentation plan.

## References

- `api-style.md`
- `rest.md`
- `response.md`
- `graphql.md`
- `trpc.md`
- `versioning.md`
- `auth.md`
- `rate-limiting.md`
- `documentation.md`
- `security-testing.md`
