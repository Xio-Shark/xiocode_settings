# AGENTS.md — Career 仓库 AI 规则

> 此文件是 AI 工具在本仓库工作时的**项目特有规则**。
> 通用规则（Glue Coding / Karpathy 原则 / Debug-First / Code Metrics / Security）见全局 `~/.claude/CLAUDE.md`，此处不重复。
> 详细子规则按触发场景引用，避免单文件过载。

## 阅读顺序

1. **本文件**：会话起手式 + 项目特有约定 + 子规则索引
2. **任务触发对应子规则**：
   - 查背景/做检索 → `AGENTS.knowledge-mcp.md`
   - 修改代码 / 重构 → `AGENTS.gitnexus.md`
   - 终端写文件 / Shell 操作 → `AGENTS.shell-safety.md`
   - 任务管理 / pipeline → `AGENTS.trellis.md`
   - Shell 输出优化 → `AGENTS.rtk.md`
3. **进入子目录工作时**：读对应 `<package>/AGENTS.md`，覆盖根级规则中与该包冲突的部分。

---

## 0. 会话起手式（首次进入仓库 MUST DO）

新会话第一条 tool call 必须先做以下两件事：

```bash
# 1) 加载 Trellis 上下文（developer identity / git status / 当前任务）
python3 ./.trellis/scripts/get_context.py

# 2) 校验 knowledge_mcp 是否可用（决定是否能走"检索优先"路径）
/Users/xioshark/Desktop/career/projects/rag/.venv/bin/python \
  -m services.knowledge_mcp.cli doctor
```

如果 `knowledge_mcp` doctor 报错，**必须**先告知用户"检索路径不可用，回退到 read_file"，再继续。

---

## 写代码前自查清单（操作化）

下手写代码前，按顺序自问：

- [ ] 这件事 `.claude/skills/` 是否已有？（先 `ls .claude/skills/`）
- [ ] 这件事 `platform/presets/` 是否已配置？
- [ ] 是否能用一行第三方库调用替代？（含 stdlib）
- [ ] 我打算放置代码的位置是 `services/` / `libs/` / `external/` 之一吗？
- [ ] 我写的是组合/调用/封装/适配，而非业务逻辑重新发明？

**任一项答案不确定 → 停下询问用户，不擅自动手。**

---

## 仓库目录约定（v2 结构）

```
projects/     # S + A + B + C 档项目代码（S 直接放，A→secondary，B→frozen）
portfolio/    # 对外展示站 + 技术博客
personal/     # 简历 / 投递 / JD 匹配（注意 submissions/ 与 jobs/ 含敏感信息）
platform/     # AI workflow 底座（services/libs/modules/presets/docs/scripts/tests）
private/      # reviewer 不会进的区：interview-prep/evidence/knowledge/archive/experiments/runs/task-history/ai-tools-archive/external-repos/execution-lists
.claude/      # 主用 AI 工具：Claude Code
.trellis/     # 主用 AI 工具：Trellis workflow
```

**可见性分层**：根目录 → projects/portfolio/personal/platform → private/

> 进行中的执行清单（如 `list.md`、`AgentKit Roadmap TO DO list.csv`）保留在根目录，便于持续推进；
> 真正归档的一次性清单（如 `view-2026-05-09.md`）才进 `private/execution-lists/`。

---

## 响应风格补充

- **默认中文回答**，除非用户明确要求其他语言
- 结束不要追加"要不要继续做 X"这类 follow-up suggestion
- 解释用散文，枚举用 bullet，简单问题不套大段标题

---

## 子规则索引

> **优先级**：`knowledge-mcp` > 其他子规则。所有"查/找/理解"类任务必须先走它，再决定是否继续读 `gitnexus` / `shell-safety` 等。

| 子文件 | 触发场景 | 关键约束 |
|--------|---------|---------|
| `AGENTS.knowledge-mcp.md` | 查背景、找证据、理解项目现状 | 先 `kb_map_question → kb_search`，再 read_file |
| `AGENTS.gitnexus.md` | 修改函数/类/方法、跨文件重构 | 先 `impact` 看 blast radius，再改 |
| `AGENTS.shell-safety.md` | 任何 shell 写文件、多行脚本 | 禁用 heredoc，优先 WriteFile 工具 |
| `AGENTS.trellis.md` | 任务管理、multi-agent pipeline | 任何 `.trellis/` 项目都走标准协议 |
| `AGENTS.rtk.md` | 执行 build/test/git/gh/docker 等命令 | 所有命令前加 `rtk` 节省 token |

## 任务路由判断准则（AI 自我判断 · 非自动 hook）

| 用户意图 | 读哪个子文件 | 然后做什么 |
|---------|------------|-----------|
| 查…/了解…/背景是什么/为什么这么设计 | `AGENTS.knowledge-mcp.md` | 走 `kb_map_question → kb_search` |
| 改…/重构…/修 bug/重命名 | `AGENTS.gitnexus.md` | 先 `gitnexus_impact` 评估爆炸半径 |
| 写脚本…/跑命令…/批量处理文件 | `AGENTS.shell-safety.md` + `AGENTS.rtk.md` | 禁用 heredoc + 命令加 `rtk` |
| 我要做…/做完了…/切换到… | `AGENTS.trellis.md` | 自动 task 协议（create/start/finish/archive） |
| 进入子项目工作 | `<package>/AGENTS.md` | 局部规则覆盖根级 |

---

## List 文档自动执行协议

> 触发关键词："创建list文档"、"做个list"、"建个执行清单"、"list一下"
> CSV 格式、状态机、完成即删规则见全局 `~/.claude/CLAUDE.md` §AI Agent 自主执行协议。
> 本节仅定义项目特有的**三组解耦拆分规则**。

### 触发条件

用户消息包含上述关键词时，**自动**执行以下流程，无需额外确认。

### 创建产出物

1. `{任务名} 规划.md` — 目标、分组策略、执行项总览表
2. `{任务名} TO DO list.csv` — 格式遵循 CLAUDE.md 统一标准（含 `group` 列）

### 三组解耦拆分规则（核心）

拆分时必须满足：

1. **组间零依赖**：A 组的任何 item 不依赖 B/C 组的输出，反之亦然
2. **组内可有依赖**：同一组内的 item 可以有顺序依赖
3. **每组至少 1 项**，总数 3–15 项
4. **拆分维度优先级**：
   - 按功能模块（前端 / 后端 / 基础设施）
   - 按数据流阶段（数据层 / 逻辑层 / 展示层）
   - 按关注点（核心功能 / 测试 / 文档）
5. **如果天然无法拆成 3 组**：先向用户说明，用 2 组或用户指定的分组数

### 执行顺序

选择一个组开始（默认 A → B → C），对该组内 item 逐条执行。该组清空后切换下一组。全部完成后删除 CSV 和规划.md。

### 中断恢复

扫描 `* TO DO list.csv` → 按 group 分组 → 找到首个非空行 → 读 `* 规划.md` → 恢复。
