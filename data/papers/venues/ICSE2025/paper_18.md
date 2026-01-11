# Code Comment Inconsistency Detection and Rectification Using a Large Language Model

**Authors**: Rong, Guoping and Yu, Yongda and Liu, Song and Tan, Xin and Zhang, Tianyi and Shen, Haifeng and Hu, Jidong

**Abstract**:

Comments are widely used in source code. If a comment is consistent with the code snippet it intends to annotate, it would aid code comprehension. Otherwise, Code Comment Inconsistency (CCI) is not only detrimental to the understanding of code, but more importantly, it would negatively impact the development, testing, and maintenance of software. To tackle this issue, existing research has been primarily focused on detecting inconsistencies with varied performance. It is evident that detection alone does not solve the problem; it merely paves the way for solving it. A complete solution requires detecting inconsistencies and, more importantly, rectifying them by amending comments. However, this type of work is scarce. In this paper, we contribute C4RLLaMA, a fine-tuned large language model based on the open-source CodeLLaMA. It not only has the ability to rectify inconsistencies by correcting relevant comment content but also outperforms state-of-the-art approaches in detecting inconsistencies. Experiments with various datasets confirm that C4RLLaMA consistently surpasses both post hoc and just-in-time CCI detection approaches. More importantly, C4RLLaMA outperforms substantially the only known CCI rectification approach in terms of multiple performance metrics. To further examine C4RLLaMA's efficacy in rectifying inconsistencies, we conducted a manual evaluation, and the results showed that the percentage of correct comment updates by C4RLLaMA was 65.0% and 55.9% in just-in-time and post hoc, respectively, implying C4RLLaMA's real potential in practical use.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00035)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
