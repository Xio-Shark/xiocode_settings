---
name: code-simplifier
description: "Use when simplifying recently changed code without changing behavior."
---

# Code Simplifier

## Overview

Refine code for clarity, consistency, and maintainability while preserving exact functionality.

## Rules

- Do not change behavior.
- Focus on recently modified code unless the user expands scope.
- Prefer clearer structure over clever compression.
- Remove unnecessary complexity, duplication, and low-value comments.

## When to use

- post-edit cleanup
- simplification pass
- maintainability refinement
- reducing noise in recently changed code

## Workflow

1. Identify the recently changed scope.
2. Remove unnecessary nesting, duplication, and weak abstractions.
3. Align with project naming and style conventions.
4. Keep helpful structure; do not flatten so hard that debugging gets worse.
5. Re-verify that behavior is unchanged.

## Focus points

- readability
- local consistency
- explicit logic
- maintainable control flow
