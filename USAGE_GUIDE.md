# APMCM数学建模资料库使用指南

## 📁 文件结构

```
D:\竞赛资料\数学建模\参考资料\claude\
├── README.md                    # 本文件
├── papers_database.json         # 论文数据库 (16篇优秀论文)
├── knowledge_base.json          # 方法论知识库
├── mathmodel.md                 # Claude Code Skill定义
├── paper_db_tool.py             # Python查询工具
├── latex_templates.py           # LaTeX模板库
└── update_guide.md              # 数据库更新指南
```

## 🚀 快速开始

### 1. 在Claude Code中使用

如果 `mathmodel.md` 已注册为skill，直接调用：
```
/mathmodel
```

或在对话中提及：
```
"帮我分析这个优化问题，应该用什么方法？"
"参考2025年A题的论文结构"
```

### 2. Python工具使用

```python
from paper_db_tool import PaperDatabase, load_knowledge_base

# 查询论文
db = PaperDatabase("papers_database.json")
papers_2025 = db.get_by_year(2025)

# 问题分类
kb = load_knowledge_base("knowledge_base.json")
from paper_db_tool import classify_problem, suggest_methods

types = classify_problem("预测销售额并优化库存", kb)
methods = suggest_methods(types[0], kb)
```

### 3. LaTeX模板使用

```python
from latex_templates import *

# 直接使用模板
print(OPTIMIZATION_MODEL)  # 优化模型
print(AHP_MODEL)           # 层次分析法
print(TIME_SERIES_MODEL)   # 时间序列
```

## 📊 数据库内容

### 论文收录
- **2022年**: 5篇 (A-E题)
- **2023年**: 3篇 (A-C题)
- **2024年**: 4篇 (A-D题)
- **2025年**: 4篇 (A-D题)
- **总计**: 16篇APMCM优秀论文

### 知识库覆盖
- 6大问题类型：优化、预测、评价、分类、微分方程、图论
- 20+建模方法及适用场景
- Python工具库推荐
- 论文结构检查清单
- 常见错误警示

## 🛠️ 主要功能

### 1. 问题类型识别
根据题目描述自动识别：
- 优化问题
- 预测问题
- 评价问题
- 分类聚类
- 微分方程
- 图论网络

### 2. 方法推荐
针对每种问题类型推荐：
- 适用的建模方法
- Python实现工具
- 参考论文

### 3. 论文写作指导
- 标准结构模板
- LaTeX公式模板
- 图表制作规范
- 常见错误提醒

### 4. 历年论文查询
- 按年份查询
- 按题号查询
- 按方法查询
- 全文关键词搜索

## 📝 使用场景

### 场景1: 比赛开始，拿到题目
```
1. 描述题目给Claude
2. 系统自动识别问题类型
3. 推荐建模方法和工具
4. 查询相关历年论文
```

### 场景2: 撰写论文
```
1. 使用LaTeX模板快速搭建结构
2. 参考标准论文结构检查清单
3. 调用对应的公式模板
4. 避免常见错误
```

### 场景3: 模型求解
```
1. 获取推荐的Python库
2. 参考代码示例
3. 进行敏感性分析
4. 模型检验
```

### 场景4: 复盘学习
```
1. 查询特定年份或题型的论文
2. 分析优秀论文的方法
3. 积累方法论知识
4. 更新数据库标注
```

## 🔄 数据库维护

### 添加新论文
1. 将PDF放入对应年份文件夹
2. 在 `papers_database.json` 添加条目
3. 分析后更新字段：
   - `problem_type`: 问题类型
   - `methods`: 使用的方法列表
   - `keywords`: 关键词
   - `structure_notes`: 亮点笔记

### 更新知识库
在 `knowledge_base.json` 中：
- 添加新方法到对应问题类型
- 更新工具推荐
- 补充写作技巧

## 💡 高级功能

### 自定义查询
```python
# 查找使用特定方法的论文
db.get_by_method("遗传算法")

# 搜索关键词
db.search("时间序列")

# 统计信息
stats = db.statistics()
```

### 批量分析
```python
# 分析所有2024年论文
papers = db.get_by_year(2024)
for p in papers:
    print(f"分析 {p['id']}: {p['title']}")
    # TODO: 添加PDF内容提取和分析
```

## 📚 扩展计划

- [ ] PDF自动提取和分析
- [ ] 建立方法-论文关联图谱
- [ ] 生成论文写作检查脚本
- [ ] 集成更多竞赛（MCM/ICM、国赛）
- [ ] 添加代码模板库
- [ ] 建立评分标准知识库

## 🤝 使用建议

1. **比赛前**: 熟悉各类问题类型和方法
2. **比赛中**: 快速查询和参考，不要过度依赖
3. **比赛后**: 详细分析优秀论文，更新数据库
4. **日常**: 积累方法论，丰富知识库

## ⚠️ 注意事项

- 参考论文结构和方法，但要有自己的创新
- 数据库需要手动更新PDF分析结果
- LaTeX模板需根据实际调整
- 方法选择要结合具体问题，不要生搬硬套

## 📞 技术支持

遇到问题时：
1. 检查文件路径是否正确
2. 确认JSON格式是否有效
3. 查看Python依赖是否安装
4. 向Claude Code求助

---

**版本**: 1.0  
**最后更新**: 2026-10-12  
**维护**: Claude Code + 用户
