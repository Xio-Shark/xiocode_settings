# CHANGELOG

> 本文档记录项目的所有重要变更，遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/) 规范。
> 版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/) 规范：`主版本号.次版本号.修订号`

---

## [Unreleased]

### 计划中
- [ ] 功能 A
- [ ] 功能 B

---

## [1.0.0] - YYYY-MM-DD

### 🎉 Added（新增）
- 新增用户注册与 X OAuth 登录功能
- 新增任务发布功能（支持 5 种互动动作）
- 新增任务大厅（公开任务列表）
- 新增任务领取与验证流程
- 新增 USDT 充值与提现功能
- 新增 T+1 自动结算系统
- 新增推广分佣机制
- 新增站内通知系统
- 新增运营后台（用户管理 / 任务管理 / 提现审批 / 系统配置）
- 新增服务条款与隐私政策页面

### 🔧 Changed（变更）
- 无

### 🐛 Fixed（修复）
- 无

### 🗑️ Deprecated（弃用）
- 无

### ❌ Removed（移除）
- 无

### 🔒 Security（安全）
- 实现 JWT 认证与授权
- 实现 API 限流（认证用户 200 req/min，未认证 30 req/min）
- 实现敏感数据加密存储（X tokens、TG bot token）
- 实现 HTTPS 强制跳转
- 实现 CORS 白名单

---

## [0.2.0] - YYYY-MM-DD

### 🎉 Added
- 新增任务验证队列（BullMQ）
- 新增 TRON 链交互模块（HD 钱包）
- 新增邮件通知（Resend）

### 🔧 Changed
- 优化任务大厅加载性能（SSR → CSR）
- 优化数据库查询（添加索引）

### 🐛 Fixed
- 修复并发领取名额时的超卖问题
- 修复 JWT 过期后无法刷新的问题
- 修复提现审批后余额未扣除的问题

---

## [0.1.0] - YYYY-MM-DD

### 🎉 Added
- 初始化项目骨架（Turborepo + NestJS + Next.js）
- 初始化数据库 Schema（18 张表）
- 初始化 Docker Compose 开发环境

---

## 版本说明

### 版本号规则

- **主版本号（Major）**：不兼容的 API 变更
- **次版本号（Minor）**：向下兼容的功能新增
- **修订号（Patch）**：向下兼容的问题修复

### 变更类型

- **🎉 Added**：新增功能
- **🔧 Changed**：功能变更（不影响兼容性）
- **🐛 Fixed**：Bug 修复
- **🗑️ Deprecated**：即将废弃的功能（但仍可用）
- **❌ Removed**：已移除的功能
- **🔒 Security**：安全相关的修复或增强

### 日期格式

- 使用 ISO 8601 格式：`YYYY-MM-DD`

---

## 示例条目

### 好的示例 ✅

```markdown
### 🎉 Added
- 新增任务发布功能，支持 5 种互动动作（点赞 / 转发 / 评论 / 关注 / 收藏）
- 新增任务大厅筛选功能，支持按奖励 / 名额 / 门槛筛选
```

### 不好的示例 ❌

```markdown
### Added
- 加了一些功能
- 修了一些 bug
```

**原因**：
- 缺少 emoji 标识
- 描述不清晰，无法让读者快速理解变更内容

---

## 迁移指南

### 从 v0.x 升级到 v1.0

#### 破坏性变更

1. **API 路由变更**
   - 旧：`/api/tasks` → 新：`/api/v1/tasks`
   - 旧：`/api/users` → 新：`/api/v1/users`

2. **数据库 Schema 变更**
   - `users` 表新增 `auth_scope` 字段（必填）
   - `task_groups` 表 `status` 字段枚举值变更

#### 迁移步骤

1. 备份数据库
   ```bash
   pg_dump $DATABASE_URL > backup_$(date +%Y%m%d).sql
   ```

2. 执行数据库迁移
   ```bash
   npx prisma migrate deploy
   ```

3. 更新前端 API 调用
   ```typescript
   // 旧
   api.get('/api/tasks')
   
   // 新
   api.get('/api/v1/tasks')
   ```

4. 重启服务
   ```bash
   pm2 restart all
   ```

---

## 贡献指南

### 如何更新 CHANGELOG

1. **每次合并 PR 时更新**
   - 在 `[Unreleased]` 部分添加变更条目
   - 使用正确的变更类型（Added / Changed / Fixed 等）
   - 描述清晰，包含关键信息

2. **发布新版本时**
   - 将 `[Unreleased]` 部分的内容移动到新版本号下
   - 添加发布日期
   - 创建新的 `[Unreleased]` 部分

3. **示例 PR 描述**
   ```markdown
   ## 变更说明
   
   ### 🎉 Added
   - 新增任务详情页分享功能
   
   ### 🐛 Fixed
   - 修复任务大厅分页错误
   
   ## CHANGELOG 更新
   
   已在 `[Unreleased]` 部分添加上述变更。
   ```

---

## 参考资源

- [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)
- [语义化版本](https://semver.org/lang/zh-CN/)
- [Conventional Commits](https://www.conventionalcommits.org/zh-hans/)
