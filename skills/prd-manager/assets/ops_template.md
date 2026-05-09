# <version> 运维文档

> 本文档聚焦「如何部署和运维」（环境变量、部署流程、监控告警、故障排查、回滚）。
> 功能需求 → `prd.md`　　技术实现 → `dev.md`　　测试验证 → `test.md`

---

## 1. 环境变量清单

### 1.1 后端环境变量

| 变量名 | 必填 | 默认值 | 说明 | 获取方式 |
|--------|------|--------|------|---------|
| `DATABASE_URL` | ✅ | - | 数据库连接字符串 | [数据库服务商控制台] |
| `REDIS_URL` | ✅ | - | Redis 连接字符串 | [Redis 服务商控制台] |
| `NODE_ENV` | ✅ | `development` | 运行环境（development/production） | 手动设置 |
| `PORT` | ❌ | `3001` | 服务端口 | 手动设置 |
| `JWT_SECRET` | ✅ | - | JWT 签名密钥 | `openssl rand -hex 32` |

### 1.2 前端环境变量

| 变量名 | 必填 | 默认值 | 说明 | 获取方式 |
|--------|------|--------|------|---------|
| `NEXT_PUBLIC_API_URL` | ✅ | - | API 基础 URL（构建时注入） | 手动设置 |
| `NEXT_PUBLIC_SITE_URL` | ✅ | - | 站点 URL（构建时注入） | 手动设置 |

> **注意**：
> - `NEXT_PUBLIC_*` 变量必须在构建时存在，不能只在运行时设置
> - 敏感变量（如 JWT_SECRET）不要提交到 Git，使用 `.env` 文件（gitignored）

### 1.3 环境变量验证

部署前检查所有必填环境变量是否已配置：

```bash
# 后端
node -e "console.log(process.env.DATABASE_URL ? '✅ DATABASE_URL' : '❌ DATABASE_URL missing')"

# 前端（构建时）
echo $NEXT_PUBLIC_API_URL
```

---

## 2. 部署流程

### 2.1 前置条件

- [ ] 所有测试通过（`pnpm test:all`）
- [ ] 代码已合并到 main 分支
- [ ] 环境变量已配置（对照上方清单）
- [ ] 数据库迁移脚本已准备（如有）
- [ ] 回滚方案已准备

### 2.2 部署步骤

#### 步骤 1：构建

```bash
# 本地构建
pnpm turbo build --filter=@project/api
pnpm turbo build --filter=@project/web
```

#### 步骤 2：数据库迁移（如有）

```bash
# 在服务器上执行
cd /opt/project/apps/api
npx prisma migrate deploy
```

#### 步骤 3：上传代码

```bash
# 使用部署脚本
bash scripts/deploy.sh

# 或手动上传
rsync -avz --delete ./dist/ user@server:/opt/project/dist/
```

#### 步骤 4：重启服务

```bash
# 使用 PM2
pm2 restart project-api
pm2 restart project-web

# 或使用 systemd
sudo systemctl restart project-api
sudo systemctl restart project-web
```

#### 步骤 5：验证部署

```bash
# 检查服务状态
curl https://api.example.com/health

# 检查日志
pm2 logs project-api --lines 50
```

### 2.3 首次部署（全新服务器）

如果是全新服务器，需要先完成以下准备工作：

1. **安装依赖**：Node.js、pnpm、PM2、Nginx
2. **配置数据库**：创建数据库、配置连接
3. **配置 Nginx**：反向代理、SSL 证书
4. **配置环境变量**：创建 `.env` 文件
5. **初始化数据库**：执行 `prisma migrate deploy`
6. **启动服务**：`pm2 start`

详细步骤见：`docs/ops/deployment-guide.md`（如有）

---

## 3. 监控告警

### 3.1 关键指标

| 指标 | 正常范围 | 告警阈值 | 监控方式 |
|------|---------|---------|---------|
| API 响应时间 | < 500ms | > 2s | APM 工具 |
| 错误率 | < 1% | > 5% | 日志聚合 |
| CPU 使用率 | < 70% | > 90% | 服务器监控 |
| 内存使用率 | < 80% | > 95% | 服务器监控 |
| 数据库连接数 | < 80% | > 95% | 数据库监控 |

### 3.2 告警渠道

- **邮件**：管理员邮箱（用于敏感告警）
- **Slack/企微/Telegram**：团队频道（用于一般告警）
- **短信**：紧急告警（P0 级别）

### 3.3 告警规则

| 告警级别 | 触发条件 | 响应时间 | 通知渠道 |
|---------|---------|---------|---------|
| **P0** | 服务不可用、数据丢失 | 立即 | 短信 + 邮件 + Slack |
| **P1** | 错误率 > 5%、响应时间 > 5s | 15 分钟内 | 邮件 + Slack |
| **P2** | CPU > 90%、内存 > 95% | 1 小时内 | Slack |
| **P3** | 非关键指标异常 | 24 小时内 | Slack |

---

## 4. 故障排查

### 4.1 常见问题

#### 问题 1：服务无法启动

**现象**：`pm2 start` 失败，或服务启动后立即退出

