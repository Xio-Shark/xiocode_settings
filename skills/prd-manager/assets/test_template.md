# <version> 测试文档

> 本文档聚焦「如何测试和验证」（测试策略、用例设计、自动化测试、验收标准）。
> 功能需求 → `prd.md`　　技术实现 → `dev.md`　　部署运维 → `ops.md`

---

## 1. 测试策略

### 1.1 测试金字塔

```
           /\
          /  \  E2E 测试（10%）
         /____\
        /      \  集成测试（30%）
       /________\
      /          \  单元测试（60%）
     /____________\
```

| 层级 | 占比 | 工具 | 覆盖目标 |
|------|------|------|---------|
| **单元测试** | 60% | Jest / Vitest | 函数 / 类 / 组件逻辑 |
| **集成测试** | 30% | Jest + Supertest / Testing Library | API 端到端 / 数据库交互 / 跨模块协作 |
| **E2E 测试** | 10% | Playwright / Cypress | 关键用户流程 / 跨系统集成 |

### 1.2 测试原则

- **测试金字塔**：单元测试为主，集成测试为辅，E2E 测试覆盖关键路径
- **测试隔离**：每个测试独立运行，不依赖其他测试的状态
- **测试数据**：使用 fixture / factory 生成测试数据，避免硬编码
- **测试覆盖率**：核心业务逻辑 ≥ 80%，关键路径 100%
- **测试可维护性**：测试代码与业务代码同步更新，避免测试腐化

---

## 2. 测试环境

### 2.1 环境清单

| 环境 | 用途 | 数据库 | 第三方服务 | 部署方式 |
|------|------|--------|-----------|---------|
| **本地开发** | 开发者本地调试 | Docker Compose | Mock / Sandbox | `pnpm dev` |
| **CI/CD** | 自动化测试 | 临时容器 | Mock | GitHub Actions |
| **Staging** | 预发布验证 | 独立实例 | Sandbox | 自动部署 |
| **Production** | 生产环境 | 生产实例 | 生产 API | 手动部署 |

### 2.2 测试数据管理

- **Seed 数据**：`prisma/seed.ts` 提供基础测试数据
- **Factory 模式**：使用 `@faker-js/faker` 生成随机测试数据
- **数据隔离**：每个测试用例使用独立的数据库事务，测试结束后回滚
- **敏感数据脱敏**：测试环境不使用生产数据，如需使用需脱敏处理

---

## 3. 单元测试

### 3.1 测试范围

- **Service 层**：业务逻辑、数据处理、异常处理
- **Controller 层**：路由、参数校验、响应格式
- **Util 函数**：工具函数、格式化、校验逻辑
- **前端组件**：UI 组件、交互逻辑、状态管理

### 3.2 测试用例设计

#### 3.2.1 后端 Service 测试示例

```typescript
// apps/api/src/modules/task/__tests__/task.service.spec.ts
describe('TaskService', () => {
  let service: TaskService;
  let prisma: PrismaService;

  beforeEach(async () => {
    const module = await Test.createTestingModule({
      providers: [TaskService, PrismaService],
    }).compile();

    service = module.get<TaskService>(TaskService);
    prisma = module.get<PrismaService>(PrismaService);
  });

  describe('createTask', () => {
    it('应该成功创建任务', async () => {
      // Arrange
      const dto = { /* ... */ };
      const mockUser = { id: 'user-1', balance: 100 };

      // Act
      const result = await service.createTask(mockUser.id, dto);

      // Assert
      expect(result).toBeDefined();
      expect(result.status).toBe('active');
    });

    it('余额不足时应该抛出异常', async () => {
      // Arrange
      const dto = { /* ... */ };
      const mockUser = { id: 'user-1', balance: 0 };

      // Act & Assert
      await expect(service.createTask(mockUser.id, dto))
        .rejects.toThrow('余额不足');
    });
  });
});
```

#### 3.2.2 前端组件测试示例

```typescript
// apps/web/src/components/ui/__tests__/Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import Button from '../Button';

describe('Button', () => {
  it('应该渲染按钮文本', () => {
    render(<Button>点击我</Button>);
    expect(screen.getByText('点击我')).toBeInTheDocument();
  });

  it('点击时应该触发回调', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>点击我</Button>);
    
    fireEvent.click(screen.getByText('点击我'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('disabled 状态下不应该触发回调', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick} disabled>点击我</Button>);
    
    fireEvent.click(screen.getByText('点击我'));
    expect(handleClick).not.toHaveBeenCalled();
  });
});
```

### 3.3 测试覆盖率目标

