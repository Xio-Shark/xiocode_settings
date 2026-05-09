# CLAUDE.md

> 本文档为 AI 助手（Claude Code）提供项目上下文，帮助其快速理解项目结构、技术栈、开发规范和关键决策。
> 这是项目的"记忆体"，应随项目演进持续更新。

---

## 项目简介

**项目名称**：[项目名称]

**项目描述**：[一句话描述项目是什么，解决什么问题]

**项目类型**：[Web 应用 / 移动应用 / API 服务 / CLI 工具 / 库 / 其他]

**项目阶段**：[概念验证 / 开发中 / 测试中 / 生产运行]

**开始时间**：YYYY-MM-DD

**当前版本**：v0.1.0

---

## 核心文档

| 文档 | 路径 | 内容 |
|------|------|------|
| PRD | `docs/prd/v1.0.0/prd.md` | 产品需求文档，定义功能规格与验收标准 |
| 设计 | `docs/design/v1.0.0/design.md` | 页面清单、交互流程、组件规范 |
| 技术开发文档 | `docs/dev/v1.0.0/dev.md` | 架构、DB Schema、API 设计、目录结构 |
| 开发计划 | `docs/plan/v1.0.0/plan.md` | 里程碑、任务清单、时间线 |
| 部署运维 | `docs/ops/v1.0.0/ops.md` | 环境变量、部署流程、监控告警、故障排查 |
| 测试文档 | `docs/test/v1.0.0/test.md` | 测试策略、用例设计、自动化测试 |
| 变更日志 | `CHANGELOG.md` | 版本历史、变更记录 |

**文档边界**：
- `prd.md` = 做什么（功能需求）
- `design.md` = 长什么样（UI/UX）
- `dev.md` = 怎么实现（技术方案）
- `plan.md` = 什么时候做（时间线）
- `ops.md` = 如何部署和运维（环境、监控、故障处理）
- `test.md` = 如何测试和验证（测试策略、用例）

---

## 技术栈

| 层 | 技术 | 版本 | 说明 |
|----|------|------|------|
| 前端框架 | [React / Vue / Angular / Next.js / ...] | X.x | [说明] |
| 前端样式 | [Tailwind / CSS Modules / Styled Components / ...] | X.x | [说明] |
| 前端状态 | [Redux / Zustand / Jotai / ...] | X.x | [说明] |
| 后端框架 | [NestJS / Express / FastAPI / Django / ...] | X.x | [说明] |
| 运行时 | [Node.js / Python / Go / ...] | X.x | [说明] |
| ORM | [Prisma / TypeORM / SQLAlchemy / ...] | X.x | [说明] |
| 数据库 | [PostgreSQL / MySQL / MongoDB / ...] | X.x | [说明] |
| 缓存/队列 | [Redis / RabbitMQ / ...] | X.x | [说明] |
| 部署 | [Vercel / Docker / K8s / ...] | — | [说明] |
| Monorepo | [Turborepo / Nx / Lerna / ...] | X.x | [说明] |

---

## 项目结构

```
project-root/
├── apps/
│   ├── web/                  # 前端应用
│   │   └── src/
│   │       ├── app/          # 页面路由
│   │       ├── components/   # UI 组件
│   │       └── lib/          # 工具函数
│   └── api/                  # 后端应用
│       └── src/
│           ├── modules/      # 业务模块
│           └── common/       # 公共模块
├── packages/
│   └── shared/               # 前后端共享代码
├── docs/                     # 文档目录
│   ├── prd/
│   ├── design/
│   ├── dev/
│   ├── plan/
│   ├── ops/
│   └── test/
├── scripts/                  # 脚本目录
├── prisma/                   # 数据库 Schema & 迁移
├── docker-compose.yml        # 本地开发环境
├── turbo.json                # Turborepo 配置
├── CHANGELOG.md              # 变更日志
└── CLAUDE.md                 # 本文档
```

---

## 常用命令

```bash
# 启动本地开发环境
pnpm dev

# 仅启动后端
pnpm --filter api dev

# 仅启动前端
pnpm --filter web dev

# 数据库迁移
pnpm --filter api prisma migrate dev

# 类型检查
pnpm type-check

# Lint
pnpm lint

# 测试
pnpm test:all

# 构建
pnpm build

# 部署
bash scripts/deploy.sh
```

