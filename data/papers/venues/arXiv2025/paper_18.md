# AgentArmor: Enforcing Program Analysis on Agent Runtime Trace to Defend Against Prompt Injection

**Authors**: Peiran Wang, Yang Liu, Yunfei Lu, Yifeng Cai, Hongbo Chen, Qingyou Yang, Jie Zhang, Jue Hong, Ye Wu

**Abstract**:

Large Language Model (LLM) agents offer a powerful new paradigm for solving various problems by combining natural language reasoning with the execution of external tools. However, their dynamic and non-transparent behavior introduces critical security risks, particularly in the presence of prompt injection attacks. In this work, we propose a novel insight that treats the agent runtime traces as structured programs with analyzable semantics. Thus, we present AgentArmor, a program analysis framework that converts agent traces into graph intermediate representation-based structured program dependency representations (e.g., CFG, DFG, and PDG) and enforces security policies via a type system. AgentArmor consists of three key components: (1) a graph constructor that reconstructs the agent's working traces as graph-based intermediate representations with control flow and data flow described within; (2) a property registry that attaches security-relevant metadata of interacted tools & data, and (3) a type system that performs static inference and checking over the intermediate representation. By representing agent behavior as structured programs, AgentArmor enables program analysis over sensitive data flow, trust boundaries, and policy violations. We evaluate AgentArmor on the AgentDojo benchmark, the results show that AgentArmor can achieve 95.75% of TPR, with only 3.66% of FPR. Our results demonstrate AgentArmor's ability to detect prompt injection vulnerabilities and enforce fine-grained security constraints.

**Link**: [Read Paper](https://www.arxiv.org/abs/2508.01249)

**Labels**: [agent design](../../labels/agent_design.md), [agent security](../../labels/agent_security.md)
