---
inclusion: always
---

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

- `services/` — 胶水层主体
- `libs/` — 本地共享库
- `third_party/` — 第三方依赖，绝对禁止修改其源码
- `external/` — 外部服务客户端封装

## Debug-First Policy (No Silent Fallbacks)

- Do **not** add mock/simulation fake success paths.
- Do **not** write defensive or fallback code.
- Prefer **full exposure**: let failures surface clearly so bugs can be fixed at the root cause.

## AI 行为准则（Karpathy 原则）

### 1. 编码前思考
- **显式陈述假设** — 不确定就询问
- **存在多种解读时，全部列出**
- **困惑时停止**

### 2. 简洁优先
- 最小代码解决问题，不投机
- 不为一次性代码创建抽象

### 3. 精准修改
- 只碰必须碰的，匹配现有风格
- 删除你的改动导致的孤儿代码

### 4. 目标驱动执行
- 将指令性任务转换为可验证目标

## Code Metrics (Hard Limits)

- **Function length**: 50 lines. Exceeded → extract helper.
- **File size**: 300 lines. Exceeded → split.
- **Nesting depth**: 3 levels.
- **Parameters**: 3 positional. More → config object.
- **No magic numbers**: extract to named constants.

## Security Baseline

- Never hardcode secrets; use environment variables.
- Parameterized queries; never concatenate user input.
- Validate all external input at system boundaries.

## RTK (Token-Optimized Commands)

**Golden Rule: Always prefix shell commands with `rtk`.** Even in `&&` chains.

| Category | Savings |
|----------|---------|
| Tests | 90-99% |
| Build | 70-87% |
| Git | 59-80% |
| Package Managers | 70-90% |

完整命令参考见项目 `AGENTS.rtk.md`。
