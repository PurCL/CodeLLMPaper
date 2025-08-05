# Automated Static Vulnerability Detection via a Holistic Neuro-symbolic Approach

**Authors**: Penghui Li, Songchen Yao, Josef Sarfati Korich, Changhua Luo, Jianjia Yu, Yinzhi Cao, Junfeng Yang

**Abstract**:

Static vulnerability detection is still a challenging problem and demands excessive human efforts, e.g., manual curation of good vulnerability patterns. None of prior works, including classic program analysis or Large Language Model (LLM)-based approaches, have fully automated such vulnerability pattern generations with reasonable detection accuracy. In this paper, we design and implement, MoCQ, a novel holistic neuro-symbolic framework that combines the complementary strengths of LLMs and classical static analysis to enable scalable vulnerability detection. The key insight is that MoCQ leverages an LLM to automatically extract vulnerability patterns and translate them into detection queries, and then on static analysis to refine such queries in a feedback loop and eventually execute them for analyzing large codebases and mining vulnerabilities. We evaluate MoCQ on seven types of vulnerabilities spanning two programming languages. We found MoCQ-generated queries uncovered at least 12 patterns that were missed by experts. On a ground truth dataset, MoCQ achieved comparable precision and recall compared to expert-crafted queries. Moreover, MoCQ has identified seven previously unknown vulnerabilities in real-world applications, demonstrating its practical effectiveness. We have responsibly disclosed them to the corresponding developers.

**Link**: [Read Paper](https://arxiv.org/abs/2504.16057)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
