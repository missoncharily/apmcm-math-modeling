# APMCM数学建模竞赛执行流程总结

## 📊 竞赛概况

### 基本信息
- **竞赛名称**: APMCM亚太地区大学生数学建模竞赛
- **历年数据**: 2022-2025年共16篇优秀论文
- **题目类型**: A/B/C/D/E题，每年3-5道题
- **竞赛时长**: 通常3-4天（72-96小时）

### 历年题目分布
```
2022年: 5题 (A/B/C/D/E)
2023年: 3题 (A/B/C)
2024年: 4题 (A/B/C/D)
2025年: 4题 (A/B/C/D)
```

---

## 🎯 完整执行流程

### 第0阶段：赛前准备（提前1-2周）

#### 环境配置
```bash
# Python环境
- Python 3.8+
- 必备库: numpy, pandas, matplotlib, scipy, sklearn
- 优化库: pulp, cvxpy, pyomo
- 深度学习: tensorflow/pytorch (可选)

# LaTeX环境
- TeX Live / MiKTeX
- 编辑器: Overleaf / TeXstudio
```

#### 知识储备
- [ ] 复习6大问题类型和常用方法
- [ ] 熟悉Python常用建模库
- [ ] 准备LaTeX论文模板
- [ ] 阅读历年优秀论文（至少3篇）
- [ ] 准备代码模板库

#### 团队分工
- **建模手**: 数学推导、模型设计
- **编程手**: 算法实现、数据处理
- **写作手**: 论文撰写、排版

---

### 第1阶段：理解题目（0-3小时）

#### 1.1 快速浏览（30分钟）
- [ ] 阅读全部题目（A/B/C/D）
- [ ] 标记关键信息：目标、约束、数据
- [ ] 初步判断题目难度和类型

#### 1.2 深度分析（2小时）
选定题目后：

**问题重述**（用自己的话）
- 背景是什么？
- 要解决什么问题？
- 给定了什么数据？
- 需要回答哪些具体问题？

**问题分类**
```python
# 使用知识库自动分类
from paper_db_tool import classify_problem, load_knowledge_base

kb = load_knowledge_base()
problem_desc = "你的问题描述"
types = classify_problem(problem_desc, kb)
print(f"可能类型: {types}")
```

**识别难点**
- 数据量大小和质量
- 约束条件复杂度
- 计算难度
- 多目标权衡

**选题决策矩阵**
| 题目 | 熟悉度 | 数据完整性 | 建模难度 | 计算量 | 创新空间 | 总分 |
|------|--------|-----------|---------|--------|---------|------|
| A题  | 8/10   | 7/10      | 6/10    | 5/10   | 7/10    | 33/50 |
| B题  | 6/10   | 9/10      | 8/10    | 7/10   | 8/10    | 38/50 |

---

### 第2阶段：文献调研与方法选择（3-6小时）

#### 2.1 查阅历年论文（2小时）
```python
# 使用论文数据库
from paper_db_tool import PaperDatabase

db = PaperDatabase()

# 查找相似问题
similar_papers = db.search("优化")  # 根据关键词搜索
for paper in similar_papers:
    print(f"{paper['id']}: {paper['methods']}")
```

**重点关注**
- 相似问题的建模思路
- 使用的方法和工具
- 论文结构和亮点
- 可能的创新点

#### 2.2 确定建模方案（2-3小时）

**方法选择决策树**
```
问题类型判断
│
├─ 优化问题
│  ├─ 线性约束 → 线性规划(LP)
│  ├─ 非线性 → 非线性规划(NLP)
│  ├─ 整数变量 → 整数规划(IP/MIP)
│  └─ NP难问题 → 启发式算法(GA/SA/PSO)
│
├─ 预测问题
│  ├─ 时间序列 → ARIMA/Prophet/LSTM
│  ├─ 多因素 → 回归分析/机器学习
│  └─ 小样本 → 灰色预测GM(1,1)
│
├─ 评价问题
│  ├─ 主观权重 → 层次分析法(AHP)
│  ├─ 客观权重 → 熵权法/PCA
│  └─ 综合排序 → TOPSIS/模糊评价
│
├─ 分类问题
│  ├─ 无监督 → K-means/层次聚类
│  └─ 有监督 → SVM/随机森林/神经网络
│
├─ 微分方程
│  ├─ 传播模型 → SIR/SEIR
│  └─ 动态演化 → ODE/PDE求解
│
└─ 图论网络
   ├─ 路径问题 → Dijkstra/Floyd
   └─ 流量问题 → 最大流/最小费用流
```

