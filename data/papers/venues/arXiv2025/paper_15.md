# ClassInvGen: Class Invariant Synthesis using Large Language Models

**Authors**: Chuyue Sun, Viraj Agashe, Saikat Chakraborty, Jubi Taneja, Clark Barrett, David Dill, Xiaokang Qiu, Shuvendu K. Lahiri

**Abstract**:

Formal program specifications in the form of preconditions, postconditions, and class invariants have several benefits for the construction and maintenance of programs. They not only aid in program understanding due to their unambiguous semantics but can also be enforced dynamically (or even statically when the language supports a formal verifier). However, synthesizing high-quality specifications in an underlying programming language is limited by the expressivity of the specifications or the need to express them in a declarative manner. Prior work has demonstrated the potential of large language models (LLMs) for synthesizing high-quality method pre/postconditions for Python and Java, but does not consider class invariants.
 In this work, we describe ClassInvGen, a method for co-generating executable class invariants and test inputs to produce high-quality class invariants for a mainstream language such as C++, leveraging LLMs' ability to synthesize pure functions. We show that ClassInvGen outperforms a pure LLM-based technique to generate specifications (from code) as well as prior data-driven invariant inference techniques such as Daikon. We contribute a benchmark of standard C++ data structures along with a harness that can help measure both the correctness and completeness of generated specifications using tests and mutants. We also demonstrate its applicability to real-world code by performing a case study on several classes within a widely used and high-integrity C++ codebase.

**Link**: [Read Paper](https://www.arxiv.org/abs/2502.18917)

**Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)
