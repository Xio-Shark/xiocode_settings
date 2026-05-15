---
scope: knowledge-retrieval
priority: P0
applies_when: ["查", "了解", "背景", "找证据", "search", "find", "explain"]
must_run_before: [Read, Edit, Grep]
overrides: all-other-agents-md
---

# AGENTS.knowledge-mcp.md — 知识检索优先规则（最高优先级）

> 此规则优先级高于所有其他 AGENTS.* 子规则。凡涉及"查背景/找证据/理解项目现状"类任务，必须先走检索，不得直接批量 read_file。

## 任务开始前必须执行（MANDATORY）

对以下类型的任务，**在读取任何文件之前**，必须先调用 knowledge_mcp：

| 任务类型 | 例子 | 必须先调用 |
|----------|------|-----------|
| 查项目背景/现状 | "当前检索质量怎么样" | `kb_map_question → kb_search` |
| 找规则/约束 | "前后端接口怎么约定的" | `kb_get_rule_pack` |
| 理解架构决策 | "为什么这么设计" | `kb_map_question → kb_search` |
| 找项目证据 | "RAG 项目的评测方式" | `kb_search` |
| 岗位/简历类问题 | "适合投哪个方向" | `kb_map_question → kb_search` |

## 推荐调用顺序

```
1. kb_map_question(query, top_k=4)   → 找主文档集合
2. kb_search(query, top_k=3, retrieval_mode="hybrid")  → 拿证据片段
3. kb_read(source_path, heading=...)  → 仅在需要原文时
```

- 已构建 embeddings 时优先 `retrieval_mode=hybrid`，否则用 `lexical`。
- 遇到明确规则/工程约束问题，可跳过 map_question，直接 `kb_get_rule_pack`。

## 允许直接 read_file 的例外

- 已经通过 kb_search 拿到了 source_path，现在要读全文
- 任务是修改代码（不是查背景），直接对目标文件做修改
- knowledge_mcp 服务未启动且当前任务紧急

## 如何确认 knowledge_mcp 可用

```bash
# 必须在 platform/ 目录下运行（Python 模块路径限制）
cd /Users/xioshark/Desktop/career/platform
../projects/rag/.venv/bin/python -m services.knowledge_mcp.cli doctor
```

**注意**：knowledge_mcp 使用 rag 项目的虚拟环境（共享依赖），但必须在 platform 目录下运行命令。
