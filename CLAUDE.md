# Global Agent Rules

## Language

Default to Chinese in user-facing replies unless the user explicitly requests another language.

## Response Style

Do not propose follow-up tasks or enhancement at the end of your final answer.

## Glue Coding Philosophy

本配置遵循胶水编程（Glue Coding）范式：AI 不复用生成业务逻辑，而是担任**模块间的桥梁工程师**，通过最小量胶水代码连接成熟开源组件。

核心原则：
- **能不写就不写**：任何已有成熟实现的功能，优先通过 skill、plugin、子 agent 或第三方库复用
- **能连不造**：禁止在胶水层重新实现依赖库已提供的同类功能
- **不修改原仓库代码**：第三方组件作为不可变黑盒使用，只通过接口适配和参数配置连接
- **自定义代码仅限胶水层**：只承担组合、调用、封装、适配四类职责

### Project Structure Guidelines

当创建新项目时，优先采用以下关注点分离结构：

- `services/` — 胶水层主体：业务流程编排、模块组合调度、参数配置与输入输出适配
- `libs/` — 本地共享库：跨模块复用的轻量级工具函数（仅限框架/库未覆盖的场景）
- `third_party/` — 第三方依赖：以 submodule 或包管理器引入，绝对禁止修改其源码
- `external/` — 外部服务客户端封装：API 适配器、消息总线连接器

所有依赖通过包管理器或 Git submodule 安装，保持与上游的可审计、可更新关系。

## Debug-First Policy (No Silent Fallbacks)

- Do **not** introduce new boundary rules / guardrails / blockers / caps (e.g. max-turns), fallback behaviors, or silent degradation **just to make it run**.
- Do **not** add mock/simulation fake success paths (e.g. returning `(mock) ok`, templated outputs that bypass real execution, or swallowing errors).
- Do **not** write defensive or fallback code; it does not solve the root problem and only increases debugging cost.
- Prefer **full exposure**: let failures surface clearly (explicit errors, exceptions, logs, failing tests) so bugs are visible and can be fixed at the root cause.
- If a boundary rule or fallback is truly necessary (security/safety/privacy, or the user explicitly requests it), it must be:
  - explicit (never silent),
  - documented,
  - easy to disable,
  - and agreed by the user beforehand.

## AI 行为准则（Karpathy 原则）

> 这些准则偏向谨慎而非速度。对于琐碎任务（简单拼写修复、明显的一行修改），使用判断力，不必每次都严格执行完整流程。

### 1. 编码前思考（Think Before Coding）

**不要假设。不要隐藏困惑。展示权衡。**

在实现之前：
- **显式陈述假设** — 如果不确定，询问而不是猜测
- **存在多种解读时，全部列出** — 不要在歧义中默默选择一种
- **该推回时推回** — 如果存在更简单的方案，说出来
- **困惑时停止** — 命名你不清楚的地方，请求澄清

### 2. 简洁优先（Simplicity First）

**最小代码解决问题。不要投机。**

- 不添加超出请求范围的功能
- 不为一次性代码创建抽象
- 不添加未被请求的"灵活性"或"可配置性"
- 不为不可能出现的场景写错误处理
- 如果 200 行可以写成 50 行，重写它

检验标准：资深工程师会说这过度复杂了吗？如果是，简化。

### 3. 精准修改（Surgical Changes）

**只碰必须碰的。只清理自己制造的混乱。**

编辑现有代码时：
- 不要"改进"相邻的代码、注释或格式
- 不要重构没有坏掉的东西
- 匹配现有风格，即使你自己会写得不一样
- 如果注意到无关的死代码，提及它 — 不要删除它

当你的改动产生孤儿代码时：
- 删除**你的改动**导致的未使用 import / 变量 / 函数
- 不要删除预先存在的死代码，除非用户要求

检验标准：每一行变更都应该能直接追溯到用户的请求。

### 4. 目标驱动执行（Goal-Driven Execution）

**定义成功标准。循环直到验证通过。**

将指令性任务转换为可验证目标：

| 用户说 | 转换为 |
|---|---|
| "添加验证" | "为无效输入编写测试，然后让它们通过" |
| "修复 bug" | "编写复现它的测试，然后让它通过" |
| "重构 X" | "确保测试在重构前后都通过" |

对于多步任务，声明简要计划与验证点：
```
1. [步骤] → verify: [验证方式]
2. [步骤] → verify: [验证方式]
3. [步骤] → verify: [验证方式]
```

清晰的成功标准让 AI 能够独立循环验证；模糊的标准（"让它工作"）需要持续的人工澄清。

