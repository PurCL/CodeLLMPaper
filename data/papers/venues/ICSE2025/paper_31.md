# TOGLL: Correct and Strong Test Oracle Generation with LLMS

**Authors**: Hossain, Soneya Binta and Dwyer, Matthew B.

**Abstract**:

Test oracles play a crucial role in software testing, enabling effective bug detection. Despite initial promise, neural methods for automated test oracle generation often result in a large number of false positives and weaker test oracles. While LLMs have shown impressive effectiveness in various software engineering tasks, including code generation, test case creation, and bug fixing, there remains a notable absence of large-scale studies exploring their effectiveness in test oracle generation. The question of whether LLMs can address the challenges in effective oracle generation is both compelling and requires thorough investigation. In this research, we present the first comprehensive study to investigate the capabilities of LLMs in generating correct, diverse, and strong test oracles capable of effectively identifying a large number of unique bugs. To this end, we fine-tuned seven code LLMs using six distinct prompts on a large dataset consisting of 110 Java projects. Utilizing the most effective finetuned LLM and prompt pair, we introduce TOGLL, a novel LLM-based method for test oracle generation. To investigate the generalizability of TOGLL, we conduct studies on 25 unseen large-scale Java projects. Besides assessing the correctness, we also assess the diversity and strength of the generated oracles. We compare the results against EvoSuite and the state-of-the-art neural method, TOGA. Our findings reveal that TOGLL can produce 3.8 times more correct assertion oracles and 4.9 times more exception oracles than TOGA. Regarding bug detection effectiveness, TOGLL can detect 1,023 unique mutants that EvoSuite cannot, which is ten times more than what TOGA can detect. Additionally, TOGLL significantly outperforms TOGA in detecting real bugs from the Defects4J dataset.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00098)

**Labels**: [program testing](../../labels/program_testing.md), [empirical study](../../labels/empirical_study.md)
