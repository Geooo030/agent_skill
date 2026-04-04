---
name: wedding-fabric-lead-hunter
description: "婚纱布料获客专家 | Wedding Fabric Lead Hunter. 专为婚纱布料/蕾丝原料供应商设计的获客技能。自动挖掘婚纱厂、礼服厂、蕾丝加工厂客户线索，生成个性化联系策略。触发词：婚纱布料获客、婚纱厂客户、蕾丝面料客户开发、wedding fabric leads."
version: 1.0.0
author: ClawDBot
license: MIT
tags: [leads, wedding, fabric, sales, b2b, outreach, prospecting]
gitRepo: git@github.com:Geooo030/agent_skill.git
updateStrategy: pull
metadata:
  openclaw:
    emoji: 👰
    requires:
      skills:
        - lead-hunter
        - lead-research-assistant-cn
        - web-tools-guide
---

# 婚纱布料获客专家 (Wedding Fabric Lead Hunter)

> 专为婚纱布料/蕾丝原料供应商设计的智能获客解决方案

## 🎯 这个技能做什么

帮助婚纱布料供应商：

1. **定义理想客户画像 (ICP)** - 明确目标客户特征
2. **多渠道挖掘线索** - 从 LinkedIn、1688、行业网站获取客户信息
3. **智能评分筛选** - 按采购意向和匹配度评分
4. **生成联系策略** - 个性化开场白和触达方案
5. **输出可执行文件** - 交互式看板 HTML 方便跟进

---

## 📦 前置依赖技能

本 skill 依赖以下技能（需先安装）：

| 技能名称 | 用途 | 安装命令 |
|----------|------|----------|
| `lead-hunter` | 线索挖掘框架 | `clawhub install lead-hunter --force` |
| `lead-research-assistant-cn` | 联系策略生成 | `clawhub install lead-research-assistant-cn --force` |
| `web-tools-guide` | Web 搜索策略 | 已内置 |

---

## 🚀 快速开始

### 第一步：确认前置技能已安装

```bash
# 检查已安装的技能
clawhub list

# 如果未安装，执行安装
clawhub install lead-hunter --force
clawhub install lead-research-assistant-cn --force
```

### 第二步：配置你的业务信息

编辑 `config/business-profile.yaml`，填入你的业务信息：

```yaml
company:
  name: "你的公司名称"
  product: "婚纱布料、蕾丝原料"
  location: "你的所在地"
  
value_proposition:
  - "源头工厂，价格优势"
  - "品质稳定，供应可靠"
  - "款式多样，支持定制"
  - "批量优惠，账期灵活"

target_regions:
  - 苏州虎丘    # 国内最大婚纱产地
  - 广州        # 婚纱批发中心
  - 潮州        # 外贸婚纱基地
  - 六安        # 新兴婚纱产业带
```

### 第三步：执行获客流程

直接告诉 AI：

> "使用 wedding-fabric-lead-hunter 帮我挖掘 20 个婚纱厂客户线索"

AI 会自动执行完整的获客流程，**包括自动导入到获客系统**。

### 执行结果

完成后你将获得：

1. 📊 **线索报告** - HTML/JSON 格式，包含评分和分类
2. 📋 **联系策略** - 高优先级客户的跟进方案
3. 📥 **数据入库** - 自动导入到 Lead CRM 系统（可通过前端查看）

---

## 📋 完整执行流程

