# Code Model Robustness

- [Calibration and Correctness of Language Models for Code](../venues/ICSE2025/paper_19.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Machine learning models are widely used, but can also often be wrong. Users would benefit from a reliable indication of whether a given output from a given model should be trusted, so a rational decision can be made whether to use the output or not. For example, outputs can be associated with a confidence measure; if this confidence measure is strongly associated with likelihood of correctness, then the model is said to be well-calibrated. A well-calibrated confidence measure can serve as a basi...
  - **Labels**: [code model](code_model.md), [code model robustness](code_model_robustness.md)


- [CodeFort: Robust Training for Code Generation Models](../venues/EMNLP2024/paper_39.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Code generation models are not robust to small perturbations, which often lead to inconsistent and incorrect generations and significantly degrade the performance of these models. Improving the robustness of code generation models is crucial to better user experience when these models are deployed in real-world applications. However, existing efforts have not addressed this issue for code generation models. To fill this gap, we propose CodeFort, a framework to improve the robustness of code gene...
  - **Labels**: [code generation](code_generation.md), [code model](code_model.md), [code model training](code_model_training.md), [code model](code_model.md), [code model robustness](code_model_robustness.md)


- [CodeImprove: Program Adaptation for Deep Code Models](../venues/ICSE2025/paper_42.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Leveraging deep learning (DL)-based code analysis tools to solve software engineering tasks is becoming increasingly popular. Code models often suffer performance degradation due to various reasons (e.g., code data shifts). Retraining is often required to address these issues, but frequent model updates are costly in labeling and deployment. In this paper, we explore an alternative solution: Adapting the program inputs to the code models. This can be achieved by two steps: 1) input validation th...
  - **Labels**: [general coding task](general_coding_task.md), [code generation](code_generation.md), [code model](code_model.md), [code model robustness](code_model_robustness.md)


- [Iterative Generation of Adversarial Example for Deep Code Models](../venues/ICSE2025/paper_26.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Deep code models are vulnerable to adversarial attacks, making it possible for semantically identical inputs to trigger different responses. Current black-box attack methods typically prioritize the impact of identifiers on the model based on custom importance scores or program context and incrementally replace identifiers to generate adversarial examples. However, these methods often fail to fully leverage feedback from failed attacks to guide subsequent attacks, resulting in problems such as l...
  - **Labels**: [code model](code_model.md), [code model robustness](code_model_robustness.md)


- [LLMEffiChecker: Understanding and Testing Efficiency Degradation of Large Language Models](../venues/TOSEM2024/paper_4.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have received much recent attention due to their human-level accuracy. While existing works mostly focus on either improving accuracy or testing accuracy robustness, the computation efficiency of LLMs, which is of paramount importance due to often vast generation demands and real-time requirements, has surprisingly received little attention. In this article, we make the first attempt to understand and test potential computation efficiency robustness in state-of-the-a...
  - **Labels**: [code model](code_model.md), [code model robustness](code_model_robustness.md)


- [Make a Feint to the East While Attacking in the West: Blinding LLM-Based Code Auditors with Flashboom Attacks](../venues/S&P2025/paper_5.md), ([S&P2025](../venues/S&P2025/README.md))

  - **Abstract**: LLM-based vulnerability auditors (e.g., GitHub Copilot) represent a significant advancement in automated code analysis, offering precise detection of security vulnerabilities. This paper explores the potential to circumvent LLM-based vulnerability auditors by diverting their focus, decided by the LLM attention mechanism, away from real vulnerable code segments. In these LLM-based vulnerability auditors, the attention mechanism is supposed to focus on potentially vulnerable code sections to ident...
  - **Labels**: [code model](code_model.md), [code model robustness](code_model_robustness.md)


- [Metamorphic-Based Many-Objective Distillation of LLMs for Code-Related Tasks](../venues/ICSE2025/paper_64.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Knowledge distillation compresses large language models (LLMs) into more compact and efficient versions that achieve similar accuracy on code-related tasks. However, as we demonstrate in this study, compressed models are four times less robust than the original LLMs when evaluated with metamorphic code. They exhibit a $\mathbf{4 4 0 \%}$ higher probability of misclassifying code clones due to minor changes in the code fragment under analysis, such as replacing parameter names with synonyms. To a...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [code model robustness](code_model_robustness.md)


- [RMCBench: Benchmarking Large Language Models' Resistance to Malicious Code](../venues/ASE2024/paper_18.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Warning: Please note that this article contains potential harmful or offensive content. This content is only for the evaluating and analysis of LLMs and does not imply any intention to promote criminal activities.The emergence of Large Language Models (LLMs) has significantly influenced various aspects of software development activities. Despite their benefits, LLMs also pose notable risks, including the potential to generate harmful content and being abused by malicious developers to create mal...
  - **Labels**: [code generation](code_generation.md), [benchmark](benchmark.md), [code model](code_model.md), [code model robustness](code_model_robustness.md)


- [ReCode: Robustness Evaluation of Code Generation Models](../venues/ACL2023/paper_13.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Code generation models have achieved impressive performance. However, they tend to be brittle as slight edits to a prompt could lead to very different generations; these robustness properties, critical for user experience when deployed in real-life applications, are not well understood. Most existing works on robustness in text or code tasks have focused on classification, while robustness in generation tasks is an uncharted area and to date there is no comprehensive benchmark for robustness in ...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [code model](code_model.md), [code model robustness](code_model_robustness.md)


- [Robust Vulnerability Detection across Compilations: LLVM-IR vs. Assembly with Transformer Model](../venues/ISSTA2025/paper_9.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Detecting vulnerabilities in binary files is a challenging task in cybersecurity, particularly when source code is unavailable and the compilation process and its parameters are unknown. Existing deep learning-based detection methods often rely on knowing a binary’s specific compilation settings, which may limit their ability to perform well on other types of binaries. In this research, we provide a thorough comparison of assembly representation and LLVM-IR to identify which representation is mo...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model robustness](code_model_robustness.md)


- [Statement-Level Adversarial Attack on Vulnerability Detection Models via Out-of-Distribution Features](../venues/FSE2025/paper_41.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Code vulnerability detection is crucial to ensure software security. Recent advancements, particularly with the emergence of Code Pre-Trained Models (CodePTMs) and Large Language Models (LLMs), have led to significant progress in this area. However, these models are easily susceptible to adversarial attacks, where even slight input modifications can lead the models to generate opposite results. Existing adversarial approaches, such as identifier replacement, code transformation, and dead code in...
  - **Labels**: [code model](code_model.md), [code model robustness](code_model_robustness.md), [static analysis](static_analysis.md), [bug detection](bug_detection.md)
