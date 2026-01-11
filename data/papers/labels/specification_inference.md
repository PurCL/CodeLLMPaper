# Specification Inference

- [AdverIntent-Agent: Adversarial Reasoning for Repair Based on Inferred Program Intent](../venues/ISSTA2025/paper_18.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Automated program repair (APR) has shown promising results, particularly with the use of neural networks. Currently, most APR tools focus on code transformations specified by test suites, rather than reasoning about the program’s intent and the high-level bug specification. Without a proper understanding of program intent, these tools tend to generate patches that overfit incomplete test suites and fail to reflect the developer’s intentions. However, reasoning about program intent is challenging...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [Can LLMs Implicitly Learn Numeric Parameter Constraints in Data Science APIs?](../venues/NeurIPS2024/paper_8.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Data science (DS) programs, typically built on popular DS libraries (such as PyTorch and NumPy) with thousands of APIs, serve as the cornerstone for various mission-critical domains such as financial systems, autonomous driving software, and coding assistants. Recently, large language models (LLMs) have been widely applied to generate DS programs across diverse scenarios, such as assisting users for DS programming or detecting critical vulnerabilities in DS frameworks. Such applications have all...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [Can LLMs Reason About Program Semantics? A Comprehensive Evaluation of LLMs on Formal Specification Inference](../venues/arXiv2025/paper_11.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Large Language Models (LLMs) are increasingly being used to automate programming tasks. Yet, LLMs' capabilities in reasoning about program semantics are still inadequately studied, leaving significant potential for further exploration. This paper introduces FormalBench, a comprehensive benchmark designed to evaluate LLMs' reasoning abilities on program semantics, particularly via the task of synthesizing formal program specifications to assist verifying program correctness. This task requires bo...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)


- [Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions?](../venues/FSE2024/paper_9.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Informal natural language that describes code functionality, such as code comments or function documentation, may contain substantial information about a program’s intent. However, there is typically no guarantee that a program’s implementation and natural language documentation are aligned. In the case of a conflict, leveraging information in code-adjacent natural language has the potential to enhance fault localization, debugging, and code trustworthiness. In practice, however, this informatio...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md), [empirical study](empirical_study.md)


- [CellularLint: A Systematic Approach to Identify Inconsistent Behavior in Cellular Network Specifications](../venues/USENIXSec2024/paper_7.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: In recent years, there has been a growing focus on scrutinizing the security of cellular networks, often attributing security vulnerabilities to issues in the underlying protocol design descriptions. These protocol design specifications, typically extensive documents that are thousands of pages long, can harbor inaccuracies, underspecifications, implicit assumptions, and internal inconsistencies. In light of the evolving landscape, we introduce CellularLint—a semi-automatic framework for inconsi...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [DAInfer: Inferring API Aliasing Specifications from Library Documentation via Neurosymbolic Optimization](../venues/FSE2024/paper_28.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Modern software systems heavily rely on various libraries, necessitating understanding API semantics in static analysis. However, summarizing API semantics remains challenging due to complex implementations or the unavailability of library code. This paper presents DAInfer, a novel approach for inferring API aliasing specifications from library documentation. Specifically, we employ Natural Language Processing (NLP) models to interpret informal semantic information provided by the documentation,...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [DiffSpec: Differential Testing with LLMs using Natural Language Specifications and Code Artifacts](../venues/arXiv2024/paper_23.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Differential testing can be an effective way to find bugs in software systems with multiple implementations that conform to the same specification, like compilers, network protocol parsers, and language runtimes. Specifications for such systems are often standardized in natural language documents, like Instruction Set Architecture (ISA) specifications, Wasm specifications or IETF RFC's. Large Language Models (LLMs) have demonstrated potential in both generating tests and handling large volumes o...
  - **Labels**: [program testing](program_testing.md), [differential testing](differential_testing.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [EAGLEYE: Exposing Hidden Web Interfaces in IoT Devices via Routing Analysis](../venues/NDSS2025/paper_5.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: Hidden web interfaces, i.e., undisclosed access channels in IoT devices, introduce great security risks and have resulted in severe attacks in recent years. However, the definition of such threats is vague, and few solutions are able to discover them. Due to their hidden nature, traditional bug detection solutions (e.g., taint analysis, fuzzing) are hard to detect them. In this paper, we present a novel solution EAGLEYE to automatically expose hidden web interfaces in IoT devices. By analyzing i...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [Enchanting program specification synthesis by large language models using static analysis and program verification](../venues/CAV2024/paper_1.md), ([CAV2024](../venues/CAV2024/README.md))

  - **Abstract**: Formal verification provides a rigorous and systematic approach to ensure the correctness and reliability of software systems. Yet, constructing specifications for the full proof relies on domain expertise and non-trivial manpower. In view of such needs, an automated approach for specification synthesis is desired. While existing automated approaches are limited in their versatility, i.e., they either focus only on synthesizing loop invariants for numerical programs, or are tailored for specific...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md), [specification inference](specification_inference.md)


- [Enhancing Security in Third-Party Library Reuse – Comprehensive Detection of 1-day Vulnerability through Code Patch Analysis](../venues/NDSS2025/paper_6.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: Nowadays, software development progressesrapidly to incorporate new features. To facilitate such growthand provide convenience for developers when creating andupdating software, reusing open-source software (i.e., thirdpartylibrary reuses) has become one of the most effectiveand efficient methods. Unfortunately, the practice of reusingthird-party libraries (TPLs) can also introduce vulnerabilities(known as 1-day vulnerabilities) because of the low maintenanceof TPLs, resulting in many vulnerable...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [Generating API Parameter Security Rules with LLM for API Misuse Detection](../venues/NDSS2025/paper_1.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: When utilizing library APIs, developers should follow the API security rules to mitigate the risk of API misuse. API Parameter Security Rule (APSR) is a common type of security rule that specifies how API parameters should be safely used and places constraints on their values. Failure to comply with the APSRs can lead to severe security issues, including null pointer dereference and memory corruption. Manually analyzing numerous APIs and their parameters to construct APSRs is labor-intensive and...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [Hermes: Unlocking Security Analysis of Cellular Network Protocols by Synthesizing Finite State Machines from Natural Language Specifications](../venues/USENIXSec2024/paper_6.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: In this paper, we present Hermes, an end-to-end framework to automatically generate formal representations from natural language cellular specifications. We first develop a neural constituency parser, NEUTREX, to process transition-relevant texts and extract transition components (i.e., states, conditions, and actions). We also design a domain-specific language to translate these transition components to logical formulas by leveraging dependency parse trees. Finally, we compile these logical for...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [Impact of large language models on generating software specifications](../venues/arXiv2023/paper_12.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Software specifications are essential for ensuring the reliability of software systems. Existing specification extraction approaches, however, suffer from limited generalizability and require manual efforts. The recent emergence of Large Language Models (LLMs), which have been successfully applied to numerous software engineering tasks, offers a promising avenue for automating this process. In this paper, we conduct the first empirical study to evaluate the capabilities of LLMs for generating so...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [LLM Assistance for Memory Safety](../venues/ICSE2025/paper_14.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Memory safety violations in low-level code, written in languages like C, continues to remain one of the major sources of software vulnerabilities. One method of removing such violations by construction is to port C code to a safe C dialect. Such dialects rely on programmer-supplied annotations to guarantee safety with minimal runtime overhead. This porting, however, is a manual process that imposes significant burden on the programmer and, hence, there has been limited adoption of this technique...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [Large Language Models for Validating Network Protocol Parsers](../venues/LangSec2025/paper_1.md), ([LangSec2025](../venues/LangSec2025/README.md))

  - **Abstract**: Network protocol parsers are essential for enabling correct and secure communication between devices. Bugs in these parsers can introduce critical vulnerabilities, including memory corruption, information leakage, and denial-of-service attacks. An intuitive way to assess parser correctness is to compare the implementation with its official protocol standard. However, this comparison is challenging because protocol standards are typically written in natural language, whereas implementations are i...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md), [bug detection](bug_detection.md)


- [SpecEval: Evaluating Code Comprehension in Large Language Models via Program Specifications](../venues/arXiv2024/paper_25.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large Language models have achieved impressive performance in automated software engineering. Extensive efforts have been made to evaluate the abilities of code LLMs in various aspects, with an increasing number of benchmarks and evaluation frameworks proposed. Apart from the most sought-after capability of code generation, the capability of code comprehension is being granted growing attention. Nevertheless, existing works assessing the code comprehension capability of LLMs exhibit varied limit...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [SpecGen: Automated Generation of Formal Program Specifications via Large Language Models](../venues/ICSE2025/paper_37.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: In the software development process, formal program specifications play a crucial role in various stages, including requirement analysis, software testing, and verification. However, manually crafting formal program specifications is rather difficult, making the job time-consuming and labor-intensive. Moreover, it is even more challenging to write specifications that correctly and comprehensively describe the semantics of complex programs. To reduce the burden on software developers, automated s...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md), [program verification](program_verification.md)


- [SpecRover: Code Intent Extraction via LLMs](../venues/ICSE2025/paper_2.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Autonomous program improvement typically involves automatically producing bug fixes and feature additions. Such program improvement can be accomplished by a combination of large language model (LLM) and program analysis capabilities, in the form of an LLM agent. Since program repair or program improvement typically requires a specification of intended behavior - specification inference can be useful for producing high quality program patches. In this work, we examine efficient and low-cost workf...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [TAPChecker: Model Checking in Trigger-Action Rules Generation Using Large Language Models](../venues/CCS2024/paper_7.md), ([CCS2024](../venues/CCS2024/README.md))

  - **Abstract**: The integration of large language models (LLMs) in smart home systems holds significant promise for automating the generation of Trigger-Action Programming (TAP) rules, potentially streamlining smart home user experiences and enhancing convenience. However, LLMs lack of holistic view of smart home IoT deployments and may introduce TAP rules that result in hazards. This paper explores the application of LLM for generating TAP rules and applying formal verification to validate and ensure the safet...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [The Midas Touch: Triggering the Capability of LLMs for RM-API Misuse Detection](../venues/NDSS2025/paper_3.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: As the basis of software resource management (RM), strictly following the RM-API constraints guarantees secure resource management and software. To enhance the RM-API application, researchers find it effective in detecting RM-API misuse on open-source software according to RM-API constraints retrieved from documentation and code. However, the current pattern-matching constraint retrieval methods have limitations: the documentation-based methods leave many API constraints irregularly distributed ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [When Threads Meet Interrupts: Effective Static Detection of Interrupt-Based Deadlocks in Linux](../venues/USENIXSec2024/paper_3.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: Deadlocking is an unresponsive state of software that arises when threads hold locks while trying to acquire other locks that are already held by other threads, resulting in a circular lock dependency. Interrupt-based deadlocks, a specific and prevalent type of deadlocks that occur within the OS kernel due to interrupt preemption, pose significant risks to system functionality, performance, and security. However, existing static analysis tools focus on resource-based deadlocks without characteri...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)
