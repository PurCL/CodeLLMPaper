# Large Language Model powered Symbolic Execution

**Authors**: Yihe Li, Ruijie Meng, Gregory J. Duck

**Abstract**:

Large Language Models (LLMs) have emerged as a promising alternative to traditional static program analysis methods, such as symbolic execution, offering the ability to reason over code directly without relying on theorem provers or SMT solvers. However, LLMs are also inherently probabilistic by nature, and therefore face significant challenges in relation to the accuracy and scale of the analysis in real-world application. Such issues often necessitate the use of larger LLMs with higher token limits, but this requires enterprise-grade hardware (GPUs) and thus limits accessibility for many users. In this paper, we propose LLM-based symbolic execution -- a novel approach that enhances LLM inference via a path-based decomposition of the program analysis tasks into smaller (more tractable) sub-tasks. The core idea is to generalize path constraints using a generic code-based representation that the LLM can directly reason over, and without translation into another (less-expressive) formal language. We implement our approach in the form of AutoExe, an LLM-based symbolic execution engine that is lightweight and language-agnostic, making it a practical tool for analyzing code that is challenging for traditional approaches. We show that AutoExe can improve both the accuracy and scale of LLM-based program analysis, especially for smaller LLMs that can run on consumer grade hardware.

**Link**: [Read Paper](https://arxiv.org/pdf/2505.13452)

**Labels**: [static analysis](../../labels/static_analysis.md), [symbolic execution](../../labels/symbolic_execution.md)
