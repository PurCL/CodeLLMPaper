# Hierarchical Repository-Level Code Summarization for Business Applications Using Local LLMs

**Authors**: Nilesh Dhulshette, Sapan Shah, Vinay Kulkarni

**Abstract**:

In large-scale software development, understanding the functionality and intent behind complex codebases is critical for effective development and maintenance. While code summarization has been widely studied, existing methods primarily focus on smaller code units, such as functions, and struggle with larger code artifacts like files and packages. Additionally, current summarization models tend to emphasize low-level implementation details, often overlooking the domain and business context that are crucial for real-world applications. This paper proposes a two-step hierarchical approach for repository-level code summarization, tailored to business applications. First, smaller code units such as functions and variables are identified using syntax analysis and summarized with local LLMs. These summaries are then aggregated to generate higher-level file and package summaries. To ensure the summaries are grounded in business context, we design custom prompts that capture the intended purpose of code artifacts based on the domain and problem context of the business application. We evaluate our approach on a business support system (BSS) for the telecommunications domain, showing that syntax analysis-based hierarchical summarization improves coverage, while business-context grounding enhances the relevance of the generated summaries.

**Link**: [Read Paper](https://arxiv.org/pdf/2501.07857)

**Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md), [agent design](../../labels/agent_design.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)
