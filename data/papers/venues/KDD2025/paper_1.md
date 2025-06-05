# CompilerDream: Learning a Compiler World Model for General Code Optimization

**Authors**: Chaoyi Deng, Jialong Wu, Ningya Feng, Jianmin Wang, Mingsheng Long

**Abstract**:

Effective code optimization in compilers is crucial for computer and software engineering. The success of these optimizations primarily depends on the selection and ordering of the optimization passes applied to the code. While most compilers rely on a fixed sequence of optimization passes, current methods to find the optimal sequence either employ impractically slow search algorithms or learning methods that struggle to generalize to code unseen during training. We introduce CompilerDream, a model-based reinforcement learning approach to general code optimization. CompilerDream comprises a compiler world model that accurately simulates the intrinsic properties of optimization passes and an agent trained on this model to produce effective optimization strategies. By training on a large-scale program dataset, CompilerDream is equipped to serve as a general code optimizer across various application scenarios and source-code languages. Our extensive experiments first highlight CompilerDream's strong optimization capabilities for autotuning, where it leads the CompilerGym leaderboard. More importantly, the zero-shot generalization ability of large-scale trained compiler world model and agent, excels across diverse datasets, surpassing LLVM's built-in optimizations and other state-of-the-art methods in both settings of value prediction and end-to-end code optimization.

**Link**: [Read Paper](https://arxiv.org/abs/2404.16077)

**Labels**: [code generation](../../labels/code_generation.md), [program optimization](../../labels/program_optimization.md)
