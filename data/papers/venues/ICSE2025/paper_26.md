# Iterative Generation of Adversarial Example for Deep Code Models

**Authors**: Huang, Li and Sun, Weifeng and Yan, Meng

**Abstract**:

Deep code models are vulnerable to adversarial attacks, making it possible for semantically identical inputs to trigger different responses. Current black-box attack methods typically prioritize the impact of identifiers on the model based on custom importance scores or program context and incrementally replace identifiers to generate adversarial examples. However, these methods often fail to fully leverage feedback from failed attacks to guide subsequent attacks, resulting in problems such as local optima bias and efficiency dilemmas. In this paper, we introduce ITGen, a novel black-box adversarial example generation method that iteratively utilizes feedback from failed attacks to refine the generation process. It employs a bitvectorbased representation of code variants to mitigate local optima bias. By integrating these bit vectors with feedback from failed attacks, ITGen uses an enhanced Bayesian optimization framework to efficiently predict the most promising code variants, significantly reducing the search space and thus addressing the efficiency dilemma. We conducted experiments on a total of nine deep code models for both understanding and generation tasks, demonstrating ITGen's effectiveness and efficiency, as well as its ability to enhance model robustness through adversarial finetuning. For example, on average, ITGen improves the attack success rate by 47.98 % and 69.70 % over the state-of-the-art techniques (i.e., ALERT and BeamAttack), respectively.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00086)

**Labels**: [code model](../../labels/code_model.md), [code model robustness](../../labels/code_model_robustness.md)
