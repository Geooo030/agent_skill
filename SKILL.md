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

AI 会自动执行完整的获客流程。

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

### 示例 1：基础使用

**用户**:
> "使用 wedding-fabric-lead-hunter 帮我找苏州婚纱厂客户"

**AI 执行**:
1. 加载 ICP 配置
2. 搜索苏州虎丘婚纱厂
3. 评分筛选
4. 生成联系策略
5. 输出看板 HTML 文件

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

*让获客更简单，让生意更好做。* 👰