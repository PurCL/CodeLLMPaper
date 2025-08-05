# Prompt Strategy

## Retrieval-augmented Generation

- [Automatic Semantic Augmentation of Language Model Prompts (for Code Summarization)](../venues/ICSE2024/paper_19.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Large Language Models (LLM) are a new class of computation engines, "programmed" via prompt engineering. Researchers are still learning how to best "program" these LLMs to help developers. We start with the intuition that developers tend to consciously and unconsciously collect semantics facts, from the code, while working. Mostly these are shallow, simple facts arising from a quick read. For a function, such facts might include parameter and local variable names, return expressions, simple pre-...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [DroidCoder: Enhanced Android Code Completion with Context-Enriched Retrieval-Augmented Generation](../venues/ASE2024/paper_13.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Android is the most popular mobile operating system. However, Android development requires extensive coding, especially for unique features such as lifecycle callbacks and UI widgets. Existing code completion methods typically utilize Retrieval-Augmented Generation (RAG) to provide contextual information for pre-trained code large language models (Code LLMs) to perform completion. Despite considerable progress in these methods, their effectiveness in Android development remains limited. This is ...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [EvoR: Evolving Retrieval for Code Generation](../venues/EMNLP2024/paper_3.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Recently the retrieval-augmented generation (RAG) has been successfully applied in code generation. However, existing pipelines for retrieval-augmented code generation (RACG) employ static knowledge bases with a single source, limiting the adaptation capabilities of Large Language Models (LLMs) to domains they have insufficient knowledge of. In this work, we develop a novel pipeline, EVOR, that employs the synchronous evolution of both queries and diverse knowledge bases. On two realistic settin...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [source code model](source_code_model.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [Hierarchical Repository-Level Code Summarization for Business Applications Using Local LLMs](../venues/arXiv2025/paper_26.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: In large-scale software development, understanding the functionality and intent behind complex codebases is critical for effective development and maintenance. While code summarization has been widely studied, existing methods primarily focus on smaller code units, such as functions, and struggle with larger code artifacts like files and packages. Additionally, current summarization models tend to emphasize low-level implementation details, often overlooking the domain and business context that ...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [Instructive Code Retriever: Learn from Large Language Model's Feedback for Code Intelligence Tasks](../venues/ASE2024/paper_2.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Recent studies proposed to leverage large language models (LLMs) with In-Context Learning (ICL) to handle code intelligence tasks without fine-tuning. ICL employs task instructions and a set of examples as demonstrations to guide the model in generating accurate answers without updating its parameters. While ICL has proven effective for code intelligence tasks, its performance heavily relies on the selected examples. Previous work has achieved some success in using BM25 to retrieve examples for ...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [Leandojo: Theorem proving with retrieval-augmented language models](../venues/NeurIPS2023/paper_6.md), ([NeurIPS2023](../venues/NeurIPS2023/README.md))

  - **Abstract**: Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large compute requirements. This has created substantial barriers to research on machine learning methods for theorem proving. This paper removes these barriers by introducing LeanDojo: an open-source Lean playground consisting of toolkits, data, models, and benchmarks. LeanDojo extracts da...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [LocAgent: Graph-Guided LLM Agents for Code Localization](../venues/ACL2025/paper_1.md), ([ACL2025](../venues/ACL2025/README.md))

  - **Abstract**: Code localization--identifying precisely where in a codebase changes need to be made--is a fundamental yet challenging task in software maintenance. Existing approaches struggle to efficiently navigate complex codebases when identifying relevant code sections. The challenge lies in bridging natural language problem descriptions with the appropriate code elements, often requiring reasoning across hierarchical structures and multiple dependencies. We introduce LocAgent, a framework that addresses ...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md), [planning](planning.md)


- [On the Impacts of Contexts on Repository-Level Code Generation](../venues/NAACL2025/paper_11.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: CodeLLMs are widely used for code generation, yet their ability to handle repository-level dependencies remains underexplored. We introduce RepoExec, a benchmark for evaluating repository-level code generation, focusing on executability, functional correctness, and dependency utilization. Our study evaluates 18 models, revealing that retaining full dependency context yields the best performance, while smaller context sizes can be misleading. Pretrained LLMs excel in correctness but often reimple...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [RACONTEUR: A Knowledgeable, Insightful, and Portable LLM-Powered Shell Command Explainer](../venues/NDSS2025/paper_2.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: Malicious shell commands are linchpins to many cyber-attacks, but may not be easy to understand by security analysts due to complicated and often disguised code structures. Advances in large language models (LLMs) have unlocked the possibility of generating understandable explanations for shell commands. However, existing general-purpose LLMs suffer from a lack of expert knowledge and a tendency to hallucinate in the task of shell command explanation. In this paper, we present Raconteur, a knowl...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [RepoAudit: An Autonomous LLM-Agent for Repository-Level Code Auditing](../venues/ICML2025/paper_2.md), ([ICML2025](../venues/ICML2025/README.md))

  - **Abstract**: Code auditing is a code review process with the goal of finding bugs. Large Language Models (LLMs) have shown substantial potential in this task, offering the ability to analyze programs without compilation and enabling customized bug detection following specified prompts. However, applying LLMs to repository-level code auditing presents notable challenges. The inherent context limits and hallucinations of LLMs can lead to the low quality of bug reports. Meanwhile, the large size of software rep...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md), [planning](planning.md)


- [RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph](../venues/ICLR2025/paper_4.md), ([ICLR2025](../venues/ICLR2025/README.md))

  - **Abstract**: Large Language Models (LLMs) excel in code generation yet struggle with modern AI software engineering tasks. Unlike traditional function-level or file-level coding tasks, AI software engineering requires not only basic coding proficiency but also advanced skills in managing and interacting with code repositories. However, existing methods often overlook the need for repository-level code understanding, which is crucial for accurately grasping the broader context and developing effective solutio...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md), [planning](planning.md)


- [Repository-Level Prompt Generation for Large Language Models of Code](../venues/ICML2023/paper_2.md), ([ICML2023](../venues/ICML2023/README.md))

  - **Abstract**: With the success of large language models (LLMs) of code and their use as code assistants (e.g. Codex used in GitHub Copilot), techniques for introducing domain-specific knowledge in the prompt design process become important. In this work, we propose a framework called Repo-Level Prompt Generator that learns to generate example-specific prompts using prompt proposals. The prompt proposals take context from the entire repository, thereby incorporating both the structure of the repository and the...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [Retrieval-Based Prompt Selection for Code-Related Few-Shot Learning](../venues/ICSE2023/paper_10.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Large language models trained on massive code corpora can generalize to new tasks without the need for task-specific fine-tuning. In few-shot learning, these models take as input a prompt, composed of natural language instructions, a few instances of task demonstration, and a query and generate an output. However, the creation of an effective prompt for code-related tasks in few-shot learning has received little attention. We present a technique for prompt creation that automatically retrieves c...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [{C}odex{G}raph: Bridging Large Language Models and Code Repositories via Code Graph Databases](../venues/NAACL2025/paper_3.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Large Language Models (LLMs) excel in stand-alone code tasks like HumanEval and MBPP, but struggle with handling entire code repositories. This challenge has prompted research on enhancing LLM-codebase interaction at a repository scale. Current solutions rely on similarity-based retrieval or manual tools and APIs, each with notable drawbacks. Similarity-based retrieval often has low recall in complex tasks, while manual tools and APIs are typically task-specific and require expert knowledge, red...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


## Reason With Code

- [Can LLMs Reason in the Wild with Programs?](../venues/EMNLP2024/paper_11.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have shown superior capability to solve reasoning problems with programs. While being a promising direction, most of such frameworks are trained and evaluated in settings with a prior knowledge of task requirements. However, as LLMs become more capable, it is necessary to assess their reasoning abilities in more realistic scenarios where many real-world problems are open-ended with ambiguous scope, and often require multiple formalisms to solve. To investigate this, ...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Chain of code: Reasoning with a language model-augmented code emulator](../venues/Google2023/paper_1.md), ([Google2023](../venues/Google2023/README.md))

  - **Abstract**: Code provides a general syntactic structure to build complex programs and perform precise computations when paired with a code interpreter -- we hypothesize that language models (LMs) can leverage code-writing to improve Chain of Thought reasoning not only for logic and arithmetic tasks, but also for linguistic ones (and in particular, those that are a mix of both). For example, consider prompting an LM to write code that counts the number of times it detects sarcasm in an essay: the LM may stru...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Code Prompting Elicits Conditional Reasoning Abilities in Text+Code LLMs](../venues/EMNLP2024/paper_25.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Reasoning is a fundamental component of language understanding. Recent prompting techniques, such as chain of thought, have consistently improved LLMs’ performance on various reasoning tasks. Nevertheless, there is still little understanding of what triggers reasoning abilities in LLMs in the inference stage. In this paper, we investigate the effect of the input representation on the reasoning abilities of LLMs. We hypothesize that representing natural language tasks as code can enhance specific...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Complementary explanations for effective in-context learning](../venues/ACL2023/paper_7.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Large language models (LLMs) have exhibited remarkable capabilities in learning from explanations in prompts, but there has been limited understanding of exactly how these explanations function or why they are effective. This work aims to better understand the mechanisms by which explanations are used for in-context learning. We first study the impact of two different factors on the performance of prompts with explanations: the computation trace (the way the solution is decomposed) and the natur...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md), [empirical study](empirical_study.md)


- [Don't Transform the Code, Code the Transforms: Towards Precise Code Rewriting using LLMs](../venues/Meta2024/paper_1.md), ([Meta2024](../venues/Meta2024/README.md))

  - **Abstract**: Tools for rewriting, refactoring and optimizing code should be fast and correct. Large language models (LLMs), by their nature, possess neither of these qualities. Yet, there remains tremendous opportunity in using LLMs to improve code. We explore the use of LLMs not to transform code, but to code transforms. We propose a chain-of-thought approach to synthesizing code transformations from a small number of input/output code examples that incorporates execution and feedback. Unlike the direct rew...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [EHRAgent: Code Empowers Large Language Models for Few-shot Complex Tabular Reasoning on Electronic Health Records](../venues/EMNLP2024/paper_36.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Clinicians often rely on data engineers to retrieve complex patient information from electronic health record (EHR) systems, a process that is both inefficient and time-consuming. We propose EHRAgent, a large language model (LLM) agent empowered with accumulative domain knowledge and robust coding capability. EHRAgent enables autonomous code generation and execution to facilitate clinicians in directly interacting with EHRs using natural language. Specifically, we formulate a multi-tabular reaso...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Empowering Multi-step Reasoning across Languages via Program-Aided Language Models](../venues/EMNLP2024/paper_27.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: In-context learning methods are popular inference strategies where Large Language Models (LLMs) are elicited to solve a task using provided demonstrations without parameter updates. Among these approaches are the reasoning methods, best exemplified by Chain-of-Thought (CoT) and Program-Aided Language Models (PAL), which elicit LLMs to generate reasoning paths, thus promoting accuracy and attracting increasing attention. However, despite the success of these methods, the ability to deliver multi-...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Explanation selection using unlabeled data for chain-of-thought prompting](../venues/EMNLP2023/paper_14.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Recent work has shown how to prompt large language models with explanations to obtain strong performance on textual reasoning tasks, i.e., the chain-of-thought paradigm. However, subtly different explanations can yield widely varying downstream task accuracy. Explanations that have not been "tuned" for a task, such as off-the-shelf explanations written by nonexperts, may lead to mediocre performance. This paper tackles the problem of how to optimize explanation-infused prompts in a blackbox fash...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md), [empirical study](empirical_study.md)


- [Fact-Checking Complex Claims with Program-Guided Reasoning](../venues/ACL2023/paper_3.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Fact-checking real-world claims often requires collecting multiple pieces of evidence and applying complex multi-step reasoning. In this paper, we present Program-Guided Fact-Checking (ProgramFC), a novel fact-checking model that decomposes complex claims into simpler sub-tasks that can be solved using a shared library of specialized functions. We first leverage the in-context learning ability of large language models to generate reasoning programs to guide the verification process. Afterward, w...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [If llm is the wizard, then code is the wand: A survey on how code empowers large language models to serve as intelligent agents](../venues/arXiv2024/paper_33.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: The prominent large language models (LLMs) of today differ from past language models not only in size, but also in the fact that they are trained on a combination of natural language and formal language (code). As a medium between humans and computers, code translates high-level goals into executable steps, featuring standard syntax, logical consistency, abstraction, and modularity. In this survey, we present an overview of the various benefits of integrating code into LLMs' training data. Speci...
  - **Labels**: [survey](survey.md), [agent design](agent_design.md), [reason with code](reason_with_code.md)


- [Language Models as Compilers: Simulating Pseudocode Execution Improves Algorithmic Reasoning in Language Models](../venues/EMNLP2024/paper_37.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Algorithmic reasoning tasks that involve complex logical patterns, such as completing Dyck language, pose challenges for large language models (LLMs), despite their recent success. Prior work has used LLMs to generate programming language and applied external compilers for such tasks. Yet, when on the fly, it is hard to generate an executable code with the correct logic for the solution. Even so, code for one instance cannot be reused for others, although they might require the same logic to sol...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [PaD: Program-aided Distillation Can Teach Small Models Reasoning Better than Chain-of-thought Fine-tuning](../venues/NAACL2024/paper_3.md), ([NAACL2024](../venues/NAACL2024/README.md))

  - **Abstract**: While large language models (LLMs) excel in various natural language processing tasks, their huge size and the inaccessibility of parameters present challenges for practical deployment. Previous studies try to distill task-specific ability from LLMs to smaller models, using data synthesis and chain-of-thought (CoT) fine-tuning. However, synthetic CoT data often contains faulty reasoning, which deteriorates the quality of distillation, especially in reasoning capabilities. In this work, we propos...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Program-Aided Reasoners (Better) Know What They Know](../venues/NAACL2024/paper_2.md), ([NAACL2024](../venues/NAACL2024/README.md))

  - **Abstract**: Prior work shows that program-aided reasoning, in which large language models (LLMs) are combined with programs written in programming languages such as Python, can significantly improve accuracy on various reasoning tasks. However, while accuracy is essential, it is also important for such reasoners to “know what they know”, which can be quantified through the calibration of the model. In this paper, we compare the calibration of Program Aided Language Models (PAL) and text-based Chain-of-thoug...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Prompting with Pseudo-Code Instructions](../venues/EMNLP2023/paper_10.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Prompting with natural language instructions has recently emerged as a popular method of harnessing the capabilities of large language models (LLM). Given the inherent ambiguity present in natural language, it is intuitive to consider the possible advantages of prompting with less ambiguous prompt styles, like pseudo-code. In this paper, we explore if prompting via pseudo-code instructions helps improve the performance of pre-trained language models. We manually create a dataset of pseudo-code p...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Question Answering as Programming for Solving Time-Sensitive Questions](../venues/EMNLP2023/paper_7.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Question answering plays a pivotal role in human daily life because it involves our acquisition of knowledge about the world. However, due to the dynamic and ever-changing nature of real-world facts, the answer can be completely different when the time constraint in the question changes. Recently, Large Language Models (LLMs) have shown remarkable intelligence in question answering, while our experiments reveal that the aforementioned problems still pose a significant challenge to existing LLMs....
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Steering Large Language Models between Code Execution and Textual Reasoning](../venues/Microsoft2024/paper_1.md), ([Microsoft2024](../venues/Microsoft2024/README.md))

  - **Abstract**: While a lot of recent research focuses on enhancing the textual reasoning capabilities of Large Language Models (LLMs) by optimizing the multi-agent framework or reasoning chains, several benchmark tasks can be solved with 100% success through direct coding, which is more scalable and avoids the computational overhead associated with textual iterating and searching. Textual reasoning has inherent limitations in solving tasks with challenges in math, logics, optimization, and searching, which is ...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [When Do Program-of-Thought Works for Reasoning?](../venues/AAAI2024/paper_1.md), ([AAAI2024](../venues/AAAI2024/README.md))

  - **Abstract**: In the realm of embodied artificial intelligence, the reasoning capabilities of Large Language Models (LLMs) play a pivotal role. Although there are effective methods like program-of-thought prompting for LLMs which uses programming language to tackle complex reasoning tasks, the specific impact of code data on the improvement of reasoning capabilities remains under-explored. To address this gap, we propose complexity-impacted reasoning score CIRS, which combines structural and logical attribute...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md), [empirical study](empirical_study.md)


## Sampling And Ranking

- [Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs](../venues/EMNLP2023/paper_6.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: A popular approach for improving the correctness of output from large language models (LLMs) is Self-Consistency - poll the LLM multiple times and output the most frequent solution. Existing Self-Consistency techniques always generate a constant number of samples per question, where a better approach will be to non-uniformly distribute the available budget based on the amount of agreement in the samples generated so far. In response, we introduce Adaptive-Consistency, a cost-efficient, model-agn...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [sampling and ranking](sampling_and_ranking.md)


- [Making Language Models Better Reasoners with Step-Aware Verifier](../venues/ACL2023/paper_2.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Few-shot learning is a challenging task that requires language models to generalize from limited examples. Large language models like GPT-3 and PaLM have made impressive progress in this area, but they still face difficulties in reasoning tasks such as GSM8K, a benchmark for arithmetic problems. To improve their reasoning skills, previous work has proposed to guide the language model with prompts that elicit a series of reasoning steps before giving the final answer, achieving a significant impr...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [sampling and ranking](sampling_and_ranking.md)


- [Ranking llm-generated loop invariants for program verification](../venues/EMNLP2023/paper_13.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Synthesizing inductive loop invariants is fundamental to automating program verification. In this work, we observe that Large Language Models (such as gpt-3.5 or gpt-4) are capable of synthesizing loop invariants for a class of programs in a 0-shot setting, yet require several samples to generate the correct invariants. This can lead to a large number of calls to a program verifier to establish an invariant. To address this issue, we propose a {\it re-ranking} approach for the generated results ...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [sampling and ranking](sampling_and_ranking.md)