---

## 核心架构要点

### 1. [关键架构决策 1]

**背景**：[为什么需要这个决策]

**方案**：[具体实现方案]

**权衡**：[优点 / 缺点 / 为什么选择这个方案]

**示例**：
```typescript
// 代码示例
```

### 2. [关键架构决策 2]

...

---

## 数据库关键约束

- [约束 1]：[说明]
- [约束 2]：[说明]
- [约束 3]：[说明]

---

## 安全规范

- [规范 1]：[说明]
- [规范 2]：[说明]
- [规范 3]：[说明]

---

## 开发规范

### 代码风格

- **命名规范**：[说明]
- **文件组织**：[说明]
- **注释规范**：[说明]

### Git 规范

- **分支策略**：[main / develop / feature / hotfix]
- **Commit 规范**：[Conventional Commits / 自定义]
- **PR 流程**：[说明]

### 测试规范

- **测试覆盖率**：[目标覆盖率]
- **测试类型**：[单元测试 / 集成测试 / E2E 测试]
- **测试命令**：`pnpm test:all`

---

## 自动化测试 — 强制规则

**任何对功能逻辑的新增 / 修改 / 删除，必须在同一个 commit 内同步更新对应的自动化测试。**

### 测试落点速查表

| 改动类型 | 必须同步更新的测试 |
|---------|---------|
| 后端 service / controller | `apps/api/src/modules/<mod>/__tests__/*.spec.ts` |
| 跨服务的事务 / 资金相关 | `apps/api/src/integration-tests/*.integration.spec.ts` |
| Prisma schema / 字段约束 | seed.ts + 集成测试用例 |
| DTO 校验规则 | 对应 service spec 或静态扫描脚本 |
| 前端组件 / 页面 / hook | 静态断言或 React Testing Library |

### 一键测试入口

| 命令 | 用途 |
|------|------|
| `pnpm test:all` | lint + typecheck + 单测 + 集成测试 + 构建 + 静态扫描 |
| `pnpm test:quick` | 仅 lint + typecheck + 单测 + 静态扫描（跳过构建与集成）|
| `pnpm test:full` | 上述 + 临时拉起后端跑运行时 API 烟测 |

### 部署前流程

1. 改完代码
2. 同步增 / 改对应自动化测试
3. `pnpm test:all` 全绿
4. `git add -A && git commit -m "<...>"`
5. `git push origin main`
6. `bash scripts/deploy.sh`

---

## PRD/设计稿驱动 + 端到端真实数据 — 强制规则

**任何"页面渲染了 / 接口返回 200 / 但运营看到的是空"都视为 P0 BUG。**

每加一个新功能 / 改动一个模块前，**必须先做端到端确认**：

1. 打开 PRD 找需求条目
2. 打开 design.md 找页面定义
3. 代码三件套必须配齐：后端 service / controller + 前端 page + 单元 / 集成测试
4. catch 块绝不允许静默吞错：必须 `console.error` 或 `showToast`
5. 验证步骤：本地起服务 → seed 真实数据 → 走一遍 happy path + edge cases

---

## 已知问题与技术债

### 已知问题

| 问题 | 影响 | 优先级 | 负责人 | 状态 |
|------|------|--------|--------|------|
| [问题描述] | [影响范围] | P1 / P2 / P3 | [姓名] | 待修复 / 修复中 / 已修复 |

### 技术债

| 技术债 | 原因 | 影响 | 优先级 | 负责人 | 状态 |
|--------|------|------|--------|--------|------|
| [技术债描述] | [为什么产生] | [影响范围] | P1 / P2 / P3 | [姓名] | 待处理 / 处理中 / 已处理 |

---

## 关键决策记录（ADR）

### ADR-001: [决策标题]

**日期**：YYYY-MM-DD

**状态**：[提议 / 已接受 / 已废弃 / 已替代]

**背景**：[为什么需要做这个决策]

**决策**：[具体决策内容]

**后果**：[这个决策带来的影响（正面 / 负面）]

**替代方案**：[考虑过但未采纳的方案]

---

## 环境变量清单

### 后端环境变量

