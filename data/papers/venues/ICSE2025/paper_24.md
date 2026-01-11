# An Empirical Study on Automatically Detecting AI-Generated Source Code: How Far are We?

**Authors**: Suh, Hyunjae and Tafreshipour, Mahan and Li, Jiawei and Bhattiprolu, Adithya and Ahmed, Iftekhar

**Abstract**:

Artificial Intelligence (AI) techniques, especially Large Language Models (LLMs), have started gaining popularity among researchers and software developers for generating source code. However, LLMs have been shown to generate code with quality issues and also incurred copyright/licensing infringements. Therefore, detecting whether a piece of source code is written by humans or AI has become necessary. This study first presents an empirical analysis to investigate the effectiveness of the existing AI detection tools in detecting AI-generated code. The results show that they all perform poorly and lack sufficient generalizability to be practically deployed. Then, to improve the performance of AI-generated code detection, we propose a range of approaches, including fine-tuning the LLMs and machine learning-based classification with static code metrics or code embedding generated from Abstract Syntax Tree (AST). Our best model outperforms state-of-the-art AI-generated code detector (GPTSniffer) and achieves an F1 score of 82.55. We also conduct an ablation study on our best-performing model to investigate the impact of different source code features on its performance.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00064)

**Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [empirical study](../../labels/empirical_study.md)
