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

- **Function length**: 50 lines (excluding blanks). Exceeded  extract helper immediately.
- **File size**: 300 lines. Exceeded  split by responsibility.
- **Nesting depth**: 3 levels. Use early returns / guard clauses to flatten.
- **Parameters**: 3 positional. More  use a config/options object.
- **Cyclomatic complexity**: 10 per function. More  decompose branching logic.
- **No magic numbers**: extract to named constants (`MAX_RETRIES = 3`, not bare `3`).

## Decoupling & Immutability

- **Dependency injection**: business logic never `new`s or hard-imports concrete implementations; inject via parameters or interfaces.
- **Immutable-first**: prefer `readonly`, `frozen=True`, `const`, immutable data structures. Never mutate function parameters or global state; return new values.

## Security Baseline

- Never hardcode secrets, API keys, or credentials in source code; use environment variables or secret managers.
- Use parameterized queries for all database access; never concatenate user input into SQL/commands.
- Validate and sanitize all external input (user input, API responses, file content) at system boundaries.
- **Conversation keys  code leaks**: When the user shares an API key in conversation (e.g. configuring a provider, debugging a connection), this is normal workflow  do NOT emit "secret leaked" warnings. Only alert when a key is written into a source code file. Frontend display is already masked; no need to remind repeatedly.

## Testing and Validation

- Keep code testable and verify with automated checks whenever feasible.
- When running backend unit tests, enforce a hard timeout of 60 seconds to avoid stuck tasks.
- Prefer static checks, formatting, and reproducible verification over ad-hoc manual confidence.

## Skills Auto-Trigger Rules

Skills 是胶水层的一级公民：每个 skill 本质上是对特定领域成熟组件的胶水封装。

### 强制触发流程（每个任务开始前必须执行）

1. **扫描**：基于用户输入内容，对照下方路由表判断是否有匹配的 skill
2. **加载**：若有匹配，**立即**用 ReadFile 读取对应 SKILL.md，不得跳过；若路由表未直接命中，但可用 skills 列表中有名称/描述高度相关的 skill，同样必须读取确认
3. **声明**：在 thinking/reasoning 中显式声明：「Loading skill: {name}」以及加载原因
4. **遵循**：严格按 SKILL.md 的指令执行，禁止在 skill 已覆盖的领域重新手写等价逻辑
5. **组合**：若多个 skill 可组合完成目标，优先编排调用，而非自建实现

### 未匹配场景

- 若明确判断无需 skill，须在 thinking 中声明「No matching skill for this request, proceeding with native tools」
- 新增 skill 前，先检查现有 skill 是否可通过参数扩展满足需求
- 禁止以"懒得读""怕超上下文"等理由跳过 skill 加载

### 扩展路由表（高频场景）

| Scenario | Skill | Trigger Keywords / Patterns |
|----------|-------|----------------------------|
| Multi-step task tracking / autonomous execution | `taskmaster` | 3+ ordered steps that produce file changes; "track tasks", "make a plan", "track progress", "long task", "big project", "autonomous", "从零开始", "长时任务", "任务管理", "做个计划" |
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

> **兜底规则**：若路由表未覆盖，但用户请求明显属于某一技术/业务领域，基于 skill 名称和描述自行判断；名称语义匹配度 > 70% 时必须读取 SKILL.md 确认。

## Taskmaster Notes

- `taskmaster` v5 supports `Single / Epic / Batch`; shape selection belongs in `SKILL.md`, not in this global file.
- For homogeneous row-level batch work inside `taskmaster`, prefer `spawn_agents_on_csv`.
- Keep task-tracking CSV and batch-worker CSV separated.

<!-- rtk-instructions v2 -->
# RTK (Rust Token Killer) — Token-Optimized Commands

## Golden Rule

**Always prefix shell commands with `rtk`**. If RTK has a dedicated filter, it uses it. If not, it passes through unchanged. This means RTK is always safe to use.

**Important**: Even in command chains with `&&`, use `rtk`:
```bash
# ❌ Wrong
git add . && git commit -m "msg" && git push

# ✅ Correct
rtk git add . && rtk git commit -m "msg" && rtk git push
```

## RTK Commands by Workflow

### Build & Compile (80-90% savings)
```bash
rtk cargo build         # Cargo build output
rtk cargo check         # Cargo check output
rtk cargo clippy        # Clippy warnings grouped by file (80%)
rtk tsc                 # TypeScript errors grouped by file/code (83%)
rtk lint                # ESLint/Biome violations grouped (84%)
rtk prettier --check    # Files needing format only (70%)
rtk next build          # Next.js build with route metrics (87%)
```

