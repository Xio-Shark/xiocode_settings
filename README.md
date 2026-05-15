# xiocode_settings

统一的多工具 AI Agent 配置仓库。一套规则，四个工具同步生效。

## 支持的工具

| 工具 | 配置位置 | 规则来源 | 自动加载 |
|------|---------|---------|---------|
| **Claude Code** | `~/.claude/` | `CLAUDE.md` | ✓ 每次会话自动注入 |
| **Codex** | `~/.codex/` | `AGENTS.md` | ✓ 每次会话自动注入 |
| **Kiro CLI** | `~/.kiro/steering/` | 7 个 steering 文件 | ✓ 按 inclusion 策略加载 |
| **Copilot CLI** | `.github/` | `copilot-instructions.md` | ✓ 项目级自动加载 |

## 核心理念

### 1. 胶水编程（Glue Coding）

AI 是模块间的桥梁工程师，不是代码生成器。优先组合现有工具，禁止在胶水层重新实现业务逻辑。

### 2. Debug-First

禁止静默降级、禁止 mock 假成功路径、禁止防御性代码掩盖错误。让失败清楚暴露，在源头修复。

### 3. Karpathy 原则

- **编码前思考**：不确定就询问，不猜测
- **简洁优先**：200 行能写成 50 行就重写
- **精准修改**：只碰必须碰的，匹配现有风格
- **目标驱动**：转换为可验证目标，循环直到通过

## 仓库结构

```
xiocode_settings/
│
├── CLAUDE.md                         # 全局规则（329 行）— 唯一权威源
├── AGENTS.md                         # 项目级规则（136 行）— career 仓库专用
├── AGENTS.*.md                       # 子规则（5 个文件，按场景按需加载）
│   ├── AGENTS.gitnexus.md            #   代码智能（impact 分析、重构）
│   ├── AGENTS.knowledge-mcp.md       #   知识检索（最高优先级）
│   ├── AGENTS.rtk.md                 #   RTK 命令速查表
│   ├── AGENTS.shell-safety.md        #   终端安全（禁 heredoc）
│   └── AGENTS.trellis.md             #   Trellis 任务管理
├── TRELLIS-WORKFLOW.md               # Multi-Agent Pipeline 工作流规范
├── codex-AGENTS.md                   # Codex 全局配置（CLAUDE.md 副本）
│
├── kiro-steering/                    # Kiro CLI steering 文件（7 个）
│   ├── global.md                     #   核心规则（always）
│   ├── skills-routing.md             #   Skill 路由表（always）
│   ├── autonomous-protocol.md        #   自主执行协议（always）
│   ├── trellis.md                    #   Trellis 检测（fileMatch）
│   ├── trellis-pipeline.md           #   Pipeline 工作流（always）
│   ├── rtk.md                        #   RTK 命令参考（manual）
│   └── shell-safety.md               #   终端安全（always）
│
├── .github/
│   └── copilot-instructions.md       # Copilot CLI 项目指令
│
├── settings.json                     # Claude Code 配置（model、hooks、env）
├── settings.local.json               # 权限白名单（28 条）
├── mcp.json                          # MCP 服务器配置
│
├── skills/                           # 57 个 skills（所有工具共享）
│   └── .system/
│       └── SKILLS-REFERENCE.md       # 完整路由表
│
├── agents/                           # Trellis Pipeline Agent 定义（6 个）
│   ├── plan.md                       #   规划 Agent
│   ├── implement.md                  #   实现 Agent
│   ├── check.md                      #   检查 Agent
│   ├── debug.md                      #   调试 Agent
│   ├── dispatch.md                   #   调度 Agent
│   └── research.md                   #   研究 Agent
│
├── hooks/                            # Claude Code hooks
│   ├── trellis-check.sh              #   Trellis 自动检测
│   └── post-session.sh               #   会话结束后自动索引
│
└── .gitignore
```

## Skills 同步策略

所有工具通过符号链接共享同一个 skills 目录：

```
~/.claude/skills/              ← 源头（57 个 skills）
    ↑            ↑              ↑
    │            │              │
~/.kiro/skills/  ~/.agents/skills/  ~/.copilot/skills/
  (symlink)       (symlink)           (symlink)
                       ↑
                 ~/.codex/skills/
                   (symlink)
```

## 规则层级

```
CLAUDE.md（全局权威源）
  ↓ 被引用
AGENTS.md（项目级补充）
  ↓ 按场景加载
AGENTS.*.md（子规则细节）
```

