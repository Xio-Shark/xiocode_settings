---
name: prd-manager
version: 2.0.0
description: 统一管理和生成 docs/ 目录下的版本化项目文档。支持从零创建完整项目文档、增量迭代版本、测试驱动开发、PRD↔代码双向验证、运维文档、事故记录、CLAUDE.md 项目记忆体。覆盖项目全生命周期：规划→开发→测试→部署→运维→审计→迭代。
---

# PRD 管理器 v2.0.0

统一管理项目文档的完整生命周期 Skill，覆盖从需求规划到生产运维的全流程。

## 核心能力矩阵

| 能力域 | 覆盖范围 | 核心价值 |
|--------|---------|---------|
| **文档生成** | PRD → Design → Dev → Plan → Ops → Test | 从零产出完整文档链路 |
| **迭代管理** | 版本号决策、增量变更、CHANGELOG | 支持小版本快速迭代 |
| **测试驱动** | 测试策略、静态扫描、部署前检查 | 代码质量保障 |
| **双向验证** | PRD→代码、代码→PRD 审计 | 防止文档与代码脱节 |
| **运维体系** | 部署 SOP、环境变量、故障排查 | 上线后运维支撑 |
| **事故记录** | 问题追踪、根因分析、教训沉淀 | 防止重复踩坑 |
| **项目记忆** | CLAUDE.md 架构决策、开发规范 | AI 协作效率提升 |
| **版本治理** | 查看、对比、搜索、归档 | 历史版本管理 |

---

## 文档边界规范（不变）

每个文档有且只有一个关注点，**严禁跨界**：

| 文档 | 回答的问题 | 不应包含 |
|------|-----------|---------|
| `prd.md` | **做什么、为什么**（功能需求、用户故事、验收标准、业务目标） | 技术选型、架构设计、数据模型、接口定义、文件结构 |
| `design.md` | **长什么样**（页面布局、交互流程、组件清单、视觉规范） | 技术实现方式、组件库选型细节、状态管理方案 |
| `plan.md` | **何时做、谁来做**（任务拆解、时间线、里程碑、风险） | 架构设计、数据模型、接口定义、技术方案对比 |
| `dev.md` | **如何实现**（技术架构、数据模型、接口设计、新增/改动的文件清单、数据库变更、技术方案选型） | 用户故事、验收标准 |
| `ops.md` | **如何部署和运维**（环境变量、部署流程、监控告警、故障排查、回滚） | 功能需求、技术实现细节 |
| `test.md` | **如何验证**（测试策略、单元测试、集成测试、静态扫描、部署前检查） | 功能需求、技术实现细节 |
| `CHANGELOG.md` | **版本间变更**（新增、修改、删除、bug 修复、breaking changes） | 完整的功能描述（应链接到 prd.md） |
| `CLAUDE.md` | **AI 可读的项目总纲**（架构决策、开发规范、已知问题、测试规则） | 具体实现代码、详细 API 文档 |

> **原则**：prd.md 中出现"使用 X 框架"是越界；dev.md 中出现"用户希望..."是越界；plan.md 中出现"数据表字段"是越界。

---

## 目录结构规范

支持两种组织模式，根据项目偏好选择：

### 模式 A：版本目录包含所有文档（默认）

```
docs/prd/
├── README.md       # 版本摘要索引（倒序，最新版本在最上方）
├── v1.5.0/
│   ├── prd.md      # 产品需求文档
│   ├── design.md   # 界面设计文档（前端项目必含）
│   ├── dev.md      # 技术开发文档
│   ├── plan.md     # 开发计划
│   ├── ops.md      # 运维文档（上线功能必含）
│   ├── test.md     # 测试文档
│   ├── CHANGELOG.md # 变更日志（v1.4.x → v1.5.0）
│   ├── sql/        # 数据库变更脚本（新增表或字段时必含）
│   │   ├── DDL.sql     # 表结构变更
│   │   └── DML_init.sql # 初始化数据
│   └── incidents/  # 事故记录（如有）
│       └── 2026-05-02-settlement-bug.md
├── v1.6.0/
│   └── ...
└── _archive/       # 已归档版本
    └── v1.0.0/
```

### 模式 B：按文档类型分目录

```
docs/
├── prd/
│   ├── README.md
│   ├── v1.5.0/
│   │   └── prd.md
│   └── v1.6.0/
│       └── prd.md
├── design/
│   ├── v1.5.0/
│   │   └── design.md
│   └── v1.6.0/
│       └── design.md
├── dev/
│   ├── v1.5.0/
│   │   └── dev.md
│   └── v1.6.0/
│       └── dev.md
├── plan/
│   └── v1.5.0/
│       └── plan.md
├── ops/
│   ├── deployment.md
│   ├── turnstile-setup.md
│   └── usdt-setup.md
└── CLAUDE.md       # 项目记忆体（根目录）
```

> **选择建议**：模式 A 适合版本边界清晰的项目；模式 B 适合文档类型独立演进的项目。Skill 自动检测并适配。

---

## 项目类型差异

根据项目类型，文档侧重点不同：

**前端项目**：
- `design.md` 为必含文档，描述界面设计、交互流程、组件设计
- `dev.md` 侧重前端技术方案（组件结构、状态管理、路由设计）
- `test.md` 包含 UI 测试、可访问性测试

**后端项目**：
- `dev.md` 为核心文档，必须包含「接口影响清单」板块（见下方规范）
- `design.md` 可选，后端通常不需要界面设计
- 涉及数据库变更时必须生成独立 SQL 脚本文件
- `ops.md` 必含环境变量清单、部署流程、监控告警

**全栈项目**：
- 所有文档类型都需要
- `dev.md` 分前后端两个章节
- `ops.md` 包含前后端部署流程

---

## 操作指南

### 0. 从零生成完整文档（新项目 / 大版本）

当用户提出"创建一个 PRD""生成项目文档""给新版本做需求和设计"等需求时，直接使用本 Skill 完成完整工作流：

#### 阶段 1：生成 `prd.md` 并等待确认

1. 收集用户需求、目标用户、优先级和范围
2. 使用 `assets/prd_template.md` 生成 PRD
3. 补全以下核心内容：
   - 项目目标与成功指标
   - 功能列表、优先级、用户故事、验收标准
   - 非功能需求
   - 约束条件与术语说明
4. 保存文件，向用户展示 PRD
5. **明确等待用户确认**，未收到确认前不继续生成后续文档

#### 阶段 2：生成设计与技术文档（用户确认 prd.md 后）

用户确认 PRD 后，生成设计和技术文档，完成后**等待用户确认 dev.md**：

**前端项目**：`design.md` → 项目审查 → `dev.md`

**后端项目**：项目审查 → `dev.md`（含接口影响清单）→ SQL 脚本（如有数据库变更）

**项目审查**（生成 `dev.md` 前必须执行）：

1. 读取项目目录结构，了解整体组织方式
2. 读取配置文件（`package.json`、`go.mod` 等），确认实际技术栈和依赖版本
3. 读取核心入口文件，了解现有架构
4. 检查本次涉及的相关模块现有实现
5. 确认方案与现有代码的命名规范、组织模式一致

