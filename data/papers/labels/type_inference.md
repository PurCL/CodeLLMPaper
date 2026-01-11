# Type Inference

- [An Empirical Study of Large Language Models for Type and Call Graph Analysis](../venues/arXiv2024/paper_2.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large Language Models (LLMs) are increasingly being explored for their potential in software engineering, particularly in static analysis tasks. In this study, we investigate the potential of current LLMs to enhance call-graph analysis and type inference for Python and JavaScript programs. We empirically evaluated 24 LLMs, including OpenAI's GPT series and open-source models like LLaMA and Mistral, using existing and newly developed benchmarks. Specifically, we enhanced TypeEvalPy, a micro-bench...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md), [call graph analysis](call_graph_analysis.md)


- [CKTyper: Enhancing Type Inference for Java Code Snippets by Leveraging Crowdsourcing Knowledge in Stack Overflow](../venues/FSE2025/paper_5.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Code snippets are widely used in technical forums to demonstrate solutions to programming problems. They can be leveraged by developers to accelerate problem-solving. However, code snippets often lack concrete types of the APIs used in them, which impedes their understanding and resue. To enhance the description of a code snippet, a number of approaches are proposed to infer the types of APIs. Although existing approaches can achieve good performance, their performance is limited by ignoring oth...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md)


- [Generative Type Inference for Python](../venues/ASE2023/paper_12.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Python is a popular dynamic programming language, evidenced by its ranking as the second most commonly used language on GitHub. However, its dynamic type system can lead to potential type errors, leading researchers to explore automatic type inference approaches for Python programs. Existing type inference approaches can be generally grouped into three categories, i.e., rule-based, supervised, and cloze- style approaches. The rule-based type inference approaches can ensure the accuracy of predic...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md)


- [Neurosymbolic Modular Refinement Type Inference](../venues/ICSE2025/paper_28.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Refinement types, a type-based generalization of Floyd-Hoare logics, are an expressive and modular means of statically ensuring a wide variety of correctness, safety, and security properties of software. However, their expressiveness and modularity means that to use them, a developer must laboriously annotate all the functions in their code with potentially complex type specifications that specify the contract for that function. We present LHC, a neurosymbolic agent that uses LLMs to automatical...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md)


- [PyTy: Repairing Static Type Errors in Python](../venues/ICSE2024/paper_12.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Gradual typing enables developers to annotate types of their own choosing, offering a flexible middle ground between no type annotations and a fully statically typed language. As more and more code bases get type-annotated, static type checkers detect an increasingly large number of type errors. Unfortunately, fixing these errors requires manual effort, hampering the adoption of gradual typing in practice. This paper presents PyTy, an automated program repair approach targeted at statically dete...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [type inference](type_inference.md)


- [Risky Dynamic Typing-related Practices in Python: An Empirical Study](../venues/TOSEM2024/paper_6.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Python’s dynamic typing nature provides developers with powerful programming abstractions. However, many type-related bugs are accumulated in code bases of Python due to the misuse of dynamic typing. The goal of this article is to aid in the understanding of developers’ high-risk practices toward dynamic typing and the early detection of type-related bugs. We first formulate the rules of six types of risky dynamic typing-related practices (type smells for short) in Python. We then develop a rule...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [TIGER: A Generating-Then-Ranking Framework for Practical Python Type Inference](../venues/ICSE2025/paper_11.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Python's dynamic typing system offers flexibility and expressiveness but can lead to type-related errors, prompting the need for automated type inference to enhance type hinting. While existing learning-based approaches show promising inference accuracy, they struggle with practical challenges in comprehensively handling various types, including complex parameterized types and (unseen) user-defined types. In this paper, we introduce TIGER, a two-stage generating-then-ranking (GTR) framework, des...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md)
