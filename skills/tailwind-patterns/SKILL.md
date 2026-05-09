---
name: tailwind-patterns
description: "Use when designing or reviewing UI built with Tailwind CSS v4."
---

# Tailwind Patterns

## Overview

Use this skill when the codebase relies on Tailwind CSS v4 and you need practical guidance on tokens, responsive layout, container queries, or component extraction.

## Rules

- Default to Tailwind v4 CSS-first patterns, not legacy config-heavy v3 habits.
- Prefer semantic tokens and reusable layout patterns over arbitrary one-off utility piles.
- Use container queries for component-level responsiveness and viewport breakpoints for page layout.
- Extract repeated utility bundles into components or structured tokens before class lists become unreadable.

## When to use

- Building or refactoring Tailwind-based UI
- Reviewing token architecture, layout decisions, or responsive behavior
- Migrating toward Tailwind v4 patterns
- Cleaning up utility sprawl in a design system

## Workflow

1. Confirm the project is using Tailwind v4 conventions.
2. Identify whether the problem is tokens, layout, responsiveness, dark mode, or component extraction.
3. Prefer semantic design tokens and CSS-first configuration.
4. Choose responsive strategy:
   - viewport breakpoints for page structure
   - container queries for reusable components
5. If utility repetition grows, extract the pattern into components, tokens, or a small shared abstraction.

## Core guidance

- Use semantic color and spacing tokens
- Favor asymmetric layouts over interchangeable generic grids
- Keep typography, dark mode, and transitions intentional rather than default
- Avoid heavy `@apply`, inline styles, and arbitrary values everywhere

## Reference use

If deeper examples are needed, load the specific reference or project files rather than expanding the main skill body.
