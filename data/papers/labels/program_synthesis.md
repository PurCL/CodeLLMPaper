# Program Synthesis

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


- [An Exploratory Study of ML Sketches and Visual Code Assistants](../venues/ICSE2025/paper_36.md), ([ICSE2025](../venues/ICSE2025/README.md))

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


- [Hysynth: Context-free llm approximation for guiding program synthesis](../venues/NeurIPS2024/paper_9.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Many structured prediction and reasoning tasks can be framed as program synthesis problems, where the goal is to generate a program in a domain-specific language (DSL) that transforms input data into the desired output. Unfortunately, purely neural approaches, such as large language models (LLMs), often fail to produce fully correct programs in unfamiliar DSLs, while purely symbolic methods based on combinatorial search scale poorly to complex problems. Motivated by these limitations, we introdu...
  - **Labels**: [program synthesis](program_synthesis.md)


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


- [Online Prompt Selection for Program Synthesis](../venues/AAAI2025/paper_2.md), ([AAAI2025](../venues/AAAI2025/README.md))

  - **Abstract**: Large Language Models (LLMs) demonstrate impressive capabilities in the domain of program synthesis. This level of performance is not, however, universal across all tasks, all LLMs and all prompting styles. There are many areas where one LLM dominates, one prompting style dominates, or where calling a symbolic solver is a better choice than an LLM. A key challenge for the user then, is to identify not only when an LLM is the right choice of solver, and the appropriate LLM to call for a given syn...
  - **Labels**: [program synthesis](program_synthesis.md)


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


- [SpecGen: Automated Generation of Formal Program Specifications via Large Language Models](../venues/ICSE2025/paper_37.md), ([ICSE2025](../venues/ICSE2025/README.md))

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


- [Towards Neural Synthesis for SMT-Assisted Proof-Oriented Programming](../venues/ICSE2025/paper_7.md), ([ICSE2025](../venues/ICSE2025/README.md))

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
