---
inclusion: fileMatch
fileMatchPattern: [".trellis/**", "**/trellis/**"]
---

# Trellis Auto-Detection (ALL PROJECTS)

> These rules apply to ANY directory containing a `.trellis/` subdirectory, across all AI tools (Claude Code, Codex, KimiCode, OpenCode).

## Universal Trellis Protocol

When you start a session in a directory with `.trellis/`:

1. **ALWAYS run context loader first**:
   ```bash
   python3 ./.trellis/scripts/get_context.py
   ```

2. **Read project AGENTS.md** (if exists) for project-specific rules that override global rules.

3. **Check knowledge_mcp availability** (if project uses it):
   ```bash
   # 由项目 AGENTS.md 指定具体命令
   ```
   If unavailable, inform user and fall back to read_file.

4. **Read relevant spec indices before coding**:
   ```bash
   cat .trellis/spec/guides/index.md
   ```

5. **Check active task status**:
   ```bash
   python3 ./.trellis/scripts/task.py list
   cat .trellis/.current-task 2>/dev/null || echo "No active task"
   ```

## Universal Auto-Task Rules

When ANY `.trellis/` project is detected, apply these intent triggers:

| User Intent | Auto-Execute | Condition |
|------------|-------------|-----------|
| "我要做 xxx" / "start xxx" / "let's work on xxx" | `task.py create "<title>" --slug <slug>` → `task.py start <slug>` | No active task |
| "做完了" / "done" / "搞定了" | `task.py finish` → `task.py archive <slug>` | Has active task |
| "放弃" / "cancel this" | `task.py archive <current>` | Has active task |
| "查看任务" / "task list" | `task.py list` | Always |
| "上下文" / "status" / "context" | `get_context.py` | Always |

## When NO `.trellis/` Exists

Operate normally without Trellis workflow. Do NOT attempt to create `.trellis/` unless user explicitly requests it.

## Trellis Quick-Init (Only When User Asks)

If user wants to set up Trellis in a new project:
```bash
trellis init -u xioshark
```
