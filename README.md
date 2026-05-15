# xiocode_settings

Claude Code 个人配置备份 — 版本管理、跨机器同步。

## 目录结构

```
xiocode_settings/
├── CLAUDE.md                    # 全局规则（329 行）
├── TRELLIS-WORKFLOW.md          # Multi-Agent Pipeline 工作流
├── settings.json                # 配置（model、hooks、env）
├── settings.local.json          # 权限白名单
├── skills/                      # 57 个 skills
│   └── .system/
│       └── SKILLS-REFERENCE.md  # Skill 路由表
├── agents/                      # 6 个 Trellis Agent 定义
└── hooks/                       # Session + Tool hooks
```

## CLAUDE.md 核心规则

| 规则 | 内容 |
|------|------|
| 胶水编程 | AI 是桥梁工程师，优先组合现有工具 |
| Debug-First | 禁止静默降级，失败必须暴露 |
| Karpathy 原则 | 编码前思考、简洁优先、精准修改、目标驱动 |
| Code Metrics | 函数 50 行、文件 300 行、嵌套 3 层 |
| Security | 不硬编码 secret，参数化 SQL |
| Skills 路由 | 13 条高频路由 + "创建list文档" 触发 |
| RTK | 所有 shell 命令加 `rtk` 前缀 |
| Trellis | 自动检测 `.trellis/`，会话启动加载上下文 |
| 自主执行协议 | 统一 CSV（group 列 + 完成即删） |
| List 文档协议 | 三组解耦拆分，自动创建规划 + CSV |

## 新机器部署

```bash
# 1. 克隆
git clone https://github.com/Xio-Shark/xiocode_settings.git /tmp/xiocode_settings

# 2. 部署到 ~/.claude
mkdir -p ~/.claude
cp /tmp/xiocode_settings/CLAUDE.md ~/.claude/
cp /tmp/xiocode_settings/TRELLIS-WORKFLOW.md ~/.claude/
cp /tmp/xiocode_settings/settings.json ~/.claude/
cp /tmp/xiocode_settings/settings.local.json ~/.claude/
cp -r /tmp/xiocode_settings/skills ~/.claude/
cp -r /tmp/xiocode_settings/hooks ~/.claude/
cp -r /tmp/xiocode_settings/agents ~/.claude/

# 3. 设置环境变量（加到 ~/.zshrc）
export ANTHROPIC_BASE_URL="http://127.0.0.1:15721"
export ANTHROPIC_AUTH_TOKEN="PROXY_MANAGED"
export ENABLE_TOOL_SEARCH="true"

# 4. 验证
claude --version
```

## 依赖

| 工具 | 安装 |
|------|------|
| Claude Code | `npm install -g @anthropic-ai/claude-code` |
| rtk | `cargo install rtk` |
| gh | `brew install gh` |

## Changelog

### 2026-05-15

- Skills 精简：90 → 57
- 统一 CSV 协议（group 列 + 完成即删）
- 新增 "创建list文档" 自动触发
- 解决 6 个跨文件冲突
- 新增 Kiro bypass 别名

### 2026-05-09

- 初始备份
