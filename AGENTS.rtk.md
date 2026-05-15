---
scope: token-optimization
priority: P2
applies_when: ["build", "test", "git", "gh", "docker", "pnpm", "npm", "lint", "命令", "shell-output"]
prefix_all_commands_with: rtk
typical_savings: "60-90%"
---

# AGENTS.rtk.md — RTK 命令速查表

> Golden Rule（"所有 shell 命令加 `rtk` 前缀"）见全局 `~/.claude/CLAUDE.md` §RTK。
> 本文件为按场景分类的完整命令参考。

## 按场景速查

### Build & Compile (80-90%)
```bash
rtk cargo build | rtk cargo check | rtk cargo clippy | rtk tsc | rtk lint | rtk prettier --check | rtk next build
```

### Test (60-99%)
```bash
rtk cargo test | rtk go test | rtk jest | rtk vitest | rtk playwright test | rtk pytest | rtk rake test | rtk rspec
```

### Git (59-80%)
```bash
rtk git status | rtk git log | rtk git diff | rtk git show | rtk git add | rtk git commit | rtk git push | rtk git pull | rtk git branch | rtk git fetch | rtk git stash | rtk git worktree
```

### GitHub (26-87%)
```bash
rtk gh pr view <num> | rtk gh pr checks | rtk gh run list | rtk gh issue list | rtk gh api
```

### JS/TS Tooling (70-90%)
```bash
rtk pnpm list | rtk pnpm outdated | rtk pnpm install | rtk npm run <script> | rtk npx <cmd> | rtk prisma
```

### Files & Search (60-75%)
```bash
rtk ls <path> | rtk read <file> | rtk grep <pattern> | rtk find <pattern>
```

### Analysis & Debug (70-90%)
```bash
rtk err <cmd> | rtk log <file> | rtk json <file> | rtk deps | rtk env | rtk summary <cmd> | rtk diff
```

### Infrastructure (85%)
```bash
rtk docker ps | rtk docker images | rtk docker logs <c> | rtk kubectl get | rtk kubectl logs
```

### Network (65-70%)
```bash
rtk curl <url> | rtk wget <url>
```

### Meta
```bash
rtk gain | rtk gain --history | rtk discover | rtk proxy <cmd>
```
