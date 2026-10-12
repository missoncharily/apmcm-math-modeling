---
name: mathmodel
description: APMCM数学建模竞赛论文写作和分析助手
---

# 数学建模竞赛助手

这个skill帮助你进行数学建模竞赛的论文写作、问题分析和方法选择。

## 功能

### 1. 论文结构指导
标准数学建模论文包含以下部分：

- **摘要** (300-500字)
  - 问题重述
  - 模型概述
  - 求解方法
  - 主要结论
  - 关键词(3-5个)

- **问题重述**
  - 用自己的话重新描述问题
  - 明确目标和约束条件

- **问题分析**
  - 问题分类(优化/预测/评价/决策)
  - 影响因素分析
  - 难点和关键点识别

- **模型假设**
  - 列出合理假设
  - 说明假设依据

- **符号说明**
  - 变量和参数定义表

- **模型建立**
  - 模型选择和理论基础
  - 数学公式推导
  - 模型框架图

- **模型求解**
  - 算法选择
  - 求解步骤
  - 代码实现(附录)

- **结果分析**
  - 数据可视化
  - 结果解释
  - 敏感性分析

- **模型检验**
  - 合理性检验
  - 稳定性检验

- **模型评价与推广**
  - 优缺点分析
  - 改进方向
  - 应用场景

- **参考文献**

### 2. 常见问题类型和方法

#### 优化问题
- 线性规划 (LP)
- 非线性规划 (NLP)
- 整数规划 (IP)
- 多目标优化
- 遗传算法、模拟退火等启发式算法

#### 预测问题
- 时间序列 (ARIMA, Prophet)
- 回归分析 (线性/非线性/逻辑回归)
- 机器学习 (随机森林, XGBoost, 神经网络)
- 灰色预测模型 (GM)

#### 评价问题
- 层次分析法 (AHP)
- 模糊综合评价
- 熵权法
- TOPSIS法
- 主成分分析 (PCA)
- 数据包络分析 (DEA)

#### 分类问题
- 聚类分析 (K-means, 层次聚类)
- 判别分析
- 支持向量机 (SVM)
- 决策树

#### 微分方程模型
- 常微分方程 (ODE)
- 偏微分方程 (PDE)
- 传染病模型 (SIR, SEIR)
- 捕食者-猎物模型

#### 网络与图论
- 最短路径
- 网络流
- 图着色
- 社交网络分析

### 3. 使用历年优秀论文

数据库位置: `D:\竞赛资料\数学建模\参考资料\claude\papers_database.json`

查看特定年份或题目的论文：
```python
import json

with open('papers_database.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# 示例：查找2025年A题
paper = next(p for p in db['papers'] if p['id'] == '2025-A')
print(f"文件路径: {paper['file_path']}")
```

### 4. 论文写作流程

1. **理解题目** (2-3小时)
   - 仔细阅读题目
   - 明确问题类型
   - 识别关键信息和数据

2. **文献调研** (2-3小时)
   - 查找相关论文和方法
   - 参考历年优秀论文
   - 确定建模思路

3. **建立模型** (8-12小时)
   - 提出假设
   - 选择合适方法
   - 建立数学模型
   - 编写求解代码

4. **求解和分析** (6-8小时)
   - 运行模型求解
   - 结果可视化
   - 敏感性分析
   - 模型检验

5. **论文撰写** (8-12小时)
   - 按标准结构写作
   - 插图和表格制作
   - 格式排版
   - 多次检查修改

6. **最终检查** (2-3小时)
   - 逻辑连贯性
   - 公式和符号一致性
   - 图表清晰度
   - 语言规范性

### 5. 常用Python库

```python
# 数值计算
import numpy as np
import scipy
from scipy.optimize import linprog, minimize

# 数据处理
import pandas as pd

# 可视化
import matplotlib.pyplot as plt
import seaborn as sns

# 机器学习
from sklearn.ensemble import RandomForestRegressor
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# 时间序列
from statsmodels.tsa.arima.model import ARIMA

# 优化
from pulp import *  # 线性规划
import cvxpy as cp  # 凸优化
```

### 6. LaTeX公式模板

**优化模型**:
```latex
\begin{align}
\min \quad & f(x) \\
\text{s.t.} \quad & g_i(x) \leq 0, \quad i=1,2,\ldots,m \\
& h_j(x) = 0, \quad j=1,2,\ldots,p \\
& x \in \mathbb{R}^n
\end{align}
```

**时间序列**:
```latex
ARIMA(p,d,q): \quad \phi(B)(1-B)^d y_t = \theta(B)\varepsilon_t
```

**层次分析法**:
```latex
\text{一致性指标:} \quad CI = \frac{\lambda_{\max} - n}{n-1}
```

## 使用方法

当你需要：
- 分析数学建模问题类型
- 选择合适的建模方法
- 撰写论文某个部分
- 参考历年优秀论文

直接告诉我你的需求，我会基于这个知识库和标准结构来帮助你。

## 示例问题

- "这个问题属于什么类型？应该用什么方法？"
- "帮我写问题分析部分"
- "如何建立优化模型？"
- "2024年B题用了什么方法？"
- "帮我检查论文结构是否完整"