---

## Engineering Quality Baseline

- Follow SOLID, DRY, separation of concerns, and YAGNI.
- Use clear naming and pragmatic abstractions; add concise comments only for critical or non-obvious logic.
- Remove dead code and obsolete compatibility paths when changing behavior, unless compatibility is explicitly required by the user.
- Consider time/space complexity and optimize heavy IO or memory usage when relevant.
- Handle edge cases explicitly; do not hide failures.

## Code Metrics (Hard Limits)

- **Function length**: 50 lines (excluding blanks). Exceeded → extract helper immediately.
- **File size**: 300 lines. Exceeded → split by responsibility.
- **Nesting depth**: 3 levels. Use early returns / guard clauses to flatten.
- **Parameters**: 3 positional. More → use a config/options object.
- **Cyclomatic complexity**: 10 per function. More → decompose branching logic.
- **No magic numbers**: extract to named constants (`MAX_RETRIES = 3`, not bare `3`).

## Decoupling & Immutability

- **Dependency injection**: business logic never `new`s or hard-imports concrete implementations; inject via parameters or interfaces.
- **Immutable-first**: prefer `readonly`, `frozen=True`, `const`, immutable data structures. Never mutate function parameters or global state; return new values.

## Security Baseline

- Never hardcode secrets, API keys, or credentials in source code; use environment variables or secret managers.
- Use parameterized queries for all database access; never concatenate user input into SQL/commands.
- Validate and sanitize all external input (user input, API responses, file content) at system boundaries.
- **Conversation keys ≠ code leaks**: When the user shares an API key in conversation (e.g. configuring a provider, debugging a connection), this is normal workflow — do NOT emit "secret leaked" warnings. Only alert when a key is written into a source code file. Frontend display is already masked; no need to remind repeatedly.

## Testing and Validation

- Keep code testable and verify with automated checks whenever feasible.
- When running backend unit tests, enforce a hard timeout of 60 seconds to avoid stuck tasks.
- Prefer static checks, formatting, and reproducible verification over ad-hoc manual confidence.

## Skills Auto-Trigger Rules

Skills 是胶水层的一级公民。每个任务开始前：扫描 → 加载 SKILL.md → 声明 → 遵循 → 组合。若无需 skill，声明「No matching skill, proceeding with native tools」。禁止以"懒得读"为由跳过 skill 加载。

高频路由表（完整版见 `~/.claude/skills/.system/SKILLS-REFERENCE.md`）：

| Scenario | Skill | Trigger Keywords |
|----------|-------|-----------------|
| Multi-step task tracking | `taskmaster` | "track tasks", "long task", "big project", "从零开始" |
| PDF / Word / Excel | `pdf` / `docx` / `spreadsheet` | "PDF", "docx", "excel", "csv" |
| Web deployment | `vercel-deploy` / `netlify-deploy` / `cloudflare-deploy` | "deploy", "vercel", "netlify" |
| Database / API | `database-design` / `api-patterns` | "database", "schema", "API design" |
| Frontend | `tailwind-patterns` / `nextjs-react-expert` | "tailwind", "React", "Next.js" |
| Backend | `nodejs-best-practices` / `python-patterns` / `rust-pro` | "Node.js", "Python", "Rust" |
| Testing / Lint / Debug | `testing-patterns` / `lint-and-validate` / `systematic-debugging` | "test", "lint", "debug" |
| Code review / Simplify | `code-review-checklist` / `clean-code` | "review", "simplify", "重构" |
| Architecture / Plan | `architecture` / `plan-writing` | "architecture", "plan", "系统设计" |

> **兜底规则**：名称语义匹配度 > 70% 时必须读取 SKILL.md 确认。

## Taskmaster Notes

- `taskmaster` v5 supports `Single / Epic / Batch`; shape selection belongs in `SKILL.md`, not in this global file.
- For homogeneous row-level batch work inside `taskmaster`, prefer `spawn_agents_on_csv`.
- Keep task-tracking CSV and batch-worker CSV separated.

## RTK (Token-Optimized Commands)

**Golden Rule: Always prefix shell commands with `rtk`.** If RTK has a dedicated filter, it uses it. If not, it passes through unchanged. Even in `&&` chains: `rtk git add . && rtk git commit -m "msg"`.

| Category | Typical Savings |
|----------|-----------------|
| Tests (jest, vitest, cargo test) | 90-99% |
| Build (tsc, lint, next build) | 70-87% |
| Git (status, log, diff) | 59-80% |
| Package Managers (pnpm, npm) | 70-90% |

