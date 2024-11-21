# VulEval: Towards Repository-Level Evaluation of Software Vulnerability Detection

**Authors**: Xin{-}Cheng Wen and Xinchen Wang and Yujia Chen and Ruida Hu and David Lo and Cuiyun Gao

**Abstract**:

Deep Learning (DL)-based methods have proven to be effective for software vulnerability detection, with a potential for substantial productivity enhancements for detecting vulnerabilities. Current methods mainly focus on detecting single functions (i.e., intra-procedural vulnerabilities), ignoring the more complex inter-procedural vulnerability detection scenarios in practice. For example, developers routinely engage with program analysis to detect vulnerabilities that span multiple functions within repositories. In addition, the widely-used benchmark datasets generally contain only intra-procedural vulnerabilities, leaving the assessment of inter-procedural vulnerability detection capabilities unexplored.To mitigate the issues, we propose a repository-level evaluation system, named \textbf{VulEval}, aiming at evaluating the detection performance of inter- and intra-procedural vulnerabilities simultaneously. Specifically, VulEval consists of three interconnected evaluation tasks: \textbf{(1) Function-Level Vulnerability Detection}, aiming at detecting intra-procedural vulnerability given a code snippet; \textbf{(2) Vulnerability-Related Dependency Prediction}, aiming at retrieving the most relevant dependencies from call graphs for providing developers with explanations about the vulnerabilities; and \textbf{(3) Repository-Level Vulnerability Detection}, aiming at detecting inter-procedural vulnerabilities by combining with the dependencies identified in the second task. VulEval also consists of a large-scale dataset, with a total of 4,196 CVE entries, 232,239 functions, and corresponding 4,699 repository-level source code in C/C++ programming languages. Our analysis highlights the current progress and future directions for software vulnerability detection.

**Link**: [Read Paper](https://doi.org/10.48550/arXiv.2404.15596)

**Labels**: static analysis, bug detection, benchmark
