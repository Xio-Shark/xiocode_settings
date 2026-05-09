---
name: clean-code
description: "Use when cleaning up or simplifying code."
---

# Clean Code

## Overview

Apply pragmatic coding standards that favor simplicity, readability, and low ceremony.

## Rules

- Prefer the simplest code that clearly solves the problem.
- Keep functions small and responsibilities narrow.
- Avoid unnecessary helpers, files, abstractions, and comments.
- Name things so the code explains itself.
- Edit all directly affected files in the same task; do not leave dependent code broken.

## When to use

- Implementing or refactoring application code
- Cleaning up over-engineered or noisy logic
- Reviewing code for maintainability and clarity

## Workflow

1. Understand what the code is supposed to do and what files depend on it.
2. Remove duplication and dead structure before adding new layers.
3. Flatten control flow with guard clauses and clear naming.
4. Keep responsibilities local and coherent.
5. Verify behavior after the cleanup.

## Focus points

- small functions
- clear names
- minimal nesting
- explicit constants instead of magic numbers
- no tutorial-style narration in code comments

## Completion check

- goal met
- all affected files updated
- verification run
- no broken imports or obvious regressions