| 模块 | 目标覆盖率 | 当前覆盖率 | 状态 |
|------|-----------|-----------|------|
| 核心业务逻辑（task / payment / verify） | ≥ 80% | — | — |
| 工具函数（utils / validators） | 100% | — | — |
| API 路由（controllers） | ≥ 70% | — | — |
| 前端组件（UI components） | ≥ 60% | — | — |

---

## 4. 集成测试

### 4.1 测试范围

- **API 端到端**：完整的 HTTP 请求 → 业务逻辑 → 数据库 → 响应
- **数据库交互**：事务、并发、约束、索引
- **跨模块协作**：任务发布 → 名额领取 → 验证 → 结算
- **第三方服务集成**：X API、TRON 链、Redis、BullMQ

### 4.2 测试用例设计

#### 4.2.1 API 集成测试示例

```typescript
// apps/api/src/integration-tests/task.integration.spec.ts
describe('Task API Integration', () => {
  let app: INestApplication;
  let prisma: PrismaService;
  let authToken: string;

  beforeAll(async () => {
    // 启动测试应用
    const moduleFixture = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();

    app = moduleFixture.createNestApplication();
    await app.init();

    prisma = app.get<PrismaService>(PrismaService);

    // 创建测试用户并获取 token
    authToken = await createTestUserAndGetToken(app);
  });

  afterAll(async () => {
    await prisma.$disconnect();
    await app.close();
  });

  describe('POST /api/v1/tasks', () => {
    it('应该成功创建任务', async () => {
      const response = await request(app.getHttpServer())
        .post('/api/v1/tasks')
        .set('Authorization', `Bearer ${authToken}`)
        .send({
          targetUrl: 'https://x.com/elonmusk/status/123',
          description: '测试任务',
          packages: [{ /* ... */ }],
        })
        .expect(201);

      expect(response.body).toHaveProperty('id');
      expect(response.body.status).toBe('active');

      // 验证数据库状态
      const task = await prisma.taskGroup.findUnique({
        where: { id: response.body.id },
      });
      expect(task).toBeDefined();
    });

    it('余额不足时应该返回 400', async () => {
      // 清空用户余额
      await prisma.user.update({
        where: { id: testUserId },
        data: { balance: 0 },
      });

      await request(app.getHttpServer())
        .post('/api/v1/tasks')
        .set('Authorization', `Bearer ${authToken}`)
        .send({ /* ... */ })
        .expect(400);
    });
  });
});
```

#### 4.2.2 并发测试示例

```typescript
describe('Slot Claiming Concurrency', () => {
  it('应该防止超卖（100 个用户同时领取 10 个名额）', async () => {
    // Arrange
    const task = await createTestTask({ slotCount: 10 });
    const users = await createTestUsers(100);

    // Act
    const results = await Promise.allSettled(
      users.map(user => claimSlot(user.id, task.packageId))
    );

    // Assert
    const successCount = results.filter(r => r.status === 'fulfilled').length;
    expect(successCount).toBe(10); // 只有 10 个成功

    const failedCount = results.filter(r => r.status === 'rejected').length;
    expect(failedCount).toBe(90); // 其余 90 个失败
  });
});
```

---

## 5. E2E 测试

### 5.1 测试范围

- **关键用户流程**：注册 → 充值 → 发布任务 → 领取任务 → 验证 → 结算 → 提现
- **跨系统集成**：X OAuth、TRON 链、邮件、推送
- **浏览器兼容性**：Chrome、Firefox、Safari、移动端

### 5.2 测试用例设计

#### 5.2.1 Playwright E2E 测试示例

```typescript
// apps/web/e2e/task-flow.spec.ts
import { test, expect } from '@playwright/test';

test.describe('任务发布与领取流程', () => {
  test('发布者发布任务 → 执行者领取 → 完成验证', async ({ page, context }) => {
    // 1. 发布者登录
    await page.goto('https://staging.xripple.app/login');
    await page.click('text=使用 X 账号登录');
    // ... X OAuth 流程 ...

    // 2. 发布任务
    await page.goto('/publish');
    await page.fill('[name="targetUrl"]', 'https://x.com/elonmusk/status/123');
    await page.fill('[name="description"]', 'E2E 测试任务');
    await page.click('text=发布任务');
    await expect(page).toHaveURL(/\/t\/[a-f0-9-]+/);

    const taskUrl = page.url();

    // 3. 执行者登录（新标签页）
    const executorPage = await context.newPage();
    await executorPage.goto('https://staging.xripple.app/login');
    // ... 执行者 OAuth 流程 ...

    // 4. 领取任务
    await executorPage.goto(taskUrl);
    await executorPage.click('text=领取');
    await executorPage.click('text=确认领取');
    await expect(executorPage.locator('text=领取成功')).toBeVisible();

    // 5. 等待验证（模拟 60 分钟后）
    // 注意：实际 E2E 不会真等 60 分钟，需要 mock 或调整测试环境的倒计时
    // ...

    // 6. 验证结算
    await executorPage.goto('/me/wallet');
    await expect(executorPage.locator('text=待结算')).toContainText('0.85 USDT');
  });
});
```

