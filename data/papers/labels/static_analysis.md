# Static Analysis

## Syntactic Analysis

- [Which Syntactic Capabilities Are Statistically Learned by Masked Language Models for Code?](../venues/ICSE2024/paper_20.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: This paper discusses the limitations of evaluating Masked Language Models (MLMs) in code completion tasks. We highlight that relying on accuracy-based measurements may lead to an overestimation of models' capabilities by neglecting the syntax rules of programming languages. To address these issues, we introduce a technique called SyntaxEval in which Syntactic Capabilities are used to enhance the evaluation of MLMs. SyntaxEval automates the process of masking elements in the model input based on ...
  - **Labels**: [static analysis](static_analysis.md), [syntactic analysis](syntactic_analysis.md), [empirical study](empirical_study.md)


## Pointer Analysis

- [Evaluating the effectiveness of deep learning models for foundational program analysis tasks](../venues/OOPSLA2024/paper_9.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: While deep neural networks provide state-of-the-art solutions to a wide range of programming language tasks, their effectiveness in dealing with foundational program analysis tasks remains under explored. In this paper, we present an empirical study that evaluates four prominent models of code (i.e., CuBERT, CodeBERT, GGNN, and Graph Sandwiches) in two such foundational tasks: (1) alias prediction, in which models predict whether two pointers must alias, may alias or must not alias; and (2) equi...
  - **Labels**: [static analysis](static_analysis.md), [pointer analysis](pointer_analysis.md), [equivalence checking](equivalence_checking.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Function Argument Nullability Using an LLM](../venues/Galois2024/paper_1.md), ([Galois2024](../venues/Galois2024/README.md))

  - **Abstract**: We think that Rust is a great language, and maybe you agree! Unfortunately, even if you do, there’s a good chance whatever application you’re working on is written in some older language such as C. To help with this, Galois has been developing c2rust, an automated transpiler (source-to-source translator) from C code into Rust code. c2rust can take almost any C and turn it into C-like Rust code, the first step in creating a new Rust application. And we’re building more features to turn C into saf...
  - **Labels**: [static analysis](static_analysis.md), [pointer analysis](pointer_analysis.md)


- [Unveiling Code Pre-Trained Models: Investigating Syntax and Semantics Capacities](../venues/TOSEM2024/paper_1.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Code models have made significant advancements in code intelligence by encoding knowledge about programming languages. While previous studies have explored the capabilities of these models in learning code syntax, there has been limited investigation on their ability to understand code semantics. Additionally, existing analyses assume that the number of edges between nodes at the abstract syntax tree&nbsp;(AST) is related to syntax distance, and also often require transforming the high-dimension...
  - **Labels**: [static analysis](static_analysis.md), [pointer analysis](pointer_analysis.md), [data-flow analysis](data-flow_analysis.md), [empirical study](empirical_study.md)


## Call Graph Analysis

- [An Empirical Study of Large Language Models for Type and Call Graph Analysis](../venues/arXiv2024/paper_2.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large Language Models (LLMs) are increasingly being explored for their potential in software engineering, particularly in static analysis tasks. In this study, we investigate the potential of current LLMs to enhance call-graph analysis and type inference for Python and JavaScript programs. We empirically evaluated 24 LLMs, including OpenAI's GPT series and open-source models like LLaMA and Mistral, using existing and newly developed benchmarks. Specifically, we enhanced TypeEvalPy, a micro-bench...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md), [call graph analysis](call_graph_analysis.md)


- [LLMs: Understanding Code Syntax and Semantics for Code Analysis](../venues/arXiv2023/paper_1.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Large language models~(LLMs) demonstrate significant potential to revolutionize software engineering (SE) by exhibiting outstanding performance in SE tasks such as code and document generation. However, the high reliability and risk control requirements in software engineering raise concerns about the lack of interpretability of LLMs. To address this concern, we conducted a study to evaluate the capabilities of LLMs and their limitations for code analysis in SE. We break down the abilities neede...
  - **Labels**: [static analysis](static_analysis.md), [data-flow analysis](data-flow_analysis.md), [call graph analysis](call_graph_analysis.md), [data-flow analysis](data-flow_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)


- [Semantic-Enhanced Indirect Call Analysis with Large Language Models](../venues/ASE2024/paper_8.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: In contemporary software development, the widespread use of indirect calls to achieve dynamic features poses challenges in constructing precise control flow graphs (CFGs), which further impacts the performance of downstream static analysis tasks. To tackle this issue, various types of indirect call analyzers have been proposed. However, they do not fully leverage the semantic information of the program, limiting their effectiveness in real-world scenarios.To address these issues, this paper prop...
  - **Labels**: [static analysis](static_analysis.md), [call graph analysis](call_graph_analysis.md)


## Data-flow Analysis

- [A Learning-Based Approach to Static Program Slicing](../venues/OOPSLA2024/paper_7.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Traditional program slicing techniques are crucial for early bug detection and manual/automated debugging of online code snippets. Nevertheless, their inability to handle incomplete code hinders their real-world applicability in such scenarios. To overcome these challenges, we present NS-Slicer, a novel learning-based approach that predicts static program slices for both complete and partial code Our tool leverages a pre-trained language model to exploit its understanding of fine-grained variabl...
  - **Labels**: [static analysis](static_analysis.md), [data-flow analysis](data-flow_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [LLMs: Understanding Code Syntax and Semantics for Code Analysis](../venues/arXiv2023/paper_1.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Large language models~(LLMs) demonstrate significant potential to revolutionize software engineering (SE) by exhibiting outstanding performance in SE tasks such as code and document generation. However, the high reliability and risk control requirements in software engineering raise concerns about the lack of interpretability of LLMs. To address this concern, we conducted a study to evaluate the capabilities of LLMs and their limitations for code analysis in SE. We break down the abilities neede...
  - **Labels**: [static analysis](static_analysis.md), [data-flow analysis](data-flow_analysis.md), [call graph analysis](call_graph_analysis.md), [data-flow analysis](data-flow_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)


- [LLMs: Understanding Code Syntax and Semantics for Code Analysis](../venues/arXiv2023/paper_1.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Large language models~(LLMs) demonstrate significant potential to revolutionize software engineering (SE) by exhibiting outstanding performance in SE tasks such as code and document generation. However, the high reliability and risk control requirements in software engineering raise concerns about the lack of interpretability of LLMs. To address this concern, we conducted a study to evaluate the capabilities of LLMs and their limitations for code analysis in SE. We break down the abilities neede...
  - **Labels**: [static analysis](static_analysis.md), [data-flow analysis](data-flow_analysis.md), [call graph analysis](call_graph_analysis.md), [data-flow analysis](data-flow_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)


- [Program Slicing in the Era of Large Language Models](../venues/arXiv2024/paper_26.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Program slicing is a critical technique in software engineering, enabling developers to isolate relevant portions of code for tasks such as bug detection, code comprehension, and debugging. In this study, we investigate the application of large language models (LLMs) to both static and dynamic program slicing, with a focus on Java programs. We evaluate the performance of four state-of-the-art LLMs- GPT-4o, GPT-3.5 Turbo, Llama-2, and Gemma-7B leveraging advanced prompting techniques, including f...
  - **Labels**: [static analysis](static_analysis.md), [data-flow analysis](data-flow_analysis.md)


- [Programl: A graph-based program representation for data flow analysis and compiler optimizations](../venues/ICML2021/paper_2.md), ([ICML2021](../venues/ICML2021/README.md))

  - **Abstract**: Machine learning (ML) is increasingly seen as a viable approach for building compiler optimization heuristics, but many ML methods cannot replicate even the simplest of the data flow analyses that are critical to making good optimization decisions. We posit that if ML cannot do that, then it is insufficiently able to reason about programs. We formulate data flow analyses as supervised learning tasks and introduce a large open dataset of programs and their corresponding labels from several analys...
  - **Labels**: [static analysis](static_analysis.md), [data-flow analysis](data-flow_analysis.md), [program optimization](program_optimization.md), [code model](code_model.md), [code model training](code_model_training.md), [IR code model](IR_code_model.md)


- [Revealing the Unseen: AI Chain on LLMs for Predicting Implicit Dataflows to Generate Dataflow Graphs in Dynamically Typed Code](../venues/TOSEM2024/paper_3.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Dataflow graphs (DFGs) capture definitions (defs) and uses across program blocks, which is a fundamental program representation for program analysis, testing and maintenance. However, dynamically typed programming languages like Python present implicit dataflow issues that make it challenging to determine def-use flow information at compile time. Static analysis methods like Soot and WALA are inadequate for handling these issues, and manually enumerating comprehensive heuristic rules is impracti...
  - **Labels**: [static analysis](static_analysis.md), [data-flow analysis](data-flow_analysis.md)


- [Sanitizing Large Language Models in Bug Detection with Data-Flow](../venues/EMNLP2024/paper_4.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large language models (LLMs) show potential in code reasoning tasks, facilitating the customization of detecting bugs in software development. However, the hallucination effect can significantly compromise the reliability of bug reports. This work formulates a new schema of bug detection and presents a novel sanitization technique that detects false positives for hallucination mitigation. Our key idea is to enforce LLMs to emit data-flow paths in few-shot chain-of-thought prompting and validate ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [data-flow analysis](data-flow_analysis.md)


- [Unveiling Code Pre-Trained Models: Investigating Syntax and Semantics Capacities](../venues/TOSEM2024/paper_1.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Code models have made significant advancements in code intelligence by encoding knowledge about programming languages. While previous studies have explored the capabilities of these models in learning code syntax, there has been limited investigation on their ability to understand code semantics. Additionally, existing analyses assume that the number of edges between nodes at the abstract syntax tree&nbsp;(AST) is related to syntax distance, and also often require transforming the high-dimension...
  - **Labels**: [static analysis](static_analysis.md), [pointer analysis](pointer_analysis.md), [data-flow analysis](data-flow_analysis.md), [empirical study](empirical_study.md)


## Symbolic Execution

- [Large Language Model powered Symbolic Execution](../venues/arXiv2025/paper_24.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have emerged as a promising alternative to traditional static program analysis methods, such as symbolic execution, offering the ability to reason over code directly without relying on theorem provers or SMT solvers. However, LLMs are also inherently probabilistic by nature, and therefore face significant challenges in relation to the accuracy and scale of the analysis in real-world application. Such issues often necessitate the use of larger LLMs with higher token l...
  - **Labels**: [static analysis](static_analysis.md), [symbolic execution](symbolic_execution.md)


## Abstract Interpretation

- [AbsInt-AI: Language Models for Abstract Interpretation](../venues/ICLR2025/paper_2.md), ([ICLR2025](../venues/ICLR2025/README.md))

  - **Abstract**: Static program analysis is a popular technique in software engineering. Traditional static analysis algorithms treat programs as sets of logical statements with well-defined semantics. These traditional analyzers can provide guarantees of their performance, such as guaranteeing that they will never miss a bug. However, they leave out lots of very rich information such as variable and field names. Language models for code on the other hand, take full advantage of information such as variable name...
  - **Labels**: [static analysis](static_analysis.md), [abstract interpretation](abstract_interpretation.md), [bug detection](bug_detection.md)


- [Can LLMs Formally Reason as Abstract Interpreters for Program Analysis?](../venues/arXiv2025/paper_16.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: LLMs have demonstrated impressive capabilities in code generation and comprehension, but their potential in being able to perform program analysis in a formal, automatic manner remains under-explored. To that end, we systematically investigate whether LLMs can reason about programs using a program analysis framework called abstract interpretation. We prompt LLMs to follow two different strategies, denoted as Compositional and Fixed Point Equation, to formally reason in the style of abstract inte...
  - **Labels**: [static analysis](static_analysis.md), [abstract interpretation](abstract_interpretation.md)


## Type Inference

- [An Empirical Study of Large Language Models for Type and Call Graph Analysis](../venues/arXiv2024/paper_2.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large Language Models (LLMs) are increasingly being explored for their potential in software engineering, particularly in static analysis tasks. In this study, we investigate the potential of current LLMs to enhance call-graph analysis and type inference for Python and JavaScript programs. We empirically evaluated 24 LLMs, including OpenAI's GPT series and open-source models like LLaMA and Mistral, using existing and newly developed benchmarks. Specifically, we enhanced TypeEvalPy, a micro-bench...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md), [call graph analysis](call_graph_analysis.md)


- [CKTyper: Enhancing Type Inference for Java Code Snippets by Leveraging Crowdsourcing Knowledge in Stack Overflow](../venues/FSE2025/paper_5.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Code snippets are widely used in technical forums to demonstrate solutions to programming problems. They can be leveraged by developers to accelerate problem-solving. However, code snippets often lack concrete types of the APIs used in them, which impedes their understanding and resue. To enhance the description of a code snippet, a number of approaches are proposed to infer the types of APIs. Although existing approaches can achieve good performance, their performance is limited by ignoring oth...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md)


- [Generative Type Inference for Python](../venues/ASE2023/paper_12.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Python is a popular dynamic programming language, evidenced by its ranking as the second most commonly used language on GitHub. However, its dynamic type system can lead to potential type errors, leading researchers to explore automatic type inference approaches for Python programs. Existing type inference approaches can be generally grouped into three categories, i.e., rule-based, supervised, and cloze- style approaches. The rule-based type inference approaches can ensure the accuracy of predic...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md)


- [Neurosymbolic Modular Refinement Type Inference](../venues/ICSE2025/paper_29.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Refinement types, a type-based generalization of Floyd-Hoare logics, are an expressive and modular means of statically ensuring a wide variety of correctness, safety, and security properties of software. However, their expressiveness and modularity means that to use them, a developer must laboriously annotate all the functions in their code with potentially complex type specifications that specify the contract for that function. We present LHC, a neurosymbolic agent that uses LLMs to automatical...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md)


- [PyTy: Repairing Static Type Errors in Python](../venues/ICSE2024/paper_12.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Gradual typing enables developers to annotate types of their own choosing, offering a flexible middle ground between no type annotations and a fully statically typed language. As more and more code bases get type-annotated, static type checkers detect an increasingly large number of type errors. Unfortunately, fixing these errors requires manual effort, hampering the adoption of gradual typing in practice. This paper presents PyTy, an automated program repair approach targeted at statically dete...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [type inference](type_inference.md)


- [Risky Dynamic Typing-related Practices in Python: An Empirical Study](../venues/TOSEM2024/paper_6.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Python’s dynamic typing nature provides developers with powerful programming abstractions. However, many type-related bugs are accumulated in code bases of Python due to the misuse of dynamic typing. The goal of this article is to aid in the understanding of developers’ high-risk practices toward dynamic typing and the early detection of type-related bugs. We first formulate the rules of six types of risky dynamic typing-related practices (type smells for short) in Python. We then develop a rule...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [TIGER: A Generating-Then-Ranking Framework for Practical Python Type Inference](../venues/ICSE2025/paper_12.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Python's dynamic typing system offers flexibility and expressiveness but can lead to type-related errors, prompting the need for automated type inference to enhance type hinting. While existing learning-based approaches show promising inference accuracy, they struggle with practical challenges in comprehensively handling various types, including complex parameterized types and (unseen) user-defined types. In this paper, we introduce TIGER, a two-stage generating-then-ranking (GTR) framework, des...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md)


## Specification Inference

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


- [CellularLint: A Systematic Approach to Identify Inconsistent Behavior in Cellular Network Specifications](../venues/USENIXSec2024/paper_6.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

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


- [Hermes: Unlocking Security Analysis of Cellular Network Protocols by Synthesizing Finite State Machines from Natural Language Specifications](../venues/USENIXSec2024/paper_5.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: In this paper, we present Hermes, an end-to-end framework to automatically generate formal representations from natural language cellular specifications. We first develop a neural constituency parser, NEUTREX, to process transition-relevant texts and extract transition components (i.e., states, conditions, and actions). We also design a domain-specific language to translate these transition components to logical formulas by leveraging dependency parse trees. Finally, we compile these logical for...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [Impact of large language models on generating software specifications](../venues/arXiv2023/paper_12.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Software specifications are essential for ensuring the reliability of software systems. Existing specification extraction approaches, however, suffer from limited generalizability and require manual efforts. The recent emergence of Large Language Models (LLMs), which have been successfully applied to numerous software engineering tasks, offers a promising avenue for automating this process. In this paper, we conduct the first empirical study to evaluate the capabilities of LLMs for generating so...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [LLM Assistance for Memory Safety](../venues/ICSE2025/paper_15.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Memory safety violations in low-level code, written in languages like C, continues to remain one of the major sources of software vulnerabilities. One method of removing such violations by construction is to port C code to a safe C dialect. Such dialects rely on programmer-supplied annotations to guarantee safety with minimal runtime overhead. This porting, however, is a manual process that imposes significant burden on the programmer and, hence, there has been limited adoption of this technique...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [Large Language Models for Validating Network Protocol Parsers](../venues/LangSec2025/paper_1.md), ([LangSec2025](../venues/LangSec2025/README.md))

  - **Abstract**: Network protocol parsers are essential for enabling correct and secure communication between devices. Bugs in these parsers can introduce critical vulnerabilities, including memory corruption, information leakage, and denial-of-service attacks. An intuitive way to assess parser correctness is to compare the implementation with its official protocol standard. However, this comparison is challenging because protocol standards are typically written in natural language, whereas implementations are i...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md), [bug detection](bug_detection.md)


- [SpecEval: Evaluating Code Comprehension in Large Language Models via Program Specifications](../venues/arXiv2024/paper_25.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large Language models have achieved impressive performance in automated software engineering. Extensive efforts have been made to evaluate the abilities of code LLMs in various aspects, with an increasing number of benchmarks and evaluation frameworks proposed. Apart from the most sought-after capability of code generation, the capability of code comprehension is being granted growing attention. Nevertheless, existing works assessing the code comprehension capability of LLMs exhibit varied limit...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [SpecGen: Automated Generation of Formal Program Specifications via Large Language Models](../venues/ICSE2025/paper_7.md), ([ICSE2025](../venues/ICSE2025/README.md))

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


## Equivalence Checking

- [Evaluating the effectiveness of deep learning models for foundational program analysis tasks](../venues/OOPSLA2024/paper_9.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: While deep neural networks provide state-of-the-art solutions to a wide range of programming language tasks, their effectiveness in dealing with foundational program analysis tasks remains under explored. In this paper, we present an empirical study that evaluates four prominent models of code (i.e., CuBERT, CodeBERT, GGNN, and Graph Sandwiches) in two such foundational tasks: (1) alias prediction, in which models predict whether two pointers must alias, may alias or must not alias; and (2) equi...
  - **Labels**: [static analysis](static_analysis.md), [pointer analysis](pointer_analysis.md), [equivalence checking](equivalence_checking.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [What can Large Language Models Capture about Code Functional Equivalence?](../venues/NAACL2025/paper_13.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Code-LLMs, LLMs pre-trained on large code corpora, have shown great progress in learning rich representations of the structure and syntax of code, successfully using it to generate or classify code fragments. At the same time, understanding if they are able to do so because they capture code semantics, and how well, is still an open question. In this paper, we tackle this problem by introducing SeqCoBench, a benchmark for systematically assessing how Code-LLMs can capture code functional equival...
  - **Labels**: [static analysis](static_analysis.md), [equivalence checking](equivalence_checking.md), [empirical study](empirical_study.md), [benchmark](benchmark.md)


## Code Similarity Analysis

- [A Multiple Representation Transformer with Optimized Abstract Syntax Tree for Efficient Code Clone Detection](../venues/ICSE2025/paper_23.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Over the past decade, the application of deep learning in code clone detection has produced remarkable results. However, the current approaches have two limitations: (a) code representation approaches with low information utilization, such as vanilla Abstract Syntax Tree (AST), leading to information redundancy which results in performance degradation; (b) low efficiency of clone detection on evaluation, resulting in excessive time costs during practical use. In this paper, we propose a Multiple...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [static analysis](static_analysis.md), [code similarity analysis](code_similarity_analysis.md)


- [BinCola: Diversity-Sensitive Contrastive Learning for Binary Code Similarity Detection](../venues/TSE2024/paper_14.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Binary Code Similarity Detection (BCSD) is a fundamental binary analysis technique in the area of software security. Recently, advanced deep learning algorithms are integrated into BCSD platforms to achieve superior performance on well-known benchmarks. However, real-world large programs embed more complex diversities due to different compilers, various optimization levels, multiple architectures and even obfuscations. Existing BCSD solutions suffer from low accuracy issues in such complicated r...
  - **Labels**: [static analysis](static_analysis.md), [code similarity analysis](code_similarity_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [Cross-lingual Code Clone Detection: When LLMs Fail Short Against Embedding-based Classifier](../venues/ASE2024/paper_41.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Cross-lingual code clone detection has gained attention in software development due to the use of multiple programming languages. Recent advances in machine learning, particularly Large Language Models (LLMs), have motivated a reexamination of this problem.This paper evaluates the performance of four LLMs and eight prompts for detecting cross-lingual code clones, as well as a pretrained embedding model for classifying clone pairs. Both approaches are tested on the XLCoST and CodeNet datasets.Our...
  - **Labels**: [static analysis](static_analysis.md), [code similarity analysis](code_similarity_analysis.md)


- [Improving Binary Code Similarity Transformer Models by Semantics-Driven Instruction Deemphasis](../venues/ISSTA2023/paper_5.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Given a function in the binary executable form, binary code similarity analysis determines a set of similar functions from a large pool of candidate functions. These similar functions are usually compiled from the same source code with different compilation setups. Such analysis has a large number of applications, such as malware detection, code clone detection, and automatic software patching. The state-of-the art methods utilize complex Deep Learning models such as Transformer models. We obser...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md), [static analysis](static_analysis.md), [code similarity analysis](code_similarity_analysis.md)


- [KEENHash: Hashing Programs into Function-Aware Embeddings for Large-Scale Binary Code Similarity Analysis](../venues/ISSTA2025/paper_10.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Binary code similarity analysis (BCSA) is a crucial research area in many fields such as cybersecurity. Specifically, function-level diffing tools are the most widely used in BCSA: they perform function matching one by one for evaluating the similarity between binary programs. However, such methods need a high time complexity, making them unscalable in large-scale scenarios (e.g., 1/n-to-n search). Towards effective and efficient program-level BCSA, we propose KEENHash, a novel hashing approach ...
  - **Labels**: [static analysis](static_analysis.md), [code similarity analysis](code_similarity_analysis.md)


- [Nova: Generative Language Models for Assembly Code with Hierarchical Attention and Contrastive Learning](../venues/arXiv2023/paper_3.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Binary code analysis is the foundation of crucial tasks in the security domain; thus building effective binary analysis techniques is more important than ever. Large language models (LLMs) although have brought impressive improvement to source code tasks, do not directly generalize to assembly code due to the unique challenges of assembly: (1) the low information density of assembly and (2) the diverse optimizations in assembly code. To overcome these challenges, this work proposes a hierarchica...
  - **Labels**: [static analysis](static_analysis.md), [program decompilation](program_decompilation.md), [static analysis](static_analysis.md), [code similarity analysis](code_similarity_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [RCFG2Vec: Considering Long-Distance Dependency for Binary Code Similarity Detection](../venues/ASE2024/paper_43.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Binary code similarity detection(BCSD), as a fundamental technique in software security, has various applications, including malware family detection, known vulnerability detection and code plagiarism detection. Recent deep learning-based BCSD approaches have demonstrated promising performance. However, they face two significant challenges that limit detection performance. First, most approaches that use sequence networks (like RNN and Transformer) utilize coarse-grained tokenization methods, wh...
  - **Labels**: [static analysis](static_analysis.md), [code similarity analysis](code_similarity_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [The Struggles of LLMs in Cross-Lingual Code Clone Detection](../venues/FSE2025/paper_15.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: With the involvement of multiple programming languages in modern software development, cross-lingual code clone detection has gained traction within the software engineering community. Numerous studies have explored this topic, proposing various promising approaches. Inspired by the significant advances in machine learning in recent years, particularly Large Language Models (LLMs), which have demonstrated their ability to tackle various tasks, this paper revisits cross-lingual code clone detecti...
  - **Labels**: [empirical study](empirical_study.md), [static analysis](static_analysis.md), [code similarity analysis](code_similarity_analysis.md)


## Bug Detection

- [A Comprehensive Study of the Capabilities of Large Language Models for Vulnerability Detection](../venues/arXiv2024/paper_16.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated great potential for code generation and other software engineering tasks. Vulnerability detection is of crucial importance to maintaining the security, integrity, and trustworthiness of software systems. Precise vulnerability detection requires reasoning about the code, making it a good case study for exploring the limits of LLMs' reasoning capabilities. Although recent work has applied LLMs to vulnerability detection using generic prompting techniq...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [AbsInt-AI: Language Models for Abstract Interpretation](../venues/ICLR2025/paper_2.md), ([ICLR2025](../venues/ICLR2025/README.md))

  - **Abstract**: Static program analysis is a popular technique in software engineering. Traditional static analysis algorithms treat programs as sets of logical statements with well-defined semantics. These traditional analyzers can provide guarantees of their performance, such as guaranteeing that they will never miss a bug. However, they leave out lots of very rich information such as variable and field names. Language models for code on the other hand, take full advantage of information such as variable name...
  - **Labels**: [static analysis](static_analysis.md), [abstract interpretation](abstract_interpretation.md), [bug detection](bug_detection.md)


- [An Exploration of Large Language Models in Malicious Source Code Detection](../venues/CCS2024/paper_5.md), ([CCS2024](../venues/CCS2024/README.md))

  - **Abstract**: Embedding malicious code within the software supply chain has become a significant concern in the information technology field. Current methods for detecting malicious code, based on signatures, behavior analysis, and traditional machine learning models, lack result interpretability. This study proposes a novel malicious code detection framework, Mal-LLM, which leverages the cost advantages of traditional machine learning models and the interpretability of LLMs. Initially, traditional machine le...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [An LLM-Based Agent-Oriented Approach for Automated Code Design Issue Localization](../venues/ICSE2025/paper_33.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Maintaining software design quality is crucial for the long-term maintainability and evolution of systems. However, design issues such as poor modularity and excessive complexity often emerge as codebases grow. Developers rely on external tools, such as program analysis techniques, to identify such issues. This work leverages Large Language Models (LLMs) to develop an automated approach for analyzing and localizing design issues. Large language models have demonstrated significant performance on...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Artemis: Toward Accurate Detection of Server-Side Request Forgeries through LLM-Assisted Inter-procedural Path-Sensitive Taint Analysis](../venues/OOPSLA2025/paper_2.md), ([OOPSLA2025](../venues/OOPSLA2025/README.md))

  - **Abstract**: Server-side request forgery (SSRF) vulnerabilities are inevitable in PHP web applications. Existing static tools in detecting vulnerabilities in PHP web applications neither contain SSRF-related features to enhance detection accuracy nor consider PHP’s dynamic type features. In this paper, we present Artemis, a static taint analysis tool for detecting SSRF vulnerabilities in PHP web applications. First, Artemis extracts both PHP built-in and third-party functions as candidate source and sink fun...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Assisting Static Analysis with Large Language Models: A ChatGPT Experiment](../venues/FSE2023/paper_6.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Recent advances of Large Language Models (LLMs), e.g., ChatGPT, exhibited strong capabilities of comprehending and responding to questions across a variety of domains. Surprisingly, ChatGPT even possesses a strong understanding of program code. In this paper, we investigate where and how LLMs can assist static analysis by asking appropriate questions. In particular, we target a specific bug-finding tool, which produces many false positives from the static analysis. In our evaluation, we find tha...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Automated Static Vulnerability Detection via a Holistic Neuro-symbolic Approach](../venues/arXiv2025/paper_17.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Static vulnerability detection is still a challenging problem and demands excessive human efforts, e.g., manual curation of good vulnerability patterns. None of prior works, including classic program analysis or Large Language Model (LLM)-based approaches, have fully automated such vulnerability pattern generations with reasonable detection accuracy. In this paper, we design and implement, MoCQ, a novel holistic neuro-symbolic framework that combines the complementary strengths of LLMs and class...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Automatically Inspecting Thousands of Static Bug Warnings with Large Language Model: How Far Are We?](../venues/TKDD2024/paper_1.md), ([TKDD2024](../venues/TKDD2024/README.md))

  - **Abstract**: Static analysis tools for capturing bugs and vulnerabilities in software programs are widely employed in practice, as they have the unique advantages of high coverage and independence from the execution environment. However, existing tools for analyzing large codebases often produce a great deal of false warnings over genuine bug reports. As a result, developers are required to manually inspect and confirm each warning, a challenging, time-consuming, and automation-essential task.
 This article ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Beware of the unexpected: Bimodal taint analysis](../venues/ISSTA2023/paper_4.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Static analysis is a powerful tool for detecting security vulnerabilities and other programming problems. Global taint tracking, in particular, can spot vulnerabilities arising from complicated data flow across multiple functions. However, precisely identifying which flows are problematic is challenging, and sometimes depends on factors beyond the reach of pure program analysis, such as conventions and informal knowledge. For example, learning that a parameter name of an API function locale ends...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Beyond Static Pattern Matching? Rethinking Automatic Cryptographic API Misuse Detection in the Era of LLMs](../venues/ISSTA2025/paper_3.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: While the automated detection of cryptographic API misuses has progressed significantly, its precision diminishes for intricate targets due to the reliance on manually defined patterns. Large Language Models (LLMs) offer a promising context-aware understanding to address this shortcoming, yet the stochastic nature and the hallucination issue pose challenges to their applications in precise security analysis. This paper presents the first systematic study to explore LLMs’ application in cryptogra...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Boosting Static Resource Leak Detection via LLM-based Resource-Oriented Intention Inference](../venues/ICSE2025/paper_38.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Resource leaks, caused by resources not being released after acquisition, often lead to performance issues and system crashes. Existing static detection techniques rely on mechanical matching of predefined resource acquisition/release APIs and null-checking conditions to find unreleased resources, suffering from both (1) false negatives caused by the incompleteness of predefined resource acquisition/release APIs and (2) false positives caused by the incompleteness of resource reachability valida...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [CORE: Resolving Code Quality Issues using LLMs](../venues/FSE2024/paper_22.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: As software projects progress, quality of code assumes paramount importance as it affects reliability, maintainability and security of software. For this reason, static analysis tools are used in developer workflows to flag code quality issues. However, developers need to spend extra efforts to revise their code to improve code quality based on the tool findings. In this work, we investigate the use of (instruction-following) large language models (LLMs) to assist developers in revising code to ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [CellularLint: A Systematic Approach to Identify Inconsistent Behavior in Cellular Network Specifications](../venues/USENIXSec2024/paper_6.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: In recent years, there has been a growing focus on scrutinizing the security of cellular networks, often attributing security vulnerabilities to issues in the underlying protocol design descriptions. These protocol design specifications, typically extensive documents that are thousands of pages long, can harbor inaccuracies, underspecifications, implicit assumptions, and internal inconsistencies. In light of the evolving landscape, we introduce CellularLint—a semi-automatic framework for inconsi...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [Closing the Gap: A User Study on the Real-world Usefulness of AI-powered Vulnerability Detection & Repair in the IDE](../venues/ICSE2025/paper_1.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: This paper presents the first empirical study of a vulnerability detection and fix tool with professional software developers on real projects that they own. We implemented DeepVulGuard, an IDE-integrated tool based on state-of-the-art detection and fix models, and show that it has promising performance on benchmarks of historic vulnerability data. DeepVulGuard scans code for vulnerabilities (including identifying the vulnerability type and vulnerable region of code), suggests fixes, provides na...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Code Comment Inconsistency Detection and Rectification Using a Large Language Model](../venues/ICSE2025/paper_19.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Comments are widely used in source code. If a comment is consistent with the code snippet it intends to annotate, it would aid code comprehension. Otherwise, Code Comment Inconsistency (CCI) is not only detrimental to the understanding of code, but more importantly, it would negatively impact the development, testing, and maintenance of software. To tackle this issue, existing research has been primarily focused on detecting inconsistencies with varied performance. It is evident that detection a...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [CoderUJB: An Executable and Unified Java Benchmark for Practical Programming Scenarios](../venues/ISSTA2024/paper_3.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: In the evolving landscape of large language models (LLMs) tailored for software engineering, the need for benchmarks that accurately reflect real-world development scenarios is paramount. Current benchmarks are either too simplistic or fail to capture the multi-tasking nature of software development. To address this, we introduce CoderUJB, a new benchmark designed to evaluate LLMs across diverse Java programming tasks that are executable and reflective of actual development scenarios, acknowledg...
  - **Labels**: [code generation](code_generation.md), [program testing](program_testing.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [Collaboration to Repository-Level Vulnerability Detection](../venues/ISSTA2024/paper_26.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Large Language Model (LLM)-based methods have proven to be effective for many software engineering domains, with a potential for substantial productivity effective for software vulnerability detection.    However, due to the limitation of the length of input contexts of LLM, the existing LLM-based methods mainly focus on detecting function-level and leveraging the in-file context information for vulnerability detection (i.e., intra-procedural vulnerabilities), ignoring the more complex inter-pro...
  - **Labels**: [code generation](code_generation.md), [bug detection](bug_detection.md)


- [Combining Fine-Tuning and LLM-Based Agents for Intuitive Smart Contract Auditing with Justifications](../venues/ICSE2025/paper_16.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Smart contracts are decentralized applications built atop blockchains like Ethereum. Recent research has shown that large language models (LLMs) have potential in auditing smart contracts, but the state-of-the-art indicates that even GPT-4 can achieve only 30% precision (when both decision and justification are correct). This is likely because off-the-shelf LLMs were primarily pre-trained on a general text/code corpus and not fine-tuned on the specific domain of Solidity smart contract auditing....
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Combining Fine-Tuning and LLM-based Agents for Intuitive Smart Contract Auditing with Justifications](../venues/ICSE2025/paper_6.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Smart contracts are decentralized applications built atop blockchains like Ethereum. Recent research has shown that large language models (LLMs) have potential in auditing smart contracts, but the state-of-the-art indicates that even GPT-4 can achieve only 30% precision (when both decision and justification are correct). This is likely because off-the-shelf LLMs were primarily pre-trained on a general text/code corpus and not fine-tuned on the specific domain of Solidity smart contract auditing....
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [agent design](agent_design.md)


- [Combining Large Language Models with Static Analyzers for Code Review Generation](../venues/arXiv2025/paper_13.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Code review is a crucial but often complex, subjective, and time-consuming activity in software development. Over the past decades, significant efforts have been made to automate this process. Early approaches focused on knowledge-based systems (KBS) that apply rule-based mechanisms to detect code issues, providing precise feedback but struggling with complex, context-dependent cases. More recent work has shifted toward fine-tuning pre-trained language models for code review, enabling broader is...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Continuous learning for android malware detection](../venues/USENIXSec2023/paper_2.md), ([USENIXSec2023](../venues/USENIXSec2023/README.md))

  - **Abstract**: Machine learning methods can detect Android malware with very high accuracy. However, these classifiers have an Achilles heel, concept drift: they rapidly become out of date and ineffective, due to the evolution of malware apps and benign apps. Our research finds that, after training an Android malware classifier on one year's worth of data, the F1 score quickly dropped from 0.99 to 0.76 after 6 months of deployment on new test samples....
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection](../venues/ICSE2024/paper_2.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Deep learning-based vulnerability detection has shown great performance and, in some studies, outperformed static analysis tools. However, the highest-performing approaches use token-based transformer models, which are not the most efficient to capture code semantics required for vulnerability detection. Classical program analysis techniques such as dataflow analysis can detect many types of bugs based on their root causes. In this paper, we propose to combine such causal-based vulnerability det...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Dependency-Aware Code Naturalness](../venues/OOPSLA2024/paper_8.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Code naturalness, which captures repetitiveness and predictability in programming languages, has proven valuable for various code-related tasks in software engineering. However, precisely measuring code naturalness remains a fundamental challenge. Existing methods measure code naturalness over individual lines of code while ignoring the deep semantic relations among different lines, e.g., program dependency, which may negatively affect the precision of the measure. Despite the intuitive appeal o...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [empirical study](empirical_study.md)


- [DiverseVul: {A} New Vulnerable Source Code Dataset for Deep Learning Based Vulnerability Detection](../venues/RAID2023/paper_1.md), ([RAID2023](../venues/RAID2023/README.md))

  - **Abstract**: We propose and release a new vulnerable source code dataset. We curate the dataset by crawling security issue websites, extracting vulnerability-fixing commits and source codes from the corresponding projects. Our new dataset contains 18,945 vulnerable functions spanning 150 CWEs and 330,492 non-vulnerable functions extracted from 7,514 commits. Our dataset covers 295 more projects than all previous datasets combined.Combining our new dataset with previous datasets, we present an analysis of the...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [Do Language Models Learn Semantics of Code? {A} Case Study in Vulnerability Detection](../venues/arXiv2023/paper_7.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Recently, pretrained language models have shown state-of-the-art performance on the vulnerability detection task. These models are pretrained on a large corpus of source code, then fine-tuned on a smaller supervised vulnerability dataset. Due to the different training objectives and the performance of the models, it is interesting to consider whether the models have learned the semantics of code relevant to vulnerability detection, namely bug semantics, and if so, how the alignment to bug semant...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Do you still need a manual smart contract audit?](../venues/arXiv2023/paper_9.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: We investigate the feasibility of employing large language models (LLMs) for conducting the security audit of smart contracts, a traditionally time-consuming and costly process. Our research focuses on the optimization of prompt engineering for enhanced security analysis, and we evaluate the performance and accuracy of LLMs using a benchmark dataset comprising 52 Decentralized Finance (DeFi) smart contracts that have previously been compromised.     Our findings reveal that, when applied to vuln...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [EAGLEYE: Exposing Hidden Web Interfaces in IoT Devices via Routing Analysis](../venues/NDSS2025/paper_5.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: Hidden web interfaces, i.e., undisclosed access channels in IoT devices, introduce great security risks and have resulted in severe attacks in recent years. However, the definition of such threats is vague, and few solutions are able to discover them. Due to their hidden nature, traditional bug detection solutions (e.g., taint analysis, fuzzing) are hard to detect them. In this paper, we present a novel solution EAGLEYE to automatically expose hidden web interfaces in IoT devices. By analyzing i...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [Effective Vulnerable Function Identification based on CVE Description Empowered by Large Language Models](../venues/ASE2024/paper_6.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Open-source software (OSS) has profoundly transformed the software development paradigm by facilitating effortless code reuse. However, in recent years, there has been an alarming increase in disclosed vulnerabilities within OSS, posing significant security risks to downstream users. Therefore, analyzing existing vulnerabilities and precisely assessing their threats to downstream applications become pivotal. Plenty of efforts have been made recently towards this problem, such as vulnerability re...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Enhancing Security in Third-Party Library Reuse – Comprehensive Detection of 1-day Vulnerability through Code Patch Analysis](../venues/NDSS2025/paper_6.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: Nowadays, software development progressesrapidly to incorporate new features. To facilitate such growthand provide convenience for developers when creating andupdating software, reusing open-source software (i.e., thirdpartylibrary reuses) has become one of the most effectiveand efficient methods. Unfortunately, the practice of reusingthird-party libraries (TPLs) can also introduce vulnerabilities(known as 1-day vulnerabilities) because of the low maintenanceof TPLs, resulting in many vulnerable...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [Enhancing Static Analysis for Practical Bug Detection: An LLM-Integrated Approach](../venues/OOPSLA2024/paper_5.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: While static analysis is instrumental in uncovering software bugs, its precision in analyzing large and intricate codebases remains challenging. The emerging prowess of Large Language Models (LLMs) offers a promising avenue to address these complexities. In this paper, we present LLift, a pioneering framework that synergizes static analysis and LLMs, with a spotlight on identifying use-before-initialization (UBI) bugs within the Linux kernel. Drawing from our insights into variable usage convent...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Enhancing Vulnerability Detection via Inter-procedural Semantic Completion](../venues/ISSTA2025/paper_11.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Inspired by advances in deep learning, numerous learning-based approaches for vulnerability detection have emerged, primarily operating at the function level for scalability. However, this design choice has a critical limitation: many vulnerabilities span multiple functions, causing function-level approaches to lose the semantics of called functions and fail to capture true vulnerability patterns. To address this issue, we propose VulnSC, a novel framework designed to enhance learning-based appr...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code summarization](code_summarization.md)


- [Error Delayed Is Not Error Handled: Understanding and Fixing Propagated Error-Handling Bugs](../venues/FSE2025/paper_33.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Error handling is critical for software reliability. In software systems, error handling may be delayed to other functions. Such propagated error handling (PEH) could easily be missed and lead to bugs. Our research reveals that PEH bugs are prevalent in software systems and, on average, take 44.1 days to fully address. Existing approaches have primarily focused on the error-handling bug within individual functions, which makes it difficult to fully address PEH bugs. In this paper, we conducted t...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Evaluating the Effectiveness of Small Language Models in Detecting Refactoring Bugs](../venues/arXiv2025/paper_12.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Popular IDEs frequently contain bugs in their refactoring implementations. Ensuring that a transformation preserves a program's behavior is a complex task. Traditional detection methods rely on predefined preconditions for each refactoring type, limiting their scalability and adaptability to new transformations. These methods often require extensive static and dynamic analyses, which are computationally expensive, time-consuming, and may still fail to detect certain refactoring bugs. This study ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Examining Zero-Shot Vulnerability Repair with Large Language Models](../venues/S&P2023/paper_1.md), ([S&P2023](../venues/S&P2023/README.md))

  - **Abstract**: Human developers can produce code with cybersecurity bugs. Can emerging ‘smart’ code completion tools help repair those bugs? In this work, we examine the use of large language models (LLMs) for code (such as OpenAI’s Codex and AI21’s Jurassic J-1) for zero-shot vulnerability repair. We investigate challenges in the design of prompts that coax LLMs into generating repaired versions of insecure code. This is difficult due to the numerous ways to phrase key information— both semantically and synta...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Explaining Software Bugs Leveraging Code Structures in Neural Machine Translation](../venues/ICSE2023/paper_6.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Software bugs claim ≈ 50\% of development time and cost the global economy billions of dollars. Once a bug is reported, the assigned developer attempts to identify and understand the source code responsible for the bug and then corrects the code. Over the last five decades, there has been significant research on automatically finding or correcting software bugs. However, there has been little research on automatically explaining the bugs to the developers, which is essential but a highly challen...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [E{\&}V: Prompting Large Language Models to Perform Static Analysis by Pseudo-code Execution and Verification](../venues/Microsoft2023/paper_2.md), ([Microsoft2023](../venues/Microsoft2023/README.md))

  - **Abstract**: Static analysis, the process of examining code without executing it, is crucial for identifying software issues. Yet, static analysis is hampered by its complexity and the need for customization for different targets. Traditional static analysis tools require extensive human effort and are often limited to specific target programs and programming languages. Recent advancements in Large Language Models (LLMs), such as GPT-4 and Llama, offer new capabilities for software engineering tasks. However...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [From Large to Mammoth: A Comparative Evaluation of Large Language Models in Vulnerability Detection](../venues/NDSS2025/paper_7.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated strong potential in tasks such as code understanding and generation. This study evaluates several advanced LLMs—such as LLaMA-2, CodeLLaMA, LLaMA-3, Mistral, Mixtral, Gemma, CodeGemma, Phi-2, Phi-3, and GPT-4—for vulnerability detection, primarily in Java, with additional tests in C/C++ to assess generalization. We transition from basic positive sample detection to a more challenging task involving both positive and negative samples and evaluate the...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis](../venues/ICSE2024/paper_17.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Smart contracts are prone to various vulnerabilities, leading to substantial financial losses over time. Current analysis tools mainly target vulnerabilities with fixed control- or data-flow patterns, such as re-entrancy and integer overflow. However, a recent study on Web3 security bugs revealed that about 80\% of these bugs cannot be audited by existing tools due to the lack of domain-specific property description and checking. Given recent advances in Large Language Models (LLMs), it is worth...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Generating API Parameter Security Rules with LLM for API Misuse Detection](../venues/NDSS2025/paper_1.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: When utilizing library APIs, developers should follow the API security rules to mitigate the risk of API misuse. API Parameter Security Rule (APSR) is a common type of security rule that specifies how API parameters should be safely used and places constraints on their values. Failure to comply with the APSRs can lead to severe security issues, including null pointer dereference and memory corruption. Manually analyzing numerous APIs and their parameters to construct APSRs is labor-intensive and...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [Gptscan: Detecting logic vulnerabilities in smart contracts by combining gpt with program analysis](../venues/ICSE2024/paper_22.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Smart contracts are prone to various vulnerabilities, leading to substantial financial losses over time. Current analysis tools mainly target vulnerabilities with fixed control- or data-flow patterns, such as re-entrancy and integer overflow. However, a recent study on Web3 security bugs revealed that about 80% of these bugs cannot be audited by existing tools due to the lack of domain-specific property description and checking. Given recent advances in Large Language Models (LLMs), it is worth ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Harnessing the power of llm to support binary taint analysis](../venues/TOSEM2024/paper_7.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: This paper proposes LATTE, the first static binary taint analysis that is powered by a large language model (LLM). LATTE is superior to the state of the art (e.g., Emtaint, Arbiter, Karonte) in three aspects. First, LATTE is fully automated while prior static binary taint analyzers need rely on human expertise to manually customize taint propagation rules and vulnerability inspection rules. Second, LATTE is significantly effective in vulnerability detection, demonstrated by our comprehensive eva...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Hermes: Unlocking Security Analysis of Cellular Network Protocols by Synthesizing Finite State Machines from Natural Language Specifications](../venues/USENIXSec2024/paper_5.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: In this paper, we present Hermes, an end-to-end framework to automatically generate formal representations from natural language cellular specifications. We first develop a neural constituency parser, NEUTREX, to process transition-relevant texts and extract transition components (i.e., states, conditions, and actions). We also design a domain-specific language to translate these transition components to logical formulas by leveraging dependency parse trees. Finally, we compile these logical for...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [How Far Have We Gone in Vulnerability Detection Using Large Language Models](../venues/arXiv2023/paper_5.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: As software becomes increasingly complex and prone to vulnerabilities, automated vulnerability detection is critically important, yet challenging. Given the significant successes of large language models (LLMs) in various tasks, there is growing anticipation of their efficacy in vulnerability detection. However, a quantitative understanding of their potential in vulnerability detection is still missing. To bridge this gap, we introduce a comprehensive vulnerability benchmark VulBench. This bench...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [Hyperion: Unveiling DApp Inconsistencies Using LLM and Dataflow-Guided Symbolic Execution](../venues/ICSE2025/paper_11.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: The rapid advancement of blockchain platforms has significantly accelerated the growth of decentralized applications (DApps). Similar to traditional applications, DApps integrate front-end descriptions that showcase their features to attract users, and back-end smart contracts for executing their business logic. However, inconsistencies between the features promoted in front-end descriptions and those actually implemented in the contract can confuse users and undermine DApps's trustworthiness. I...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Identifying Multi-parameter Constraint Errors in Python Data Science Library API Documentation](../venues/ISSTA2025/paper_22.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Modern AI- and Data-intensive software systems rely heavily on data science and machine learning libraries that provide essential algorithmic implementations and computational frameworks. These libraries expose complex APIs whose correct usage has to follow constraints among multiple interdependent parameters. Developers using these APIs are expected to learn about the constraints through the provided documentation and any discrepancy may lead to unexpected behaviors. However, maintaining correc...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [If At First You Don’t Succeed, Try, Try, Again...? Insights and LLM-informed Tooling for Detecting Retry Bugs in Software Systems](../venues/SOSP2024/paper_1.md), ([SOSP2024](../venues/SOSP2024/README.md))

  - **Abstract**: Retry—the re-execution of a task on failure—is a common mechanism to enable resilient software systems. Yet, despite its commonality and long history, retry remains difficult to implement and test. Guided by our study of real-world retry issues, we propose a novel suite of static and dynamic techniques to detect retry problems in software. We find that the ad-hoc nature of retry implementation poses challenges for traditional program analysis but can be well suited for large language models; and...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Interleaving Static Analysis and LLM Prompting](../venues/SOAP2024/paper_1.md), ([SOAP2024](../venues/SOAP2024/README.md))

  - **Abstract**: This paper presents a new approach for using Large Language Models (LLMs) to improve static program analysis. Specifically, during program analysis, we interleave calls to the static analyzer and queries to the LLM: the prompt used to query the LLM is constructed using intermediate results from the static analysis, and the result from the LLM query is used for subsequent analysis of the program. We apply this novel approach to the problem of error-specification inference of functions in systems ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Jtrans: Jump-aware transformer for binary code similarity detection](../venues/ISSTA2022/paper_1.md), ([ISSTA2022](../venues/ISSTA2022/README.md))

  - **Abstract**: Binary code similarity detection (BCSD) has important applications in various fields such as vulnerabilities detection, software component analysis, and reverse engineering. Recent studies have shown that deep neural networks (DNNs) can comprehend instructions or control-flow graphs (CFG) of binary code and support BCSD. In this study, we propose a novel Transformer-based approach, namely jTrans, to learn representations of binary code. It is the first solution that embeds control flow informati...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [KNighter: Transforming Static Analysis with LLM-Synthesized Checkers](../venues/arXiv2025/paper_10.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Static analysis is a powerful technique for bug detection in critical systems like operating system kernels. However, designing and implementing static analyzers is challenging, timeconsuming, and typically limited to predefined bug patterns. While large language models (LLMs) have shown promise for static analysis, directly applying them to scan large codebases remains impractical due to computational constraints and contextual limitations. We present KNighter, the first approach that unlocks p...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [LAMD: Context-driven Android Malware Detection and Classification with LLMs](../venues/arXiv2025/paper_4.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: The rapid growth of mobile applications has escalated Android malware threats. Although there are numerous detection methods, they often struggle with evolving attacks, dataset biases, and limited explainability. Large Language Models (LLMs) offer a promising alternative with their zero-shot inference and reasoning capabilities. However, applying LLMs to Android malware detection presents two key challenges: (1)the extensive support code in Android applications, often spanning thousands of class...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [LLM-Assisted Static Analysis for Detecting Security Vulnerabilities](../venues/arXiv2024/paper_21.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Software is prone to security vulnerabilities. Program analysis tools to detect them have limited effectiveness in practice due to their reliance on human labeled specifications. Large language models (or LLMs) have shown impressive code generation capabilities but they cannot do complex reasoning over code to detect such vulnerabilities especially since this task requires whole-repository analysis. We propose IRIS, a neuro-symbolic approach that systematically combines LLMs with static analysis...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [LLM-based Resource-Oriented Intention Inference for Static Resource Detection](../venues/ICSE2025/paper_5.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Resource leaks, caused by resources not being released after acquisition, often lead to performance issues and system crashes. Existing static detection techniques rely on mechanical matching of predefined resource acquisition/release APIs and null-checking conditions to find unreleased resources, suffering from both (1) false negatives caused by the incompleteness of predefined resource acquisition/release APIs and (2) false positives caused by the unsoundness of resource reachability validatio...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [LLM4Vuln: {A} Unified Evaluation Framework for Decoupling and Enhancing LLMs' Vulnerability Reasoning](../venues/arXiv2024/paper_19.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated significant potential in various tasks, including vulnerability detection. However, current efforts in this area are preliminary, lacking clarity on whether LLMs' vulnerability reasoning capabilities stem from the models themselves or external aids such as knowledge retrieval and tooling support.This paper aims to isolate LLMs' vulnerability reasoning from other capabilities, such as vulnerability knowledge adoption, context information retrieval, a...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [LLMDFA: Analyzing Dataflow in Code with Large Language Model](../venues/NeurIPS2024/paper_6.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Dataflow analysis is a fundamental code analysis technique that identifies dependencies between program values. Traditional approaches typically necessitate successful compilation and expert customization, hindering their applicability and usability for analyzing uncompilable programs with evolving analysis needs in realworld scenarios. This paper presents LLMDFA, an LLM-powered compilation-free and customizable dataflow analysis framework. To address hallucinations for reliable results, we deco...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?): A Comprehensive Evaluation, Framework, and Benchmarks](../venues/S&P2024/paper_1.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have been suggested for use in automated vulnerability repair, but benchmarks showing they can consistently identify security-related bugs are lacking. We thus develop SecLLMHolmes, a fully automated evaluation framework that performs the most detailed investigation to date on whether LLMs can reliably identify and reason about security-related bugs. We construct a set of 228 code scenarios and analyze eight of the most capable LLMs across eight different investigati...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Large Language Models for Code Analysis: Do LLMs Really Do Their Job?](../venues/USENIXSec2024/paper_1.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated significant potential in the realm of natural language understanding and programming code processing tasks. Their capacity to comprehend and generate human-like code has spurred research into harnessing LLMs for code analysis purposes. However, the existing body of literature falls short in delivering a systematic evaluation and assessment of LLMs' effectiveness in code analysis, particularly in the context of obfuscated code.This paper seeks to bri...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Large Language Models for In-File Vulnerability Localization Can Be “Lost in the End”](../venues/FSE2025/paper_12.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Traditionally, software vulnerability detection research has focused on individual small functions due to earlier language processing technologies’ limitations in handling larger inputs. However, this function-level approach may miss bugs that span multiple functions and code blocks. Recent advancements in artificial intelligence have enabled processing of larger inputs, leading everyday software developers to increasingly rely on chat-based large language models (LLMs) like GPT-3.5 and GPT-4 to...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Large Language Models for Validating Network Protocol Parsers](../venues/LangSec2025/paper_1.md), ([LangSec2025](../venues/LangSec2025/README.md))

  - **Abstract**: Network protocol parsers are essential for enabling correct and secure communication between devices. Bugs in these parsers can introduce critical vulnerabilities, including memory corruption, information leakage, and denial-of-service attacks. An intuitive way to assess parser correctness is to compare the implementation with its official protocol standard. However, this comparison is challenging because protocol standards are typically written in natural language, whereas implementations are i...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md), [bug detection](bug_detection.md)


- [Large language model-powered smart contract vulnerability detection: New perspectives](../venues/arXiv2023/paper_10.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: This paper provides a systematic analysis of the opportunities, challenges, and potential solutions of harnessing Large Language Models (LLMs) such as GPT-4 to dig out vulnerabilities within smart contracts based on our ongoing research. For the task of smart contract vulnerability detection, achieving practical usability hinges on identifying as many true vulnerabilities as possible while minimizing the number of false positives. Nonetheless, our empirical study reveals contradictory yet intere...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Learning to Detect and Localize Multilingual Bugs](../venues/FSE2024/paper_31.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Increasing studies have shown bugs in multi-language software as a critical loophole in modern software quality assurance, especially those induced by language interactions (i.e., multilingual bugs). Yet existing tool support for bug detection/localization remains largely limited to single-language software, despite the long-standing prevalence of multi-language systems in various real-world software domains. Extant static/dynamic analysis and deep learning (DL) based approaches all face major c...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Leveraging Large Language Model to Assist Detecting Rust Code Comment Inconsistency](../venues/ASE2024/paper_5.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Rust is renowned for its robust memory safety capabilities, yet its distinctive memory management model poses substantial challenges in both writing and understanding programs. Within Rust source code, comments are employed to clearly delineate conditions that might cause panic behavior, thereby warning developers about potential hazards associated with specific operations. Therefore, comments are particularly crucial for documenting Rust's program logic and design. Nevertheless, as modern softw...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Leveraging Large Language Models to Detect NPM Malicious Packages](../venues/ICSE2025/paper_44.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Existing malicious code detection techniques demand the integration of multiple tools to detect different malware patterns, often suffering from high misclassification rates. Therefore, malicious code detection techniques could be enhanced by adopting advanced, more automated approaches to achieve high accuracy and a low misclassification rate. The goal of this study is to aid security analysts in detecting malicious packages by empirically studying the effectiveness of Large Language Models (LL...
  - **Labels**: [program testing](program_testing.md), [bug detection](bug_detection.md)


- [Leveraging Semantic Relations in Code and Data to Enhance Taint Analysis of Embedded Systems](../venues/USENIXSec2024/paper_2.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: IoT devices have significantly impacted our daily lives, and detecting vulnerabilities in embedded systems early on is critical for ensuring their security. Among the existing vulnerability detection techniques for embedded systems, static taint analysis has been proven effective in detecting severe vulnerabilities, such as command injection vulnerabilities, which can cause remote code execution. Nevertheless, static taint analysis is faced with the problem of identifying sources comprehensively...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Minimizing False Positives in Static Bug Detection via LLM-Enhanced Path Feasibility Analysis](../venues/arXiv2025/paper_8.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Static bug analyzers play a crucial role in ensuring software quality. However, existing analyzers for bug detection in large codebases often suffer from high false positive rates. This is primarily due to the limited capabilities of analyzers in path feasibility validation with multiple conditional branches and complex data dependencies. While current LLM-based approaches attempt to address this issue, their effectiveness remains limited due to insufficient constraint cascade analysis and scala...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Planning a Large Language Model for Static Detection of Runtime Errors in Code Snippets](../venues/ICSE2025/paper_34.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have been excellent in generating and reasoning about source code and natural-language texts. They can recognize patterns, syntax, and semantics in code, making them effective in several software engineering tasks. However, they exhibit weaknesses in reasoning about the program execution. They primarily operate on static code representations, failing to capture the dynamic behavior and state changes that occur during program execution. In this paper, we advance the c...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Pre-training by Predicting Program Dependencies for Vulnerability Analysis Tasks](../venues/ICSE2024/paper_30.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Vulnerability analysis is crucial for software security. Inspired by the success of pre-trained models on software engineering tasks, this work focuses on using pre-training techniques to enhance the understanding of vulnerable code and boost vulnerability analysis. The code understanding ability of a pre-trained model is highly related to its pre-training objectives. The semantic structure, e.g., control and data dependencies, of code is important for vulnerability analysis. However, existing p...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [PropertyGPT: LLM-driven Formal Verification of Smart Contracts through Retrieval-Augmented Property Generation](../venues/NDSS2025/paper_8.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: Formal verification is a technique that can prove the correctness of a system with respect to a certain specification or property. It is especially valuable for security-sensitive smart contracts that manage billions in cryptocurrency assets. Although existing research has developed various static verification tools (or provers) for smart contracts, a key missing component is theautomated generation of comprehensive properties, including invariants, pre-/post-conditions, and rules. Hence, indust...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [program verification](program_verification.md)


- [ROCODE: Integrating Backtracking Mechanism and Program Analysis in Large Language Models for Code Generation](../venues/ICSE2025/paper_40.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large language models (LLMs) have achieved impressive performance in code generation recently, offering programmers revolutionary assistance in software development. However, due to the auto-regressive nature of LLMs, they are susceptible to error accumulation during code generation. Once an error is produced, LLMs can merely continue to generate the subsequent code conditioned on it, given their inability to adjust previous outputs. Existing LLM-based approaches typically consider post-revising...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [RealVul: Can We Detect Vulnerabilities in Web Applications with LLM?](../venues/EMNLP2024/paper_24.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: The latest advancements in large language models (LLMs) have sparked interest in their potential for software vulnerability detection. However, there is currently a lack of research specifically focused on vulnerabilities in the PHP language, and challenges in data sampling and processing persist, hindering the model’s ability to effectively capture the characteristics of specific vulnerabilities. In this paper, we present RealVul, the first LLM-based framework designed for PHP vulnerability det...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [RepoAudit: An Autonomous LLM-Agent for Repository-Level Code Auditing](../venues/ICML2025/paper_2.md), ([ICML2025](../venues/ICML2025/README.md))

  - **Abstract**: Code auditing is a code review process with the goal of finding bugs. Large Language Models (LLMs) have shown substantial potential in this task, offering the ability to analyze programs without compilation and enabling customized bug detection following specified prompts. However, applying LLMs to repository-level code auditing presents notable challenges. The inherent context limits and hallucinations of LLMs can lead to the low quality of bug reports. Meanwhile, the large size of software rep...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md), [planning](planning.md)


- [Risky Dynamic Typing-related Practices in Python: An Empirical Study](../venues/TOSEM2024/paper_6.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Python’s dynamic typing nature provides developers with powerful programming abstractions. However, many type-related bugs are accumulated in code bases of Python due to the misuse of dynamic typing. The goal of this article is to aid in the understanding of developers’ high-risk practices toward dynamic typing and the early detection of type-related bugs. We first formulate the rules of six types of risky dynamic typing-related practices (type smells for short) in Python. We then develop a rule...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Robust Vulnerability Detection across Compilations: LLVM-IR vs. Assembly with Transformer Model](../venues/ISSTA2025/paper_9.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Detecting vulnerabilities in binary files is a challenging task in cybersecurity, particularly when source code is unavailable and the compilation process and its parameters are unknown. Existing deep learning-based detection methods often rely on knowing a binary’s specific compilation settings, which may limit their ability to perform well on other types of binaries. In this research, we provide a thorough comparison of assembly representation and LLVM-IR to identify which representation is mo...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model robustness](code_model_robustness.md)


- [SCALE: Constructing Structured Natural Language Comment Trees for Software Vulnerability Detection](../venues/ISSTA2024/paper_4.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Recently, there has been a growing interest in automatic software vulnerability detection.     Pre-trained model-based approaches have demonstrated superior performance than other Deep Learning (DL)-based approaches in detecting vulnerabilities.     However, the existing pre-trained model-based approaches generally employ code sequences as input during prediction, and may ignore vulnerability-related structural information, as reflected in the following two aspects.     First, they tend to fail ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [SV-TrustEval-C: Evaluating Structure and Semantic Reasoning in Large Language Models for Source Code Vulnerability Analysis](../venues/S&P2025/paper_1.md), ([S&P2025](../venues/S&P2025/README.md))

  - **Abstract**: As Large Language Models (LLMs) evolve in understanding and generating code, accurately evaluating their reliability in analyzing source code vulnerabilities becomes in-creasingly vital. While studies have examined LLM capabilities in tasks like vulnerability detection and repair, they often over-look the importance of both structure and semantic reasoning crucial for trustworthy vulnerability analysis. To address this gap, we introduce SV-TRUSTEVAL-C, a benchmark designed to evaluate LLMs' abil...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)


- [Safe4U: Identifying Unsound Safe Encapsulations of Unsafe Calls in Rust using LLMs](../venues/ISSTA2025/paper_6.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Rust is an emerging programming language that ensures safety through strict compile-time checks. A Rust function marked as unsafe indicates it has additional safety requirements (e.g., initialized, not null), known as contracts in the community. These unsafe functions can only be called within explicit unsafe blocks and the contracts must be guaranteed by the caller. To reuse and reduce unsafe code, the community recommends using safe encapsulation of unsafe calls (EUC) in practice. However, an ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Sanitizing Large Language Models in Bug Detection with Data-Flow](../venues/EMNLP2024/paper_4.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large language models (LLMs) show potential in code reasoning tasks, facilitating the customization of detecting bugs in software development. However, the hallucination effect can significantly compromise the reliability of bug reports. This work formulates a new schema of bug detection and presents a novel sanitization technique that detects false positives for hallucination mitigation. Our key idea is to enforce LLMs to emit data-flow paths in few-shot chain-of-thought prompting and validate ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [data-flow analysis](data-flow_analysis.md)


- [SecVulEval: Benchmarking LLMs for Real-World C/C++ Vulnerability Detection](../venues/arXiv2025/paper_2.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have shown promise in software engineering tasks, but evaluating their effectiveness in vulnerability detection is challenging due to the lack of high-quality datasets. Most existing datasets are limited to function-level labels, ignoring finer-grained vulnerability patterns and crucial contextual information. Also, poor data quality such as mislabeling, inconsistent annotations, and duplicates can lead to inflated performance and weak generalization. Moreover, by in...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [Semantic Sleuth: Identifying Ponzi Contracts via Large Language Models](../venues/ASE2024/paper_11.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Smart contracts, self-executing agreements directly encoded in code, are fundamental to blockchain technology, especially in decentralized finance (DeFi) and Web3. However, the rise of Ponzi schemes in smart contracts poses significant risks, leading to substantial financial losses and eroding trust in blockchain systems. Existing detection methods, such as PonziGuard, depend on large amounts of labeled data and struggle to identify unseen Ponzi schemes, limiting their reliability and generaliza...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [SkipAnalyzer: An Embodied Agent for Code Analysis with Large Language Models](../venues/arXiv2023/paper_8.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: We introduce SkipAnalyzer, a large language model (LLM)-powered tool for static code analysis. SkipAnalyzer has three components: 1) an LLM-based static bug detector that scans source code and reports specific types of bugs, 2) an LLM-based false-positive filter that can identify false-positive bugs in the results of static bug detectors (e.g., the result of step 1) to improve detection accuracy, and 3) an LLM-based patch generator that can generate patches for the detected bugs above. As a proo...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [agent design](agent_design.md)


- [Smart-LLaMA-DPO: Reinforced Large Language Model for Explainable Smart Contract Vulnerability Detection](../venues/ISSTA2025/paper_4.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Smart contract vulnerability detection is a critical challenge in the rapidly evolving blockchain landscape. Existing vulnerability detection methods face two main issues: (1) Existing datasets lack comprehensiveness and sufficient quality, with limited vulnerability type coverage and insufficient distinction between high-quality and low-quality explanations for preference learning. (2) Large language models (LLMs) often struggle with accurately interpreting specific concepts in smart contract s...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Smartinv: Multimodal learning for smart contract invariant inference](../venues/S&P2024/paper_4.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Smart contracts are software programs that enable diverse business activities on the blockchain. Recent research has identified new classes of "machine un-auditable" bugs that arise from source code not meeting underlying transaction contexts. Existing detection methods require human understanding of underlying transaction logic and manual reasoning across different sources of context (i.e., modalities), such as code and natural language specifying the expected transaction behavior.To automate t...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Source Code Vulnerability Detection: Combining Code Language Models and Code Property Graphs](../venues/arXiv2024/paper_17.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Currently, deep learning successfully applies to code vulnerability detection by learning from code sequences or property graphs. However, sequence-based methods often overlook essential code attributes such as syntax, control flow, and data dependencies, whereas graph-based approaches might underestimate the semantics of code and face challenges in capturing long-distance contextual information.To address this gap, we propose Vul-LMGNN, a unified model that combines pre-trained code language mo...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Stanceformer: Target-Aware Transformer for Stance Detection](../venues/EMNLP2024/paper_5.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: The task of Stance Detection involves discerning the stance expressed in a text towards a specific subject or target. Prior works have relied on existing transformer models that lack the capability to prioritize targets effectively. Consequently, these models yield similar performance regardless of whether we utilize or disregard target information, undermining the task’s significance. To address this challenge, we introduce Stanceformer, a target-aware transformer model that incorporates enhanc...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Statement-Level Adversarial Attack on Vulnerability Detection Models via Out-of-Distribution Features](../venues/FSE2025/paper_41.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Code vulnerability detection is crucial to ensure software security. Recent advancements, particularly with the emergence of Code Pre-Trained Models (CodePTMs) and Large Language Models (LLMs), have led to significant progress in this area. However, these models are easily susceptible to adversarial attacks, where even slight input modifications can lead the models to generate opposite results. Existing adversarial approaches, such as identifier replacement, code transformation, and dead code in...
  - **Labels**: [code model](code_model.md), [code model robustness](code_model_robustness.md), [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [The EarlyBIRD Catches the Bug: On Exploiting Early Layers of Encoder Models for More Efficient Code Classification](../venues/FSE2023/paper_12.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: The use of modern Natural Language Processing (NLP) techniques has shown to be beneficial for software engineering tasks, such as vulnerability detection and type inference. However, training deep NLP models requires significant computational resources. This paper explores techniques that aim at achieving the best usage of resources and available information in these models.  We propose a generic approach, EarlyBIRD, to build composite representations of code from the early layers of a pre-train...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)


- [The Emergence of Large Language Models in Static Analysis: A First Look through Micro-Benchmarks](../venues/Forge2024/paper_1.md), ([Forge2024](../venues/Forge2024/README.md))

  - **Abstract**: Binary code similarity detection(BCSD), as a fundamental technique in software security, has various applications, including malware family detection, known vulnerability detection and code plagiarism detection. Recent deep learning-based BCSD approaches have demonstrated promising performance. However, they face two significant challenges that limit detection performance. First, most approaches that use sequence networks (like RNN and Transformer) utilize coarse-grained tokenization methods, wh...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [The Hitchhiker's Guide to Program Analysis, Part II: Deep Thoughts by LLMs](../venues/arXiv2025/paper_3.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Static analysis is a cornerstone for software vulnerability detection, yet it often struggles with the classic precision-scalability trade-off. In practice, such tools often produce high false positive rates, particularly in large codebases like the Linux kernel. This imprecision can arise from simplified vulnerability modeling and over-approximation of path and data constraints. While large language models (LLMs) show promise in code understanding, their naive application to program analysis yi...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [The Midas Touch: Triggering the Capability of LLMs for RM-API Misuse Detection](../venues/NDSS2025/paper_3.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: As the basis of software resource management (RM), strictly following the RM-API constraints guarantees secure resource management and software. To enhance the RM-API application, researchers find it effective in detecting RM-API misuse on open-source software according to RM-API constraints retrieved from documentation and code. However, the current pattern-matching constraint retrieval methods have limitations: the documentation-based methods leave many API constraints irregularly distributed ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [Top Score on the Wrong Exam: On Benchmarking in Machine Learning for Vulnerability Detection](../venues/arXiv2024/paper_20.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: According to our survey of the machine learning for vulnerability detection (ML4VD) literature published in the top Software Engineering conferences, every paper in the past 5 years defines ML4VD as a binary classification problem: Given a function, does it contain a security flaw?In this paper, we ask whether this decision can really be made without further context and study both vulnerable and non-vulnerable functions in the most popular ML4VD datasets. A function is vulnerable if it was invol...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Twin Graph-Based Anomaly Detection via Attentive Multi-Modal Learning for Microservice System](../venues/ASE2023/paper_16.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Microservice architecture has sprung up over recent years for managing enterprise applications, due to its ability to independently deploy and scale services. Despite its benefits, ensuring the reliability and safety of a microservice system remains highly challenging. Existing anomaly detection algorithms based on a single data modality (i.e., metrics, logs, or traces) fail to fully account for the complex correlations and interactions between different modalities, leading to false negatives an...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Understanding the Effectiveness of Large Language Models in Detecting Security Vulnerabilities](../venues/arXiv2023/paper_6.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: While automated vulnerability detection techniques have made promising progress in detecting security vulnerabilities, their scalability and applicability remain challenging. The remarkable performance of Large Language Models (LLMs), such as GPT-4 and CodeLlama, on code-related tasks has prompted recent works to explore if LLMs can be used to detect vulnerabilities. In this paper, we perform a more comprehensive study by concurrently examining a higher number of datasets, languages and LLMs, an...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Utilizing Precise and Complete Code Context to Guide LLM in Automatic False Positive Mitigation](../venues/arXiv2024/paper_37.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Static Application Security Testing(SAST) tools are crucial for early bug detection and code quality but often generate false positives that slow development. Automating false positive mitigation is thus essential for advancing SAST tools. Past efforts use static/dynamic analysis or machine learning. The advent of Large Language Models, adept at understanding natural language and code, offers promising ways to improve the accuracy and usability of SAST tools. However, existing LLM-based methods ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [VALAR: Streamlining Alarm Ranking in Static Analysis with Value-Flow Assisted Active Learning](../venues/ASE2023/paper_15.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Static analyzers play a critical role in program defects and security vulnerabilities detection. Despite their importance, the widespread adoption of static analysis techniques in industrial development faces numerous obstacles, among which the high rate of false alarms constitutes a significant one. To address this issue, we propose a novel approach called Valar, which performs alarm ranking for advanced value-flow analysis using the active learning technique. Active learning algorithms minimiz...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [VGX: Large-Scale Sample Generation for Boosting Learning-Based Software Vulnerability Analyses](../venues/ICSE2024/paper_29.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Accompanying the successes of learning-based defensive software vulnerability analyses is the lack of large and quality sets of labeled vulnerable program samples, which impedes further advancement of those defenses. Existing automated sample generation approaches have shown potentials yet still fall short of practical expectations due to the high noise in the generated samples. This paper proposes VGX, a new technique aimed for large-scale generation of high-quality vulnerability datasets. Give...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [VULGEN: Realistic Vulnerability Generation Via Pattern Mining and Deep Learning](../venues/ICSE2023/paper_11.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Building new, powerful data-driven defenses against prevalent software vulnerabilities needs sizable, quality vulnerability datasets, so does large-scale benchmarking of existing defense solutions. Automatic data generation would promisingly meet the need, yet there is little work aimed to generate much-needed quality vulnerable samples. Meanwhile, existing similar and adaptable techniques suffer critical limitations for that purpose. In this paper, we present VULGEN, the first injection-based v...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [VulEval: Towards Repository-Level Evaluation of Software Vulnerability Detection](../venues/arXiv2024/paper_15.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Deep Learning (DL)-based methods have proven to be effective for software vulnerability detection, with a potential for substantial productivity enhancements for detecting vulnerabilities. Current methods mainly focus on detecting single functions (i.e., intra-procedural vulnerabilities), ignoring the more complex inter-procedural vulnerability detection scenarios in practice. For example, developers routinely engage with program analysis to detect vulnerabilities that span multiple functions wi...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [VulExplainer: A Transformer-Based Hierarchical Distillation for Explaining Vulnerability Types](../venues/TSE2023/paper_1.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: Deep learning-based vulnerability prediction approaches are proposed to help under-resourced security practitioners to detect vulnerable functions. However, security practitioners still do not know what type of vulnerabilities correspond to a given prediction (aka CWE-ID). Thus, a novel approach to explain the type of vulnerabilities for a given prediction is imperative. In this paper, we propose &lt;italic&gt;VulExplainer&lt;/italic&gt;, an approach to explain the type of vulnerabilities. We re...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Vulnerability Detection with Code Language Models: How Far Are We?](../venues/ICSE2025/paper_4.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: In the context of the rising interest in code language models (code LMs) and vulnerability detection, we study the effectiveness of code LMs for detecting vulnerabilities. Our analysis reveals significant shortcomings in existing vulnerability datasets, including poor data quality, low label accuracy, and high duplication rates, leading to unreliable model performance in realistic vulnerability detection scenarios. Additionally, the evaluation methods used with these datasets are not representat...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [When Threads Meet Interrupts: Effective Static Detection of Interrupt-Based Deadlocks in Linux](../venues/USENIXSec2024/paper_3.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: Deadlocking is an unresponsive state of software that arises when threads hold locks while trying to acquire other locks that are already held by other threads, resulting in a circular lock dependency. Interrupt-based deadlocks, a specific and prevalent type of deadlocks that occur within the OS kernel due to interrupt preemption, pose significant risks to system functionality, performance, and security. However, existing static analysis tools focus on resource-based deadlocks without characteri...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [specification inference](specification_inference.md)


- [Where is it? Tracing the Vulnerability-relevant Files from Vulnerability Reports](../venues/ICSE2024/paper_18.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: With the widely usage of open-source software, supply-chain-based vulnerability attacks, including SolarWind and Log4Shell, have posed significant risks to software security. Currently, people rely on vulnerability advisory databases or commercial software bill of materials (SBOM) to defend against potential risks. Unfortunately, these datasets do not provide finer-grained file-level vulnerability information, compromising their effectiveness. Previous works have not adequately addressed this is...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Who Judges the Judge: An Empirical Study on Online Judge Tests](../venues/ISSTA2023/paper_1.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Online Judge platforms play a pivotal role in education, competitive programming, recruitment, career training, and large language model training. They rely on predefined test suites to judge the correctness of submitted solutions. It is therefore important that the solution judgement is reliable and free from potentially misleading false positives (i.e., incorrect solutions that are judged as correct). In this paper, we conduct an empirical study of 939 coding problems with 541,552 solutions, a...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Your Instructions Are Not Always Helpful: Assessing the Efficacy of Instruction Fine-tuning for Software Vulnerability Detection](../venues/arXiv2024/paper_18.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Software, while beneficial, poses potential cybersecurity risks due to inherent vulnerabilities. Detecting these vulnerabilities is crucial, and deep learning has shown promise as an effective tool for this task due to its ability to perform well without extensive feature engineering. However, a challenge in deploying deep learning for vulnerability detection is the limited availability of training data. Recent research highlights the deep learning efficacy in diverse tasks. This success is attr...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [iSMELL: Assembling LLMs with Expert Toolsets for Code Smell Detection and Refactoring](../venues/ASE2024/paper_22.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Detecting and refactoring code smells is challenging, laborious, and sustaining. Although large language models have demonstrated potential in identifying various types of code smells, they also have limitations such as input-output token restrictions, difficulty in accessing repository-level knowledge, and performing dynamic source code analysis. Existing learning-based methods or commercial expert toolsets have advantages in handling complex smells. They can analyze project structures and cont...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [{DCE}-{LLM}: Dead Code Elimination with Large Language Models](../venues/NAACL2025/paper_8.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Dead code introduces several challenges in software development, such as increased binary size and maintenance difficulties. It can also obscure logical errors and be exploited for obfuscation in malware. For LLM-based code-related tasks, dead code introduces vulnerabilities that can mislead these models, raising security concerns. Although modern compilers and IDEs offer dead code elimination, sophisticated patterns can bypass these tools. A universal approach that includes classification, loca...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [program optimization](program_optimization.md)


## Program Verification

- [Automated Program Refinement: Guide and Verify Code Large Language Model with Refinement Calculus](../venues/POPL2025/paper_1.md), ([POPL2025](../venues/POPL2025/README.md))

  - **Abstract**: Recently, the rise of code-centric large language models (LLMs) appears to have reshaped the software engineering world with low-barrier tools like Copilot that can generate code easily. However, there is no correctness guarantee for the code generated by LLMs, which suffer from the hallucination problem, and their output is fraught with risks. Besides, the end-to-end process from specification to code through LLMs is a non-transparent and uncontrolled black box. This opacity makes it difficult ...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Baldur: Whole-Proof Generation and Repair with Large Language Models](../venues/FSE2023/paper_3.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Formally verifying software is a highly desirable but labor-intensive task.  Recent work has developed methods to automate formal verification using proof assistants, such as Coq and Isabelle/HOL, e.g., by training a model to predict one proof step at a time and using that model to search through the space of possible proofs.  This paper introduces a new method to automate formal verification: We use large language models, trained on natural language and code and fine-tuned on proofs, to generat...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Can ChatGPT support software verification?](../venues/FASE2024/paper_1.md), ([FASE2024](../venues/FASE2024/README.md))

  - **Abstract**: Large language models have become increasingly effective in software engineering tasks such as code generation, debugging and repair. Language models like ChatGPT can not only generate code, but also explain its inner workings and in particular its correctness. This raises the question whether we can utilize ChatGPT to support formal software verification....
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Can large language models reason about program invariants?](../venues/ICML2023/paper_3.md), ([ICML2023](../venues/ICML2023/README.md))

  - **Abstract**: Identifying invariants is an important program analysis task with applications towards program understanding, bug finding, vulnerability analysis, and formal verification. Existing tools for identifying program invariants rely on dynamic analysis, requiring traces collected from multiple executions in order to produce reliable invariants. We study the application of large language models to invariant prediction, finding that models trained on source code and fine-tuned for invariant generation c...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [ClassInvGen: Class Invariant Synthesis using Large Language Models](../venues/arXiv2025/paper_14.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Formal program specifications in the form of preconditions, postconditions, and class invariants have several benefits for the construction and maintenance of programs. They not only aid in program understanding due to their unambiguous semantics but can also be enforced dynamically (or even statically when the language supports a formal verifier). However, synthesizing high-quality specifications in an underlying programming language is limited by the expressivity of the specifications or the n...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Clause2Inv: A Generate-Combine-Check Framework for Loop Invariant Inference](../venues/ISSTA2025/paper_13.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Loop invariant inference is a fundamental, yet challenging, problem in program verification. Recent work adopts the guess-and-check framework, where candidate loop invariants are iteratively generated in the guess step and verified in the check step. A major challenge of this general framework is to produce high-quality candidate invariants in each iteration so that the inference procedure can converge quickly. Empirically, we observe that existing approaches may struggle with guessing the compl...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [CoqPilot, a plugin for LLM-based generation of proofs](../venues/ASE2024/paper_36.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: We present CoqPilot, a VS Code extension designed to help automate writing of Coq proofs. The plugin collects the parts of proofs marked with the admit tactic in a Coq file, i.e., proof holes, and combines LLMs along with non-machine-learning methods to generate proof candidates for the holes. Then, CoqPilot checks if each proof candidate solves the given subgoal and, if successful, replaces the hole with it. The focus of CoqPilot is twofold. Firstly, we want to allow users to seamlessly combine...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Enchanting program specification synthesis by large language models using static analysis and program verification](../venues/CAV2024/paper_1.md), ([CAV2024](../venues/CAV2024/README.md))

  - **Abstract**: Formal verification provides a rigorous and systematic approach to ensure the correctness and reliability of software systems. Yet, constructing specifications for the full proof relies on domain expertise and non-trivial manpower. In view of such needs, an automated approach for specification synthesis is desired. While existing automated approaches are limited in their versatility, i.e., they either focus only on synthesizing loop invariants for numerical programs, or are tailored for specific...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md), [specification inference](specification_inference.md)


- [Enhancing Automated Loop Invariant Generation for Complex Programs with Large Language Models](../venues/arXiv2024/paper_24.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Automated program verification has always been an important component of building trustworthy software. While the analysis of real-world programs remains a theoretical challenge, the automation of loop invariant analysis has effectively resolved the problem. However, real-world programs that often mix complex data structures and control flows pose challenges to traditional loop invariant generation tools. To enhance the applicability of invariant generation techniques, we proposed ACInv, an Auto...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Finding inductive loop invariants using large language models](../venues/arXiv2023/paper_11.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**:     Loop invariants are fundamental to reasoning about programs with loops. They establish properties about a given loop's behavior. When they additionally are inductive, they become useful for the task of formal verification that seeks to establish strong mathematical guarantees about program's runtime behavior. The inductiveness ensures that the invariants can be checked locally without consulting the entire program, thus are indispensable artifacts in a formal proof of correctness. Finding in...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Hypothesis search: Inductive reasoning with language models](../venues/ICLR2024/paper_2.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Inductive reasoning is a core problem-solving capacity: humans can identify underlying principles from a few examples, which can then be robustly generalized to novel scenarios. Recent work has evaluated large language models (LLMs) on inductive reasoning tasks by directly prompting them yielding "in context learning." This can work well for straightforward inductive tasks, but performs very poorly on more complex tasks such as the Abstraction and Reasoning Corpus (ARC). In this work, we propose...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md)


- [LLM Meets Bounded Model Checking: Neuro-symbolic Loop Invariant Inference](../venues/ASE2024/paper_7.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Loop invariant inference, a key component in program verification, is a challenging task due to the inherent undecidability and complex loop behaviors in practice. Recently, machine learning based techniques have demonstrated impressive performance in generating loop invariants automatically. However, these methods highly rely on the labeled training data, and are intrinsically random and uncertain, leading to unstable performance. In this paper, we investigate a synergy of large language models...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [LLM-Aided Automatic Modeling for Security Protocol Verification](../venues/ICSE2025/paper_56.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Symbolic protocol analysis serves as a pivotal technique for protocol design, security analysis, and the safeguarding of information assets. Several modern tools such as Tamarin and ProVerif have been proven successful in modeling and verifying real-world protocols, including complex protocols like TLS 1.3 and 5G AKA. However, developing formal models for protocol verification is a non-trivial task, which hinders the wide adoption of these powerful tools in practical protocol analysis. In this w...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [LLM-Generated Invariants for Bounded Model Checking Without Loop Unrolling](../venues/ASE2024/paper_23.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: We investigate a modification of the classical Bounded Model Checking (BMC) procedure that does not handle loops through unrolling but via modifications to the control flow graph (CFG). A portion of the CFG representing a loop is replaced by a node asserting invariants of the loop. We generate these invariants using Large Language Models (LLMs) and use a first-order theorem prover to ensure the correctness of the generated statements. We thus transform programs to loop-free variants in a sound m...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Large Language Models for Safe Minimization](../venues/ICSE2025/paper_57.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Several tasks in program analysis, verification, and testing are modeled as constraint solving problems, utilizing SMT solvers as the reasoning engine. In this work, we aim to investigate the reasoning capabilities of large language models (LLMs) toward reducing the size of an infeasible string constraint system by exploiting inter-constraint interactions such that the remaining ones are still unsatisfiable. We term this safe minimization. Motivated by preliminary observations of hallucination a...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Laurel: Unblocking Automated Verification with Large Language Models](../venues/OOPSLA2025/paper_3.md), ([OOPSLA2025](../venues/OOPSLA2025/README.md))

  - **Abstract**: Program verifiers such as Dafny automate proofs by outsourcing them to an SMT solver. This automation is not perfect, however, and the solver often requires hints in the form of assertions, creating a burden for the proof engineer. In this paper, we propose, a tool that alleviates this burden by automatically generating assertions using large language models (LLMs). To improve the success rate of LLMs in this task, we design two domain-specific prompting techniques. First, we help the LLM determ...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Lemur: Integrating large language models in automated program verification](../venues/ICLR2024/paper_6.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: The demonstrated code-understanding capability of LLMs raises the question of whether they can be used for automated program verification, a task that typically demands high-level abstract reasoning about program properties that is challenging for verification tools. We propose a general methodology to combine the power of LLMs and automated reasoners for automated program verification. We formally describe this methodology as a set of derivation rules and prove its soundness. We instantiate the...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Leveraging LLMs for Program Verification](../venues/FMCAD2024/paper_1.md), ([FMCAD2024](../venues/FMCAD2024/README.md))

  - **Abstract**: Loop invariants are fundamental to reasoning about programs with loops. They establish properties about a given loop’s behavior. When they additionally are inductive, they become useful for the task of formal verification that seeks to establish strong mathematical guarantees about program’s runtime behavior. The inductiveness ensures that the invariants can be checked locally without consulting the entire program, thus are indispensable artifacts in a formal proof of correctness. Finding induct...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [PropertyGPT: LLM-driven Formal Verification of Smart Contracts through Retrieval-Augmented Property Generation](../venues/NDSS2025/paper_8.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: Formal verification is a technique that can prove the correctness of a system with respect to a certain specification or property. It is especially valuable for security-sensitive smart contracts that manage billions in cryptocurrency assets. Although existing research has developed various static verification tools (or provers) for smart contracts, a key missing component is theautomated generation of comprehensive properties, including invariants, pre-/post-conditions, and rules. Hence, indust...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [program verification](program_verification.md)


- [QEDCartographer: Automating Formal Verification Using Reward-Free Reinforcement Learning](../venues/ICSE2025/paper_3.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Formal verification is a promising method for producing reliable software, but the difficulty of manually writing verification proofs severely limits its utility in practice. Recent methods have automated some proof synthesis by guiding a search through the proof space using a theorem prover. Unfortunately, the theorem prover provides only the crudest estimate of progress, resulting in effectively undirected search. To address this problem, we create QEDCartographer, an automated proof-synthesis...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Ranking llm-generated loop invariants for program verification](../venues/EMNLP2023/paper_13.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Synthesizing inductive loop invariants is fundamental to automating program verification. In this work, we observe that Large Language Models (such as gpt-3.5 or gpt-4) are capable of synthesizing loop invariants for a class of programs in a 0-shot setting, yet require several samples to generate the correct invariants. This can lead to a large number of calls to a program verifier to establish an invariant. To address this issue, we propose a {\it re-ranking} approach for the generated results ...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [sampling and ranking](sampling_and_ranking.md)


- [SpecGen: Automated Generation of Formal Program Specifications via Large Language Models](../venues/ICSE2025/paper_7.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: In the software development process, formal program specifications play a crucial role in various stages, including requirement analysis, software testing, and verification. However, manually crafting formal program specifications is rather difficult, making the job time-consuming and labor-intensive. Moreover, it is even more challenging to write specifications that correctly and comprehensively describe the semantics of complex programs. To reduce the burden on software developers, automated s...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md), [program verification](program_verification.md)


- [Towards AI-Assisted Synthesis of Verified Dafny Methods](../venues/FSE2024/paper_23.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Large language models show great promise in many domains, including programming. A promise is easy to make but hard to keep, and language models often fail to keep their promises, generating erroneous code. A promising avenue to keep models honest is to incorporate formal verification: generating programs’ specifications as well as code so that the code can be proved correct with respect to the specifications. Unfortunately, existing large language models show a severe lack of proficiency in ver...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Towards General Loop Invariant Generation: A Benchmark of Programs with Memory Manipulation](../venues/NeurIPS2024/paper_7.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Program verification is vital for ensuring software reliability, especially in the context of increasingly complex systems. Loop invariants, remaining true before and after each iteration of loops, are crucial for this verification process. Traditional provers and machine learning based methods for generating loop invariants often require expert intervention or extensive labeled data, and typically only handle numerical property verification. These methods struggle with programs involving comple...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md), [benchmark](benchmark.md)


- [Towards Neural Synthesis for SMT-Assisted Proof-Oriented Programming](../venues/ICSE2025/paper_8.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Proof-oriented programs mix computational content with proofs of program correctness. However, the human effort involved in programming and proving is still substantial, despite the use of Satisfiability Modulo Theories (SMT) solvers to automate proofs in languages such as F*. Seeking to spur research on using AI to automate the construction of proof-oriented programs, we curate a dataset of 600K lines of open-source F* programs and proofs, including software used in production systems ranging f...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)


- [VERT: Verified Equivalent Rust Transpilation with Large Language Models as Few-Shot Learners](../venues/arXiv2024/paper_34.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Rust is a programming language that combines memory safety and low-level control, providing C-like performance while guaranteeing the absence of undefined behaviors by default. Rust's growing popularity has prompted research on safe and correct transpiling of existing code-bases to Rust. Existing work falls into two categories: rule-based and large language model (LLM)-based. While rule-based approaches can theoretically produce correct transpilations that maintain input-output equivalence to th...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Verified Code Transpilation with LLMs](../venues/NeurIPS2024/paper_4.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Domain-specific languages (DSLs) are integral to various software workflows. Such languages offer domain-specific optimizations and abstractions that improve code readability and maintainability. However, leveraging these languages requires developers to rewrite existing code using the specific DSL's API. While large language models (LLMs) have shown some success in automatic code transpilation, none of them provide any functional correctness guarantees on the transpiled code. Another approach f...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md)


## Program Optimization

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


- [Search-Based LLMs for Code Optimization](../venues/ICSE2025/paper_13.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: The code written by developers usually suffers from efficiency problems and contain various performance bugs. These inefficiencies necessitate the research of automated refactoring methods for code optimization. Early research in code optimization employs rule-based methods and focuses on specific inefficiency issues, which are labor-intensive and suffer from the low coverage issue. Recent work regards the task as a sequence generation problem, and resorts to deep learning (DL) techniques such a...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [static analysis](static_analysis.md), [program optimization](program_optimization.md)


- [{DCE}-{LLM}: Dead Code Elimination with Large Language Models](../venues/NAACL2025/paper_8.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Dead code introduces several challenges in software development, such as increased binary size and maintenance difficulties. It can also obscure logical errors and be exploited for obfuscation in malware. For LLM-based code-related tasks, dead code introduces vulnerabilities that can mislead these models, raising security concerns. Although modern compilers and IDEs offer dead code elimination, sophisticated patterns can bypass these tools. A universal approach that includes classification, loca...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [program optimization](program_optimization.md)


## Code Summarization

- [Automatic Semantic Augmentation of Language Model Prompts (for Code Summarization)](../venues/ICSE2024/paper_19.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Large Language Models (LLM) are a new class of computation engines, "programmed" via prompt engineering. Researchers are still learning how to best "program" these LLMs to help developers. We start with the intuition that developers tend to consciously and unconsciously collect semantics facts, from the code, while working. Mostly these are shallow, simple facts arising from a quick read. For a function, such facts might include parameter and local variable names, return expressions, simple pre-...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [BinQuery: A Novel Framework for Natural Language-Based Binary Code Retrieval](../venues/ISSTA2025/paper_15.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Binary Function Retrieval (BFR) is crucial in reverse engineering for identifying specific functions in binary code, especially those associated with malicious behavior or vulnerabilities. Traditional BFR methods rely on heuristics, often lacking the efficiency and adaptability needed for large-scale or diverse binary analysis tasks. To address these challenges, we present BinQuery, a Natural Language-based BFR (NL-based BFR) framework that uses natural language queries to retrieve relevant bina...
  - **Labels**: [static analysis](static_analysis.md), [code search](code_search.md), [code summarization](code_summarization.md)


- [Calibration of Large Language Models on Code Summarization](../venues/FSE2025/paper_38.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: A brief, fluent, and relevant summary can be helpful during program comprehension; however, such a summary does require significant human effort to produce. Often, good summaries are unavailable in software projects, which makes maintenance more difficult. There has been a considerable body of research into automated AI-based methods, using Large Language models (LLMs), to generate summaries of code; there also has been quite a bit of work on ways to measure the performance of such summarization...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md)


- [CoSS: Leveraging Statement Semantics for Code Summarization](../venues/TSE2023/paper_4.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: Automated code summarization tools allow generating descriptions for code snippets in natural language, which benefits software development and maintenance. Recent studies demonstrate that the quality of generated summaries can be improved by using additional code representations beyond token sequences. The majority of contemporary approaches mainly focus on extracting code syntactic and structural information from abstract syntax trees (ASTs). However, from the view of macro-structures, it is c...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Code Structure–Guided Transformer for Source Code Summarization](../venues/TOSEM2023/paper_3.md), ([TOSEM2023](../venues/TOSEM2023/README.md))

  - **Abstract**: Code summaries help developers comprehend programs and reduce their time to infer the program functionalities during software maintenance. Recent efforts resort to deep learning techniques such as sequence-to-sequence models for generating accurate code summaries, among which Transformer-based approaches have achieved promising performance. However, effectively integrating the code structure information into the Transformer is under-explored in this task domain. In this article, we propose a nov...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md)


- [Enhanced Prompting Framework for Code Summarization with Large Language Models](../venues/ISSTA2025/paper_25.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Code summarization is essential for enhancing the efficiency of software development, enabling developers to swiftly comprehend and maintain software projects. Recent efforts utilizing large language models for generating precise code summaries have shown promising performance, primarily due to their advanced generative capabilities. LLMs that employ continuous prompting techniques can explore a broader problem space, potentially unlocking greater capabilities. However, they also present specifi...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md)


- [Enhancing Vulnerability Detection via Inter-procedural Semantic Completion](../venues/ISSTA2025/paper_11.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Inspired by advances in deep learning, numerous learning-based approaches for vulnerability detection have emerged, primarily operating at the function level for scalability. However, this design choice has a critical limitation: many vulnerabilities span multiple functions, causing function-level approaches to lose the semantics of called functions and fail to capture true vulnerability patterns. To address this issue, we propose VulnSC, a novel framework designed to enhance learning-based appr...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code summarization](code_summarization.md)


- [EyeTrans: Merging Human and Machine Attention for Neural Code Summarization](../venues/FSE2024/paper_30.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Neural code summarization leverages deep learning models to automatically generate brief natural language summaries of code snippets. The development of Transformer models has led to extensive use of attention during model design. While existing work has primarily and almost exclusively focused on static properties of source code and related structural representations like the Abstract Syntax Tree (AST), few studies have considered human attention — that is, where programmers focus while examini...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [empirical study](empirical_study.md)


- [Hierarchical Repository-Level Code Summarization for Business Applications Using Local LLMs](../venues/arXiv2025/paper_25.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: In large-scale software development, understanding the functionality and intent behind complex codebases is critical for effective development and maintenance. While code summarization has been widely studied, existing methods primarily focus on smaller code units, such as functions, and struggle with larger code artifacts like files and packages. Additionally, current summarization models tend to emphasize low-level implementation details, often overlooking the domain and business context that ...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [Intention is All you Need: Refining your Code from your Intention](../venues/ICSE2025/paper_55.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Code refinement aims to enhance existing code by addressing issues, refactoring, and optimizing to improve quality and meet specific requirements. As software projects scale in size and complexity, the traditional iterative exchange between re-viewers and developers becomes increasingly burdensome. While recent deep learning techniques have been explored to accelerate this process, their performance remains limited, primarily due to challenges in accurately understanding reviewers' intents. This...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [code summarization](code_summarization.md)


- [Learning to Generate Structured Code Summaries From Hybrid Code Context](../venues/TSE2024/paper_11.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Code summarization aims to automatically generate natural language descriptions for code, and has become a rapidly expanding research area in the past decades. Unfortunately, existing approaches mainly focus on the “one-to-one” mapping from methods to short descriptions, which hinders them from becoming practical tools: 1) The program context is ignored, so they have difficulty in predicting labels outside the target method; 2) They are typically trained to generate brief function descriptions w...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [benchmark](benchmark.md)


- [LiSSA: Toward Generic Traceability Link Recovery Through Retrieval- Augmented Generation](../venues/ICSE2025/paper_54.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: There are a multitude of software artifacts which need to be handled during the development and maintenance of a software system. These artifacts interrelate in multiple, complex ways. Therefore, many software engineering tasks are enabled - and even empowered - by a clear understanding of artifact interrelationships and also by the continued advancement of techniques for automated artifact linking. However, current approaches in automatic Traceability Link Recovery (TLR) target mostly the links...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [static analysis](static_analysis.md), [code summarization](code_summarization.md), [code search](code_search.md)


- [Natural Is the Best: Model-Agnostic Code Simplification for Pre-trained Large Language Models](../venues/FSE2024/paper_17.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Pre-trained Large Language Models (LLM) have achieved remarkable successes in several domains. However, code-oriented LLMs are often heavy in computational complexity, and quadratically with the length of the input code sequence. Toward simplifying the input program of an LLM, the state-of-the-art approach has the strategies to filter the input code tokens based on the attention scores given by the LLM. The decision to simplify the input program should not rely on the attention patterns of an LL...
  - **Labels**: [static analysis](static_analysis.md), [code search](code_search.md), [code summarization](code_summarization.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [RACONTEUR: A Knowledgeable, Insightful, and Portable LLM-Powered Shell Command Explainer](../venues/NDSS2025/paper_2.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: Malicious shell commands are linchpins to many cyber-attacks, but may not be easy to understand by security analysts due to complicated and often disguised code structures. Advances in large language models (LLMs) have unlocked the possibility of generating understandable explanations for shell commands. However, existing general-purpose LLMs suffer from a lack of expert knowledge and a tendency to hallucinate in the task of shell command explanation. In this paper, we present Raconteur, a knowl...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [SimLLM: Calculating Semantic Similarity in Code Summaries using a Large Language Model-Based Approach](../venues/FSE2024/paper_4.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Code summaries are pivotal in software engineering, serving to improve code readability, maintainability, and collaboration. While recent advancements in Large Language Models (LLMs) have opened new avenues for automatic code summarization, existing metrics for evaluating summary quality, such as BLEU and BERTScore, have notable limitations. Specifically, these existing metrics either fail to capture the nuances of semantic meaning in summaries or are further limited in understanding domain-spec...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md)


- [Source Code Summarization in the Era of Large Language Models](../venues/ICSE2025/paper_18.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: To support software developers in understanding and maintaining programs, various automatic (source) code summarization techniques have been proposed to generate a concise natural language summary (i.e., comment) for a given code snippet. Recently, the emergence of large language models (LLMs) has led to a great boost in the performance of coderelated tasks. In this paper, we undertake a systematic and comprehensive study on code summarization in the era of LLMs, which covers multiple aspects in...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [empirical study](empirical_study.md)


- [Understanding Code Changes Practically with Small-Scale Language Models](../venues/ASE2024/paper_3.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Recent studies indicate that traditional techniques for understanding code changes are not as effective as techniques that directly prompt language models (LMs). However, current LM-based techniques heavily rely on expensive, large LMs (LLMs) such as GPT-4 and Llama-13b, which are either commercial or prohibitively costly to deploy on a wide scale, thereby restricting their practical applicability. This paper explores the feasibility of deploying small LMs (SLMs) while maintaining comparable or ...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


## Code Search

- [BinQuery: A Novel Framework for Natural Language-Based Binary Code Retrieval](../venues/ISSTA2025/paper_15.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Binary Function Retrieval (BFR) is crucial in reverse engineering for identifying specific functions in binary code, especially those associated with malicious behavior or vulnerabilities. Traditional BFR methods rely on heuristics, often lacking the efficiency and adaptability needed for large-scale or diverse binary analysis tasks. To address these challenges, we present BinQuery, a Natural Language-based BFR (NL-based BFR) framework that uses natural language queries to retrieve relevant bina...
  - **Labels**: [static analysis](static_analysis.md), [code search](code_search.md), [code summarization](code_summarization.md)


- [LiSSA: Toward Generic Traceability Link Recovery Through Retrieval- Augmented Generation](../venues/ICSE2025/paper_54.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: There are a multitude of software artifacts which need to be handled during the development and maintenance of a software system. These artifacts interrelate in multiple, complex ways. Therefore, many software engineering tasks are enabled - and even empowered - by a clear understanding of artifact interrelationships and also by the continued advancement of techniques for automated artifact linking. However, current approaches in automatic Traceability Link Recovery (TLR) target mostly the links...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [static analysis](static_analysis.md), [code summarization](code_summarization.md), [code search](code_search.md)


- [Natural Is the Best: Model-Agnostic Code Simplification for Pre-trained Large Language Models](../venues/FSE2024/paper_17.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Pre-trained Large Language Models (LLM) have achieved remarkable successes in several domains. However, code-oriented LLMs are often heavy in computational complexity, and quadratically with the length of the input code sequence. Toward simplifying the input program of an LLM, the state-of-the-art approach has the strategies to filter the input code tokens based on the attention scores given by the LLM. The decision to simplify the input program should not rely on the attention patterns of an LL...
  - **Labels**: [static analysis](static_analysis.md), [code search](code_search.md), [code summarization](code_summarization.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [On the Effectiveness of Transfer Learning for Code Search](../venues/TSE2023/paper_6.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: The Transformer architecture and transfer learning have marked a quantum leap in natural language processing, improving the state of the art across a range of text-based tasks. This paper examines how these advancements can be applied to and improve code search. To this end, we pre-train a BERT-based model on combinations of natural language and source code data and fine-tune it on pairs of StackOverflow question titles and code answers. Our results show that the pre-trained models consistently ...
  - **Labels**: [static analysis](static_analysis.md), [code search](code_search.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Self-Supervised Query Reformulation for Code Search](../venues/FSE2023/paper_9.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Automatic query reformulation is a widely utilized technology for enriching user requirements and enhancing the outcomes of code search. It can be conceptualized as a machine translation task, wherein the objective is to rephrase a given query into a more comprehensive alternative. While showing promising results, training such a model typically requires a large parallel corpus of query pairs (i.e., the original query and a reformulated query) that are confidential and unpublished by online code...
  - **Labels**: [static analysis](static_analysis.md), [code search](code_search.md)


- [Survey of Code Search Based on Deep Learning](../venues/TOSEM2024/paper_10.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Code writing is repetitive and predictable, inspiring us to develop various code intelligence techniques. This survey focuses on code search, that is, to retrieve code that matches a given natural language query by effectively capturing the semantic similarity between the query and code. Deep learning, being able to extract complex semantics information, has achieved great success in this field. Recently, various deep learning methods, such as graph neural networks and pretraining models, have b...
  - **Labels**: [survey](survey.md), [static analysis](static_analysis.md), [code search](code_search.md)


- [Virtual Compiler Is All You Need For Assembly Code Search](../venues/ACL2024/paper_11.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Assembly code search is vital for reducing the burden on reverse engineers, allowing them to quickly identify specific functions using natural language within vast binary programs.Despite its significance, this critical task is impeded by the complexities involved in building high-quality datasets. This paper explores training a Large Language Model (LLM) to emulate a general compiler. By leveraging Ubuntu packages to compile a dataset of 20 billion tokens, we further continue pre-train CodeLlam...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [static analysis](static_analysis.md), [code search](code_search.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Zero-Shot Cross-Domain Code Search without Fine-Tuning](../venues/FSE2025/paper_26.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Code search is a crucial task in software engineering, aiming to retrieve code snippets that are semantically relevant to a natural language query. Recently, Pre-trained Language Models (PLMs) have shown remarkable success and are widely adopted for code search tasks. However, PLM-based methods often struggle in cross-domain scenarios. When applied to a new domain, they typically require extensive fine-tuning with substantial data. Even worse, the data scarcity problem in new domains often force...
  - **Labels**: [static analysis](static_analysis.md), [code search](code_search.md)


## Software Composition Analysis

- [BinaryAI: Binary Software Composition Analysis via Intelligent Binary Source Code Matching](../venues/ICSE2024/paper_31.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: While third-party libraries (TPLs) are extensively reused to enhance productivity during software development, they can also introduce potential security risks such as vulnerability propagation. Software composition analysis (SCA), proposed to identify reused TPLs for reducing such risks, has become an essential procedure within modern DevSecOps. As one of the mainstream SCA techniques, binary-to-source SCA identifies the third-party source projects contained in binary files via binary source co...
  - **Labels**: [static analysis](static_analysis.md), [software composition analysis](software_composition_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [Can Large Language Models Comprehend Code Stylometry?](../venues/ASE2024/paper_39.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Code Authorship Attribution (CAA) has several applications such as copyright disputes, plagiarism detection and criminal prosecution. Existing studies mainly focused on CAA by proposing machine learning (ML) and Deep Learning (DL) based techniques. The main limitations of ML-based techniques are (a) manual feature engineering is required to train these models and (b) they are vulnerable to adversarial attack. In this study, we initially fine-tune five Large Language Models (LLMs) for CAA and eva...
  - **Labels**: [static analysis](static_analysis.md), [software composition analysis](software_composition_analysis.md)


- [Maltracker: A Fine-Grained NPM Malware Tracker Copiloted by LLM-Enhanced Dataset](../venues/ISSTA2024/paper_24.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: As the largest package registry, Node Package Manager (NPM) has become the prime target for various supply chain attacks recently and has been flooded with numerous malicious packages, posing significant security risks to end-users. Learning-based methods have demonstrated promising performance with good adaptability to various types of attacks. However, they suffer from two main limitations. First, they often utilize metadata features or coarse-grained code features extracted at the package lev...
  - **Labels**: [static analysis](static_analysis.md), [software composition analysis](software_composition_analysis.md)


