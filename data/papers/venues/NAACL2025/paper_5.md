# {C}ode{T}ree: Agent-guided Tree Search for Code Generation with Large Language Models

**Authors**: Li, Jierui  and      Le, Hung  and      Zhou, Yingbo  and      Xiong, Caiming  and      Savarese, Silvio  and      Sahoo, Doyen

**Abstract**:

Pretrained on massive amounts of code and text data, large language models (LLMs) have demonstrated remarkable achievements in performing code generation tasks. With additional execution-based feedback, these models can act as agents with capabilities to self-refine and improve generated code autonomously. However, on challenging coding tasks with extremely large search space, current agentic approaches still struggle with multi-stage planning, generating, and debugging. To address this problem, we propose CodeTree, a framework for LLM agents to efficiently explore the search space in different stages of the code generation process. Specifically, we adopted a unified tree structure to explicitly explore different coding strategies, generate corresponding coding solutions, and subsequently refine the solutions. In each stage, critical decision-making (ranking, termination, expanding) of the exploration process is guided by both the environmental execution-based feedback and LLM-agent-generated feedback. We comprehensively evaluated CodeTree on 7 code generation benchmarks and demonstrated the significant performance gains of CodeTree against strong baselines. Using GPT-4o as the base model, we consistently achieved top results of 95.1{\%} on HumanEval, 98.7{\%} on MBPP, and 43.0{\%} on CodeContests. On the challenging SWEBench benchmark, our approach led to significant performance gains, achieving a 31.9{\%} solving rate.

**Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.189/)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [agent design](../../labels/agent_design.md), [planning](../../labels/planning.md)