- **CLAUDE.md** 定义通用规则（Glue Coding、Karpathy、Code Metrics、Security、Skills 路由、Trellis、自主执行协议）
- **AGENTS.md** 定义项目特有规则（会话起手式、目录约定、List 文档协议、子规则索引）
- **AGENTS.*.md** 定义场景细节（GitNexus 操作、knowledge_mcp 检索、RTK 命令、Shell 安全、Trellis 任务管理）

## 关键协议

### 自主执行协议

所有 ≥2 步骤的任务自动触发：

```csv
id,group,item,status,notes
1,A,步骤描述,TODO,
2,B,步骤描述,TODO,
```

- 统一 CSV 格式（含 `group` 列）
- 完成即删（CSV 只反映未完成工作）
- 三组解耦拆分（组间零依赖）

### List 文档自动执行

触发词："创建list文档"、"做个list"、"建个执行清单"

自动产出：
1. `{任务名} 规划.md` — 目标、分组策略
2. `{任务名} TO DO list.csv` — 带 group 列的执行清单

### Trellis 自动检测

检测到 `.trellis/` 目录时自动：
1. 运行 `get_context.py` 加载上下文
2. 读取 `AGENTS.md` 项目规则
3. 检查 `knowledge_mcp` 可用性
4. 读取 spec 索引
5. 检查活跃任务状态

## 在新机器上部署

```bash
# 1. 克隆配置仓库
git clone https://github.com/Xio-Shark/xiocode_settings.git /tmp/xiocode_settings

# 2. Claude Code
mkdir -p ~/.claude
cp /tmp/xiocode_settings/CLAUDE.md ~/.claude/
cp /tmp/xiocode_settings/settings.json ~/.claude/
cp /tmp/xiocode_settings/settings.local.json ~/.claude/
cp /tmp/xiocode_settings/TRELLIS-WORKFLOW.md ~/.claude/
cp -r /tmp/xiocode_settings/skills ~/.claude/
cp -r /tmp/xiocode_settings/hooks ~/.claude/
cp -r /tmp/xiocode_settings/agents ~/.claude/

# 3. Codex
mkdir -p ~/.codex
cp /tmp/xiocode_settings/codex-AGENTS.md ~/.codex/AGENTS.md

# 4. Kiro CLI
mkdir -p ~/.kiro/steering
cp /tmp/xiocode_settings/kiro-steering/*.md ~/.kiro/steering/

# 5. Skills 符号链接
ln -sf ~/.claude/skills ~/.agents/skills
ln -sf ~/.claude/skills ~/.kiro/skills
ln -sf ~/.claude/skills ~/.copilot/skills

# 6. 环境变量（加到 ~/.zshrc）
export ANTHROPIC_BASE_URL="http://127.0.0.1:15721"
export ANTHROPIC_AUTH_TOKEN="PROXY_MANAGED"
export ENABLE_TOOL_SEARCH="true"

# 7. Kiro bypass 别名（可选）
echo 'alias kiro="kiro-cli chat -a"' >> ~/.zshrc
echo 'alias kt="kiro-cli chat -a --tui"' >> ~/.zshrc

# 8. 验证
source ~/.zshrc
claude --version
rtk --version
kiro-cli --version
```

## 依赖

| 工具 | 用途 | 安装方式 |
|------|------|---------|
| Claude Code | AI CLI | `npm install -g @anthropic-ai/claude-code` |
| Codex | AI CLI (OpenAI) | `npm install -g @openai/codex` |
| Kiro CLI | AI CLI (AWS) | `brew install kiro-cli` |
| Copilot CLI | AI CLI (GitHub) | `npm install -g @github/copilot` |
| rtk | Token 优化器 | `cargo install rtk` |
| gh | GitHub CLI | `brew install gh` |
| trellis | 多 Agent Pipeline | `pip install trellis-ai` |

## Changelog

### 2026-05-15 — 多工具统一配置

- Skills 精简：90 → 57（删除 34 个冗余/phantom skills）
- 统一 CSV 协议：group 列 + 完成即删，所有工具一致
- 新增 "创建list文档" 自动触发（三组解耦拆分）
- 同步配置到 Codex、Kiro CLI、Copilot CLI
- 新增 Kiro steering 文件（7 个）
- 新增 `.github/copilot-instructions.md`
- 通过符号链接统一 skills（4 个工具共享 57 个 skills）
- 解决 6 个跨文件冲突（RTK、CSV、会话启动、commit 策略、AGENTS.md 加载、路由合并）
- 新增 Kiro bypass 别名（`kiro` / `kt`）

### 2026-05-09 — 初始备份

- 首次备份 `~/.claude/` 配置

## License

个人配置，仅供参考。