> **审查原则**：技术方案必须基于实际代码，而非模板假设。

生成 `dev.md` 后，向用户展示，**等待用户明确确认后再进入下一阶段**。

#### 阶段 3：生成 `plan.md` + `test.md` + `ops.md`（用户确认 dev.md 后）

基于已确认的 `prd.md` 和 `dev.md` 生成配套文档：

1. `plan.md`：使用 `assets/plan_template.md`，仅包含任务拆解、里程碑时间线、负责人、风险与依赖
2. `test.md`：使用 `assets/test_template.md`，定义测试策略、单元测试清单、集成测试场景、静态扫描规则
3. `ops.md`（如有上线功能）：使用 `assets/ops_template.md`，包含环境变量、部署流程、监控告警、故障排查
4. 完成后更新 `docs/prd/README.md` 的版本摘要

> 规则：流程为 `prd.md（确认）→ design/dev（确认）→ plan + test + ops → README 摘要`；prd.md 和 dev.md 两个节点需要用户确认。

### 1. 增量迭代版本（小版本 / 补丁版本）

当用户提出"在 v1.7.7 基础上修复 XX bug""给 v1.7.8 添加 YY 功能"等增量需求时：

#### 1.1 版本号决策

根据变更类型自动建议版本号（遵循语义化版本规范）：

| 变更类型 | 版本号变化 | 示例 | 触发条件 |
|---------|-----------|------|---------|
| **Major** | v1.x.x → v2.0.0 | 架构重构、破坏性变更、核心模型变更 | 不兼容旧版本 |
| **Minor** | v1.7.x → v1.8.0 | 新增功能、新增模块、新增 API | 向后兼容 |
| **Patch** | v1.7.7 → v1.7.8 | bug 修复、性能优化、小改进 | 向后兼容 |

**决策流程**：
1. 读取当前最新版本号
2. 询问用户变更类型（或根据描述自动判断）
3. 建议新版本号，等待用户确认
4. 创建新版本目录

#### 1.2 增量文档生成

**原则**：只更新受影响的文档，不重新生成所有文档。

1. **必须更新**：
   - `CHANGELOG.md`：记录本次变更（新增、修改、删除、bug 修复）
   - `dev.md`：如有代码变更，更新文件变更清单、接口影响清单
   - `test.md`：如有新功能或 bug 修复，更新测试用例

2. **按需更新**：
   - `prd.md`：如有新需求或需求变更
   - `design.md`：如有 UI 变更
   - `ops.md`：如有环境变量、部署流程变更
   - `plan.md`：如有时间线调整

3. **自动生成**：
   - `CHANGELOG.md`：对比上一版本，自动生成变更摘要

**示例**：
```
用户：在 v1.7.7 基础上修复 settlement_failed 少退款 bug
Skill：
  1. 建议版本号 v1.7.8（patch）
  2. 创建 docs/prd/v1.7.8/ 或 docs/dev/v1.7.8/
  3. 生成 CHANGELOG.md：记录 bug 修复
  4. 更新 dev.md：文件变更清单（task.service.ts）
  5. 更新 test.md：新增回归测试用例
  6. 不更新 prd.md（需求未变）
```

#### 1.3 CHANGELOG 生成规则

使用 `assets/changelog_template.md`，自动对比上一版本：

```markdown
# v1.7.8 变更日志

**发布日期**：2026-05-03
**基于版本**：v1.7.7

## 🐛 Bug 修复

- **settlement_failed 少退款漏洞**：`handleT1Exhausted` 未 decrement slot_taken，导致 group 过期时少退款
  - 影响文件：`apps/api/src/modules/task/task.service.ts`
  - 修复方式：在 `handleT1Exhausted` 中添加 `slotTaken -= 1` + `ledger.unlock`
  - 相关 PR：#123

## 🧪 测试

- 新增回归测试：`settlement_failed` 场景的退款验证

## 📝 文档

- 更新 `CLAUDE.md`：补充 settlement_failed 处理逻辑
```

### 2. 测试驱动闭环

每个版本必须定义可执行的测试策略，确保代码质量和部署安全。

#### 2.1 测试文档生成

使用 `assets/test_template.md` 生成 `test.md`，包含：

1. **测试策略**：单元测试覆盖率目标、集成测试场景、E2E 测试范围
2. **单元测试清单**：每个 PRD 需求对应的测试用例
3. **集成测试场景**：跨模块、跨服务的测试场景
4. **静态扫描规则**：代码规范、安全漏洞、性能问题
5. **部署前检查清单**：必须通过的检查项

#### 2.2 静态扫描脚本

为每个版本生成或更新静态扫描脚本（如 `scripts/comprehensive-test.mjs`），包含：

1. **PRD 覆盖率检查**：验证代码是否实现了 PRD 中的所有需求
2. **字段约束验证**：验证 DTO 字段长度、类型、必填项
3. **安全检查**：验证 auth guard、input sanitization、SQL injection 防护
4. **计算准确性**：验证金额计算、费率计算、精度处理
5. **文档一致性**：验证前端文案与设计文档一致

**示例**：
```javascript
// scripts/comprehensive-test.mjs 片段
section('§1 PRD Coverage Check');
const prdFile = readFile('docs/prd/v1.7.8/prd.md');
const requirements = extractRequirements(prdFile);
for (const req of requirements) {
  const implemented = checkImplementation(req);
  implemented ? pass(`需求 ${req.id} 已实现`) : fail(`需求 ${req.id} 未实现`);
}
```

#### 2.3 部署前检查清单

每个版本的 `test.md` 必须包含部署前检查清单：

- [ ] 所有单元测试通过（`pnpm test`）
- [ ] 所有集成测试通过（`pnpm test:integration`）
- [ ] 静态扫描无 critical 错误（`node scripts/comprehensive-test.mjs`）
- [ ] 代码审查完成
- [ ] 环境变量已配置（对照 `ops.md`）
- [ ] 数据库迁移脚本已验证（如有）
- [ ] 回滚方案已准备

#### 2.4 测试与代码同步规则

**强制规则**：任何代码变更必须同步更新测试。

| 代码变更类型 | 必须同步的测试 |
|-------------|---------------|
| 新增功能 | 新增单元测试 + 集成测试 + 更新 `test.md` |
| Bug 修复 | 新增回归测试 + 更新 `test.md` |
| 重构 | 确保现有测试通过 + 更新测试文档 |
| API 变更 | 更新接口测试 + 更新 `test.md` |
| 数据库变更 | 新增迁移测试 + 更新 `test.md` |

**检查方式**：静态扫描脚本验证每个 service/controller 是否有对应的测试文件。

### 3. PRD ↔ 代码双向验证

防止 PRD 与代码脱节，建立双向验证机制。

#### 3.1 正向验证：PRD → 代码

**目标**：确保 PRD 中的每个需求都有对应的代码实现。