### Test (60-99% savings)
```bash
rtk cargo test          # Cargo test failures only (90%)
rtk go test             # Go test failures only (90%)
rtk jest                # Jest failures only (99.5%)
rtk vitest              # Vitest failures only (99.5%)
rtk playwright test     # Playwright failures only (94%)
rtk pytest              # Python test failures only (90%)
rtk rake test           # Ruby test failures only (90%)
rtk rspec               # RSpec test failures only (60%)
rtk test <cmd>          # Generic test wrapper - failures only
```

### Git (59-80% savings)
```bash
rtk git status          # Compact status
rtk git log             # Compact log (works with all git flags)
rtk git diff            # Compact diff (80%)
rtk git show            # Compact show (80%)
rtk git add             # Ultra-compact confirmations (59%)
rtk git commit          # Ultra-compact confirmations (59%)
rtk git push            # Ultra-compact confirmations
rtk git pull            # Ultra-compact confirmations
rtk git branch          # Compact branch list
rtk git fetch           # Compact fetch
rtk git stash           # Compact stash
rtk git worktree        # Compact worktree
```

Note: Git passthrough works for ALL subcommands, even those not explicitly listed.

### GitHub (26-87% savings)
```bash
rtk gh pr view <num>    # Compact PR view (87%)
rtk gh pr checks        # Compact PR checks (79%)
rtk gh run list         # Compact workflow runs (82%)
rtk gh issue list       # Compact issue list (80%)
rtk gh api              # Compact API responses (26%)
```

### JavaScript/TypeScript Tooling (70-90% savings)
```bash
rtk pnpm list           # Compact dependency tree (70%)
rtk pnpm outdated       # Compact outdated packages (80%)
rtk pnpm install        # Compact install output (90%)
rtk npm run <script>    # Compact npm script output
rtk npx <cmd>           # Compact npx command output
rtk prisma              # Prisma without ASCII art (88%)
```

### Files & Search (60-75% savings)
```bash
rtk ls <path>           # Tree format, compact (65%)
rtk read <file>         # Code reading with filtering (60%)
rtk grep <pattern>      # Search grouped by file (75%)
rtk find <pattern>      # Find grouped by directory (70%)
```

### Analysis & Debug (70-90% savings)
```bash
rtk err <cmd>           # Filter errors only from any command
rtk log <file>          # Deduplicated logs with counts
rtk json <file>         # JSON structure without values
rtk deps                # Dependency overview
rtk env                 # Environment variables compact
rtk summary <cmd>       # Smart summary of command output
rtk diff                # Ultra-compact diffs
```

### Infrastructure (85% savings)
```bash
rtk docker ps           # Compact container list
rtk docker images       # Compact image list
rtk docker logs <c>     # Deduplicated logs
rtk kubectl get         # Compact resource list
rtk kubectl logs        # Deduplicated pod logs
```

### Network (65-70% savings)
```bash
rtk curl <url>          # Compact HTTP responses (70%)
rtk wget <url>          # Compact download output (65%)
```

### Meta Commands
```bash
rtk gain                # View token savings statistics
rtk gain --history      # View command history with savings
rtk discover            # Analyze Claude Code sessions for missed RTK usage
rtk proxy <cmd>         # Run command without filtering (for debugging)
rtk init                # Add RTK instructions to CLAUDE.md
rtk init --global       # Add RTK to ~/.claude/CLAUDE.md
```

## Token Savings Overview

| Category | Commands | Typical Savings |
|----------|----------|-----------------|
| Tests | vitest, playwright, cargo test | 90-99% |
| Build | next, tsc, lint, prettier | 70-87% |
| Git | status, log, diff, add, commit | 59-80% |
| GitHub | gh pr, gh run, gh issue | 26-87% |
| Package Managers | pnpm, npm, npx | 70-90% |
| Files | ls, read, grep, find | 60-75% |
| Infrastructure | docker, kubectl | 85% |
| Network | curl, wget | 65-70% |

Overall average: **60-90% token reduction** on common development operations.
<!-- /rtk-instructions -->

---

# Trellis Auto-Detection (ALL PROJECTS)

> These rules apply to ANY directory containing a `.trellis/` subdirectory, across all AI tools (Claude Code, Codex, KimiCode, OpenCode).

## Universal Trellis Protocol

When you start a session in a directory with `.trellis/`:

1. **ALWAYS run context loader first**:
   ```bash
   python3 ./.trellis/scripts/get_context.py
   ```

