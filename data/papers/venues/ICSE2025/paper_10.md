# Hyperion: Unveiling DApp Inconsistencies Using LLM and Dataflow-Guided Symbolic Execution

**Authors**: Yang, Shuo and Lin, Xingwei and Chen, Jiachi and Zhong, Qingyuan and Xiao, Lei and Huang, Renke and Wang, Yanlin and Zheng, Zibin

**Abstract**:

The rapid advancement of blockchain platforms has significantly accelerated the growth of decentralized applications (DApps). Similar to traditional applications, DApps integrate front-end descriptions that showcase their features to attract users, and back-end smart contracts for executing their business logic. However, inconsistencies between the features promoted in front-end descriptions and those actually implemented in the contract can confuse users and undermine DApps's trustworthiness. In this paper, we first conducted an empirical study to identify seven types of inconsistencies, each exemplified by a real-world DApp. Furthermore, we introduce Hyperion, an approach designed to automatically identify inconsistencies between front-end descriptions and back-end code implementation in DApps. This method leverages a fine-tuned large language model LLaMA2 to analyze DApp descriptions and employs dataflow-guided symbolic execution for contract bytecode analysis. Finally, Hyperion reports the inconsistency based on predefined detection patterns. The experiment on our ground truth dataset consisting of 54 DApps shows that Hyperion reaches 84.06% overall recall and 92.06 % overall precision in reporting DApp inconsistencies. We also implement Hyperion to analyze 835 real-world DApps. The experimental results show that Hyperion discovers 459 real-world DApps containing at least one inconsistency.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00015)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
