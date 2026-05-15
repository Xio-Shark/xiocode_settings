# xiocode_settings

Multi-tool AI agent configuration — unified rules across Claude Code, Codex, Kiro CLI, and GitHub Copilot CLI.

## Tool Coverage

| Tool | Config Location | Rules Source |
|------|----------------|-------------|
| Claude Code | `~/.claude/` | `CLAUDE.md` (auto-injected) |
| Codex | `~/.codex/` | `codex-AGENTS.md` (copy of CLAUDE.md) |
| Kiro CLI | `~/.kiro/` | `kiro-steering/*.md` (7 files) |
| Copilot CLI | `.github/` | `copilot-instructions.md` |

All tools share the same `skills/` directory via symlinks.

## Directory Structure

```
xiocode_settings/
├── CLAUDE.md                    # Global rules (329 lines) — source of truth
├── AGENTS.md                    # Project-level rules (136 lines)
├── AGENTS.*.md                  # Sub-rules (gitnexus, knowledge-mcp, rtk, shell-safety, trellis)
├── TRELLIS-WORKFLOW.md          # Multi-Agent Pipeline spec
├── codex-AGENTS.md              # Codex global config (copy of CLAUDE.md)
│
├── kiro-steering/               # Kiro CLI steering files
│   ├── global.md                # Core rules (always loaded)
│   ├── skills-routing.md        # Skill trigger table (always loaded)
│   ├── autonomous-protocol.md   # CSV execution protocol (always loaded)
│   ├── trellis.md               # Trellis auto-detection (fileMatch)
│   ├── trellis-pipeline.md      # Pipeline workflow (always loaded)
│   ├── rtk.md                   # RTK commands (manual)
│   └── shell-safety.md          # Shell safety rules (always loaded)
│
├── .github/
│   └── copilot-instructions.md  # Copilot CLI project instructions
│
├── settings.json                # Claude Code config (model, env, hooks)
├── settings.local.json          # Permission allowlist
├── mcp.json                     # MCP servers config
│
├── skills/                      # 57 skills (shared across all tools via symlinks)
│   └── .system/
│       └── SKILLS-REFERENCE.md  # Complete routing table
│
├── agents/                      # Trellis Pipeline agent definitions
├── hooks/                       # Session + tool hooks
├── commands/                    # Custom slash commands
├── external/                    # MCP bridge scripts
└── memory/                      # AI memory system
```

## Core Rules (CLAUDE.md)

| Section | Purpose |
|---------|---------|
| Glue Coding Philosophy | AI as bridge engineer, not code generator |
| Debug-First Policy | No silent fallbacks, no mock success |
| Karpathy Principles | Think before coding, simplicity first, surgical changes |
| Code Metrics | 50-line functions, 300-line files, 3-level nesting |
| Security Baseline | No hardcoded secrets, parameterized queries |
| Skills Auto-Trigger | 13-route table + "创建list文档" trigger |
| RTK | All shell commands prefixed with `rtk` |
| Trellis Auto-Detection | Session start + auto-task rules |
| AI Agent Protocol | Unified CSV format (group column, delete-on-complete) |
| List Document Protocol | 3-group decoupling, auto-split, auto-cleanup |

## Skills Sync Strategy

```
~/.claude/skills/          ← Source of truth (57 skills)
    ↑           ↑           ↑
    │           │           │
~/.kiro/skills/  ~/.agents/skills/  ~/.copilot/skills/
  (symlink)       (symlink)           (symlink)
                     ↑
               ~/.codex/skills/
                 (symlink)
```

## Setup on a New Machine

```bash
# 1. Clone
git clone https://github.com/Xio-Shark/xiocode_settings.git /tmp/xiocode_settings

# 2. Copy Claude Code config
cp /tmp/xiocode_settings/CLAUDE.md ~/.claude/
cp /tmp/xiocode_settings/settings.json ~/.claude/
cp /tmp/xiocode_settings/settings.local.json ~/.claude/
cp -r /tmp/xiocode_settings/skills ~/.claude/
cp -r /tmp/xiocode_settings/hooks ~/.claude/
cp -r /tmp/xiocode_settings/agents ~/.claude/
cp /tmp/xiocode_settings/TRELLIS-WORKFLOW.md ~/.claude/

# 3. Copy Codex config
cp /tmp/xiocode_settings/codex-AGENTS.md ~/.codex/AGENTS.md

# 4. Copy Kiro steering
cp /tmp/xiocode_settings/kiro-steering/*.md ~/.kiro/steering/

# 5. Setup shared skills symlinks
ln -sf ~/.claude/skills ~/.agents/skills
ln -sf ~/.claude/skills ~/.kiro/skills
ln -sf ~/.claude/skills ~/.copilot/skills

# 6. Set environment variables
export ANTHROPIC_BASE_URL="http://127.0.0.1:15721"
export ANTHROPIC_AUTH_TOKEN="PROXY_MANAGED"
export ENABLE_TOOL_SEARCH="true"

# 7. Verify
claude --version
rtk --version
```

## Changelog

### 2026-05-15 — Multi-Tool Sync & Cleanup

- Cleaned skills: 90 → 57 (removed 34 redundant/phantom skills)
- Unified CSV protocol: group column + delete-on-complete across all tools
- Added "创建list文档" auto-trigger with 3-group decoupling
- Synced config to Codex, Kiro CLI, and Copilot CLI
- Added Kiro steering files (7 files)
- Added `.github/copilot-instructions.md`
- Unified skills via symlinks across all 4 tools
- Resolved 6 cross-file conflicts (RTK, CSV, session startup, commit strategy, AGENTS.md loading, route merge)

### 2026-05-09 — Initial Backup

- Initial snapshot of `~/.claude/` configuration