```
┌─────────────────────────────────────────────────────────────────┐
│                    婚纱布料获客完整流程                            │
└─────────────────────────────────────────────────────────────────┘

Phase 1: 准备阶段
├─ 1.1 检查前置技能安装状态
├─ 1.2 加载业务配置文件
└─ 1.3 加载 ICP 配置

Phase 2: 线索挖掘阶段
├─ 2.1 Web 搜索婚纱厂信息
│   ├─ 搜索苏州虎丘婚纱厂
│   ├─ 搜索潮州外贸婚纱厂
│   ├─ 搜索六安婚纱产业带
│   └─ 搜索广州婚纱企业
├─ 2.2 访问行业名录网站
│   ├─ 天下工厂婚纱名录
│   ├─ 1688 婚纱加工厂
│   └─ 中国制造网婚纱厂
└─ 2.3 整理原始线索数据

Phase 3: 线索评分阶段
├─ 3.1 按 ICP 配置计算评分
│   ├─ 行业匹配度 (25分)
│   ├─ 地区匹配度 (20分)
│   ├─ 公司规模 (15分)
│   ├─ 采购意向信号 (25分)
│   └─ 活跃度 (15分)
├─ 3.2 分类优先级
│   ├─ Hot (≥70分): 高优先级
│   ├─ Warm (50-69分): 中等优先级
│   └─ Cold (<50分): 低优先级/竞品
└─ 3.3 生成评分报告

Phase 4: 联系策略生成阶段
├─ 4.1 为高优先级客户生成策略
│   ├─ 为什么是好客户
│   ├─ 价值主张
│   ├─ 联系方式
│   ├─ 联系策略
│   └─ 开场白话术
└─ 4.2 输出可执行文件

Phase 5: 输出阶段
├─ 5.1 生成 JSON 格式线索文件
├─ 5.2 读取获客看板 HTML 模板
├─ 5.3 将线索数据注入模板生成看板 HTML
└─ 5.4 上传看板 HTML 文件并提供下载链接

Phase 6: 数据导入阶段 (自动导入到获客系统)
├─ 6.1 调用 CRM API 登录获取 token
│   └─ POST http://localhost:8080/api/auth/login
├─ 6.2 将线索数据转换为 CRM Lead 格式
│   ├─ 字段映射（根据 Lead Entity 定义）
│   │   ├─ company_name → companyName (必填)
│   │   ├─ company_type → companyType
│   │   ├─ region → region
│   │   ├─ country → country
│   │   ├─ phone → contactPhone
│   │   ├─ email → contactEmail
│   │   ├─ website → website
│   │   ├─ address → address
│   │   ├─ business_scope → businessScope
│   │   ├─ intent_signals → intentSignals
│   │   ├─ decision_maker_role → decisionMakerRole
│   │   ├─ score → priorityScore (转为整数)
│   │   ├─ priority → priorityLevel (hot/warm/cold)
│   │   ├─ source_url → sourceUrl
│   │   ├─ notes → notes
│   │   └─ status → status (默认 new_lead)
│   ├─ 枚举值转换
│   │   ├─ priority: hot/warm/cold → PriorityLevel enum
│   │   └─ status: new → new_lead (LeadStatus enum)
│   └─ 数据清理
│       ├─ contactPhone 截断到 50 字符
│       ├─ contactEmail 截断到 100 字符
│       └─ 移除无联系方式的数据
├─ 6.3 批量调用 POST /api/leads/import 接口
│   └─ Authorization: Bearer {token}
├─ 6.4 验证导入结果并显示统计
│   ├─ 调用 GET /api/leads 获取总数
│   ├─ 调用 GET /api/leads/stats/by-country 统计
│   └─ 调用 GET /api/leads/stats/by-priority 统计
└─ 6.5 更新本地看板导入状态
│   ├─ 枚举值转换
│   │   ├─ priority: hot/warm/cold → PriorityLevel enum
│   │   └─ status: new → new_lead (LeadStatus enum)
│   └─ 数据清理
│       ├─ contactPhone 截断到 50 字符
│       ├─ contactEmail 截断到 100 字符
│       └─ 移除无联系方式的数据
├─ 6.3 批量调用 POST /api/leads/import 接口
│   └─ Authorization: Bearer {token}
├─ 6.4 验证导入结果并显示统计
│   ├─ 调用 GET /api/leads 获取总数
│   ├─ 调用 GET /api/leads/stats/by-country 统计
│   └─ 调用 GET /api/leads/stats/by-priority 统计
└─ 6.5 更新本地看板导入状态
>>>>>>> 46715c2 (feat: 完善获客数据自动导入到 Lead CRM 系统)
```

---

## 📁 Skill 文件结构

```
wedding-fabric-lead-hunter/
├── SKILL.md                    # 本文件 - 技能说明
├── config/                     # 配置文件
│   ├── icp-wedding-fabric.yaml # ICP 配置
│   └── business-profile.yaml   # 业务配置模板
├── templates/                  # 模板文件
│   ├── lead-template.json      # 线索数据模板
│   └── 获客看板.html            # 看板 HTML 模板
├── scripts/                    # 执行脚本
│   └── search-queries.md       # 搜索关键词列表
├── references/                 # 参考资料
│   ├── wedding-regions.md      # 婚纱产业带介绍
│   └── decision-makers.md      # 决策人角色说明
└── output/                     # 输出目录
    ├── leads.json              # 线索 JSON
    └── 获客看板.html            # 生成的看板 HTML
```

