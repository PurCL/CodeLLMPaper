# Bug Reproduction

- [A Knowledge Enhanced Large Language Model for Bug Localization](../venues/FSE2025/paper_25.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: A significant number of bug reports are generated every day as software systems continue to develop. Large Language Models (LLMs) have been used to correlate bug reports with source code to locate bugs automatically. The existing research has shown that LLMs are effective for bug localization and can increase software development efficiency. However, these studies still have two limitations. First, these models fail to capture context information about bug reports and source code. Second, these ...
  - **Labels**: [program testing](program_testing.md), [bug reproduction](bug_reproduction.md)


- [COCA: Generative Root Cause Analysis for Distributed Systems with Code Knowledge](../venues/ICSE2025/paper_66.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Runtime failures are commonplace in modern distributed systems. When such issues arise, users often turn to platforms such as Github or JIRA to report them and request assistance. Automatically identifying the root cause of these failures is critical for ensuring high reliability and availability. However, prevailing automatic root cause analysis (RCA) approaches rely significantly on comprehensive runtime monitoring data, which is often not fully available in issue platforms. Recent methods lev...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [bug reproduction](bug_reproduction.md)


- [Evaluating Diverse Large Language Models for Automatic and General Bug Reproduction](../venues/TSE2024/paper_13.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Bug reproduction is a critical developer activity that is also challenging to automate, as bug reports are often in natural language and thus can be difficult to transform to test cases consistently. As a result, existing techniques mostly focused on crash bugs, which are easier to automatically detect and verify. In this work, we overcome this limitation by using large language models (LLMs), which have been demonstrated to be adept at natural language processing and code generation. By prompti...
  - **Labels**: [program testing](program_testing.md), [bug reproduction](bug_reproduction.md), [empirical study](empirical_study.md)


- [Large Language Models are Few-Shot Testers: Exploring LLM-Based General Bug Reproduction](../venues/ICSE2023/paper_5.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Many automated test generation techniques have been developed to aid developers with writing tests. To facilitate full automation, most existing techniques aim to either increase coverage, or generate exploratory inputs. However, existing test generation techniques largely fall short of achieving more semantic objectives, such as generating tests to reproduce a given bug report. Reproducing bugs is nonetheless important, as our empirical study shows that the number of tests added in open source ...
  - **Labels**: [program testing](program_testing.md), [bug reproduction](bug_reproduction.md)


- [NIODebugger: A Novel Approach to Repair Non-Idempotent-Outcome Tests with LLM-Based Agent](../venues/ICSE2025/paper_61.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Flaky tests, characterized by inconsistent results across repeated executions, present significant challenges in software testing, especially during regression testing. Recently, there has been emerging research interest in non-idempotentoutcome (NIO) flaky tests-tests that pass on the initial run but fail on subsequent executions within the same environment. Despite progress in utilizing Large Language Models (LLMs) to address flaky tests, existing methods have not tackled NIO flaky tests. The ...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [bug reproduction](bug_reproduction.md), [code generation](code_generation.md), [program repair](program_repair.md)


- [ReproCopilot: LLM-Driven Failure Reproduction with Dynamic Refinement](../venues/FSE2025/paper_37.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Failure reproduction is a crucial step for debugging software systems, but it is often challenging and time-consuming, especially when the failures are caused by complex inputs, states, or environments. In this paper, we present ReproCopilot, a tool that leverages program analysis and a large language model (LLM) to generate a workload (i.e., code and inputs) that can reproduce a given failure. ReproCopilot proposes two novel techniques: state-oriented code generation and dynamic refinement. The...
  - **Labels**: [program testing](program_testing.md), [bug reproduction](bug_reproduction.md)
