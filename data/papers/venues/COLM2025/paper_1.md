# CALLME: Call Graph Augmentation with Large Language Models for Javascript

**Authors**: Michael Wang, Kexin Pei, Armando Solar-Lezama

**Abstract**:

Building precise call graphs for Javascript programs is a fundamental build-ing block for many important software engineering and security applications such as bug detection, program repair, and refactoring. However, resolving dynamic calls using static analysis is challenging because it requires enumerating all possible values of both the object and the field. As a result, static call graph construction algorithms for Javascript ignore such dynamic calls, resulting in missed edges and a high false negative rate. We present a new approach, CALLME, that combines Language Models (LMs) with a custom static analyzer to address this challenge. Our key insight is in using LMs to incorporate additional modalities such as variable names, natural language documentation, and calling contexts, which are often sufficient to resolve dynamic property calls, but are difficult to incorporate in traditional static analysis. We implement our approach in CALLME and evaluate it on a dataset of call edges that are dependent on dynamic property accesses. CALLME achieves 80% accuracy and 0.79 F1, outperforming the state-of-the- art static analyzer by 30% and 0.60, respectively. To study the effectiveness of CALLME on downstream analysis tasks, we evaluate it on our manually curated dataset with 25 known Javascript vulnerabilities. CALLME can detect 24 vulnerabilities with only 3 false positives, whereas static analysis tools based on current call graph construction algorithms miss all of them.

**Link**: [Read Paper](https://openreview.net/forum?id=xZi2rMUcAO#discussion)

**Labels**: [static analysis](../../labels/static_analysis.md), [call graph analysis](../../labels/call_graph_analysis.md)
