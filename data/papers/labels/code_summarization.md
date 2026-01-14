# Code Summarization

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


- [Hierarchical Repository-Level Code Summarization for Business Applications Using Local LLMs](../venues/arXiv2025/paper_29.md), ([arXiv2025](../venues/arXiv2025/README.md))

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


- [Source Code Summarization in the Era of Large Language Models](../venues/ICSE2025/paper_17.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: To support software developers in understanding and maintaining programs, various automatic (source) code summarization techniques have been proposed to generate a concise natural language summary (i.e., comment) for a given code snippet. Recently, the emergence of large language models (LLMs) has led to a great boost in the performance of coderelated tasks. In this paper, we undertake a systematic and comprehensive study on code summarization in the era of LLMs, which covers multiple aspects in...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [empirical study](empirical_study.md)


- [Understanding Code Changes Practically with Small-Scale Language Models](../venues/ASE2024/paper_3.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Recent studies indicate that traditional techniques for understanding code changes are not as effective as techniques that directly prompt language models (LMs). However, current LM-based techniques heavily rely on expensive, large LMs (LLMs) such as GPT-4 and Llama-13b, which are either commercial or prohibitively costly to deploy on a wide scale, thereby restricting their practical applicability. This paper explores the feasibility of deploying small LMs (SLMs) while maintaining comparable or ...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)
