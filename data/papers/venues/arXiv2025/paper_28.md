# C2SaferRust: Transforming C Projects into Safer Rust with NeuroSymbolic Techniques

**Authors**: Vikram Nitin, Rahul Krishna, Luiz Lemos do Valle, Baishakhi Ray

**Abstract**:

In recent years, there has been a lot of interest in converting C code to Rust, to benefit from the memory and thread safety guarantees of Rust. C2Rust is a rule-based system that can automatically convert C code to functionally identical Rust, but the Rust code that it produces is non-idiomatic, i.e., makes extensive use of unsafe Rust, a subset of the language that doesn't have memory or thread safety guarantees. At the other end of the spectrum are LLMs, which produce idiomatic Rust code, but these have the potential to make mistakes and are constrained in the length of code they can process. In this paper, we present C2SaferRust, a novel approach to translate C to Rust that combines the strengths of C2Rust and LLMs. We first use C2Rust to convert C code to non-idiomatic, unsafe Rust. We then decompose the unsafe Rust code into slices that can be individually translated to safer Rust by an LLM. After processing each slice, we run end-to-end test cases to verify that the code still functions as expected. We also contribute a benchmark of 7 real-world programs, translated from C to unsafe Rust using C2Rust. Each of these programs also comes with end-to-end test cases. On this benchmark, we are able to reduce the number of raw pointers by up to 38%, and reduce the amount of unsafe code by up to 28%, indicating an increase in safety. The resulting programs still pass all test cases. C2SaferRust also shows convincing gains in performance against two previous techniques for making Rust code safer.

**Link**: [Read Paper](https://arxiv.org/pdf/2501.14257)

**Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)