| 变量名 | 必填 | 默认值 | 说明 | 获取方式 |
|--------|------|--------|------|---------|
| `DATABASE_URL` | ✅ | - | 数据库连接字符串 | [数据库服务商控制台] |
| `REDIS_URL` | ✅ | - | Redis 连接字符串 | [Redis 服务商控制台] |
| `NODE_ENV` | ✅ | `development` | 运行环境 | 手动设置 |
| `PORT` | ❌ | `3001` | 服务端口 | 手动设置 |
| `JWT_SECRET` | ✅ | - | JWT 签名密钥 | `openssl rand -hex 32` |

### 前端环境变量

| 变量名 | 必填 | 默认值 | 说明 | 获取方式 |
|--------|------|--------|------|---------|
| `NEXT_PUBLIC_API_URL` | ✅ | - | API 基础 URL | 手动设置 |
| `NEXT_PUBLIC_SITE_URL` | ✅ | - | 站点 URL | 手动设置 |

---

## 部署架构

### 生产环境

- **前端**：[Vercel / Cloudflare Pages / Nginx]
- **后端**：[Docker + VPS / K8s / Serverless]
- **数据库**：[Supabase / AWS RDS / 自建]
- **缓存**：[Upstash / AWS ElastiCache / 自建]

### 部署流程

1. [步骤 1]
2. [步骤 2]
3. [步骤 3]

详见：`docs/ops/v1.0.0/ops.md`

---

## 监控与告警

### 关键指标

| 指标 | 正常范围 | 告警阈值 | 监控方式 |
|------|---------|---------|---------|
| API 响应时间 | < 500ms | > 2s | APM 工具 |
| 错误率 | < 1% | > 5% | 日志聚合 |
| CPU 使用率 | < 70% | > 90% | 服务器监控 |
| 内存使用率 | < 80% | > 95% | 服务器监控 |

### 告警渠道

- **邮件**：管理员邮箱
- **Slack/企微/Telegram**：团队频道
- **短信**：紧急告警（P0 级别）

---

## 团队协作

### 团队成员

| 角色 | 姓名 | 联系方式 | 负责范围 |
|------|------|---------|---------|
| 技术负责人 | [姓名] | [邮箱/电话] | 架构、部署、故障处理 |
| 产品负责人 | [姓名] | [邮箱/电话] | 需求、设计、验收 |
| 开发负责人 | [姓名] | [邮箱/电话] | 代码、功能、bug 修复 |

### 沟通渠道

- **日常沟通**：[Slack / 企微 / 飞书]
- **代码评审**：[GitHub / GitLab]
- **项目管理**：[Jira / Linear / Notion]

---

## 给 Claude 的元规则

### 行为准则

- **默认假设需要测试**：看到用户提出"修一下 X / 加一个 Y / 改 Z 的逻辑"，默认假设需要同步加 / 改测试，并在 commit 里一起带上
- **不要省略测试**：用户没有点头说"不用测试"之前，不要省
- **改完后必须跑测试**：改完后，必须执行一次 `pnpm test:all`（或者至少 `pnpm test:quick`）确认没引入回归再提 commit
- **端到端验证**：新功能必须先打开 PRD 找需求条目，打开 design.md 找页面定义，代码三件套必须配齐
- **不要静默吞错**：catch 块绝不允许静默吞错，必须 `console.error` 或 `showToast`

### 文档维护

- **CLAUDE.md 是活文档**：随项目演进持续更新，记录关键决策、架构变更、已知问题
- **CHANGELOG.md 同步更新**：每次合并 PR 时更新 `[Unreleased]` 部分
- **文档边界清晰**：prd.md = 做什么，design.md = 长什么样，dev.md = 怎么实现，plan.md = 什么时候做

---

## 参考资源

- [项目官网]：https://example.com
- [API 文档]：https://api.example.com/docs
- [设计系统]：https://design.example.com
- [监控面板]：https://monitoring.example.com

---

## 更新日志

| 日期 | 更新内容 | 更新人 |
|------|---------|--------|
| YYYY-MM-DD | 初始化 CLAUDE.md | [姓名] |
| YYYY-MM-DD | 新增自动化测试规则 | [姓名] |
| YYYY-MM-DD | 新增 ADR-001 | [姓名] |

---

**最后更新**：YYYY-MM-DD
