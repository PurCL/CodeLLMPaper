# LLM-Based Repair of Static Nullability Errors

**Authors**: Karimipour, Nima and Pradel, Michael and Kellogg, Martin and Sridharan, Manu

**Abstract**:

Modern Java projects increasingly adopt static analysis tools that prevent null-pointer exceptions by treating nullness as a type property. However, integrating such tools into large, existing codebases remains a significant challenge. While annotation inference can eliminate many errors automatically, a subset of residual errors -- typically a mix of real bugs and false positives -- often persist and can only be resolved via code changes. Manually addressing these errors is tedious and error-prone. Large language models (LLMs) offer a promising path toward automating these repairs, but naively-prompted LLMs often generate incorrect, contextually-inappropriate edits. Resolving a nullability error demands a deep understanding of how a symbol is used across the codebase, often spanning methods, classes, and packages. We present NullRepair, a system that integrates LLMs into a structured workflow for resolving the errors from a nullability checker. NullRepair's decision process follows a flowchart derived from manual analysis of 200 real-world errors. It leverages static analysis to identify safe and unsafe usage regions of symbols, using error-free usage examples to contextualize model prompts. Patches are generated through an iterative interaction with the LLM that incorporates project-wide context and decision logic. Our evaluation on 12 real-world Java projects shows that NullRepair resolves an average of 72% of the errors that remain after applying a state-of-the-art annotation inference technique. Unlike a naively-prompted LLM, NullRepair also largely preserves program semantics, with all unit tests passing in 10/12 projects after applying every edit proposed by NullRepair, and 98% or more tests passing in the remaining two projects.

**Link**: [Read Paper](https://arxiv.org/pdf/2507.20674)

**Labels**: [program repair](../../labels/program_repair.md)
