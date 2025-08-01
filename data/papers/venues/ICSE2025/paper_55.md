# Intention is All you Need: Refining your Code from your Intention

**Authors**: Guo, Qi and Xie, Xiaofei and Liu, Shangqing and Hu, Ming and Li, Xiaohong and Bu, Lei

**Abstract**:

Code refinement aims to enhance existing code by addressing issues, refactoring, and optimizing to improve quality and meet specific requirements. As software projects scale in size and complexity, the traditional iterative exchange between re-viewers and developers becomes increasingly burdensome. While recent deep learning techniques have been explored to accelerate this process, their performance remains limited, primarily due to challenges in accurately understanding reviewers' intents. This paper proposes an intention-based code refinement technique that enhances the conventional comment-to-code process by explicitly extracting reviewer intentions from the comments. Our approach consists of two key phases: Intention Extraction and Intention Guided Revision Generation. Intention Extraction categorizes comments using predefined templates, while Intention Guided Revision Generation employs large language models (LLMs) to generate revised code based on these defined intentions. Three categories with eight subcategories are designed for comment transformation, which is followed by a hybrid approach that combines rule-based and LLM-based classifiers for accurate classification. Extensive experiments with five LLMs (G PT 40, GPT3.5, DeepSeekV2, DeepSeek7B, CodeQwen7B) under different prompting settings demonstrate that our approach achieves 79 % accuracy in intention extraction and up to 66 % in code refinement generation. Our results highlight the potential of our approach in enhancing data quality and improving the efficiency of code refinement.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00191)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md)
