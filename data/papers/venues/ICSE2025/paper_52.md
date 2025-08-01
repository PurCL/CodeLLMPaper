# A Multi-Agent Approach for REST API Testing with Semantic Graphs and LLM-Driven Inputs

**Authors**: Kim, Myeongsoo and Stennett, Tyler and Sinha, Saurabh and Orso, Alessandro

**Abstract**:

As modern web services increasingly rely on REST APIs, their thorough testing has become crucial. Furthermore, the advent of REST API documentation languages, such as the OpenAPI Specification, has led to the emergence of many black-box REST API testing tools. However, these tools often focus on individual test elements in isolation (e.g., APIs, parameters, values), resulting in lower coverage and less effectiveness in fault detection. To address these limitations, we present AutoRestTest, the first black-box tool to adopt a dependency-embedded multi-agent approach for REST API testing that integrates multi-agent reinforcement learning (MARL) with a semantic property dependency graph (SPDG) and Large Language Models (LLMs). Our approach treats REST API testing as a separable problem, where four agents-API, dependency, parameter, and value agents-collaborate to optimize API exploration. LLMs handle domain-specific value generation, the SPDG model simplifies the search space for dependencies using a similarity score between API operations, and MARL dynamically optimizes the agents' behavior. Our evaluation of AutoRestTest on 12 real-world REST services shows that it outperforms the four leading black-box REST API testing tools, including those assisted by RESTGPT (which generates realistic test inputs using LLMs), in terms of code coverage, operation coverage, and fault detection. Notably, AutoRestTest is the only tool able to trigger an internal server error in the Spotify service. Our ablation study illustrates that each component of AutoRestTest-the SPDG, the LLM, and the agent-learning mechanism-contributes to its overall effectiveness.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00179)

**Labels**: [program testing](../../labels/program_testing.md), [library testing](../../labels/library_testing.md)