**排查步骤**：
1. 检查日志：`pm2 logs project-api --err --lines 100`
2. 检查环境变量：`pm2 env 0`（0 是进程 ID）
3. 检查端口占用：`lsof -i :3001`
4. 检查数据库连接：`psql $DATABASE_URL`

**常见原因**：
- 环境变量缺失或错误
- 端口被占用
- 数据库连接失败
- 依赖未安装

**解决方案**：
- 补充缺失的环境变量
- 更换端口或停止占用进程
- 检查数据库连接字符串
- 执行 `pnpm install`

#### 问题 2：API 返回 500 错误

**现象**：前端请求 API 返回 500 Internal Server Error

**排查步骤**：
1. 检查后端日志：`pm2 logs project-api --err --lines 100`
2. 查找具体错误堆栈
3. 检查数据库连接
4. 检查第三方服务（如 Redis、外部 API）

**常见原因**：
- 代码逻辑错误（空指针、类型错误）
- 数据库查询失败
- 第三方服务不可用

**解决方案**：
- 根据错误堆栈修复代码
- 检查数据库状态
- 检查第三方服务状态

#### 问题 3：前端页面无法访问

**现象**：访问网站返回 502 Bad Gateway 或 404 Not Found

**排查步骤**：
1. 检查 Nginx 状态：`sudo systemctl status nginx`
2. 检查 Nginx 配置：`sudo nginx -t`
3. 检查前端服务状态：`pm2 list`
4. 检查 Nginx 日志：`sudo tail -f /var/log/nginx/error.log`

**常见原因**：
- Nginx 配置错误
- 前端服务未启动
- 端口配置错误

**解决方案**：
- 修复 Nginx 配置并重载：`sudo nginx -t && sudo systemctl reload nginx`
- 启动前端服务：`pm2 start project-web`
- 检查 Nginx 配置中的 proxy_pass 端口

### 4.2 日志查看

```bash
# PM2 日志
pm2 logs project-api --lines 100
pm2 logs project-api --err --lines 100

# Nginx 日志
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# 系统日志
sudo journalctl -u project-api -n 100
```

---

## 5. 回滚方案

### 5.1 代码回滚

```bash
# 方式 1：Git revert（推荐）
git revert <commit-hash>
git push origin main
bash scripts/deploy.sh

# 方式 2：Git reset（慎用）
git reset --hard <previous-commit>
git push origin main --force
bash scripts/deploy.sh
```

### 5.2 数据库回滚

如果本次部署包含数据库迁移，需要准备回滚 SQL：

```sql
-- 回滚示例：删除新增的表
DROP TABLE IF EXISTS new_table;

-- 回滚示例：删除新增的字段
ALTER TABLE users DROP COLUMN new_field;
```

**执行回滚**：
```bash
psql $DATABASE_URL < rollback.sql
```

### 5.3 回滚验证

回滚后必须验证：
- [ ] 服务正常启动
- [ ] 关键功能可用
- [ ] 数据库状态正确
- [ ] 无错误日志

---

## 6. 性能优化

### 6.1 数据库优化

- 添加索引：高频查询字段
- 查询优化：避免 N+1 查询
- 连接池配置：根据负载调整

### 6.2 缓存策略

- Redis 缓存：热点数据
- CDN 缓存：静态资源
- 浏览器缓存：前端资源

### 6.3 负载均衡

- 水平扩展：多实例部署
- 负载均衡器：Nginx / HAProxy
- 健康检查：定期检查实例状态

---

## 7. 安全加固

### 7.1 服务器安全

- [ ] 禁用 root 登录
- [ ] 配置防火墙（只开放必要端口）
- [ ] 定期更新系统补丁
- [ ] 配置 fail2ban 防暴力破解

### 7.2 应用安全

- [ ] 使用 HTTPS（SSL 证书）
- [ ] 配置 CORS 白名单
- [ ] 输入验证和过滤
- [ ] SQL 注入防护（使用 ORM）
- [ ] XSS 防护（CSP 头）

### 7.3 数据安全

- [ ] 定期备份数据库
- [ ] 敏感数据加密存储
- [ ] 访问日志记录
- [ ] 定期审计权限

---

## 8. 备份与恢复

### 8.1 数据库备份

```bash
# 自动备份脚本（每日执行）
pg_dump $DATABASE_URL > backup_$(date +%Y%m%d).sql

# 保留最近 7 天的备份
find /backup -name "backup_*.sql" -mtime +7 -delete
```

### 8.2 代码备份

```bash
# Git 仓库即为备份
git push origin main

# 额外备份到其他 Git 服务
git push backup main
```

### 8.3 恢复流程

```bash
# 恢复数据库
psql $DATABASE_URL < backup_20260503.sql

# 恢复代码
git checkout <commit-hash>
bash scripts/deploy.sh
```

---

## 9. 联系方式

| 角色 | 姓名 | 联系方式 | 负责范围 |
|------|------|---------|---------|
| 技术负责人 | [姓名] | [邮箱/电话] | 架构、部署、故障处理 |
| 运维负责人 | [姓名] | [邮箱/电话] | 服务器、监控、备份 |
| 开发负责人 | [姓名] | [邮箱/电话] | 代码、功能、bug 修复 |
