# AbsInt-AI: Language Models for Abstract Interpretation

**Authors**: Michael Wang, Kexin Pei, Armando Solar-Lezama

**Abstract**:

Static program analysis is a popular technique in software engineering. Traditional static analysis algorithms treat programs as sets of logical statements with well-defined semantics. These traditional analyzers can provide guarantees of their performance, such as guaranteeing that they will never miss a bug. However, they leave out lots of very rich information such as variable and field names. Language models for code on the other hand, take full advantage of information such as variable names, but it is extremely difficult to provide guarantees of their output. In this work, we present ABSINT-AI, a language model augmented static analyzer based on abstract interpretation that combines the best of both worlds. Using a language model in ABSINT-AI achieves up to a 70% decrease in false positives for bug detection while providing guarantees of never missing a bug.

**Link**: [Read Paper](https://openreview.net/forum?id=3RP6YmKo59)

**Labels**: [static analysis](../../labels/static_analysis.md), [abstract interpretation](../../labels/abstract_interpretation.md), [bug detection](../../labels/bug_detection.md)
