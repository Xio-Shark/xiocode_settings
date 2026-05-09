---
name: "gh-fix-ci"
description: "Use when GitHub Actions CI is failing and the user wants log-based triage."
---


# Gh Pr Checks Plan Fix

## Rules

- 只处理 GitHub Actions 里的失败检查，不扩展到 Buildkite 等外部提供方。
- 先拿到失败检查与日志证据，再写结论，不靠猜测。
- 对外部检查只汇报 `detailsUrl`，不要伪装成已经排查过。

## Workflow

1. Run `gh auth status`; if unauthenticated, stop and ask the user to log in.
2. Resolve the PR with `gh pr view` or the user-provided PR URL/number.
3. Use `scripts/inspect_pr_checks.py` first to list failing checks and fetch actionable GitHub Actions logs.
4. If needed, fall back to `gh pr checks`, `gh run view`, and direct job logs via `gh api`.
5. Summarize the failing check, the run URL, and the shortest useful log excerpt.
6. Draft a fix plan and implement only after explicit approval.
7. After changes, re-run the relevant checks or tell the user exactly what to rerun.

## Reference

- Primary helper: `scripts/inspect_pr_checks.py`
