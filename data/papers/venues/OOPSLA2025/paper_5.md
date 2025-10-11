# Interleaving Large Language Models for Compiler Testing

**Authors**: Ni, Yunbo and Li, Shaohua

**Abstract**:

Testing compilers with AI models, especially large language models (LLMs), has shown great promise. However, current approaches struggle with two key problems: The generated programs for testing compilers are often too simple, and extensive testing with the LLMs is computationally expensive. In this paper, we propose a novel compiler testing framework that decouples the testing process into two distinct phases: an offline phase and an online phase. In the offline phase, we use LLMs to generate a collection of small but feature-rich code pieces. In the online phase, we reuse these code pieces by strategically combining them to build high-quality and valid test programs, which are then used to test compilers. We implement this idea in a tool, LegoFuzz, for testing C compilers. The results are striking: we found 66 bugs in GCC and LLVM, the most widely used C compilers. Almost half of the bugs are miscompilation bugs, which are serious and hard-to-find bugs that none of the existing LLM-based tools could find. We believe this efficient design opens up new possibilities for using AI models in software testing beyond just C compilers.

**Link**: [Read Paper](https://doi.org/10.1145/3763079)

**Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)
