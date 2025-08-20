# Hysynth: Context-free llm approximation for guiding program synthesis

**Authors**: Barke, Shraddha and Anaya Gonzalez, Emmanuel and Kasibatla, Saketh Ram and Berg-Kirkpatrick, Taylor and Polikarpova, Nadia

**Abstract**:

Many structured prediction and reasoning tasks can be framed as program synthesis problems, where the goal is to generate a program in a domain-specific language (DSL) that transforms input data into the desired output. Unfortunately, purely neural approaches, such as large language models (LLMs), often fail to produce fully correct programs in unfamiliar DSLs, while purely symbolic methods based on combinatorial search scale poorly to complex problems. Motivated by these limitations, we introduce a hybrid approach, where LLM completions for a given task are used to learn a task-specific, context-free surrogate model, which is then used to guide program synthesis. We evaluate this hybrid approach on three domains, and show that it outperforms both unguided search and direct sampling from LLMs, as well as existing program synthesizers.

**Link**: [Read Paper](https://openreview.net/forum?id=5jt0ZSA6Co)

**Labels**: [program synthesis](../../labels/program_synthesis.md)
