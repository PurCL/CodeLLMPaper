# Program Decompilation

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