---

## 🎓 使用示例

### 示例 1：基础使用（自动导入）

**用户**:
> "使用 wedding-fabric-lead-hunter 帮我找苏州婚纱厂客户"

**AI 执行**:
1. 加载 ICP 配置
2. 搜索苏州虎丘婚纱厂
3. 评分筛选
4. 生成联系策略
5. 输出看板 HTML 文件
6. **自动调用 `/api/leads/import` 接口导入数据到 CRM**

**AI 会自动执行导入**:
```
📤 正在导入线索到获客系统...
✅ 导入成功! 共导入 X 条线索
```

### 示例 2：指定地区

**用户**:
> "帮我挖掘潮州外贸婚纱厂客户，生成联系策略"

**AI 执行**:
1. 专注于潮州地区搜索
2. 筛选外贸婚纱厂
3. 针对外贸特点生成策略

### 示例 3：指定数量

**用户**:
> "帮我找 30 个六安婚纱产业带的客户"

**AI 执行**:
1. 深挖六安婚纱企业
2. 生成 30+ 条线索
3. 批量联系策略

---

## ⚙️ 配置说明

### ICP 配置 (icp-wedding-fabric.yaml)

定义理想客户画像：

| 维度 | 权重 | 说明 |
|------|------|------|
| 行业匹配 | 25% | 婚纱厂、礼服厂、蕾丝加工厂 |
| 地区匹配 | 20% | 苏州、潮州、六安、广州等 |
| 公司规模 | 15% | 50-300 人中型工厂优先 |
| 采购意向 | 25% | 近期招聘、展会、扩产信号 |
| 活跃度 | 15% | 近期有动态、联系方式完整 |

### 业务配置 (business-profile.yaml)

填写你的公司信息和优势，用于生成个性化联系策略。

---

## 📊 输出文件说明

### leads.json

完整线索 JSON 数据，用于数据存储和后续处理。

### 获客看板.html

交互式看板 HTML 文件，可直接在浏览器中打开使用，功能包括：

| 功能 | 说明 |
|------|------|
| 统计概览 | 总客户数、平均评分、高优先级数量 |
| 筛选功能 | 按地区(苏州/潮州/六安)、优先级筛选 |
| 客户卡片 | 显示公司名称、类型、地址、联系方式、评分 |
| 详情弹窗 | 点击卡片查看完整联系策略 |
| 开场白话术 | 3 套可直接使用的开场白 |
| 联系建议 | 最佳联系时间、跟进频率 |

看板数据字段：

| 字段 | 说明 |
|------|------|
| 公司名称 | 企业全称 |
| 公司类型 | 婚纱厂/礼服厂/加工厂 |
| 所在地 | 详细地址 |
| 联系电话 | 联系方式 |
| 联系邮箱 | 邮箱地址 |
| 决策人角色 | 厂长/采购经理/总经理 |
| 优先评分 | 0-100 分 |
| 为什么是好客户 | 3-5 条具体理由 |
| 价值主张 | 你能提供什么价值 |
| 联系策略 | 如何接触客户 |
| 开场白 1-3 | 可直接使用的话术 |
| 最佳联系时间 | 建议联系时段 |
| 跟进频率 | 跟进节奏建议 |

---

## 🔧 高级用法

### 自定义搜索关键词

编辑 `scripts/search-queries.md` 添加自定义搜索词。

### 调整 ICP 权重

编辑 `config/icp-wedding-fabric.yaml` 调整评分权重。

### 添加新的婚纱产业带

编辑 `references/wedding-regions.md` 添加新地区。

---

## 🔄 自动导入到获客系统

**每次执行完线索挖掘后，自动将数据导入到 Lead CRM 系统。**

### 导入流程

```
线索生成完成 → 自动调用 API → 数据入库 → 显示统计
```

### API 配置

导入脚本默认连接本地 CRM 系统：

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| API 地址 | `http://localhost:8080/api` | 后端服务地址 |
| 用户名 | `admin` | 登录用户 |
| 密码 | `admin123` | 登录密码 |

**修改配置**：编辑 `scripts/import-to-crm.py` 顶部的默认值。

### 字段映射表

