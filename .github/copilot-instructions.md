# Copilot Instructions — Career 工作区

> 此文件是 GitHub Copilot CLI 在本仓库的项目级指令。
> 详细子规则见项目根 `AGENTS.md` 及其引用的 `AGENTS.*.md` 子文件。

## Language

Default to Chinese in user-facing replies unless the user explicitly requests another language.

## Glue Coding Philosophy

- **能不写就不写**：优先复用 skill、plugin、子 agent、第三方库
- **能连不造**：禁止在胶水层重新实现依赖库功能
- **不修改第三方代码**：以不可变黑盒使用
- **自定义代码仅限胶水层**：组合、调用、封装、适配

## Karpathy 原则

1. **编码前思考**：不确定就询问，不猜测
2. **简洁优先**：最小代码解决问题
3. **精准修改**：只碰必须碰的，匹配现有风格
4. **目标驱动**：转换为可验证目标

## Code Metrics

- Function: 50 lines max
- File: 300 lines max
- Nesting: 3 levels max
- Parameters: 3 positional max
- No magic numbers

## Debug-First

- 禁止 mock/simulation 假成功路径
- 禁止防御性代码掩盖真实错误
- 让失败清楚暴露，在源头修复

## Security

- 绝不硬编码 secret / API key
- 参数化 SQL，不拼接用户输入
- 所有外部输入在系统边界处校验

## RTK

所有 shell 命令加 `rtk` 前缀（token 优化，60-90% 节省）。

## Trellis Session Start

进入仓库时按顺序执行：

```bash
# 1) 加载上下文
python3 ./.trellis/scripts/get_context.py

# 2) 校验 knowledge_mcp
/Users/xioshark/Desktop/career/projects/rag/.venv/bin/python -m services.knowledge_mcp.cli doctor
```

## Trellis Auto-Task Rules

| 用户意图 | 动作 |
|---------|------|
| "我要做 xxx" / "start xxx" | `task.py create` → `task.py start` |
| "做完了" / "done" | `task.py finish` → `task.py archive` |
| "放弃" / "cancel" | `task.py archive <current>` |
| "查看任务" | `task.py list` |
| "上下文" / "status" | `get_context.py` |

详见 `AGENTS.trellis.md`。

## Sub-Rules

详见项目根 `AGENTS.md`，按场景加载：
- 查背景 → `AGENTS.knowledge-mcp.md`
- 改代码 → `AGENTS.gitnexus.md`
- Shell 操作 → `AGENTS.shell-safety.md`
- 任务管理 → `AGENTS.trellis.md`
- 命令优化 → `AGENTS.rtk.md`

## List 文档自动执行协议

触发关键词："创建list文档"、"做个list"、"建个执行清单"

自动创建 `{任务名} 规划.md` + `{任务名} TO DO list.csv`（含 `group` 列），拆为 3 组解耦任务，完成即删。

详见 `AGENTS.md` §List 文档自动执行协议。
