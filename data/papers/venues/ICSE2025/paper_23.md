# Licoeval: Evaluating LLMs on License Compliance in Code Generation

**Authors**: Xu, Weiwei and Gao, Kai and He, Hao and Zhou, Minghui

**Abstract**:

Recent advances in Large Language Models (LLMs) have revolutionized code generation, leading to widespread adoption of AI coding tools by developers. However, LLMs can generate license-protected code without providing the necessary license information, leading to potential intellectual property violations during software production. This paper addresses the critical, yet underexplored, issue of license compliance in LLM-generated code by establishing a benchmark to evaluate the ability of LLMs to provide accurate license information for their generated code. To establish this benchmark, we conduct an empirical study to identify a reasonable standard for “striking similarity” that excludes the possibility of independent creation, indicating a copy relationship between the LLM output and certain opensource code. Based on this standard, we propose LiCoEval, to evaluate the license compliance capabilities of LLMs, i.e., the ability to provide accurate license or copyright information when they generate code with striking similarity to already existing copyrighted code. Using LiCoEval, we evaluate 14 popular LLMs, finding that even top-performing LLMs produce a non-negligible proportion (0.88 % to 2.01 %) of code strikingly similar to existing open-source implementations. Notably, most LLMs fail to provide accurate license information, particularly for code under copyleft licenses. These findings underscore the urgent need to enhance LLM compliance capabilities in code generation tasks. Our study provides a foundation for future research and development to improve license compliance in AIassisted software development, contributing to both the protection of open-source software copyrights and the mitigation of legal risks for LLM users.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00052)

**Labels**: [empirical study](../../labels/empirical_study.md), [code generation](../../labels/code_generation.md)
