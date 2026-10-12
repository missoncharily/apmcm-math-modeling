# APMCM数学建模竞赛论文资料库

## 数据库结构

### papers_database.json
包含2022-2025年APMCM竞赛优秀论文的结构化数据：

- **id**: 论文唯一标识符 (格式: YYYY-X)
- **year**: 年份
- **problem**: 题目编号 (A/B/C/D/E)
- **title**: 论文标题
- **file_path**: PDF文件完整路径
- **problem_type**: 问题类型 (优化问题/数据分析/预测建模/评价问题等)
- **methods**: 使用的建模方法列表
- **keywords**: 关键词标签
- **structure_notes**: 论文结构和亮点笔记

## 使用方法

### 1. 查询论文
```python
import json

with open('papers_database.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# 按年份查询
papers_2025 = [p for p in db['papers'] if p['year'] == 2025]

# 按问题编号查询
problem_a = [p for p in db['papers'] if p['problem'] == 'A']
```

### 2. 更新论文信息
手动分析PDF后，更新对应条目的字段：
- problem_type: 标注问题类型
- methods: 添加使用的方法
- keywords: 提取关键词
- structure_notes: 记录论文特色

### 3. 使用Claude Code Skill
调用 `/mathmodel` skill来辅助论文写作和问题分析。

## 论文统计

- 2022年: 5篇 (A-E题)
- 2023年: 3篇 (A-C题)
- 2024年: 4篇 (A-D题)
- 2025年: 4篇 (A-D题)
- **总计: 16篇优秀论文**

## 待完成任务

- [ ] 安装PDF阅读工具以提取论文内容
- [ ] 分析每篇论文的问题类型和方法
- [ ] 提取论文关键词和建模技巧
- [ ] 建立方法论知识图谱
- [ ] 创建问题类型分类索引
