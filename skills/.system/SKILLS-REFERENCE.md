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
| Word document creation / editing | `docx` | "word", "docx", "Word文档", "docx-js", "python-docx" |
| Spreadsheet / Excel / CSV | `spreadsheet` | "excel", "xlsx", "csv", "spreadsheet", "表格", "openpyxl", "pandas" |
| Image generation / editing | `imagegen` | "generate image", "图片生成", "DALL-E", "OpenAI Image", "画图" |
| Video download | `video-downloader` | "download youtube", "youtube video", "下载视频", "YouTube" |
| Web deployment - Vercel | `vercel-deploy` | "deploy to vercel", "vercel", "部署到vercel" |
| Web deployment - Netlify | `netlify-deploy` | "deploy to netlify", "netlify" |
| Web deployment - Cloudflare | `cloudflare-deploy` | "cloudflare", "workers", "pages" |
| Web deployment - Render | `render-deploy` | "deploy to Render", "render.yaml" |
| Database design / ORM / migration | `database-design` | "database", "schema", "ORM", "migration", "索引", "数据库设计" |
| API design | `api-patterns` | "API design", "REST", "GraphQL", "接口设计" |
| Frontend with Tailwind | `tailwind-patterns` | "tailwind", "Tailwind CSS", "v4" |
| React / Next.js optimization | `nextjs-react-expert` | "React", "Next.js", "组件优化", "性能优化", "Vercel" |
| Node.js backend | `nodejs-best-practices` | "Node.js", "Express", "NestJS", "async", "event loop" |
| Python patterns | `python-patterns` | "Python", "Flask", "Django", "FastAPI", "pattern" |
| Rust | `rust-pro` | "Rust", "Cargo", "tokio", "lifetime", "borrow" |
| Testing strategy | `testing-patterns` | "test strategy", "unit test", "integration test", "E2E", "测试策略" |
| TDD workflow | `tdd-workflow` | "TDD", "test driven", "red-green-refactor" |
| Lint / format / validate | `lint-and-validate` | "lint", "format", "check", "validate", "types", "static analysis" |
| Debug / systematic debugging | `systematic-debugging` | "debug", "排查", "定位问题", "hang", "deadlock", "系统调试" |
| Performance profiling | `performance-profiling` | "profile", "性能分析", "benchmark", "pprof", "flamegraph" |
| Screenshot | `screenshot` | "screenshot", "截图", "屏幕截图", "desktop capture" |
| Speech-to-text | `transcribe` | "transcribe", "转录", "字幕", "语音识别", "speech to text" |
| Text-to-speech | `speech` | "text to speech", "语音合成", "narration", "语音生成" |
| Jupyter notebook | `jupyter-notebook` | "jupyter", "ipynb", "notebook", ".ipynb" |
| GitHub PR review comments | `gh-address-comments` | "review comment", "PR comment", "address comment" |
| GitHub CI fix | `gh-fix-ci` | "CI failing", "GitHub Actions", "workflow failed", "fix CI" |
| Email drafting | `email-draft-polish` | "draft email", "写邮件", "email", "cold outreach" |
| Content research & writing | `content-research-writer` | "write article", "content", "博客", "写作", "citation" |
| Resume generation | `tailored-resume-generator` | "resume", "简历", "CV", "tailor resume" |
| Meeting notes | `meeting-notes-and-actions` | "meeting notes", "会议纪要", "meeting transcript", "action items" |
| SEO | `seo-fundamentals` | "SEO", "search engine", "排名", "Core Web Vitals" |
| i18n / localization | `i18n-localization` | "i18n", "localization", "翻译", "国际化", "locale", "RTL" |
| Figma to code | `figma-implement-design` | "Figma", "design to code", "Figma MCP", "1:1 visual fidelity" |
| Playwright automation | `playwright` | "playwright", "browser automation", "e2e test", "screenshot test" |
| Prompt optimization | `prompt-optimizer` | "optimize prompt", "优化提示词", "EARS", "requirement" |
| Plan writing | `plan-writing` | "write a plan", "制定计划", "规划", "implementation plan" |
| Architecture decision | `architecture` | "architecture", "系统设计", "技术选型", "tradeoff" |
| Code review | `code-review-checklist` | "code review", "review code", "代码审查", "audit code" |
| Clean code / simplify | `clean-code` / `code-simplifier` | "clean up", "simplify", "重构", "简化", "简化代码" |
| Documentation | `documentation-templates` | "documentation", "文档模板", "写文档", "doc structure" |
| Brainstorming | `brainstorming` | "brainstorm", "头脑风暴", "讨论", "想法", "Socratic" |
| Changelog generation | `changelog-generator` | "changelog", "release notes", "更新日志", "版本记录" |
| Domain name brainstorming | `domain-name-brainstormer` | "domain name", "域名", " brainstorm domain" |
| Invoice organization | `invoice-organizer` | "invoice", "receipt", "发票", "报销", "tax" |
| Lead research | `lead-research-assistant` | "lead", "prospect", "sales", "潜在客户", "BD" |
| Raffle / winner picker | `raffle-winner-picker` | "raffle", "winner", "抽奖", "随机选择", "contest" |
| Competitive ads analysis | `competitive-ads-extractor` | "competitor ads", "ad library", "竞品广告", "Facebook Ads" |
| Internal communications | `internal-comms` | "internal comm", "status report", "team update", "newsletter", "incident report" |
| Support ticket triage | `support-ticket-triage` | "support ticket", "customer support", "工单", "Zendesk" |
| Web design audit | `web-design-guidelines` | "audit web", "design audit", "UI audit", "web UI" |
| Mobile app design | `mobile-design` | "mobile app design", "app design", "移动端设计" |
| Canvas design | `canvas-design` | "canvas", "设计稿", "视觉设计", "static design" |
| Theme factory | `theme-factory` | "theme", "样式主题", "配色", "colors", "fonts" |
| Weather SVG | `weather-svg-creator` | "weather", "天气", "SVG", "weather card" |
| Game development | `game-development` | "game", "游戏开发", "game engine", "游戏架构" |
| Godot best practices | `godot-best-practices` | "Godot", "GDScript", "scene", "signal", "node" |
| Web game | `develop-web-game` | "web game", "浏览器游戏", "HTML5 game", "canvas game" |
| Pixel art | `pixel-art` | "pixel art", "像素画", "sprite", "tileset", "palette", "dithering" |
| Algorithmic art | `algorithmic-art` | "generative art", "算法艺术", "creative coding", "processing" |
| Sora video | `sora` | "Sora", "video generation", "AI video", "OpenAI video" |
| Image enhancement | `image-enhancer` | "enhance image", "improve image", "画质增强", "sharpen" |
| Office doc reader | `office-doc-reader` | "read docx", "read pdf", "read pptx", "OCR", "office document" |
| OpenAI docs | `openai-docs` | "OpenAI documentation", "OpenAI API docs", "official docs" |
| Server management | `server-management` | "server", "运维", "Linux server", "SSH", "deployment" |
| Bash / Linux | `bash-linux` | "bash script", "shell script", "Linux command", "pipe", "grep", "awk" |
| PowerShell | `powershell-windows` | "PowerShell", "Windows script", "Windows automation" |
| LLDB debug | `debug-lldb` | "lldb", "GDB", "debugger", "backtrace", "thread", "hang" |
| Continuous learning | `continuous-learning` | "continuous learning", "extract patterns", "session learning", "automated extraction" |
| Doc coauthoring | `doc-coauthoring` | "co-author", "coauthor", "协作写作", "documentation workflow" |
| Executing plans | `executing-plans` | "execute plan", "执行计划", "plan execution", "review checkpoints" |
| Create plan | `create-plan` | "create plan", "制定计划", "planning", "task plan" |
| Find skills | `find-skills` | "find skill", "how to do", "有没有 skill", "discover skill" |
| Skill installer | `skill-installer` | "install skill", "添加 skill", "curated list", "GitHub repo skill" |
| Skill creator | `skill-creator` | "create skill", "新建 skill", "写 skill", "update skill" |
| Skill share | `skill-share` | "share skill", "分享 skill", "Slack", "team skill" |
| Template skill | `template-skill` | "template skill", "skill 模板", "skill scaffold" |
| Spreadsheet formula | `spreadsheet-formula-helper` | "Excel formula", "spreadsheet formula", "公式", "pivot table", "array formula" |
| Todo list CSV | `todo-list-csv` | "todo", "CSV 任务", "任务列表", "update_plan", "TODO list" |
| Geo/GEO optimization | `geo-fundamentals` | "GEO", "generative engine optimization", "AI search", "ChatGPT search" |
| Meeting insights | `meeting-insights-analyzer` | "meeting insights", "communication analysis", "会议分析", "filler words" |
| Brand guidelines | `brand-guidelines` | "brand", "Anthropic brand", "品牌规范", "brand styling" |
| Yeet (GitHub PR) | `yeet` | "yeet", "stage commit push PR", "一键PR", "gh PR" |
| File organizer | `file-organizer` | "organize files", "整理文件", "文件分类", "cleanup", "duplicates" |
| Manus agent | `manus` | "manus", "install agent", "autonomous agent", "planning agent" |
| MCP builder | `mcp-builder` | "MCP", "Model Context Protocol", "MCP server", "tool design" |
| Code architect | `code-architect` | "code architect", "implementation blueprint", "feature architecture" |
| Code explorer | `code-explorer` | "code explorer", "deep analysis", "how feature works", "cross-cutting" |
| Frontend design | `frontend-design` | "frontend design", "web interface", "UI design", "component design" |
| Atlas (macOS ChatGPT app) | `atlas` | "Atlas", "ChatGPT Atlas", "macOS ChatGPT", "AppleScript" |
