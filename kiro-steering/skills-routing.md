---
inclusion: always
---

# Skills Auto-Trigger Rules

Skills 是胶水层的一级公民。每个任务开始前：扫描 → 加载 SKILL.md → 声明 → 遵循 → 组合。若无需 skill，声明「No matching skill, proceeding with native tools」。

## 高频路由表

| Scenario | Skill | Trigger Keywords |
|----------|-------|-----------------|
| Multi-step task tracking | `taskmaster` | "track tasks", "long task", "big project", "从零开始" |
| PDF | `pdf` | "PDF", "pdf", "poppler", "reportlab" |
| Web deployment | `vercel-deploy` / `netlify-deploy` / `cloudflare-deploy` | "deploy", "vercel", "netlify", "cloudflare" |
| Database / API | `database-design` / `api-patterns` | "database", "schema", "API design" |
| Frontend | `tailwind-patterns` / `nextjs-react-expert` / `frontend-design` | "tailwind", "React", "Next.js", "UI design" |
| Backend | `nodejs-best-practices` / `python-patterns` / `rust-pro` | "Node.js", "Python", "Rust" |
| Testing / Lint / Debug | `testing-patterns` / `lint-and-validate` / `systematic-debugging` | "test", "lint", "debug" |
| Code review / Simplify | `caveman-review` / `simplify` | "review", "simplify", "重构" |
| Architecture / Plan | `architecture` / `plan-writing` | "architecture", "plan", "系统设计" |
| 改代码 / 重构 / 修 bug | 读 `AGENTS.gitnexus.md` | "改", "重构", "rename", "修 bug", "impact" |
| 创建执行清单 | `todo-list-csv` + 读 `AGENTS.md` §List 文档自动执行协议 | "创建list文档", "做个list", "建个执行清单" |

> **兜底规则**：名称语义匹配度 > 70% 时必须读取 SKILL.md 确认。

## 完整路由表

完整版见 `~/.claude/skills/.system/SKILLS-REFERENCE.md`。