根据 Lead CRM 系统的 Lead Entity 定义，原始线索数据 → CRM 数据库字段映射：

| 原始字段 | CRM 字段 | 类型/约束 | 说明 |
|----------|----------|-----------|------|
| company_name | companyName | String (必填) | 公司名称，不能为空 |
| company_type | companyType | String (100) | 公司类型：婚纱厂/礼服厂/加工厂 |
| region | region | String (100) | 地区：虎丘/潮州/六安等 |
| country | country | String (100) | 国家：中国/土耳其/UAE等 |
| phone | contactPhone | String (50) | 联系电话，截断到50字符 |
| email | contactEmail | String (100) | 联系邮箱，截断到100字符 |
| website | website | String | 公司网站 |
| address | address | String (500) | 详细地址 |
| business_scope | businessScope | TEXT | 业务范围/主营业务 |
| intent_signals | intentSignals | TEXT | 意向信号（多个用分号分隔） |
| decision_maker_role | decisionMakerRole | String (100) | 决策人角色：厂长/采购经理 |
| score | priorityScore | Integer | 优先评分 (0-100) |
| priority | priorityLevel | Enum | 优先级：hot/warm/cold |
| source_url | sourceUrl | String (500) | 信息来源链接 |
| notes | notes | TEXT | 备注信息 |
| status | status | Enum | 客户状态：默认 new_lead |

**枚举值说明：**

1. **priorityLevel** (优先级):
   - `hot` - 高优先级（评分 ≥70）
   - `warm` - 中等优先级（评分 50-69）
   - `cold` - 低优先级（评分 <50）

2. **status** (客户状态):
   - `new_lead` - 新线索（默认值）
   - `contacting` - 正在联系
   - `negotiating` - 商务谈判
   - `converted` - 已成交
   - `lost` - 已流失

**数据清理规则：**
- `contactPhone` 字段截断到 50 字符
- `contactEmail` 字段截断到 100 字符
- 移除无联系方式（电话和邮箱都为空）的数据
- 自动添加 `status: "new_lead"` 和 `createdAt/updatedAt` 时间戳

### 手动导入

如果需要单独导入已有线索文件：

```bash
# 导入 JSON 文件
python3 ~/.openclaw/workspace/skills/wedding-fabric-lead-hunter/scripts/import-to-crm.py leads.json

# 只查看统计
python3 ~/.openclaw/workspace/skills/wedding-fabric-lead-hunter/scripts/import-to-crm.py --stats

# 指定 API 地址
python3 ~/.openclaw/workspace/skills/wedding-fabric-lead-hunter/scripts/import-to-crm.py leads.json --api http://your-server:8080/api
```

### 导入结果验证

导入完成后，AI 会显示：

```
✅ 导入成功! 共导入 37 条线索

📈 数据库最新统计:
   总线索数: 150 条
   
按国家:
   中国: 80 条
   土耳其: 30 条
   阿联酋: 20 条

按优先级:
   hot: 45 条
   warm: 68 条
```

---

## ⚠️ 采集约束 (CRITICAL)

**必须包含联系方式，否则不采集：**

| 必填字段 | 说明 |
|----------|------|
| 手机号/电话 | 至少一个有效电话号码 |
| 邮箱 | 或至少一个有效邮箱地址 |

**校验规则：**
- 电话：7-15位数字，可包含 `-`、`+`、空格
- 邵箱：标准邮箱格式

**无联系方式时：**
- 自动跳过，不采集该线索
- 不计入输出统计

---

## 💾 数据存储

### 本地存储路径

```
~/.openclaw/workspace/skills/wedding-fabric-lead-hunter/
└── data/
    ├── lead-dashboard.json      # 看板主文件（增量累积）
    ├── leads-history/           # 历史线索归档
    │   ├── 2026-04-03.json
    │   ├── 2026-04-06.json
    │   └── ...
    └── stats.json               # 统计数据
```

### 看板增量更新

每次执行新增数据到看板，不覆盖历史数据：

- **累积模式**: `append` - 新线索追加到看板
- **自动去重**: 按 `公司名 + 电话` 判断重复
- **数据保留**: 90天历史数据

---

## 📊 获客看板

看板数据结构 (`lead-dashboard.json`):

