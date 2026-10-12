# 数学建模论文数据库更新指南

## 📋 更新流程

### 当你阅读了一篇优秀论文后，按以下步骤更新数据库：

## 1. 分析论文内容

### 1.1 识别问题类型
阅读论文的"问题分析"部分，确定问题属于：
- ✅ **优化问题**: 求最大/最小值，资源分配
- ✅ **预测问题**: 时间序列，趋势预测
- ✅ **评价问题**: 多指标综合评价，排序
- ✅ **分类问题**: 聚类分析，模式识别
- ✅ **微分方程**: 传播模型，动态演化
- ✅ **图论网络**: 路径规划，网络分析

### 1.2 提取建模方法
记录论文使用的主要方法（按重要性排序）：
```
例如：
- 主要方法：ARIMA时间序列模型
- 辅助方法：灰色预测GM(1,1)
- 优化算法：粒子群算法PSO
```

### 1.3 提取关键词
从以下来源提取关键词：
- 论文摘要中的关键词
- 问题的核心概念
- 使用的主要技术

### 1.4 记录结构亮点
注意论文的特色部分：
```
- 创新点：XXX
- 图表质量：XXX
- 敏感性分析方法：XXX
- 代码规范性：XXX
```

## 2. 更新 papers_database.json

### 找到对应论文条目
```json
{
  "id": "2025-A",
  "year": 2025,
  "problem": "A",
  "title": "2025年A题优秀论文",
  "file_path": "D:\\竞赛资料\\...",
  "problem_type": "未分析",  // 👈 更新这里
  "methods": [],              // 👈 更新这里
  "keywords": [],             // 👈 更新这里
  "structure_notes": ""       // 👈 更新这里
}
```

### 更新为完整信息
```json
{
  "id": "2025-A",
  "year": 2025,
  "problem": "A",
  "title": "2025年A题优秀论文",
  "file_path": "D:\\竞赛资料\\...",
  "problem_type": "预测问题+优化问题",
  "methods": [
    "ARIMA时间序列",
    "灰色预测GM(1,1)",
    "粒子群算法PSO",
    "蒙特卡洛模拟"
  ],
  "keywords": [
    "需求预测",
    "库存优化",
    "多目标优化",
    "敏感性分析"
  ],
  "structure_notes": "创新点：将预测和优化结合，建立了两阶段模型。图表质量高，敏感性分析详细。代码注释清晰。"
}
```

## 3. 更新 knowledge_base.json（可选）

### 如果发现新方法或新应用场景

在对应问题类型下添加方法：
```json
{
  "name": "新方法名称",
  "applicable": "适用场景描述",
  "tools": ["Python库1", "Python库2"]
}
```

## 4. 验证更新

### 使用Python工具验证
```python
from paper_db_tool import PaperDatabase

db = PaperDatabase("papers_database.json")

# 查看统计
stats = db.statistics()
print(f"已分析: {stats['analyzed']}/{stats['total']}")

# 查看更新的论文
paper = db.get_by_id("2025-A")
print(paper)

# 测试方法查询
papers = db.get_by_method("ARIMA")
print(f"使用ARIMA的论文: {len(papers)}篇")
```

## 5. 更新示例

### 示例1：优化问题论文
```json
{
  "id": "2024-B",
  "problem_type": "多目标优化问题",
  "methods": [
    "遗传算法NSGA-II",
    "层次分析法AHP",
    "帕累托前沿分析"
  ],
  "keywords": [
    "多目标优化",
    "权衡分析",
    "决策支持"
  ],
  "structure_notes": "使用NSGA-II求解多目标问题，图表展示了帕累托前沿。模型检验部分用了对比实验。"
}
```

### 示例2：评价问题论文
```json
{
  "id": "2023-C",
  "problem_type": "综合评价问题",
  "methods": [
    "层次分析法AHP",
    "熵权法",
    "TOPSIS",
    "主成分分析PCA"
  ],
  "keywords": [
    "综合评价",
    "指标体系",
    "权重确定",
    "主客观赋权"
  ],
  "structure_notes": "结合主观AHP和客观熵权法，构建了组合赋权模型。指标体系设计合理，一致性检验完整。"
}
```

### 示例3：预测问题论文
```json
{
  "id": "2022-D",
  "problem_type": "时间序列预测",
  "methods": [
    "ARIMA",
    "LSTM神经网络",
    "Prophet",
    "模型集成"
  ],
  "keywords": [
    "时间序列",
    "深度学习",
    "预测精度",
    "模型对比"
  ],
  "structure_notes": "对比了统计方法和深度学习方法，使用加权平均进行模型集成。预测结果可视化清晰，包含置信区间。"
}
```

## 6. 批量更新模板

如果需要快速更新多篇论文，可以创建更新脚本：

```python
import json

# 待更新的论文信息
updates = [
    {
        "id": "2025-A",
        "problem_type": "预测+优化",
        "methods": ["ARIMA", "遗传算法"],
        "keywords": ["需求预测", "库存优化"],
        "structure_notes": "两阶段模型，结构清晰"
    },
    # 添加更多...
]

# 读取数据库
with open('papers_database.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# 批量更新
for update in updates:
    for paper in db['papers']:
        if paper['id'] == update['id']:
            paper.update(update)
            print(f"已更新: {update['id']}")

# 保存
with open('papers_database.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("批量更新完成！")
```

## 7. 数据质量检查

### 检查项目：
- [ ] 所有字段都已填写
- [ ] methods列表按重要性排序
- [ ] keywords数量3-6个
- [ ] structure_notes简洁有重点
- [ ] problem_type准确分类
- [ ] JSON格式正确（无语法错误）

### 运行检查脚本：
```python
from paper_db_tool import PaperDatabase

db = PaperDatabase()

# 检查未完成的条目
for paper in db.papers:
    if not paper['methods']:
        print(f"⚠️ {paper['id']} 未分析")
    elif len(paper['keywords']) < 3:
        print(f"⚠️ {paper['id']} 关键词过少")
```

## 8. 定期维护

### 每次比赛后：
1. 添加当年新论文到文件夹
2. 更新papers_database.json添加新条目
3. 阅读分析后补充详细信息

### 每学期：
1. 回顾已有论文，补充遗漏信息
2. 更新knowledge_base.json的方法库
3. 整理新的LaTeX模板

### 每年：
1. 统计最常用的方法
2. 总结问题类型趋势
3. 更新README和使用指南

## 9. 协作更新

如果多人共同维护：
1. 更新前先备份JSON文件
2. 明确分工（按年份或题号）
3. 统一更新格式和标准
4. 定期合并和审核

## 10. 常见问题

**Q: 论文使用了很多方法，都要记录吗？**  
A: 记录3-5个主要方法即可，按重要性排序。

**Q: 问题类型模糊怎么办？**  
A: 可以用"+"连接，如"预测+优化"。

**Q: structure_notes写多详细？**  
A: 1-2句话概括亮点即可，不超过100字。

**Q: 如何确保JSON格式正确？**  
A: 使用在线JSON验证器，或用Python的json.load测试。

---

**提示**: 每次更新完记得备份JSON文件！
