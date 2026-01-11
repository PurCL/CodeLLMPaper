# A Multiple Representation Transformer with Optimized Abstract Syntax Tree for Efficient Code Clone Detection

**Authors**: Yu, Tianchen and Yuan, Li and Lin, Liannan and He, Hongkui

**Abstract**:

Over the past decade, the application of deep learning in code clone detection has produced remarkable results. However, the current approaches have two limitations: (a) code representation approaches with low information utilization, such as vanilla Abstract Syntax Tree (AST), leading to information redundancy which results in performance degradation; (b) low efficiency of clone detection on evaluation, resulting in excessive time costs during practical use. In this paper, we propose a Multiple Representation Transformer with an Optimized Abstract Syntax Tree (MRT-OAST) to introduce an efficient code representation method while achieving competitive performance. Specifically, MRT-OAST strategically prunes and enhances the AST, utilizing both pre-order and post-order traversals to represent two different representations. To speed up the evaluation process, MRT-OAST utilizes a pure Siamese Network and employs cosine similarity to compare the similarity between codes. Our approach effectively reduces AST sequences to 40 % and 39 % of their original length in Java and C/C++ while preserving structural information. In code clone detection tasks, our model surpasses state-of-the-art approaches on OJClone and Google Code Jam. During the evaluation of BigCloneBench, our model has a 5x speed improvement compared to the state-of-the-art lightweight model and a 563x speed improvement compared to the BERT-based model, with only a 0.3 % and 0.9 % decrease in $F_{1}$-score.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00050)

**Labels**: [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md)
