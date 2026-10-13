---
name: builtmodel
description: APMCM 数学建模竞赛助手。用于分析赛题、检索仓库论文与方法、生成写作和代码起始模板、规划竞赛流程及检查论文。
---

# APMCM 数学建模助手（Codex）

Use this skill for APMCM preparation and competition work in Codex. This repository also contains a Claude Code version under `.claude/skills/builtmodel/`; the guidance and CLI commands are parallel, while invocation and skill locations are platform-specific.

## 运行查询工具

从本仓库根目录运行仓库内 CLI：

```powershell
python .agents/skills/builtmodel/scripts/main.py [command] [arguments]
```

用户没有指定命令时运行 `overview`。将题目描述和章节名原样传给对应命令；含空格的参数需加引号。

## 命令

- `overview`：显示数据库统计和已覆盖的问题类型。
- `analyze <题目描述>`：初步分类并列出方法、适用场景和工具；结合目标、变量、约束和数据核验匹配结果。
- `method <方法名或问题类型>`：查询方法说明及适用条件，并报告数据库是否有对应标注论文。
- `paper <论文编号或关键词>`：检索论文记录，例如 `2025-A`。记录中的 PDF 路径不代表已经读取 PDF。
- `write <章节>`：给出写作检查项和 LaTeX 起始模板；依据题目、数据和计算结果替换所有占位内容。
- `process [阶段]`：查看备赛、选题、调研建模、写作或提交阶段任务。
- `code <类型>`：生成优化、预测、评价、分类、ODE 或图论的起始代码；根据实际数据补齐并检查依赖、边界和输出。
- `check [阶段]`：检查论文结构、数据、模型或提交材料。

## 工作要求

1. 对依赖仓库数据的问题先运行 CLI，再按需阅读 `mathmodel.md`、`APMCM竞赛执行流程总结.md`、`往届题目分析总结.md` 或 `优秀论文学习指南.md`。
2. 说明方法适用条件和局限。题目目标、约束或数据缺失时，指出缺口，不虚构假设、论文内容或结果。
3. 让论文内容可以追溯到用户数据和计算过程；不要把模板占位符或未验证代码写成事实。
4. 当前数据库有 16 篇论文记录、尚无方法标注。方法或相似论文检索为空时，说明数据库覆盖限制，并转向题目分析资料继续判断。

## 示例

在 Codex 中显式调用：

```text
$builtmodel analyze 预测销量并优化库存
$builtmodel paper 2025-A
$builtmodel write 摘要
```

命令行直接运行：

```powershell
python .agents/skills/builtmodel/scripts/main.py analyze "预测销量并优化库存"
python .agents/skills/builtmodel/scripts/main.py paper 2025-A
```
