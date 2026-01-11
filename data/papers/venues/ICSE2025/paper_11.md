# TIGER: A Generating-Then-Ranking Framework for Practical Python Type Inference

**Authors**: Wang, Chong and Zhang, Jian and Lou, Yiling and Liu, Mingwei and Sun, Weisong and Liu, Yang and Peng, Xin

**Abstract**:

Python's dynamic typing system offers flexibility and expressiveness but can lead to type-related errors, prompting the need for automated type inference to enhance type hinting. While existing learning-based approaches show promising inference accuracy, they struggle with practical challenges in comprehensively handling various types, including complex parameterized types and (unseen) user-defined types. In this paper, we introduce TIGER, a two-stage generating-then-ranking (GTR) framework, designed to effectively handle Python's diverse type categories. TIGER leverages fine-tuned pre-trained code models to train a generative model with a span masking objective and a similarity model with a contrastive training objective. This approach allows TIGER to generate a wide range of type candidates, including complex parameterized types in the generating stage, and accurately rank them with user-defined types in the ranking stage. Our evaluation on the ManyTypes4Py dataset shows TIGER's advantage over existing methods in various type categories, notably improving accuracy in inferring user-defined and unseen types by 11.2% and 20.1% respectively in Top-5 Exact Match. Moreover, the experimental results not only demonstrate TIGER's superior performance and efficiency, but also underscore the significance of its generating and ranking stages in enhancing automated type inference.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00019)

**Labels**: [static analysis](../../labels/static_analysis.md), [type inference](../../labels/type_inference.md)
