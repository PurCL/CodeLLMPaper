# Aligning the Objective of LLM-Based Program Repair

**Authors**: Xu, Junjielong and Fu, Ying and Tan, Shin Hwei and He, Pinjia

**Abstract**:

Large language models (LLMs) have achieved decent results on automated program repair (APR). However, the next token prediction training objective of decoder-only LLMs (e.g., GPT-4) is misaligned with the masked span prediction objective of current infilling-style methods, which impedes LLMs from fully leveraging pre-trained knowledge for program repair. In addition, while some LLMs can locate and repair bugs in certain functions using the related artifacts (e.g., test cases), existing methods still depend on statement-level fault localization methods to provide a list of buggy hunks for repair. This restriction hinders LLMs from exploring potential patches beyond the given locations. In this paper, we investigate a new approach to adapt LLMs to program repair. Our core insight is that LLM's APR capability can be greatly improved by simply aligning the output to their training objective and allowing them to refine the whole program without first identifying faulty statements. Based on this insight, we designed D4C, a straightforward prompting framework for APR. D4C can repair 180 bugs correctly in Defects4J, with each patch being sampled only 10 times. This surpasses the SOTA APR methods with perfect fault localization by 10 % and reduces the patch sampling number by 90 %. Our findings reveal that (1) objective alignment is crucial for fully exploiting LLM's pre-trained capability, and (2) replacing the traditional localize-buggy-hunks-then-repair workflow with direct debugging is more effective for LLM-based APR methods. Thus, we believe this paper introduces a new mindset for harnessing LLMs in APR.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00169)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
