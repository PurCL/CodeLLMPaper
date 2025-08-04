# Program Testing

## General Testing

- [Blended Analysis for Predictive Execution](../venues/FSE2025/paper_40.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Although Large Language Models (LLMs) are highly proficient in understanding source code and descriptive texts, they have limitations in reasoning on dynamic program behaviors, such as execution trace and code coverage prediction, and runtime error prediction, which usually require actual program execution. To advance the ability of LLMs in predicting dynamic behaviors, we leverage the strengths of both approaches, Program Analysis (PA) and LLM, in building PredEx, a predictive executor for Pyth...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md)


- [CRISPE: Semantic-Guided Execution Planning and Dynamic Reasoning for Enhancing Code Coverage Prediction](../venues/FSE2025/paper_39.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: While LLMs excel in understanding source code and descriptive texts for tasks like code generation, code completion, etc., they exhibit weaknesses in predicting dynamic program behavior, such as code coverage and runtime error detection, which typically require program execution. Aiming to advance the capability of LLMs in reasoning and predicting the program behavior at runtime, we present CRISPE (short for Coverage Rationalization and Intelligent Selection ProcedurE), a novel approach for code...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md)


- [CoverUp: Effective High Coverage Test Generation for Python](../venues/FSE2025/paper_36.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Testing is an essential part of software development. Test generation tools attempt to automate the otherwise labor-intensive task of test creation, but generating high-coverage tests remains challenging. This paper proposes CoverUp, a novel approach to driving the generation of high-coverage Python regression tests. CoverUp combines coverage analysis, code context, and feedback in prompts that iteratively guide the LLM to generate tests that improve line and branch coverage.   We evaluate our p...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md)


- [Doc2OracLL: Investigating the Impact of Documentation on LLM-Based Test Oracle Generation](../venues/FSE2025/paper_23.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Code documentation is a critical artifact of software development, bridging human understanding and machine-   readable code. Beyond aiding developers in code comprehension and maintenance, documentation also plays   a critical role in automating various software engineering tasks, such as test oracle generation (TOG). In Java,   Javadoc comments offer structured, natural language documentation embedded directly within the source   code, typically describing functionality, usage, parameters, ret...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md), [empirical study](empirical_study.md)


- [Tratto: A Neuro-Symbolic Approach to Deriving Axiomatic Test Oracles](../venues/ISSTA2025/paper_28.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: This paper presents Tratto, a neuro-symbolic approach that generates assertions (boolean expressions) that can serve as axiomatic oracles, from source code and documentation. The symbolic module of Tratto takes advantage of the grammar of the programming language, the unit under test, and the context of the unit (its class and available APIs) to restrict the search space of the tokens that can be successfully used to generate valid oracles. The neural module of Tratto uses transformers fine-tune...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md)


- [You Name It, I Run It: An LLM Agent to Execute Tests of Arbitrary Projects](../venues/ISSTA2025/paper_1.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: The ability to execute the test suite of a project is essential in many scenarios, e.g., to assess code quality and code coverage, to validate code changes made by developers or automated tools, and to ensure compatibility with dependencies. Despite its importance, executing the test suite of a project can be challenging in practice because different projects use different programming languages, software ecosystems, build systems, testing frameworks, and other tools. These challenges make it dif...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md), [agent design](agent_design.md)