**建模方案文档**
```markdown
## 建模方案

### 问题1：XXX
- **方法**: ARIMA时间序列 + 灰色预测
- **理由**: 历史数据充足，趋势明显
- **工具**: statsmodels, numpy
- **预期难点**: 数据预处理、参数选择

### 问题2：XXX
- **方法**: 多目标遗传算法NSGA-II
- **理由**: 多目标冲突，无解析解
- **工具**: DEAP, matplotlib
- **预期难点**: 目标函数设计、参数调优
```

#### 2.3 数据探索（1小时）
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
data = pd.read_csv('data.csv')

# 基本信息
print(data.info())
print(data.describe())

# 缺失值检查
print(data.isnull().sum())

# 可视化
plt.figure(figsize=(12, 6))
data.plot()
plt.title('Data Overview')
plt.savefig('data_overview.png', dpi=300)
```

---

### 第3阶段：模型建立（6-12小时）

#### 3.1 模型假设（1小时）
**假设清单模板**
```latex
\begin{enumerate}
\item 假设数据真实可靠，无重大测量误差
\item 假设影响因素在研究期内保持相对稳定
\item 假设XXX符合XXX分布（需说明依据）
\item 假设忽略XXX的影响（说明合理性）
\end{enumerate}
```

**假设原则**
- ✅ 合理简化，不能过度
- ✅ 每个假设要说明依据
- ✅ 假设要和后续模型一致
- ❌ 避免循环论证的假设

#### 3.2 符号定义（30分钟）
```latex
\begin{table}[h]
\centering
\caption{符号说明}
\begin{tabular}{cl}
\hline
符号 & 含义 \\
\hline
$x_i$ & 决策变量$i$，表示XXX $(i=1,2,\ldots,n)$ \\
$y_t$ & 时刻$t$的XXX值 \\
$\alpha$ & XXX系数，范围$[0,1]$ \\
$\lambda$ & 拉格朗日乘子 \\
\hline
\end{tabular}
\end{table}
```

#### 3.3 模型构建（4-8小时）

**优化模型示例**
```latex
\begin{align}
\min \quad & f(x) = \sum_{i=1}^{n} c_i x_i \label{eq:obj}\\
\text{s.t.} \quad & \sum_{i=1}^{n} a_{ij} x_i \leq b_j, \quad j=1,2,\ldots,m \label{eq:con1}\\
& x_i \geq 0, \quad i=1,2,\ldots,n \label{eq:con2}\\
& x_i \in \mathbb{Z}, \quad i \in I \label{eq:con3}
\end{align}
```

**模型框图**
```
输入数据 → 数据预处理 → 特征提取 
    ↓
模型训练 ← 参数优化 ← 交叉验证
    ↓
模型评估 → 结果输出 → 可视化
```

**代码框架**
```python
class OptimizationModel:
    def __init__(self, data):
        self.data = data
        self.model = None
        self.results = None
    
    def preprocess(self):
        """数据预处理"""
        pass
    
    def build_model(self):
        """构建优化模型"""
        from pulp import *
        
        # 定义问题
        prob = LpProblem("Problem", LpMinimize)
        
        # 定义变量
        x = LpVariable.dicts("x", range(n), lowBound=0)
        
        # 目标函数
        prob += lpSum([c[i]*x[i] for i in range(n)])
        
        # 约束条件
        for j in range(m):
            prob += lpSum([a[j][i]*x[i] for i in range(n)]) <= b[j]
        
        self.model = prob
        return prob
    
    def solve(self):
        """求解模型"""
        self.model.solve()
        self.results = {
            'status': LpStatus[self.model.status],
            'objective': value(self.model.objective),
            'variables': {v.name: v.varValue for v in self.model.variables()}
        }
        return self.results
    
    def visualize(self):
        """结果可视化"""
        pass
```

#### 3.4 算法实现（2-3小时）

**遗传算法示例**
```python
from deap import base, creator, tools, algorithms
import numpy as np

# 定义适应度和个体
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

def evaluate(individual):
    """评估函数"""
    x = np.array(individual)
    return (np.sum(x**2),)  # 示例目标函数

# 初始化工具箱
toolbox = base.Toolbox()
toolbox.register("attr_float", np.random.uniform, -10, 10)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_float, n=10)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# 运行算法
pop = toolbox.population(n=50)
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("min", np.min)

