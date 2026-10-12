"""
LaTeX论文模板片段
用于快速生成数学建模论文的各个部分
"""

# 摘要模板
ABSTRACT_TEMPLATE = r"""
\begin{abstract}
\textbf{摘要：}

针对XXX问题，本文建立了XXX模型，运用XXX方法进行求解。

\textbf{针对问题一}，我们分析了XXX因素对XXX的影响。通过XXX方法，建立了XXX模型。求解得到XXX结果。

\textbf{针对问题二}，我们进一步考虑了XXX约束条件。采用XXX算法进行优化，得到最优解为XXX。

\textbf{针对问题三}，我们进行了敏感性分析和模型检验，结果表明模型具有良好的稳定性和适用性。

最后，我们对模型进行了评价和推广，指出了改进方向。

\textbf{关键词：}XXX；XXX；XXX；XXX

\end{abstract}
"""

# 优化模型模板
OPTIMIZATION_MODEL = r"""
\subsection{模型建立}

\subsubsection{目标函数}
本问题的优化目标是XXX，建立目标函数如下：
\begin{equation}
\min \quad Z = f(x_1, x_2, \ldots, x_n)
\end{equation}

\subsubsection{约束条件}
根据问题分析，模型需要满足以下约束：
\begin{align}
g_i(x_1, x_2, \ldots, x_n) &\leq b_i, \quad i=1,2,\ldots,m \\
h_j(x_1, x_2, \ldots, x_n) &= c_j, \quad j=1,2,\ldots,p \\
x_k &\geq 0, \quad k=1,2,\ldots,n
\end{align}

\subsubsection{完整模型}
综上，建立优化模型如下：
\begin{equation}
\begin{aligned}
\min \quad & f(x_1, x_2, \ldots, x_n) \\
\text{s.t.} \quad & g_i(x_1, x_2, \ldots, x_n) \leq b_i, \quad i=1,2,\ldots,m \\
& h_j(x_1, x_2, \ldots, x_n) = c_j, \quad j=1,2,\ldots,p \\
& x_k \geq 0, \quad k=1,2,\ldots,n
\end{aligned}
\end{equation}
"""

# 层次分析法模板
AHP_MODEL = r"""
\subsection{层次分析法(AHP)}

\subsubsection{建立层次结构}
将决策问题分为目标层、准则层和方案层。

\subsubsection{构造判断矩阵}
对同一层次的元素两两比较，构造判断矩阵：
\begin{equation}
A = (a_{ij})_{n \times n}
\end{equation}
其中，$a_{ij}$表示元素$i$相对于元素$j$的重要程度。

\subsubsection{计算权重向量}
采用特征值法计算权重：
\begin{equation}
AW = \lambda_{\max}W
\end{equation}
对特征向量归一化得到权重向量$W$。

\subsubsection{一致性检验}
计算一致性指标：
\begin{equation}
CI = \frac{\lambda_{\max} - n}{n-1}
\end{equation}
一致性比率：
\begin{equation}
CR = \frac{CI}{RI}
\end{equation}
当$CR < 0.1$时，认为判断矩阵具有满意的一致性。
"""

# 时间序列模板
TIME_SERIES_MODEL = r"""
\subsection{ARIMA时间序列模型}

\subsubsection{平稳性检验}
对原始序列进行ADF检验，判断序列的平稳性。

\subsubsection{差分处理}
若序列非平稳，进行$d$阶差分：
\begin{equation}
\nabla^d y_t = (1-B)^d y_t
\end{equation}

\subsubsection{模型定阶}
通过ACF和PACF图确定ARIMA$(p,d,q)$模型的阶数。

\subsubsection{参数估计}
ARIMA$(p,d,q)$模型的数学表达式为：
\begin{equation}
\phi(B)(1-B)^d y_t = \theta(B)\varepsilon_t
\end{equation}
其中：
\begin{itemize}
\item $\phi(B) = 1 - \phi_1 B - \phi_2 B^2 - \cdots - \phi_p B^p$为自回归多项式
\item $\theta(B) = 1 + \theta_1 B + \theta_2 B^2 + \cdots + \theta_q B^q$为移动平均多项式
\item $\varepsilon_t$为白噪声序列
\end{itemize}
"""

# 表格模板
TABLE_TEMPLATE = r"""
\begin{table}[htbp]
\centering
\caption{XXX}
\label{tab:xxx}
\begin{tabular}{cccc}
\toprule
列1 & 列2 & 列3 & 列4 \\
\midrule
数据1 & 数据2 & 数据3 & 数据4 \\
数据5 & 数据6 & 数据7 & 数据8 \\
\bottomrule
\end{tabular}
\end{table}
"""

# 图片模板
FIGURE_TEMPLATE = r"""
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{figures/xxx.png}
\caption{XXX}
\label{fig:xxx}
\end{figure}
"""

# 符号说明模板
NOTATION_TEMPLATE = r"""
\section{符号说明}
\begin{table}[htbp]
\centering
\caption{符号说明}
\begin{tabular}{cl}
\toprule
符号 & 说明 \\
\midrule
$x_i$ & XXX \\
$y_j$ & XXX \\
$\alpha$ & XXX \\
$\beta$ & XXX \\
\bottomrule
\end{tabular}
\end{table}
"""

# 敏感性分析模板
SENSITIVITY_TEMPLATE = r"""
\section{敏感性分析}

为了检验模型的稳定性，我们对关键参数进行敏感性分析。

\subsection{参数扰动实验}
选取参数$\alpha$，在$[\alpha-20\%, \alpha+20\%]$范围内变动，观察目标函数的变化。

\begin{figure}[htbp]
\centering
\includegraphics[width=0.7\textwidth]{figures/sensitivity.png}
\caption{参数敏感性分析}
\label{fig:sensitivity}
\end{figure}

\subsection{结果分析}
从图\ref{fig:sensitivity}可以看出，当参数$\alpha$在XXX范围内变化时，目标函数值变化不超过XX\%，说明模型对该参数不敏感，具有良好的稳定性。
"""

# 模型评价模板
EVALUATION_TEMPLATE = r"""
\section{模型评价}

\subsection{模型优点}
\begin{itemize}
\item 模型建立合理，充分考虑了XXX因素
\item 求解方法科学，结果可靠
\item 模型具有良好的稳定性和适用性
\end{itemize}

\subsection{模型缺点}
\begin{itemize}
\item 假设XXX可能与实际情况存在偏差
\item 未考虑XXX因素的影响
\item 计算复杂度较高
\end{itemize}

\subsection{模型改进}
\begin{itemize}
\item 可以引入XXX方法来改进XXX
\item 可以考虑XXX因素的影响
\item 可以采用XXX算法提高求解效率
\end{itemize}
"""

if __name__ == "__main__":
    print("LaTeX模板库加载成功")
    print("可用模板:")
    print("- ABSTRACT_TEMPLATE: 摘要")
    print("- OPTIMIZATION_MODEL: 优化模型")
    print("- AHP_MODEL: 层次分析法")
    print("- TIME_SERIES_MODEL: 时间序列")
    print("- TABLE_TEMPLATE: 表格")
    print("- FIGURE_TEMPLATE: 图片")
    print("- NOTATION_TEMPLATE: 符号说明")
    print("- SENSITIVITY_TEMPLATE: 敏感性分析")
    print("- EVALUATION_TEMPLATE: 模型评价")
