---
name: nodejs-best-practices
description: "Use when designing or implementing non-trivial Node.js code and you need framework, runtime, async, or architecture guidance."
---

# Node.js Best Practices

## Overview

Use this skill for Node.js design decisions, not for memorizing boilerplate.

## Rules

- Pick framework and runtime from deployment target, performance needs, and team constraints.
- Keep HTTP concerns, business logic, and data access separate when the app is large enough to justify it.
- Use async patterns deliberately; do not block the event loop with heavy CPU work.
- Validate untrusted inputs at boundaries and keep security concerns explicit.

## When to use

- Choosing between Hono, Fastify, Express, Next API routes, or a similar Node shape
- Designing Node.js service architecture
- Reviewing async behavior, validation, or error handling
- Making runtime or module-system decisions

## Workflow

1. Clarify deployment target and app shape.
2. Choose framework/runtime based on cold start, throughput, ecosystem, and team familiarity.
3. Keep architecture layered when complexity justifies it.
4. Choose async patterns that match the workload.
5. Apply validation, error handling, and security at the system boundary.

## Guidance

- Edge/serverless -> Hono is often a fit
- High-performance API -> Fastify is often a fit
- Legacy or maximum ecosystem compatibility -> Express is often a fit
- Full-stack app with frontend coupling -> Next API routes or similar may be enough

## Output expectations

- justify the selected framework or runtime
- call out event-loop and security implications
- keep implementation guidance concrete
