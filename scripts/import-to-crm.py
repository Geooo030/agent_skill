#!/usr/bin/env python3
"""
婚纱客户线索导入到 Lead CRM 系统
将生成的线索数据通过 API 批量导入到数据库

使用方式:
    python3 import-to-crm.py leads.json
    python3 import-to-crm.py --file leads.json --api http://localhost:8080/api
"""

import json
import sys
import os
import uuid
import requests
from datetime import datetime

# 默认 API 配置
DEFAULT_API_BASE = "http://localhost:8080/api"
DEFAULT_USER = "admin"
DEFAULT_PASS = "admin123"

class LeadCRMImporter:
    """线索导入器"""
    
    def __init__(self, api_base=None, username=None, password=None):
        self.api_base = api_base or DEFAULT_API_BASE
        self.username = username or DEFAULT_USER
        self.password = password or DEFAULT_PASS
        self.token = None
    
    def login(self):
        """登录获取 JWT token"""
        url = f"{self.api_base}/auth/login"
        response = requests.post(url, json={
            "username": self.username,
            "password": self.password
        })
        if response.status_code == 200:
            data = response.json()
            self.token = data["data"]["token"]
            return True
        else:
            print(f"❌ 登录失败: {response.text}")
            return False
    
    def transform_lead(self, raw_lead):
        """将原始线索转换为 CRM 格式
        
        支持多种数据格式：
        - wedding-fabric-lead-hunter 格式
        - lead-hunter 格式
        - 手动录入格式
        
        注意：每次导入都生成新的 UUID，避免 ID 冲突
        """
        # 始终生成新的 UUID（避免与已有数据冲突）
        lead_id = str(uuid.uuid4())
        
        # 处理意向信号 - 从数组转为字符串
        intent_signals = raw_lead.get("intent_signals", [])
        if isinstance(intent_signals, list):
            intent_signals = ";".join(intent_signals)
        elif isinstance(intent_signals, str):
            intent_signals = intent_signals
        
        # 处理优先级 - 支持多种字段名
        priority_level = raw_lead.get("priority_level") or raw_lead.get("priority") or "warm"
        if priority_level not in ["hot", "warm", "cold"]:
            priority_level = "warm"
        
        # 处理评分 - 支持多种字段名，确保是整数
        priority_score = raw_lead.get("priority_score") or raw_lead.get("score") or 0
        if isinstance(priority_score, str):
            try:
                priority_score = int(priority_score)
            except ValueError:
                priority_score = 0
        priority_score = int(priority_score)
        
        # 处理状态
        status = raw_lead.get("status", "new")
        # CRM 使用的状态枚举
        status_map = {
            "new": "new_lead",
            "new_lead": "new_lead",
            "contacting": "contacting",
            "negotiating": "negotiating",
            "converted": "converted",
            "lost": "lost"
        }
        status = status_map.get(status, "new_lead")
        
        # 处理联系方式 - 支持多种字段名，截断过长的电话号码
        phone = raw_lead.get("contact_phone") or raw_lead.get("phone") or raw_lead.get("whatsapp") or ""
        # 如果电话号码包含多个号码，只取第一个
        if phone and len(phone) > 50:
            # 尝试提取第一个电话号码
            phones = phone.split(",")
            if phones:
                phone = phones[0].strip()
            # 如果还是太长，截断
            if len(phone) > 50:
                phone = phone[:50]
        email = raw_lead.get("contact_email") or raw_lead.get("email") or ""
        
        # 处理地址 - 支持多种字段名
        address = raw_lead.get("address") or raw_lead.get("location") or ""
        
        # 处理业务描述 - 支持多种字段名
        business_scope = raw_lead.get("business_scope") or raw_lead.get("business_description") or ""
        
        # 处理决策人 - 支持多种字段名
        decision_maker = raw_lead.get("decision_maker_role") or raw_lead.get("decision_maker") or ""
        
        # 处理网站 URL - 截断过长的 URL
        website = raw_lead.get("website") or ""
        if len(website) > 255:
            website = website[:255]
        
        # 处理来源 URL - 支持多种字段名，截断过长
        source_url = raw_lead.get("source_url") or raw_lead.get("website") or ""
        if len(source_url) > 500:
            source_url = source_url[:500]
        
        # 处理备注 - 可合并 why_good_lead 和 contact_strategy
        notes = raw_lead.get("notes") or ""
        if raw_lead.get("why_good_lead"):
            notes = f"{notes}\n为什么是好客户: {raw_lead.get('why_good_lead')}"
        if raw_lead.get("contact_strategy"):
            notes = f"{notes}\n联系策略: {raw_lead.get('contact_strategy')}"
        
        # 构建 CRM 格式的线索
        crm_lead = {
            "id": lead_id,
            "companyName": raw_lead.get("company_name", ""),
            "companyType": raw_lead.get("company_type", ""),
            "country": raw_lead.get("country", "中国"),
            "region": raw_lead.get("region", ""),
            "address": address,
            "contactPhone": phone,
            "contactEmail": email,
            "website": raw_lead.get("website", ""),
            "businessScope": business_scope,
            "intentSignals": intent_signals,
            "decisionMakerRole": decision_maker,
            "priorityScore": priority_score,
            "priorityLevel": priority_level,
            "sourceUrl": source_url,
            "notes": notes.strip(),
            "status": status
        }
        
        return crm_lead
    
    def import_leads(self, leads):
        """批量导入线索"""
        if not self.token:
            print("❌ 未登录，请先调用 login()")
            return None
        
        # 转换线索格式
        crm_leads = [self.transform_lead(lead) for lead in leads]
        
        url = f"{self.api_base}/leads/import"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=crm_leads)
        return response.json()
    
    def get_stats(self):
        """获取导入统计"""
        if not self.token:
            return None
        
        headers = {"Authorization": f"Bearer {self.token}"}
        
        # 按国家统计
        country_stats = requests.get(
            f"{self.api_base}/leads/stats/by-country",
            headers=headers
        ).json()
        
        # 按优先级统计
        priority_stats = requests.get(
            f"{self.api_base}/leads/stats/by-priority",
            headers=headers
        ).json()
        
        return {
            "by_country": country_stats.get("data", []),
            "by_priority": priority_stats.get("data", [])
        }


