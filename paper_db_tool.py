#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数学建模论文数据库查询工具
用于快速检索和分析APMCM历年优秀论文
"""

import json
from pathlib import Path
from typing import List, Dict, Optional

class PaperDatabase:
    def __init__(self, db_path: str = "papers_database.json"):
        """初始化数据库"""
        with open(db_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.papers = self.data['papers']

    def get_by_year(self, year: int) -> List[Dict]:
        """按年份查询论文"""
        return [p for p in self.papers if p['year'] == year]

    def get_by_problem(self, problem: str) -> List[Dict]:
        """按题号查询论文"""
        return [p for p in self.papers if p['problem'] == problem.upper()]

    def get_by_id(self, paper_id: str) -> Optional[Dict]:
        """按ID查询单篇论文"""
        for p in self.papers:
            if p['id'] == paper_id:
                return p
        return None

    def get_by_method(self, method: str) -> List[Dict]:
        """按方法查询论文"""
        return [p for p in self.papers
                if method.lower() in [m.lower() for m in p.get('methods', [])]]

    def get_by_type(self, problem_type: str) -> List[Dict]:
        """按问题类型查询论文"""
        return [p for p in self.papers
                if problem_type in p.get('problem_type', '')]

    def list_all_years(self) -> List[int]:
        """列出所有年份"""
        return sorted(set(p['year'] for p in self.papers))

    def list_all_methods(self) -> List[str]:
        """列出所有已标注的方法"""
        methods = set()
        for p in self.papers:
            methods.update(p.get('methods', []))
        return sorted(methods)

    def statistics(self) -> Dict:
        """数据库统计信息"""
        years = {}
        for p in self.papers:
            year = p['year']
            years[year] = years.get(year, 0) + 1

        analyzed = sum(1 for p in self.papers if p.get('methods'))

        return {
            'total': len(self.papers),
            'by_year': years,
            'analyzed': analyzed,
            'unanalyzed': len(self.papers) - analyzed
        }

    def search(self, keyword: str) -> List[Dict]:
        """全文搜索（标题、关键词、笔记）"""
        results = []
        kw_lower = keyword.lower()
        for p in self.papers:
            if (kw_lower in p['title'].lower() or
                kw_lower in ' '.join(p.get('keywords', [])).lower() or
                kw_lower in p.get('structure_notes', '').lower()):
                results.append(p)
        return results


def load_knowledge_base(kb_path: str = "knowledge_base.json") -> Dict:
    """加载知识库"""
    with open(kb_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def classify_problem(description: str, kb: Dict) -> List[str]:
    """
    根据问题描述自动分类
    返回可能的问题类型列表
    """
    desc_lower = description.lower()
    matches = []

    for ptype_key, ptype_data in kb['problem_types'].items():
        keywords = ptype_data['keywords']
        if any(kw in desc_lower for kw in keywords):
            matches.append(ptype_data['name'])

    return matches


def suggest_methods(problem_type: str, kb: Dict) -> List[Dict]:
    """根据问题类型推荐建模方法"""
    for ptype_key, ptype_data in kb['problem_types'].items():
        if ptype_data['name'] == problem_type:
            return ptype_data['methods']
    return []


# 使用示例
if __name__ == "__main__":
    # 初始化数据库
    db = PaperDatabase()

    # 统计信息
    print("=== 数据库统计 ===")
    stats = db.statistics()
    print(f"总论文数: {stats['total']}")
    print(f"已分析: {stats['analyzed']}")
    print(f"未分析: {stats['unanalyzed']}")
    print(f"年份分布: {stats['by_year']}")
    print()

    # 查询示例
    print("=== 2025年论文 ===")
    papers_2025 = db.get_by_year(2025)
    for p in papers_2025:
        print(f"{p['id']}: {p['title']}")
    print()

    # 加载知识库
    kb = load_knowledge_base()

    # 问题分类示例
    print("=== 问题分类示例 ===")
    test_desc = "预测未来三年的销售额，并进行敏感性分析"
    types = classify_problem(test_desc, kb)
    print(f"问题描述: {test_desc}")
    print(f"可能类型: {types}")
    print()

    # 方法推荐
    if types:
        print(f"=== {types[0]} 推荐方法 ===")
        methods = suggest_methods(types[0], kb)
        for m in methods:
            print(f"- {m['name']}: {m['applicable']}")
            print(f"  工具: {', '.join(m['tools'])}")
