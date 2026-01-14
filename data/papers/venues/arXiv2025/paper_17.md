# Can LLMs Formally Reason as Abstract Interpreters for Program Analysis?

**Authors**: Jacqueline L. Mitchell, Brian Hyeongseok Kim, Chenyu Zhou, Chao Wang

**Abstract**:

LLMs have demonstrated impressive capabilities in code generation and comprehension, but their potential in being able to perform program analysis in a formal, automatic manner remains under-explored. To that end, we systematically investigate whether LLMs can reason about programs using a program analysis framework called abstract interpretation. We prompt LLMs to follow two different strategies, denoted as Compositional and Fixed Point Equation, to formally reason in the style of abstract interpretation, which has never been done before to the best of our knowledge. We validate our approach using state-of-the-art LLMs on 22 challenging benchmark programs from the Software Verification Competition (SV-COMP) 2019 dataset, widely used in program analysis. Our results show that our strategies are able to elicit abstract interpretation-based reasoning in the tested models, but LLMs are susceptible to logical errors, especially while interpreting complex program structures, as well as general hallucinations. This highlights key areas for improvement in the formal reasoning capabilities of LLMs.

**Link**: [Read Paper](https://arxiv.org/abs/2503.12686)

**Labels**: [static analysis](../../labels/static_analysis.md), [abstract interpretation](../../labels/abstract_interpretation.md)