**实现方式**：
1. 在 `test.md` 中为每个 PRD 需求定义验收测试
2. 静态扫描脚本读取 `prd.md`，提取需求列表
3. 检查每个需求是否有对应的：
   - 代码文件（根据 `dev.md` 的文件变更清单）
   - 测试用例（根据 `test.md` 的测试清单）
   - API 端点（根据 `dev.md` 的接口影响清单）

**示例**：
```javascript
// scripts/audit-feature-completeness.mjs
const prd = readPRD('docs/prd/v1.7.8/prd.md');
const dev = readDev('docs/dev/v1.7.8/dev.md');
const test = readTest('docs/test/v1.7.8/test.md');

for (const requirement of prd.requirements) {
  const hasCode = dev.fileChanges.some(f => f.relates(requirement.id));
  const hasTest = test.testCases.some(t => t.covers(requirement.id));
  const hasAPI = dev.apiChanges.some(a => a.implements(requirement.id));
  
  if (!hasCode || !hasTest || !hasAPI) {
    fail(`需求 ${requirement.id} 未完整实现`);
  }
}
```

#### 3.2 反向验证：代码 → PRD

**目标**：确保代码中的每个功能都有 PRD 依据。

**实现方式**：
1. 扫描代码中的新增 controller/service/API
2. 检查是否在 `dev.md` 的接口影响清单中
3. 检查是否在 `prd.md` 中有对应需求
4. 检查是否在 `test.md` 中有对应测试

**示例**：
```javascript
// scripts/audit-code-coverage.mjs
const controllers = scanControllers('apps/api/src/modules/');
const dev = readDev('docs/dev/v1.7.8/dev.md');
const prd = readPRD('docs/prd/v1.7.8/prd.md');

for (const controller of controllers) {
  const inDev = dev.apiChanges.includes(controller.endpoint);
  const inPRD = prd.requirements.some(r => r.covers(controller.feature));
  
  if (!inDev || !inPRD) {
    warn(`API ${controller.endpoint} 缺少 PRD 依据`);
  }
}
```

#### 3.3 审计脚本清单

每个项目应包含以下审计脚本（放在 `scripts/` 目录）：

| 脚本 | 用途 | 检查内容 |
|------|------|---------|
| `audit-feature-completeness.mjs` | PRD 覆盖率 | PRD 需求是否都有代码实现 |
| `audit-db-indexes.mjs` | 数据库规范 | 表结构、索引、字段类型、精度 |
| `audit-security-perf.mjs` | 安全与性能 | 硬编码密钥、SQL 注入、N+1 查询 |
| `comprehensive-test.mjs` | 综合检查 | 字段约束、计算准确性、文档一致性 |

**集成到 CI/CD**：
```yaml
# .github/workflows/ci.yml
- name: Run audits
  run: |
    node scripts/audit-feature-completeness.mjs
    node scripts/audit-db-indexes.mjs
    node scripts/audit-security-perf.mjs
    node scripts/comprehensive-test.mjs
```

### 4. 运维文档体系

每个上线功能必须有对应的运维文档，确保部署和运维的可操作性。

#### 4.1 运维文档生成

使用 `assets/ops_template.md` 生成 `ops.md`，包含：

1. **环境变量清单**：前后端所有环境变量、默认值、必填项、获取方式
2. **部署流程 SOP**：从零部署到生产的完整步骤
3. **监控告警**：关键指标、告警阈值、告警渠道
4. **故障排查**：常见问题、排查步骤、解决方案
5. **回滚方案**：回滚步骤、数据恢复、影响范围

#### 4.2 环境变量管理

**原则**：所有环境变量必须在 `ops.md` 中文档化。

**格式**：
```markdown
## 环境变量清单

### 后端（NestJS）

| 变量名 | 必填 | 默认值 | 说明 | 获取方式 |
|--------|------|--------|------|---------|
| `DATABASE_URL` | ✅ | - | PostgreSQL 连接字符串 | Supabase 控制台 |
| `TURNSTILE_SECRET_KEY` | ✅ | - | Cloudflare Turnstile Secret Key | https://dash.cloudflare.com/ → Turnstile |
| `NODE_ENV` | ✅ | `development` | 运行环境 | 手动设置 |

### 前端（Next.js）

| 变量名 | 必填 | 默认值 | 说明 | 获取方式 |
|--------|------|--------|------|---------|
| `NEXT_PUBLIC_TURNSTILE_SITE_KEY` | ✅ | - | Cloudflare Turnstile Site Key（构建时注入） | https://dash.cloudflare.com/ → Turnstile |
| `NEXT_PUBLIC_API_URL` | ✅ | - | API 基础 URL | 手动设置 |
```

**检查方式**：静态扫描脚本验证代码中使用的环境变量是否都在 `ops.md` 中文档化。

#### 4.3 部署流程 SOP

**原则**：部署流程必须可复现、可自动化、可回滚。

**格式**：
```markdown
## 部署流程

### 前置条件

- [ ] 所有测试通过
- [ ] 代码已合并到 main 分支
- [ ] 环境变量已配置
- [ ] 数据库迁移脚本已准备

### 部署步骤

1. **构建**：`bash scripts/deploy-local-build.sh`
2. **上传**：自动上传到服务器
3. **迁移**：`npx prisma migrate deploy`（如有数据库变更）
4. **重启**：`pm2 restart xripple-api && pm2 restart xripple-web`
5. **验证**：访问 `https://api.xripple.app/health` 确认 200

### 回滚步骤

1. **代码回滚**：`git revert <commit-hash> && git push`
2. **重新部署**：`bash scripts/deploy-local-build.sh`
3. **数据库回滚**（如有）：执行回滚 SQL 脚本
4. **验证**：确认服务恢复正常
```

#### 4.4 故障排查手册

**原则**：常见问题必须有明确的排查步骤和解决方案。

**格式**：
```markdown
## 故障排查

### 问题 1：用户无法领取任务，提示"领取失败，请重试"

**排查步骤**：
1. 检查后端日志：`sudo pm2 logs xripple-api --err --lines 100`
2. 查找 POST /api/v1/slots 请求，查看具体错误
3. 常见原因：
   - Turnstile 验证失败（token 过期或重复使用）
   - 用户不满足领取条件（粉丝数、认证状态）
   - 名额已满

**解决方案**：
- 如果是 Turnstile 问题：提示用户刷新页面重试
- 如果是条件不满足：返回具体原因给用户
- 如果是名额已满：正常业务逻辑
```

### 5. 事故记录与回溯

生产环境发现的问题必须记录，防止重复踩坑。

#### 5.1 事故记录生成

使用 `assets/incident_template.md` 生成事故记录，放在 `docs/prd/<version>/incidents/` 或 `docs/incidents/`。

**命名规范**：`YYYY-MM-DD-<简短描述>.md`，如 `2026-05-02-settlement-bug.md`

**内容结构**：
```markdown
# 事故记录：settlement_failed 少退款漏洞