```json
{
  "generated_at": "2026-04-03T03:00:00",
  "total_leads": 150,
  "by_priority": {
    "hot": 45,
    "warm": 68,
    "cold": 37
  },
  "by_region": {
    "苏州虎丘": 60,
    "潮州": 40,
    "六安": 30,
    "广州": 20
  },
  "leads": [
    {
      "id": "lead-001",
      "company_name": "苏州XX婚纱厂",
      "phone": "13800138000",
      "email": "contact@example.com",
      "score": 85,
      "priority": "hot",
      "contact_strategy": "...",
      "first_seen": "2026-04-03T03:00:00",
      "last_updated": "2026-04-06T06:00:00"
    }
  ]
}
```

---

## ⏰ 定时任务 (Cron)

**自动执行频率**: 每 3 小时

| 时间点 | 执行内容 |
|--------|----------|
| 00:00 | 搜索苏州虎丘婚纱厂 |
| 03:00 | 搜索潮州外贸婚纱厂 |
| 06:00 | 搜索六安婚纱产业带 |
| 09:00 | 搜索广州婚纱企业 |
| 12:00 | 评分筛选 + 去重 |
| 15:00 | 生成联系策略 |
| 18:00 | 更新看板数据 |
| 21:00 | 输出统计报告 |

**手动触发：**

告诉 AI：

> "执行 wedding-fabric-lead-hunter 定时任务"

---

## 🔄 自动更新机制

本 Skill 从 Git 仓库同步，保持最新版本：

- **Git 仓库**: `git@github.com:Geooo030/agent_skill.git`
- **更新策略**: `pull` (从仓库拉取最新代码)

### 如何更新 Skill

**方式一：手动更新**

```bash
cd ~/.openclaw/workspace/skills/wedding-fabric-lead-hunter
git pull origin main
```

**方式二：AI 自动更新**

告诉 AI：

> "更新 wedding-fabric-lead-hunter skill 到最新版本"

AI 会自动执行 `git pull` 拉取最新代码。

### 更新检查频率

建议每周检查一次更新，或在以下情况更新：

- 新功能发布时
- ICP 配置优化后
- 搜索关键词库扩充后

---

## 💡 最佳实践

1. **定期执行** - 每月执行一次，获取最新线索
2. **优先跟进 Hot 线索** - 评分 ≥70 的客户优先联系
3. **结合线下展会** - 展会后执行搜索，获取参展企业信息
4. **多渠道触达** - 电话 + 微信 + 邮件组合使用

---

## 📞 支持与反馈

如有问题或建议，请联系 ClawDBot 团队。

---

## 🤖 AI 执行时的自动导入

**重要：当 AI 执行 wedding-fabric-lead-hunter 技能时，必须在最后自动将数据导入到获客系统。**

### 导入执行流程

```
生成线索报告后 → AI 自动执行以下步骤:

1. 读取生成的 lead-dashboard.json 或 leads.json

2. 调用 CRM API 登录获取 token
   POST http://localhost:8080/api/auth/login
   Headers: {"Content-Type": "application/json"}
   Body: {"username": "admin", "password": "admin123"}
   
   Response: {"success": true, "data": {"token": "eyJhbG..."}}

3. 将线索数据转换为 CRM Lead 格式:
   
   示例转换:
   {
     // 原始数据
     "company_name": "苏州XX婚纱厂",
     "company_type": "婚纱厂",
     "region": "虎丘",
     "country": "中国",
     "phone": "13800138000",
     "email": "contact@example.com",
     "website": "http://example.com",
     "address": "苏州市虎丘区...",
     "business_scope": "婚纱生产、定制",
     "intent_signals": "近期扩产;招聘采购",
     "decision_maker_role": "厂长",
     "score": 85,
     "priority": "hot",
     "source_url": "http://...",
     "notes": "优质客户"
   }
   
   转换为 CRM 格式:
   {
     "companyName": "苏州XX婚纱厂",
     "companyType": "婚纱厂",
     "region": "虎丘",
     "country": "中国",
     "contactPhone": "13800138000",
     "contactEmail": "contact@example.com",
     "website": "http://example.com",
     "address": "苏州市虎丘区...",
     "businessScope": "婚纱生产、定制",
     "intentSignals": "近期扩产;招聘采购",
     "decisionMakerRole": "厂长",
     "priorityScore": 85,
     "priorityLevel": "hot",
     "sourceUrl": "http://...",
     "notes": "优质客户",
     "status": "new_lead"
   }

4. 批量导入:
   POST http://localhost:8080/api/leads/import
   Headers: {
     "Authorization": "Bearer eyJhbG...",
     "Content-Type": "application/json"
   }
   Body: [{...lead1}, {...lead2}, ...]

5. 验证导入结果并报告:
   ✅ 导入成功! 共导入 X 条线索
   
   查询统计:
   GET http://localhost:8080/api/leads/stats/by-country
   GET http://localhost:8080/api/leads/stats/by-priority
```

