# LLM Assistance for Memory Safety

**Authors**: Mohammed, Nausheen and Lal, Akash and Rastogi, Aseem and Sharma, Rahul and Roy, Subhajit

**Abstract**:

Memory safety violations in low-level code, written in languages like C, continues to remain one of the major sources of software vulnerabilities. One method of removing such violations by construction is to port C code to a safe C dialect. Such dialects rely on programmer-supplied annotations to guarantee safety with minimal runtime overhead. This porting, however, is a manual process that imposes significant burden on the programmer and, hence, there has been limited adoption of this technique. The task of porting not only requires inferring annotations, but may also need refactoring/rewriting of the code to make it amenable to such annotations. In this paper, we use Large Language Models (LLMs) towards addressing both these concerns. We show how to harness LLM capabilities to do complex code reasoning as well as rewriting of large codebases. We also present a novel framework for whole-program transformations that leverages lightweight static analysis to break the transformation into smaller steps that can be carried out effectively by an LLM. We implement our ideas in a tool called MSA that targets the CheckedC dialect. We evaluate MSA on several micro-benchmarks, as well as real-world code ranging up to 20K lines of code. We showcase superior performance compared to a vanilla LLM baseline, as well as demonstrate improvement over a state-of-the-art symbolic (non-LLM) technique.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00023)

**Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)
