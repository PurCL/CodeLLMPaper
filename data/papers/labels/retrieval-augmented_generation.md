# Retrieval-augmented Generation

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
