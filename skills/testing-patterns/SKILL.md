---
name: testing-patterns
description: "Use when designing or improving a test strategy for unit, integration, or end-to-end coverage."
---

# Testing Patterns

## Overview

Use this skill for test strategy decisions, test layering, and reliability improvements.

## Rules

- Test behavior, not internal implementation trivia.
- Pick the cheapest test level that can prove the requirement.
- Keep tests isolated, deterministic, and readable.
- Fix flaky behavior at the root cause instead of normalizing instability.

## When to use

- choosing unit vs integration vs e2e coverage
- designing test structure
- mocking strategy
- cleaning up flaky or noisy suites

## Workflow

1. Identify what risk must be proved.
2. Choose the right test layer.
3. Define setup, data, and dependency boundaries.
4. Write clear assertions and stable test names.
5. Remove duplication and fix flakiness before expanding coverage.

## Focus points

- testing pyramid balance
- AAA structure
- mock boundaries
- test data strategy
- cleanup and repeatability
