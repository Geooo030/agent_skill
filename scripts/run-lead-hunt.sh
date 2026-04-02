#!/bin/bash
# 婚纱布料获客流程执行脚本
# 使用方法: ./run-lead-hunt.sh [地区] [数量]

set -e

echo "══════════════════════════════════════════════════════════════"
echo "           婚纱布料获客专家 - Wedding Fabric Lead Hunter"
echo "══════════════════════════════════════════════════════════════"

# 检查前置技能
echo ""
echo "📋 Phase 1: 检查前置技能..."
echo ""

if ! clawhub list | grep -q "lead-hunter"; then
    echo "⚠️  lead-hunter 未安装，正在安装..."
    clawhub install lead-hunter --force
fi

if ! clawhub list | grep -q "lead-research-assistant-cn"; then
    echo "⚠️  lead-research-assistant-cn 未安装，正在安装..."
    clawhub install lead-research-assistant-cn --force
fi

echo "✅ 前置技能检查完成"
echo ""

# 显示使用说明
echo "══════════════════════════════════════════════════════════════"
echo "📖 使用说明"
echo "══════════════════════════════════════════════════════════════"
echo ""
echo "直接在对话中使用以下命令："
echo ""
echo "1. 挖掘线索:"
echo "   \"使用 wedding-fabric-lead-hunter 帮我挖掘苏州婚纱厂客户\""
echo ""
echo "2. 指定地区和数量:"
echo "   \"帮我找 30 个潮州外贸婚纱厂客户\""
echo ""
echo "3. 生成联系策略:"
echo "   \"为高优先级客户生成联系策略并输出 Excel\""
echo ""
echo "══════════════════════════════════════════════════════════════"
echo ""
echo "📁 Skill 文件位置: /root/.openclaw/workspace/skills/wedding-fabric-lead-hunter/"
echo ""
echo "📂 输出文件位置: /root/.openclaw/workspace/skills/wedding-fabric-lead-hunter/output/"
echo ""
echo "══════════════════════════════════════════════════════════════"