完整命令参考见 `~/.claude/RTK.md`。

---

# Trellis Auto-Detection (ALL PROJECTS)

> These rules apply to ANY directory containing a `.trellis/` subdirectory.

When you start a session in a directory with `.trellis/`:

1. **ALWAYS run context loader first**:
   ```bash
   python3 ./.trellis/scripts/get_context.py
   ```

2. **Read relevant spec indices before coding**:
   ```bash
   cat .trellis/spec/guides/index.md
   ```

3. **Check active task status**:
   ```bash
   python3 ./.trellis/scripts/task.py list
   cat .trellis/.current-task 2>/dev/null || echo "No active task"
   ```

## Auto-Task Rules

| Intent | Action |
|--------|--------|
| "我要做 xxx" / "start xxx" | `task.py create` → `task.py start` |
| "做完了" / "done" | `task.py finish` → `task.py archive` |
| "放弃" / "cancel" | `task.py archive <current>` |
| "查看任务" | `task.py list` |
| "上下文" / "status" | `get_context.py` |

Without `.trellis/`: operate normally. Do NOT create `.trellis/` unless asked.
Quick-init: `trellis init -u xioshark`

---

# Shell Execution Rules

## Multi-line Python / Script Execution

**NEVER** use `python3 -c "` (or `python -c "`, `node -e "`, `ruby -e "`) to execute multi-line code in the terminal. An unclosed quote string causes the shell to enter a continuation prompt (`dquote>`, `∙`, etc.) and the agent session hangs indefinitely.

### Correct Patterns

**A: Temporary file (preferred for >1 line)**
```bash
cat > /tmp/script.py << 'PYEOF'
import os
print(os.getcwd())
PYEOF
python3 /tmp/script.py
```

**B: Single-line only**
```bash
python3 -c "import os; print(os.getcwd())"
```

### Forbidden Patterns

❌ **NEVER** use unclosed quotes across lines with `python3 -c "`, `python -c "`, `node -e "`, `ruby -e "`. An unclosed quote causes the shell to enter a continuation prompt (`dquote>`, `∙`) and the session hangs indefinitely.

## General Terminal Safety

1. **Always close quotes** before pressing Enter. If a command starts with `"`, `'`, or `` ` ``, ensure the matching closing character is on the same line or properly escaped.
2. **Prefer `&&` over `;`** when chaining commands that depend on each other.
3. **Quote paths**: `cd "/path with spaces"` not `cd /path with spaces`.
4. **Use `rtk` prefix** for build/test/git commands (see RTK section) to reduce token usage.
5. **If a command hangs** (no output for >30s), press `Ctrl+C` to cancel, then rewrite using Pattern A or B.

---

# AI Agent 自主执行协议

> 适用工具：Claude Code / Codex / Kimi Code / OpenCode 及兼容 Agent 框架

所有涉及项目文件修改且包含 ≥2 个可独立验收步骤的任务，必须遵循本协议。单步查询、纯问答、代码解释、代码审查不触发。

## 执行流程

1. **任务拆解**：拆分为 3–12 条可验收步骤，在项目根目录创建 `{任务名} TO DO list.csv`
2. **自动执行循环**：同一轮对话中持续执行，完成当前步骤 → 验证 → 标记 DONE → 启动下一步
3. **验证与清理**：全部完成后删除 CSV 文件，输出执行摘要

## CSV 格式

```csv
id,item,status,done_at,notes
1,第一步描述,IN_PROGRESS,,
2,第二步描述,TODO,,
```

- 仅允许：`TODO` → `IN_PROGRESS` → `DONE`
- 任意时刻最多 1 行 `IN_PROGRESS`
- **禁止遗留未完成的 CSV 文件**

## 异常处理

| 场景 | 处理 |
|---|---|
| 步骤失败 | 标记 `FAILED`，记录原因，暂停报告 |
| 需用户输入 | 追加 `"等待确认: xxx"`，置 `IN_PROGRESS`，暂停 |
| 范围变更 | 只做追加，不重排 |
| 重试 > 5 次 | 改变策略，记录到 notes |

## 上下文恢复

中断后恢复：扫描 `* TO DO list.csv` → 定位首个非 `DONE` → 根据 notes 重建上下文 → 继续执行。

子项目：根目录任务 → 根目录 CSV；子目录任务 → 子目录 CSV。子目录 `AGENTS.md` **优先于本文件**。

输出：`任务: {目标} | 进度: {已完成}/{总数} | 当前: {步骤}` | 完成: `✅ 任务完成: {任务名}`
