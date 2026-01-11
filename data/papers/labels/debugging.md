# Debugging

- [A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization](../venues/FSE2024/paper_5.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Fault Localization (FL), in which a developer seeks to identify which part of the code is malfunctioning and needs to be fixed, is a recurring challenge in debugging. To reduce developer burden, many automated FL techniques have been proposed. However, prior work has noted that existing techniques fail to provide rationales for the suggested locations, hindering developer adoption of these techniques. With this in mind, we propose AutoFL, a Large Language Model (LLM)-based FL technique that gene...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md)


- [COCA: Generative Root Cause Analysis for Distributed Systems with Code Knowledge](../venues/ICSE2025/paper_66.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Runtime failures are commonplace in modern distributed systems. When such issues arise, users often turn to platforms such as Github or JIRA to report them and request assistance. Automatically identifying the root cause of these failures is critical for ensuring high reliability and availability. However, prevailing automatic root cause analysis (RCA) approaches rely significantly on comprehensive runtime monitoring data, which is often not fully available in issue platforms. Recent methods lev...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [bug reproduction](bug_reproduction.md)


- [ChatDBG: Augmenting Debugging with Large Language Models](../venues/FSE2025/paper_24.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Debugging is a critical but challenging task for programmers. This paper proposes ChatDBG, an AI-powered debugging assistant. ChatDBG integrates large language models (LLMs) to significantly enhance the capabilities and user-friendliness of conventional debuggers. ChatDBG lets programmers engage in a collaborative dialogue with the debugger, allowing them to pose complex questions about program state, perform root cause analysis for crashes or assertion failures, and explore open-ended queries l...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md)


- [Effective Large Language Model Debugging with Best-first Tree Search](../venues/NVDIA2024/paper_1.md), ([NVDIA2024](../venues/NVDIA2024/README.md))

  - **Abstract**: Large Language Models (LLMs) show promise in code generation tasks. However, their code-writing abilities are often limited in scope: while they can successfully implement simple functions, they struggle with more complex tasks. A fundamental difference with how an LLM writes code, compared to a human programmer, is that it cannot consistently spot and fix bugs. Debugging is a crucial skill for programmers and it enables iterative code refinement towards a correct implementation. In this work, w...
  - **Labels**: [code generation](code_generation.md), [debugging](debugging.md)


- [Instruct, Not Assist: LLM-based Multi-Turn Planning and Hierarchical Questioning for Socratic Code Debugging](../venues/EMNLP2024/paper_10.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Socratic questioning is an effective teaching strategy, encouraging critical thinking and problem-solving. The conversational capabilities of large language models (LLMs) show great potential for providing scalable, real-time student guidance. However, current LLMs often give away solutions directly, making them ineffective instructors. We tackle this issue in the code debugging domain with TreeInstruct, an Instructor agent guided by a novel state space-based planning algorithm. TreeInstruct ask...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [agent design](agent_design.md), [planning](planning.md)


- [Isolating Compiler Bugs by Generating Effective Witness Programs With Large Language Models](../venues/TSE2024/paper_4.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Compiler bugs pose a significant threat to safety-critical applications, and promptly as well as effectively isolating these bugs is crucial for assuring the quality of compilers. However, the limited availability of debugging information on reported bugs complicates the compiler bug isolation task. Existing compiler bug isolation approaches convert the problem into a test program mutation problem, but they are still limited by ineffective mutation strategies or high human effort requirements. D...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [LPR: Large Language Models-Aided Program Reduction](../venues/ISSTA2024/paper_5.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Program reduction is a widely used technique to facilitate debugging                compilers by automatically minimizing programs that trigger                compiler bugs. Existing program reduction techniques are either                generic to a wide range of languages (such as Perses and Vulcan)                or specifically optimized for one certain language by exploiting                language-specific knowledge (e.g., C-Reduce). However, synergistically                combining both g...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [program testing](program_testing.md), [debugging](debugging.md)


- [Large Language Models for Test-Free Fault Localization](../venues/ICSE2024/paper_3.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Fault Localization (FL) aims to automatically localize buggy lines of code, a key first step in many manual and automatic debugging tasks. Previous FL techniques assume the provision of input tests, and often require extensive program analysis, program instrumentation, or data preprocessing. Prior work on deep learning for APR struggles to learn from small datasets and produces limited results on real-world programs. Inspired by the ability of large language models (LLMs) of code to adapt to new...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [NIODebugger: A Novel Approach to Repair Non-Idempotent-Outcome Tests with LLM-Based Agent](../venues/ICSE2025/paper_61.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Flaky tests, characterized by inconsistent results across repeated executions, present significant challenges in software testing, especially during regression testing. Recently, there has been emerging research interest in non-idempotentoutcome (NIO) flaky tests-tests that pass on the initial run but fail on subsequent executions within the same environment. Despite progress in utilizing Large Language Models (LLMs) to address flaky tests, existing methods have not tackled NIO flaky tests. The ...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [bug reproduction](bug_reproduction.md), [code generation](code_generation.md), [program repair](program_repair.md)


- [Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning](../venues/FSE2024/paper_29.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Program slicing, the process of extracting program statements that influence values at a designated location (known as the slicing criterion), is helpful in both manual and automated debugging. However, such slicing techniques prove ineffective in scenarios where executing specific inputs is prohibitively expensive, or even impossible, as with partial code. In this paper, we introduce ND-Slicer, a predictive slicing methodology that caters to specific executions based on a particular input, over...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Reasoning Runtime Behavior of a Program with LLM: How Far are We?](../venues/ICSE2025/paper_9.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large language models for code (i.e., code LLMs) have shown strong code understanding and generation capabilities. To evaluate the capabilities of code LLMs in various aspects, many benchmarks have been proposed (e.g., HumanEval and ClassEval). Code reasoning is one of the most essential abilities of code LLMs (i.e., predicting code execution behaviors such as program output and execution path), but existing benchmarks for code reasoning are not sufficient. Typically, they focus on predicting th...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)


- [SelfPiCo: Self-Guided Partial Code Execution with LLMs](../venues/ISSTA2024/paper_16.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Code executability plays a vital role in software debugging and testing (e.g., detecting runtime exceptions or assertion violations). However, code execution, especially partial or arbitrary code execution, is a non-trivial task due to missing definitions and complex third-party dependencies. To make partial code (such as code snippets posted on the web or code fragments deep inside complex software projects) executable, the existing study has proposed a machine learning model to predict the und...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md)


- [Show Me Why It’s Correct: Saving 1/3 of Debugging Time in Program Repair with Interactive Runtime Comparison](../venues/OOPSLA2025/paper_1.md), ([OOPSLA2025](../venues/OOPSLA2025/README.md))

  - **Abstract**: Automated Program Repair (APR) holds the promise of alleviating the burden of debugging and fixing software bugs. Despite this, developers still need to manually inspect each patch to confirm its correctness, which is tedious and time-consuming. This challenge is exacerbated in the presence of plausible patches, which accidentally pass test cases but may not correctly fix the bug. To address this challenge, we propose an interactive approach called iFix to facilitate patch understanding and comp...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [program testing](program_testing.md), [debugging](debugging.md)


- [Teaching large language models to self-debug](../venues/ICLR2024/paper_7.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Large language models (LLMs) have achieved impressive performance on code generation. However, for complex programming tasks, generating the correct solution in one go becomes challenging, thus some prior works have designed program repair approaches to improve code generation performance. In this work, we propose Self-Debugging, which teaches a large language model to debug its predicted program via few-shot demonstrations. In particular, we demonstrate that Self-Debugging can teach the large l...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md)


- [Treefix: Enabling Execution with a Tree of Prefixes](../venues/ICSE2025/paper_59.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: The ability to execute code is a prerequisite for various dynamic program analyses. Learning-guided execution has been proposed as an approach to enable the execution of arbitrary code snippets by letting a neural model predict likely values for any missing variables. Although state-of-the-art learning-guided execution approaches, such as LExecutor, can enable the execution of a relative high amount of code, they are limited to predicting a restricted set of possible values and do not use any fe...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md)


- [{COAST}: Enhancing the Code Debugging Ability of {LLM}s through Communicative Agent Based Data Synthesis](../venues/NAACL2025/paper_12.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Code debugging is a vital stage of software development, essential for ensuring the reliability and performance of Large Language Models (LLMs) in the code generation task. Human debugging typically follows a multi-stage process, which includes Bug Localization, Bug Identification, Code Repair, and Code Recognition. However, existing code debugging benchmarks predominantly focus on the Code Repair stage, which offers only a limited perspective on evaluating the debugging capabilities of LLMs. In...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [agent design](agent_design.md), [code model](code_model.md), [code model training](code_model_training.md)
