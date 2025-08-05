# ICLR2025

Number of papers: 4

## [AbsInt-AI: Language Models for Abstract Interpretation](paper_2.md)
- **Authors**: Michael Wang, Kexin Pei, Armando Solar-Lezama
- **Abstract**: Static program analysis is a popular technique in software engineering. Traditional static analysis algorithms treat programs as sets of logical statements with well-defined semantics. These traditional analyzers can provide guarantees of their performance, such as guaranteeing that they will never miss a bug. However, they leave out lots of very rich information such as variable and field names. Language models for code on the other hand, take full advantage of information such as variable name...
- **Link**: [Read Paper](https://openreview.net/forum?id=3RP6YmKo59)
- **Labels**: [static analysis](../../labels/static_analysis.md), [abstract interpretation](../../labels/abstract_interpretation.md), [bug detection](../../labels/bug_detection.md)


## [LLM-Driven Multi-step Translation from C to Rust using Static Analysis](paper_3.md)
- **Authors**: Tianyang Zhou, Haowen Lin, Somesh Jha, Mihai Christodorescu, Kirill Levchenko, Varun Chandrasekaran
- **Abstract**: Translating software written in legacy languages to modern languages, such as C to Rust, has significant benefits in improving memory safety while maintaining high performance. However, manual translation is cumbersome, error-prone, and produces unidiomatic code. Large language models (LLMs) have demonstrated promise in producing idiomatic translations, but offer no correctness guarantees as they lack the ability to capture all the semantics differences between the source and target languages. T...
- **Link**: [Read Paper](https://arxiv.org/html/2503.12511v2)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph](paper_4.md)
- **Authors**: Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu
- **Abstract**: Large Language Models (LLMs) excel in code generation yet struggle with modern AI software engineering tasks. Unlike traditional function-level or file-level coding tasks, AI software engineering requires not only basic coding proficiency but also advanced skills in managing and interacting with code repositories. However, existing methods often overlook the need for repository-level code understanding, which is crucial for accurately grasping the broader context and developing effective solutio...
- **Link**: [Read Paper](https://openreview.net/forum?id=dw9VUsSHGB)
- **Labels**: [agent design](../../labels/agent_design.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md), [planning](../../labels/planning.md)


## [Type-Aware Constraining for Code LLMs](paper_1.md)
- **Authors**: Niels Mündler, Jingxuan He, Hao Wang, Koushik Sen, Dawn Song, Martin Vechev
- **Abstract**: Large Language Models (LLMs) have achieved notable success in code generation. However, they still frequently produce invalid code, as they do not precisely model formal aspects of programming languages. Constrained decoding is a promising approach to alleviate this issue and has been successfully applied to domain-specific languages and syntactic features, but is not able to enforce more semantic features, such as well-typedness. To address this issue, we introduce type-aware constrained decodi...
- **Link**: [Read Paper](https://openreview.net/forum?id=DNAapYMXkc)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [code model](../../labels/code_model.md)
