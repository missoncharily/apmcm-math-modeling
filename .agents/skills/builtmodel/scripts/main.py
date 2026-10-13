#!/usr/bin/env python3
"""Command-line helper for the repository's APMCM knowledge base."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Callable

for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8", errors="replace")


def find_repository_root() -> Path:
    script_path = Path(__file__).resolve()
    search_roots = (script_path.parent, Path.cwd().resolve())
    seen: set[Path] = set()
    for search_root in search_roots:
        for candidate in (search_root, *search_root.parents):
            if candidate in seen:
                continue
            seen.add(candidate)
            if (candidate / "papers_database.json").is_file() and (
                candidate / "knowledge_base.json"
            ).is_file():
                return candidate
    raise FileNotFoundError(
        "Could not find papers_database.json and knowledge_base.json from "
        f"{script_path} or the current directory. Run this skill from the APMCM repository."
    )


ROOT = find_repository_root()
sys.path.insert(0, str(ROOT))

from latex_templates import (  # noqa: E402
    ABSTRACT_TEMPLATE,
    AHP_MODEL,
    EVALUATION_TEMPLATE,
    FIGURE_TEMPLATE,
    NOTATION_TEMPLATE,
    OPTIMIZATION_MODEL,
    SENSITIVITY_TEMPLATE,
    TABLE_TEMPLATE,
    TIME_SERIES_MODEL,
)
from paper_db_tool import (  # noqa: E402
    PaperDatabase,
    classify_problem,
    load_knowledge_base,
    suggest_methods,
)


def load_data() -> tuple[PaperDatabase, dict]:
    return (
        PaperDatabase(str(ROOT / "papers_database.json")),
        load_knowledge_base(str(ROOT / "knowledge_base.json")),
    )


def overview(db: PaperDatabase, kb: dict, _args: list[str]) -> None:
    stats = db.statistics()
    print("APMCM 数学建模知识库")
    print(f"论文记录：{stats['total']} 篇；带方法标注：{stats['analyzed']} 篇")
    years = "、".join(str(year) for year in db.list_all_years())
    print(f"收录年份：{years or '无'}")
    print("\n问题类型与方法：")
    for entry in kb.get("problem_types", {}).values():
        methods = "、".join(item.get("name", "") for item in entry.get("methods", []))
        print(f"- {entry.get('name', '未命名')}: {entry.get('description', '')}")
        print(f"  方法：{methods or '暂无'}")
    if stats["unanalyzed"]:
        print(
            f"\n提示：{stats['unanalyzed']} 篇论文尚无方法标注；"
            "检索不到方法时，请查阅题目分析文档。"
        )


def analyze(db: PaperDatabase, kb: dict, args: list[str]) -> None:
    if not args:
        raise ValueError("用法：analyze <题目描述>")
    description = " ".join(args)
    types = classify_problem(description, kb)
    print(f"题目描述：{description}")
    if not types:
        print("没有匹配到明确的问题类型。请补充目标、决策变量、约束和数据特征。")
        return
    for problem_type in types:
        print(f"\n可能类型：{problem_type}")
        for method in suggest_methods(problem_type, kb):
            tools = "、".join(method.get("tools", [])) or "未指定"
            print(f"- {method.get('name', '未命名')}: {method.get('applicable', '')}")
            print(f"  工具：{tools}")
        papers = db.get_by_type(problem_type)
        if papers:
            print("  已标注的相关论文：" + "、".join(p.get("id", "") for p in papers))
    print("\n分类由关键词匹配产生，需结合题目目标、约束和数据核验。")


def method_lookup(db: PaperDatabase, kb: dict, args: list[str]) -> None:
    if not args:
        raise ValueError("用法：method <方法名或问题类型>")
    query = " ".join(args).casefold()
    matches: list[tuple[str, dict]] = []
    for entry in kb.get("problem_types", {}).values():
        for method in entry.get("methods", []):
            if query in method.get("name", "").casefold() or query in entry.get("name", "").casefold():
                matches.append((entry.get("name", "未命名"), method))
    if not matches:
        print(f"知识库中没有找到“{' '.join(args)}”。可先运行 overview 查看已有类型。")
        return
    for problem_type, item in matches:
        print(f"{item.get('name', '未命名')}（{problem_type}）")
        print(f"适用场景：{item.get('applicable', '未说明')}")
        print("工具：" + ("、".join(item.get("tools", [])) or "未指定"))
        papers = [
            paper
            for paper in db.papers
            if any(item.get("name", "").casefold() in tag.casefold() for tag in paper.get("methods", []))
        ]
        if papers:
            print("已标注论文：" + "、".join(p.get("id", "") for p in papers))
        else:
            print("已标注论文：数据库暂无匹配记录")


def paper_lookup(db: PaperDatabase, _kb: dict, args: list[str]) -> None:
    if not args:
        raise ValueError("用法：paper <题号或关键词>")
    query = " ".join(args)
    exact = db.get_by_id(query.upper())
    results = [exact] if exact else db.search(query)
    if not results:
        print(f"没有找到“{query}”对应的论文记录。")
        return
    for paper in results:
        print(f"{paper.get('id', '未知 ID')}: {paper.get('title', '未命名')}")
        print(f"问题类型：{paper.get('problem_type') or '未标注'}")
        print("方法：" + ("、".join(paper.get("methods", [])) or "未标注"))
        print("关键词：" + ("、".join(paper.get("keywords", [])) or "未标注"))
        if paper.get("structure_notes"):
            print(f"笔记：{paper['structure_notes']}")
        if paper.get("file_path"):
            print(f"文件路径：{paper['file_path']}")


WRITE_TEMPLATES = {
    "abstract": ("摘要", ABSTRACT_TEMPLATE),
    "摘要": ("摘要", ABSTRACT_TEMPLATE),
    "optimization": ("优化模型", OPTIMIZATION_MODEL),
    "优化": ("优化模型", OPTIMIZATION_MODEL),
    "ahp": ("层次分析法", AHP_MODEL),
    "层次分析法": ("层次分析法", AHP_MODEL),
    "time-series": ("时间序列", TIME_SERIES_MODEL),
    "时间序列": ("时间序列", TIME_SERIES_MODEL),
    "table": ("表格", TABLE_TEMPLATE),
    "表格": ("表格", TABLE_TEMPLATE),
    "figure": ("图片", FIGURE_TEMPLATE),
    "图片": ("图片", FIGURE_TEMPLATE),
    "notation": ("符号说明", NOTATION_TEMPLATE),
    "符号": ("符号说明", NOTATION_TEMPLATE),
    "sensitivity": ("敏感性分析", SENSITIVITY_TEMPLATE),
    "敏感性": ("敏感性分析", SENSITIVITY_TEMPLATE),
    "evaluation": ("模型评价", EVALUATION_TEMPLATE),
    "评价": ("模型评价", EVALUATION_TEMPLATE),
}


def write_section(_db: PaperDatabase, kb: dict, args: list[str]) -> None:
    if not args:
        raise ValueError("用法：write <章节>")
    query = " ".join(args)
    normalized = query.casefold()
    match = next(
        (value for key, value in WRITE_TEMPLATES.items() if key.casefold() == normalized),
        None,
    )
    print(f"章节：{match[0] if match else query}")
    print("\n写作检查要点：")
    for item in kb.get("paper_structure_checklist", []):
        if query in item or (match and match[0] in item):
            print(f"- {item}")
    if match:
        print("\nLaTeX 起始模板（请替换所有 XXX 占位内容）：")
        print(match[1].strip())
    else:
        print("未找到专用模板。按章节目标组织论证，并保持数据、公式和结论可核验。")


PROCESS_STAGES = {
    "prepare": ("赛前准备", ["检查 Python 与 LaTeX 环境", "阅读至少 3 篇优秀论文", "确认团队分工并准备共享目录"]),
    "analyze": ("读题与选题", ["逐题列出目标、约束、数据和交付物", "评估熟悉度、数据完整性、难度、算力和创新空间", "重述每个子问题并记录待确认假设"]),
    "research": ("调研与方案", ["检索相似题目和论文并记录来源", "比较候选模型的假设、数据需求和验证方式", "为每个子问题写明方法、理由、工具和风险"]),
    "solve": ("建模与求解", ["先实现最小可运行模型", "检查数据质量、约束满足和数值边界", "进行基准对比、敏感性分析和稳定性检验", "保存代码、参数、随机种子和结果"]),
    "write": ("论文写作", ["按问题组织模型、算法、结果和解释", "统一变量、单位、图表编号和引用", "确保每个结论都能追溯到数据或计算结果"]),
    "final": ("提交检查", ["运行全部代码并确认结果可复现", "检查摘要、公式、图表、参考文献和附件", "确认文件命名、格式要求和提交截止时间"]),
}
STAGE_ALIASES = {
    "0": "prepare", "赛前": "prepare", "赛前准备": "prepare", "准备": "prepare", "prepare": "prepare",
    "1": "analyze", "读题": "analyze", "选题": "analyze", "读题与选题": "analyze", "analyze": "analyze",
    "2": "research", "调研": "research", "方案": "research", "调研与方案": "research", "research": "research",
    "3": "solve", "建模": "solve", "求解": "solve", "建模与求解": "solve", "solve": "solve",
    "4": "write", "写作": "write", "论文写作": "write", "write": "write",
    "5": "final", "提交": "final", "收尾": "final", "提交检查": "final", "final": "final",
}


def process(_db: PaperDatabase, _kb: dict, args: list[str]) -> None:
    if not args:
        for key, (title, tasks) in PROCESS_STAGES.items():
            print(f"{title}（{key}）")
            for task in tasks:
                print(f"- {task}")
        return
    raw_stage = " ".join(args).casefold()
    stage_key = STAGE_ALIASES.get(raw_stage)
    if not stage_key:
        raise ValueError("阶段可用值：prepare、analyze、research、solve、write、final，或对应中文阶段名。")
    title, tasks = PROCESS_STAGES[stage_key]
    print(title)
    for task in tasks:
        print(f"- {task}")


CODE_SNIPPETS = {
    "optimization": '''import numpy as np
from scipy.optimize import linprog

# Replace coefficients and bounds with values derived from the problem.
c = np.array([1.0, 2.0])
A_ub = np.array([[1.0, 1.0]])
b_ub = np.array([10.0])
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=(0, None), method="highs")
if not result.success:
    raise RuntimeError(result.message)
print("decision variables:", result.x)
print("objective:", result.fun)
''',
    "prediction": '''import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

values = [120, 128, 133, 141, 147, 154, 162, 169]
index = pd.period_range("2020", periods=len(values), freq="Y")
series = pd.Series(values, index=index)
train, test = series.iloc[:-3], series.iloc[-3:]
model = ARIMA(train, order=(1, 1, 1)).fit()
forecast = model.forecast(steps=len(test))
print(pd.DataFrame({"actual": test, "forecast": forecast}))
''',
    "evaluation": '''import numpy as np

# Replace with a positive reciprocal pairwise-comparison matrix.
A = np.array([[1.0, 2.0, 4.0], [1 / 2, 1.0, 3.0], [1 / 4, 1 / 3, 1.0]])
values, vectors = np.linalg.eig(A)
index = int(np.argmax(values.real))
weights = np.abs(vectors[:, index].real)
weights /= weights.sum()
lambda_max = values[index].real
ci = (lambda_max - len(A)) / (len(A) - 1)
cr = ci / 0.58  # Random index for n=3
print("weights:", weights)
print("consistency ratio:", cr)
# Review the judgments if CR >= 0.1.
''',
    "classification": '''from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X = [[1.0, 2.0], [1.5, 1.8], [8.0, 8.0], [8.0, 9.0]]
X_scaled = StandardScaler().fit_transform(X)
labels = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(X_scaled)
print(labels)
''',
    "ode": '''import numpy as np
from scipy.integrate import solve_ivp

def rhs(t, state):
    x, y = state
    return [x - 0.1 * x * y, -y + 0.075 * x * y]

solution = solve_ivp(rhs, (0, 20), [10, 5], dense_output=True)
if not solution.success:
    raise RuntimeError(solution.message)
print(solution.t, solution.y)
''',
    "graph": '''import networkx as nx

graph = nx.DiGraph()
graph.add_weighted_edges_from([("A", "B", 2), ("B", "C", 3), ("A", "C", 8)])
path = nx.shortest_path(graph, "A", "C", weight="weight")
cost = nx.shortest_path_length(graph, "A", "C", weight="weight")
print(path, cost)
''',
}
CODE_ALIASES = {
    "优化": "optimization", "optimization": "optimization", "lp": "optimization",
    "预测": "prediction", "prediction": "prediction", "时间序列": "prediction",
    "评价": "evaluation", "evaluation": "evaluation", "ahp": "evaluation",
    "分类": "classification", "聚类": "classification", "classification": "classification",
    "微分方程": "ode", "ode": "ode", "图论": "graph", "网络": "graph", "graph": "graph",
}


def code_template(_db: PaperDatabase, _kb: dict, args: list[str]) -> None:
    if not args:
        raise ValueError("用法：code <optimization|prediction|evaluation|classification|ode|graph>")
    query = " ".join(args).casefold()
    key = CODE_ALIASES.get(query)
    if not key:
        raise ValueError("类型可用值：optimization、prediction、evaluation、classification、ode、graph，或对应中文名称。")
    print(f"代码起始模板：{key}（需按题目改写并验证）")
    print(CODE_SNIPPETS[key].rstrip())


CHECKS = {
    "data": ["记录来源、单位、时间范围和样本口径", "检查缺失值、重复值、异常值和字段类型", "避免训练/测试数据泄漏", "说明清洗规则及其对结果的影响"],
    "model": ["明确定义决策变量、参数、目标函数和约束", "说明方法选择依据及关键假设", "检查约束可行性、边界条件和求解状态", "设置基准比较并做敏感性或稳健性检验"],
    "final": ["摘要准确覆盖问题、方法、结果和结论", "公式、变量、单位、表格和图号前后一致", "结果解释与图表、代码输出相符", "参考文献和数据来源完整", "代码和附件可复现且文件符合提交要求"],
}


def checklist(_db: PaperDatabase, kb: dict, args: list[str]) -> None:
    stage = " ".join(args).casefold() if args else "final"
    if stage in ("论文", "paper", "结构"):
        items = kb.get("paper_structure_checklist", [])
        title = "论文结构"
    else:
        aliases = {
            "数据": "data",
            "模型": "model",
            "写作": "paper",
            "writing": "paper",
            "终稿": "final",
            "提交": "final",
            "final": "final",
        }
        key = aliases.get(stage, stage)
        if key == "paper":
            items = kb.get("paper_structure_checklist", [])
            title = "论文结构"
            key = ""
        if key == "final" and not args:
            key = "final"
        if key in CHECKS:
            items = CHECKS[key]
            title = {"data": "数据检查", "model": "模型检查", "final": "终稿检查"}[key]
        elif key:
            raise ValueError("阶段可用值：paper、data、model、final，或对应中文名称。")
    print(title)
    for item in items:
        print(f"[ ] {item}")
    if title == "终稿检查":
        print("\n论文结构参考：")
        for item in kb.get("paper_structure_checklist", []):
            print(f"[ ] {item}")


COMMANDS: dict[str, Callable[[PaperDatabase, dict, list[str]], None]] = {
    "overview": overview,
    "analyze": analyze,
    "method": method_lookup,
    "paper": paper_lookup,
    "write": write_section,
    "process": process,
    "code": code_template,
    "check": checklist,
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="查询 APMCM 竞赛资料并输出方法、流程和写作模板。",
        epilog="示例：python .claude/skills/builtmodel/scripts/main.py analyze '预测未来销量'",
    )
    parser.add_argument("command", nargs="?", choices=COMMANDS, default="overview")
    parser.add_argument("arguments", nargs="*")
    parsed = parser.parse_args(argv)
    try:
        db, kb = load_data()
        COMMANDS[parsed.command](db, kb, parsed.arguments)
    except (FileNotFoundError, ValueError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
