# LLMs Meet Library Evolution: Evaluating Deprecated API Usage in LLM-Based Code Completion

**Authors**: Wang, Chong and Huang, Kaifeng and Zhang, Jian and Feng, Yebo and Zhang, Lyuye and Liu, Yang and Peng, Xin

**Abstract**:

Large language models (LLMs), pre-trained or fine-tuned on large code corpora, have shown effectiveness in generating code completions. However, in LLM-based code completion, LLMs may struggle to use correct and up-to-date Application Programming Interfaces (APIs) due to the rapid and continuous evolution of libraries. While existing studies have highlighted issues with predicting incorrect APIs, the specific problem of deprecated API usage in LLM-based code completion has not been thoroughly investigated. To address this gap, we conducted the first evaluation study on deprecated API usage in LLM-based code completion. This study involved seven advanced LLMs, 145 API mappings from eight popular Python libraries, and $\mathbf{2 8, 1 2 5}$ completion prompts. The study results reveal the status quo (i.e., API usage plausibility and deprecated usage rate) of deprecated API and replacing API usage in LLM-based code completion from the perspectives of model, prompt, and library, and indicate the root causes behind. Based on these findings, we propose two lightweight fixing approaches, Replaceapi and InsertPrompt, which can serve as baseline approaches for future research on mitigating deprecated API usage in LLM-based completion. Additionally, we provide implications for future research on integrating library evolution with LLMdriven software development.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00245)

**Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md)