**发现时间**：2026-05-02 23:00
**影响范围**：生产环境，1 个用户，损失 0.6 USDT
**严重程度**：P1（资金安全）
**状态**：✅ 已修复

## 问题描述

`verify.processor.ts` 的 `onFailed` handler 在 BullMQ attempts 用尽时，只 log 不退款，导致 slot 永远 locked。

## 根因分析

1. `onFailed` 是异步回调，但旧实现只有 `logger.error`，没有调用 `releaseSlotAsExhausted`
2. `TOKEN_REFRESH_FAILED` 异常未被识别，导致 BullMQ 重试 3 次（每次都失败）
3. Group 关闭时，`token_suspended` slot 未被同步清理，钱白锁 7 天等 recycle

## 修复方案

1. `onFailed` 改为 async，调用 `releaseSlotAsExhausted`
2. `verify.processor` catch 块识别 `TOKEN_REFRESH_FAILED`，直接 release
3. `task.service` 新增 `releaseSuspendedSlotsOnGroupClose`，在 group 关闭事务里同步清理

## 影响范围

- 受影响用户：1 个（已手动补退 0.6 USDT）
- 受影响版本：v1.7.7 及之前
- 修复版本：v1.7.8

## 教训

1. **异步回调必须有兜底逻辑**：BullMQ 的 `onFailed` 是最后一道防线
2. **资金相关路径必须有完整测试**：回归测试覆盖所有失败路径
3. **告警必须走正确渠道**：敏感数据不能走公开 TG/企微

## 相关文档

- PRD：`docs/prd/v1.7.8/prd.md`
- 修复 PR：#123
- 回归测试：`apps/api/src/integration-tests/slots-oversell.integration.spec.ts`
```

#### 5.2 事故驱动的文档更新

每个事故修复后，必须同步更新以下文档：

1. **CHANGELOG.md**：记录 bug 修复
2. **test.md**：新增回归测试用例
3. **CLAUDE.md**：补充架构决策、已知问题、注意事项
4. **ops.md**：如有运维相关，更新故障排查手册

#### 5.3 事故分类与优先级

| 严重程度 | 定义 | 响应时间 | 示例 |
|---------|------|---------|------|
| **P0** | 服务不可用、数据丢失 | 立即 | 数据库崩溃、API 全部 500 |
| **P1** | 资金安全、核心功能异常 | 2 小时内 | 少退款、多扣款、支付失败 |
| **P2** | 非核心功能异常 | 24 小时内 | 通知未发送、UI 显示错误 |
| **P3** | 体验问题、性能问题 | 1 周内 | 加载慢、文案错误 |

### 6. CLAUDE.md 项目记忆体

CLAUDE.md 是 AI 可读的项目总纲，承载架构决策、开发规范、已知问题、测试规则等。

#### 6.1 CLAUDE.md 生成

使用 `assets/claude_template.md` 生成 `CLAUDE.md`，放在项目根目录。

**内容结构**：
```markdown
# CLAUDE.md

本文档为 AI 助手提供项目上下文，包含架构决策、开发规范、已知问题、测试规则。

## 项目简介

[一句话描述项目]

## 核心文档

| 文档 | 路径 | 内容 |
|------|------|------|
| PRD | `docs/prd/v1.7.8/prd.md` | 功能需求与验收标准 |
| 设计 | `docs/design/v1.7.8/design.md` | 页面设计与交互流程 |
| 技术 | `docs/dev/v1.7.8/dev.md` | 架构、数据模型、API 设计 |
| 运维 | `docs/ops/deployment.md` | 部署流程与故障排查 |

## 技术栈

[列出实际使用的技术栈和版本]

## 架构决策记录（ADR）

### ADR-001：X OAuth Token 自动续期

**背景**：X OAuth access_token 默认 2h 过期，但 verify 是异步的（领取 + 60min），到 verify 时 token 几乎必然过期。

**决策**：`xapi.getValidUserAccessToken(userId)` 自动续期 + phase1 验证结果即最终结果。

**理由**：
- 距过期 > 5min：直接返回当前 token
- 距过期 < 5min 或已过期：用 refresh_token 拿新 token
- refresh_token 也失效：清空 DB tokens + throw TOKEN_REFRESH_FAILED

**影响**：
- T+1 批处理不再调用 X API 二次验证
- phase1 验证失败的 slot 直接释放

### ADR-002：资金锁释放规则

**背景**：任务到期只退「未领取部分」，已被领取的 slot 如果落到失败分支，钱必须由各分支自己同步 unlock。

**决策**：12 条退款路径全景图（task.service.ts:46 顶部注释为唯一权威）。

**理由**：group 已结束后没人会再接手该 slot，钱永远锁。

**影响**：
- phase1 verify 失败：group closed 时事务内 unlock
- TOKEN_REFRESH_FAILED：直接 release
- BullMQ attempts 用尽：onFailed async + 兜底 release
- group 关闭时清挂起：releaseSuspendedSlotsOnGroupClose

## 开发规范

### 代码规范

- 任何对功能逻辑的新增/修改/删除，必须在同一个 commit 内同步更新对应的自动化测试
- 涉及资金的逻辑必须 100% 确认后才能修改
- 所有余额变动必须通过 LedgerService（原子事务）

### 测试规范

- 单元测试：每个 service/controller 必须有对应的 spec 文件
- 集成测试：资金相关、并发相关必须有集成测试
- 静态扫描：`pnpm test:all` 包含 lint + typecheck + 单测 + 集成 + 静态扫描

### Git 规范

- 只创建新 commit，不 amend（除非 pre-commit hook 失败）
- 提交信息格式：`feat/fix/refactor: 简短描述`
- 部署前必须：`pnpm test:all` 全绿

## 已知问题

### 问题 1：Turnstile token 只能使用一次

**现象**：用户多次尝试领取任务，返回"人机验证失败"。

**原因**：Turnstile token 是一次性的，用过就失效。

**解决**：刷新页面重新生成 token。

## 测试规则

### 部署前检查清单

- [ ] `pnpm test:all` 全绿
- [ ] 环境变量已配置（对照 ops.md）
- [ ] 数据库迁移脚本已验证
- [ ] 回滚方案已准备

### 静态扫描规则