2. **Read relevant spec indices before coding**:
   ```bash
   cat .trellis/spec/guides/index.md
   # Plus whichever package is relevant:
   # cat .trellis/spec/frontend/index.md
   # cat .trellis/spec/backend/index.md
   ```

3. **Check active task status**:
   ```bash
   python3 ./.trellis/scripts/task.py list
   cat .trellis/.current-task 2>/dev/null || echo "No active task"
   ```

## Universal Auto-Task Rules

When ANY `.trellis/` project is detected, apply these intent triggers:

| User Intent | Auto-Execute | Condition |
|------------|-------------|-----------|
| "我要做 xxx" / "start xxx" / "let's work on xxx" | `task.py create "<title>" --slug <slug>` → `task.py start <slug>` | No active task |
| "做完了" / "done" / "搞定了" | `task.py finish` → `task.py archive <slug>` | Has active task |
| "放弃" / "cancel this" | `task.py archive <current>` | Has active task |
| "查看任务" / "task list" | `task.py list` | Always |
| "上下文" / "status" / "context" | `get_context.py` | Always |

## When NO `.trellis/` Exists

Operate normally without Trellis workflow. Do NOT attempt to create `.trellis/` unless user explicitly requests it.

## Trellis Quick-Init (Only When User Asks)

If user wants to set up Trellis in a new project:
```bash
trellis init -u xioshark
```

---

# Shell Execution Rules

## Multi-line Python / Script Execution

**NEVER** use `python3 -c "` (or `python -c "`, `node -e "`, `ruby -e "`) to execute multi-line code in the terminal. An unclosed quote string causes the shell to enter a continuation prompt (`dquote>`, `∙`, etc.) and the agent session hangs indefinitely.

### Correct Patterns

**Pattern A: Temporary file (preferred for >1 line)**
```bash
cat > /tmp/fix_yaml.py << 'PYEOF'
import yaml
from pathlib import Path

for p in Path('.').glob('private/tasks/*.yaml'):
    try:
        yaml.safe_load(p.read_text())
    except Exception as e:
        print(f"Broken: {p} — {e}")
PYEOF
python3 /tmp/fix_yaml.py
```

**Pattern B: Heredoc without temp file**
```bash
python3 << 'PYEOF'
import os
print(os.getcwd())
PYEOF
```

**Pattern C: Single-line only (for trivial one-liners)**
```bash
python3 -c "import os; print(os.getcwd())"
```

### Forbidden Patterns

```bash
# ❌ NEVER — unclosed double quote
python3 -c "
import os
print(os.getcwd())
"

# ❌ NEVER — unclosed single quote
python3 -c '
import os
print(os.getcwd())
'

# ❌ NEVER — mixing quotes across lines
node -e "
console.log('hello')
"
```

## General Terminal Safety

1. **Always close quotes** before pressing Enter. If a command starts with `"`, `'`, or `` ` ``, ensure the matching closing character is on the same line or properly escaped.
2. **Prefer `&&` over `;`** when chaining commands that depend on each other.
3. **Quote paths**: `cd "/path with spaces"` not `cd /path with spaces`.
4. **Use `rtk` prefix** for build/test/git commands (see RTK section) to reduce token usage.
5. **If a command hangs** (no output for >30s), press `Ctrl+C` to cancel, then rewrite using Pattern A or B.


---

# AI Agent 自主执行协议（新增）

> 适用工具：Codex / Claude Code / Kimi Code / OpenCode 及兼容 Agent 框架

本文档定义了 AI Agent 在执行多步骤任务时的标准工作流。**所有涉及项目文件修改且包含 ≥2 个可独立验收步骤的任务，必须遵循本协议。**

---

## 1. 触发条件

当用户请求满足以下任一条件时，激活本协议：

- 需要新增、修改、删除项目文件
- 需要修复 bug、实现功能、重构代码
- 需要运行测试、构建、部署
- 任务可拆解为 2 个及以上可独立验收的步骤

**单步查询、纯问答、代码解释、代码审查类任务不触发本协议。**

---

## 2. 执行流程（全自动，禁止中断）

### Step 1: 任务拆解与清单创建

1. 将任务拆分为 **3–12 条可验收步骤**，每条以动词开头，描述具体交付物
2. 确定任务名（取自用户请求的短标题，去除标点，过长则截断）
3. 在项目根目录创建 CSV 清单文件：`{任务名} TO DO list.csv`

CSV 格式规范：

```csv
id,item,status,done_at,notes
1,第一步描述,IN_PROGRESS,,
2,第二步描述,TODO,,
3,第三步描述,TODO,,
```

- `id`：从 1 开始的整数
- `item`：步骤描述（与计划同步）
- `status`：`TODO` / `IN_PROGRESS` / `DONE`
- `done_at`：完成时间（ISO 8601，未完成留空）
- `notes`：验证结果、文件路径等备注

### Step 2: 自动执行循环

**核心规则：Agent 必须在同一轮对话/会话中持续执行，直到所有步骤完成，禁止中途停止等待用户确认。**

执行循环逻辑：

```
WHILE 存在 status != "DONE" 的待办项:
  1. 读取 CSV，确认当前 IN_PROGRESS 项
  2. 执行该步骤所需的所有操作（读写文件、运行命令等）
  3. 验证执行结果（运行测试、检查输出、验证文件存在性等）
  4. 将该步骤标记为 DONE，记录 done_at 和 notes
  5. 将下一项 TODO 标记为 IN_PROGRESS
  6. 更新 CSV 文件