### 导入命令

AI 在执行完线索挖掘后，**必须**运行以下命令完成导入：

**方式一：通过 curl 直接调用 API（推荐）**

```bash
# 步骤 1: 登录获取 JWT token
TOKEN=$(curl -s -X POST http://localhost:8080/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}' \
  | jq -r '.data.token')

echo "✅ 登录成功，获取到 token"

# 步骤 2: 将 lead-dashboard.json 转换为 CRM 格式并导入
# 需要先将原始线索数据转换为符合 Lead Entity 的格式
python3 ~/.openclaw/workspace/skills/wedding-fabric-lead-hunter/scripts/convert-and-import.py \
  --input ~/.openclaw/workspace/skills/wedding-fabric-lead-hunter/data/lead-dashboard.json \
  --token "$TOKEN"

# 步骤 3: 验证导入结果
curl -s -X GET http://localhost:8080/api/leads \
  -H "Authorization: Bearer $TOKEN" \
  | jq '.data.totalElements'
```

**方式二：使用 Python 转换脚本**

```bash
# 创建转换脚本（如果 scripts 目录中不存在）
python3 ~/.openclaw/workspace/skills/wedding-fabric-lead-hunter/scripts/import-to-crm.py \
  ~/.openclaw/workspace/skills/wedding-fabric-lead-hunter/data/lead-dashboard.json
```

**API 地址配置：**
- 默认地址：`http://localhost:8080/api`
- 生产环境：`http://43.155.154.87:8080/api`

### 导入成功示例输出

```
============================================================
婚纱线索导入工具 (Lead CRM Importer)
============================================================

🔐 正在登录系统...
   ✅ 登录成功! Token: eyJhbG...

📦 正在加载线索文件: lead-dashboard.json
   共加载 20 条线索

📊 线索分布:
   中国: 12 条
   土耳其: 5 条
   UAE: 3 条

📤 正在转换数据格式...
   ✅ 已转换 20 条数据为 CRM Lead 格式

📤 正在导入 20 条线索到 CRM...
   POST http://localhost:8080/api/leads/import
   ✅ 导入成功! 共导入 20 条线索

📈 数据库最新统计:
   
   总线索数: 57 条
   
   按国家分布:
   GET /api/leads/stats/by-country
   - 中国: 30 条
   - 土耳其: 15 条
   - UAE: 12 条
   
   按优先级分布:
   GET /api/leads/stats/by-priority
   - hot: 20 条
   - warm: 27 条
   - cold: 10 条

✅ 导入完成! 可在前端查看: http://43.155.154.87:3000
============================================================
```

---

## 📝 转换脚本示例

创建 `scripts/convert-and-import.py` 文件，实现数据转换和导入：

