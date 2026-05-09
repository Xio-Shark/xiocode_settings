---
name: python-patterns
description: "Use when designing or implementing Python code."
---

# Python Patterns

## Overview

Use this skill for practical Python architecture choices rather than copy-paste snippets.

## Rules

- Choose framework and structure based on the actual product shape, not habit.
- Use async only for I/O-bound workloads that benefit from it.
- Type public APIs and important boundaries; do not overtype every local variable.
- Validate data at the boundary and keep project structure proportional to size.

## When to use

- Choosing between FastAPI, Django, Flask, or a simpler Python shape
- Deciding sync vs async design
- Structuring Python projects or services
- Applying typing, validation, or service-layer boundaries

## Workflow

1. Clarify what is being built: script, API, full-stack app, worker, or service.
2. Pick framework/runtime shape that matches the product and team constraints.
3. Decide sync vs async from workload characteristics.
4. Design boundaries:
   - routes/controllers
   - services
   - models or repositories
   - schemas/validation
5. Add types and validation where they improve correctness and readability.

## Guidance

- API-first or async-heavy service -> FastAPI is often the default
- Full-stack/admin-heavy app -> Django is often the default
- Small/simple app or script -> lighter structure is usually enough
- I/O-bound -> async
- CPU-bound -> sync plus dedicated workers or multiprocessing

## Output expectations

- explain the chosen framework or architecture
- call out tradeoffs
- keep the code idiomatic and proportionate
