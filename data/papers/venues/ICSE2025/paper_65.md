# LWDIFF: an LLM-Assisted Differential Testing Framework for Webassembly Runtimes

**Authors**: Zhou, Shiyao and Wang, Jincheng and Ye, He and Zhou, Hao and Goues, Claire Le and Luo, Xiapu

**Abstract**:

WebAssembly (Wasm) runtimes execute Wasm programs, a popular low-level language for efficiently executing high-level languages in browsers, with broad applications across diverse domains. The correctness of those runtimes is critical for both functionality and security of Wasm execution, motivating testing approaches that target Wasm runtimes specifically. However, existing Wasm testing frameworks fail to generate test cases that effectively test all three phases of runtime, i.e., decoding, validation, and execution. To address this research gap, we propose a new differential testing framework for Wasm runtimes, which leverages knowledge from the Wasm language specification that prior techniques overlooked, enhancing comprehensive testing of runtime functionality. Specifically, we first use a large language model to extract that knowledge from the specification. We use that knowledge in the context of multiple novel mutation operators that generate test cases with diverse features to test all three runtime phases. We evaluate LWDIFF by applying it to eight Wasm runtimes. Compared with the state-of-the-art Wasm testers, LWDIFF achieves the highest branch coverage and identifies the largest number of bugs. In total, LWDIFF discovers 31 bugs across eight runtimes, all of which are confirmed, with 25 of them previously undiscovered.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00233)

**Labels**: [program testing](../../labels/program_testing.md), [differential testing](../../labels/differential_testing.md)
