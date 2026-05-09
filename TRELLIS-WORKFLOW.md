---
name: trellis-workflow
description: |
  Trellis Multi-Agent Pipeline 全局工作流规范。
  定义任务目录结构、Phase 顺序、文档模板、验收标准和协作契约。
  所有 Agent 在执行 Trellis 工作流时都必须遵循此规范。
tools: []
model: opus
---

# Trellis Multi-Agent Pipeline 工作流规范

> 本文档定义了 Multi-Agent Pipeline 的完整工作流。
> 各 Agent 的 prompt 中不再重复这些细节，而是通过阅读本文档获取上下文。

---

## 1. 任务目录结构

当前任务由 `.trellis/.current-task` 文件指定，内容为任务目录的相对路径。

```
.trellis/tasks/{MM}-{DD}-{name}/
├── task.json           # 任务配置（branch, scope, dev_type, status, next_action, current_phase）
├── prd.md              # 需求文档
├── info.md             # 技术设计（可选）
├── implement.jsonl     # Implement phase 上下文文件列表
├── check.jsonl         # Check phase 上下文文件列表
└── debug.jsonl         # Debug phase 上下文文件列表
```

### task.json 字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `branch` | string | Git 分支名，如 `feature/user-auth` |
| `scope` | string | 提交消息 scope，如 `auth`, `api`, `ui` |
| `dev_type` | string | `backend` / `frontend` / `fullstack` |
| `status` | string | `pending` / `planning` / `implementing` / `checking` / `debugging` / `review` / `rejected` |
| `next_action` | array | Phase 执行顺序，如 `["implement", "check", "finish", "create-pr"]` |
| `current_phase` | string | 当前执行到的 phase |
| `pr_url` | string | PR 链接（create-pr 后填充）|

### JSONL 上下文文件格式

每行一个 JSON 对象：
```json
{"file": "relative/path.md", "reason": "why this file is needed"}
```

---

## 2. Phase 定义与执行顺序

标准 Pipeline 顺序：

```
plan → implement → check → debug(如有) → finish → create-pr
```

| Phase | 负责 Agent | 输入 | 输出 | 最大超时 |
|-------|-----------|------|------|---------|
| **plan** | plan | 用户需求 + 代码库分析 | 完整任务目录 | 15 min |
| **implement** | implement | prd.md + info.md + implement.jsonl | 代码变更 | 30 min |
| **check** | check | git diff + check.jsonl | 修复后的代码 + 验证结果 | 15 min |
| **debug** | debug | 错误描述 + debug.jsonl | 修复后的代码 | 20 min |
| **finish** | check (带 [finish] 标记) | 全部变更 + finish-work.md | 最终检查 + spec 更新 | 15 min |
| **create-pr** | dispatch (bash) | 变更分支 | Draft PR | 5 min |

### Phase 切换规则

- Dispatch Agent 读取 `task.json` 的 `next_action` 数组，按顺序执行
- 每个 phase 完成后，Dispatch 不需要手动更新 `current_phase` — Hook 系统会自动更新
- 如果 check 发现问题，dispatch 应调用 debug agent 修复，然后重新 check
- 只有 create-pr 可以执行 `git commit`

---

## 3. 需求评估标准（Plan Phase）

Plan Agent 在动手前必须评估需求。以下情况必须 **Reject**：

| 类别 | 判断标准 |
|------|---------|
| **Unclear** | "Make it better" / "Fix the bugs" — 无具体产出定义 |
| **Incomplete** | 缺少实现所需的关键信息 |
| **Out of Scope** | 与项目目的不符，或需修改外部系统 |
| **Harmful** | 安全漏洞、破坏性操作、绕过访问控制 |
| **Too Large** | 多个无关功能捆绑，应拆分为独立 feature |

### Reject 流程

1. 更新 `task.json`：`status = "rejected"`
2. 写入 `$TASK_DIR/REJECTED.md`：
   ```markdown
   # Plan Rejected
   ## Reason: <category>
   ## Details: <specific explanation>
   ## Suggestions: <how to revise>
   ## To Retry: <commands>
   ```
3. stdout 输出 `=== PLAN REJECTED ===`，然后立即退出

---

## 4. prd.md 模板

```markdown
# Task: {TASK_NAME}

## Overview
[Brief description of what this feature does]

## Requirements
- [Requirement 1]
- [Requirement 2]

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

## Technical Notes
[Any technical considerations from research agent]

## Out of Scope
- [What this feature does NOT include]
```