pop, logbook = algorithms.eaSimple(pop, toolbox, 
                                    cxpb=0.7, mutpb=0.2, 
                                    ngen=100, 
                                    stats=stats, halloffame=hof,
                                    verbose=True)

print(f"最优解: {hof[0]}")
print(f"最优值: {hof[0].fitness.values[0]}")
```

---

### 第4阶段：模型求解与分析（8-12小时）

#### 4.1 模型求解（4-6小时）

**求解检查清单**
- [ ] 算法收敛性检查
- [ ] 结果合理性验证
- [ ] 边界条件测试
- [ ] 多次运行一致性

**常见问题处理**
```python
# 问题1: 优化不收敛
# 解决: 调整初始值、学习率、迭代次数

# 问题2: 结果不合理
# 解决: 检查约束条件、目标函数、数据范围

# 问题3: 计算时间过长
# 解决: 简化模型、并行计算、采样近似
```

#### 4.2 结果可视化（2-3小时）

**图表规范**
```python
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体和风格
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

# 子图布局
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 图1: 时间序列
axes[0, 0].plot(time, values, 'b-', linewidth=2, label='实际值')
axes[0, 0].plot(time, predicted, 'r--', linewidth=2, label='预测值')
axes[0, 0].set_xlabel('时间', fontsize=12)
axes[0, 0].set_ylabel('数值', fontsize=12)
axes[0, 0].set_title('时间序列预测结果', fontsize=14, fontweight='bold')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# 图2: 柱状图
axes[0, 1].bar(categories, heights, color='steelblue', alpha=0.7)
axes[0, 1].set_xlabel('类别', fontsize=12)
axes[0, 1].set_ylabel('数值', fontsize=12)
axes[0, 1].set_title('不同方案对比', fontsize=14, fontweight='bold')

# 图3: 散点图
axes[1, 0].scatter(x, y, c=colors, s=50, alpha=0.6)
axes[1, 0].set_xlabel('X轴', fontsize=12)
axes[1, 0].set_ylabel('Y轴', fontsize=12)
axes[1, 0].set_title('相关性分析', fontsize=14, fontweight='bold')

# 图4: 热力图
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', 
            cmap='RdYlGn', center=0, ax=axes[1, 1])
