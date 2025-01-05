# ICSE2025

Number of papers: 5

## [Closing the Gap: A User Study on the Real-world Usefulness of AI-powered Vulnerability Detection & Repair in the IDE](paper_1.md)
- **Authors**: Benjamin Steenhoek, Kalpathy Sivaraman, Renata Saldivar Gonzalez, Yevhen Mohylevskyy, Roshanak Zilouchian Moghaddam, Wei Le
- **Abstract**: This paper presents the first empirical study of a vulnerability detection and fix tool with professional software developers on real projects that they own. We implemented DeepVulGuard, an IDE-integrated tool based on state-of-the-art detection and fix models, and show that it has promising performance on benchmarks of historic vulnerability data. DeepVulGuard scans code for vulnerabilities (including identifying the vulnerability type and vulnerable region of code), suggests fixes, provides na...
- **Link**: [Read Paper](https://www.arxiv.org/abs/2412.14306)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [empirical study](../../labels/empirical_study.md)


## [Combining Fine-Tuning and LLM-based Agents for Intuitive Smart Contract Auditing with Justifications](paper_5.md)
- **Authors**: Ma, Wei and Wu, Daoyuan and Sun, Yuqiang and Wang, Tianwen and Liu, Shangqing and Zhang, Jian and Xue, Yue and Liu, Yang
- **Abstract**: Smart contracts are decentralized applications built atop blockchains like Ethereum. Recent research has shown that large language models (LLMs) have potential in auditing smart contracts, but the state-of-the-art indicates that even GPT-4 can achieve only 30% precision (when both decision and justification are correct). This is likely because off-the-shelf LLMs were primarily pre-trained on a general text/code corpus and not fine-tuned on the specific domain of Solidity smart contract auditing....
- **Link**: [Read Paper](https://arxiv.org/pdf/2403.16073)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [agent design](../../labels/agent_design.md)


## [LLM-based Resource-Oriented Intention Inference for Static Resource Detection](paper_4.md)
- **Authors**: Wang, Chong and Liu, Jianan and Peng, Xin and Liu, Yang and Lou, Yiling
- **Abstract**: Resource leaks, caused by resources not being released after acquisition, often lead to performance issues and system crashes. Existing static detection techniques rely on mechanical matching of predefined resource acquisition/release APIs and null-checking conditions to find unreleased resources, suffering from both (1) false negatives caused by the incompleteness of predefined resource acquisition/release APIs and (2) false positives caused by the unsoundness of resource reachability validatio...
- **Link**: [Read Paper](https://arxiv.org/abs/2311.04448)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [QEDCartographer: Automating Formal Verification Using Reward-Free Reinforcement Learning](paper_2.md)
- **Authors**: Alex Sanchez-Stern, Abhishek Varghese, Zhanna Kaufman, Dylan Zhang, Talia Ringer, Yuriy Brun
- **Abstract**: Formal verification is a promising method for producing reliable software, but the difficulty of manually writing verification proofs severely limits its utility in practice. Recent methods have automated some proof synthesis by guiding a search through the proof space using a theorem prover. Unfortunately, the theorem prover provides only the crudest estimate of progress, resulting in effectively undirected search. To address this problem, we create QEDCartographer, an automated proof-synthesis...
- **Link**: [Read Paper](https://arxiv.org/abs/2408.09237)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


## [Vulnerability Detection with Code Language Models: How Far Are We?](paper_3.md)
- **Authors**: Yangruibo Ding and Yanjun Fu and Omniyyah Ibrahim and Chawin Sitawarin and Xinyun Chen and Basel Alomair and David A. Wagner and Baishakhi Ray and Yizheng Chen
- **Abstract**: In the context of the rising interest in code language models (code LMs) and vulnerability detection, we study the effectiveness of code LMs for detecting vulnerabilities. Our analysis reveals significant shortcomings in existing vulnerability datasets, including poor data quality, low label accuracy, and high duplication rates, leading to unreliable model performance in realistic vulnerability detection scenarios. Additionally, the evaluation methods used with these datasets are not representat...
- **Link**: [Read Paper](https://doi.org/10.48550/arXiv.2403.18624)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)
