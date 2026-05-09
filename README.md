# xiocode_settings

Personal Claude Code configuration — version controlled, cross-machine sync, and reproducible AI-assisted development workflow.

## Philosophy

This configuration follows three core principles:

1. **Glue Coding** — AI acts as a bridge engineer, not a code generator. Prefer composing existing tools (skills, plugins, libraries) over writing custom business logic.
2. **Debug-First** — Failures surface explicitly. No silent fallbacks, no mock success paths, no defensive code that hides root causes.
3. **Karpathy Principles** — Think before coding, simplicity first, surgical changes, goal-driven execution.

## Directory Structure

```
xiocode_settings/
├── CLAUDE.md              # Core agent rules (297 lines)
│                           # Language, glue coding, debug-first policy,
│                           # Karpathy principles, code metrics, security baseline
├── AGENTS.md              # Agent index — links to agents/*.md + Trellis workflow
├── TRELLIS-WORKFLOW.md    # Multi-Agent Pipeline spec (plan → implement → check → debug → finish → create-pr)
├── RTK.md                 # Token-Optimized Commands reference (60-90% token savings)
│
├── settings.json          # Main config: model (opus[1m]), hooks, env, statusLine
├── settings.local.json    # Permission allowlist (28 entries)
├── mcp.json               # 7 MCP servers (context7, gitnexus, shadcn, genericagent-browser,
│                           # omc, code-agent-insights, personal-kb)
│
├── agents/                # 6 Agent definitions for Trellis Pipeline
│   ├── plan.md            # Pipeline planner — evaluates and rejects bad requirements
│   ├── implement.md       # Code implementer — reads spec, writes code
│   ├── check.md           # Quality checker — fixes issues, not just reports
│   ├── debug.md           # Bug fixer — precise fixes, no refactoring
│   ├── dispatch.md        # Pipeline dispatcher — phase orchestration
│   └── research.md        # Researcher — find and explain, no modifications
│
├── hooks/                 # PreToolUse + session hooks
│   ├── trellis-check.sh   # Auto-detect .trellis projects on Bash tool use
│   ├── post-session.sh    # Auto-index sessions via code-agent-insights
│   └── gitnexus/          # GitNexus MCP hook integration
│
├── memory/                # AI Memory system (user, feedback, project, reference)
│   ├── MEMORY.md          # Index
│   ├── user_role.md       # User background and preferences
│   ├── feedback_terse.md  # No trailing summaries / follow-ups
│   └── feedback_glue_coding.md  # Prefer composing existing tools
│
├── external/              # MCP bridge scripts (stable paths)
│   ├── genericagent-browser-mcp.py   # Browser automation MCP bridge
│   └── personal-kb-mcp.py            # Personal knowledge base MCP bridge
│
├── commands/              # Custom slash commands
│   └── trellis/           # Trellis workflow commands (20+ commands)
│
├── ccline/                # Custom status line (Rust binary + themes)
│   ├── ccline             # Binary
│   ├── models.toml        # Model config
│   └── themes/            # 9 color themes
│
├── skills/.system/        # Skill reference docs
│   └── SKILLS-REFERENCE.md    # Complete 90-row routing table
│
├── tasks/                 # Runtime task state (not versioned)
├── teams/                 # Agent team configs (not versioned)
└── plugins-data/          # Plugin runtime data (not versioned)
```

## Key Metrics

| Component | Before | After | Change |
|-----------|--------|-------|--------|
| CLAUDE.md | 685 lines | **297 lines** | -57% |
| AGENTS.md | 685 lines | **31 lines** | -95% |
| Skills routing | inline | extracted to `skills/.system/` | +113 lines ref |
| RTK commands | 30 lines | **full reference** | +200 lines |
| MCP security | hardcoded API key | **env var only** | fixed |
| Permissions | 5 entries | **28 entries** | +460% |
| Duplicate skills | 91 total | **90 total** | -1 duplicate |

## Changelog

### 2026-05-09 — Configuration Optimization

**Commit:** `7f3e88c` — `refactor: optimize Claude Code config`

- **CLAUDE.md slimmed** (685 → 297 lines, -57%)
  - Extracted RTK command reference → `RTK.md`
  - Extracted skills routing table → `skills/.system/SKILLS-REFERENCE.md`
  - Retained: glue coding philosophy, debug-first policy, Karpathy principles, code metrics, security baseline, shell execution rules, AI agent autonomous execution protocol
- **AGENTS.md deduplicated** (685 → 31 lines, -95%)
  - Removed duplicate content identical to CLAUDE.md
  - Now a pure agent index linking to `agents/*.md` and `TRELLIS-WORKFLOW.md`
- **MCP security hardening**
  - Removed hardcoded `ctx7sk-...` API key from `mcp.json`
  - Context7 MCP now reads from `CONTEXT7_API_KEY` environment variable (persisted in `~/.zshrc`)
  - Moved `genericagent-browser` and `personal-kb` bridge scripts from `Downloads/` / `Desktop/` → `external/` for stable paths
- **Memory system booted**
  - Added `user_role.md` — senior engineer profile, glue coding philosophy
  - Added `feedback_terse.md` — no trailing summaries
  - Added `feedback_glue_coding.md` — prefer tool composition
  - Added `MEMORY.md` index
- **Permissions expanded** (5 → 28 entries)
  - Added rtk, find, grep, cat, wc, npm info, diff, MCP commands, Trellis scripts, .claude dir operations
- **Cleanup**
  - Removed duplicate `react-best-practices` skill (identical to `nextjs-react-expert`)
  - Deleted old `settings.json.bak.*` files

### 2026-05-09 — Nature Skills Submodule Inline

**Commit:** `2e503b7` — `fix: inline nature-skills submodule content`

- Inlined `nature-skills` submodule content into the repository

### 2026-05-09 — Initial Backup

**Commit:** `867cffa` — `feat: backup Claude Code settings from 2026-05-09`

- Initial snapshot of `~/.claude/` configuration
- Included: CLAUDE.md, AGENTS.md, settings.json, mcp.json, RTK.md, TRELLIS-WORKFLOW.md, agents/, hooks/, commands/, ccline/, skills/ (90 skills), tasks/, teams/

## Setup on a New Machine

```bash
# 1. Clone
git clone https://github.com/Xio-Shark/xiocode_settings.git ~/.claude

# 2. Install dependencies
# - rtk (Rust Token Killer): cargo install rtk  # or via homebrew
# - ccline: cp ccline/target/release/ccometixline ~/.claude/ccline/ccline
# - Claude Code CLI: npm install -g @anthropic-ai/claude-code

# 3. Set environment variables
export ANTHROPIC_BASE_URL="http://127.0.0.1:15721"   # or your proxy
export ANTHROPIC_AUTH_TOKEN="PROXY_MANAGED"           # or your key
export CONTEXT7_API_KEY="your-context7-key"           # for context7 MCP
export ENABLE_TOOL_SEARCH="true"
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS="1"

# 4. Verify
claude --version
rtk --version
```

## Dependencies

| Tool | Purpose | Install |
|------|---------|---------|
| Claude Code | AI CLI | `npm install -g @anthropic-ai/claude-code` |
| rtk | Token optimizer | `cargo install rtk` / homebrew |
| gh | GitHub CLI | `brew install gh` |
| ccline | Custom status line | Build from source (Rust) |
| trellis | Multi-agent pipeline | `pip install trellis-ai` |
| cai | Code agent insights | `pnpm install -g cai-mcp` |

## License

Personal configuration — use as reference for your own setup.
