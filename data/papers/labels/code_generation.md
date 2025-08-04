# Code Generation

## Program Synthesis

- [A Closer Look at Different Difficulty Levels Code Generation Abilities of ChatGPT](../venues/ASE2023/paper_6.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Code generation aims to generate source code implementing human requirements illustrated with natural language specifications. With the rapid development of intelligent software engineering, automated code generation has become a hot research topic in both artificial intelligence and software engineering, and researchers have made significant achievements on code generation. More recently, large language models (LLMs) have demonstrated outstanding performance on code generation tasks, such as Ch...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [A Pair Programming Framework for Code Generation via Multi-Plan Exploration and Feedback-Driven Refinement](../venues/ASE2024/paper_21.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Large language models (LLMs) have achieved impressive performance on code generation. Although prior studies enhanced LLMs with prompting techniques and code refinement, they still struggle with complex programming problems due to rigid solution plans. In this paper, we draw on pair programming practices to propose PairCoder, a novel LLM-based framework for code generation. PairCoder incorporates two collaborative LLM agents, namely a Navigator agent for high-level planning and a Driver agent fo...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [planning](planning.md)


- [AI Coders Are among Us: Rethinking Programming Language Grammar towards Efficient Code Generation](../venues/ISSTA2024/paper_13.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Artificial Intelligence (AI) models have emerged as another important audience for programming languages alongside humans and machines, as we enter the era of large language models (LLMs). LLMs can now perform well in coding competitions and even write programs like developers to solve various tasks, including mathematical problems. However, the grammar and layout of current programs are designed to cater the needs of human developers -- with many grammar tokens and formatting tokens being used ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [AMR-Evol: Adaptive Modular Response Evolution Elicits Better Knowledge Distillation for Large Language Models in Code Generation](../venues/EMNLP2024/paper_17.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: The impressive performance of proprietary LLMs like GPT4 in code generation has led to a trend to replicate these capabilities in open-source models through knowledge distillation (e.g. Code Evol-Instruct). However, these efforts often neglect the crucial aspect of response quality, relying heavily on teacher models for direct response distillation. This paradigm, especially for complex instructions, can degrade the quality of synthesized data, compromising the knowledge distillation process. To...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [API-Assisted Code Generation for Question Answering on Varied Table Structures](../venues/EMNLP2023/paper_9.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: A persistent challenge to table question answering (TableQA) by generating executable programs has been adapting to varied table structures, typically requiring domain-specific logical forms. In response, this paper introduces a unified TableQA framework that: (1) provides a unified representation for structured tables as multi-index Pandas data frames, (2) uses Python as a powerful querying language, and (3) uses few-shot prompting to translate NL questions into Python programs, which are execu...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [An Exploratory Study of ML Sketches and Visual Code Assistants](../venues/ICSE2025/paper_37.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: This paper explores the integration of Visual Code Assistants in Integrated Development Environments (IDEs). In Software Engineering, whiteboard sketching is often the initial step before coding, serving as a crucial collaboration tool for developers. Previous studies have investigated patterns in SE sketches and how they are used in practice, yet methods for directly using these sketches for code generation remain limited. The emergence of visually-equipped large language models presents an opp...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [software maintenance and deployment](software_maintenance_and_deployment.md)


- [Ansible Lightspeed: A Code Generation Service for IT Automation](../venues/ASE2024/paper_30.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: The availability of Large Language Models (LLMs) which can generate code, has made it possible to create tools that improve developer productivity. Integrated development environments or IDEs which developers use to write software are often used as an interface to interact with LLMs. Although many such tools have been released, almost all of them focus on general-purpose programming languages. Domain-specific languages, such as those crucial for Information Technology (IT) automation, have not r...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [ArchCode: Incorporating Software Requirements in Code Generation with Large Language Models](../venues/ACL2024/paper_1.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: This paper aims to extend the code generation capability of large language models (LLMs) to automatically manage comprehensive software requirements from given textual descriptions. Such requirements include both functional (i.e. achieving expected behavior for inputs) and non-functional (e.g., time/space performance, robustness, maintainability) requirements. However, textual descriptions can either express requirements verbosely or may even omit some of them. We introduce ARCHCODE, a novel fra...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Are Human Rules Necessary? Generating Reusable APIs with CoT Reasoning and In-Context Learning](../venues/FSE2024/paper_14.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Inspired by the great potential of Large Language Models (LLMs) for solving complex coding tasks, in this paper, we propose a novel approach, named Code2API, to automatically perform APIzation for Stack Overflow code snippets. Code2API does not require additional model training or any manual crafting rules and can be easily deployed on personal computers without relying on other external tools. Specifically, Code2API guides the LLMs through well-designed prompts to generate well-formed APIs for ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [source code model](source_code_model.md)


- [B4: Towards Optimal Assessment of Plausible Code Solutions with Plausible Tests](../venues/ASE2024/paper_27.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Selecting the best code solution from multiple generated ones is an essential task in code generation, which can be achieved by using some reliable validators (e.g., developer-written test cases) for assistance. Since reliable test cases are not always available and can be expensive to build in practice, researchers propose to automatically generate test cases to assess code solutions. However, when both code solutions and test cases are plausible and not reliable, selecting the best solution be...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Benchmarking Language Model Creativity: A Case Study on Code Generation](../venues/NAACL2025/paper_4.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: As LLMs become increasingly prevalent, it is interesting to consider how ``creative'' these models can be. From cognitive science, creativity consists of at least two key characteristics: \textit{convergent} thinking (purposefulness to achieve a given goal) and \textit{divergent} thinking (adaptability to explore new environments or constraints) (CITATION). In this work, we introduce a framework for quantifying LLM creativity that incorporates the two design ingredients: (1) We introduce DENIAL ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)


- [Benchmarking and Improving Text-to-SQL Generation under Ambiguity](../venues/EMNLP2023/paper_3.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Research in Text-to-SQL conversion has been largely benchmarked against datasets where each text query corresponds to one correct SQL. However, natural language queries over real-life databases frequently involve significant ambiguity about the intended SQL due to overlapping schema names and multiple confusing relationship paths. To bridge this gap, we develop a novel benchmark called AmbiQT with over 3000 examples where each text is interpretable as two plausible SQLs due to lexical and/or str...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)


- [CRUSH4SQL: Collective Retrieval Using Schema Hallucination For Text2SQL](../venues/EMNLP2023/paper_8.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Existing Text-to-SQL generators require the entire schema to be encoded with the user text. This is expensive or impractical for large databases with tens of thousands of columns. Standard dense retrieval techniques are inadequate for schema subsetting of a large structured database, where the correct semantics of retrieval demands that we rank sets of schema elements rather than individual documents. In response, we propose a two-stage process for effective coverage during retrieval. First, we ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Causality-Aided Evaluation and Explanation of Large Language Model-Based Code Generation](../venues/ISSTA2025/paper_17.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: While code generation has been widely used in various software development scenarios, the quality of the generated code is not guaranteed. This has been a particular concern in the era of large language models (LLM)-based code generation, where LLMs, deemed a complex and powerful black-box model, are instructed by a high-level natural language specification, namely a prompt, to generate code. Nevertheless, effectively evaluating and explaining the code generation capability of LLMs is inherently...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Chain-of-Thought in Neural Code Generation: From and for Lightweight Language Models](../venues/TSE2024/paper_3.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated remarkable potential in code generation. The integration of Chain of Thought (CoT) reasoning can further boost their performance. However, current CoT methods often require manual writing or LLMs with over 100 billion parameters to generate, impeding their applicability in resource-constrained scenarios. In this study, we investigate lightweight Language Models (&lt;inline-formula&gt;&lt;tex-math notation="LaTeX"&gt;$ell$&lt;/tex-math&gt;&lt;alterna...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [ClarifyGPT: A Framework for Enhancing LLM-Based Code Generation via Requirements Clarification](../venues/FSE2024/paper_13.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Large Language Models (LLMs), such as ChatGPT, have demonstrated impressive capabilities in automatically generating code from provided natural language requirements. However, in real-world practice, it is inevitable that the requirements written by users might be ambiguous or insufficient. Current LLMs will directly generate programs according to those unclear requirements, regardless of interactive clarification, which will likely deviate from the original user intents. To bridge that gap, we ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [CoCoST: Automatic Complex Code Generation with Online Searching and Correctness Testing](../venues/EMNLP2024/paper_34.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large Language Models have revolutionized code generation ability by converting natural language descriptions into executable code. However, generating complex code within real-world scenarios remains challenging due to intricate structures, subtle bugs, understanding of advanced data types, and lack of supplementary contents. To address these challenges, we introduce the CoCoST framework, which enhances complex code generation by online searching for more information with planned queries and co...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)


- [Code4Struct: Code Generation for Few-Shot Event Structure Prediction](../venues/ACL2023/paper_8.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Large Language Model (LLM) trained on a mixture of text and code has demonstrated impressive capability in translating natural language (NL) into structured code. We observe that semantic structures can be conveniently translated into code and propose Code4Struct to leverage such text-to-structure translation capability to tackle structured prediction tasks. As a case study, we formulate Event Argument Extraction (EAE) as converting text into event-argument structures that can be represented as ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges](../venues/ACL2024/paper_3.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have shown promise in automated code generation but typically excel only in simpler tasks such as generating standalone code units. However, real-world software development often involves complex code repositories with complex dependencies and extensive documentation. To enable LLMs to handle these realworld repo-level code generation, we present CodeAgent, a novel LLM-based agent framework that employs external tools for effective repo-level code generation. CodeAge...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)


- [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](../venues/ICLR2024/paper_5.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have already become quite proficient at solving simpler programming tasks like those in HumanEval or MBPP benchmarks. However, solving more complex and competitive programming tasks is still quite challenging for these models - possibly due to their tendency to generate solutions as monolithic code blocks instead of decomposing them into logical sub-tasks and sub-modules. On the other hand, experienced programmers instinctively write modularized code with abstraction...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors](../venues/ACL2023/paper_5.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Large language models (LLMs) pre-trained on massive corpora have demonstrated impressive few-shot learning ability on many NLP tasks. A common practice is to recast the task into a text-to-text format such that generative LLMs of natural language (NL-LLMs) like GPT-3 can be prompted to solve it. However, it is nontrivial to perform information extraction (IE) tasks with NL-LLMs since the output of the IE task is usually structured and therefore is hard to be converted into plain text. In this pa...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [CodeIP: A Grammar-Guided Multi-Bit Watermark for Large Language Models of Code](../venues/EMNLP2024/paper_9.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have achieved remarkable progress in code generation. It now becomes crucial to identify whether the code is AI-generated and to determine the specific model used, particularly for purposes such as protecting Intellectual Property (IP) in industry and preventing cheating in programming exercises. To this end, several attempts have been made to insert watermarks into machine-generated code. However, existing approaches are limited to inserting only a single bit of inf...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model security](code_model_security.md)


- [CodeJudge: Evaluating Code Generation with Large Language Models](../venues/EMNLP2024/paper_35.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have shown promising performance in code generation. However, how to reliably evaluate code generated by LLMs remains an unresolved problem. This paper presents CodeJudge, a code evaluation framework that leverages LLMs to evaluate the semantic correctness of generated code without the need for test cases. We investigate different ways to guide the LLM in performing “slow thinking” to arrive at an in-depth and reliable evaluation. We experimented with four LLMs as ev...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [CodePlan: Repository-Level Coding using LLMs and Planning](../venues/FSE2024/paper_20.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Software engineering activities such as package migration, fixing error reports from static analysis or testing, and adding type annotations or other specifications to a codebase, involve pervasively editing the entire repository of code.     We formulate these activities as repository-level coding tasks.         Recent tools like GitHub Copilot, which are powered by Large Language Models (LLMs), have succeeded in offering high-quality solutions to localized coding problems.     Repository-level...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [planning](planning.md)


- [ConTested: Consistency-Aided Tested Code Generation with LLM](../venues/ISSTA2025/paper_8.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Recent advancements in large language models (LLMs) have significantly improved code generation, which generates code snippets automatically based on natural language requirements. Despite achieving state-of-the-art performance, LLMs often struggle to generate accurate and reliable code, requiring developers to spend substantial effort debugging and evaluating the generated output. Researchers have proposed leveraging Consistency to select code that passes more tests (inter-consistency) and demo...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [program testing](program_testing.md)


- [Contextualized Data-Wrangling Code Generation in Computational Notebooks](../venues/ASE2024/paper_19.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Data wrangling, the process of preparing raw data for further analysis in computational notebooks, is a crucial yet time-consuming step in data science. Code generation has the potential to automate the data wrangling process to reduce analysts' overhead by translating user intents into executable code. Precisely generating data wrangling code necessitates a comprehensive consideration of the rich context present in notebooks, including textual context, code context and data context. However, no...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [CoqPilot, a plugin for LLM-based generation of proofs](../venues/ASE2024/paper_36.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: We present CoqPilot, a VS Code extension designed to help automate writing of Coq proofs. The plugin collects the parts of proofs marked with the admit tactic in a Coq file, i.e., proof holes, and combines LLMs along with non-machine-learning methods to generate proof candidates for the holes. Then, CoqPilot checks if each proof candidate solves the given subgoal and, if successful, replaces the hole with it. The focus of CoqPilot is twofold. Firstly, we want to allow users to seamlessly combine...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md)


- [DA-Code: Agent Data Science Code Generation Benchmark for Large Language Models](../venues/EMNLP2024/paper_28.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: We introduce DA-Code, a code generation benchmark specifically designed to assess LLMs on agent-based data science tasks. This benchmark features three core elements: First, the tasks within DA-Code are inherently challenging, setting them apart from traditional code generation tasks and demanding advanced coding skills in grounding and planning. Second, examples in DA-Code are all based on real and diverse data, covering a wide range of complex data wrangling and analytics tasks. Third, to solv...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)


- [DeclarUI: Bridging Design and Development with Automated Declarative UI Code Generation](../venues/FSE2025/paper_6.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Declarative UI frameworks have gained widespread adoption in mobile app development, offering benefits such as improved code readability and easier maintenance. Despite these advantages, the process of translating UI designs into functional code remains challenging and time-consuming. Recent advancements in multimodal large language models (MLLMs) have shown promise in directly generating mobile app code from user interface (UI) designs. However, the direct application of MLLMs to this task is l...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Divide-and-Conquer: Generating UI Code from Screenshots](../venues/FSE2025/paper_28.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Websites are critical in today’s digital world, with over 1.11 billion currently active and approximately 252,000 new sites launched daily. Converting website layout design into functional UI code is a time-consuming yet indispensable step of website development. Manual methods of converting visual designs into functional code present significant challenges, especially for non-experts. To explore automatic design-to-code solutions, we first conduct a motivating study on GPT-4o and identify three...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Do Large Language Models Pay Similar Attention Like Human Programmers When Generating Code?](../venues/FSE2024/paper_11.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have recently been widely used for code generation. Due to the complexity and opacity of LLMs, little is known about how these models generate code. We made the first attempt to bridge this knowledge gap by investigating whether LLMs attend to the same parts of a task description as human programmers during code generation. An analysis of six LLMs, including GPT-4, on two popular code generation benchmarks revealed a consistent misalignment between LLMs' and programm...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [DocCGen: Document-based Controlled Code Generation](../venues/EMNLP2024/paper_33.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Recent developments show that Large Language Models (LLMs) produce state-of-the-art performance on natural language (NL) to code generation for resource-rich general-purpose languages like C++, Java, and Python. However, their practical usage for structured domain-specific languages (DSLs) such as YAML, JSON is limited due to domain-specific schema, grammar, and customizations generally unseen by LLMs during pre-training. Efforts have been made to mitigate this challenge via in-context learning ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [DolphCoder: Echo-Locating Code Large Language Models with Diverse and Multi-Objective Instruction Tuning](../venues/ACL2024/paper_14.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Code Large Language Models (Code LLMs) have demonstrated outstanding performance in code-related tasks. Various instruction finetuning approaches have been proposed to boost the code generation performance of pre-trained Code LLMs. In this paper, we introduce a diverse instruction model DolphCoder with self-evaluating for code generation. It learns diverse instruction targets and combines a code evaluation objective to enhance its code generation ability. Our model achieves superior performance ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Dynamic Scoring Code Token Tree: A Novel Decoding Strategy for Generating High-Performance Code](../venues/ASE2024/paper_20.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Within the realms of scientific computing, large-scale data processing, and artificial intelligence-powered computation, disparities in performance, which originate from differing code implementations, directly influence the practicality of the code. Although existing works tried to utilize code knowledge to enhance the execution performance of codes generated by large language models, they neglect code evaluation outcomes which directly refer to the code execution details, resulting in ineffici...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [ECCO: Can We Improve Model-Generated Code Efficiency Without Sacrificing Functional Correctness?](../venues/EMNLP2024/paper_31.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Although large language models (LLMs) have been largely successful in generating functionally correct programs, conditioning models to produce efficient solutions while ensuring correctness remains a challenge. Further, unreliability in benchmarking code efficiency is a hurdle across varying hardware specifications for popular interpreted languages such as Python. In this paper, we present ECCO, a reproducible benchmark for evaluating program efficiency via two paradigms: natural language (NL) b...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [EGFE: End-to-end Grouping of Fragmented Elements in UI Designs with Multimodal Learning](../venues/ICSE2024/paper_23.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: When translating UI design prototypes to code in industry, automatically generating code from design prototypes can expedite the development of applications and GUI iterations. However, in design prototypes without strict design specifications, UI components may be composed of fragmented elements. Grouping these fragmented elements can greatly improve the readability and maintainability of the generated code. Current methods employ a two-stage strategy that introduces hand-crafted rules to group...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Enhance Hardware Domain Specific Large Language Model with Reinforcement Learning for Resilience](../venues/CCS2024/paper_8.md), ([CCS2024](../venues/CCS2024/README.md))

  - **Abstract**: To enhance the performance of large language models (LLMs) on hardware design tasks, we focus on training with reinforcement learning(RL) to improve LLMs' syntax synthesis and functional verification performance. We observed significant gains in power, performance, and area (PPA) metrics by applying RL. Specifically, DeepSeek Code saw a 23.6\% performance increase, while the RTLCoder improved by 7.86\%. Our findings demonstrate the effectiveness of RL in refining LLMs for more accurate hardware ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Enhancing Code Generation via Bidirectional Comment-Level Mutual Grounding](../venues/ICSE2025/paper_48.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated unprecedented capability in code generation. However, LLM-generated code is still plagued with a wide range of functional errors, especially for complex programming tasks that LLMs have not seen before. Recent studies have shown that developers often struggle with inspecting and fixing incorrect code generated by LLMs, diminishing their productivity and trust in LLM-based code generation. Inspired by the mutual grounding theory in communication, we ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Enhancing Discourse Dependency Parsing with Sentence Dependency Parsing: A Unified Generative Method Based on Code Representation](../venues/EMNLP2024/paper_14.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Due to the high complexity of Discourse Dependency Parsing (DDP) tasks, their existing annotation resources are relatively scarce compared to other NLP tasks, and different DDP tasks also have significant differences in annotation schema. These issues have led to the dilemma of low resources for DDP tasks. Thanks to the powerful capabilities of Large Language Models (LLMs) in cross-task learning, we can use LLMs to model dependency parsing under different annotation schema in an unified manner, ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Enhancing Large Language Models in Coding Through Multi-Perspective Self-Consistency](../venues/ACL2024/paper_9.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Large language models (LLMs) have exhibited remarkable ability in code generation. However, generating the correct solution in a single attempt still remains a challenge. Prior works utilize verification properties in software engineering to verify and re-rank solutions in a majority voting manner. But the assumption behind them that generated verification properties have better qualities than solutions may not always hold. In this paper, we treat them equally as different perspectives of LLMs’ ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Evaluating In-Context Learning of Libraries for Code Generation](../venues/NAACL2024/paper_4.md), ([NAACL2024](../venues/NAACL2024/README.md))

  - **Abstract**: Contemporary Large Language Models (LLMs) exhibit a high degree of code generation and comprehension capability. A particularly promising area is their ability to interpret code modules from unfamiliar libraries for solving user-instructed tasks. Recent work has shown that large proprietary LLMs can learn novel library usage in-context from demonstrations. These results raise several open questions: whether demonstrations of library usage is required, whether smaller (and more open) models also ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [Few-Shot Natural Language to First-Order Logic Translation via Code Generation](../venues/NAACL2025/paper_9.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Translation of natural language to first-order logical formula (NL-FOL) has recently gained significant attention for its critical role in logic-based NLP applications. Some studies attempt to utilize pretrained language models in a sequence-to-sequence manner for the NL-FOL task. However, these methods encounter challenges such as (1) inconsistency between the training and inference phases and (2) the data-intensive and resource-intensive finetuning process. This paper introduces a novel NL-FOL...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [From Misuse to Mastery: Enhancing Code Generation with Knowledge-Driven AI Chaining](../venues/ASE2023/paper_11.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Large Language Models (LLMs) have shown promising results in automatic code generation by improving coding efficiency to a certain extent. However, generating high-quality and reliable code remains a formidable task because of LLMs' lack of good programming practice, especially in exception handling. In this paper, we first conduct an empirical study and summarize three crucial challenges of LLMs in exception handling, i.e., incomplete exception handling, incorrect exception handling and abuse o...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](../venues/NeurIPS2024/paper_5.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: In this work we consider Code World Models, world models generated by a Large Language Model (LLM) in the form of Python code for model-based Reinforcement Learning (RL). Calling code instead of LLMs for planning has the advantages of being precise, reliable, interpretable, and extremely efficient. However, writing appropriate Code World Models requires the ability to understand complex instructions, to generate exact code with non-trivial logic and to self-debug a long program with feedback fro...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [How Do Humans Write Code? Large Models Do It the Same Way Too](../venues/EMNLP2024/paper_20.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Program-of-Thought (PoT) replaces natural language-based Chain-of-Thought (CoT) as the most popular method in Large Language Models (LLMs) mathematical reasoning tasks by utilizing external tool calls to circumvent computational errors. However, our evaluation of the GPT-4 and Llama series reveals that using PoT introduces more reasoning errors, such as incorrect formulas or flawed logic, compared to CoT. To address this issue, we propose Human-Think Language (HTL), which leverages a suite of st...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [HumanEvo: An Evolution-Aware Benchmark for More Realistic Evaluation of Repository-Level Code Generation](../venues/ICSE2025/paper_62.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: To evaluate the repository-level code generation capabilities of Large Language Models (LLMs) in complex real-world software development scenarios, many evaluation methods have been developed. These methods typically leverage contextual code from the latest version of a project to assist LLMs in accurately generating the desired function. However, such evaluation methods fail to consider the dynamic evolution of software projects over time, which we refer to as evolution-ignored settings. This i...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md), [benchmark](benchmark.md)


- [Hypothesis search: Inductive reasoning with language models](../venues/ICLR2024/paper_2.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Inductive reasoning is a core problem-solving capacity: humans can identify underlying principles from a few examples, which can then be robustly generalized to novel scenarios. Recent work has evaluated large language models (LLMs) on inductive reasoning tasks by directly prompting them yielding "in context learning." This can work well for straightforward inductive tasks, but performs very poorly on more complex tasks such as the Abstraction and Reasoning Corpus (ARC). In this work, we propose...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md)


- [INTERTRANS: Leveraging Transitive Intermediate Translations to Enhance LLM-Based Code Translation](../venues/ICSE2025/paper_67.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Code translation aims to convert a program from one programming language (PL) to another. This long-standing software engineering task is crucial for modernizing legacy systems, ensuring cross-platform compatibility, enhancing performance, and more. However, automating this process remains challenging due to many syntactic and semantic differences between PLs. Recent studies show that even advanced techniques such as large language models (LLMs), especially open-source LLMs, still struggle with ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Impeding LLM-assisted Cheating in Introductory Programming Assignments via Adversarial Perturbation](../venues/EMNLP2024/paper_16.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: While Large language model (LLM)-based programming assistants such as CoPilot and ChatGPT can help improve the productivity of professional software developers, they can also facilitate cheating in introductory computer programming courses. Assuming instructors have limited control over the industrial-strength models, this paper investigates the baseline performance of 5 widely used LLMs on a collection of introductory programming problems, examines adversarial perturbations to degrade their per...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [Improving Code Extraction from Coding Screencasts Using a Code-Aware Encoder-Decoder Model](../venues/ASE2023/paper_4.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Accurate automatic code extraction from tutorial videos is crucial for software developers seeking to reuse the code contained in these videos. Current methods using optical character recognition (OCR) often yield inaccurate results due to code complexity and variations in screencast formats. To address this issue, we introduce CodeT5-OCRfix, an approach that leverages the pre-trained code-aware large language model CodeT5 to enhance code extraction accuracy by post-processing OCRed code. We fir...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [JavaBench: A Benchmark of Object-Oriented Code Generation for Evaluating Large Language Models](../venues/ASE2024/paper_17.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Code generation benchmarks such as HumanEval are widely adopted to evaluate LLMs' capabilities. However, after consolidating the latest 24 benchmarks, we noticed three significant imbalances. First, imbalanced programming language. 95.8\% of benchmarks involve Python, while only 5 benchmarks involve Java, resulting in an insufficient understanding of LLMs' capability to generate Java code. Second, imbalanced code granularity. Function-/statement-level benchmarks account for over 83.3\% of benchm...
  - **Labels**: [benchmark](benchmark.md), [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Knowledge Transfer from High-Resource to Low-Resource Programming Languages for Code LLMs](../venues/OOPSLA2024/paper_2.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Over the past few years, Large Language Models of Code (Code LLMs) have started to have a significant impact on programming practice. Code LLMs are also emerging as building blocks for research in programming languages and software engineering. However, the quality of code produced by a Code LLM varies significantly by programming language. Code LLMs produce impressive results on high-resource programming languages that are well represented in their training data (e.g., Java, Python, or JavaScri...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [LLM-Based Test-Driven Interactive Code Generation: User Study and Empirical Evaluation](../venues/TSE2024/paper_2.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Large language models (LLMs) have shown great potential in automating significant aspects of coding by producing natural code from informal natural language (NL) intent. However, given NL is informal, it does not lend easily to checking that the generated code correctly satisfies the user intent. In this paper, we propose a novel interactive workflow &lt;sc&gt;TiCoder&lt;/sc&gt; for guided intent clarification (i.e., partial formalization) through tests to support the generation of more accurate...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [Language-to-Code Translation with a Single Labeled Example](../venues/EMNLP2024/paper_23.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Tools for translating natural language into code promise natural, open-ended interaction with databases, web APIs, and other software systems. However, this promise is complicated by the diversity and continual development of these systems, each with its own interface and distinct set of features. Building a new language-to-code translator, even starting with a large language model (LM), typically requires annotating a large set of natural language commands with their associated programs. In thi...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)


- [Large Language Models Meet NL2Code: A Survey](../venues/ACL2023/paper_4.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: The task of generating code from a natural language description, or NL2Code, is considered a pressing and significant challenge in code intelligence. Thanks to the rapid development of pre-training techniques, surging large language models are being proposed for code, sparking the advances in NL2Code. To facilitate further research and applications in this field, in this paper, we present a comprehensive survey of 27 existing large language models for NL2Code, and also review benchmarks and metr...
  - **Labels**: [survey](survey.md), [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Lightweight reranking for language model generations](../venues/ACL2024/paper_21.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Large Language Models (LLMs) can exhibit considerable variation in the quality of their sampled outputs. Reranking and selecting the best generation from the sampled set is a popular way of obtaining strong gains in generation quality. In this paper, we present a novel approach for reranking LLM generations. Unlike other techniques that might involve additional inferences or training a specialized reranker, our approach relies on easy to compute pairwise statistics between the generations that h...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Lost at C: a user study on the security implications of large language model code assistants](../venues/USENIXSec2023/paper_1.md), ([USENIXSec2023](../venues/USENIXSec2023/README.md))

  - **Abstract**: Large Language Models (LLMs) such as OpenAI Codex are increasingly being used as AI-based coding assistants. Understanding the impact of these tools on developers' code is paramount, especially as recent work showed that LLMs may suggest cybersecurity vulnerabilities. We conduct a security-driven user study (N=58) to assess code written by student programmers when assisted by LLMs. Given the potential severity of low-level bugs as well as their relative frequency in real-world projects, we taske...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [MLLM-Based UI2Code Automation Guided by UI Layout Information](../venues/ISSTA2025/paper_14.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Converting user interfaces into code (UI2Code) is a crucial step in website development, which is time-consuming and labor-intensive. The automation of UI2Code is essential to streamline this task, beneficial for improving the development efficiency. There exist deep learning-based methods for the task; however, they heavily rely on a large amount of labeled training data and struggle with generalizing to real-world, unseen web page designs. The advent of Multimodal Large Language Models (MLLMs)...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [MPCoder: Multi-user Personalized Code Generator with Explicit and Implicit Style Representation Learning](../venues/ACL2024/paper_12.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated great potential for assisting developers in their daily development. However, most research focuses on generating correct code, how to use LLMs to generate personalized code has seldom been investigated. To bridge this gap, we proposed MPCoder (Multi-user Personalized Code Generator) to generate personalized code for multiple users. To better learn coding style features, we utilize explicit coding style residual learning to capture the syntax code s...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [MapCoder: Multi-Agent Code Generation for Competitive Problem Solving](../venues/ACL2024/paper_16.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Code synthesis, which requires a deep understanding of complex natural language (NL) problem descriptions, generation of code instructions for complex algorithms and data structures, and the successful execution of comprehensive unit tests, presents a significant challenge. Thus, while large language models (LLMs) demonstrate impressive proficiency in natural language processing (NLP), their performance in code generation tasks remains limited. In this paper, we introduce a new approach to code ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md)


- [MultiPL-E: A Scalable and Polyglot Approach to Benchmarking Neural Code Generation](../venues/TSE2023/paper_3.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: Large language models have demonstrated the ability to generate both natural language and programming language text. Although contemporary code generation models are trained on corpora with several programming languages, they are tested using benchmarks that are typically monolingual. The most widely used code generation benchmarks only target Python, so there is little quantitative evidence of how code generation models perform on other programming languages. We propose MultiPL-E, a system for ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)


- [Multitask Pretraining with Structured Knowledge for Text-to-SQL Generation](../venues/ACL2023/paper_9.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Many machine learning-based low-code or no-code applications involve generating code that interacts with structured knowledge. For example, one of the most studied tasks in this area is generating SQL code from a natural language statement. Prior work shows that incorporating context information from the database schema, such as table and column names, is beneficial to model performance on this task. In this work we present a large pretraining dataset and strategy for learning representations of...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)


- [Natural Language Commanding via Program Synthesis](../venues/Microsoft2023/paper_1.md), ([Microsoft2023](../venues/Microsoft2023/README.md))

  - **Abstract**: We present Semantic Interpreter, a natural language-friendly AI system for productivity software such as Microsoft Office that leverages large language models (LLMs) to execute user intent across application features. While LLMs are excellent at understanding user intent expressed as natural language, they are not sufficient for fulfilling application-specific user intent that requires more than text-to-text transformations. We therefore introduce the Office Domain Specific Language (ODSL), a co...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [No Need to Lift a Finger Anymore? Assessing the Quality of Code Generation by ChatGPT](../venues/TSE2024/paper_6.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated impressive capabilities across various natural language processing (NLP) tasks, such as machine translation, question answering, summarization, and so on. Additionally, LLMs are also highly valuable in supporting software engineering tasks, particularly in the field of code generation. Automatic code generation is a process of automatically generating source code or executable code based on given specifications or requirements, improving developer p...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [On Extracting Specialized Code Abilities from Large Language Models: A Feasibility Study](../venues/ICSE2024/paper_6.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Recent advances in large language models (LLMs) significantly boost their usage in software engineering. However, training a well-performing LLM demands a substantial workforce for data collection and annotation. Moreover, training datasets may be proprietary or partially open, and the process often requires a costly GPU cluster. The intellectual property value of commercial LLMs makes them attractive targets for imitation attacks, but creating an imitation model with comparable parameters still...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [On Leakage of Code Generation Evaluation Datasets](../venues/EMNLP2024/paper_15.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: In this paper, we consider contamination by code generation test sets, in particular in their use in modern large language models.We discuss three possible sources of such contamination and show findings supporting each of them: (i) direct data leakage, (ii) indirect data leakage through the use of synthetic data and (iii) overfitting to evaluation sets during model selection.To address this, we release Less Basic Python Problems (LBPP): an uncontaminated new benchmark of 161 prompts with their ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)


- [On Sample-Efficient Code Generation](../venues/EMNLP2023/paper_18.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Large language models often struggle to predict runtime behavior in code generation tasks, leading to a reliance on rejection sampling (best-of-n) to generate multiple code snippets then select the best. Our distinction is reducing sampling costs, without compromising generation quality. We introduce EFFICODE, a novel framework that prioritizes sampling on test problems that models can solve. We show how EFFICODE estimates solvability to optimize computational costs during multiple sampling. Bas...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [On the Impacts of Contexts on Repository-Level Code Generation](../venues/NAACL2025/paper_11.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: CodeLLMs are widely used for code generation, yet their ability to handle repository-level dependencies remains underexplored. We introduce RepoExec, a benchmark for evaluating repository-level code generation, focusing on executability, functional correctness, and dependency utilization. Our study evaluates 18 models, revealing that retaining full dependency context yields the best performance, while smaller context sizes can be misleading. Pretrained LLMs excel in correctness but often reimple...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [Oracle-Guided Program Selection from Large Language Models](../venues/ISSTA2024/paper_9.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: While large language models (LLMs) have shown significant advancements in code generation, their susceptibility to producing incorrect code poses a significant challenge to the adoption of LLM-generated programs. This issue largely stems from the reliance on natural language descriptions as informal oracles in code generation. Current strategies to mitigate this involve selecting the best program from multiple LLM-generated alternatives, judged by criteria like the consistency of their execution...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [PACGBI: A Pipeline for Automated Code Generation from Backlog Items](../venues/ASE2024/paper_34.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: While there exist several tools to leverage Large Language Models (LLMs) for code generation, their capabilities are limited to the source code editor and are disconnected from the overall software development process. These tools typically generate standalone code snippets that still require manual integration into the codebase. There is still a lack of integrated solutions that seamlessly automate the entire development cycle, from backlog items to code generation and merge requests. We presen...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [PTD-SQL: Partitioning and Targeted Drilling with LLMs in Text-to-SQL](../venues/EMNLP2024/paper_19.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have emerged as powerful tools for Text-to-SQL tasks, exhibiting remarkable reasoning capabilities. Different from tasks such as math word problem and commonsense reasoning, SQL solutions have a relatively fixed pattern. This facilitates the investigation of whether LLMs can benefit from categorical thinking, mirroring how humans acquire knowledge through inductive reasoning based on comparable examples. In this study, we propose that employing query group partitioni...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [Personalized Distillation: Empowering Open-Sourced LLMs with Adaptive Learning for Code Generation](../venues/EMNLP2023/paper_2.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: With the rise of powerful closed-sourced LLMs (ChatGPT, GPT-4), there are increasing interests in distilling the capabilies of close-sourced LLMs to smaller open-sourced LLMs. Previous distillation methods usually prompt ChatGPT to generate a set of instructions and answers, for the student model to learn. However, such standard distillation approach neglects the merits and conditions of the student model. Inspired by modern teaching principles, we design a personalised distillation process, in ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Preference-Guided Refactored Tuning for Retrieval Augmented Code Generation](../venues/ASE2024/paper_1.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Retrieval-augmented code generation utilizes Large Language Models as the generator and significantly expands their code generation capabilities by providing relevant code, documentation, and more via the retriever. The current approach suffers from two primary limitations: 1) information redundancy. The indiscriminate inclusion of redundant information can result in resource wastage and may misguide generators, affecting their effectiveness and efficiency. 2) preference gap. Due to different op...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Python Code Generation by Asking Clarification Questions](../venues/ACL2023/paper_10.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Code generation from text requires understanding the user’s intent from a natural languagedescription and generating an executable code snippet that satisfies this intent. While recent pretrained language models demonstrate remarkable performance for this task, these models fail when the given natural language description is under-specified. In this work, we introduce a novel and more realistic setup for this task. We hypothesize that the under-specification of a natural language description can...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [PythonSaga: Redefining the Benchmark to Evaluate Code Generating LLMs](../venues/EMNLP2024/paper_22.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Driven by the surge in code generation using large language models (LLMs), numerous benchmarks have emerged to evaluate these LLMs capabilities. We conducted a large-scale human evaluation of *HumanEval* and *MBPP*, two popular benchmarks for Python code generation, analyzing their diversity and difficulty. Our findings unveil a critical bias towards a limited set of programming concepts, neglecting most of the other concepts entirely. Furthermore, we uncover a worrying prevalence of easy tasks ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)


- [Quantifying Contamination in Evaluating Code Generation Capabilities of Language Models](../venues/ACL2024/paper_4.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: While large language models have achieved remarkable performance on various code generation benchmarks, there have been growing concerns regarding potential contamination of these benchmarks as they may be leaked into pretraining and finetuning data. While recent work has investigated contamination in natural language generation and understanding tasks, there has been less extensive research into how data contamination impacts the evaluation of code generation, which is critical for understandin...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [ROCODE: Integrating Backtracking Mechanism and Program Analysis in Large Language Models for Code Generation](../venues/ICSE2025/paper_40.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large language models (LLMs) have achieved impressive performance in code generation recently, offering programmers revolutionary assistance in software development. However, due to the auto-regressive nature of LLMs, they are susceptible to error accumulation during code generation. Once an error is produced, LLMs can merely continue to generate the subsequent code conditioned on it, given their inability to adjust previous outputs. Existing LLM-based approaches typically consider post-revising...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Revisiting the Impact of Pursuing Modularity for Code Generation](../venues/EMNLP2024/paper_13.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Modular programming, which aims to construct the final program by integrating smaller, independent building blocks, has been regarded as a desirable practice in software development. However, with the rise of recent code generation agents built upon large language models (LLMs), a question emerges: is this traditional practice equally effective for these new tools? In this work, we assess the impact of modularity in code generation by introducing a novel metric for its quantitative measurement. ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [SGCode: A Flexible Prompt-Optimizing System for Secure Generation of Code](../venues/CCS2024/paper_9.md), ([CCS2024](../venues/CCS2024/README.md))

  - **Abstract**: This paper introduces SGCode, a flexible prompt-optimizing system to generate secure code with large language models (LLMs). SGCode integrates recent prompt-optimization approaches with LLMs in a unified system accessible through front-end and back-end APIs, enabling users to 1) generate secure code, which is free of vulnerabilities, 2) review and share security analysis, and 3) easily switch from one prompt optimization approach to another, while providing insights on model and system performan...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [code model](code_model.md), [code model security](code_model_security.md)


- [SOEN-101: Code Generation by Emulating Software Process Models Using Large Language Model Agents](../venues/ICSE2025/paper_43.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Software process models are essential to facilitate collaboration and communication among software teams to solve complex development tasks. Inspired by these software engineering practices, we present FlowGen - a code generation framework that emulates software process models based on multiple Large Language Model (LLM) agents. We emulate three process models, FlowGenWaterfall, FlowGenTDD, and FlowGenScrum, by assigning LLM agents to embody roles (i.e., requirement engineer, architect, develope...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md)


- [SWE-GPT: A Process-Centric Language Model for Automated Software Improvement](../venues/ISSTA2025/paper_32.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated remarkable performance in code generation, significantly enhancing the coding efficiency of developers. Recent advancements in LLM-based agents have led to significant progress in end-to-end automatic software engineering (ASE), particularly in software maintenance (e.g., fixing software issues) and evolution (e.g., adding new features). Despite these encouraging advances, current research faces two major challenges. First, state-of-the-art performa...
  - **Labels**: [general coding task](general_coding_task.md), [code generation](code_generation.md), [program synthesis](program_synthesis.md), [software maintenance and deployment](software_maintenance_and_deployment.md), [agent design](agent_design.md)


- [SecCodePLT: A Unified Platform for Evaluating the Security of Code GenAI](../venues/arXiv2024/paper_3.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Language models for code (CodeLMs) have emerged as powerful tools for code-related tasks, outperforming traditional methods and standard machine learning approaches. However, these models are susceptible to security vulnerabilities, drawing increasing research attention from domains such as software engineering, artificial intelligence, and cybersecurity. Despite the growing body of research focused on the security of CodeLMs, a comprehensive survey in this area remains absent. To address this g...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model security](code_model_security.md), [benchmark](benchmark.md)


- [Self-Collaboration Code Generation via ChatGPT](../venues/TOSEM2024/paper_5.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Although large language models (LLMs) have demonstrated remarkable code-generation ability, they still struggle with complex tasks. In real-world software development, humans usually tackle complex tasks through collaborative teamwork, a strategy that significantly controls development complexity and enhances software quality. Inspired by this, we present a self-collaboration framework for code generation employing LLMs, exemplified by ChatGPT. Specifically, through role instructions, (1) Multip...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Self-Planning Code Generation with Large Language Models](../venues/TOSEM2024/paper_2.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Although large language models (LLMs) have demonstrated impressive ability in code generation, they are still struggling to address the complicated intent provided by humans. It is widely acknowledged that humans typically employ planning to decompose complex problems and schedule solution steps prior to implementation. To this end, we introduce planning into code generation to help the model understand complex intent and reduce the difficulty of problem-solving. This paper proposes a self-plann...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [planning](planning.md), [empirical study](empirical_study.md)


- [Sifting through the Chaff: On Utilizing Execution Feedback for Ranking the Generated Code Candidates](../venues/ASE2024/paper_4.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Large Language Models (LLMs), such as GPT-4, StarCoder, and Code Llama, are transforming the way developers approach programming by automatically generating code based on given contexts, such as natural language descriptions or incomplete surrounding code. Despite advancements, generating syntactically and semantically correct code remains challenging, especially for complex programming tasks. Existing approaches typically generate multiple candidate solutions using LLMs to increase the likeliho...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Smaller but Better: Self-Paced Knowledge Distillation for Lightweight yet Effective LCMs](../venues/FSE2025/paper_42.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Large code models (LCMs) have remarkably advanced the field of code generation. Despite their impressive capabilities, they still face practical deployment issues, such as high inference costs, limited accessibility of proprietary LCMs, and adaptability issues of ultra-large LCMs. These issues highlight the critical need for more accessible, lightweight yet effective LCMs. Knowledge distillation (KD) offers a promising solution, which transfers the programming capabilities of larger, advanced LC...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md)


- [Socratic Human Feedback (SoHF): Expert Steering Strategies for LLM Code Generation](../venues/EMNLP2024/paper_21.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large Language Models (LLMs) are increasingly used for generating code solutions, empowered by features like self-debugging and self-reflection. However, LLMs often struggle with complex programming problems without human guidance. This paper investigates the strategies employed by expert programmers to steer code-generating LLMs toward successful outcomes. Through a study involving experts using natural language to guide GPT-4, Gemini Ultra, and, Claude 3.5 Sonnet on highly difficult programmin...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [SpecGen: Automated Generation of Formal Program Specifications via Large Language Models](../venues/ICSE2025/paper_7.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: In the software development process, formal program specifications play a crucial role in various stages, including requirement analysis, software testing, and verification. However, manually crafting formal program specifications is rather difficult, making the job time-consuming and labor-intensive. Moreover, it is even more challenging to write specifications that correctly and comprehensively describe the semantics of complex programs. To reduce the burden on software developers, automated s...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md), [program verification](program_verification.md)


- [Statically Contextualizing Large Language Models with Typed Holes](../venues/OOPSLA2024/paper_1.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Large language models (LLMs) have reshaped the landscape of program synthesis. However, contemporary LLM-based code completion systems often hallucinate broken code because they lack appropriate code context, particularly when working with definitions that are neither in the training data nor near the cursor. This paper demonstrates that tighter integration with the type and binding structure of the programming language in use, as exposed by its language server, can help address this contextuali...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)


- [StepCoder: Improving Code Generation with Reinforcement Learning from Compiler Feedback](../venues/ACL2024/paper_13.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: The advancement of large language models (LLMs) has significantly propelled the field of code generation. Previous work integrated reinforcement learning (RL) with compiler feedback for exploring the output space of LLMs to enhance code generation quality. However, the lengthy code generated by LLMs in response to complex human requirements makes RL exploration a challenge. Also, since the unit tests may not cover the complicated code, optimizing LLMs by using these unexecuted code snippets is i...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Symbolic Planning and Code Generation for Grounded Dialogue](../venues/EMNLP2023/paper_4.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Large language models (LLMs) excel at processing and generating text and code. However, LLMs have had limited applicability in grounded task-oriented dialogue as they are difficult to steer toward task objectives and fail to handle novel grounding. We present a modular and interpretable grounded dialogue system that addresses these shortcomings by composing LLMs with a symbolic planner and grounded code execution. Our system, consists of a reader and planner: the reader leverages an LLM to conve...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [planning](planning.md)


- [Test-Driven Development and LLM-based Code Generation](../venues/ASE2024/paper_25.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Recent Large Language Models (LLMs) have demonstrated significant capabilities in generating code snippets directly from problem statements. This increasingly automated process mirrors traditional human-led software development, where code is often written in response to a requirement. Historically, Test-Driven Development (TDD) has proven its merit, requiring developers to write tests before the functional code, ensuring alignment with the initial problem statements. Applying TDD principles to ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [The First Prompt Counts the Most! An Evaluation of Large Language Models on Iterative Example-Based Code Generation](../venues/ISSTA2025/paper_24.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: The capabilities of Large Language Models (LLMs) in code generation have been extensively studied, particularly for implementing target functionalities from natural-language descriptions. As an alternative to natural language, input-output (I/O) examples provide an accessible, unambiguous, and flexible way to describe functionalities. However, their inherent diversity, opaqueness, and incompleteness impose greater challenges for understanding and implementing the target requirements. Therefore, ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Towards AI-Assisted Synthesis of Verified Dafny Methods](../venues/FSE2024/paper_23.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Large language models show great promise in many domains, including programming. A promise is easy to make but hard to keep, and language models often fail to keep their promises, generating erroneous code. A promising avenue to keep models honest is to incorporate formal verification: generating programs’ specifications as well as code so that the code can be proved correct with respect to the specifications. Unfortunately, existing large language models show a severe lack of proficiency in ver...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Towards Greener Yet Powerful Code Generation via Quantization: An Empirical Study](../venues/FSE2023/paper_8.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: ML-powered code generation aims to assist developers to write code in a more productive manner by intelligently generating code blocks based on natural language prompts. Recently, large pretrained deep learning models have pushed the boundary of code generation and achieved impressive performance. However, the huge number of model parameters poses a significant challenge to their adoption in a typical software development environment, where a developer might use a standard laptop or mid-size ser...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [Towards Neural Synthesis for SMT-Assisted Proof-Oriented Programming](../venues/ICSE2025/paper_8.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Proof-oriented programs mix computational content with proofs of program correctness. However, the human effort involved in programming and proving is still substantial, despite the use of Satisfiability Modulo Theories (SMT) solvers to automate proofs in languages such as F*. Seeking to spur research on using AI to automate the construction of proof-oriented programs, we curate a dataset of 600K lines of open-source F* programs and proofs, including software used in production systems ranging f...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)


- [Towards Understanding the Characteristics of Code Generation Errors Made by Large Language Models](../venues/ICSE2025/paper_53.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated unprecedented capabilities in code generation. However, there remains a limited understanding of code generation errors that LLMs can produce. To bridge the gap, we conducted an in-depth analysis of code generation errors across six representative LLMs on the HumanEval dataset. Specifically, we first employed open coding and thematic analysis to distill a comprehensive taxonomy of code generation errors. We analyzed two dimensions of error character...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)


- [UICoder: Finetuning Large Language Models to Generate User Interface Code through Automated Feedback](../venues/NAACL2024/paper_5.md), ([NAACL2024](../venues/NAACL2024/README.md))

  - **Abstract**: Many large language models (LLMs) struggle to consistently generate UI code that compiles and produces visually relevant designs. Existing approaches to improve generation rely either on expensive human feedback or distilling a proprietary model. In this paper, we explore the use of automated feedback (compilers and multi-modal models) to guide LLMs to generate high-quality UI code. Our method starts with an existing LLM and iteratively produces improved models by self-generating a large synthet...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [UniCoder: Scaling Code Large Language Model via Universal Code](../venues/ACL2024/paper_10.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Intermediate reasoning or acting steps have successfully improved large language models (LLMs) for handling various downstream natural language processing (NLP) tasks.When applying LLMs for code generation, recent works mainly focus on directing the models to articulate intermediate natural-language reasoning steps, as in chain-of-thought (CoT) prompting, and then output code with the natural language or other structured intermediate steps. However, such output is not suitable for code translati...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [IR code model](IR_code_model.md)


- [Verified Code Transpilation with LLMs](../venues/NeurIPS2024/paper_4.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Domain-specific languages (DSLs) are integral to various software workflows. Such languages offer domain-specific optimizations and abstractions that improve code readability and maintainability. However, leveraging these languages requires developers to rewrite existing code using the specific DSL's API. While large language models (LLMs) have shown some success in automatic code transpilation, none of them provide any functional correctness guarantees on the transpiled code. Another approach f...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Verified multi-step synthesis using large language models and monte carlo tree search](../venues/NeurIPS2024/paper_3.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: We present an approach using Monte Carlo Tree Search (MCTS) to guide Large Language Models (LLMs) to generate verified programs in Dafny, Lean and Coq. Our method, which we call VMCTS, leverages the verifier inside the search algorithm by checking partial programs at each step. In combination with the LLM prior, the verifier feedback raises the synthesis capabilities of open source models. On a set of five verified programming problems, we find that in four problems where the base model cannot s...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [When to Stop? Towards Efficient Code Generation in LLMs with Excess Token Prevention](../venues/ISSTA2024/paper_12.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Code generation aims to automatically generate code snippets that meet given natural language requirements and plays an important role in software development. Although Code LLMs have shown excellent performance in this domain, their long generation time poses a signification limitation in practice use. In this paper, we first conduct an in-depth preliminary study with different Code LLMs on code generation task and identify a significant efficiency issue, i.e., continual generation of excess to...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md)


- [Who Wrote this Code? Watermarking for Code Generation](../venues/ACL2024/paper_15.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Since the remarkable generation performance of large language models raised ethical and legal concerns, approaches to detect machine-generated text by embedding watermarks are being developed.However, we discover that the existing works fail to function appropriately in code generation tasks due to the task’s nature of having low entropy.Extending a logit-modifying watermark method, we propose Selective WatErmarking via Entropy Thresholding (SWEET), which enhances detection ability and mitigates...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model security](code_model_security.md)


- [{C}ode{T}ree: Agent-guided Tree Search for Code Generation with Large Language Models](../venues/NAACL2025/paper_5.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Pretrained on massive amounts of code and text data, large language models (LLMs) have demonstrated remarkable achievements in performing code generation tasks. With additional execution-based feedback, these models can act as agents with capabilities to self-refine and improve generated code autonomously. However, on challenging coding tasks with extremely large search space, current agentic approaches still struggle with multi-stage planning, generating, and debugging. To address this problem,...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [planning](planning.md)


- [{D}esign2{C}ode: Benchmarking Multimodal Code Generation for Automated Front-End Engineering](../venues/NAACL2025/paper_6.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Generative AI has made rapid advancements in recent years, achieving unprecedented capabilities in multimodal understanding and code generation. This can enable a new paradigm of front-end development in which multimodal large language models (MLLMs) directly convert visual designs into code implementations. In this work, we construct Design2Code {--} the first real-world benchmark for this task. Specifically, we manually curate 484 diverse real-world webpages as test cases and develop a set of ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md)


- [{PLEX}: Adaptive Parameter-Efficient Fine-Tuning for Code {LLM}s using Lottery-Tickets](../venues/NAACL2025/paper_1.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Fine-tuning large language models (LLMs) for code generation is challenging due to computational costs and the underrepresentation of some programming languages (PLs) in pre-training. We propose PLEX, a lottery-ticket based parameter-efficient fine-tuning (PEFT) method that adapts LLMs to either well-supported and underrepresented PLs.During lottery ticket selection, PLEX employs a dual strategy: for well-represented PLs, it leverages the LLM{'}s full parametric knowledge by selecting from full ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md)


## Code Completion

- [A Static Evaluation of Code Completion by Large Language Models](../venues/ACL2023/paper_12.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Large language models trained on code have shown great potential to increase productivity of software developers. Several execution-based benchmarks have been proposed to evaluate functional correctness of model-generated code on simple programming problems. Nevertheless, it is expensive to perform the same evaluation on complex real-world projects considering the execution cost. On the other hand, static analysis tools such as linters, which can detect errors without running the program, haven’...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)


- [Attribution-guided Adversarial Code Prompt Generation for Code Completion Models](../venues/ASE2024/paper_45.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Large language models have made significant progress in code completion, which may further remodel future software development. However, these code completion models are found to be highly risky as they may introduce vulnerabilities unintentionally or be induced by a special input, i.e., adversarial code prompt. Prior studies mainly focus on the robustness of these models, but their security has not been fully analyzed.In this paper, we propose a novel approach AdvPro that can automatically gene...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model security](code_model_security.md)


- [CCTest: Testing and Repairing Code Completion Systems](../venues/ICSE2023/paper_2.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Code completion, a highly valuable topic in the software development domain, has been increasingly promoted for use by recent advances in large language models (LLMs). To date, visible LLM-based code completion frameworks such as GitHub Copilot and GPT are trained using deep learning over vast quantities of unstructured text and open source code. As the paramount component and the cornerstone in daily programming tasks, code completion has largely boosted professionals' efficiency in building re...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [CoEdPilot: Recommending Code Edits with Learned Prior Edit Relevance, Project-wise Awareness, and Interactive Nature](../venues/ISSTA2024/paper_8.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Recent years have seen the development of LLM-based code generation. Compared to generating code in a software project, incremental code edits are empirically observed to be more frequent. The emerging code editing approaches usually formulate the problem as generating an edit based on known relevant prior edits and context. However, practical code edits can be more complicated. First, an editing session can include multiple (ir)relevant edits to the code under edit. Second, the inference of the...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [DiffCoder: Enhancing Large Language Model on API Invocation via Analogical Code Exercises](../venues/FSE2024/paper_16.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: The task of code generation aims to generate code solutions based on given programming problems. Recently, code large language models (code LLMs) have shed new light on this task, owing to their formidable code generation capabilities. While these models are powerful, they seldom focus on further improving the accuracy of library-oriented API invocation. Nonetheless, programmers frequently invoke APIs in routine coding tasks. In this paper, we aim to enhance the proficiency of existing code LLMs...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [Domain Adaptive Code Completion via Language Models and Decoupled Domain Databases](../venues/ASE2023/paper_18.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated remarkable performance in code completion. However, due to the lack of domain-specific knowledge, they may not be optimal in completing code that requires intensive domain knowledge for example completing the library names. Although there are several works that have confirmed the effectiveness of fine-tuning techniques to adapt language models for code completion in specific domains. They are limited by the need for constant fine-tuning of the model...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [DroidCoder: Enhanced Android Code Completion with Context-Enriched Retrieval-Augmented Generation](../venues/ASE2024/paper_13.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Android is the most popular mobile operating system. However, Android development requires extensive coding, especially for unique features such as lifecycle callbacks and UI widgets. Existing code completion methods typically utilize Retrieval-Augmented Generation (RAG) to provide contextual information for pre-trained code large language models (Code LLMs) to perform completion. Despite considerable progress in these methods, their effectiveness in Android development remains limited. This is ...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [EvoR: Evolving Retrieval for Code Generation](../venues/EMNLP2024/paper_3.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Recently the retrieval-augmented generation (RAG) has been successfully applied in code generation. However, existing pipelines for retrieval-augmented code generation (RACG) employ static knowledge bases with a single source, limiting the adaptation capabilities of Large Language Models (LLMs) to domains they have insufficient knowledge of. In this work, we develop a novel pipeline, EVOR, that employs the synchronous evolution of both queries and diverse knowledge bases. On two realistic settin...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [source code model](source_code_model.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [Follow-Up Attention: An Empirical Study of Developer and Neural Model Code Exploration](../venues/TSE2024/paper_12.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Recent neural models of code, such as OpenAI Codex and AlphaCode, have demonstrated remarkable proficiency at code generation due to the underlying attention mechanism. However, it often remains unclear how the models actually process code, and to what extent their reasoning and the way their attention mechanism scans the code matches the patterns of developers. A poor understanding of the model reasoning process limits the way in which current neural models are leveraged today, so far mostly fo...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [benchmark](benchmark.md)


- [Grace: Language Models Meet Code Edits](../venues/FSE2023/paper_4.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Developers spend a significant amount of time in editing code for a variety of reasons such as bug fixing or adding new features. Designing effective methods to predict code edits has been an active yet challenging area of research due to the diversity of code edits and the difficulty of capturing the developer intent. In this work, we address these challenges by endowing pre-trained large language models (LLMs) with the knowledge of relevant prior associated edits, which we call the Grace (Gene...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph](../venues/ASE2024/paper_10.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: The performance of repository-level code completion depends upon the effective leverage of both general and repository-specific knowledge. Despite the impressive capability of code LLMs in general code completion tasks, they often exhibit less satisfactory performance on repository-level completion due to the lack of repository-specific knowledge in these LLMs. To address this problem, we propose GraphCoder, a retrieval-augmented code completion framework that leverages LLMs' general code knowle...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [Grounded Copilot: How Programmers Interact with Code-Generating Models](../venues/OOPLSA2023/paper_1.md), ([OOPLSA2023](../venues/OOPLSA2023/README.md))

  - **Abstract**: Powered by recent advances in code-generating models, AI assistants like Github Copilot promise to change the face of programming forever. But what is this new face of programming? We present the first grounded theory analysis of how programmers interact with Copilot, based on observing 20 participants—with a range of prior experience using the assistant—as they solve diverse programming tasks across four languages. Our main finding is that interactions with programming assistants are bimodal: i...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)


- [HiRoPE: Length Extrapolation for Code Models Using Hierarchical Position](../venues/ACL2024/paper_2.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Addressing the limitation of context length in large language models for code-related tasks is the primary focus of this paper. Existing LLMs are constrained by their pre-trained context lengths, leading to performance issues in handling long complex code sequences. Inspired by how human programmers navigate code, we introduce Hierarchical Rotary Position Embedding (HiRoPE), a novel approach that enhances the traditional rotary position embedding into a hierarchical format based on the hierarchi...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [LLM-Based Method Name Suggestion with Automatically Generated Context-Rich Prompts](../venues/FSE2025/paper_11.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Accurate method naming is crucial for code readability and maintainability. However, manually creating concise and meaningful names remains a significant challenge. To this end, in this paper, we propose an approach based on Large Language Model (LLMs) to suggest method names according to function descriptions. The key of the approach is ContextCraft, an automated algorithm for generating context-rich prompts for LLM that suggests the expected method names according to the prompts. For a given q...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [LLMs Meet Library Evolution: Evaluating Deprecated API Usage in LLM-Based Code Completion](../venues/ICSE2025/paper_68.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large language models (LLMs), pre-trained or fine-tuned on large code corpora, have shown effectiveness in generating code completions. However, in LLM-based code completion, LLMs may struggle to use correct and up-to-date Application Programming Interfaces (APIs) due to the rapid and continuous evolution of libraries. While existing studies have highlighted issues with predicting incorrect APIs, the specific problem of deprecated API usage in LLM-based code completion has not been thoroughly in...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [Language Models for Code Completion: A Practical Evaluation](../venues/ICSE2024/paper_26.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Transformer-based language models for automatic code completion have shown great promise so far, yet the evaluation of these models rarely uses real data. This study provides both quantitative and qualitative assessments of three public code language models when completing real-world code. We first developed an open-source IDE extension, Code4Me, for the online evaluation of the models. We collected real auto-completion usage data for over a year from more than 1200 users, resulting in over 600K...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [LongCoder: {A} Long-Range Pre-trained Language Model for Code Completion](../venues/ICML2023/paper_1.md), ([ICML2023](../venues/ICML2023/README.md))

  - **Abstract**: In this paper, we introduce a new task for code completion that focuses on handling long code input and propose a sparse Transformer model, called LongCoder, to address this task. LongCoder employs a sliding window mechanism for self-attention and introduces two types of globally accessible tokens-bridge tokens and memory tokens-to improve performance and efficiency. Bridge tokens are inserted throughout the input sequence to aggregate local information and facilitate global interaction, while m...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [On the Applicability of Language Models to Block-Based Programs](../venues/ICSE2023/paper_8.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Block-based programming languages like SCRATCH are increasingly popular for programming education and end-user programming. Recent program analyses build on the insight that source code can be modelled using techniques from natural language processing. Many of the regularities of source code that support this approach are due to the syntactic overhead imposed by textual programming languages. This syntactic overhead, however, is precisely what block-based languages remove in order to simplify pr...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [On the Evaluation of Neural Code Translation: Taxonomy and Benchmark](../venues/ASE2023/paper_14.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: In recent years, neural code translation has gained increasing attention. While most of the research focuses on improving model architectures and training processes, we notice that the evaluation process and benchmark for code translation models are severely limited: they primarily treat source code as natural languages and provide a holistic accuracy score while disregarding the full spectrum of model capabilities across different translation types and complexity. In this paper, we present a co...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)


- [RepoSim: Evaluating Prompt Strategies for Code Completion via User Behavior Simulation](../venues/ASE2024/paper_33.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Large language models (LLMs) have revolutionized code completion tasks. IDE plugins such as MarsCode can generate code recommendations, saving developers significant time and effort. However, current evaluation methods for code completion are limited by their reliance on static code benchmarks, which do not consider human interactions and evolving repositories. This paper proposes RepoSim, a novel benchmark designed to evaluate code completion tasks by simulating the evolving process of reposito...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [Repository-Level Prompt Generation for Large Language Models of Code](../venues/ICML2023/paper_2.md), ([ICML2023](../venues/ICML2023/README.md))

  - **Abstract**: With the success of large language models (LLMs) of code and their use as code assistants (e.g. Codex used in GitHub Copilot), techniques for introducing domain-specific knowledge in the prompt design process become important. In this work, we propose a framework called Repo-Level Prompt Generator that learns to generate example-specific prompts using prompt proposals. The prompt proposals take context from the entire repository, thereby incorporating both the structure of the repository and the...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [Rewriting the Code: A Simple Method for Large Language Model Augmented Code Search](../venues/ACL2024/paper_8.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: In code search, the Generation-Augmented Retrieval (GAR) framework, which generates exemplar code snippets to augment queries, has emerged as a promising strategy to address the principal challenge of modality misalignment between code snippets and natural language queries, particularly with the demonstrated code generation capabilities of Large Language Models (LLMs). Nevertheless, our preliminary investigations indicate that the improvements conferred by such an LLM-augmented framework are som...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)


- [TrojanPuzzle: Covertly Poisoning Code-Suggestion Models](../venues/S&P2024/paper_3.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: With tools like GitHub Copilot, automatic code suggestion is no longer a dream in software engineering. These tools, based on large language models, are typically trained on massive corpora of code mined from unvetted public sources. As a result, these models are susceptible to data poisoning attacks where an adversary manipulates the model’s training by injecting malicious data. Poisoning attacks could be designed to influence the model’s suggestions at run time for chosen contexts, such as ind...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [code generation](code_generation.md), [code completion](code_completion.md)


- [Type-Aware Constraining for Code LLMs](../venues/ICLR2025/paper_1.md), ([ICLR2025](../venues/ICLR2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have achieved notable success in code generation. However, they still frequently produce invalid code, as they do not precisely model formal aspects of programming languages. Constrained decoding is a promising approach to alleviate this issue and has been successfully applied to domain-specific languages and syntactic features, but is not able to enforce more semantic features, such as well-typedness. To address this issue, we introduce type-aware constrained decodi...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md)


- [When Neural Code Completion Models Size up the Situation: Attaining Cheaper and Faster Completion through Dynamic Model Inference](../venues/ICSE2024/paper_7.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Leveraging recent advancements in large language models, modern neural code completion models have demonstrated the capability to generate highly accurate code suggestions. However, their massive size poses challenges in terms of computational costs and environmental impact, hindering their widespread adoption in practical scenarios. Dynamic inference emerges as a promising solution, as it allocates minimal computation during inference while maintaining the model's performance. In this research,...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)


## Program Repair

- [AdverIntent-Agent: Adversarial Reasoning for Repair Based on Inferred Program Intent](../venues/ISSTA2025/paper_18.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Automated program repair (APR) has shown promising results, particularly with the use of neural networks. Currently, most APR tools focus on code transformations specified by test suites, rather than reasoning about the program’s intent and the high-level bug specification. Without a proper understanding of program intent, these tools tend to generate patches that overfit incomplete test suites and fail to reflect the developer’s intentions. However, reasoning about program intent is challenging...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [Agentless: Demystifying LLM-based Software Engineering Agents](../venues/FSE2025/paper_2.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Recent advancements in large language models (LLMs) have significantly advanced the automation of software development tasks, including code synthesis, program repair, and test generation. More recently, researchers and industry practitioners have developed various autonomous LLM agents to perform end-to-end software development tasks. These agents are equipped with the ability to use tools, run commands, observe feedback from the environment, and plan for future actions. However, the complexity...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Aligning the Objective of LLM-Based Program Repair](../venues/ICSE2025/paper_49.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large language models (LLMs) have achieved decent results on automated program repair (APR). However, the next token prediction training objective of decoder-only LLMs (e.g., GPT-4) is misaligned with the masked span prediction objective of current infilling-style methods, which impedes LLMs from fully leveraging pre-trained knowledge for program repair. In addition, while some LLMs can locate and repair bugs in certain functions using the related artifacts (e.g., test cases), existing methods s...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [An Empirical Study on Fine-Tuning Large Language Models of Code for Automated Program Repair](../venues/ASE2023/paper_2.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: The advent of large language models (LLMs) has opened up new opportunities for automated program repair (APR). In particular, some recent studies have explored how to leverage large language models of code (LLMCs) for program repair tasks and show promising results. However, most of them adopt the zero/few-shot learning paradigm for APR, which directly use LLMCs to generate the possibly correct code given its surrounding context. Though effective, the repair capabilities of LLMCs based on the fi...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Are “Solved Issues” in SWE-bench Really Solved Correctly?](../venues/arXiv2025/paper_15.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Automated issue solving aims to resolve real-world issues in software repositories. The most popular benchmarks for automated issue solving are SWE-bench and its human-filtered subset SWE-bench Verified. These benchmarks leverage testing to validate generated patches. However, because testing is rarely exhaustive, a patch may pass the tests but nevertheless fail to match the developers' expectations. Unfortunately, it is currently unclear to what extent evaluations performed with SWE-bench suffe...
  - **Labels**: [benchmark](benchmark.md), [code generation](code_generation.md), [program repair](program_repair.md)


- [AutoCodeRover: Autonomous Program Improvement](../venues/ISSTA2024/paper_20.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Researchers have made significant progress in automating the software development process in the past decades. Automated techniques for issue summarization, bug reproduction, fault localization, and program repair have been built to ease the workload of developers. Recent progress in Large Language Models (LLMs) has significantly impacted the development process, where developers can use LLM-based programming assistants to achieve automated coding. Nevertheless, software engineering involves the...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automated Program Repair in the Era of Large Pre-Trained Language Models](../venues/ICSE2023/paper_4.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Automated Program Repair (APR) aims to help developers automatically patch software bugs. However, current state-of-the-art traditional and learning-based APR techniques face the problem of limited patch variety, failing to fix complicated bugs. This is mainly due to the reliance on bug-fixing datasets to craft fix templates (traditional) or directly predict potential patches (learning-based). Large Pre-Trained Language Models (LLMs), trained using billions of text/code tokens, can potentially h...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automated Program Repair via Conversation: Fixing 162 out of 337 Bugs for $0.42 Each using ChatGPT](../venues/ISSTA2024/paper_10.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Automated Program Repair (APR) aims to automatically generate patches for buggy programs. Traditional APR techniques suffer from a lack of patch variety as they rely heavily on handcrafted or mined bug fixing patterns and cannot easily generalize to other bug/fix types. To address this limitation, recent APR work has been focused on leveraging modern Large Language Models (LLMs) to directly generate patches for APR. Such LLM-based APR tools work by first constructing an input prompt built using ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automated Program Repair via Conversation:Fixing 162 out of 337 Bugs for $0.42 Each using ChatGPT](../venues/ISSTA2024/paper_2.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Automated Program Repair (APR) aims to automatically generate patches for buggy programs. Traditional APR techniques suffer from a lack of patch variety as they rely heavily on handcrafted or mined bug fixing patterns and cannot easily generalize to other bug/fix types. To address this limitation, recent APR work has been focused on leveraging modern Large Language Models (LLMs) to directly generate patches for APR. Such LLM-based APR tools work by first constructing an input prompt built using ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automated Repair of Programs from Large Language Models](../venues/ICSE2023/paper_3.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Large language models such as Codex, have shown the capability to produce code for many programming tasks. However, the success rate of existing models is low, especially for complex programming tasks. One of the reasons is that language models lack awareness of program semantics, resulting in incorrect programs, or even programs which do not compile. In this paper, we systematically study whether automated program repair (APR) techniques can fix the incorrect solutions produced by language mode...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automatically Fixing Dependency Breaking Changes](../venues/FSE2025/paper_29.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Breaking changes in dependencies are a common challenge in software development, requiring manual intervention to resolve. This study examines how well LLM automate the repair of breaking changes caused by dependency updates in Java projects. Although earlier methods have mostly concentrated on detecting breaking changes or investigating their impact, they have not been able to completely automate the repair process. We introduce and compare two new approaches: an agentic system that combines au...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Benchmarking Automated Program Repair: An Extensive Study on Both Real-World and Artificial Bugs](../venues/ISSTA2024/paper_7.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: As bugs are inevitable and prevalent in real-world programs, many Automated Program Repair (APR) techniques have been proposed to generate patches for them. However, due to the lack of a standard for evaluating APR techniques, prior works tend to use different settings and benchmarks in evaluation, threatening the trustworthiness of the evaluation results. Additionally, they typically only adopt plausibility and genuineness as evaluation metrics, which may potentially mask some underlying issues...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)


- [Better Patching Using LLM Prompting, via Self-Consistency](../venues/ASE2023/paper_5.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Large Language models (LLMs) can be induced to solve non-trivial problems with “few-shot” prompts including illustrative problem-solution examples. Now if the few-shots also include “chain of thought” ($\mathcal{C}oT$) explanations, which are of the form problem-explanation-solution, LLMs will generate a “explained” solution, and perform even better. Recently an exciting, substantially better technique, self-consistency [1] ($\mathcal{S}-C$) has emerged, based on the intuition that there are man...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md)


- [CREF: An LLM-Based Conversational Software Repair Framework for Programming Tutors](../venues/ISSTA2024/paper_11.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: With the proven effectiveness of Large Language Models (LLMs) in code-related tasks, researchers have explored their potential for program repair. However, existing repair benchmarks might have influenced LLM training data, potentially causing data leakage. To evaluate LLMs’ realistic repair capabilities, (i) we introduce an extensive, non-crawled benchmark TutorCode, comprising 1,239 C++ defect codes and associated information such as tutor guidance, solution description, failing test cases, an...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Closing the Gap: A User Study on the Real-world Usefulness of AI-powered Vulnerability Detection & Repair in the IDE](../venues/ICSE2025/paper_1.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: This paper presents the first empirical study of a vulnerability detection and fix tool with professional software developers on real projects that they own. We implemented DeepVulGuard, an IDE-integrated tool based on state-of-the-art detection and fix models, and show that it has promising performance on benchmarks of historic vulnerability data. DeepVulGuard scans code for vulnerabilities (including identifying the vulnerability type and vulnerable region of code), suggests fixes, provides na...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Code Change Intention, Development Artifact, and History Vulnerability: Putting Them Together for Vulnerability Fix Detection by LLM](../venues/FSE2025/paper_8.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Detecting vulnerability fix commits in open-source software is crucial for maintaining software security. To help OSS identify vulnerability fix commits, several automated approaches are developed. However, existing approaches like VulFixMiner and CoLeFunDa, focus solely on code changes, neglecting essential context from development artifacts. Tools like Vulcurator, which integrates issue reports, fail to leverage semantic associations between different development artifacts (e.g., pull requests...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Coffee-Gym: An Environment for Evaluating and Improving Natural Language Feedback on Erroneous Code](../venues/EMNLP2024/paper_38.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: This paper presents Coffee-Gym, a comprehensive RL environment for training models that provide feedback on code editing. Coffee-Gym includes two major components: (1) Coffee, a dataset containing humans’ code edit traces for coding questions and human-written feedback for editing erroneous code; (2) CoffeeEval, a reward function that faithfully reflects the helpfulness of feedback by assessing the performance of the revised code in unit tests. With them, Coffee-Gym addresses the unavailability ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)


- [ContractTinker: LLM-Empowered Vulnerability Repair for Real-World Smart Contracts](../venues/ASE2024/paper_35.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Smart contracts are susceptible to being exploited by attackers, especially when facing real-world vulnerabilities. To mitigate this risk, developers often rely on third-party audit services to identify potential vulnerabilities before project deployment. Nevertheless, repairing the identified vulnerabilities is still complex and laborintensive, particularly for developers lacking security expertise. Moreover, existing pattern-based repair tools mostly fail to address real-world vulnerabilities ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Copilot-in-the-Loop: Fixing Code Smells in Copilot-Generated Python Code using Copilot](../venues/ASE2024/paper_31.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: As one of the most popular dynamic languages, Python experiences a decrease in readability and maintainability when code smells are present. Recent advancements in Large Language Models have sparked growing interest in AI-enabled tools for both code generation and refactoring. GitHub Copilot is one such tool that has gained widespread usage. Copilot Chat, released in September 2023, functions as an interactive tool aimed at facilitating natural language-powered coding. However, limited attention...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Copiloting the Copilots: Fusing Large Language Models with Completion Engines for Automated Program Repair](../venues/FSE2023/paper_1.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: During Automated Program Repair (APR), it can be challenging&nbsp;to synthesize correct patches for real-world systems in general-purpose programming languages. Recent Large Language Models&nbsp;(LLMs) have been shown to be helpful “copilots” in assisting developers with various coding tasks, and have also been directly&nbsp;applied for patch synthesis. However, most LLMs treat programs as&nbsp;sequences of tokens, meaning that they are ignorant of the underlying semantics constraints of the tar...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [DR.FIX: Automatically Fixing Data Races at Industry Scale](../venues/PLDI2025/paper_1.md), ([PLDI2025](../venues/PLDI2025/README.md))

  - **Abstract**: Data races are a prevalent class of concurrency bugs in shared-memory parallel programs, posing significant challenges to software reliability and reproducibility. While there is an extensive body of research on detecting data races and a wealth of practical detection tools across various programming languages, considerably less effort has been directed toward automatically fixing data races at an industrial scale. In large codebases, data races are continuously introduced and exhibit myriad pat...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Demystifying Memorization in LLM-Based Program Repair via a General Hypothesis Testing Framework](../venues/FSE2025/paper_35.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have achieved remarkable success in various applications, particularly in code-related tasks such as code generation and program repair, setting new performance benchmarks. However, the extensive use of large training corpora raises concerns about whether these achievements stem from genuine understanding or mere memorization of training data—a question often overlooked in current research. This paper aims to study the memorization issue within LLM-based program repa...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [DesignRepair: Dual-Stream Design Guideline-Aware Frontend Repair with Large Language Models](../venues/ICSE2025/paper_36.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: The rise of Large Language Models (LLMs) has streamlined frontend interface creation through tools like Vercel's v0, yet surfaced challenges in design quality (e.g., accessibility, and usability). Current solutions, often limited by their focus, generalisability, or data dependency, fall short in addressing these complexities. Moreover, none of them examine the quality of LLM-generated UI design. In this work, we introduce DesignRepair, a novel dual-stream design guideline-aware system to examin...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Element-Based Automated DNN Repair with Fine-Tuned Masked Language Model](../venues/FSE2025/paper_3.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Deep Neural Networks (DNNs) are prevalent across a wide range of applications. Despite their success, the complexity and opaque nature of DNNs pose significant challenges in debugging and repairing DNN models, limiting their reliability and broader adoption. In this paper, we propose MLM4DNN, an element-based automated DNN repair method. Unlike previous techniques that focus on post-training adjustments or rely heavily on predefined bug patterns, MLM4DNN repairs DNNs by leveraging a fine-tuned M...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Error Delayed Is Not Error Handled: Understanding and Fixing Propagated Error-Handling Bugs](../venues/FSE2025/paper_33.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Error handling is critical for software reliability. In software systems, error handling may be delayed to other functions. Such propagated error handling (PEH) could easily be missed and lead to bugs. Our research reveals that PEH bugs are prevalent in software systems and, on average, take 44.1 days to fully address. Existing approaches have primarily focused on the error-handling bug within individual functions, which makes it difficult to fully address PEH bugs. In this paper, we conducted t...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Exploring Parameter-Efficient Fine-Tuning of Large Language Model on Automated Program Repair](../venues/ASE2024/paper_14.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Automated Program Repair (APR) aims to fix bugs by generating patches. And existing work has demonstrated that "pre-training and fine-tuning" paradigm enables Large Language Models (LLMs) improve fixing capabilities on APR. However, existing work mainly focuses on Full-Model Fine-Tuning (FMFT) for APR and limited research has been conducted on the execution-based evaluation of Parameter-Efficient Fine-Tuning (PEFT) for APR. Comparing to FMFT, PEFT can reduce computing resource consumption withou...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [FIXDRIVE: Automatically Repairing Autonomous Vehicle Driving Behaviour for $0.08 per Violation](../venues/ICSE2025/paper_60.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Autonomous Vehicles (AVs) are advancing rapidly, with Level-4 AVs already operating in real-world conditions. Current AVs, however, still lag behind human drivers in adaptability and performance, often exhibiting overly conservative behaviours and occasionally violating traffic laws. Existing solutions, such as runtime enforcement, mitigate this by automatically repairing the AV's planned trajectory at runtime, but such approaches lack transparency and should be a measure of last resort. It woul...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [FastFixer: An Efficient and Effective Approach for Repairing Programming Assignments](../venues/ASE2024/paper_12.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Providing personalized and timely feedback for student's programming assignments is useful for programming education. Automated program repair (APR) techniques have been used to fix the bugs in programming assignments, where the Large Language Models (LLMs) based approaches have shown promising results. Given the growing complexity of identifying and fixing bugs in advanced programming assignments, current fine-tuning strategies for APR are inadequate in guiding the LLM to identify bugs and make...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Fixing 7,400 Bugs for 1$: Cheap Crash-Site Program Repair](../venues/arXiv2025/paper_17.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: The rapid advancement of bug-finding techniques has led to the discovery of more vulnerabilities than developers can reasonably fix, creating an urgent need for effective Automated Program Repair (APR) methods. However, the complexity of modern bugs often makes precise root cause analysis difficult and unreliable. To address this challenge, we propose crash-site repair to simplify the repair task while still mitigating the risk of exploitation. In addition, we introduce a template-guided patch g...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Fixing Large Language Models' Specification Misunderstanding for Better Code Generation](../venues/ICSE2025/paper_35.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Code generation is to automatically generate source code conforming to a given programming specification, which has received extensive attention especially with the development of large language models (LLMs). Due to the inherent difficulty of code generation, the code generated by LLMs may not be aligned with the specification. Although thought-eliciting prompting techniques have been proposed to enhance the code generation performance of LLMs, producing correct understanding for complicated pr...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [How Effective Are Neural Networks for Fixing Security Vulnerabilities](../venues/ISSTA2023/paper_3.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Security vulnerability repair is a difficult task that is in dire need of automation. Two groups of techniques have shown promise: (1) large code language models (LLMs) that have been pre-trained on source code for tasks such as code completion, and (2) automated program repair (APR) techniques that use deep learning (DL) models to automatically fix software bugs. This paper is the first to study and compare Java vulnerability repair capabilities of LLMs and DL-based APR models. The contribution...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)


- [Improving Automated Program Repair with Domain Adaptation](../venues/TOSEM2024/paper_8.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Automated Program Repair (APR) is defined as the process of fixing a bug/defect in the source code, by an automated tool. APR tools have recently experienced promising results by leveraging state-of-the-art Neural Language Processing (NLP) techniques. APR tools such as TFix and CodeXGLUE that combine text-to-text transformers with software-specific techniques are outperforming alternatives, these days. However, in most APR studies, the train and test sets are chosen from the same set of projects...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Improving Transformer-based Program Repair Model through False Behavior Diagnosis](../venues/EMNLP2023/paper_17.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Research on automated program repairs using transformer-based models has recently gained considerable attention. The comprehension of the erroneous behavior of a model enables the identification of its inherent capacity and provides insights for improvement. However, the current landscape of research on program repair models lacks an investigation of their false behavior. Thus, we propose a methodology for diagnosing and treating the false behaviors of transformer-based program repair models. Sp...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [InferFix: End-to-End Program Repair with LLMs](../venues/FSE2023/paper_5.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Software development life cycle is profoundly influenced by bugs; their introduction, identification, and eventual resolution account for a significant portion of software development cost. This has motivated software engineering researchers and practitioners to propose different approaches for automating the identification and repair of software defects. Large Language Models (LLMs) have been adapted to the program repair task through few-shot demonstration learning and instruction prompting, t...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Intention is All you Need: Refining your Code from your Intention](../venues/ICSE2025/paper_55.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Code refinement aims to enhance existing code by addressing issues, refactoring, and optimizing to improve quality and meet specific requirements. As software projects scale in size and complexity, the traditional iterative exchange between re-viewers and developers becomes increasingly burdensome. While recent deep learning techniques have been explored to accelerate this process, their performance remains limited, primarily due to challenges in accurately understanding reviewers' intents. This...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [code summarization](code_summarization.md)


- [Investigating the Transferability of Code Repair for Low-Resource Programming Languages](../venues/NAACL2025/paper_2.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Large language models (LLMs) have shown remarkable performance on code generation tasks. A recent use case is iterative code repair, where an LLM fixes an incorrect program by rationalizing about errors and generating new code. Recent works augment the code repair process by integrating modern techniques such as chain-of-thought reasoning or distillation, but only study their benefits on high-resource languages like Python, and ignore low-resource languages like Perl. To address this gap of know...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Is Self-Repair a Silver Bullet for Code Generation?](../venues/ICLR2023/paper_1.md), ([ICLR2023](../venues/ICLR2023/README.md))

  - **Abstract**: Large language models have shown remarkable aptitude in code generation, but still struggle to perform complex tasks. Self-repair---in which the model debugs and repairs its own code---has recently become a popular way to boost performance in these settings. However, despite its increasing popularity, existing studies of self-repair have been limited in scope; in many settings, its efficacy thus remains poorly understood. In this paper, we analyze Code Llama, GPT-3.5 and GPT-4's ability to perfo...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Knowledge-Enhanced Program Repair for Data Science Code](../venues/ICSE2025/paper_69.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: This paper introduces DSrepair, a knowledge-enhanced program repair approach designed to repair the buggy code generated by LLMs in the data science domain. DSrepair uses knowledge graph based RAG for API knowledge retrieval and bug knowledge enrichment to construct repair prompts for LLMs. Specifically, to enable knowledge graph-based API retrieval, we construct DS-KG (Data Science Knowledge Graph) for widely used data science libraries. For bug knowledge enrichment, we employ an abstract synta...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [LLM-Based Repair of Static Nullability Errors](../venues/arXiv2025/paper_26.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Modern Java projects increasingly adopt static analysis tools that prevent null-pointer exceptions by treating nullness as a type property. However, integrating such tools into large, existing codebases remains a significant challenge. While annotation inference can eliminate many errors automatically, a subset of residual errors -- typically a mix of real bugs and false positives -- often persist and can only be resolved via code changes. Manually addressing these errors is tedious and error-pr...
  - **Labels**: [program repair](program_repair.md)


- [LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?): A Comprehensive Evaluation, Framework, and Benchmarks](../venues/S&P2024/paper_1.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have been suggested for use in automated vulnerability repair, but benchmarks showing they can consistently identify security-related bugs are lacking. We thus develop SecLLMHolmes, a fully automated evaluation framework that performs the most detailed investigation to date on whether LLMs can reliably identify and reason about security-related bugs. We construct a set of 228 code scenarios and analyze eight of the most capable LLMs across eight different investigati...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Mining Action Rules for Defect Reduction Planning](../venues/FSE2024/paper_12.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Defect reduction planning plays a vital role in enhancing software quality and minimizing software maintenance costs. By training a black box machine learning model and “explaining” its predictions, explainable AI for software engineering aims to identify the code characteristics that impact maintenance risks. However, post-hoc explanations do not always faithfully reflect what the original model computes. In this paper, we introduce CounterACT, a Counterfactual ACTion rule mining approach that ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Mystique: Automated Vulnerability Patch Porting with Semantic and Syntactic-Enhanced LLM](../venues/FSE2025/paper_4.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Branching repositories facilitates efficient software development but can also inadvertently propagate vulnerabilities. When an original branch is patched, other unfixed branches remain vulnerable unless the patch is successfully ported. However, due to inherent discrepancies between branches, many patches cannot be directly applied and require manual intervention, which is time-consuming and leads to delays in patch porting, increasing vulnerability risks. Existing automated patch porting appro...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [NIODebugger: A Novel Approach to Repair Non-Idempotent-Outcome Tests with LLM-Based Agent](../venues/ICSE2025/paper_61.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Flaky tests, characterized by inconsistent results across repeated executions, present significant challenges in software testing, especially during regression testing. Recently, there has been emerging research interest in non-idempotentoutcome (NIO) flaky tests-tests that pass on the initial run but fail on subsequent executions within the same environment. Despite progress in utilizing Large Language Models (LLMs) to address flaky tests, existing methods have not tackled NIO flaky tests. The ...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [bug reproduction](bug_reproduction.md), [code generation](code_generation.md), [program repair](program_repair.md)


- [Neurosymbolic Repair of Test Flakiness](../venues/ISSTA2024/paper_17.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Test flakiness, a non-deterministic behavior of builds irrelevant to code changes, is a major and continuing impediment to deliver- ing reliable software. The very few techniques for the automated repair of test flakiness are specifically crafted to repair either Order- Dependent (OD) or Implementation-Dependent (ID) flakiness. They are also all symbolic approaches, i.e., they leverage program analy- sis to detect and repair known test flakiness patterns and root causes, failing to generalize. T...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [OmniGIRL: A Multilingual and Multimodal Benchmark for GitHub Issue Resolution](../venues/ISSTA2025/paper_2.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: The GitHub issue resolution task aims to resolve issues reported in repositories automatically. With advances in large language models (LLMs), this task has gained increasing attention, and several benchmarks are proposed to evaluate the issue resolution ability of LLMs. However, existing benchmarks have three main limitations. First, current benchmarks focus on a single programming language, limiting the evaluation of issues from repositories across different languages. Second, they usually cov...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Out of Context: How important is Local Context in Neural Program Repair?](../venues/ICSE2024/paper_27.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Deep learning source code models have been applied very successfully to the problem of automated program repair. One of the standing issues is the small input window of current models which often cannot fully fit the context code required for a bug fix (e.g., method or class declarations of a project). Instead, input is often restricted to the local context, that is, the lines below and above the bug location. In this work we study the importance of this local context on repair success: how much...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Out of Sight, Out of Mind: Better Automatic Vulnerability Repair by Broadening Input Ranges and Sources](../venues/ICSE2024/paper_28.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: The advances of deep learning (DL) have paved the way for automatic software vulnerability repair approaches, which effectively learn the mapping from the vulnerable code to the fixed code. Nevertheless, existing DL-based vulnerability repair methods face notable limitations: 1) they struggle to handle lengthy vulnerable code, 2) they treat code as natural language texts, neglecting its inherent structure, and 3) they do not tap into the valuable expert knowledge present in the expert system. To...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Programming Assistant for Exception Handling with CodeBERT](../venues/ICSE2024/paper_13.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: With practical code reuse, the code fragments from developers' forums often migrate to applications. Owing to the incomplete nature of such fragments, they often lack the details on exception handling. The adaptation for exception handling to the codebase is not trivial as developers must learn and memorize what API methods could cause exceptions and what exceptions need to be handled. We propose Neurex, an exception handling recommender that learns from complete code, and accepts a given Java c...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [PyDex: Repairing Bugs in Introductory Python Assignments using LLMs](../venues/OOPSLA2024/paper_6.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Students often make mistakes in their introductory programming assignments as part of their learning process. Unfortunately, providing custom repairs for these mistakes can require a substantial amount of time and effort from class instructors. Automated program repair (APR) techniques can be used to synthesize such fixes. Prior work has explored the use of symbolic and neural techniques for APR in the education domain. Both types of approaches require either substantial engineering efforts or l...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [PyTy: Repairing Static Type Errors in Python](../venues/ICSE2024/paper_12.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Gradual typing enables developers to annotate types of their own choosing, offering a flexible middle ground between no type annotations and a fully statically typed language. As more and more code bases get type-annotated, static type checkers detect an increasingly large number of type errors. Unfortunately, fixing these errors requires manual effort, hampering the adoption of gradual typing in practice. This paper presents PyTy, an automated program repair approach targeted at statically dete...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [type inference](type_inference.md)


- [RepairAgent: An Autonomous, LLM-Based Agent for Program Repair](../venues/ICSE2025/paper_46.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Automated program repair has emerged as a powerful technique to mitigate the impact of software bugs on system reliability and user experience. This paper introduces Repair Agent, the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM). Unlike existing deep learning-based approaches, which prompt a model with a fixed prompt or in a fixed feedback loop, our work treats the LLM as an agent capable of autonomously planning and executi...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [agent design](agent_design.md)


- [Repairagent: An autonomous, llm-based agent for program repair](../venues/arXiv2024/paper_11.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Automated program repair has emerged as a powerful technique to mitigate the impact of software bugs on system reliability and user experience. This paper introduces RepairAgent, the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM). Unlike existing deep learning-based approaches, which prompt a model with a fixed prompt or in a fixed feedback loop, our work treats the LLM as an agent capable of autonomously planning and executin...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [agent design](agent_design.md), [planning](planning.md)


- [Repairing Bugs with the Introduction of New Variables: A Multi-Agent Large Language Model](../venues/CCS2024/paper_6.md), ([CCS2024](../venues/CCS2024/README.md))

  - **Abstract**: Trained on billions of tokens, large language models (LLMs) have a broad range of empirical knowledge which enables them to generate software patches with complex repair patterns. We leverage the powerful code-fixing capabilities of LLMs and propose VarPatch, a multi-agent conversational automated program repair (APR) technique that iteratively queries the LLM to generate software patches by providing various prompts and context information. VarPatch focuses on the variable addition repair patte...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Revisiting Unnaturalness for Automated Program Repair in the Era of Large Language Models](../venues/ICSE2025/paper_28.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: The problem of software quality has motivated the development of a variety of techniques for Automatic Program Repair (APR). Meanwhile, recent advances in AI and Large Language Models (LLMs) have produced orders of magnitude performance improvements over previous code generation techniques, affording promising opportunities for program repair and its constituent subproblems (e.g., fault localization, patch generation). Because models are trained on large volumes of code in which defects are rela...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [RustAssistant: Using LLMs to Fix Compilation Errors in Rust Code](../venues/ICSE2025/paper_14.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: The Rust programming language, with its safety guarantees, has established itself as a viable choice for low-level systems programming language over the traditional, unsafe alternatives like C/C++. These guarantees come from a strong ownership-based type system, as well as primitive support for features like closures, pattern matching, etc., that make the code more concise and amenable to reasoning. These unique Rust features also pose a steep learning curve for programmers. This paper presents ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Self-Edit: Fault-Aware Code Editor for Code Generation](../venues/ACL2023/paper_1.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated an impressive ability to generate codes on competitive programming tasks. However, with limited sample numbers, LLMs still suffer from poor accuracy. Inspired by the process of human programming, we propose a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task. We execute the generated code on the example test case provided in the q...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)


- [Show Me Why It’s Correct: Saving 1/3 of Debugging Time in Program Repair with Interactive Runtime Comparison](../venues/OOPSLA2025/paper_1.md), ([OOPSLA2025](../venues/OOPSLA2025/README.md))

  - **Abstract**: Automated Program Repair (APR) holds the promise of alleviating the burden of debugging and fixing software bugs. Despite this, developers still need to manually inspect each patch to confirm its correctness, which is tedious and time-consuming. This challenge is exacerbated in the presence of plausible patches, which accidentally pass test cases but may not correctly fix the bug. To address this challenge, we propose an interactive approach called iFix to facilitate patch understanding and comp...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [program testing](program_testing.md), [debugging](debugging.md)


- [SpecRover: Code Intent Extraction via LLMs](../venues/ICSE2025/paper_2.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Autonomous program improvement typically involves automatically producing bug fixes and feature additions. Such program improvement can be accomplished by a combination of large language model (LLM) and program analysis capabilities, in the form of an LLM agent. Since program repair or program improvement typically requires a specification of intended behavior - specification inference can be useful for producing high quality program patches. In this work, we examine efficient and low-cost workf...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [Swe-bench: Can language models resolve real-world github issues?](../venues/ICLR2024/paper_1.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Language models have outpaced our ability to evaluate them effectively, but for their future development it is essential to study the frontier of their capabilities. We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language models. To this end, we introduce SWE-bench, an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popul...
  - **Labels**: [benchmark](benchmark.md), [code generation](code_generation.md), [program repair](program_repair.md)


- [Template-Guided Program Repair in the Era of Large Language Models](../venues/ICSE2025/paper_17.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Recent advancements in automated program repair (APR) have been significantly driven by the application of Large Language Models (LLMs). In particular, the integration of LLMs with traditional template-based repair methods has demonstrated effective outcomes. Despite this, the synergy between the strengths of traditional methods and LLMs remains underexploited. This oversight originates from the indiscriminate use of templates and their insufficient coverage. Also, using small-scale LLMs within ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [The Best of Both Worlds: Combining Learned Embeddings with Engineered Features for Accurate Prediction of Correct Patches](../venues/TOSEM2023/paper_2.md), ([TOSEM2023](../venues/TOSEM2023/README.md))

  - **Abstract**: A large body of the literature on automated program repair develops approaches where patches are automatically generated to be validated against an oracle (e.g., a test suite). Because such an oracle can be imperfect, the generated patches, although validated by the oracle, may actually be incorrect. While the state-of-the-art explores research directions that require dynamic information or rely on manually-crafted heuristics, we study the benefit of learning code representations in order to lea...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [The Fact Selection Problem in LLM-Based Program Repair](../venues/ICSE2025/paper_47.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Recent research has shown that incorporating bug-related facts, such as stack traces and GitHub issues, into prompts enhances the bug-fixing capabilities of large language models (LLMs). Considering the ever-increasing context window of these models, a critical question arises: what and how many facts should be included in prompts to maximise the chance of correctly fixing bugs? To answer this question, we conducted a large-scale study, employing over 19K prompts featuring various combinations o...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [The Plastic Surgery Hypothesis in the Era of Large Language Models](../venues/ASE2023/paper_9.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Automated Program Repair (APR) aspires to automatically generate patches for an input buggy program. Traditional APR tools typically focus on specific bug types and fixes through the use of templates, heuristics, and formal specifications. However, these techniques are limited in terms of the bug types and patch variety they can produce. As such, researchers have designed various learning-based APR tools with recent work focused on directly using Large Language Models (LLMs) for APR. While LLM-b...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [ThinkRepair: Self-Directed Automated Program Repair](../venues/ISSTA2024/paper_15.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Though many approaches have been proposed for Automated Program Repair (APR) and indeed achieved remarkable performance, they still have limitations in fixing bugs that require analyzing and reasoning about the logic of the buggy program. Recently, large language models (LLMs) instructed by prompt engineering have attracted much attention for their powerful ability to address many kinds of tasks including bug-fixing. However, the quality of the prompt will highly affect the ability of LLMs and m...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Towards Efficient Fine-Tuning of Language Models With Organizational Data for Automated Software Review](../venues/TSE2024/paper_1.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Large language models like BERT and GPT possess significant capabilities and potential impacts across various applications. Software engineers often use these models for code-related tasks, including generating, debugging, and summarizing code. Nevertheless, large language models still have several flaws, including model hallucination. (e.g., generating erroneous code and producing outdated and inaccurate programs) and the substantial computational resources and energy required for training and ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Towards Low-Resource Automatic Program Repair with Meta-Learning and Pretrained Language Models](../venues/EMNLP2023/paper_15.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Automatic program repair (APR) has gained increasing attention as an essential technique in software development to reduce manual debugging efforts and boost developers’ productivity. Recent advances in deep learning (DL) based models have demonstrated promising results by learning from large-scale bug-fix examples in a data-driven manner. However, in practical scenarios, software bugs have an imbalanced distribution, and the fixing knowledge learned by APR models often only capture the patterns...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Vision Transformer Inspired Automated Vulnerability Repair](../venues/TOSEM2024/paper_9.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Recently, automated vulnerability repair approaches have been widely adopted to combat increasing software security issues. In particular, transformer-based encoder-decoder models achieve competitive results. Whereas vulnerable programs may only consist of a few vulnerable code areas that need repair, existing AVR approaches lack a mechanism guiding their model to pay more attention to vulnerable code areas during repair generation. In this article, we propose a novel vulnerability repair framew...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [iSMELL: Assembling LLMs with Expert Toolsets for Code Smell Detection and Refactoring](../venues/ASE2024/paper_22.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Detecting and refactoring code smells is challenging, laborious, and sustaining. Although large language models have demonstrated potential in identifying various types of code smells, they also have limitations such as input-output token restrictions, difficulty in accessing repository-level knowledge, and performing dynamic source code analysis. Existing learning-based methods or commercial expert toolsets have advantages in handling complex smells. They can analyze project structures and cont...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [bug detection](bug_detection.md)


## Program Transformation

- [AlphaTrans: A Neuro-Symbolic Compositional Approach for Repository-Level Code Translation and Validation](../venues/FSE2025/paper_1.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Code translation transforms programs from one programming language (PL) to another. Several rule-based transpilers have been designed to automate code translation between different pairs of PLs. However, the rules can become obsolete as the PLs evolve and cannot generalize to other PLs. Recent studies have explored the automation of code translation using Large Language Models (LLMs). One key observation is that such techniques may work well for crafted benchmarks but fail to generalize to the s...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Automated Program Refinement: Guide and Verify Code Large Language Model with Refinement Calculus](../venues/POPL2025/paper_1.md), ([POPL2025](../venues/POPL2025/README.md))

  - **Abstract**: Recently, the rise of code-centric large language models (LLMs) appears to have reshaped the software engineering world with low-barrier tools like Copilot that can generate code easily. However, there is no correctness guarantee for the code generated by LLMs, which suffer from the hallucination problem, and their output is fraught with risks. Besides, the end-to-end process from specification to code through LLMs is a non-transparent and uncontrolled black box. This opacity makes it difficult ...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Automated Unit Test Refactoring](../venues/FSE2025/paper_10.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Test smells arise from poor design practices and insufficient domain knowledge, which can lower the quality of test code and make it harder to maintain and update. Manually refactoring of test smells is time-consuming and error-prone, highlighting the necessity for automated approaches. Current rule-based refactoring methods often struggle in scenarios not covered by predefined rules and lack the flexibility needed to handle diverse cases effectively. In this paper, we propose a novel approach c...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Automated Validation of COBOL to Java Transformation](../venues/ASE2024/paper_38.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Recent advances in Large Language Model (LLM) based Generative AI techniques have made it feasible to translate enterpriselevel code from legacy languages such as COBOL to modern languages such as Java or Python. While the results of LLM-based automatic transformation are encouraging, the resulting code cannot be trusted to correctly translate the original code. We propose a framework and a tool to help validate the equivalence of COBOL and translated Java. The results can also help repair the c...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Bridging Gaps in LLM Code Translation: Reducing Errors with Call Graphs and Bridged Debuggers](../venues/ASE2024/paper_40.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: When using large language models (LLMs) for code translation of complex software, numerous compilation and runtime errors can occur due to insufficient context awareness. To address this issue, this paper presents a code translation method based on call graphs and bridged debuggers: TransGraph. TransGraph first obtains the call graph of the entire code project using the Language Server Protocol, which provides a detailed description of the function call relationships in the program. Through this...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Bridging Operator Semantic Inconsistencies: A Source-Level Cross-Framework Model Conversion Approach](../venues/FSE2025/paper_27.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: As deep learning (DL) frameworks become widely used, converting models between frameworks is crucial for ecosystem flexibility. However, interestingly, existing model converters commonly focus on syntactic operator API mapping—transpiling operator names and parameters—which results in API compatibility issues (i.e., incompatible parameters, missing operators). These issues arise from semantic inconsistencies due to differences in operator implementation, causing conversion failure or performance...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [empirical study](empirical_study.md)


- [C2SaferRust: Transforming C Projects into Safer Rust with NeuroSymbolic Techniques](../venues/arXiv2025/paper_25.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: In recent years, there has been a lot of interest in converting C code to Rust, to benefit from the memory and thread safety guarantees of Rust. C2Rust is a rule-based system that can automatically convert C code to functionally identical Rust, but the Rust code that it produces is non-idiomatic, i.e., makes extensive use of unsafe Rust, a subset of the language that doesn't have memory or thread safety guarantees. At the other end of the spectrum are LLMs, which produce idiomatic Rust code, but...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [CRUST-Bench: A Comprehensive Benchmark for C-to-safe-Rust Transpilation](../venues/arXiv2025/paper_6.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: C-to-Rust transpilation is essential for modernizing legacy C code while enhancing safety and interoperability with modern Rust ecosystems. However, no dataset currently exists for evaluating whether a system can transpile C into safe Rust that passes a set of test cases. We introduce CRUST-Bench, a dataset of 100 C repositories, each paired with manually-written interfaces in safe Rust as well as test cases that can be used to validate correctness of the transpilation. By considering entire rep...
  - **Labels**: [benchmark](benchmark.md), [code generation](code_generation.md), [program transformation](program_transformation.md)


- [ClassEval-T: Evaluating Large Language Models in Class-Level Code Translation](../venues/ISSTA2025/paper_19.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: In recent years, Large Language Models (LLMs) have dramatically advanced the performance of automated code translation, making their computational accuracy score reach up to over 80\% on many previous benchmarks. However, most code samples in these benchmarks are short, standalone, statement/method-level, and algorithmic, which is not aligned with practical coding tasks. Therefore, it is still unknown the actual capability of LLMs in translating code samples written for daily development.    To ...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Concrat: An Automatic C-to-Rust Lock API Translator for Concurrent Programs](../venues/ICSE2023/paper_7.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Concurrent programs suffer from data races. To prevent data races, programmers use locks. However, programs can eliminate data races only when they acquire and release correct locks at correct timing. The lock API of C, in which people have developed a large portion of legacy system programs, does not validate the correct use of locks. On the other hand, Rust, a recently developed system programming language, provides a lock API that guarantees the correct use of locks via type checking. This ma...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Context-aware Code Segmentation for C-to-Rust Translation using Large Language Models](../venues/arXiv2024/paper_35.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: There is strong motivation to translate C code into Rust code due to the continuing threat of memory safety vulnerabilities in existing C programs and the significant attention paid to Rust as an alternative to the C language. While large language models (LLMs) show promise for automating this translation by generating more natural and safer code than rule-based methods, previous studies have shown that LLM-generated Rust code often fails to compile, even for relatively small C programs, due to ...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Domain-specific transformer models for query translation](../venues/ACL2023/paper_11.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Due to the democratization of e-commerce, many product companies are listing their goods for online shopping. For periodic buying within a domain such as Grocery, consumers are generally inclined to buy certain brands of products. Due to a large non-English speaking population in India, we observe a significant percentage of code-mix Hinglish search queries e.g., sasta atta. An intuitive approach to dealing with code-mix queries is to train an encoder-decoder model to translate the query to Engl...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Enabling Memory Safety of C Programs using LLMs](../venues/arXiv2024/paper_14.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Memory safety violations in low-level code, written in languages like C, continues to remain one of the major sources of software vulnerabilities. One method of removing such violations by construction is to port C code to a safe C dialect. Such dialects rely on programmer-supplied annotations to guarantee safety with minimal runtime overhead. This porting, however, is a manual process that imposes significant burden on the programmer and, hence, there has been limited adoption of this technique...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Exploring and Unleashing the Power of Large Language Models in Automated Code Translation](../venues/FSE2024/paper_6.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Code translation tools, namely transpilers, are developed for automatic source-to-source translation. Latest learning-based transpilers have shown impressive enhancement against rule-based counterparts in both translation accuracy and readability, owing to their task-specific pre-training on extensive monolingual corpora. Nevertheless, their current performance still remains unsatisfactory for practical deployment, and the associated training resources are also prohibitively expensive. Large Lan...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [code model](code_model.md), [code model training](code_model_training.md), [empirical study](empirical_study.md)


- [Guess \& Sketch: Language Model Guided Transpilation](../venues/ICLR2024/paper_3.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Maintaining legacy software requires many software and systems engineering hours. Assembly code programs, which demand low-level control over the computer machine state and have no variable names, are particularly difficult for humans to analyze. Existing conventional program translators guarantee correctness, but are hand-engineered for the source and target programming languages in question. Learned transpilation, i.e. automatic translation of code, offers an alternative to manual re-writing a...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [HECS: A Hypergraph Learning-Based System for Detecting Extract Class Refactoring Opportunities](../venues/ISSTA2024/paper_25.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: HECS is an advanced tool designed for Extract Class refactoring by leveraging hypergraph learning to model complex dependencies within large classes. Unlike traditional tools that rely on direct one-to-one dependency graphs, HECS uses intra-class dependency hypergraphs to capture one-to-many relationships. This allows HECS to provide more accurate and relevant refactoring suggestions. The tool constructs hypergraphs for each target class, attributes nodes using a pre-trained code model, and trai...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Introducing Compiler Semantics into Large Language Models as Programming Language Translators: A Case Study of C to x86 Assembly](../venues/EMNLP2024/paper_2.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Compilers are complex software containing millions of lines of code, taking years to develop. This paper investigates to what extent Large Language Models (LLMs) can replace hand-crafted compilers in translating high-level programming languages to machine instructions, using C to x86 assembly as a case study. We identify two challenges of using LLMs for code translation and introduce two novel data pre-processing techniques to address the challenges: numerical value conversion and training data ...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [LLM Assistance for Memory Safety](../venues/ICSE2025/paper_15.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Memory safety violations in low-level code, written in languages like C, continues to remain one of the major sources of software vulnerabilities. One method of removing such violations by construction is to port C code to a safe C dialect. Such dialects rely on programmer-supplied annotations to guarantee safety with minimal runtime overhead. This porting, however, is a manual process that imposes significant burden on the programmer and, hence, there has been limited adoption of this technique...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [LLM-Based Java Concurrent Program to ArkTS Converter](../venues/ASE2024/paper_37.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: HarmonyOS NEXT is a distributed operating system developed to support HarmonyOS native apps. To support the new and independent Harmony ecosystem, developers are required to migrate their applications from Android to HarmonyOS. However, HarmonyOS utilizes ArkTS, a superset of TypeScript, as the programming language for application development. Hence, migrating applications to HarmonyOS requires translating programs across different program languages, e.g., Java, which is known to be very challen...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [LLM-Driven Multi-step Translation from C to Rust using Static Analysis](../venues/ICLR2025/paper_3.md), ([ICLR2025](../venues/ICLR2025/README.md))

  - **Abstract**: Translating software written in legacy languages to modern languages, such as C to Rust, has significant benefits in improving memory safety while maintaining high performance. However, manual translation is cumbersome, error-prone, and produces unidiomatic code. Large language models (LLMs) have demonstrated promise in producing idiomatic translations, but offer no correctness guarantees as they lack the ability to capture all the semantics differences between the source and target languages. T...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [LPR: Large Language Models-Aided Program Reduction](../venues/ISSTA2024/paper_5.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Program reduction is a widely used technique to facilitate debugging                compilers by automatically minimizing programs that trigger                compiler bugs. Existing program reduction techniques are either                generic to a wide range of languages (such as Perses and Vulcan)                or specifically optimized for one certain language by exploiting                language-specific knowledge (e.g., C-Reduce). However, synergistically                combining both g...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [program testing](program_testing.md), [debugging](debugging.md)


- [Learning performance-improving code edits](../venues/ICLR2024/paper_4.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: With the waning of Moore's law, optimizing program performance has become a major focus of software research. However, high-level optimizations such as API and algorithm changes remain elusive due to the difficulty of understanding the semantics of code. Simultaneously, pretrained large language models (LLMs) have demonstrated strong capabilities at solving a wide range of programming tasks. To that end, we introduce a framework for adapting LLMs to high-level program optimization. First, we cur...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Lost in Translation: A Study of Bugs Introduced by Large Language Models while Translating Code](../venues/ICSE2024/paper_10.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Code translation aims to convert source code from one programming language (PL) to another. Given the promising abilities of large language models (LLMs) in code synthesis, researchers are exploring their potential to automate code translation. The prerequisite for advancing the state of LLM-based code translation is to understand their promises and limitations over existing techniques. To that end, we present a large-scale empirical study to investigate the ability of general LLMs and code LLMs...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [empirical study](empirical_study.md)


- [Multilingual Code Co-evolution using Large Language Models](../venues/FSE2023/paper_2.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Many software projects implement APIs and algorithms in multiple programming languages. Maintaining such projects is tiresome, as developers have to ensure that any change (e.g., a bug fix or a new feature) is being propagated, timely and without errors, to implementations in other programming languages. In the world of ever-changing software, using rule-based translation tools (i.e., transpilers) or machine learning models for translating code from one language to another provides limited value...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [One-to-One or One-to-Many? Suggesting Extract Class Refactoring Opportunities with Intra-class Dependency Hypergraph Neural Network](../venues/ISSTA2024/paper_19.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Excessively large classes that encapsulate multiple responsibilities are challenging to comprehend and maintain. Addressing this issue, several Extract Class refactoring tools have been proposed, employing a two-phase process: identifying suitable fields or methods for extraction, and implementing the mechanics of refactoring. These tools traditionally generate an intra-class dependency graph to analyze the class structure, applying hard-coded rules based on this graph to unearth refactoring opp...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Porting Software Libraries to OpenHarmony: Transitioning from TypeScript or JavaScript to ArkTS](../venues/ISSTA2025/paper_20.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: OpenHarmony emerges as a potent force in the mobile app domain, poised to stand alongside established industry giants. ArkTS is its main language, enhancing TypeScript (TS) and JavaScript (JS) with strict typing for improved performance. Developers are encouraged to port popular TS/JS libraries to OpenHarmony, supported by detailed guidelines. However, this requires a deep understanding of ArkTS syntax, following porting specifications, and making manual changes. An automated solution is crucial...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Program Skeletons for Automated Program Translation](../venues/PLDI2025/paper_3.md), ([PLDI2025](../venues/PLDI2025/README.md))

  - **Abstract**: Translating software between programming languages is a challenging task, for which automated techniques have been elusive and hard to scale up to larger programs. A key difficulty in cross-language translation is that one has to re-express the intended behavior of the source program into idiomatic constructs of a different target language. This task needs abstracting away from the source language-specific details, while keeping the overall functionality the same. In this work, we propose a nove...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Rectifier: Code translation with corrector via llms](../venues/arXiv2024/paper_13.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Software migration is garnering increasing attention with the evolution of software and society. Early studies mainly relied on handcrafted translation rules to translate between two languages, the translation process is error-prone and time-consuming. In recent years, researchers have begun to explore the use of pre-trained large language models (LLMs) in code translation. However, code translation is a complex task that LLMs would generate mistakes during code translation, they all produce cer...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Refactoring programs using large language models with few-shot examples](../venues/APSEC2023/paper_1.md), ([APSEC2023](../venues/APSEC2023/README.md))

  - **Abstract**: A less complex and more straightforward program is a crucial factor that enhances its maintainability and makes writing secure and bug-free programs easier. However, due to its heavy workload and the risks of breaking the working programs, programmers are reluctant to do code refactoring, and thus, it also causes the loss of potential learning experiences. To mitigate this, we demonstrate the application of using a large language model (LLM), GPT-3.5, to suggest less complex versions of the user...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Refactoring to Pythonic Idioms: A Hybrid Knowledge-Driven Approach Leveraging Large Language Models](../venues/FSE2024/paper_2.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Pythonic idioms are highly valued and widely used in the Python programming community. However, many  Python users find it challenging to use Pythonic idioms. Adopting rule-based approach or LLM-only approach is not sufficient to overcome three persistent challenges of code idiomatization including code miss, wrong detection and wrong refactoring. Motivated by the determinism of rules and adaptability of LLMs, we propose a hybrid approach consisting of three modules. We not only write prompts to...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Rethinking Code Refinement: Learning to Judge Code Efficiency](../venues/EMNLP2024/paper_12.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated impressive capabilities in understanding and generating codes. Due to these capabilities, many recent methods are proposed to automatically refine the codes with LLMs. However, we should rethink that the refined codes (from LLMs and even humans) are not always more efficient than their original versions. On the other hand, running two different versions of codes and comparing them every time is not ideal and time-consuming. Therefore, in this work, ...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Rust-lancet: Automated Ownership-Rule-Violation Fixing with Behavior Preservation](../venues/ICSE2024/paper_11.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: As a relatively new programming language, Rust is designed to provide both memory safety and runtime performance. To achieve this goal, Rust conducts rigorous static checks against its safety rules during compilation, effectively eliminating memory safety issues that plague C/C++ programs. Although useful, the safety rules pose programming challenges to Rust programmers, since programmers can easily violate safety rules when coding in Rust, leading their code to be rejected by the Rust compiler,...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Scalable, Validated Code Translation of Entire Projects using Large Language Models](../venues/PLDI2025/paper_2.md), ([PLDI2025](../venues/PLDI2025/README.md))

  - **Abstract**: Large language models (LLMs) show promise in code translation due to their ability to generate idiomatic code. However, a significant limitation when using LLMs for code translation is scalability: existing works have shown a drop in translation success rates for code exceeding around 100 lines. We overcome this limitation by developing a modular approach to translation, where we partition the code into small code fragments which can be translated independently and semantically validated (that i...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Search-Based LLMs for Code Optimization](../venues/ICSE2025/paper_13.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: The code written by developers usually suffers from efficiency problems and contain various performance bugs. These inefficiencies necessitate the research of automated refactoring methods for code optimization. Early research in code optimization employs rule-based methods and focuses on specific inefficiency issues, which are labor-intensive and suffer from the low coverage issue. Recent work regards the task as a sequence generation problem, and resorts to deep learning (DL) techniques such a...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [static analysis](static_analysis.md), [program optimization](program_optimization.md)


- [Semi-Supervised Code Translation Overcoming the Scarcity of Parallel Code Data](../venues/ASE2024/paper_24.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Neural code translation is the task of converting source code from one programming language to another. One of the main challenges is the scarcity of parallel code data, which hinders the ability of translation models to learn accurate cross-language alignments. In this paper, we introduce MIRACLE, a semi-supervised approach that improves code translation through synthesizing high-quality parallel code data and curriculum learning on code data with ascending alignment levels. MIRACLE leverages s...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Specification-Driven Code Translation Powered by Large Language Models: How Far Are We?](../venues/arXiv2024/paper_22.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large Language Models (LLMs) are increasingly being applied across various domains, including code-related tasks such as code translation. Previous studies have explored using LLMs for translating code between different programming languages. Since LLMs are more effective with natural language, using natural language as an intermediate representation in code translation tasks presents a promising approach. In this work, we investigate using NL-specification as an intermediate representation for ...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Three Heads Are Better Than One: Suggesting Move Method Refactoring Opportunities with Inter-class Code Entity Dependency Enhanced Hybrid Hypergraph Neural Network](../venues/ASE2024/paper_15.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Methods implemented in incorrect classes will cause excessive reliance on other classes than their own, known as a typical code smell symptom: feature envy, which makes it difficult to maintain increased coupling between classes. Addressing this issue, several Move Method refactoring tools have been proposed, employing a two-phase process: identifying misplaced methods to move and appropriate classes to receive, and implementing the mechanics of refactoring. These tools traditionally use hard-co...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [Towards Translating Real-World Code with LLMs: A Study of Translating to Rust](../venues/arXiv2024/paper_36.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large language models (LLMs) show promise in code translation - the task of translating code written in one programming language to another language - due to their ability to write code in most programming languages. However, LLM's effectiveness on translating real-world code remains largely unstudied. In this work, we perform the first substantial study on LLM-based translation to Rust by assessing the ability of five state-of-the-art LLMs, GPT4, Claude 3, Claude 2.1, Gemini Pro, and Mixtral. W...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [TransLLaMa: LLM-based Simultaneous Translation System](../venues/EMNLP2024/paper_1.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Decoder-only large language models (LLMs) have recently demonstrated impressive capabilities in text generation and reasoning. Nonetheless, they have limited applications in simultaneous machine translation (SiMT), currently dominated by encoder-decoder transformers. This study demonstrates that, after fine-tuning on a small dataset comprising causally aligned source and target sentence pairs, a pre-trained open-source LLM can control input segmentation directly by generating a special “wait” to...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [empirical study](empirical_study.md)


- [Unprecedented Code Change Automation: The Fusion of LLMs and Transformation by Example](../venues/FSE2024/paper_19.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Software developers often repeat the same code changes within a project or across different projects. These repetitive changes are known as “code change patterns” (CPATs). Automating CPATs is crucial to expedite the software development process. While current Transformation by Example (TBE) techniques can automate CPATs, they are limited by the quality and quantity of the provided input examples. Thus, they miss transforming code variations that do not have the exact syntax, data-, or control-fl...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md)


- [VERT: Verified Equivalent Rust Transpilation with Large Language Models as Few-Shot Learners](../venues/arXiv2024/paper_34.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Rust is a programming language that combines memory safety and low-level control, providing C-like performance while guaranteeing the absence of undefined behaviors by default. Rust's growing popularity has prompted research on safe and correct transpiling of existing code-bases to Rust. Existing work falls into two categories: rule-based and large language model (LLM)-based. While rule-based approaches can theoretically produce correct transpilations that maintain input-output equivalence to th...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [static analysis](static_analysis.md), [program verification](program_verification.md)


- [Virtual Compiler Is All You Need For Assembly Code Search](../venues/ACL2024/paper_11.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Assembly code search is vital for reducing the burden on reverse engineers, allowing them to quickly identify specific functions using natural language within vast binary programs.Despite its significance, this critical task is impeded by the complexities involved in building high-quality datasets. This paper explores training a Large Language Model (LLM) to emulate a general compiler. By leveraging Ubuntu packages to compile a dataset of 20 billion tokens, we further continue pre-train CodeLlam...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [static analysis](static_analysis.md), [code search](code_search.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


## Program Decompilation

- [Beyond Classification: Inferring Function Names in Stripped Binaries via Domain Adapted LLMs](../venues/NDSS2025/paper_4.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: Function name inference in stripped binaries is an important yet challenging task for many security applications, such as malware analysis and vulnerability discovery, due to the need to grasp binary code semantics amidst diverse instruction sets, architectures, compiler optimizations, and obfuscations. While machine learning has made significant progress in this field, existing methods often struggle with unseen data, constrained by their reliance on a limited vocabulary-based classification ap...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md), [static analysis](static_analysis.md), [program decompilation](program_decompilation.md)


- [DeGPT: Optimizing Decompiler Output with LLM](../venues/NDSS2024/paper_1.md), ([NDSS2024](../venues/NDSS2024/README.md))

  - **Abstract**: Reverse engineering is essential in malware analysis, vulnerability discovery, etc. Decompilers assist the reverse engineers by lifting the assembly to the high-level programming language, which highly boosts binary comprehension. However, decompilers suffer from problems such as meaningless variable names, redundant variables, and lacking comments describing the purpose of the code. Previous studies have shown promising performance in refining the decompiler output by training the models with h...
  - **Labels**: [static analysis](static_analysis.md), [program decompilation](program_decompilation.md)


- [DecLLM: LLM-Augmented Recompilable Decompilation for Enabling Programmatic Use of Decompiled Code](../venues/ISSTA2025/paper_27.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Decompilers are widely used in reverse engineering (RE) to convert compiled executables into human-readable pseudocode and support various security analysis tasks. Existing decompilers, such as IDA Pro and Ghidra, focus on enhancing the readability of decompiled code rather than its recompilability, which limits further programmatic use, such as for CodeQL-based vulnerability analysis that requires compilable versions of the decompiled code. Recent LLM-based approaches for enhancing decompilatio...
  - **Labels**: [code generation](code_generation.md), [program decompilation](program_decompilation.md)


- [DiSCo: Towards Decompiling EVM Bytecode to Source Code using Large Language Models](../venues/FSE2025/paper_31.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Understanding the Ethereum smart contract bytecode is essential for ensuring cryptoeconomics security. However, existing decompilers primarily convert bytecode into pseudocode, which is not easily comprehensible for general users, potentially leading to misunderstanding of contract behavior and increased vulnerability to scams or exploits. In this paper, we propose DiSCo, the first LLMs-based EVM decompilation pipeline, which aims to enable LLMs to understand the opaque bytecode and lift it into...
  - **Labels**: [code generation](code_generation.md), [program decompilation](program_decompilation.md)


- [LLM4Decompile: Decompiling Binary Code with Large Language Models](../venues/EMNLP2024/paper_18.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Decompilation aims to convert binary code to high-level source code, but traditional tools like Ghidra often produce results that are difficult to read and execute. Motivated by the advancements in Large Language Models (LLMs), we propose LLM4Decompile, the first and largest open-source LLM series (1.3B to 33B) trained to decompile binary code. We optimize the LLM training process and introduce the LLM4Decompile-End models to decompile binary directly. The resulting models significantly outperfo...
  - **Labels**: [static analysis](static_analysis.md), [program decompilation](program_decompilation.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [Lmpa: Improving decompilation by synergy of large language model and program analysis](../venues/arXiv2023/paper_2.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Decompilation aims to recover the source code form of a binary executable. It has many applications in security and software engineering such as malware analysis, vulnerability detection and code reuse. A prominent challenge in decompilation is to recover variable names. We propose a novel method that leverages the synergy of large language model (LLM) and program analysis. Language models encode rich multi-modal knowledge, but its limited input size prevents providing sufficient global context ...
  - **Labels**: [static analysis](static_analysis.md), [program decompilation](program_decompilation.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [Nova: Generative Language Models for Assembly Code with Hierarchical Attention and Contrastive Learning](../venues/arXiv2023/paper_3.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Binary code analysis is the foundation of crucial tasks in the security domain; thus building effective binary analysis techniques is more important than ever. Large language models (LLMs) although have brought impressive improvement to source code tasks, do not directly generalize to assembly code due to the unique challenges of assembly: (1) the low information density of assembly and (2) the diverse optimizations in assembly code. To overcome these challenges, this work proposes a hierarchica...
  - **Labels**: [static analysis](static_analysis.md), [program decompilation](program_decompilation.md), [static analysis](static_analysis.md), [code similarity analysis](code_similarity_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [ReSym: Harnessing LLMs to Recover Variable and Data Structure Symbols from Stripped Binaries](../venues/CCS2024/paper_1.md), ([CCS2024](../venues/CCS2024/README.md))

  - **Abstract**: Decompilation aims to recover a binary executable to the source code form and hence has a wide range of applications in cyber security, such as malware analysis and legacy code hardening. A prominent challenge is to recover variable symbols, including both primitive and complex types such as user-defined data structures, along with their symbol information such as names and types. Existing efforts focus on solving parts of the problem, eg, recovering only types (without names) or only local vari...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md), [static analysis](static_analysis.md), [program decompilation](program_decompilation.md)


- [Refining Decompiled C Code with Large Language Models](../venues/arXiv2023/paper_4.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: A C decompiler converts an executable into source code. The recovered C source code, once re-compiled, is expected to produce an executable with the same functionality as the original executable. With over twenty years of development, C decompilers have been widely used in production to support reverse engineering applications. Despite the prosperous development of C decompilers, it is widely acknowledged that decompiler outputs are mainly used for human consumption, and are not suitable for aut...
  - **Labels**: [static analysis](static_analysis.md), [program decompilation](program_decompilation.md)


- [Self-Constructed Context Decompilation with Fined-grained Alignment Enhancement](../venues/EMNLP2024/paper_7.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Decompilation transforms compiled code back into a high-level programming language for analysis when source code is unavailable. Previous work has primarily focused on enhancing decompilation performance by increasing the scale of model parameters or training data for pre-training. Based on the characteristics of the decompilation task, we propose two methods: (1) Without fine-tuning, the Self-Constructed Context Decompilation (sc²dec) method recompiles the LLM’s decompilation results to constru...
  - **Labels**: [static analysis](static_analysis.md), [program decompilation](program_decompilation.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md), [benchmark](benchmark.md)


- [TypeForge: Synthesizing and Selecting Best-Fit Composite Data Types for Stripped Binaries](../venues/S&P2025/paper_2.md), ([S&P2025](../venues/S&P2025/README.md))

  - **Abstract**: Static binary analysis is a widely used approach for ensuring the security of closed-source software. However, the absence of type information in stripped binaries, particularly for composite data types, poses significant challenges for both static analyzers and reverse engineering experts in achieving efficient and accurate analysis. Existing methods often struggle with inaccuracies and scalability limitations when dealing with such data types. To address these problems, we present Typeforge, a...
  - **Labels**: [static analysis](static_analysis.md), [program decompilation](program_decompilation.md)


- [WaDec: Decompiling WebAssembly Using Large Language Model](../venues/ASE2024/paper_9.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: WebAssembly (abbreviated Wasm) has emerged as a cornerstone of web development, offering a compact binary format that allows high-performance applications to run at near-native speeds in web browsers. Despite its advantages, Wasm's binary nature presents significant challenges for developers and researchers, particularly regarding readability when debugging or analyzing web applications. Therefore, effective decompilation becomes crucial. Unfortunately, traditional decompilers often struggle wit...
  - **Labels**: [static analysis](static_analysis.md), [program decompilation](program_decompilation.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


