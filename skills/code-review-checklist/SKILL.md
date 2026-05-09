---
name: code-review-checklist
description: "Use when reviewing code."
---

# Code Review Checklist

## Overview

Use this skill as a compact checklist for code review work.

## Rules

- Prioritize correctness and security before style.
- Report concrete issues, not vague discomfort.
- Distinguish blocking findings from minor suggestions.
- Prefer exact file/line references when possible.

## Review areas

- correctness
- security
- performance
- code quality
- testing
- documentation

## Workflow

1. Check whether the code actually does what it claims.
2. Look for security and data-handling issues.
3. Review performance-sensitive paths and obvious inefficiencies.
4. Evaluate readability, duplication, abstraction level, and maintainability.
5. Confirm testing and documentation are adequate for the change.

## Output expectations

- blocking issues
- important improvements
- minor nits or questions
- positive findings when relevant
