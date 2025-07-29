# DiSCo: Towards Decompiling EVM Bytecode to Source Code using Large Language Models

**Authors**: Su, Xing and Liang, Hanzhong and Wu, Hao and Niu, Ben and Xu, Fengyuan and Zhong, Sheng

**Abstract**:

Understanding the Ethereum smart contract bytecode is essential for ensuring cryptoeconomics security. However, existing decompilers primarily convert bytecode into pseudocode, which is not easily comprehensible for general users, potentially leading to misunderstanding of contract behavior and increased vulnerability to scams or exploits. In this paper, we propose DiSCo, the first LLMs-based EVM decompilation pipeline, which aims to enable LLMs to understand the opaque bytecode and lift it into smart contract code. DiSCo introduces three core technologies. First, a logic-invariant intermediate representation is proposed to reproject the low-level bytecode into high-level abstracted units. The second technique involves semantic enhancement based on a novel type-aware graph model to infer stripped variables during compilation, enhancing the lifting effect. The third technology is a flexible method incorporating code specifications to construct LLM-comprehensible prompts for source code generation. Extensive experiments illustrate that our generated code guarantees a high compilability rate at 75\%, with differential fuzzing pass rate averaging at 50\%. Manual validation results further indicate that the generated solidity contracts significantly outperforms baseline methods in tasks such as code comprehension and attack reproduction.

**Link**: [Read Paper](https://doi.org/10.1145/3729373)

**Labels**: [code generation](../../labels/code_generation.md), [program decompilation](../../labels/program_decompilation.md)