- PRD 覆盖率：所有需求都有代码实现
- 字段约束：DTO 字段长度、类型、必填项
- 安全检查：auth guard、input sanitization
- 计算准确性：金额计算、费率计算
```

#### 6.2 CLAUDE.md 更新规则

**触发时机**：
1. 新增架构决策（如选择技术方案、设计模式）
2. 发现生产问题并修复（补充已知问题）
3. 新增开发规范（如代码规范、测试规范）
4. 新增测试规则（如静态扫描规则）

**更新方式**：
- 架构决策：追加 ADR-XXX 章节
- 已知问题：追加问题描述 + 解决方案
- 开发规范：更新对应章节
- 测试规则：更新对应章节

#### 6.3 CLAUDE.md 与其他文档的关系

| 文档 | 关系 | 示例 |
|------|------|------|
| `prd.md` | CLAUDE.md 不重复 PRD 内容，只链接 | "功能需求见 prd.md" |
| `dev.md` | CLAUDE.md 记录架构决策，dev.md 记录实现细节 | ADR vs 文件变更清单 |
| `ops.md` | CLAUDE.md 记录运维注意事项，ops.md 记录操作步骤 | "注意 X" vs "执行 Y" |
| `test.md` | CLAUDE.md 记录测试规则，test.md 记录测试用例 | "必须测试 X" vs "测试用例 Y" |

### 7. 版本治理（保留原有功能）

#### 7.1 初始化

当 `docs/prd/` 目录不存在时，先引导用户初始化：

1. 提示用户 PRD 目录尚不存在
2. 创建 `docs/prd/` 目录
3. 建议从 `v0.1.0` 开始，或由用户指定版本号
4. 继续执行创建版本流程

#### 7.2 列出版本

```bash
ls -la docs/prd/
```

展示汇总信息（语义化排序），包含状态总览：

```
📊 PRD 状态总览
────────────────────
v1.7.8  🔄 进行中    3 个需求  (P0:1 P1:2)
v1.7.7  ✅ 已完成    2 个 bug 修复
v1.6.0  ✅ 已完成    5 个需求  (P0:2 P1:2 P2:1)
────────────────────
共 3 个版本 | 1 个归档
```

#### 7.3 查看结构

```bash
find docs/prd/<version> -name "*.md" | sort
```

汇总存在的文档及其用途。

#### 7.4 创建版本

1. 确定版本号（根据现有版本自动建议下一个语义化版本）
2. **冲突检测**：若 `docs/prd/<version>/` 已存在，提示用户选择：覆盖 / 换版本号 / 取消
3. 创建目录：`mkdir -p docs/prd/<version>`
4. 生成文档（默认至少生成 `prd.md`；前端项目补 `design.md`，后端项目补 `dev.md`，完整模式下再生成 `plan.md` + `test.md` + `ops.md`）
5. 从 `assets/` 目录加载对应模板，填入用户提供的上下文
6. 更新 `docs/prd/README.md` 中的版本摘要，采用倒序排列，最新版本放在最上方
7. 保存文件并确认位置

#### 7.5 扩展版本

1. 读取现有的 prd.md
2. 追加新需求章节（使用用户故事格式）
3. 如需则更新 plan.md、design.md、dev.md、test.md、ops.md
4. 若版本摘要发生变化，同步更新 `docs/prd/README.md`

#### 7.6 对比版本

读取两个版本的文档，生成结构化对比：

```
版本对比: v1.7.7 vs v1.7.8
─────────────────────────────
新增需求:
  无

Bug 修复:
  + settlement_failed 少退款漏洞

文件变更:
  M apps/api/src/modules/task/task.service.ts
  M apps/api/src/modules/verify/verify.processor.ts

测试变更:
  + 新增回归测试：settlement_failed 场景

优先级变更:
  无

时间线变更:
  无
```

也可使用 `git diff docs/prd/<version-a>/prd.md docs/prd/<version-b>/prd.md` 进行原始对比。

#### 7.7 归档版本

1. 确认要归档的版本号
2. 创建归档目录（如不存在）：`mkdir -p docs/prd/_archive/`
3. 移动版本：`mv docs/prd/<version> docs/prd/_archive/<version>`
4. 更新 `docs/prd/README.md`，移除或调整对应版本摘要
5. 确认归档完成

#### 7.8 跨版本搜索

```bash
grep -r "<关键词>" docs/prd/ --include="*.md" -l
```

展示匹配的版本和文件列表。

#### 7.9 更新版本摘要 README

每当新增、扩展、归档版本后，都要同步维护 `docs/prd/README.md`。

要求如下：

1. **采用倒序排列**：最新版本必须放在最上面
2. **摘要信息精简清晰**：每个版本至少包含版本号、状态、日期、核心变更摘要
3. **路径可点击**：摘要中应链接到对应版本目录或核心文档
4. **归档版本单独分组**：如需展示历史归档版本，放在 README 下方单独区块

推荐格式示例：

```md
# PRD 版本索引

## 当前版本

- `v1.7.8`｜🔄 进行中｜2026-05-03
  - 摘要：修复 settlement_failed 少退款漏洞
  - 文档：[`dev.md`](./v1.7.8/dev.md) / [`CHANGELOG.md`](./v1.7.8/CHANGELOG.md) / [`test.md`](./v1.7.8/test.md)

- `v1.7.7`｜✅ 已完成｜2026-05-01
  - 摘要：资金安全修复 + 待结算佣金列
  - 文档：[`dev.md`](./v1.7.7/dev.md) / [`CHANGELOG.md`](./v1.7.7/CHANGELOG.md)

## 已归档

- `v1.0.0`｜✅ 已归档
  - 文档：[`archive`](./_archive/v1.0.0/)
```

---

## AI 协作规范

### 对话流程设计

#### 1. 项目初始化流程

```
用户：我想做一个任务众包平台
AI：
  → 询问：项目名称？技术栈（前端/后端框架）？初始版本号（默认 v0.1.0）？
  → 用户回答后
  → 询问：核心功能模块有哪些？优先级如何？
  → 用户回答后
  → 生成 prd.md
  → 展示并明确等待确认："请确认 PRD 是否符合预期，确认后我会继续生成设计和技术文档"
  → 用户确认后
  → 项目审查（读取现有代码）
  → 生成 design.md（前端）/ dev.md
  → 展示并明确等待确认："请确认技术方案是否可行，确认后我会生成开发计划和测试文档"
  → 用户确认后
  → 生成 plan.md + test.md + ops.md + CHANGELOG.md + CLAUDE.md
  → 更新 README.md
  → 提醒："⚠️ 根据测试驱动原则，开发时必须同步写测试，部署前必须执行 pnpm test:all"
```

#### 2. 功能迭代流程

```
用户：在 v1.7.7 基础上修复 XX bug
AI：
  → 识别变更类型：bug 修复 → patch 版本
  → 建议版本号：v1.7.8
  → 询问：bug 的具体表现？影响范围？根因是什么？
  → 用户回答后
  → 生成 CHANGELOG.md（记录 bug 修复）
  → 更新 dev.md（文件变更清单）
  → 更新 test.md（回归测试用例）
  → 提醒："⚠️ 必须新增回归测试，防止此 bug 再次出现"
  → 提醒："⚠️ 如果是生产事故，建议记录到 incidents/"
```

#### 3. 需求不明确时的追问

```
用户：我想加个登录功能
AI：
  → 追问："登录方式是什么？（账号密码 / 手机验证码 / 第三方 OAuth）"
  → 追问："是新版本还是在现有版本上迭代？"
  → 追问："有什么特殊要求？（如首次登录强制改密、异常登录提醒）"
  → 用户回答后
  → 继续正常流程