**要求**：
- 需求必须具体、可验证
- 包含验收标准（Check Agent 据此验证）
- 明确 Out of Scope 防止范围蔓延

---

## 5. 上下文注入规则

### implement.jsonl

包含实现阶段需要的 spec 文件和代码参考：
```bash
python3 ./.trellis/scripts/task.py init-context "$PLAN_TASK_DIR" "$PLAN_DEV_TYPE"
# 然后由 research agent 补充相关代码模式
```

### check.jsonl

包含质量检查需要的规范文件：
- `finish-work.md` — 提交前检查清单
- `check-cross-layer.md` — 跨层验证
- `check.md` — 检查规范
- 相关 spec 文件

### debug.jsonl

包含调试需要的上下文：
- 相关 spec 文件
- 错误信息（如有）

### finish 的特殊标记

当 prompt 包含 `[finish]` 时，注入的上下文不同：
- `finish-work.md` 检查清单
- `update-spec.md` 规范更新模板
- `prd.md` 用于验证需求是否全部满足

---

## 6. Completion Markers 系统（Ralph Loop）

Check Agent 和 Finish Agent 处于 Ralph Loop 控制下。Loop 会**阻塞直到所有标记输出**。

### 标记来源

从 `check.jsonl` 中提取每个条目的 `reason` 字段，生成 `{REASON}_FINISH`：

```json
{"file": "...", "reason": "TypeCheck"}
{"file": "...", "reason": "Lint"}
{"file": "...", "reason": "CodeReview"}
```

→ 必须输出：
- `TYPECHECK_FINISH`
- `LINT_FINISH`
- `CODEREVIEW_FINISH`

### 无 check.jsonl 时

输出 `ALL_CHECKS_FINISH`

### 报告格式模板

```markdown
## Self-Check Complete

### Files Checked
- src/components/Feature.tsx

### Issues Found and Fixed
1. `<file>:<line>` - <what was fixed>

### Issues Not Fixed
(If any, with reasons)

### Verification Results
- TypeCheck: Passed TYPECHECK_FINISH
- Lint: Passed LINT_FINISH

### Summary
Checked X files, found Y issues, all fixed.
ALL_CHECKS_FINISH
```

---

## 7. Debug 报告格式

```markdown
## Fix Report

### Issues Fixed
1. `[P1]` `<file>:<line>` - <what was fixed>
2. `[P2]` `<file>:<line>` - <what was fixed>

### Issues Not Fixed
- `<file>:<line>` - <reason why not fixed>

### Verification
- TypeCheck: Pass
- Lint: Pass

### Summary
Fixed X/Y issues. Z issues require discussion.
```

### 优先级定义

| 标记 | 含义 | 处理方式 |
|------|------|---------|
| `[P1]` | Must fix（阻塞性） | 必须先修复 |
| `[P2]` | Should fix（重要） | 强烈建议修复 |
| `[P3]` | Optional（可选） |  nice to have |

---

## 8. Implement 报告格式

```markdown
## Implementation Complete

### Files Modified
- `src/components/Feature.tsx` - New component

### Implementation Summary
1. Created Feature component...

### Verification Results
- Lint: Passed
- TypeCheck: Passed
```

---

## 9. Research 报告格式

```markdown
## Search Results

### Query
{original query}

### Files Found
| File Path | Description |
|-----------|-------------|
| `src/services/xxx.ts` | Main implementation |

### Code Pattern Analysis
{Describe discovered patterns, cite specific files and line numbers}

### Related Spec Documents
- `.trellis/spec/xxx.md` - {description}

### Not Found
{If some content was not found, explain}
```

---

## 10. create-pr 动作

由 Dispatch Agent 通过 Bash 执行：

```bash
python3 ./.trellis/scripts/multi_agent/create_pr.py
```

行为：
1. Stage and commit all changes（排除 workspace）
2. Push to origin
3. Create Draft PR via `gh pr create`
4. Update `task.json`：`status = "review"`, `pr_url`, `current_phase`

**这是唯一允许 git commit 的 phase。**

---

## 11. 通用约束

### 所有 Agent 共享

- **不要手动更新 `current_phase`** — Hook 自动处理
- **只有 create-pr 可以 git commit** — 其他 phase 禁止 `git commit` / `git push` / `git merge`
- **所有子 Agent 使用高质量模型** — 复杂任务用 opus
- **Dispatch 保持简单** — 复杂逻辑属于子 Agent

### 精度原则

- Precise fixes for reported issues
- Follow specs
- Verify each fix
- Don't refactor surrounding code
- Don't add new features
- Don't modify unrelated files
