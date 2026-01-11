# Program Optimization

- [CompilerDream: Learning a Compiler World Model for General Code Optimization](../venues/KDD2025/paper_1.md), ([KDD2025](../venues/KDD2025/README.md))

  - **Abstract**: Effective code optimization in compilers is crucial for computer and software engineering. The success of these optimizations primarily depends on the selection and ordering of the optimization passes applied to the code. While most compilers rely on a fixed sequence of optimization passes, current methods to find the optimal sequence either employ impractically slow search algorithms or learning methods that struggle to generalize to code unseen during training. We introduce CompilerDream, a mo...
  - **Labels**: [static analysis](static_analysis.md), [program optimization](program_optimization.md)


- [CompilerGym: robust, performant compiler optimization environments for AI research](../venues/CGO2022/paper_1.md), ([CGO2022](../venues/CGO2022/README.md))

  - **Abstract**: Interest in applying Artificial Intelligence (AI) techniques to compiler optimizations is increasing rapidly, but compiler research has a high entry barrier. Unlike in other domains, compiler and AI researchers do not have access to the datasets and frameworks that enable fast iteration and development of ideas, and getting started requires a significant engineering investment. What is needed is an easy, reusable experimental infrastructure for real world compiler optimization tasks that can ser...
  - **Labels**: [static analysis](static_analysis.md), [program optimization](program_optimization.md), [benchmark](benchmark.md)


- [LLM Compiler: Foundation Language Models for Compiler Optimization](../venues/CC2025/paper_1.md), ([CC2025](../venues/CC2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated remarkable capabilities across a variety of software engineering and coding tasks. However, their application in the domain of code and compiler optimization remains underexplored. Training LLMs is resource-intensive, requiring substantial GPU hours and extensive data collection, which can be prohibitive. To address this gap, we introduce LLM Compiler, a suite of robust, openly available, pre-trained models specifically designed for compiler tasks. ...
  - **Labels**: [static analysis](static_analysis.md), [program optimization](program_optimization.md), [code model](code_model.md), [code model training](code_model_training.md), [IR code model](IR_code_model.md)


- [Language Models for Code Optimization: Survey, Challenges and Future Directions](../venues/arXiv2025/paper_5.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Language models (LMs) built upon deep neural networks (DNNs) have recently demonstrated breakthrough effectiveness in software engineering tasks such as code generation, completion, and repair. This has paved the way for the emergence of LM-based code optimization techniques, which are crucial for enhancing the performance of existing programs, such as accelerating program execution time. However, a comprehensive survey dedicated to this specific application has been lacking. To fill this gap, w...
  - **Labels**: [static analysis](static_analysis.md), [program optimization](program_optimization.md), [survey](survey.md)


- [Programl: A graph-based program representation for data flow analysis and compiler optimizations](../venues/ICML2021/paper_2.md), ([ICML2021](../venues/ICML2021/README.md))

  - **Abstract**: Machine learning (ML) is increasingly seen as a viable approach for building compiler optimization heuristics, but many ML methods cannot replicate even the simplest of the data flow analyses that are critical to making good optimization decisions. We posit that if ML cannot do that, then it is insufficiently able to reason about programs. We formulate data flow analyses as supervised learning tasks and introduce a large open dataset of programs and their corresponding labels from several analys...
  - **Labels**: [static analysis](static_analysis.md), [data-flow analysis](data-flow_analysis.md), [program optimization](program_optimization.md), [code model](code_model.md), [code model training](code_model_training.md), [IR code model](IR_code_model.md)


- [Reductive Analysis with Compiler-Guided Large Language Models for Input-Centric Code Optimizations](../venues/PLDI2025/paper_4.md), ([PLDI2025](../venues/PLDI2025/README.md))

  - **Abstract**: Input-centric program optimization aims to optimize code by considering the relations between program inputs and program behaviors. Despite its promise, a long-standing barrier for its adoption is the difficulty of automatically identifying critical features of complex inputs. This paper introduces a novel technique, reductive analysis through compiler-guided Large Language Models (LLMs), to solve the problem through a synergy between compilers and LLMs. It uses a reductive approach to overcome ...
  - **Labels**: [static analysis](static_analysis.md), [program optimization](program_optimization.md)


- [Search-Based LLMs for Code Optimization](../venues/ICSE2025/paper_12.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: The code written by developers usually suffers from efficiency problems and contain various performance bugs. These inefficiencies necessitate the research of automated refactoring methods for code optimization. Early research in code optimization employs rule-based methods and focuses on specific inefficiency issues, which are labor-intensive and suffer from the low coverage issue. Recent work regards the task as a sequence generation problem, and resorts to deep learning (DL) techniques such a...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [static analysis](static_analysis.md), [program optimization](program_optimization.md)


- [{DCE}-{LLM}: Dead Code Elimination with Large Language Models](../venues/NAACL2025/paper_8.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Dead code introduces several challenges in software development, such as increased binary size and maintenance difficulties. It can also obscure logical errors and be exploited for obfuscation in malware. For LLM-based code-related tasks, dead code introduces vulnerabilities that can mislead these models, raising security concerns. Although modern compilers and IDEs offer dead code elimination, sophisticated patterns can bypass these tools. A universal approach that includes classification, loca...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [program optimization](program_optimization.md)