```

### 确认机制

| 阶段 | 确认类型 | 说明 |
|------|---------|------|
| `prd.md` 生成后 | **强制确认** | 必须用户明确确认才能继续 |
| `dev.md` 生成后 | **强制确认** | 必须用户明确确认才能继续 |
| `plan.md` / `test.md` / `ops.md` | **可选确认** | 可批量生成，用户有异议再调整 |
| `CHANGELOG.md` / `CLAUDE.md` | **自动更新** | 无需确认，自动维护 |

**确认话术示例**：
- "请确认 PRD 是否符合预期，确认后我会继续生成设计和技术文档"
- "请确认技术方案是否可行，确认后我会生成开发计划和测试文档"
- "已生成所有文档，请检查是否有遗漏或需要调整的地方"

### 质量门禁

#### 拒绝场景（必须阻止）

| 场景 | AI 行为 | 话术示例 |
|------|---------|---------|
| 用户要求跳过测试 | **拒绝** | "根据测试驱动原则，任何代码变更必须同步更新测试。跳过测试会导致代码质量无法保障，建议先写测试再写代码。" |
| 用户提供的需求过于模糊 | **拒绝并追问** | "需求描述不够清晰，我需要了解：1. 用户角色是谁？2. 核心流程是什么？3. 有什么业务规则？" |
| 用户要求直接改代码不更新文档 | **拒绝** | "根据 PRD 驱动原则，代码变更前必须先更新 prd.md 或 dev.md。文档与代码脱节会导致后续维护困难。" |
| 涉及资金的逻辑未经确认就修改 | **拒绝** | "涉及资金的逻辑必须 100% 确认后才能修改。请先明确：1. 变更的具体逻辑？2. 影响范围？3. 测试方案？" |

#### 警告场景（提醒但允许）

| 场景 | AI 行为 | 话术示例 |
|------|---------|---------|
| 后端项目跳过 design.md | **警告但允许** | "后端项目通常不需要 design.md，但如果有管理后台或 API 文档页面，建议补充。" |
| 开发阶段跳过 ops.md | **警告但允许** | "开发阶段可以暂时跳过 ops.md，但上线前必须补充，否则部署和运维会遇到困难。" |
| 未记录生产事故 | **警告** | "建议将此问题记录到 incidents/，防止重复踩坑。" |

### 强制规则执行

#### 规则 1：测试驱动

**触发时机**：每次生成 dev.md 后

**AI 行为**：
```
⚠️ 测试驱动提醒：
1. 任何代码变更必须同步更新测试
2. 部署前必须执行 pnpm test:all 确保全绿
3. 新增功能必须有单元测试 + 集成测试
4. Bug 修复必须有回归测试
```

#### 规则 2：PRD 驱动

**触发时机**：用户要求直接改代码时

**AI 行为**：
```
⚠️ PRD 驱动提醒：
1. 代码变更前必须先更新 prd.md 或 dev.md
2. 确保文档与代码保持一致
3. 如果是 bug 修复，更新 CHANGELOG.md
```

#### 规则 3：端到端验证

**触发时机**：部署前

**AI 行为**：
```
⚠️ 部署前检查清单：
- [ ] pnpm test:all 全绿
- [ ] 环境变量已配置（对照 ops.md）
- [ ] 数据库迁移脚本已验证
- [ ] 回滚方案已准备
- [ ] 本地起服务 → seed 真实数据 → 走一遍 happy path + edge cases
```

### 自检清单

#### prd.md 生成后自检

AI 在生成 prd.md 后，自动检查以下项：

- [ ] 是否明确了用户角色和使用场景？
- [ ] 是否定义了验收标准？
- [ ] 是否标注了优先级（P0/P1/P2）？
- [ ] 是否避免了技术实现细节？
- [ ] 是否包含成功指标？

**如有缺失**：主动补充或提醒用户补充

#### dev.md 生成后自检

- [ ] 是否包含了数据库 Schema 变更？
- [ ] 是否列出了 API 接口影响清单（后端项目必须）？
- [ ] 是否考虑了向后兼容性？
- [ ] 是否避免了业务需求描述？
- [ ] 是否基于实际代码（而非模板假设）？

**如有缺失**：主动补充或提醒用户补充

#### test.md 生成后自检

- [ ] 是否定义了测试策略（单元/集成/E2E）？
- [ ] 是否为每个 PRD 需求定义了测试用例？
- [ ] 是否包含部署前检查清单？
- [ ] 是否定义了测试覆盖率目标？

**如有缺失**：主动补充或提醒用户补充

#### ops.md 生成后自检

- [ ] 是否列出了所有环境变量？
- [ ] 是否包含完整的部署流程？
- [ ] 是否包含故障排查手册？
- [ ] 是否包含回滚方案？

**如有缺失**：主动补充或提醒用户补充

#### plan.md 生成后自检

- [ ] 是否包含任务拆解（每个任务有明确的负责人和截止日期）？
- [ ] 是否包含里程碑时间线？
- [ ] 是否标注了任务状态（⏳ 规划中 | 🔄 进行中 | ✅ 已完成）？
- [ ] 是否识别了风险与依赖？
- [ ] 是否避免了技术实现细节（应在 dev.md）？

**如有缺失**：主动补充或提醒用户补充

#### CHANGELOG.md 生成后自检

- [ ] 是否明确了版本号和发布日期？
- [ ] 是否使用了正确的变更类型（Added/Changed/Fixed/Deprecated/Removed/Security）？
- [ ] 是否包含了所有本次变更（对比上一版本）？
- [ ] 是否链接到相关 PR 或 issue？
- [ ] 破坏性变更是否有迁移指南？

**如有缺失**：主动补充或提醒用户补充

#### CLAUDE.md 生成后自检

- [ ] 是否包含项目简介和技术栈？
- [ ] 是否包含核心文档路径？
- [ ] 是否包含架构决策记录（ADR）？
- [ ] 是否包含开发规范和测试规则？
- [ ] 是否包含给 AI 的元规则？

**如有缺失**：主动补充或提醒用户补充

### 错误处理

#### 版本号冲突

**场景**：用户要求创建的版本号已存在

**AI 行为**：
```
⚠️ 版本冲突：docs/prd/v1.7.8/ 已存在

请选择：
1. 覆盖现有版本（⚠️ 会丢失现有内容）
2. 使用新版本号（建议：v1.7.9）
3. 取消操作

请输入选项（1/2/3）：
```

**用户选择后**：
- 选项 1：再次确认 "确认覆盖 v1.7.8？此操作不可逆。（输入 YES 确认）"
- 选项 2：使用新版本号继续
- 选项 3：取消操作

#### 信息不完整

**场景**：用户提供的信息不足以生成文档

**AI 行为**：
```
⚠️ 信息不完整，无法生成文档

缺少以下信息：
- [ ] 项目名称
- [ ] 技术栈
- [ ] 核心功能模块

请补充上述信息后重试。
```

#### 文档生成失败

**场景**：模板文件缺失或读取失败

**AI 行为**：
```
❌ 文档生成失败：assets/prd_template.md 不存在

请检查：
1. Skill 目录是否完整？
2. assets/ 目录下是否有所有模板文件？

