# Agent Definitions

> This file is an index. Each agent has its own definition file in `~/.claude/agents/`.
> Loaded automatically by Claude Code when spawning sub-agents.

| Agent | File | Role | Tools |
|-------|------|------|-------|
| **plan** | `agents/plan.md` | Pipeline 规划师。评估需求、生成任务目录。 | Read, Bash, Glob, Grep, Task |
| **implement** | `agents/implement.md` | 代码实现专家。阅读 spec 后编写代码。 | Read, Write, Edit, Bash, Glob, Grep |
| **check** | `agents/check.md` | 代码质量检查。对比 spec 审查 diff，发现问题直接修复。 | Read, Write, Edit, Bash, Glob, Grep |
| **debug** | `agents/debug.md` | Bug 修复专家。精准定位、按 spec 修复。 | Read, Write, Edit, Bash, Glob, Grep |
| **dispatch** | `agents/dispatch.md` | Pipeline 主调度员。按 Phase 顺序调用子 Agent。 | Read, Bash |
| **research** | `agents/research.md` | 调研专家。纯调研不修改代码。 | Read, Glob, Grep, Skill |

## Universal Agent Rules

All agents in the Trellis Pipeline share these constraints:

- **Only create-pr phase can git commit** — Other phases must NOT `git commit` / `git push` / `git merge`
- **Do NOT manually update `current_phase`** — Hooks handle this automatically
- **All sub-agents use high-quality model** — Complex tasks use `opus`
- **Dispatch stays simple** — Complex logic belongs in sub-agents
- **Precision principle** — Precise fixes, follow specs, verify each fix, don't refactor unrelated code

## Phase Sequence

```
plan → implement → check → debug(if needed) → finish → create-pr
```

For full workflow specification, see `~/.claude/TRELLIS-WORKFLOW.md`.