### 5.3 E2E 测试策略

- **关键路径优先**：覆盖 80% 用户使用的核心流程
- **Mock 第三方服务**：X API、TRON 链使用 Sandbox 或 Mock
- **并行执行**：使用 Playwright 的 worker 并行运行测试
- **失败重试**：网络不稳定时自动重试 1-2 次
- **截图 & 录屏**：失败时自动保存截图和视频

---

## 6. 性能测试

### 6.1 测试目标

| 指标 | 目标值 | 测试工具 |
|------|--------|---------|
| API 响应时间（P95） | < 500ms | k6 / Artillery |
| 并发用户数 | ≥ 1000 | k6 |
| 数据库查询时间 | < 100ms | Prisma Metrics |
| 页面加载时间（FCP） | < 1.5s | Lighthouse |
| 页面加载时间（LCP） | < 2.5s | Lighthouse |

### 6.2 压力测试脚本示例

```javascript
// k6-load-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '2m', target: 100 },  // 2 分钟内增加到 100 用户
    { duration: '5m', target: 100 },  // 保持 100 用户 5 分钟
    { duration: '2m', target: 500 },  // 2 分钟内增加到 500 用户
    { duration: '5m', target: 500 },  // 保持 500 用户 5 分钟
    { duration: '2m', target: 0 },    // 2 分钟内降到 0
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% 的请求 < 500ms
    http_req_failed: ['rate<0.01'],   // 错误率 < 1%
  },
};

export default function () {
  // 测试任务列表 API
  let res = http.get('https://api.xripple.app/api/v1/tasks');
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });

  sleep(1);
}
```

---

## 7. 安全测试

### 7.1 测试范围

- **认证 & 授权**：JWT 过期、权限绕过、CSRF
- **输入验证**：SQL 注入、XSS、命令注入
- **敏感数据**：密钥泄露、日志脱敏、传输加密
- **API 限流**：暴力破解、DDoS 防护

### 7.2 测试用例清单

| 测试项 | 测试方法 | 预期结果 |
|--------|---------|---------|
| SQL 注入 | 在输入框输入 `' OR '1'='1` | 被拦截或转义 |
| XSS 攻击 | 输入 `<script>alert('xss')</script>` | 被转义或过滤 |
| JWT 过期 | 使用过期 token 访问 API | 返回 401 |
| 权限绕过 | 普通用户访问 `/api/admin` | 返回 403 |
| CSRF 攻击 | 跨域请求修改数据 | 被 CORS 拦截 |
| 暴力破解 | 1 分钟内发送 1000 次请求 | 触发限流 429 |

---

## 8. 验收测试

### 8.1 验收标准

每个功能模块的验收标准在 `prd.md` 中定义，测试时需逐条验证。

#### 8.1.1 示例：任务发布功能验收清单

- [ ] 用户可以输入 X 链接并自动解析推文信息
- [ ] 用户可以选择 1-5 种互动动作
- [ ] 用户可以设置奖励金额（≥ 最低奖励）
- [ ] 用户可以设置名额数量（≥ 最少名额）
- [ ] 用户可以设置任务有效期（≤ 最长有效期）
- [ ] 余额不足时显示明确提示
- [ ] 发布成功后跳转到任务详情页
- [ ] 发布成功后扣除相应余额并锁定

### 8.2 回归测试

每次发布前，必须执行回归测试清单：

- [ ] 核心功能（任务发布 / 领取 / 验证 / 结算）正常
- [ ] 充值 / 提现流程正常
- [ ] 通知推送正常
- [ ] 运营后台功能正常
- [ ] 无明显性能退化
- [ ] 无新增安全漏洞

---

## 9. 测试自动化

### 9.1 CI/CD 集成