END WHILE
```

状态流转约束：
- 仅允许：`TODO` → `IN_PROGRESS` → `DONE`
- 任意时刻最多只有 **1 行** `IN_PROGRESS`
- 只要仍有未完成项，必须保持恰好 1 行 `IN_PROGRESS`

### Step 3: 验证与清理

1. 确认 CSV 中所有行的 `status` 均为 `DONE`
2. 删除 CSV 文件：`{任务名} TO DO list.csv`
3. 输出执行摘要，包含：
   - 任务目标
   - 完成的步骤数 / 总步骤数
   - 关键交付物列表
   - 验证结果

**禁止将未完成的 CSV 文件遗留或提交进仓库。**

---

## 3. 自动化脚本（优先使用）

若项目已配置 `todo-list-csv` 技能脚本，优先使用以下命令操作，避免手动编辑 CSV：

```bash
# 创建清单（默认第 1 条为 IN_PROGRESS）
python3 ~/.agents/skills/todo-list-csv/scripts/todo_csv.py init \
  --title "{任务名}" \
  --item "步骤1" "步骤2" "步骤3" ...

# 推进一步（完成当前 IN_PROGRESS，启动下一个 TODO）
python3 ~/.agents/skills/todo-list-csv/scripts/todo_csv.py advance \
  --file "{CSV路径}" \
  --notes "{验证摘要}"

# 查看当前状态
python3 ~/.agents/skills/todo-list-csv/scripts/todo_csv.py status \
  --file "{CSV路径}" --verbose

# 全部完成后清理
python3 ~/.agents/skills/todo-list-csv/scripts/todo_csv.py cleanup \
  --file "{CSV路径}"
```

**脚本不可用时，使用标准文件读写工具按 CSV 格式规范直接操作。**

---

## 4. 异常处理

| 场景 | 处理方式 |
|---|---|
| 步骤执行失败 | 标记该步骤 `status=FAILED`，记录失败原因到 `notes`，暂停执行并报告用户 |
| 需要用户输入/决策 | 在 CSV 中追加步骤 `"等待用户确认: {具体事项}"`，置为 `IN_PROGRESS`，然后暂停 |
| 任务范围变更 | 只做"追加"操作，在 CSV 末尾新增步骤，避免重排/重编号 |
| 重试超过 5 次 | 改变策略或拆分更细步骤，记录到 `notes` |

---

## 5. 上下文恢复

若会话中断后恢复，按以下顺序重建上下文：

1. 扫描项目根目录，查找名称匹配 `* TO DO list.csv` 的文件
2. 读取 CSV，定位第一个非 `DONE` 的项
3. 根据已完成步骤的 `notes` 重建执行上下文
4. 继续执行循环

---

## 6. 子项目适用规则

本工作区包含多个子项目（`一面/`, `二面/`, `三面/` 等）。执行时：

- **若在根目录接收任务**：在根目录创建 CSV，操作可能涉及多个子项目
- **若在子目录内接收任务**：优先在该子目录创建 CSV，仅操作该子项目范围
- 各子目录下的 `AGENTS.md` 如存在特殊规则，**优先于本文件**

---

## 7. 输出格式

每次状态更新必须包含以下字段（简洁输出，避免冗余）：

```
任务: {任务目标}
进度: {已完成数}/{总数}
当前: {当前步骤描述}
验证: {最新验证方式和结果}
文件: {CSV文件路径}
```

全部完成后输出：

```
✅ 任务完成: {任务名}
步骤: {N}/{N} 全部完成
交付: {关键文件/结果列表}
```
