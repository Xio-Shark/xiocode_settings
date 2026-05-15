---
scope: task-lifecycle
priority: P1
applies_when: ["我要做", "做完了", "done", "切换到", "task", "任务", "session start"]
must_run_at_session_start: ["python3 ./.trellis/scripts/get_context.py"]
requires_dir: .trellis/
---

# AGENTS.trellis.md — Trellis 工作流补充规则

> 通用 Trellis 规则（上下文加载、Auto-Task 基础规则表）见全局 `~/.claude/CLAUDE.md` §Trellis Auto-Detection。
> 本文件为项目特有的详细协议。

## 任务管理命令

```bash
python3 ./.trellis/scripts/task.py list                                    # 列出活跃任务
python3 ./.trellis/scripts/task.py create "<title>" --slug <task-name>     # 创建
python3 ./.trellis/scripts/task.py start <task-name>                       # 开始
python3 ./.trellis/scripts/task.py finish                                  # 完成
python3 ./.trellis/scripts/task.py archive <task-name>                     # 归档
```

**当前任务**记录在 `.trellis/.current-task`。

## Session Recording

代码提交并测试后，记录会话：

```bash
python3 ./.trellis/scripts/add_session.py \
  --title "Session Title" --commit "<hash>" --summary "Brief summary"
```

自动追加到 `journal-N.md`（2000 行自动轮转）。

## 可用 Agent

| Agent | Purpose | Trigger |
|-------|---------|---------|
| `implement` | Code implementation | `/agent implement` |
| `check` | Code quality checks | `/agent check` |
| `debug` | Bug fixing | `/agent debug` |
| `research` | Technical research | `/agent research` |

## Slash Commands

| Command | When to use |
|---------|-------------|
| `/trellis:finish-work` | Pre-commit checklist |
| `/trellis:break-loop` | Post-debug analysis |
| `/trellis:check-cross-layer` | Cross-layer verification |

## 工作流原则

1. **Read before write** — 先获取上下文和 spec
2. **One task at a time** — 不同时开发多个无关任务
3. **Follow standards** — 遵守 `.trellis/spec/` 规范
4. **Record promptly** — 每次会话后更新 journal
5. **Commit 策略** — 遵循 CLAUDE.md §AI Agent 自主执行协议 §commit 策略（默认禁止 AI commit，除非项目明确允许）

---

## Auto-Task 详细协议

> 全局 CLAUDE.md 有基础 5 条意图规则，以下为完整执行协议。

### 意图检测表

| 用户意图 | 自动执行 | 条件 |
|---------|---------|------|
| "我要做 xxx" / "开始 xxx" / "给我做 xxx" | `task.py create` → `task.py start` | 无活跃任务时 |
| "做完了" / "done" / "搞定了" | `task.py finish` → `task.py archive` | 有活跃任务时 |
| "这个不要了" / "放弃" / "cancel" | `task.py archive <current>` | 有活跃任务时 |
| "查看任务" / "有什么任务" | `task.py list` | 始终 |
| "切换到 xxx" / "继续 xxx" | `task.py start <slug>` | 任务存在时 |
| "给我上下文" / "当前状态" | `get_context.py` | 始终 |

### Auto-Slug 生成规则

- 小写 kebab-case，去除标点，最长 30 字符
- 示例："优化面试准备流程" → `optimize-interview-prep`

### 安全规则

- 有活跃任务时不自动创建新任务（先询问是否完成当前）
- 无活跃任务时不自动完成（正常响应）
- 始终显示执行的命令
- 命令失败时报告错误，不静默吞掉
