# Code Similarity Analysis

- [A Multiple Representation Transformer with Optimized Abstract Syntax Tree for Efficient Code Clone Detection](../venues/ICSE2025/paper_22.md), ([ICSE2025](../venues/ICSE2025/README.md))

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
