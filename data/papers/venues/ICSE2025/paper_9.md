# Reasoning Runtime Behavior of a Program with LLM: How Far are We?

**Authors**: Chen, Junkai and Pan, Zhiyuan and Hu, Xing and Li, Zhenhao and Li, Ge and Xia, Xin

**Abstract**:

Large language models for code (i.e., code LLMs) have shown strong code understanding and generation capabilities. To evaluate the capabilities of code LLMs in various aspects, many benchmarks have been proposed (e.g., HumanEval and ClassEval). Code reasoning is one of the most essential abilities of code LLMs (i.e., predicting code execution behaviors such as program output and execution path), but existing benchmarks for code reasoning are not sufficient. Typically, they focus on predicting the input and output of a program, ignoring the evaluation of the intermediate behavior during program execution, as well as the logical consistency (e.g., the model should not give the correct output if the prediction of execution path is wrong) when performing the reasoning. To address these problems, in this paper, we propose a framework, namely $\boldsymbol{\mathcal{R}\mathbf{Eval}$, for evaluating code reasoning abilities and consistency of code LLMs with program execution. We utilize existing code benchmarks and adapt them to new benchmarks within our framework. A large-scale empirical study is conducted and most LLMs show unsatisfactory performance on both Runtime Behavior Reasoning (i.e., an average accuracy of 44.4%) and Incremental Consistency Evaluation (i.e., an average IC score of 10.3). Evaluation results of current code LLMs reflect the urgent need for the community to strengthen the code reasoning capability of code LLMs. Our code, data and $\boldsymbol{\mathcal{R}\mathbf{Eval}$ leaderboard are available at https://r-eval.github.io.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00012)

**Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md), [benchmark](../../labels/benchmark.md), [empirical study](../../labels/empirical_study.md)