```yaml
# .github/workflows/test.yml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '22'
      
      - name: Install dependencies
        run: pnpm install
      
      - name: Run linter
        run: pnpm lint
      
      - name: Run type check
        run: pnpm type-check
      
      - name: Run unit tests
        run: pnpm test:unit
      
      - name: Run integration tests
        run: pnpm test:integration
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

### 9.2 测试命令清单

| 命令 | 说明 |
|------|------|
| `pnpm test:unit` | 运行所有单元测试 |
| `pnpm test:integration` | 运行所有集成测试 |
| `pnpm test:e2e` | 运行所有 E2E 测试 |
| `pnpm test:all` | 运行所有测试（lint + typecheck + unit + integration + build + 静态扫描）|
| `pnpm test:quick` | 快速测试（跳过 build 和集成测试）|
| `pnpm test:full` | 完整测试（包含运行时 API 烟测）|
| `pnpm test:watch` | 监听模式运行单元测试 |
| `pnpm test:coverage` | 生成测试覆盖率报告 |

---

## 10. 测试数据与 Fixture

### 10.1 Seed 数据

```typescript
// prisma/seed.ts
async function main() {
  // 创建测试用户
  const testUser = await prisma.user.create({
    data: {
      xUserId: 'test-user-1',
      xUsername: 'testuser',
      displayName: 'Test User',
      balance: 1000,
      authScope: 'executor',
    },
  });

  // 创建测试任务
  const testTask = await prisma.taskGroup.create({
    data: {
      publisherId: testUser.id,
      targetUrl: 'https://x.com/elonmusk/status/123',
      description: '测试任务',
      status: 'active',
      packages: {
        create: [{
          actions: ['like', 'retweet'],
          rewardPerSlot: 10,
          slotCount: 100,
        }],
      },
    },
  });
}
```

### 10.2 Factory 模式

```typescript
// apps/api/src/test-utils/factories.ts
import { faker } from '@faker-js/faker';

export function createTestUser(overrides = {}) {
  return {
    xUserId: faker.string.uuid(),
    xUsername: faker.internet.userName(),
    displayName: faker.person.fullName(),
    balance: 1000,
    authScope: 'executor',
    ...overrides,
  };
}

export function createTestTask(overrides = {}) {
  return {
    targetUrl: 'https://x.com/elonmusk/status/123',
    description: faker.lorem.sentence(),
    status: 'active',
    ...overrides,
  };
}
```

---

## 11. 测试报告

### 11.1 测试执行报告模板

| 项目 | 内容 |
|------|------|
| **测试版本** | v1.5.0 |
| **测试时间** | YYYY-MM-DD HH:MM |
| **测试人员** | [姓名] |
| **测试环境** | Staging |
| **测试范围** | 任务发布 / 领取 / 验证 / 结算 |

#### 测试结果

| 测试类型 | 总数 | 通过 | 失败 | 跳过 | 通过率 |
|---------|------|------|------|------|--------|
| 单元测试 | 150 | 148 | 2 | 0 | 98.7% |
| 集成测试 | 50 | 48 | 2 | 0 | 96.0% |
| E2E 测试 | 20 | 19 | 1 | 0 | 95.0% |
| **总计** | **220** | **215** | **5** | **0** | **97.7%** |

#### 失败用例

| 用例 ID | 用例名称 | 失败原因 | 严重级别 | 负责人 | 状态 |
|---------|---------|---------|---------|--------|------|
| TC-001 | 余额不足时发布任务 | 错误提示不明确 | P2 | [姓名] | 已修复 |
| TC-045 | 并发领取名额 | 偶现超卖 | P1 | [姓名] | 修复中 |

---

## 12. 测试最佳实践

### 12.1 编写测试的原则

- **AAA 模式**：Arrange（准备）→ Act（执行）→ Assert（断言）
- **单一职责**：每个测试只验证一个行为
- **独立性**：测试之间不相互依赖
- **可读性**：测试名称清晰描述测试内容
- **可维护性**：避免重复代码，使用 helper 函数

### 12.2 常见反模式

- ❌ **测试实现细节**：测试应该关注行为，而非实现
- ❌ **过度 Mock**：过多 Mock 会让测试失去意义
- ❌ **脆弱的测试**：依赖具体的 DOM 结构或 CSS 类名
- ❌ **慢测试**：单元测试应该在毫秒级完成
- ❌ **忽略边界条件**：只测试 happy path

### 12.3 测试金句

> "测试不是为了证明代码没有 bug，而是为了在 bug 出现时快速定位。"

> "好的测试是最好的文档。"

> "如果测试难写，说明代码设计有问题。"

---

## 13. 附录

### 13.1 测试工具清单

| 工具 | 用途 | 官网 |
|------|------|------|
| Jest | 单元测试 / 集成测试 | https://jestjs.io/ |
| Vitest | 单元测试（Vite 项目）| https://vitest.dev/ |
| Testing Library | React 组件测试 | https://testing-library.com/ |
| Playwright | E2E 测试 | https://playwright.dev/ |
| Cypress | E2E 测试 | https://www.cypress.io/ |
| k6 | 性能测试 | https://k6.io/ |
| Supertest | API 测试 | https://github.com/visionmedia/supertest |

### 13.2 测试资源

- [测试金字塔](https://martinfowler.com/articles/practical-test-pyramid.html)
- [Jest 最佳实践](https://github.com/goldbergyoni/javascript-testing-best-practices)
- [Playwright 文档](https://playwright.dev/docs/intro)
