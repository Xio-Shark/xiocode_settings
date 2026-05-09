---
name: web-design-guidelines
description: "Use when auditing a web UI."
---

# Web Design Guidelines

## Overview

Audit implemented UI files against current web interface guidelines and report findings with concrete file/line references.

## Rules

- Fetch the latest guideline source before auditing.
- Review the actual target files, not the whole repo by default.
- Output findings tersely and concretely.
- If no target files are provided, ask which files or patterns should be audited.

## When to use

- UI audit
- accessibility review
- design guideline compliance check
- “review my UI” style requests

## Workflow

1. Fetch the latest guideline document from the source URL.
2. Read the requested files or file pattern.
3. Compare implementation against the fetched rules.
4. Return findings in terse `file:line` style.

## Guideline source

`https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`