如果问题持续，请重新安装 Skill。
```

### 常见问题（FAQ）

#### Q1：后端项目需要生成 design.md 吗？

**A**：通常不需要。后端项目的核心是 dev.md（技术架构、API 设计）。但如果有管理后台或 API 文档页面，可以补充 design.md。

**AI 行为**：警告但允许跳过

#### Q2：开发阶段可以跳过 ops.md 吗？

**A**：可以暂时跳过，但上线前必须补充。ops.md 包含环境变量、部署流程、故障排查，缺少会导致部署和运维困难。

**AI 行为**：警告但允许跳过

#### Q3：如何处理破坏性变更？

**A**：
1. 版本号升级到 Major（如 v1.x.x → v2.0.0）
2. 在 CHANGELOG.md 中明确标注 "⚠️ Breaking Changes"
3. 提供迁移指南（如 API 变更、数据库迁移）
4. 在 CLAUDE.md 中记录架构决策（为什么要做破坏性变更）

#### Q4：如何处理多人协作？

**A**：
1. 每个人在自己的分支上工作
2. 文档变更通过 PR 合并到 main
3. 版本号由团队统一管理（避免冲突）
4. CLAUDE.md 记录团队协作规范

#### Q5：如何处理历史版本的 bug？

**A**：
1. 在当前最新版本基础上修复（patch 版本）
2. 如果需要修复历史版本，创建新的 patch 版本（如 v1.7.8 → v1.7.9）
3. 不建议修改已归档的版本

#### Q6：用户中途改需求怎么办？

**AI 行为**：
```
用户：我想改一下 prd.md 的需求

AI：好的，请问：
    1. 是修改现有需求，还是新增需求？
    2. 如果是修改，是否需要更新版本号？（建议：需求变更 → Minor 版本）
    3. 如果是新增，优先级是什么？

用户回答后：
    → 更新 prd.md
    → 同步更新 dev.md（如有技术方案变更）
    → 同步更新 test.md（如有测试用例变更）
    → 更新 CHANGELOG.md
```

#### Q7：如何删除某个版本？

**AI 行为**：
```
用户：删除 v1.7.8

AI：⚠️ 删除版本是危险操作，建议归档而非删除。

请选择：
1. 归档到 _archive/（推荐）
2. 彻底删除（⚠️ 不可恢复）
3. 取消操作

请输入选项（1/2/3）：
```

**用户选择后**：
- 选项 1：移动到 _archive/
- 选项 2：再次确认 "确认删除 v1.7.8？此操作不可逆。（输入 YES 确认）"
- 选项 3：取消操作

#### Q8：如何修改已归档的版本？

**AI 行为**：
```
用户：修改 _archive/v1.0.0/prd.md

AI：⚠️ 不建议修改已归档的版本。

建议方案：
1. 如果是修复历史 bug，在当前版本创建新的 patch 版本
2. 如果是补充文档，可以修改归档版本，但需要在 CHANGELOG.md 中说明

是否继续修改归档版本？（y/n）
```

### 示例对话

#### 示例 1：项目初始化（完整流程）

```
用户：我想做一个任务众包平台，类似 XRipple

AI：好的，我需要先了解几个问题：
    1. 项目名称是什么？
    2. 技术栈是什么？（前端框架 / 后端框架 / 数据库）
    3. 初始版本号？（默认 v0.1.0）

用户：项目名 TaskHub，Next.js + NestJS + PostgreSQL，版本 v0.1.0

AI：明白了。接下来请描述核心功能模块和优先级：
    - 有哪些核心功能？（如用户认证、任务发布、任务领取、支付结算）
    - 哪些是 P0（必须有）、P1（重要）、P2（可选）？

用户：P0 是用户认证（X OAuth）+ 任务发布 + 任务领取，P1 是支付结算，P2 是推广分佣

AI：收到。我现在生成 prd.md...
    [生成 prd.md]
    
    已生成 PRD 文档，包含：
    - 项目目标与成功指标
    - 功能列表（P0: 3 个，P1: 1 个，P2: 1 个）
    - 用户故事与验收标准
    - 非功能需求
    
    请确认 PRD 是否符合预期，确认后我会继续生成设计和技术文档。

用户：确认

AI：好的。我先审查一下项目现有代码...
    [读取 package.json、tsconfig.json、目录结构]
    
    已完成项目审查，现在生成技术文档...
    [生成 design.md（前端）和 dev.md]
    
    已生成：
    - design.md：页面结构、交互流程、组件清单
    - dev.md：技术架构、数据模型（5 张表）、API 设计、文件变更清单
    
    请确认技术方案是否可行，确认后我会生成开发计划和测试文档。

用户：确认

AI：好的。现在生成配套文档...
    [生成 plan.md + test.md + ops.md + CHANGELOG.md + CLAUDE.md]
    [更新 docs/prd/README.md]
    
    已完成所有文档生成：
    - plan.md：4 周开发计划，10 个任务
    - test.md：测试策略、单元测试清单、部署前检查清单
    - ops.md：环境变量、部署流程、监控告警
    - CHANGELOG.md：v0.1.0 初始版本
    - CLAUDE.md：项目记忆体，包含架构决策、开发规范
    
    ⚠️ 重要提醒：
    1. 开发时必须同步写测试（测试驱动原则）
    2. 部署前必须执行 pnpm test:all 确保全绿
    3. 涉及资金的逻辑必须 100% 确认后才能修改
    
    文档已保存到 docs/prd/v0.1.0/，可以开始开发了。
```

#### 示例 2：功能迭代（增量变更）

```
用户：在 v1.7.7 基础上修复 settlement_failed 少退款 bug

AI：收到。这是一个 bug 修复，建议版本号为 v1.7.8（patch）。
    
    请描述：
    1. bug 的具体表现是什么？
    2. 影响范围有多大？（多少用户受影响？）
    3. 根因是什么？

用户：verify.processor 的 onFailed handler 只 log 不退款，导致 slot 永远 locked。
     影响 1 个用户，损失 0.6 USDT。
     根因是 onFailed 是异步回调，但旧实现没有调用 releaseSlotAsExhausted。

AI：明白了。这是一个 P1 级别的资金安全问题。
    
    我现在生成修复文档...
    [生成 CHANGELOG.md]
    [更新 dev.md：文件变更清单]
    [更新 test.md：回归测试用例]
    
    已完成：
    - CHANGELOG.md：记录 bug 修复详情
    - dev.md：更新文件变更清单（verify.processor.ts）
    - test.md：新增回归测试用例（settlement_failed 场景）
    
    ⚠️ 重要提醒：
    1. 必须新增回归测试，防止此 bug 再次出现
    2. 建议记录到 incidents/2026-05-02-settlement-bug.md
    3. 部署前必须执行 pnpm test:all 确保全绿
    4. 涉及资金的逻辑，修复后必须人工验证
    
    是否需要我生成事故记录文档？

用户：需要

