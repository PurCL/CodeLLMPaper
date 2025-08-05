# Benchmark

## Agent Design

- [AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](../venues/ACL2024/paper_6.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Autonomous agents that address day-to-day digital tasks (e.g., ordering groceries for a household), must not only operate multiple apps (e.g., notes, messaging, shopping app) via APIs, but also generate rich code with complex control flow in an iterative manner based on their interaction with the environment. However, existing benchmarks for tool use are inadequate, as they only cover tasks that require a simple sequence of API calls. To remedy this gap, we built AppWorld Engine, a high-quality ...
  - **Labels**: [benchmark](benchmark.md), [agent design](agent_design.md)

## Code Generation

- [Are “Solved Issues” in SWE-bench Really Solved Correctly?](../venues/arXiv2025/paper_15.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Automated issue solving aims to resolve real-world issues in software repositories. The most popular benchmarks for automated issue solving are SWE-bench and its human-filtered subset SWE-bench Verified. These benchmarks leverage testing to validate generated patches. However, because testing is rarely exhaustive, a patch may pass the tests but nevertheless fail to match the developers' expectations. Unfortunately, it is currently unclear to what extent evaluations performed with SWE-bench suffe...
  - **Labels**: [benchmark](benchmark.md), [code generation](code_generation.md), [program repair](program_repair.md)

- [Benchmarking Automated Program Repair: An Extensive Study on Both Real-World and Artificial Bugs](../venues/ISSTA2024/paper_7.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: As bugs are inevitable and prevalent in real-world programs, many Automated Program Repair (APR) techniques have been proposed to generate patches for them. However, due to the lack of a standard for evaluating APR techniques, prior works tend to use different settings and benchmarks in evaluation, threatening the trustworthiness of the evaluation results. Additionally, they typically only adopt plausibility and genuineness as evaluation metrics, which may potentially mask some underlying issues...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)

- [Benchmarking Language Model Creativity: A Case Study on Code Generation](../venues/NAACL2025/paper_4.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: As LLMs become increasingly prevalent, it is interesting to consider how ``creative'' these models can be. From cognitive science, creativity consists of at least two key characteristics: \textit{convergent} thinking (purposefulness to achieve a given goal) and \textit{divergent} thinking (adaptability to explore new environments or constraints) (CITATION). In this work, we introduce a framework for quantifying LLM creativity that incorporates the two design ingredients: (1) We introduce DENIAL ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)

- [Benchmarking and Improving Text-to-SQL Generation under Ambiguity](../venues/EMNLP2023/paper_3.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Research in Text-to-SQL conversion has been largely benchmarked against datasets where each text query corresponds to one correct SQL. However, natural language queries over real-life databases frequently involve significant ambiguity about the intended SQL due to overlapping schema names and multiple confusing relationship paths. To bridge this gap, we develop a novel benchmark called AmbiQT with over 3000 examples where each text is interpretable as two plausible SQLs due to lexical and/or str...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)

- [CRUST-Bench: A Comprehensive Benchmark for C-to-safe-Rust Transpilation](../venues/arXiv2025/paper_6.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: C-to-Rust transpilation is essential for modernizing legacy C code while enhancing safety and interoperability with modern Rust ecosystems. However, no dataset currently exists for evaluating whether a system can transpile C into safe Rust that passes a set of test cases. We introduce CRUST-Bench, a dataset of 100 C repositories, each paired with manually-written interfaces in safe Rust as well as test cases that can be used to validate correctness of the transpilation. By considering entire rep...
  - **Labels**: [benchmark](benchmark.md), [code generation](code_generation.md), [program transformation](program_transformation.md)

- [CoCoST: Automatic Complex Code Generation with Online Searching and Correctness Testing](../venues/EMNLP2024/paper_34.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large Language Models have revolutionized code generation ability by converting natural language descriptions into executable code. However, generating complex code within real-world scenarios remains challenging due to intricate structures, subtle bugs, understanding of advanced data types, and lack of supplementary contents. To address these challenges, we introduce the CoCoST framework, which enhances complex code generation by online searching for more information with planned queries and co...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)

- [CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges](../venues/ACL2024/paper_3.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have shown promise in automated code generation but typically excel only in simpler tasks such as generating standalone code units. However, real-world software development often involves complex code repositories with complex dependencies and extensive documentation. To enable LLMs to handle these realworld repo-level code generation, we present CodeAgent, a novel LLM-based agent framework that employs external tools for effective repo-level code generation. CodeAge...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)

- [CodeBenchGen: Creating Scalable Execution-based Code Generation Benchmarks](../venues/arXiv2024/paper_9.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: To facilitate evaluation of code generation systems across diverse scenarios, we present CodeBenchGen, a framework to create scalable execution-based benchmarks that only requires light guidance from humans. Specifically, we leverage a large language model (LLM) to convert an arbitrary piece of code into an evaluation example, including test cases for execution-based evaluation. We illustrate the usefulness of our framework by creating a dataset, Exec-CSN, which includes 1,931 examples involving...
  - **Labels**: [code generation](code_generation.md), [benchmark](benchmark.md)

- [CoderUJB: An Executable and Unified Java Benchmark for Practical Programming Scenarios](../venues/ISSTA2024/paper_3.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: In the evolving landscape of large language models (LLMs) tailored for software engineering, the need for benchmarks that accurately reflect real-world development scenarios is paramount. Current benchmarks are either too simplistic or fail to capture the multi-tasking nature of software development. To address this, we introduce CoderUJB, a new benchmark designed to evaluate LLMs across diverse Java programming tasks that are executable and reflective of actual development scenarios, acknowledg...
  - **Labels**: [code generation](code_generation.md), [program testing](program_testing.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)

- [Coffee-Gym: An Environment for Evaluating and Improving Natural Language Feedback on Erroneous Code](../venues/EMNLP2024/paper_38.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: This paper presents Coffee-Gym, a comprehensive RL environment for training models that provide feedback on code editing. Coffee-Gym includes two major components: (1) Coffee, a dataset containing humans’ code edit traces for coding questions and human-written feedback for editing erroneous code; (2) CoffeeEval, a reward function that faithfully reflects the helpfulness of feedback by assessing the performance of the revised code in unit tests. With them, Coffee-Gym addresses the unavailability ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)

- [DA-Code: Agent Data Science Code Generation Benchmark for Large Language Models](../venues/EMNLP2024/paper_28.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: We introduce DA-Code, a code generation benchmark specifically designed to assess LLMs on agent-based data science tasks. This benchmark features three core elements: First, the tasks within DA-Code are inherently challenging, setting them apart from traditional code generation tasks and demanding advanced coding skills in grounding and planning. Second, examples in DA-Code are all based on real and diverse data, covering a wide range of complex data wrangling and analytics tasks. Third, to solv...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)

- [Evaluating Large Language Models in Class-Level Code Generation](../venues/ICSE2024/paper_9.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Recently, many large language models (LLMs) have been proposed, showing advanced proficiency in code generation. Meanwhile, many efforts have been dedicated to evaluating LLMs on code generation benchmarks such as HumanEval. Although being very helpful for comparing different LLMs, existing evaluation focuses on a simple code generation scenario (i.e., function-level or statement-level code generation), which mainly asks LLMs to generate one single code unit (e.g., a function or a statement) for...
  - **Labels**: [code generation](code_generation.md), [benchmark](benchmark.md)

- [EvoCodeBench: An Evolving Code Generation Benchmark Aligned with Real-World Code Repositories](../venues/arXiv2024/paper_8.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: How to evaluate Large Language Models (LLMs) in code generation is an open question. Existing benchmarks demonstrate poor alignment with real-world code repositories and are insufficient to evaluate the coding abilities of LLMs. This paper proposes a new benchmark - EvoCodeBench to address the preceding problems, which has three primary advances. (1) EvoCodeBench aligns with real-world repositories in multiple dimensions, e.g., code distributions and dependency distributions. (2) EvoCodeBench of...
  - **Labels**: [benchmark](benchmark.md), [code generation](code_generation.md)

- [Follow-Up Attention: An Empirical Study of Developer and Neural Model Code Exploration](../venues/TSE2024/paper_12.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Recent neural models of code, such as OpenAI Codex and AlphaCode, have demonstrated remarkable proficiency at code generation due to the underlying attention mechanism. However, it often remains unclear how the models actually process code, and to what extent their reasoning and the way their attention mechanism scans the code matches the patterns of developers. A poor understanding of the model reasoning process limits the way in which current neural models are leveraged today, so far mostly fo...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [benchmark](benchmark.md)

- [How Effective Are Neural Networks for Fixing Security Vulnerabilities](../venues/ISSTA2023/paper_3.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Security vulnerability repair is a difficult task that is in dire need of automation. Two groups of techniques have shown promise: (1) large code language models (LLMs) that have been pre-trained on source code for tasks such as code completion, and (2) automated program repair (APR) techniques that use deep learning (DL) models to automatically fix software bugs. This paper is the first to study and compare Java vulnerability repair capabilities of LLMs and DL-based APR models. The contribution...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)

- [HumanEvo: An Evolution-Aware Benchmark for More Realistic Evaluation of Repository-Level Code Generation](../venues/ICSE2025/paper_62.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: To evaluate the repository-level code generation capabilities of Large Language Models (LLMs) in complex real-world software development scenarios, many evaluation methods have been developed. These methods typically leverage contextual code from the latest version of a project to assist LLMs in accurately generating the desired function. However, such evaluation methods fail to consider the dynamic evolution of software projects over time, which we refer to as evolution-ignored settings. This i...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md), [benchmark](benchmark.md)

- [JavaBench: A Benchmark of Object-Oriented Code Generation for Evaluating Large Language Models](../venues/ASE2024/paper_17.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Code generation benchmarks such as HumanEval are widely adopted to evaluate LLMs' capabilities. However, after consolidating the latest 24 benchmarks, we noticed three significant imbalances. First, imbalanced programming language. 95.8\% of benchmarks involve Python, while only 5 benchmarks involve Java, resulting in an insufficient understanding of LLMs' capability to generate Java code. Second, imbalanced code granularity. Function-/statement-level benchmarks account for over 83.3\% of benchm...
  - **Labels**: [benchmark](benchmark.md), [code generation](code_generation.md), [program synthesis](program_synthesis.md)

- [Language-to-Code Translation with a Single Labeled Example](../venues/EMNLP2024/paper_23.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Tools for translating natural language into code promise natural, open-ended interaction with databases, web APIs, and other software systems. However, this promise is complicated by the diversity and continual development of these systems, each with its own interface and distinct set of features. Building a new language-to-code translator, even starting with a large language model (LM), typically requires annotating a large set of natural language commands with their associated programs. In thi...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)

- [MultiPL-E: A Scalable and Polyglot Approach to Benchmarking Neural Code Generation](../venues/TSE2023/paper_3.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: Large language models have demonstrated the ability to generate both natural language and programming language text. Although contemporary code generation models are trained on corpora with several programming languages, they are tested using benchmarks that are typically monolingual. The most widely used code generation benchmarks only target Python, so there is little quantitative evidence of how code generation models perform on other programming languages. We propose MultiPL-E, a system for ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)

- [Multitask Pretraining with Structured Knowledge for Text-to-SQL Generation](../venues/ACL2023/paper_9.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Many machine learning-based low-code or no-code applications involve generating code that interacts with structured knowledge. For example, one of the most studied tasks in this area is generating SQL code from a natural language statement. Prior work shows that incorporating context information from the database schema, such as table and column names, is beneficial to model performance on this task. In this work we present a large pretraining dataset and strategy for learning representations of...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)

- [On Leakage of Code Generation Evaluation Datasets](../venues/EMNLP2024/paper_15.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: In this paper, we consider contamination by code generation test sets, in particular in their use in modern large language models.We discuss three possible sources of such contamination and show findings supporting each of them: (i) direct data leakage, (ii) indirect data leakage through the use of synthetic data and (iii) overfitting to evaluation sets during model selection.To address this, we release Less Basic Python Problems (LBPP): an uncontaminated new benchmark of 161 prompts with their ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)

- [PythonSaga: Redefining the Benchmark to Evaluate Code Generating LLMs](../venues/EMNLP2024/paper_22.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Driven by the surge in code generation using large language models (LLMs), numerous benchmarks have emerged to evaluate these LLMs capabilities. We conducted a large-scale human evaluation of *HumanEval* and *MBPP*, two popular benchmarks for Python code generation, analyzing their diversity and difficulty. Our findings unveil a critical bias towards a limited set of programming concepts, neglecting most of the other concepts entirely. Furthermore, we uncover a worrying prevalence of easy tasks ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)

- [RMCBench: Benchmarking Large Language Models' Resistance to Malicious Code](../venues/ASE2024/paper_18.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Warning: Please note that this article contains potential harmful or offensive content. This content is only for the evaluating and analysis of LLMs and does not imply any intention to promote criminal activities.The emergence of Large Language Models (LLMs) has significantly influenced various aspects of software development activities. Despite their benefits, LLMs also pose notable risks, including the potential to generate harmful content and being abused by malicious developers to create mal...
  - **Labels**: [code generation](code_generation.md), [benchmark](benchmark.md), [code model](code_model.md), [code model robustness](code_model_robustness.md)

- [SecCodePLT: A Unified Platform for Evaluating the Security of Code GenAI](../venues/arXiv2024/paper_3.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Language models for code (CodeLMs) have emerged as powerful tools for code-related tasks, outperforming traditional methods and standard machine learning approaches. However, these models are susceptible to security vulnerabilities, drawing increasing research attention from domains such as software engineering, artificial intelligence, and cybersecurity. Despite the growing body of research focused on the security of CodeLMs, a comprehensive survey in this area remains absent. To address this g...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model security](code_model_security.md), [benchmark](benchmark.md)

- [Self-Edit: Fault-Aware Code Editor for Code Generation](../venues/ACL2023/paper_1.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated an impressive ability to generate codes on competitive programming tasks. However, with limited sample numbers, LLMs still suffer from poor accuracy. Inspired by the process of human programming, we propose a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task. We execute the generated code on the example test case provided in the q...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)

- [Statically Contextualizing Large Language Models with Typed Holes](../venues/OOPSLA2024/paper_1.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Large language models (LLMs) have reshaped the landscape of program synthesis. However, contemporary LLM-based code completion systems often hallucinate broken code because they lack appropriate code context, particularly when working with definitions that are neither in the training data nor near the cursor. This paper demonstrates that tighter integration with the type and binding structure of the programming language in use, as exposed by its language server, can help address this contextuali...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [Swe-bench: Can language models resolve real-world github issues?](../venues/ICLR2024/paper_1.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Language models have outpaced our ability to evaluate them effectively, but for their future development it is essential to study the frontier of their capabilities. We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language models. To this end, we introduce SWE-bench, an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popul...
  - **Labels**: [benchmark](benchmark.md), [code generation](code_generation.md), [program repair](program_repair.md)

- [Towards Neural Synthesis for SMT-Assisted Proof-Oriented Programming](../venues/ICSE2025/paper_8.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Proof-oriented programs mix computational content with proofs of program correctness. However, the human effort involved in programming and proving is still substantial, despite the use of Satisfiability Modulo Theories (SMT) solvers to automate proofs in languages such as F*. Seeking to spur research on using AI to automate the construction of proof-oriented programs, we curate a dataset of 600K lines of open-source F* programs and proofs, including software used in production systems ranging f...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [{D}esign2{C}ode: Benchmarking Multimodal Code Generation for Automated Front-End Engineering](../venues/NAACL2025/paper_6.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Generative AI has made rapid advancements in recent years, achieving unprecedented capabilities in multimodal understanding and code generation. This can enable a new paradigm of front-end development in which multimodal large language models (MLLMs) directly convert visual designs into code implementations. In this work, we construct Design2Code {--} the first real-world benchmark for this task. Specifically, we manually curate 484 diverse real-world webpages as test cases and develop a set of ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)

## Code Model

- [Follow-Up Attention: An Empirical Study of Developer and Neural Model Code Exploration](../venues/TSE2024/paper_12.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Recent neural models of code, such as OpenAI Codex and AlphaCode, have demonstrated remarkable proficiency at code generation due to the underlying attention mechanism. However, it often remains unclear how the models actually process code, and to what extent their reasoning and the way their attention mechanism scans the code matches the patterns of developers. A poor understanding of the model reasoning process limits the way in which current neural models are leveraged today, so far mostly fo...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [benchmark](benchmark.md)

- [Model Editing for LLMs4Code: How Far are we?](../venues/ICSE2025/paper_22.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large Language Models for Code (LLMs4Code) have been found to exhibit outstanding performance in the software engineering domain, especially the remarkable performance in coding tasks. However, even the most advanced LLMs4Code can inevitably contain incorrect or outdated code knowledge. Due to the high cost of training LLMs4Code, it is impractical to re-train the models for fixing these problematic code knowledge. Model editing is a new technical field for effectively and efficiently correcting ...
  - **Labels**: [code model](code_model.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [OpenAI’s Approach to External Red Teaming for AI Models and Systems](../venues/OpenAI2024/paper_1.md), ([OpenAI2024](../venues/OpenAI2024/README.md))

  - **Abstract**: Red teaming has emerged as a critical practice in assessing the possible risks of AI models and systems. It aids in the discovery of novel risks, stress testing possible gaps in existing mitigations, enriching existing quantitative safety metrics, facilitating the creation of new safety measurements, and enhancing public trust and the legitimacy of AI risk assessments. This white paper describes OpenAI’s work to date in external red teaming and draws some more general conclusions from this work....
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [benchmark](benchmark.md)

- [RMCBench: Benchmarking Large Language Models' Resistance to Malicious Code](../venues/ASE2024/paper_18.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Warning: Please note that this article contains potential harmful or offensive content. This content is only for the evaluating and analysis of LLMs and does not imply any intention to promote criminal activities.The emergence of Large Language Models (LLMs) has significantly influenced various aspects of software development activities. Despite their benefits, LLMs also pose notable risks, including the potential to generate harmful content and being abused by malicious developers to create mal...
  - **Labels**: [code generation](code_generation.md), [benchmark](benchmark.md), [code model](code_model.md), [code model robustness](code_model_robustness.md)

- [RedAgent: Red Teaming Large Language Models with Context-aware Autonomous Language Agent](../venues/arXiv2024/paper_4.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Recently, advanced Large Language Models (LLMs) such as GPT-4 have been integrated into many real-world applications like Code Copilot. These applications have significantly expanded the attack surface of LLMs, exposing them to a variety of threats. Among them, jailbreak attacks that induce toxic responses through jailbreak prompts have raised critical safety concerns. To identify these threats, a growing number of red teaming approaches simulate potential adversarial scenarios by crafting jailb...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [benchmark](benchmark.md)

- [SecCodePLT: A Unified Platform for Evaluating the Security of Code GenAI](../venues/arXiv2024/paper_3.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Language models for code (CodeLMs) have emerged as powerful tools for code-related tasks, outperforming traditional methods and standard machine learning approaches. However, these models are susceptible to security vulnerabilities, drawing increasing research attention from domains such as software engineering, artificial intelligence, and cybersecurity. Despite the growing body of research focused on the security of CodeLMs, a comprehensive survey in this area remains absent. To address this g...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model security](code_model_security.md), [benchmark](benchmark.md)

- [Self-Constructed Context Decompilation with Fined-grained Alignment Enhancement](../venues/EMNLP2024/paper_7.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Decompilation transforms compiled code back into a high-level programming language for analysis when source code is unavailable. Previous work has primarily focused on enhancing decompilation performance by increasing the scale of model parameters or training data for pre-training. Based on the characteristics of the decompilation task, we propose two methods: (1) Without fine-tuning, the Self-Constructed Context Decompilation (sc²dec) method recompiles the LLM’s decompilation results to constru...
  - **Labels**: [static analysis](static_analysis.md), [program decompilation](program_decompilation.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md), [benchmark](benchmark.md)

- [Traces of Memorisation in Large Language Models for Code](../venues/ICSE2024/paper_8.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Large language models have gained significant popularity because of their ability to generate human-like text and potential applications in various fields, such as Software Engineering. Large language models for code are commonly trained on large unsanitised corpora of source code scraped from the internet. The content of these datasets is memorised and can be extracted by attackers with data extraction attacks. In this work, we explore memorisation in large language models for code and compare ...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [benchmark](benchmark.md)

## General Coding Task

- [An Empirical Study to Evaluate AIGC Detectors on Code Content](../venues/ASE2024/paper_16.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Artificial Intelligence Generated Content (AIGC) has garnered considerable attention for its impressive performance, with Large Language Models (LLMs), like ChatGPT, emerging as a leading AIGC model that produces high-quality responses across various applications, including software development and maintenance. Despite its potential, the misuse of LLMs, especially in security and safety-critical domains, such as academic integrity and answering questions on Stack Overflow, poses significant conc...
  - **Labels**: [general coding task](general_coding_task.md), [benchmark](benchmark.md)

- [CodeScope: An Execution-based Multilingual Multitask Multidimensional Benchmark for Evaluating LLMs on Code Understanding and Generation](../venues/ACL2024/paper_18.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated remarkable performance on assisting humans in programming and facilitating programming automation. However, existing benchmarks for evaluating the code understanding and generation capacities of LLMs suffer from severe limitations. First, most benchmarks are insufficient as they focus on a narrow range of popular programming languages and specific tasks, whereas real-world software development scenarios show a critical need to implement systems with...
  - **Labels**: [general coding task](general_coding_task.md), [benchmark](benchmark.md)

- [ComplexCodeEval: A Benchmark for Evaluating Large Code Models on More Complex Code](../venues/ASE2024/paper_28.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: In recent years, with the widespread attention of academia and industry on the application of large language models (LLMs) to code-related tasks, an increasing number of large code models (LCMs) have been proposed and corresponding evaluation benchmarks have continually emerged. Although existing evaluation benchmarks are helpful for comparing different LCMs, they may not reflect the performance of LCMs in various development scenarios. Specifically, they might evaluate model performance in only...
  - **Labels**: [general coding task](general_coding_task.md), [benchmark](benchmark.md)

- [On Improving Repository-Level Code QA for Large Language Models](../venues/ACL2024/paper_7.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Large Language Models (LLMs) such as ChatGPT, GitHub Copilot, Llama, or Mistral assist programmers as copilots and knowledge sources to make the coding process faster and more efficient. This paper aims to improve the copilot performance by implementing different self-alignment processes and retrieval-augmented generation (RAG) pipelines, as well as their combination. To test the effectiveness of all approaches, we create a dataset and apply a model-based evaluation, using LLM as a judge. It is ...
  - **Labels**: [general coding task](general_coding_task.md), [benchmark](benchmark.md)

- [XCodeEval: An Execution-based Large Scale Multilingual Multitask Benchmark for Code Understanding, Generation, Translation and Retrieval](../venues/ACL2024/paper_20.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Recently, pre-trained large language models (LLMs) have shown impressive abilities in generating codes from natural language descriptions, repairing buggy codes, translating codes between languages, and retrieving relevant code segments. However, the evaluation of these models has often been performed in a scattered way on only one or two specific tasks, in a few languages, at a partial granularity (e.g., function) level, and in many cases without proper training data. Even more concerning is th...
  - **Labels**: [general coding task](general_coding_task.md), [benchmark](benchmark.md)

## Program Testing

- [BountyBench: Dollar Impact of AI Agent Attackers and Defenders on Real-World Cybersecurity Systems](../venues/arXiv2025/paper_21.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: AI agents have the potential to significantly alter the cybersecurity landscape. To help us understand this change, we introduce the first framework to capture offensive and defensive cyber-capabilities in evolving real-world systems. Instantiating this framework with BountyBench, we set up 25 systems with complex, real-world codebases. To capture the vulnerability lifecycle, we define three task types: Detect (detecting a new vulnerability), Exploit (exploiting a specific vulnerability), and Pa...
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md), [benchmark](benchmark.md)

- [CoderUJB: An Executable and Unified Java Benchmark for Practical Programming Scenarios](../venues/ISSTA2024/paper_3.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: In the evolving landscape of large language models (LLMs) tailored for software engineering, the need for benchmarks that accurately reflect real-world development scenarios is paramount. Current benchmarks are either too simplistic or fail to capture the multi-tasking nature of software development. To address this, we introduce CoderUJB, a new benchmark designed to evaluate LLMs across diverse Java programming tasks that are executable and reflective of actual development scenarios, acknowledg...
  - **Labels**: [code generation](code_generation.md), [program testing](program_testing.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)

- [Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models](../venues/arXiv2024/paper_31.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Language Model (LM) agents for cybersecurity that are capable of autonomously identifying vulnerabilities and executing exploits have the potential to cause real-world impact. Policymakers, model providers, and other researchers in the AI and cybersecurity communities are interested in quantifying the capabilities of such agents to help mitigate cyberrisk and investigate opportunities for penetration testing. Toward that end, we introduce Cybench, a framework for specifying cybersecurity tasks a...
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md), [benchmark](benchmark.md)

- [CyberGym: Evaluating AI Agents' Cybersecurity Capabilities with Real-World Vulnerabilities at Scale](../venues/arXiv2025/paper_20.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Large language model (LLM) agents are becoming increasingly skilled at handling cybersecurity tasks autonomously. Thoroughly assessing their cybersecurity capabilities is critical and urgent, given the high stakes in this domain. However, existing benchmarks fall short, often failing to capture real-world scenarios or being limited in scope. To address this gap, we introduce CyberGym, a large-scale and high-quality cybersecurity evaluation framework featuring 1,507 real-world vulnerabilities fou...
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md), [benchmark](benchmark.md)

- [Interactive Tools Substantially Assist LM Agents in Finding Security Vulnerabilities](../venues/arXiv2025/paper_19.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Although language model (LM) agents have demonstrated increased performance in multiple domains, including coding and web-browsing, their success in cybersecurity has been limited. We present EnIGMA, an LM agent for autonomously solving Capture The Flag (CTF) challenges. We introduce new tools and interfaces to improve the agent's ability to find and exploit security vulnerabilities, focusing on interactive terminal programs. These novel Interactive Agent Tools enable LM agents, for the first ti...
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md), [benchmark](benchmark.md)

- [Language agents as hackers: Evaluating cybersecurity skills with capture the flag](../venues/NeurIPS2023/paper_1.md), ([NeurIPS2023](../venues/NeurIPS2023/README.md))

  - **Abstract**: Amidst the advent of language models (LMs) and their wide-ranging capabilities, concerns have been raised about their implications with regards to privacy and security. In particular, the emergence of language agents as a promising aid for automating and augmenting digital work poses immediate questions concerning their misuse as malicious cybersecurity actors. With their exceptional compute efficiency and execution speed relative to human counterparts, language agents may be extremely adept at ...
  - **Labels**: [program testing](program_testing.md), [vulnerability exploitation](vulnerability_exploitation.md), [benchmark](benchmark.md)

- [Reasoning Runtime Behavior of a Program with LLM: How Far are We?](../venues/ICSE2025/paper_10.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large language models for code (i.e., code LLMs) have shown strong code understanding and generation capabilities. To evaluate the capabilities of code LLMs in various aspects, many benchmarks have been proposed (e.g., HumanEval and ClassEval). Code reasoning is one of the most essential abilities of code LLMs (i.e., predicting code execution behaviors such as program output and execution path), but existing benchmarks for code reasoning are not sufficient. Typically, they focus on predicting th...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [UniTSyn: A Large-Scale Dataset Capable of Enhancing the Prowess of Large Language Models for Program Testing](../venues/ISSTA2024/paper_27.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: The remarkable capability of large language models (LLMs) in generating high-quality code has drawn increasing attention in the software testing community. However, existing code LLMs often demonstrate unsatisfactory capabilities in generating accurate, complete tests since they were trained on code snippets collected without differentiating between code for testing and for other purposes. In this paper, we present a large-scale dataset, UniTSyn, which can enhance LLMs for Unit Test Synthesis. A...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [benchmark](benchmark.md)

## Static Analysis

- [Can LLMs Reason About Program Semantics? A Comprehensive Evaluation of LLMs on Formal Specification Inference](../venues/arXiv2025/paper_11.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Large Language Models (LLMs) are increasingly being used to automate programming tasks. Yet, LLMs' capabilities in reasoning about program semantics are still inadequately studied, leaving significant potential for further exploration. This paper introduces FormalBench, a comprehensive benchmark designed to evaluate LLMs' reasoning abilities on program semantics, particularly via the task of synthesizing formal program specifications to assist verifying program correctness. This task requires bo...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [CompilerGym: robust, performant compiler optimization environments for AI research](../venues/CGO2022/paper_1.md), ([CGO2022](../venues/CGO2022/README.md))

  - **Abstract**: Interest in applying Artificial Intelligence (AI) techniques to compiler optimizations is increasing rapidly, but compiler research has a high entry barrier. Unlike in other domains, compiler and AI researchers do not have access to the datasets and frameworks that enable fast iteration and development of ideas, and getting started requires a significant engineering investment. What is needed is an easy, reusable experimental infrastructure for real world compiler optimization tasks that can ser...
  - **Labels**: [static analysis](static_analysis.md), [program optimization](program_optimization.md), [benchmark](benchmark.md)

- [DiverseVul: {A} New Vulnerable Source Code Dataset for Deep Learning Based Vulnerability Detection](../venues/RAID2023/paper_1.md), ([RAID2023](../venues/RAID2023/README.md))

  - **Abstract**: We propose and release a new vulnerable source code dataset. We curate the dataset by crawling security issue websites, extracting vulnerability-fixing commits and source codes from the corresponding projects. Our new dataset contains 18,945 vulnerable functions spanning 150 CWEs and 330,492 non-vulnerable functions extracted from 7,514 commits. Our dataset covers 295 more projects than all previous datasets combined.Combining our new dataset with previous datasets, we present an analysis of the...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)

- [How Far Have We Gone in Vulnerability Detection Using Large Language Models](../venues/arXiv2023/paper_5.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: As software becomes increasingly complex and prone to vulnerabilities, automated vulnerability detection is critically important, yet challenging. Given the significant successes of large language models (LLMs) in various tasks, there is growing anticipation of their efficacy in vulnerability detection. However, a quantitative understanding of their potential in vulnerability detection is still missing. To bridge this gap, we introduce a comprehensive vulnerability benchmark VulBench. This bench...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)

- [LLM4Vuln: {A} Unified Evaluation Framework for Decoupling and Enhancing LLMs' Vulnerability Reasoning](../venues/arXiv2024/paper_19.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated significant potential in various tasks, including vulnerability detection. However, current efforts in this area are preliminary, lacking clarity on whether LLMs' vulnerability reasoning capabilities stem from the models themselves or external aids such as knowledge retrieval and tooling support.This paper aims to isolate LLMs' vulnerability reasoning from other capabilities, such as vulnerability knowledge adoption, context information retrieval, a...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)

- [Learning to Generate Structured Code Summaries From Hybrid Code Context](../venues/TSE2024/paper_11.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Code summarization aims to automatically generate natural language descriptions for code, and has become a rapidly expanding research area in the past decades. Unfortunately, existing approaches mainly focus on the “one-to-one” mapping from methods to short descriptions, which hinders them from becoming practical tools: 1) The program context is ignored, so they have difficulty in predicting labels outside the target method; 2) They are typically trained to generate brief function descriptions w...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [benchmark](benchmark.md)

- [SV-TrustEval-C: Evaluating Structure and Semantic Reasoning in Large Language Models for Source Code Vulnerability Analysis](../venues/S&P2025/paper_1.md), ([S&P2025](../venues/S&P2025/README.md))

  - **Abstract**: As Large Language Models (LLMs) evolve in understanding and generating code, accurately evaluating their reliability in analyzing source code vulnerabilities becomes in-creasingly vital. While studies have examined LLM capabilities in tasks like vulnerability detection and repair, they often over-look the importance of both structure and semantic reasoning crucial for trustworthy vulnerability analysis. To address this gap, we introduce SV-TRUSTEVAL-C, a benchmark designed to evaluate LLMs' abil...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [SecVulEval: Benchmarking LLMs for Real-World C/C++ Vulnerability Detection](../venues/arXiv2025/paper_2.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have shown promise in software engineering tasks, but evaluating their effectiveness in vulnerability detection is challenging due to the lack of high-quality datasets. Most existing datasets are limited to function-level labels, ignoring finer-grained vulnerability patterns and crucial contextual information. Also, poor data quality such as mislabeling, inconsistent annotations, and duplicates can lead to inflated performance and weak generalization. Moreover, by in...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)

- [Self-Constructed Context Decompilation with Fined-grained Alignment Enhancement](../venues/EMNLP2024/paper_7.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Decompilation transforms compiled code back into a high-level programming language for analysis when source code is unavailable. Previous work has primarily focused on enhancing decompilation performance by increasing the scale of model parameters or training data for pre-training. Based on the characteristics of the decompilation task, we propose two methods: (1) Without fine-tuning, the Self-Constructed Context Decompilation (sc²dec) method recompiles the LLM’s decompilation results to constru...
  - **Labels**: [static analysis](static_analysis.md), [program decompilation](program_decompilation.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md), [benchmark](benchmark.md)

- [Towards General Loop Invariant Generation: A Benchmark of Programs with Memory Manipulation](../venues/NeurIPS2024/paper_7.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Program verification is vital for ensuring software reliability, especially in the context of increasingly complex systems. Loop invariants, remaining true before and after each iteration of loops, are crucial for this verification process. Traditional provers and machine learning based methods for generating loop invariants often require expert intervention or extensive labeled data, and typically only handle numerical property verification. These methods struggle with programs involving comple...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md), [benchmark](benchmark.md)

- [Towards Neural Synthesis for SMT-Assisted Proof-Oriented Programming](../venues/ICSE2025/paper_8.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Proof-oriented programs mix computational content with proofs of program correctness. However, the human effort involved in programming and proving is still substantial, despite the use of Satisfiability Modulo Theories (SMT) solvers to automate proofs in languages such as F*. Seeking to spur research on using AI to automate the construction of proof-oriented programs, we curate a dataset of 600K lines of open-source F* programs and proofs, including software used in production systems ranging f...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [VULGEN: Realistic Vulnerability Generation Via Pattern Mining and Deep Learning](../venues/ICSE2023/paper_11.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Building new, powerful data-driven defenses against prevalent software vulnerabilities needs sizable, quality vulnerability datasets, so does large-scale benchmarking of existing defense solutions. Automatic data generation would promisingly meet the need, yet there is little work aimed to generate much-needed quality vulnerable samples. Meanwhile, existing similar and adaptable techniques suffer critical limitations for that purpose. In this paper, we present VULGEN, the first injection-based v...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)

- [VulEval: Towards Repository-Level Evaluation of Software Vulnerability Detection](../venues/arXiv2024/paper_15.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Deep Learning (DL)-based methods have proven to be effective for software vulnerability detection, with a potential for substantial productivity enhancements for detecting vulnerabilities. Current methods mainly focus on detecting single functions (i.e., intra-procedural vulnerabilities), ignoring the more complex inter-procedural vulnerability detection scenarios in practice. For example, developers routinely engage with program analysis to detect vulnerabilities that span multiple functions wi...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)

- [Vulnerability Detection with Code Language Models: How Far Are We?](../venues/ICSE2025/paper_4.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: In the context of the rising interest in code language models (code LMs) and vulnerability detection, we study the effectiveness of code LMs for detecting vulnerabilities. Our analysis reveals significant shortcomings in existing vulnerability datasets, including poor data quality, low label accuracy, and high duplication rates, leading to unreliable model performance in realistic vulnerability detection scenarios. Additionally, the evaluation methods used with these datasets are not representat...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)

- [What can Large Language Models Capture about Code Functional Equivalence?](../venues/NAACL2025/paper_13.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Code-LLMs, LLMs pre-trained on large code corpora, have shown great progress in learning rich representations of the structure and syntax of code, successfully using it to generate or classify code fragments. At the same time, understanding if they are able to do so because they capture code semantics, and how well, is still an open question. In this paper, we tackle this problem by introducing SeqCoBench, a benchmark for systematically assessing how Code-LLMs can capture code functional equival...
  - **Labels**: [static analysis](static_analysis.md), [equivalence checking](equivalence_checking.md), [empirical study](empirical_study.md), [benchmark](benchmark.md)