axes[1, 1].set_title('相关系数矩阵', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('results.png', dpi=300, bbox_inches='tight')
plt.show()
```

**图表类型选择**
- 时间序列 → 折线图
- 类别对比 → 柱状图/雷达图
- 相关关系 → 散点图/热力图
- 分布情况 → 直方图/箱线图
- 地理数据 → 地图可视化
- 网络关系 → 网络图

#### 4.3 敏感性分析（2-3小时）

**单因素敏感性**
```python
def sensitivity_analysis(base_params, param_name, variation_range):
    """
    单因素敏感性分析
    
    Args:
        base_params: 基准参数字典
        param_name: 要分析的参数名
        variation_range: 变化范围 (如 [-20%, +20%])
    """
    results = []
    base_value = base_params[param_name]
    
    for ratio in np.linspace(variation_range[0], variation_range[1], 11):
        params = base_params.copy()
        params[param_name] = base_value * (1 + ratio)
        
        # 重新运行模型
        result = run_model(params)
        results.append({
            'variation': ratio * 100,
            'param_value': params[param_name],
            'objective': result['objective']
        })
    
    # 可视化
    df = pd.DataFrame(results)
    plt.figure(figsize=(10, 6))
    plt.plot(df['variation'], df['objective'], 'o-', linewidth=2)
    plt.xlabel(f'{param_name}变化百分比 (%)', fontsize=12)
    plt.ylabel('目标函数值', fontsize=12)
    plt.title(f'{param_name}敏感性分析', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.axvline(x=0, color='r', linestyle='--', alpha=0.5)
    plt.savefig(f'sensitivity_{param_name}.png', dpi=300)
    
    return df
```

**多因素敏感性**
```python
# 正交实验设计
from itertools import product

factors = {
    'alpha': [0.8, 1.0, 1.2],
    'beta': [0.9, 1.0, 1.1],
    'gamma': [0.95, 1.0, 1.05]
}

results = []
for values in product(*factors.values()):
    params = dict(zip(factors.keys(), values))
    result = run_model(params)
    results.append({**params, 'objective': result['objective']})

df = pd.DataFrame(results)
print(df.sort_values('objective').head(10))
```

#### 4.4 模型检验（1-2小时）

**合理性检验**
- [ ] 结果是否符合实际意义
- [ ] 极端情况下的表现
- [ ] 与已知结果对比
- [ ] 专家经验验证

**稳定性检验**
```python
# 多次运行检验
results = []
for i in range(30):
    result = run_model(random_seed=i)
    results.append(result['objective'])

mean = np.mean(results)
std = np.std(results)
cv = std / mean  # 变异系数

print(f"平均值: {mean:.4f}")
print(f"标准差: {std:.4f}")
print(f"变异系数: {cv:.4f}")

# CV < 0.1 表示稳定性好
```

**预测精度检验**
```python
from sklearn.metrics import mean_squared_error, r2_score

# 回测验证
train_size = int(len(data) * 0.8)
train_data = data[:train_size]
test_data = data[train_size:]

model.fit(train_data)
predictions = model.predict(test_data)

mse = mean_squared_error(test_data, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(test_data, predictions)
mape = np.mean(np.abs((test_data - predictions) / test_data)) * 100

print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")
print(f"MAPE: {mape:.2f}%")
```

---

### 第5阶段：论文撰写（10-16小时）

#### 5.1 论文结构（参照mathmodel.md）

**标准结构**
```
1. 摘要 (300-500字) - 2小时
2. 问题重述 - 1小时
3. 问题分析 - 2小时
4. 模型假设 - 1小时
5. 符号说明 - 0.5小时
6. 模型建立 - 3小时
7. 模型求解 - 2小时
8. 结果分析 - 2小时
9. 模型检验 - 1小时
10. 模型评价 - 1小时
11. 参考文献 - 0.5小时
12. 附录(代码) - 准备好即可
```

#### 5.2 摘要撰写

**四段式结构**
```latex
\begin{abstract}

\textbf{【问题重述】} 本文针对XXX问题，需要解决以下三个方面：
(1) XXX；(2) XXX；(3) XXX。

\textbf{【模型方法】} 针对问题一，建立了XXX模型，采用XXX方法求解。
针对问题二，基于XXX理论，构建了XXX模型。针对问题三，运用XXX算法，
得到最优方案。

\textbf{【求解过程】} 首先对数据进行XXX处理，然后XXX，
最后通过XXX得到结果。模型求解使用了Python/MATLAB实现。

\textbf{【主要结论】} 问题一的结果为XXX；问题二得到XXX；
问题三的最优方案是XXX。敏感性分析表明模型稳定性良好。

\textbf{关键词：}XXX；XXX；XXX；XXX

\end{abstract}
```

#### 5.3 LaTeX技巧

**常用宏定义**
```latex
% 导言区
\usepackage{amsmath, amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{algorithm, algorithmic}
\usepackage{listings}

% 自定义命令
\newcommand{\R}{\mathbb{R}}
\newcommand{\argmin}{\mathop{\mathrm{argmin}}}
\newcommand{\E}{\mathbb{E}}

% 代码高亮
\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    commentstyle=\color{gray},
    stringstyle=\color{red},
    numbers=left,
    numberstyle=\tiny\color{gray},
    frame=single,
    breaklines=true
}
```

**插入代码**
```latex
\begin{lstlisting}[caption=优化模型求解代码, label=code:optimize]
from pulp import *

prob = LpProblem("Optimization", LpMinimize)
x = LpVariable.dicts("x", range(n), lowBound=0)
prob += lpSum([c[i]*x[i] for i in range(n)])
prob.solve()
\end{lstlisting}
```

#### 5.4 图表制作规范

**三线表**
```latex
\begin{table}[h]
\centering
\caption{不同方案对比结果}
\label{tab:comparison}
\begin{tabular}{cccc}
\toprule
方案 & 成本(元) & 效益(元) & 综合得分 \\
\midrule
方案1 & 10000 & 15000 & 0.85 \\
方案2 & 12000 & 18000 & 0.92 \\
方案3 & 11000 & 16500 & 0.88 \\
\bottomrule
\end{tabular}
\end{table}
```

**插入图片**
```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.8\textwidth]{results.png}
\caption{时间序列预测结果}
\label{fig:prediction}
\end{figure}

如图\ref{fig:prediction}所示，预测结果与实际值吻合良好。
```

#### 5.5 写作注意事项

**✅ 应该做的**
- 逻辑清晰，前后呼应
- 公式编号并在文中引用
- 图表标题完整，坐标轴有单位
- 关键结论用加粗突出
- 代码规范，有注释
- 数字保留合理精度

**❌ 不应该做的**
- 口语化表达
- 大段代码放正文
- 图表质量差
- 公式推导跳步骤
- 结论无依据
- 格式混乱

---

### 第6阶段：检查与提交（2-4小时）

#### 6.1 论文检查清单

**内容完整性**
- [ ] 摘要包含问题、方法、结论、关键词
- [ ] 问题分析深入，非简单重述
- [ ] 模型假设合理有依据
- [ ] 符号说明表完整
- [ ] 模型推导逻辑清晰
- [ ] 求解步骤详细
- [ ] 结果分析充分
- [ ] 有敏感性分析
- [ ] 有模型检验
- [ ] 有模型评价
- [ ] 参考文献格式规范
- [ ] 附录代码完整

**格式规范性**
- [ ] 字体大小统一
- [ ] 公式居中编号
- [ ] 图表编号连续
- [ ] 页眉页脚正确
- [ ] 行距段距合适
- [ ] 无明显排版错误

**逻辑连贯性**
- [ ] 假设和模型一致
- [ ] 符号前后统一
- [ ] 图表与正文对应
- [ ] 结论有数据支撑
- [ ] 全文逻辑通顺

#### 6.2 常见错误检查

```python
# 自动检查脚本
def check_paper(tex_file):
    """检查LaTeX论文常见问题"""
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # 检查1: 未引用的图表
    figures = re.findall(r'\\label\{fig:(\w+)\}', content)
    for fig in figures:
        if f'\\ref{{fig:{fig}}}' not in content:
            issues.append(f"图 fig:{fig} 未在正文引用")
    
    # 检查2: 未引用的公式
    equations = re.findall(r'\\label\{eq:(\w+)\}', content)
    for eq in equations:
        if f'\\ref{{eq:{eq}}}' not in content:
            issues.append(f"公式 eq:{eq} 未在正文引用")
    
    # 检查3: 中文标点
    if re.search(r'[,;:\.][\u4e00-\u9fa5]', content):
        issues.append("可能存在中英文标点混用")
    
    return issues
```

#### 6.3 导出PDF

```bash
# LaTeX编译
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex

# 检查PDF
pdfinfo main.pdf
```

#### 6.4 提交前最后检查

**5分钟快速检查**
1. PDF能否正常打开
2. 页数是否符合要求
3. 文件大小是否合理
4. 队伍信息是否正确
5. 是否有遗漏的TODO标记

---

## 🎓 往届题目类型分析

### 2022年题目特征
```
A题: 优化问题 (附带数据文件Attachment 2.xlsx)
B题: 数据分析
C题: 温度数据分析 (CSV数据)
D题: 预测/时间序列
E题: 数据分析 (XLSX数据)
```

### 2023年题目特征
```
A题: 优化/决策
B题: 数据分析
C题: 综合建模
```

### 2024年题目特征
```
A题: 优化问题 (Answer.xls数据)
B题: 复杂建模
C题: 数据分析
D题: 综合问题 (多个附件Attachment 1-5.pdf)
```

### 2025年题目特征
```
A题: 综合建模
B题: 数据分析
C题: 关税数据分析 (大规模数据集tariff_data_2015-2025.zip)
D题: 优化问题 (Table.xlsx)
```

### 题目特点总结
- **数据密集型**: C题常涉及大规模数据处理
- **优化导向**: A/D题多为优化或决策问题
- **综合性强**: 后期题目越来越注重多方法结合
- **数据格式**: Excel/CSV/PDF附件，需要数据处理能力

---

## 📚 方法论知识图谱

### 问题类型 → 方法映射

#### 1. 优化问题
**线性规划 (LP)**
```python
from scipy.optimize import linprog

c = [1, 2]  # 目标函数系数
A_ub = [[1, 1], [2, 1]]  # 不等式约束系数
b_ub = [4, 5]  # 不等式约束右端
res = linprog(c, A_ub=A_ub, b_ub=b_ub, method='highs')
```

**非线性规划 (NLP)**
```python
from scipy.optimize import minimize

def objective(x):
    return x[0]**2 + x[1]**2

def constraint1(x):
    return x[0] + x[1] - 1

con1 = {'type': 'eq', 'fun': constraint1}
res = minimize(objective, [0, 0], constraints=[con1])
```

**整数规划 (IP)**
```python
from pulp import *

prob = LpProblem("IP", LpMinimize)
x = LpVariable("x", lowBound=0, cat='Integer')
y = LpVariable("y", lowBound=0, cat='Integer')
prob += 2*x + 3*y  # 目标
prob += x + y >= 5  # 约束
prob.solve()
```

#### 2. 预测问题
**ARIMA时间序列**
```python
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(data, order=(2, 1, 2))
fitted = model.fit()
forecast = fitted.forecast(steps=10)
```

**随机森林回归**
```python
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
predictions = rf.predict(X_test)
```

#### 3. 评价问题
**层次分析法 (AHP)**
```python
import numpy as np

def ahp_weight(matrix):
    """计算AHP权重"""
    n = len(matrix)
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    max_idx = np.argmax(eigenvalues)
    max_eigen = eigenvalues[max_idx].real
    max_vector = eigenvectors[:, max_idx].real
    
    # 归一化
    weights = max_vector / np.sum(max_vector)
    
    # 一致性检验
    CI = (max_eigen - n) / (n - 1)
    RI = {1:0, 2:0, 3:0.58, 4:0.90, 5:1.12, 6:1.24, 7:1.32, 8:1.41, 9:1.45}
    CR = CI / RI[n] if n in RI else None
    
    return weights, CR

# 判断矩阵示例
matrix = np.array([
    [1, 2, 5],
    [1/2, 1, 3],
    [1/5, 1/3, 1]
])

weights, CR = ahp_weight(matrix)
print(f"权重: {weights}")
print(f"一致性比率CR: {CR:.4f}")
if CR < 0.1:
    print("通过一致性检验")
```

**TOPSIS法**
```python
def topsis(data, weights, benefit_cols):
    """TOPSIS综合评价"""
    # 标准化
    normalized = data / np.sqrt((data**2).sum(axis=0))
    
    # 加权
    weighted = normalized * weights
    
    # 理想解
    positive_ideal = np.zeros(data.shape[1])
    negative_ideal = np.zeros(data.shape[1])
    
    for i in range(data.shape[1]):
        if i in benefit_cols:
            positive_ideal[i] = weighted[:, i].max()
            negative_ideal[i] = weighted[:, i].min()
        else:
            positive_ideal[i] = weighted[:, i].min()
            negative_ideal[i] = weighted[:, i].max()
    
    # 距离
    d_pos = np.sqrt(((weighted - positive_ideal)**2).sum(axis=1))
    d_neg = np.sqrt(((weighted - negative_ideal)**2).sum(axis=1))
    
    # 综合得分
    scores = d_neg / (d_pos + d_neg)
    
    return scores
```

---

## 💡 实战技巧与经验

### 时间管理策略

**黄金分配法则**
- 30%: 理解题目+文献调研 (10小时)
- 40%: 建模+求解+分析 (24小时)
- 30%: 论文撰写+检查 (12小时)

**关键时间节点**
```
0h: 比赛开始，快速浏览题目
3h: 完成选题和初步方案
6h: 确定建模方法，开始编程
12h: 第一版模型完成
24h: 主要结果产出
36h: 开始论文初稿
48h: 论文主体完成
60h: 完善图表和分析
66h: 最后检查和润色
72h: 提交截止
```

### 团队协作模式

**并行工作流**
```
建模手: 数学推导 → 模型验证 → 理论分析
    ↓
编程手: 代码实现 → 算法调优 → 结果产出
    ↓
写作手: 论文框架 → 逐步填充 → 格式排版
```

**协作工具**
- 代码: GitHub / Gitee
- 文档: Overleaf (LaTeX在线协作)
- 沟通: 微信/腾讯会议
- 文件: 百度网盘/坚果云同步

### 常见陷阱与应对

**陷阱1: 选题失误**
- 症状: 做了很久发现无从下手
- 预防: 前3小时充分讨论，不轻易改题
- 应对: 如必须换题，在12小时内决定

**陷阱2: 过度优化**
- 症状: 在局部细节上花费过多时间
- 预防: 先求完整，再求完美
- 应对: 设定时间限制，到点就进入下一阶段

**陷阱3: 论文时间不足**
- 症状: 最后12小时才开始写论文
- 预防: 边做边写，至少36小时开始
- 应对: 使用模板快速填充，保证完整性

**陷阱4: 数据问题**
- 症状: 数据缺失/异常导致无法建模
- 预防: 前6小时完成数据探索
- 应对: 合理假设填补、异常值处理

**陷阱5: 代码调试地狱**
- 症状: 算法一直不收敛或报错
- 预防: 使用成熟库、先跑通简单案例
- 应对: 简化模型、采用启发式方法

### 提分技巧

**创新点设计**
- 方法创新: 结合多种方法
- 模型改进: 在经典模型上改进
- 分析深度: 多角度多层次分析
- 可视化: 清晰美观的图表

**论文亮点打造**
```
1. 摘要: 开门见山，突出创新
2. 问题分析: 深入挖掘，建立框架
3. 模型框图: 清晰的流程和逻辑
4. 公式推导: 规范完整，有理论依据
5. 结果展示: 多维度可视化
6. 敏感性分析: 充分细致
7. 模型检验: 多种方法验证
8. 代码规范: 注释清晰，可重现
```

**高分论文特征**
- ✅ 逻辑严密，层次清晰
- ✅ 方法得当，计算正确
- ✅ 分析深入，结论可靠
- ✅ 图表精美，一目了然
- ✅ 有创新点或改进
- ✅ 格式规范，无明显错误

---

## 🛠️ 工具箱速查

### Python必备库
```python
# 数值计算
import numpy as np
import scipy
from scipy import optimize, integrate, stats

# 数据处理
import pandas as pd

# 可视化
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 机器学习
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 时间序列
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
import prophet

# 优化
from pulp import *
import cvxpy as cp
from scipy.optimize import linprog, minimize

# 网络
import networkx as nx

# 深度学习 (可选)
import tensorflow as tf
import torch
```

### 快速启动代码模板

**数据加载模板**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 配置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 加载数据
data = pd.read_csv('data.csv', encoding='utf-8')
# data = pd.read_excel('data.xlsx')

# 基本信息
print("数据形状:", data.shape)
print("\n前5行:")
print(data.head())
print("\n数据类型:")
print(data.dtypes)
print("\n统计描述:")
print(data.describe())
print("\n缺失值:")
print(data.isnull().sum())
```

**可视化模板**
```python
def plot_analysis(data, save_path='analysis.png'):
    """综合分析可视化"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. 时间序列
    axes[0, 0].plot(data.index, data['value'], 'b-', linewidth=2)
    axes[0, 0].set_title('时间序列趋势', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('时间')
    axes[0, 0].set_ylabel('数值')
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. 分布直方图
    axes[0, 1].hist(data['value'], bins=30, color='steelblue', 
                    alpha=0.7, edgecolor='black')
    axes[0, 1].set_title('数据分布', fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('数值')
    axes[0, 1].set_ylabel('频数')
    
    # 3. 箱线图
    axes[1, 0].boxplot(data['value'])
    axes[1, 0].set_title('箱线图', fontsize=14, fontweight='bold')
    axes[1, 0].set_ylabel('数值')
    
    # 4. 相关性
    if data.shape[1] > 1:
        corr = data.corr()
        im = axes[1, 1].imshow(corr, cmap='RdYlGn', aspect='auto')
        axes[1, 1].set_title('相关系数矩阵', fontsize=14, fontweight='bold')
        plt.colorbar(im, ax=axes[1, 1])
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
```

### LaTeX模板库

**完整论文模板结构**
```latex
\documentclass[12pt,a4paper]{article}

% 包导入
\usepackage[UTF8]{ctex}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{geometry}
\usepackage{hyperref}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{algorithm}
\usepackage{algorithmic}

% 页面设置
\geometry{left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm}

% 代码样式
\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    commentstyle=\color{gray},
    stringstyle=\color{red},
    numbers=left,
    numberstyle=\tiny\color{gray},
    frame=single,
    breaklines=true
}

\title{\textbf{XXX问题的数学建模与分析}}
\author{队伍编号：XXX}
\date{}

\begin{document}

\maketitle

\begin{abstract}
此处为摘要内容...

\textbf{关键词：}优化模型；ARIMA；敏感性分析；Python
\end{abstract}

\newpage
\tableofcontents
\newpage

\section{问题重述}
...

\section{问题分析}
...

\section{模型假设}
\begin{enumerate}
\item 假设1
\item 假设2
\end{enumerate}

\section{符号说明}
\begin{table}[h]
\centering
\caption{符号说明}
\begin{tabular}{cl}
\toprule
符号 & 含义 \\
\midrule
$x_i$ & XXX \\
\bottomrule
\end{tabular}
\end{table}

\section{模型建立}
...

\section{模型求解}
...

\section{结果分析}
...

\section{模型检验}
...

\section{模型评价}
\subsection{模型优点}
\subsection{模型缺点}
\subsection{模型改进}

\begin{thebibliography}{99}
\bibitem{ref1} 作者. 标题[J]. 期刊, 年份, 卷(期): 页码.
\end{thebibliography}

\newpage
\appendix
\section{代码}
\begin{lstlisting}
# Python代码
import numpy as np
\end{lstlisting}

\end{document}
```

---

## 📖 参考资源

### 在线资源
- **优秀论文**: `D:\竞赛资料\数学建模\参考资料\论文`
- **往届题目**: `D:\竞赛资料\数学建模\参考资料\往届题目`
- **本地知识库**: `D:\竞赛资料\数学建模\参考资料\claude`

### 推荐学习资源
- 《数学建模算法与应用》司守奎
- 《MATLAB数学建模方法与实践》王正林
- Python数据分析与建模实战
- 优秀论文精选集

### Claude Code工具
```bash
# 使用mathmodel skill
/mathmodel

# 查询论文数据库
cd D:\竞赛资料\数学建模\参考资料\claude
python paper_db_tool.py
```

---

## ✅ 竞赛检查清单

### 赛前准备
- [ ] Python/MATLAB环境配置
- [ ] LaTeX环境安装
- [ ] 常用库安装测试
- [ ] 代码模板准备
- [ ] 论文模板准备
- [ ] 历年论文阅读（至少3篇）
- [ ] 团队分工明确

### 比赛进行中
- [ ] 0-3h: 选题完成
- [ ] 3-6h: 建模方案确定
- [ ] 6-12h: 第一版模型
- [ ] 12-24h: 主要结果产出
- [ ] 24-36h: 论文初稿
- [ ] 36-48h: 论文主体完成
- [ ] 48-60h: 完善分析和图表
- [ ] 60-66h: 最后检查
- [ ] 66-72h: 提交前检查

### 提交前检查
- [ ] 论文结构完整
- [ ] 所有图表清晰
- [ ] 公式编号正确
- [ ] 参考文献格式规范
- [ ] 代码完整可运行
- [ ] PDF能正常打开
- [ ] 队伍信息正确
- [ ] 文件大小合理

---

## 🎯 成功要素总结

### 三大核心
1. **扎实的数学基础**: 理解模型本质
2. **熟练的编程能力**: 快速实现验证
3. **清晰的表达能力**: 论文逻辑严密

### 五个关键
1. **选题准确**: 选择适合自己的题目
2. **方法得当**: 选择合适的建模方法
3. **求解正确**: 算法实现无误
4. **分析深入**: 多角度多层次
5. **论文规范**: 格式清晰完整

### 七项注意
1. 时间管理：严格按计划执行
2. 团队协作：明确分工，高效沟通
3. 边做边写：不要堆积到最后
4. 结果验证：多次检查合理性
5. 图表质量：清晰美观专业
6. 代码规范：注释完整可重现
7. 细节完善：格式、标点、公式

---

## 📞 紧急情况处理

### 模型跑不出结果
1. 简化模型，先跑通基础版本
2. 检查数据预处理
3. 调整算法参数
4. 考虑使用启发式方法
5. 如果实在不行，用手工计算小规模案例

### 时间严重不足
1. 优先保证论文完整性
2. 使用模板快速填充
3. 图表可以简化但要清晰
4. 代码放附录简化说明
5. 关键是逻辑清晰

### 团队意见分歧
1. 限时讨论，投票决定
2. 相信建模手的判断
3. 不要反复推翻重来
4. 记录所有方案备用

### 设备故障
1. 实时云端备份（Overleaf/GitHub）
2. 准备备用电脑
3. 保存多个版本
4. 定时导出PDF

---

## 🌟 最后的话

数学建模竞赛不仅是技术的比拼，更是：
- **思维能力**的体现
- **团队协作**的考验  
- **抗压能力**的锻炼
- **学习能力**的展示

记住：
> "完成比完美更重要"  
> "逻辑清晰比方法高深更重要"  
> "团队协作比个人英雄更重要"

祝各位参赛者取得好成绩！🏆

---

**文档版本**: v1.0  
**创建日期**: 2026-10-13  
**适用竞赛**: APMCM亚太地区大学生数学建模竞赛  
**维护者**: Claude Code AI Assistant
