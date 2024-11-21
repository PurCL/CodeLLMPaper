# SpecGen: Automated Generation of Formal Program Specifications via Large Language Models

**Authors**: Ma, Lezhi and Liu, Shangqing and Li, Yi and Xie, Xiaofei and Bu, Lei

**Abstract**:

In software development, formal program specifications play a crucial role in various stages. However, manually crafting formal program specifications is rather difficult, making the job time-consuming and labor-intensive. Moreover, it is even more challenging to write specifications that correctly and comprehensively describe the semantics of complex programs. To reduce the burden on software developers, automated specification generation methods have emerged. However, existing methods usually rely on predefined templates or grammar, making them struggle to accurately describe the behavior and functionality of complex real-world programs. To tackle this challenge, we introduce SpecGen, a novel technique for formal program specification generation based on Large Language Models. Our key insight is to overcome the limitations of existing methods by leveraging the code comprehension capability of LLMs. The process of SpecGen consists of two phases. The first phase employs a conversational approach that guides the LLM to generate appropriate specifications for a given program. The second phase, designed for where the LLM fails to generate correct specifications, applies four mutation operators to the model-generated specifications and selects verifiable specifications from the mutated ones through a novel heuristic selection strategy by assigning different weights of variants in an efficient manner. To evaluate the performance of SpecGen, we manually construct a dataset containing 120 test cases. Our experimental results demonstrate that SpecGen succeeds in generating verifiable specifications for 100 out of 120 programs, outperforming the existing purely LLM-based approaches and conventional specification generation tools. Further investigations on the quality of generated specifications indicate that SpecGen can comprehensively articulate the behaviors of the input program.

**Link**: [Read Paper](No Link Available)

**Labels**: static analysis, specification inference
