# Automatic Semantic Augmentation of Language Model Prompts (for Code Summarization)

**Authors**: Ahmed, Toufique and Pai, Kunal Suresh and Devanbu, Premkumar and Barr, Earl

**Abstract**:

Large Language Models (LLM) are a new class of computation engines, "programmed" via prompt engineering. Researchers are still learning how to best "program" these LLMs to help developers. We start with the intuition that developers tend to consciously and unconsciously collect semantics facts, from the code, while working. Mostly these are shallow, simple facts arising from a quick read. For a function, such facts might include parameter and local variable names, return expressions, simple pre- and post-conditions, and basic control and data flow, etc.One might assume that the powerful multi-layer architecture of transformer-style LLMs makes them implicitly capable of doing this simple level of "code analysis" and extracting such information, while processing code: but are they, really? If they aren't, could explicitly adding this information help? Our goal here is to investigate this question, using the code summarization task and evaluate whether automatically augmenting an LLM's prompt with semantic facts explicitly, actually helps.Prior work shows that LLM performance on code summarization benefits from embedding a few code \&amp; summary exemplars in the prompt, before the code to be summarized. While summarization performance has steadily progressed since the early days, there is still room for improvement: LLM performance on code summarization still lags its performance on natural-language tasks like translation and text summarization.We find that adding semantic facts to the code in the prompt actually does help! This approach improves performance in several different settings suggested by prior work, including for three different Large Language Models. In most cases, we see improvements, as measured by a range of commonly-used metrics; for the PHP language in the challenging CodeSearchNet dataset, this augmentation actually yields performance surpassing 30 BLEU1. In addition, we have also found that including semantic facts yields a substantial enhancement in LLMs' line completion performance.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3639183)

**Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)