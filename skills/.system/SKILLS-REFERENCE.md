---
name: skills-reference
description: Complete skill routing table for Claude Code. Auto-trigger reference.
type: reference
---

# Skills Auto-Trigger Reference

> This is the full routing table extracted from CLAUDE.md. The abbreviated version in CLAUDE.md covers the top 10 most frequent scenarios.
> If a scenario is not in the abbreviated table, check here.

## How to Use

1. Scan user input against the "Trigger Keywords" column
2. If match > 70% semantic similarity, read the skill's `SKILL.md`
3. Declare in thinking: "Loading skill: {name}"
4. Follow the skill's instructions exactly

## Full Routing Table

| Scenario | Skill | Trigger Keywords / Patterns |
|----------|-------|----------------------------|
| Multi-step task tracking / autonomous execution | `taskmaster` | "track tasks", "make a plan", "track progress", "long task", "big project", "autonomous", "从零开始", "长时任务", "任务管理", "做个计划" |
| PDF creation / editing / analysis | `pdf` | "PDF", "pdf", "poppler", "reportlab", "pdfplumber" |
| Web deployment - Vercel | `vercel-deploy` | "deploy to vercel", "vercel", "部署到vercel" |
| Web deployment - Netlify | `netlify-deploy` | "deploy to netlify", "netlify" |
| Web deployment - Cloudflare | `cloudflare-deploy` | "cloudflare", "workers", "pages" |
| Database design / ORM / migration | `database-design` | "database", "schema", "ORM", "migration", "索引", "数据库设计" |
| API design | `api-patterns` | "API design", "REST", "GraphQL", "接口设计" |
| Frontend with Tailwind | `tailwind-patterns` | "tailwind", "Tailwind CSS", "v4" |
| React / Next.js optimization | `nextjs-react-expert` | "React", "Next.js", "组件优化", "性能优化", "Vercel" |
| Frontend design / UI | `frontend-design` | "frontend design", "web interface", "UI design", "component design" |
| React composition patterns | `vercel-composition-patterns` | "compound component", "render props", "composition pattern" |
| Node.js backend | `nodejs-best-practices` | "Node.js", "Express", "NestJS", "async", "event loop" |
| Python patterns | `python-patterns` | "Python", "Flask", "Django", "FastAPI", "pattern" |
| Rust | `rust-pro` | "Rust", "Cargo", "tokio", "lifetime", "borrow" |
| Testing strategy | `testing-patterns` | "test strategy", "unit test", "integration test", "E2E", "测试策略" |
| TDD workflow | `tdd-workflow` | "TDD", "test driven", "red-green-refactor" |
| Lint / format / validate | `lint-and-validate` | "lint", "format", "check", "validate", "types", "static analysis" |
| Debug / systematic debugging | `systematic-debugging` | "debug", "排查", "定位问题", "hang", "deadlock", "系统调试" |
| Deep bug analysis / post-fix | `break-loop` | "root cause", "bug analysis", "prevent bug", "深度分析" |
| Code validation against spec | `check` | "check code", "validate against spec", "guideline check" |
| Cross-layer verification | `check-cross-layer` | "cross-layer", "跨层检查", "data flow check" |
| Pre-commit checklist | `finish-work` | "finish work", "pre-commit", "提交前检查" |
| Unit test improvement | `improve-ut` | "improve test", "test coverage", "增加测试" |
| Screenshot | `screenshot` | "screenshot", "截图", "屏幕截图", "desktop capture" |
| Jupyter notebook | `jupyter-notebook` | "jupyter", "ipynb", "notebook", ".ipynb" |
| GitHub PR review comments | `gh-address-comments` | "review comment", "PR comment", "address comment" |
| GitHub CI fix | `gh-fix-ci` | "CI failing", "GitHub Actions", "workflow failed", "fix CI" |
| Content research & writing | `content-research-writer` | "write article", "content", "博客", "写作", "citation" |
| Playwright automation | `playwright` | "playwright", "browser automation", "e2e test", "screenshot test" |
| Prompt optimization | `prompt-optimizer` | "optimize prompt", "优化提示词", "EARS", "requirement" |
| Plan writing | `plan-writing` | "write a plan", "制定计划", "规划", "implementation plan" |
| Architecture decision | `architecture` | "architecture", "系统设计", "技术选型", "tradeoff" |
| Code review (compressed) | `caveman-review` | "code review", "review code", "代码审查", "review PR" |
| Code simplify | `simplify` | "clean up", "simplify", "重构", "简化", "简化代码" |
| Requirements brainstorm | `brainstorm` | "brainstorm", "头脑风暴", "讨论", "想法", "需求不明确" |
| Stress-test a plan | `grill-me` | "grill me", "拷问", "压力测试", "poke holes", "devil's advocate" |
| Changelog generation | `changelog-generator` | "changelog", "release notes", "更新日志", "版本记录" |
| MCP server building | `mcp-builder` | "MCP", "Model Context Protocol", "MCP server", "tool design" |
| Claude API / Anthropic SDK | `claude-api` | "claude api", "anthropic sdk", "prompt caching", "@anthropic-ai/sdk" |
| Nature/CNS citations | `nature-citation` | "Nature引用", "CNS", "分段引用", "自动给出引用", "找引用" |
| Todo list CSV tracking | `todo-list-csv` | "todo", "CSV 任务", "任务列表", "TODO list" |
| Find / discover skills | `find-skills` | "find skill", "how to do", "有没有 skill", "discover skill" |
| Create new skill | `skill-creator` / `create-command` | "create skill", "新建 skill", "写 skill" |
| Integrate skill to spec | `integrate-skill` | "integrate skill", "集成 skill", "规范" |
| Update code-spec | `update-spec` | "update spec", "更新规范", "capture contract" |
| Record session progress | `record-session` | "record session", "记录进度", "journal" |
| Onboard new developer | `onboard` | "onboard", "入职", "workflow guide" |
| Start session / load context | `start` | "start session", "开始会话", "加载上下文" |
| Before dev / read guidelines | `before-dev` | "before dev", "开发前", "read guidelines" |
| Multi-agent parallel | `parallel` | "parallel", "并行开发", "multi-agent" |
| PRD management | `prd-manager` | "PRD", "需求文档", "prd version" |
| Code agent insights | `code-agent-insights-workflow` | "code agent insights", "session search" |
| GitNexus code intelligence | `gitnexus` | "gitnexus", "code graph", "impact analysis", "blast radius" |
| Caveman mode (compressed) | `caveman` | "caveman mode", "talk like caveman", "省 token" |
| Caveman commit | `caveman-commit` | "commit message", "generate commit", "/commit" |
| Caveman compress memory | `caveman-compress` | "compress memory", "压缩记忆文件" |
| Caveman help | `caveman-help` | "caveman help", "caveman commands" |