- [exLong: Generating Exceptional Behavior Tests with Large Language Models](../venues/ICSE2025/paper_51.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Many popular programming languages, including C#, Java, and Python, support exceptions. Exceptions are thrown during program execution if an unwanted event happens, e.g., a method is invoked with an illegal argument value. Software developers write exceptional behavior tests (EBTs) to check that their code detects unwanted events and throws appropriate exceptions. Prior research studies have shown the importance of EBTs, but those studies also highlighted that developers put most of their effort...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md)


## Fuzzing

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


- [Rug: Turbo Llm for Rust Unit Test Generation](../venues/ICSE2025/paper_31.md), ([ICSE2025](../venues/ICSE2025/README.md))

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


- [Your Fix Is My Exploit: Enabling Comprehensive DL Library API Fuzzing with Large Language Models](../venues/ICSE2025/paper_21.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Deep learning (DL) libraries are widely used to form the basis of various AI applications in computer vision, natural language processing, and software engineering domains. Despite their popularity, DL libraries are known to have vulnerabilities, such as buffer overflows, use-after-free, and integer overflows, that can be exploited to compromise the security or effectiveness of the underlying libraries. While traditional fuzzing techniques have been used to find bugs in software, they are not we...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


## Library Testing

- [A Multi-Agent Approach for REST API Testing with Semantic Graphs and LLM-Driven Inputs](../venues/ICSE2025/paper_52.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: As modern web services increasingly rely on REST APIs, their thorough testing has become crucial. Furthermore, the advent of REST API documentation languages, such as the OpenAPI Specification, has led to the emergence of many black-box REST API testing tools. However, these tools often focus on individual test elements in isolation (e.g., APIs, parameters, values), resulting in lower coverage and less effectiveness in fault detection. To address these limitations, we present AutoRestTest, the f...
  - **Labels**: [program testing](program_testing.md), [library testing](library_testing.md)


- [CrossProbe: LLM-Empowered Cross-Project Bug Detection for Deep Learning Frameworks](../venues/ISSTA2025/paper_33.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Deep Learning (DL) models may introduce reliability challenges in the underlying DL frameworks. These frameworks may be prone to bugs that can lead to crash or wrong results, particularly when involving complex model architectures and substantial computational demands. Such framework bugs can disrupt DL applications, impacting customer experience and potentially causing financial losses. Traditional approaches to testing DL frameworks face limitations in adapting to the vast search space of mode...
  - **Labels**: [program testing](program_testing.md), [library testing](library_testing.md)


- [LLM Based Input Space Partitioning Testing for Library APIs](../venues/ICSE2025/paper_45.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Automated library APIs testing is difficult as it requires exploring a vast space of parameter inputs that may involve objects with complex data types. Existing search based approaches, with limited knowledge of relations between object states and program branches, often suffer from the low efficiency issue, i.e., tending to generate invalid inputs. Symbolic execution based approaches can effectively identify such relations, but fail to scale to large programs. In this work, we present an LLM-ba...
  - **Labels**: [program testing](program_testing.md), [library testing](library_testing.md)


- [Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models](../venues/ISSTA2023/paper_2.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Deep Learning (DL) systems have received exponential growth in popularity and have become ubiquitous in our everyday life. Such systems are built on top of popular DL libraries, e.g., TensorFlow and PyTorch which provide APIs as building blocks for DL systems. Detecting bugs in these DL libraries is critical for almost all downstream DL systems in ensuring effectiveness/safety for end users. Meanwhile, traditional fuzzing techniques can be hardly effective for such a challenging domain since the...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [library testing](library_testing.md)


- [LlamaRestTest: Effective REST API Testing with Small Language Models](../venues/FSE2025/paper_7.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Modern web services rely heavily on REST APIs, typically documented using the OpenAPI specification. The widespread adoption of this standard has resulted in the development of many black-box testing tools that generate tests based on OpenAPI specifications. Although Large Language Models (LLMs) have shown promising test-generation abilities, their application to REST API testing remains mostly unexplored. We present LlamaRestTest, a novel approach that employs two custom LLMs-created by fine-tu...
  - **Labels**: [program testing](program_testing.md), [library testing](library_testing.md)


## DBMS Testing

- [Sedar: Obtaining High-Quality Seeds for DBMS Fuzzing via Cross-DBMS SQL Transfer](../venues/ICSE2024/paper_16.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Effective DBMS fuzzing relies on high-quality initial seeds, which serve as the starting point for mutation. These initial seeds should incorporate various DBMS features to explore the state space thoroughly. While built-in test cases are typically used as initial seeds, many DBMSs lack comprehensive test cases, making it difficult to apply state-of-the-art fuzzing techniques directly.To address this, we propose Sedar which produces initial seeds for a target DBMS by transferring test cases from...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [DBMS testing](DBMS_testing.md)


## Compiler Testing

- [Clozemaster: Fuzzing Rust Compiler by Harnessing Llms for Infilling Masked Real Programs](../venues/ICSE2025/paper_50.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Ensuring the reliability of the Rust compiler is of paramount importance, given increasing adoption of Rust for critical systems development, due to its emphasis on memory and thread safety. However, generating valid test programs for the Rust compiler poses significant challenges, given Rust's complex syntax and strict requirements. With the growing popularity of large language models (LLMs), much research in software testing has explored using LLMs to generate test cases. Still, directly using...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [Fuzzing JavaScript Interpreters with Coverage-Guided Reinforcement Learning for LLM-Based Mutation](../venues/ISSTA2024/paper_22.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: JavaScript interpreters, crucial for modern web browsers, require an effective fuzzing method to identify security-related bugs. However, the strict grammatical requirements for input present significant challenges. Recent efforts to integrate language models for context- aware mutation in fuzzing are promising but lack the necessary coverage guidance to be fully effective. This paper presents a novel technique called CovRL (Coverage-guided Reinforcement Learning) that combines Large Language Mo...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [LLM-Based Code Generation Method for Golang Compiler Testing](../venues/FSE2023/paper_7.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Modern optimizing compilers are among the most complex software systems humans build. One way to identify subtle compiler bugs is fuzzing. Both the quantity and the quality of testcases are crucial to the performance of fuzzing. Traditional testcase-generation methods, such as Csmith and YARPGen, have been proven successful at discovering compiler bugs. However, such generated testcases have limited coverage and quantity. In this paper, we present a code generation method for compiler testing ba...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [The Mutators Reloaded: Fuzzing Compilers with Large Language Model Generated Mutation Operators](../venues/ASPLOS2024/paper_1.md), ([ASPLOS2024](../venues/ASPLOS2024/README.md))

  - **Abstract**: Crafting high-quality mutators–the core of mutation-based fuzzing that shapes the search space–is challenging. It requires human expertise and creativity, and their implementation demands knowledge of compiler internals. This paper presents MetaMut framework for developing new, useful mutators for compiler fuzzing. It integrates our compilerdomain knowledge into prompts and processes that can best harness the capabilities of a large language model. With MetaMut, we have successfully created 118 ...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models](../venues/OOPSLA2024/paper_3.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Compiler correctness is crucial, as miscompilation can falsify program behaviors, leading to serious consequences over the software supply chain. In the literature, fuzzing has been extensively studied to uncover compiler defects. However, compiler fuzzing remains challenging: Existing arts focus on black- and grey-box fuzzing, which generates test programs without sufficient understanding of internal compiler behaviors. As such, they often fail to construct test programs to exercise intricate o...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


## Gui Testing

- [LLMDroid: Enhancing Automated Mobile App GUI Testing Coverage with Large Language Model Guidance](../venues/FSE2025/paper_14.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: With the rapid development of Large Language Models (LLMs), their integration into automated mobile GUI testing has emerged as a promising research direction. However, existing LLM-based testing approaches face significant challenges, including time inefficiency and high costs due to constant LLM querying. To address these issues, this paper introduces LLMDroid, a novel testing framework designed to enhance existing automated mobile GUI testing tools by leveraging LLMs more efficiently. The work...
  - **Labels**: [program testing](program_testing.md), [GUI testing](GUI_testing.md)


## Protocol Fuzzing

- [Large Language Model guided Protocol Fuzzing](../venues/NDSS2024/paper_2.md), ([NDSS2024](../venues/NDSS2024/README.md))

  - **Abstract**: How to find security flaws in a protocol implementation without a machine-readable specification of the protocol? Facing the internet, protocol implementations are particularly security-critical software systems where inputs must adhere to a specific structure and order that is often informally specified in hundreds of pages in natural language (RFC). Without some machine-readable version of that protocol, it is difficult to automatically generate valid test inputs for its implementation that fo...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [protocol fuzzing](protocol_fuzzing.md)


## Mutation Testing

- [LLMorpheus: Mutation Testing using Large Language Models](../venues/arXiv2024/paper_29.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: In mutation testing, the quality of a test suite is evaluated by introducing faults into a program and determining whether the program's tests detect them. Most existing approaches for mutation testing involve the application of a fixed set of mutation operators, e.g., replacing a "+" with a "-" or removing a function's body. However, certain types of real-world bugs cannot easily be simulated by such approaches, limiting their effectiveness. This paper presents a technique where a Large Languag...
  - **Labels**: [program testing](program_testing.md), [mutation testing](mutation_testing.md)


- [Large Language Models for Equivalent Mutant Detection: How Far Are We?](../venues/ISSTA2024/paper_23.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Mutation testing is vital for ensuring software quality. However, the presence of equivalent mutants is known to introduce redundant cost and bias issues, hindering the effectiveness of mutation testing in practical use. Although numerous equivalent mutant detection (EMD) techniques have been proposed, they exhibit limitations due to the scarcity of training data and challenges in generalizing to unseen mutants. Recently, large language models (LLMs) have been extensively adopted in various code...
  - **Labels**: [program testing](program_testing.md), [mutation testing](mutation_testing.md), [empirical study](empirical_study.md)


## Unit Testing

- [A Large-Scale Empirical Study on Fine-Tuning Large Language Models for Unit Testing](../venues/ISSTA2025/paper_26.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Unit testing plays a pivotal role in software development, improving software quality and reliability. However, generating effective test cases manually is time-consuming, prompting interest in unit testing research.   Recently, Large Language Models (LLMs) have shown potential in various unit testing tasks, including test generation, assertion generation, and test evolution, but existing studies are limited in scope and lack a systematic evaluation of the effectiveness of LLMs.    To bridge thi...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md)


- [An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation](../venues/TSE2024/paper_10.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Unit tests play a key role in ensuring the correctness of software. However, manually creating unit tests is a laborious task, motivating the need for automation. Large Language Models (LLMs) have recently been applied to various aspects of software development, including their suggested use for automated generation of unit tests, but while requiring additional training or few-shot learning on examples of existing tests. This paper presents a large-scale empirical evaluation on the effectiveness...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md)


- [Automated Unit Test Refactoring](../venues/FSE2025/paper_10.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Test smells arise from poor design practices and insufficient domain knowledge, which can lower the quality of test code and make it harder to maintain and update. Manually refactoring of test smells is time-consuming and error-prone, highlighting the necessity for automated approaches. Current rule-based refactoring methods often struggle in scenarios not covered by predefined rules and lack the flexibility needed to handle diverse cases effectively. In this paper, we propose a novel approach c...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [code generation](code_generation.md), [program transformation](program_transformation.md)


- [ChatGPT vs SBST: A Comparative Assessment of Unit Test Suite Generation](../venues/TSE2024/paper_5.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Recent advancements in large language models (LLMs) have demonstrated exceptional success in a wide range of general domain tasks, such as question answering and following instructions. Moreover, LLMs have shown potential in various software engineering applications. In this study, we present a systematic comparison of test suites generated by the ChatGPT LLM and the state-of-the-art SBST tool EvoSuite. Our comparison is based on several critical factors, including correctness, readability, code...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md)


- [Domain Adaptation for Code Model-Based Unit Test Case Generation](../venues/ISSTA2024/paper_28.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Recently, deep learning-based test case generation approaches have been proposed to automate the generation of unit test cases. In this study, we leverage Transformer-based code models to generate               unit tests with the help of Domain Adaptation (DA) at a project level. Specifically, we use CodeT5, a relatively small language model trained on source code data, and fine-tune it on the test generation               task. Then, we apply domain adaptation to each target project data to le...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md)


- [Evaluating and Improving ChatGPT for Unit Test Generation](../venues/FSE2024/paper_7.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Unit testing plays an essential role in detecting bugs in functionally-discrete program units (e.g., methods). Manually writing high-quality unit tests is time-consuming and laborious. Although the traditional techniques are able to generate tests with reasonable coverage, they are shown to exhibit low readability and still cannot be directly adopted by developers in practice. Recent work has shown the large potential of large language models (LLMs) in unit test generation. By being pre-trained ...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md), [code generation](code_generation.md)


- [Less Is More: On the Importance of Data Quality for Unit Test Generation](../venues/FSE2025/paper_18.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Unit testing is crucial for software development and maintenance. Effective unit testing ensures and improves software quality, but writing unit tests is time-consuming and labor-intensive. Recent studies have proposed deep learning (DL) techniques or large language models (LLMs) to automate unit test generation. These models are usually trained or fine-tuned on large-scale datasets. Despite growing awareness of the importance of data quality, there has been limited research on the quality of da...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md)


- [On the Evaluation of Large Language Models in Unit Test Generation](../venues/ASE2024/paper_26.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Unit testing is an essential activity in software development for verifying the correctness of software components. However, manually writing unit tests is challenging and time-consuming. The emergence of Large Language Models (LLMs) offers a new direction for automating unit test generation. Existing research primarily focuses on closed-source LLMs (e.g., ChatGPT and CodeX) with fixed prompting strategies, leaving the capabilities of advanced open-source LLMs with various prompting settings une...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md)


- [Rug: Turbo Llm for Rust Unit Test Generation](../venues/ICSE2025/paper_31.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Unit testing improves software quality by evaluating isolated sections of the program. This approach alleviates the need for comprehensive program-wide testing and confines the potential error scope within the software. However, unit test development is time-consuming, requiring developers to create appropriate test contexts and determine input values to cover different code regions. This problem is particularly pronounced in Rust due to its intricate type system, making traditional unit test ge...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [fuzzing](fuzzing.md)


- [STRUT: Structured Seed Case Guided Unit Test Generation for C Programs using LLMs](../venues/ISSTA2025/paper_31.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Unit testing plays a crucial role in bug detection and ensuring software correctness. It helps developers identify errors early in development, thereby reducing software defects. In recent years, large language models (LLMs) have demonstrated significant potential in automating unit test generation. However, using LLMs to generate unit tests faces many challenges. 1) The execution pass rate of the test cases generated by LLMs is low. 2) The test case coverage is inadequate, making it challenging...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md)


- [Towards Understanding the Effectiveness of Large Language Models on Directed Test Input Generation](../venues/ASE2024/paper_42.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Automatic testing has garnered significant attention and success over the past few decades. Techniques such as unit testing and coverage-guided fuzzing have revealed numerous critical software bugs and vulnerabilities. However, a long-standing, formidable challenge for existing techniques is how to achieve higher testing coverage. Constraint-based techniques, such as symbolic execution and concolic testing, have been well-explored and integrated into the existing approaches. With the popularity ...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md)


- [UniTSyn: A Large-Scale Dataset Capable of Enhancing the Prowess of Large Language Models for Program Testing](../venues/ISSTA2024/paper_27.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: The remarkable capability of large language models (LLMs) in generating high-quality code has drawn increasing attention in the software testing community. However, existing code LLMs often demonstrate unsatisfactory capabilities in generating accurate, complete tests since they were trained on code snippets collected without differentiating between code for testing and for other purposes. In this paper, we present a large-scale dataset, UniTSyn, which can enhance LLMs for Unit Test Synthesis. A...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [benchmark](benchmark.md)


## Differential Testing

- [Chatgpt-Based Test Generation for Refactoring Engines Enhanced by Feature Analysis on Examples](../venues/ICSE2025/paper_58.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Software refactoring is widely employed to improve software quality. However, conducting refactorings manually is tedious, time-consuming, and error-prone. Consequently, automated and semi-automated tool support is highly desirable for software refactoring in the industry, and most of the main-stream IDEs provide powerful tool support for refactoring. However, complex refactoring engines are prone to errors, which in turn may result in imperfect and incorrect refactorings. To this end, in this p...
  - **Labels**: [program testing](program_testing.md), [differential testing](differential_testing.md)


- [DiffSpec: Differential Testing with LLMs using Natural Language Specifications and Code Artifacts](../venues/arXiv2024/paper_23.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Differential testing can be an effective way to find bugs in software systems with multiple implementations that conform to the same specification, like compilers, network protocol parsers, and language runtimes. Specifications for such systems are often standardized in natural language documents, like Instruction Set Architecture (ISA) specifications, Wasm specifications or IETF RFC's. Large Language Models (LLMs) have demonstrated potential in both generating tests and handling large volumes o...
  - **Labels**: [program testing](program_testing.md), [differential testing](differential_testing.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [LWDIFF: an LLM-Assisted Differential Testing Framework for Webassembly Runtimes](../venues/ICSE2025/paper_65.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: WebAssembly (Wasm) runtimes execute Wasm programs, a popular low-level language for efficiently executing high-level languages in browsers, with broad applications across diverse domains. The correctness of those runtimes is critical for both functionality and security of Wasm execution, motivating testing approaches that target Wasm runtimes specifically. However, existing Wasm testing frameworks fail to generate test cases that effectively test all three phases of runtime, i.e., decoding, vali...
  - **Labels**: [program testing](program_testing.md), [differential testing](differential_testing.md)


- [METAMON: Finding Inconsistencies between Program Documentation and Behavior using Metamorphic LLM Queries](../venues/LLM4Code2025/paper_1.md), ([LLM4Code2025](../venues/LLM4Code2025/README.md))

  - **Abstract**: Code documentation can, if written precisely, help developers better understand the code they accompany. However, unlike code, code documentation cannot be automatically verified via execution, potentially leading to inconsistencies between documentation and the actual behavior. While such inconsistencies can harmful for developer’s understanding of the code, checking and finding them remains a costly task due to the involvement of human engineers. This paper proposes METAMON, which uses an exis...
  - **Labels**: [program testing](program_testing.md), [differential testing](differential_testing.md)


- [Nuances are the Key: Unlocking ChatGPT to Find Failure-Inducing Tests with Differential Prompting](../venues/ASE2023/paper_7.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Automated detection of software failures is an important but challenging software engineering task. It involves finding in a vast search space the failure-inducing test cases that contain an input triggering the software fault and an oracle asserting the incorrect execution. We are motivated to study how far this outstanding challenge can be solved by recent advances in large language models (LLMs) such as ChatGPT. However, our study reveals that ChatGPT has a relatively low success rate (28.8%)...
  - **Labels**: [program testing](program_testing.md), [differential testing](differential_testing.md)


- [OpDiffer: LLM-Assisted Opcode-Level Differential Testing of Ethereum Virtual Machine](../venues/ISSTA2025/paper_23.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: As Ethereum continues to thrive, the Ethereum Virtual Machine (EVM) has become the cornerstone powering tens of millions of active smart contracts. Intuitively, security issues in EVMs could lead to inconsistent behaviors among smart contracts or even denial-of-service of the entire blockchain network. However, to the best of our knowledge, only a limited number of studies focus on the security of EVMs. Moreover, they suffer from 1) insufficient test input diversity and invalid semantics; and 2)...
  - **Labels**: [program testing](program_testing.md), [differential testing](differential_testing.md)


## Debugging

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


- [Reasoning Runtime Behavior of a Program with LLM: How Far are We?](../venues/ICSE2025/paper_10.md), ([ICSE2025](../venues/ICSE2025/README.md))

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


## Bug Reproduction

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


## Vulnerability Exploitation

- [BountyBench: Dollar Impact of AI Agent Attackers and Defenders on Real-World Cybersecurity Systems](../venues/arXiv2025/paper_20.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: AI agents have the potential to significantly alter the cybersecurity landscape. To help us understand this change, we introduce the first framework to capture offensive and defensive cyber-capabilities in evolving real-world systems. Instantiating this framework with BountyBench, we set up 25 systems with complex, real-world codebases. To capture the vulnerability lifecycle, we define three task types: Detect (detecting a new vulnerability), Exploit (exploiting a specific vulnerability), and Pa...
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md), [benchmark](benchmark.md)


- [CVE-Bench: A Benchmark for AI Agents' Ability to Exploit Real-World Web Application Vulnerabilities](../venues/ICML2025/paper_3.md), ([ICML2025](../venues/ICML2025/README.md))

  - **Abstract**: Large language model (LLM) agents are increasingly capable of autonomously conducting cyberattacks, posing significant threats to existing applications. This growing risk highlights the urgent need for a real-world benchmark to evaluate the ability of LLM agents to exploit web application vulnerabilities. However, existing benchmarks fall short as they are limited to abstracted Capture the Flag competitions or lack comprehensive coverage. Building a benchmark for real-world vulnerabilities invol...
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md)


- [Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models](../venues/arXiv2024/paper_31.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Language Model (LM) agents for cybersecurity that are capable of autonomously identifying vulnerabilities and executing exploits have the potential to cause real-world impact. Policymakers, model providers, and other researchers in the AI and cybersecurity communities are interested in quantifying the capabilities of such agents to help mitigate cyberrisk and investigate opportunities for penetration testing. Toward that end, we introduce Cybench, a framework for specifying cybersecurity tasks a...
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md), [benchmark](benchmark.md)


- [CyberGym: Evaluating AI Agents' Cybersecurity Capabilities with Real-World Vulnerabilities at Scale](../venues/arXiv2025/paper_19.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Large language model (LLM) agents are becoming increasingly skilled at handling cybersecurity tasks autonomously. Thoroughly assessing their cybersecurity capabilities is critical and urgent, given the high stakes in this domain. However, existing benchmarks fall short, often failing to capture real-world scenarios or being limited in scope. To address this gap, we introduce CyberGym, a large-scale and high-quality cybersecurity evaluation framework featuring 1,507 real-world vulnerabilities fou...
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md), [benchmark](benchmark.md)


- [Evaluating Offensive Security Capabilities of Large Language Models](../venues/Google2024/paper_2.md), ([Google2024](../venues/Google2024/README.md))

  - **Abstract**: At Project Zero, we constantly seek to expand the scope and effectiveness of our vulnerability research. Though much of our work still relies on traditional methods like manual source code audits and reverse engineering, we're always looking for new approaches....
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md)


- [From Naptime to Big Sleep: Using Large Language Models To Catch Vulnerabilities In Real-World Code](../venues/Google2024/paper_1.md), ([Google2024](../venues/Google2024/README.md))

  - **Abstract**: In our previous post, Project Naptime: Evaluating Offensive Security Capabilities of Large Language Models, we introduced our framework for large-language-model-assisted vulnerability research and demonstrated its potential by improving the state-of-the-art performance on Meta's CyberSecEval2 benchmarks. Since then, Naptime has evolved into Big Sleep, a collaboration between Google Project Zero and Google DeepMind....
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md)


- [Interactive Tools Substantially Assist LM Agents in Finding Security Vulnerabilities](../venues/arXiv2025/paper_18.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Although language model (LM) agents have demonstrated increased performance in multiple domains, including coding and web-browsing, their success in cybersecurity has been limited. We present EnIGMA, an LM agent for autonomously solving Capture The Flag (CTF) challenges. We introduce new tools and interfaces to improve the agent's ability to find and exploit security vulnerabilities, focusing on interactive terminal programs. These novel Interactive Agent Tools enable LM agents, for the first ti...
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md), [benchmark](benchmark.md)


- [Language agents as hackers: Evaluating cybersecurity skills with capture the flag](../venues/NeurIPS2023/paper_1.md), ([NeurIPS2023](../venues/NeurIPS2023/README.md))

  - **Abstract**: Amidst the advent of language models (LMs) and their wide-ranging capabilities, concerns have been raised about their implications with regards to privacy and security. In particular, the emergence of language agents as a promising aid for automating and augmenting digital work poses immediate questions concerning their misuse as malicious cybersecurity actors. With their exceptional compute efficiency and execution speed relative to human counterparts, language agents may be extremely adept at ...
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md), [benchmark](benchmark.md)


- [PoCGen: Generating Proof-of-Concept Exploits for Vulnerabilities in Npm Packages](../venues/arXiv2025/paper_27.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Security vulnerabilities in software packages are a significant concern for developers and users alike. Patching these vulnerabilities in a timely manner is crucial to restoring the integrity and security of software systems. However, previous work has shown that vulnerability reports often lack proof-of-concept (PoC) exploits, which are essential for fixing the vulnerability, testing patches, and avoiding regressions. Creating a PoC exploit is challenging because vulnerability reports are infor...
  - **Labels**: [vulnerability exploitation](vulnerability_exploitation.md)


- [Teams of LLM Agents can Exploit Zero-Day Vulnerabilities](../venues/arXiv2024/paper_30.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: LLM agents have become increasingly sophisticated, especially in the realm of cybersecurity. Researchers have shown that LLM agents can exploit real-world vulnerabilities when given a description of the vulnerability and toy capture-the-flag problems. However, these agents still perform poorly on real-world vulnerabilities that are unknown to the agent ahead of time (zero-day vulnerabilities). In this work, we show that teams of LLM agents can exploit real-world, zero-day vulnerabilities. Prior ...
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md)


- [The Seeds of the Future Sprout from History: Fuzzing for Unveiling Vulnerabilities in Prospective Deep-Learning Libraries](../venues/ICSE2025/paper_39.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: The widespread application of large language models (LLMs) underscores the importance of deep learning (DL) technologies that rely on foundational DL libraries such as PyTorch and TensorFlow. Despite their robust features, these libraries face challenges with scalability and adaptation to rapid advancements in the LLM community. In response, tech giants like Apple and Huawei are developing their own DL libraries to enhance performance, increase scalability, and safeguard intellectual property. E...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [vulnerability exploitation](vulnerability_exploitation.md)


- [Vulnhuntr: Autonomous AI Finds First 0-Day Vulnerabilities in Wild](../venues/ProtectAI2024/paper_1.md), ([ProtectAI2024](../venues/ProtectAI2024/README.md))

  - **Abstract**: Today, we introduce [Vulnhuntr](https://github.com/protectai/vulnhuntr), a Python static code analyzer that leverages the power of large language models (LLMs) to find and explain complex, multistep vulnerabilities. Thanks to the capabilities of models like Claude 3.5, AI has now uncovered more than a dozen remotely exploitable 0-day vulnerabilities targeting open-source projects in the AI ecosystem with over 10,000 GitHub stars in just a few hours of running it. These discoveries include full-b...
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md)


