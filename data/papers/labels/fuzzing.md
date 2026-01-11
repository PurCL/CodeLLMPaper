# Fuzzing

- [Clozemaster: Fuzzing Rust Compiler by Harnessing Llms for Infilling Masked Real Programs](../venues/ICSE2025/paper_50.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Ensuring the reliability of the Rust compiler is of paramount importance, given increasing adoption of Rust for critical systems development, due to its emphasis on memory and thread safety. However, generating valid test programs for the Rust compiler poses significant challenges, given Rust's complex syntax and strict requirements. With the growing popularity of large language models (LLMs), much research in software testing has explored using LLMs to generate test cases. Still, directly using...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [CodaMosa: Escaping Coverage Plateaus in Test Generation with Pre-Trained Large Language Models](../venues/ICSE2023/paper_1.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Search-based software testing (SBST) generates high-coverage test cases for programs under test with a combination of test case generation and mutation. SBST's performance relies on there being a reasonable probability of generating test cases that exercise the core logic of the program under test. Given such test cases, SBST can then explore the space around them to exercise various parts of the program. This paper explores whether Large Language Models (LLMs) of code, such as OpenAI's Codex, c...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Code-Aware Prompting: A Study of Coverage-Guided Test Generation in Regression Setting using LLM](../venues/FSE2024/paper_25.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Testing plays a pivotal role in ensuring software quality, yet conventional Search Based Software Testing (SBST) methods often struggle with complex software units, achieving suboptimal test coverage. Recent work using large language models (LLMs) for test generation have focused on improving generation quality through optimizing the test generation context and correcting errors in model outputs, but use fixed prompting strategies that prompt the model to generate tests without additional guidan...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Drowzee: Metamorphic Testing for Fact-Conflicting Hallucination Detection in Large Language Models](../venues/OOPSLA2024/paper_4.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Large language models (LLMs) have revolutionized language processing, but face critical challenges with security, privacy, and generating hallucinations — coherent but factually inaccurate outputs. A major issue is fact-conflicting hallucination (FCH), where LLMs produce content contradicting ground truth facts. Addressing FCH is difficult due to two key challenges: 1) Automatically constructing and updating benchmark datasets is hard, as existing methods rely on manually curated static benchmar...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [From One Thousand Pages of Specification to Unveiling Hidden Bugs:Large Language Model Assisted Fuzzing of Matter IoT Devices](../venues/USENIXSec2024/paper_5.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: Matter is an IoT connectivity standard backed by over two hundred companies. Since the release of its specification in October 2022, numerous IoT devices have become Matter-compatible. Identifying bugs and vulnerabilities in Matter devices is thus an emerging important problem. This paper introduces mGPTFuzz, the first Matter fuzzer in the literature. Our approach harnesses the extensive and detailed information within the Matter specification to guide the generation of test inputs. However, due...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Fuzz4All: Universal Fuzzing with Large Language Models](../venues/ICSE2024/paper_15.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Fuzzing has achieved tremendous success in discovering bugs and vulnerabilities in various software systems. Systems under test (SUTs) that take in programming or formal language as inputs, e.g., compilers, runtime engines, constraint solvers, and software libraries with accessible APIs, are especially important as they are fundamental building blocks of software development. However, existing fuzzers for such systems often target a specific language, and thus cannot be easily applied to other l...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Fuzzing BusyBox: Leveraging LLM and Crash Reuse for Embedded Bug Unearthing](../venues/USENIXSec2024/paper_4.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: BusyBox, an open-source software bundling over 300 essential Linux commands into a single executable, is ubiquitous in Linux-based embedded devices. Vulnerabilities in BusyBox can have far-reaching consequences, affecting a wide array of devices. This research, driven by the extensive use of BusyBox, delved into its analysis. The study revealed the prevalence of older BusyBox versions in real-world embedded products, prompting us to conduct fuzz testing on BusyBox. Fuzzing, a pivotal software te...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Fuzzing JavaScript Interpreters with Coverage-Guided Reinforcement Learning for LLM-Based Mutation](../venues/ISSTA2024/paper_22.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: JavaScript interpreters, crucial for modern web browsers, require an effective fuzzing method to identify security-related bugs. However, the strict grammatical requirements for input present significant challenges. Recent efforts to integrate language models for context- aware mutation in fuzzing are promising but lack the necessary coverage guidance to be fully effective. This paper presents a novel technique called CovRL (Coverage-guided Reinforcement Learning) that combines Large Language Mo...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [How Effective Are They? Exploring Large Language Model Based Fuzz Driver Generation](../venues/ISSTA2024/paper_14.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Fuzz drivers are essential for library API fuzzing. However, automatically generating fuzz drivers is a complex task, as it demands the creation of high-quality, correct, and robust API usage code. An LLM-based (Large Language Model) approach for generating fuzz drivers is a promising area of research. Unlike traditional program analysis-based generators, this text-based approach is more generalized and capable of harnessing a variety of API usage information, resulting in code that is friendly ...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Interleaving Large Language Models for Compiler Testing](../venues/OOPSLA2025/paper_5.md), ([OOPSLA2025](../venues/OOPSLA2025/README.md))

  - **Abstract**: Testing compilers with AI models, especially large language models (LLMs), has shown great promise. However, current approaches struggle with two key problems: The generated programs for testing compilers are often too simple, and extensive testing with the LLMs is computationally expensive. In this paper, we propose a novel compiler testing framework that decouples the testing process into two distinct phases: an offline phase and an online phase. In the offline phase, we use LLMs to generate a...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [KernelGPT: Enhanced Kernel Fuzzing via Large Language Models](../venues/arXiv2024/paper_39.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Bugs in operating system kernels can affect billions of devices and users all over the world. As a result, a large body of research has been focused on kernel fuzzing, i.e., automatically generating syscall (system call) sequences to detect potential kernel bugs or vulnerabilities. Kernel fuzzing aims to generate valid syscall sequences guided by syscall specifications that define both the syntax and semantics of syscalls. While there has been existing work trying to automate syscall specificati...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [LLM-Based Code Generation Method for Golang Compiler Testing](../venues/FSE2023/paper_7.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Modern optimizing compilers are among the most complex software systems humans build. One way to identify subtle compiler bugs is fuzzing. Both the quantity and the quality of testcases are crucial to the performance of fuzzing. Traditional testcase-generation methods, such as Csmith and YARPGen, have been proven successful at discovering compiler bugs. However, such generated testcases have limited coverage and quantity. In this paper, we present a code generation method for compiler testing ba...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [LLMIF: Augmented Large Language Model for Fuzzing IoT Devices](../venues/S&P2024/paper_2.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Despite the efficacy of fuzzing in verifying the implementation correctness of network protocols, existing IoT protocol fuzzing approaches grapple with several limitations, including obfuscated message formats, unresolved message dependencies, and a lack of evaluations on the testing cases. These limitations significantly curtail the capabilities of IoT fuzzers in vulnerability identification. In this work, we show that the protocol specification contains fruitful descriptions of protocol messag...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Large Language Model assisted Hybrid Fuzzing](../venues/arXiv2024/paper_5.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Greybox fuzzing is one of the most popular methods for detecting software vulnerabilities, which conducts a biased random search within the program input space. To enhance its effectiveness in achieving deep coverage of program behaviors, greybox fuzzing is often combined with concolic execution, which performs a path-sensitive search over the domain of program inputs. In hybrid fuzzing, conventional greybox fuzzing is followed by concolic execution in an iterative loop, where reachability roadb...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Large Language Model guided Protocol Fuzzing](../venues/NDSS2024/paper_2.md), ([NDSS2024](../venues/NDSS2024/README.md))

  - **Abstract**: How to find security flaws in a protocol implementation without a machine-readable specification of the protocol? Facing the internet, protocol implementations are particularly security-critical software systems where inputs must adhere to a specific structure and order that is often informally specified in hundreds of pages in natural language (RFC). Without some machine-readable version of that protocol, it is difficult to automatically generate valid test inputs for its implementation that fo...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [protocol fuzzing](protocol_fuzzing.md)


- [Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models](../venues/ISSTA2023/paper_2.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Deep Learning (DL) systems have received exponential growth in popularity and have become ubiquitous in our everyday life. Such systems are built on top of popular DL libraries, e.g., TensorFlow and PyTorch which provide APIs as building blocks for DL systems. Detecting bugs in these DL libraries is critical for almost all downstream DL systems in ensuring effectiveness/safety for end users. Meanwhile, traditional fuzzing techniques can be hardly effective for such a challenging domain since the...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [library testing](library_testing.md)


- [Large Language Models Based Fuzzing Techniques: A Survey](../venues/arXiv2024/paper_38.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: In the modern era where software plays a pivotal role, software security and vulnerability analysis have become essential for software development. Fuzzing test, as an efficient software testing method, are widely used in various domains. Moreover, the rapid development of Large Language Models (LLMs) has facilitated their application in the field of software testing, demonstrating remarkable performance. Considering existing fuzzing test techniques are not entirely automated and software vulner...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [survey](survey.md)


- [Large Language Models are Edge-Case Generators: Crafting Unusual Programs for Fuzzing Deep Learning Libraries](../venues/ICSE2024/paper_5.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Bugs in Deep Learning (DL) libraries may affect almost all downstream DL applications, and it is crucial to ensure the quality of such systems. It is challenging to generate valid input programs for fuzzing DL libraries, since the input programs need to satisfy both the syntax/semantics of the supported languages (e.g., Python) and the tensor/operator constraints for constructing valid computational graphs. Recently, the TitanFuzz work demonstrates that modern Large Language Models (LLMs) can be...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Llm4fuzz: Guided fuzzing of smart contracts with large language models](../venues/arXiv2024/paper_28.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: As blockchain platforms grow exponentially, millions of lines of smart contract code are being deployed to manage extensive digital assets. However, vulnerabilities in this mission-critical code have led to significant exploitations and asset losses. Thorough automated security analysis of smart contracts is thus imperative. This paper introduces LLM4Fuzz to optimize automated smart contract security analysis by leveraging large language models (LLMs) to intelligently guide and prioritize fuzzin...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Prompt Fuzzing for Fuzz Driver Generation](../venues/CCS2023/paper_2.md), ([CCS2023](../venues/CCS2023/README.md))

  - **Abstract**: Writing high-quality fuzz drivers is time-consuming and requires a deep understanding of the library. However, the performance of the state-of-the-art automatic fuzz driver generation techniques leaves a lot to be desired. Fuzz drivers, which are learned from consumer code, can reach deep states but are restricted to their external inputs. On the other hand, interpretative fuzzing can explore most APIs but requires numerous attempts in a vast search space. We propose PromptFuzz, a coverage-guide...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [ProphetFuzz: Fully Automated Prediction and Fuzzing of High-Risk Option Combinations with Only Documentation via Large Language Model](../venues/CCS2024/paper_2.md), ([CCS2024](../venues/CCS2024/README.md))

  - **Abstract**: Vulnerabilities related to option combinations pose a significant challenge in software security testing due to their vast search space. Previous research primarily addressed this challenge through mutation or filtering techniques, which inefficiently treated all option combinations as having equal potential for vulnerabilities, thus wasting considerable time on non-vulnerable targets and resulting in low testing efficiency. In this paper, we utilize carefully designed prompt engineering to driv...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Rug: Turbo Llm for Rust Unit Test Generation](../venues/ICSE2025/paper_30.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Unit testing improves software quality by evaluating isolated sections of the program. This approach alleviates the need for comprehensive program-wide testing and confines the potential error scope within the software. However, unit test development is time-consuming, requiring developers to create appropriate test contexts and determine input values to cover different code regions. This problem is particularly pronounced in Rust due to its intricate type system, making traditional unit test ge...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [fuzzing](fuzzing.md)


- [SMT Solver Validation Empowered by Large Pre-Trained Language Models](../venues/ASE2023/paper_3.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: SMT solvers are utilized to check the satisfiability of logic formulas and have been applied in various crucial domains, including software verification, test case generation, and program synthesis. However, bugs hidden in SMT solvers can lead to severe consequences, causing erroneous results in these domains. Therefore, ensuring the reliability and robustness of SMT solvers is of critical importance. Despite several testing approaches proposed for SMT solvers, generating effective test formulas...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Sedar: Obtaining High-Quality Seeds for DBMS Fuzzing via Cross-DBMS SQL Transfer](../venues/ICSE2024/paper_16.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Effective DBMS fuzzing relies on high-quality initial seeds, which serve as the starting point for mutation. These initial seeds should incorporate various DBMS features to explore the state space thoroughly. While built-in test cases are typically used as initial seeds, many DBMSs lack comprehensive test cases, making it difficult to apply state-of-the-art fuzzing techniques directly.To address this, we propose Sedar which produces initial seeds for a target DBMS by transferring test cases from...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [DBMS testing](DBMS_testing.md)


- [The Mutators Reloaded: Fuzzing Compilers with Large Language Model Generated Mutation Operators](../venues/ASPLOS2024/paper_1.md), ([ASPLOS2024](../venues/ASPLOS2024/README.md))

  - **Abstract**: Crafting high-quality mutators–the core of mutation-based fuzzing that shapes the search space–is challenging. It requires human expertise and creativity, and their implementation demands knowledge of compiler internals. This paper presents MetaMut framework for developing new, useful mutators for compiler fuzzing. It integrates our compilerdomain knowledge into prompts and processes that can best harness the capabilities of a large language model. With MetaMut, we have successfully created 118 ...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [The Seeds of the Future Sprout from History: Fuzzing for Unveiling Vulnerabilities in Prospective Deep-Learning Libraries](../venues/ICSE2025/paper_39.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: The widespread application of large language models (LLMs) underscores the importance of deep learning (DL) technologies that rely on foundational DL libraries such as PyTorch and TensorFlow. Despite their robust features, these libraries face challenges with scalability and adaptation to rapid advancements in the LLM community. In response, tech giants like Apple and Huawei are developing their own DL libraries to enhance performance, increase scalability, and safeguard intellectual property. E...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [vulnerability exploitation](vulnerability_exploitation.md)


- [Towards Translating Real-World Code with LLMs: A Study of Translating to Rust](../venues/arXiv2024/paper_36.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large language models (LLMs) show promise in code translation - the task of translating code written in one programming language to another language - due to their ability to write code in most programming languages. However, LLM's effectiveness on translating real-world code remains largely unstudied. In this work, we perform the first substantial study on LLM-based translation to Rust by assessing the ability of five state-of-the-art LLMs, GPT4, Claude 3, Claude 2.1, Gemini Pro, and Mixtral. W...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Unlocking Low Frequency Syscalls in Kernel Fuzzing with Dependency-Based RAG](../venues/ISSTA2025/paper_12.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Most coverage-guided kernel fuzzers test operating system kernels based on syscall sequence synthesis. However, there are still syscalls rarely or not covered (called low frequency syscalls, LFS) in a period of fuzzing, meaning the relevant code branches remain unexplored. This is due to the complex dependencies of the LFS and mutation uncertainty, which makes it difficult for fuzzers to generate corresponding syscall sequences. Since many kernel fuzzers can dynamically learn syscall dependencie...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [When fuzzing meets llms: Challenges and opportunities](../venues/FSE2024/paper_27.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Fuzzing, a widely-used technique for bug detection, has seen advancements through Large Language Models (LLMs). Despite their potential, LLMs face specific challenges in fuzzing. In this paper, we identified five major challenges of LLM-assisted fuzzing. To support our findings, we revisited the most recent papers from top-tier conferences, confirming that these challenges are widespread. As a remedy, we propose some actionable recommendations to help improve applying LLM in Fuzzing and conduct ...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [survey](survey.md)


- [WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models](../venues/OOPSLA2024/paper_3.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Compiler correctness is crucial, as miscompilation can falsify program behaviors, leading to serious consequences over the software supply chain. In the literature, fuzzing has been extensively studied to uncover compiler defects. However, compiler fuzzing remains challenging: Existing arts focus on black- and grey-box fuzzing, which generates test programs without sufficient understanding of internal compiler behaviors. As such, they often fail to construct test programs to exercise intricate o...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [Your Fix Is My Exploit: Enabling Comprehensive DL Library API Fuzzing with Large Language Models](../venues/ICSE2025/paper_20.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Deep learning (DL) libraries are widely used to form the basis of various AI applications in computer vision, natural language processing, and software engineering domains. Despite their popularity, DL libraries are known to have vulnerabilities, such as buffer overflows, use-after-free, and integer overflows, that can be exploited to compromise the security or effectiveness of the underlying libraries. While traditional fuzzing techniques have been used to find bugs in software, they are not we...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)
