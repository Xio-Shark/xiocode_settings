---
name: code-explorer
description: "Use when deeply analyzing how a feature works across an existing codebase."
---

# Code Explorer

## Overview

Trace a feature from entry point through implementation layers so later work starts from real code understanding.

## Rules

- Start from entry points and follow execution flow instead of skimming files randomly.
- Map responsibilities, dependencies, and data flow across layers.
- Use file and line references in findings.
- Prioritize understanding over premature solution design.

## When to use

- feature exploration
- architecture tracing
- dependency mapping
- preparing to modify or extend unfamiliar code

## Workflow

1. Find entry points.
2. Trace the main execution path through business logic and data layers.
3. Identify important transformations, dependencies, and side effects.
4. Summarize the key files and architectural decisions needed to understand the feature.

## Output expectations

- entry points
- execution flow
- key components and responsibilities
- major dependencies
- essential file list
