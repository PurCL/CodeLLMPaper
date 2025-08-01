# CodeImprove: Program Adaptation for Deep Code Models

**Authors**: Rathnasuriya, Ravishka and Zhao, Zijie and Yang, Wei

**Abstract**:

Leveraging deep learning (DL)-based code analysis tools to solve software engineering tasks is becoming increasingly popular. Code models often suffer performance degradation due to various reasons (e.g., code data shifts). Retraining is often required to address these issues, but frequent model updates are costly in labeling and deployment. In this paper, we explore an alternative solution: Adapting the program inputs to the code models. This can be achieved by two steps: 1) input validation that focuses on identifying whether an input is an out-of-scope input program that are beyond a model's handling capability, and 2) input adaptation that adapts out-of-scope inputs to become in-scope inputs. Validating program input is challenging, as current techniques focus on continuous inputs such as image data and fail with discrete inputs like code data, which have unique characteristics and are processed differently by deep learning models. Adapting out-of-scope programs is also challenging due to their vast search spaces. Therefore, in this paper, we propose CodeImprove, which distinguishes out-of-scope from normal inputs and converts such out-of-scope inputs back to in-scope inputs through program transformation. In particular, we propose a validity score metric to identify out-of-scope inputs and leverage genetics algorithms to apply semantic preserving program transformation to convert out-ofscope inputs to in-scope inputs. Our experimental results show CodeImprove can enhance upto 8.78% of accuracy, and 51.28% of relative improvements in three code models on two SE tasks. Additionally, our input validation is promising in detecting out-of-scope inputs (AUC score of 0.924).

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00139)

**Labels**: [general coding task](../../labels/general_coding_task.md), [code generation](../../labels/code_generation.md), [code model](../../labels/code_model.md), [code model robustness](../../labels/code_model_robustness.md)