```python
#!/usr/bin/env python3
"""
Lead CRM 导入脚本
将 wedding-fabric-lead-hunter 的线索数据转换为 CRM Lead 格式并导入
"""

import json
import requests
import argparse
from typing import List, Dict

# API 配置
API_BASE_URL = "http://localhost:8080/api"
AUTH_URL = f"{API_BASE_URL}/auth/login"
IMPORT_URL = f"{API_BASE_URL}/leads/import"
STATS_URL = f"{API_BASE_URL}/leads/stats"

# 登录配置
USERNAME = "admin"
PASSWORD = "admin123"

def login() -> str:
    """登录获取 JWT token"""
    response = requests.post(
        AUTH_URL,
        json={"username": USERNAME, "password": PASSWORD},
        headers={"Content-Type": "application/json"}
    )
    data = response.json()
    if data.get("success"):
        return data["data"]["token"]
    else:
        raise Exception("登录失败: " + data.get("message", "未知错误"))

def convert_lead(original: Dict) -> Dict:
    """将原始线索数据转换为 CRM Lead 格式"""
    return {
        "companyName": original.get("company_name"),
        "companyType": original.get("company_type"),
        "country": original.get("country"),
        "region": original.get("region"),
        "address": original.get("address", ""),
        "contactPhone": original.get("phone", "")[:50] if original.get("phone") else "",
        "contactEmail": original.get("email", "")[:100] if original.get("email") else "",
        "website": original.get("website", ""),
        "businessScope": original.get("business_scope", ""),
        "intentSignals": original.get("intent_signals", ""),
        "decisionMakerRole": original.get("decision_maker_role", ""),
        "priorityScore": int(original.get("score", 0)),
        "priorityLevel": original.get("priority", "warm"),
        "sourceUrl": original.get("source_url", ""),
        "notes": original.get("notes", ""),
        "status": "new_lead"  # 默认为新线索
    }

def import_leads(leads: List[Dict], token: str) -> int:
    """批量导入线索到 CRM"""
    response = requests.post(
        IMPORT_URL,
        json=leads,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )
    data = response.json()
    if data.get("success"):
        return data["data"]
    else:
        raise Exception("导入失败: " + data.get("message", "未知错误"))

def get_stats(token: str):
    """获取导入后的统计数据"""
    headers = {"Authorization": f"Bearer {token}"}
    
    # 获取总数
    response = requests.get(f"{API_BASE_URL}/leads", headers=headers)
    total = response.json()["data"]["totalElements"]
    
    # 按国家统计
    response = requests.get(f"{STATS_URL}/by-country", headers=headers)
    by_country = response.json()["data"]
    
    # 按优先级统计
    response = requests.get(f"{STATS_URL}/by-priority", headers=headers)
    by_priority = response.json()["data"]
    
    return total, by_country, by_priority

def main():
    parser = argparse.ArgumentParser(description="导入线索到 Lead CRM")
    parser.add_argument("--input", required=True, help="输入文件路径")
    parser.add_argument("--token", help="JWT token (可选)")
    args = parser.parse_args()
    
    print("=" * 60)
    print("婚纱线索导入工具 (Lead CRM Importer)")
    print("=" * 60)
    
    # 登录
    print("\n🔐 正在登录系统...")
    token = args.token or login()
    print("   ✅ 登录成功! Token:", token[:20] + "...")
    
    # 加载线索数据
    print(f"\n📦 正在加载线索文件: {args.input}")
    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 提取线索列表
    if "leads" in data:
        leads_data = data["leads"]
    else:
        leads_data = data if isinstance(data, list) else []
    
    print(f"   共加载 {len(leads_data)} 条线索")
    
    # 过滤无效数据（无联系方式）
    valid_leads = [
        lead for lead in leads_data
        if lead.get("phone") or lead.get("email")
    ]
    
    print(f"\n📊 有效线索: {len(valid_leads)} 条")
    
    # 转换数据格式
    print("\n📤 正在转换数据格式...")
    crm_leads = [convert_lead(lead) for lead in valid_leads]
    print(f"   ✅ 已转换 {len(crm_leads)} 条数据为 CRM Lead 格式")
    
    # 批量导入
    print(f"\n📤 正在导入 {len(crm_leads)} 条线索到 CRM...")
    imported_count = import_leads(crm_leads, token)
    print(f"   ✅ 导入成功! 共导入 {imported_count} 条线索")
    
    # 获取统计
    print("\n📈 数据库最新统计:")
    total, by_country, by_priority = get_stats(token)
    print(f"   总线索数: {total} 条")
    
    print("\n   按国家分布:")
    for country, count in by_country:
        print(f"   - {country}: {count} 条")
    
    print("\n   按优先级分布:")
    for priority, count in by_priority:
        print(f"   - {priority}: {count} 条")
    
    print("\n✅ 导入完成! 可在前端查看: http://43.155.154.87:3000")
    print("=" * 60)

if __name__ == "__main__":
    main()
```

**使用方法：**

```bash
# 创建脚本文件
cat > ~/.openclaw/workspace/skills/wedding-fabric-lead-hunter/scripts/convert-and-import.py << 'EOF'
[上述代码内容]
EOF

# 运行脚本
python3 ~/.openclaw/workspace/skills/wedding-fabric-lead-hunter/scripts/convert-and-import.py \
  --input ~/.openclaw/workspace/skills/wedding-fabric-lead-hunter/data/lead-dashboard.json
```

---

*让获客更简单，让生意更好做。* 👰