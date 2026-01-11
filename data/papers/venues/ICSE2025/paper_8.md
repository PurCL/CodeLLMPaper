# Between Lines of Code: Unraveling the Distinct Patterns of Machine and Human Programmers

**Authors**: Shi, Yuling and Zhang, Hongyu and Wan, Chengcheng and Gu, Xiaodong

**Abstract**:

Large language models have catalyzed an unprece-dented wave in code generation. While achieving significant advances, they blur the distinctions between machine- and human-authored source code, causing integrity and authenticity issues of software artifacts. Previous methods such as DetectGPthave proven effective in discerning machine-generated texts, but they do not identify and harness the unique patterns of machine-generated code. Thus, its applicability falters when applied to code. In this paper, we carefully study the specific patterns that characterize machine- and human-authored code. Through a rigorous analysis of code attributes such as lexical diversity, conciseness, and naturalness, we expose unique patterns inherent to each source. We particularly notice that the syntactic segmentation of code is a critical factor in identifying its provenance. Based on our findings, we propose DetectCodeGPT, a novel method for detecting machine-generated code, which improves DetectGPT by capturing the distinct stylized patterns of code. Diverging from conventional techniques that depend on external LLMs for perturbations, DetectCodeGPT perturbs the code corpus by strategically inserting spaces and newlines, ensuring both efficacy and efficiency. Experiment results show that our approach significantly outperforms state-of-the-art techniques in detecting machine-generated code.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00005)

**Labels**: [code model](../../labels/code_model.md)
