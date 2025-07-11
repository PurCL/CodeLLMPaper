# Scalable, Validated Code Translation of Entire Projects using Large Language Models

**Authors**: Hanliang Zhang, Cristina David, Meng Wang, Brandon Paulsen, Daniel Kroening

**Abstract**:

Large language models (LLMs) show promise in code translation due to their ability to generate idiomatic code. However, a significant limitation when using LLMs for code translation is scalability: existing works have shown a drop in translation success rates for code exceeding around 100 lines. We overcome this limitation by developing a modular approach to translation, where we partition the code into small code fragments which can be translated independently and semantically validated (that is, by checking I/O equivalence). When this approach is applied naively, we discover that LLMs are unreliable when translating features of the source language that do not have a direct mapping to the target language, and that the LLM often gets stuck in repair loops when attempting to fix errors. To address these issues, we introduce two key concepts: (1) feature mapping, which integrates predefined translation rules with LLM-based translation to guide the LLM in navigating subtle language differences and producing semantically accurate code; and (2) type-compatibility, which facilitates localized checks at the function signature level to detect errors early, thereby narrowing the scope of potential repairs. We apply our approach to translating real-world Go codebases to Rust, demonstrating that we can consistently generate reliable Rust translations for projects up to 9,700 lines of code and 780 functions, with an average of 73% of functions successfully validated for I/O equivalence, considerably higher than any existing work.

**Link**: [Read Paper](https://dl.acm.org/doi/10.1145/3729315)

**Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)