AI：好的，生成事故记录...
    [生成 incidents/2026-05-02-settlement-bug.md]
    [更新 CLAUDE.md：补充已知问题]
    
    已完成事故记录，包含：
    - 问题描述、根因分析、修复方案
    - 影响范围、教训总结
    - 相关文档链接
    
    所有文档已更新完毕，可以开始修复了。
```

#### 示例 3：需求不明确时的追问

```
用户：我想加个登录功能

AI：好的，我需要先了解几个问题：
    1. 登录方式是什么？
       - 账号密码登录
       - 手机验证码登录
       - 第三方 OAuth（如 Google、GitHub、X）
       - 以上多种组合
    
    2. 是新版本还是在现有版本上迭代？
       - 如果是新版本，建议版本号是什么？
       - 如果是迭代，基于哪个版本？
    
    3. 有什么特殊要求？
       - 首次登录强制改密？
       - 异常登录提醒？
       - 多设备登录限制？
       - 其他安全要求？

用户：X OAuth 登录，在 v1.8.0 新版本，需要首次登录强制改密

AI：收到。我现在生成 prd.md...
    [继续正常流程]
```

---

## 使用模式

**从零创建完整文档**：
```
用户：创建一个 v1.8.0 PRD，实现会员订阅功能
Skill：
  1. 生成 prd.md → 等用户确认
  2. 生成 design.md + 项目审查 + dev.md → 等用户确认
  3. 生成 plan.md + test.md + ops.md
  4. 更新 README.md
```

**增量迭代版本**：
```
用户：在 v1.7.7 基础上修复 settlement_failed bug
Skill：
  1. 建议版本号 v1.7.8（patch）
  2. 生成 CHANGELOG.md
  3. 更新 dev.md（文件变更清单）
  4. 更新 test.md（回归测试）
  5. 不更新 prd.md（需求未变）
```

**查看状态**：
```
用户：显示所有 PRD 版本
Skill：列出版本 → 展示状态总览
```

**扩展需求**：
```
用户：在 v1.7.8 中添加功能
Skill：读取现有文档 → 追加需求 → 更新关联文档
```

**归档旧版**：
```
用户：归档 v1.0.0
Skill：确认版本 → 移动到 _archive/ → 确认完成
```

**搜索需求**：
```
用户：搜索认证相关的需求
Skill：跨版本 grep → 展示结果
```

**生成运维文档**：
```
用户：为 v1.7.9 Turnstile 功能生成运维文档
Skill：
  1. 生成 ops.md（环境变量、部署流程、故障排查）
  2. 或生成独立文档 docs/ops/turnstile-setup.md
```

**记录生产事故**：
```
用户：记录 2026-05-02 的 settlement_failed bug
Skill：
  1. 生成 incidents/2026-05-02-settlement-bug.md
  2. 更新 CHANGELOG.md
  3. 更新 test.md（回归测试）
  4. 更新 CLAUDE.md（已知问题）
```

**PRD 覆盖率审计**：
```
用户：检查 v1.7.8 的 PRD 是否都实现了
Skill：
  1. 读取 prd.md 提取需求列表
  2. 读取 dev.md 检查文件变更
  3. 读取 test.md 检查测试覆盖
  4. 生成审计报告
```

---

## 最佳实践

- 始终使用语义化版本（v1.7.8, v2.0.0）
- 新建项目或新版本时，优先走完整生成流程：`prd.md` → `design.md` → `plan.md` → 项目审查 → `dev.md` → `test.md` → `ops.md`
- 每次生成、扩展、归档版本后，都要同步更新 `docs/prd/README.md`
- **文档边界原则**：
  - prd.md 中出现技术选型/框架/接口是越界 → 移至 dev.md
  - plan.md 中出现数据模型/架构图是越界 → 移至 dev.md
  - dev.md 中出现"用户希望"/"业务目标"是越界 → 移至 prd.md
- **技术方案必须基于实际代码**：生成 dev.md 前，先读取项目现有代码，确保方案与实际架构一致
- 在 plan.md 中使用状态标记：⏳ 规划中 | 🔄 进行中 | ✅ 已完成 | ❌ 已取消
- 已完成或废弃的版本及时归档到 `_archive/`
- **测试与代码同步**：任何代码变更必须同步更新测试
- **运维文档先行**：上线功能必须先有 ops.md
- **事故必须记录**：生产问题修复后必须记录到 incidents/
- **CLAUDE.md 持续更新**：架构决策、已知问题、开发规范随项目演进持续更新

---

## 后端项目 dev.md 必含板块：接口影响清单

后端项目的 `dev.md` 必须包含「接口影响清单」板块，明确记录当前版本对所有接口的影响，包含三部分：

### 1. 新增接口

| 接口 | 说明 | 影响点 |
|------|------|--------|
| `POST /xxx/add` | 新增功能 | 需新建 Controller/Service/Mapper |

### 2. 改动接口

必须列出**字段级别的调整说明**：

| 接口 | 改动内容 | 影响点 |
|------|----------|--------|
| `POST /xxx/query` | 响应新增 `fieldA`（String）、`fieldB`（Long）字段 | RespDTO 新增 2 个字段，Service 层增加聚合查询 |

### 3. 删除接口

| 接口 | 说明 | 影响点 |
|------|------|--------|
| `POST /xxx/old` | 废弃旧接口 | 前端需迁移到新接口 |

> 注意：如果没有某类变更（如无删除接口），填写"无"即可，不可省略板块。

---

## SQL 脚本规范

涉及新增数据库表、新增字段或初始化数据时，必须在版本目录下生成独立的 SQL 脚本文件：

```
docs/prd/<version>/sql/
├── DDL.sql          # 表结构变更
└── DML_init.sql     # 初始化数据
```

**DDL.sql** 包含：
- `CREATE TABLE` 建表语句（含完整字段、索引、约束、注释）
- `ALTER TABLE` 新增字段、新增索引语句

**DML_init.sql** 包含：
- 字典数据初始化（如权益类型、角色模板等）
- 历史数据迁移/回填语句（注释形式，按需执行）
- 执行前提说明（如"先执行 DDL.sql"）

> 注意：SQL 脚本应可直接在 MySQL 8.0+ / PostgreSQL 14+ 环境执行，字段注释使用 COMMENT，表引擎使用 InnoDB / 默认。

---

## 资源文件

- `assets/prd_template.md` — 产品需求文档模板
- `assets/design_template.md` — 界面设计文档模板
- `assets/dev_template.md` — 技术开发文档模板
- `assets/plan_template.md` — 开发计划模板
- `assets/ops_template.md` — 运维文档模板（新增）
- `assets/test_template.md` — 测试文档模板（新增）
- `assets/changelog_template.md` — 变更日志模板（新增）
- `assets/incident_template.md` — 事故记录模板（新增）
- `assets/claude_template.md` — CLAUDE.md 项目记忆体模板（新增）
- `assets/readme_template.md` — PRD 版本索引 README 模板
- `references/ascii_design_patterns.md` — ASCII 原型设计参考
- `references/priority_definitions.md` — P0-P3 优先级定义
