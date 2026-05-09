---
name: gh-address-comments
description: "Use when addressing review comments on the open GitHub PR for the current branch."
---

# GH Address Comments

## Overview

Use GitHub CLI to inspect open PR comments, summarize what needs to change, and apply fixes for the selected threads.

## Rules

- Verify `gh` authentication before trying to inspect the PR.
- Summarize and number comment threads before changing code.
- Let the user choose which comments to address when multiple threads exist.
- Re-authenticate and retry if `gh` fails because of login or rate limits.

## Workflow

1. Run `gh auth status`.
2. Find the open PR for the current branch.
3. Fetch comments and review threads.
4. Summarize each thread with the likely fix scope.
5. Ask the user which numbered comments to address.
6. Apply fixes for the selected comments.

## Output expectations

- PR identified
- numbered comment list
- short action summary per thread
- applied fixes for selected items
