---
name: performance-profiling
description: "Use when profiling software performance."
---

# Performance Profiling

## Overview

Profile first, then optimize the actual bottleneck.

## Rules

- Never guess performance problems without measurement.
- Fix the largest bottleneck before micro-optimizing smaller ones.
- Validate every optimization with before/after evidence.
- Prefer removing unnecessary work over making bad work slightly faster.

## When to use

- slow page load
- slow interactions
- runtime jank
- memory growth
- bundle or network performance analysis

## Workflow

1. Measure the baseline.
2. Identify the dominant bottleneck.
3. Apply one targeted optimization.
4. Re-measure to confirm the change helped.

## Common focus areas

- page load and Core Web Vitals
- bundle size
- runtime main-thread cost
- rendering work
- memory retention
- network waterfalls

## References

- `scripts/lighthouse_audit.py`