def load_leads_from_file(filepath):
    """从文件加载线索数据"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 支持多种格式
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        # 可能是看板格式
        if "leads" in data:
            return data["leads"]
        else:
            return [data]
    else:
        return []


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='导入婚纱线索到 CRM 系统')
    parser.add_argument('file', nargs='?', help='线索 JSON 文件路径')
    parser.add_argument('--api', default=DEFAULT_API_BASE, help='API 地址')
    parser.add_argument('--user', default=DEFAULT_USER, help='用户名')
    parser.add_argument('--pass', dest='password', default=DEFAULT_PASS, help='密码')
    parser.add_argument('--stats', action='store_true', help='只显示统计信息')
    
    args = parser.parse_args()
    
    # 创建导入器
    importer = LeadCRMImporter(
        api_base=args.api,
        username=args.user,
        password=args.password
    )
    
    print("=" * 60)
    print("婚纱线索导入工具 (Lead CRM Importer)")
    print("=" * 60)
    
    # 登录
    print("\n🔐 正在登录系统...")
    if not importer.login():
        sys.exit(1)
    print("   ✅ 登录成功!")
    
    # 如果只是查看统计
    if args.stats:
        stats = importer.get_stats()
        print("\n📊 当前数据库统计:")
        print("\n按国家:")
        for item in stats.get("by_country", []):
            print(f"   {item[0]}: {item[1]} 条")
        print("\n按优先级:")
        for item in stats.get("by_priority", []):
            print(f"   {item[0]}: {item[1]} 条")
        return
    
    # 导入文件
    if not args.file:
        print("\n❌ 请提供线索文件路径")
        print("   使用方式: python3 import-to-crm.py leads.json")
        sys.exit(1)
    
    # 加载线索
    print(f"\n📦 正在加载线索文件: {args.file}")
    leads = load_leads_from_file(args.file)
    
    if not leads:
        print("   ❌ 未找到线索数据")
        sys.exit(1)
    
    print(f"   共加载 {len(leads)} 条线索")
    
    # 按国家统计
    countries = {}
    for lead in leads:
        c = lead.get("country", lead.get("region", "Unknown"))
        countries[c] = countries.get(c, 0) + 1
    
    print("\n📊 线索分布:")
    for c, n in sorted(countries.items(), key=lambda x: -x[1]):
        print(f"   {c}: {n} 条")
    
    # 导入
    print(f"\n📤 正在导入 {len(leads)} 条线索到 CRM...")
    result = importer.import_leads(leads)
    
    if result and result.get("success"):
        imported = result.get("data", 0)
        print(f"\n✅ 导入成功! 共导入 {imported} 条线索")
        
        # 显示最新统计
        stats = importer.get_stats()
        print("\n📈 数据库最新统计:")
        total = sum(item[1] for item in stats.get("by_country", []))
        print(f"   总线索数: {total} 条")
    else:
        print(f"\n❌ 导入失败: {result}")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("导入完成!")
    print("=" * 60)


if __name__ == "__main__":
    main()