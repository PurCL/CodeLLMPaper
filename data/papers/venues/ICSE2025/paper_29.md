# An Empirical Study on Commit Message Generation Using LLMs via In-Context Learning

**Authors**: Wu, Yifan and Wang, Yunpeng and Li, Ying and Tao, Wei and Yu, Siyu and Yang, Haowen and Jiang, Wei and Li, Jianguo

**Abstract**:

Commit messages concisely describe code changes in natural language and are important for software maintenance. Several approaches have been proposed to automatically generate commit messages, but they still suffer from critical limitations, such as time-consuming training and poor generalization ability. To tackle these limitations, we propose to borrow the weapon of large language models (LLMs) and in-context learning (ICL). Our intuition is based on the fact that the training corpora of LLMs contain extensive code changes and their pairwise commit messages, which makes LLMs capture the knowledge about commits, while ICL can exploit the knowledge hidden in the LLMs and enable them to perform downstream tasks without model tuning. However, it remains unclear how well LLMs perform on commit message generation via ICL. In this paper, we conduct an empirical study to investigate the capability of LLMs to generate commit messages via ICL. Specifically, we first explore the impact of different settings on the performance of ICL-based commit message generation. We then compare ICL-based commit message generation with state-of-the-art approaches on a popular multilingual dataset and a new dataset we created to mitigate potential data leakage. The results show that ICL-based commit message generation significantly outperforms state-of-the-art approaches on subjective evaluation and achieves better generalization ability. We further analyze the root causes for LLM's underperformance and propose several implications, which shed light on future research directions for using LLMs to generate commit messages.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00091)

**Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [commit message generation](../../labels/commit_message_generation.md), [empirical study](../../labels/empirical_study.md)
