# Program Skeletons for Automated Program Translation

**Authors**: Bo Wang, Tianyu Li, Ruishi Li, Umang Mathur, Prateek Saxena

**Abstract**:

Translating software between programming languages is a challenging task, for which automated techniques have been elusive and hard to scale up to larger programs. A key difficulty in cross-language translation is that one has to re-express the intended behavior of the source program into idiomatic constructs of a different target language. This task needs abstracting away from the source language-specific details, while keeping the overall functionality the same. In this work, we propose a novel and systematic approach for making such translation amenable to automation based on a framework we call program skeletons. A program skeleton retains the high-level structure of the source program by abstracting away and effectively summarizing lower-level concrete code fragments, which can be mechanically translated to the target programming language. A skeleton, by design, permits many different ways of filling in the concrete implementation for fragments, which can work in conjunction with existing data-driven code synthesizers. Most importantly, skeletons can conceptually enable sound decomposition, i.e., if each individual fragment is correctly translated, taken together with the mechanically translated skeleton, the final translated program is deemed to be correct as a whole. We present a prototype system called SKEL embodying the idea of skeleton-based translation from Python to JavaScript. Our results show promising scalability compared to prior works. For 9 real-world Python programs, some with more than about 1k lines of code, 95% of their code fragments can be automatically translated, while about 5% require manual effort. All the final translations are correct with respect to whole-program test suites.

**Link**: [Read Paper](https://dl.acm.org/doi/10.1145/3729287)

**Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)
