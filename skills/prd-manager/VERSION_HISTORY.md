---

## 版本历史

### v2.0.0 (2026-05-03)

**重大更新**：从文档模板库升级为完整的 AI 协作流程引擎

#### 🎉 新增

- **AI 协作规范**：完整的对话流程设计、确认机制、质量门禁、强制规则执行
- **自检清单**：prd.md / dev.md / test.md / ops.md / plan.md / CHANGELOG.md / CLAUDE.md 生成后自动检查
- **示例对话**：3 个完整对话示例（项目初始化、功能迭代、需求追问）
- **错误处理**：版本冲突、信息不完整、文档生成失败的处理流程
- **常见问题（FAQ）**：8 个常见场景的处理方案
- **5 个新模板**：ops_template.md / test_template.md / incident_template.md / changelog_template.md / claude_template.md

#### 🔧 变更

- 文档类型从 4 种扩展到 8 种（新增 ops / test / CHANGELOG / CLAUDE / incidents）
- 强化测试驱动、PRD 驱动、端到端验证的执行机制
- 明确 prd.md 和 dev.md 需要强制确认，其他文档可批量生成

#### 📝 文档

- 补充完整的对话流程设计
- 补充质量门禁规则（拒绝场景 + 警告场景）
- 补充自检清单（7 种文档类型）
- 补充错误处理流程
- 补充 FAQ（8 个常见问题）

### v1.0.0 (2026-04-XX)

**初始版本**：基础的 PRD 文档管理功能

#### 功能

- 生成 prd.md / design.md / dev.md / plan.md
- 版本管理（创建、查看、对比、搜索、归档）
- 支持两种目录结构（版本优先 / 类型优先）
- 文档边界规范
- 语义化版本管理

---

## 许可证

MIT License

Copyright (c) 2026 wlzh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
