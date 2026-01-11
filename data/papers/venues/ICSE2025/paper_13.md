# RustAssistant: Using LLMs to Fix Compilation Errors in Rust Code

**Authors**: Deligiannis, Pantazis and Lal, Akash and Mehrotra, Nikita and Poddar, Rishi and Rastogi, Aseem

**Abstract**:

The Rust programming language, with its safety guarantees, has established itself as a viable choice for low-level systems programming language over the traditional, unsafe alternatives like C/C++. These guarantees come from a strong ownership-based type system, as well as primitive support for features like closures, pattern matching, etc., that make the code more concise and amenable to reasoning. These unique Rust features also pose a steep learning curve for programmers. This paper presents a tool called RustAssistant that leverages the emergent capabilities of Large Language Models (LLMs) to automatically suggest fixes for Rust compilation errors. RustAssistant uses a careful combination of prompting techniques as well as iteration between an LLM and the Rust compiler to deliver high accuracy of fixes. RustAssistant is able to achieve an impressive peak accuracy of roughly 74% on real-world compilation errors in popular open-source Rust repositories. We also contribute a dataset of Rust compilation errors to enable further research.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00022)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
