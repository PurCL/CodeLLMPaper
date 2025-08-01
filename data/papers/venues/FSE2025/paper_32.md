# Code Red! On the Harmfulness of Applying Off-the-Shelf Large Language Models to Programming Tasks

**Authors**: Al-Kaswan, Ali and Deatc, Sebastian and Ko\c{c}, Beg\"{u}m and van Deursen, Arie and Izadi, Maliheh

**Abstract**:

Nowadays, developers increasingly rely on solutions powered by Large Language Models (LLM) to assist them with their coding tasks. This makes it crucial to align these tools with human values to prevent malicious misuse.   In this paper,   we propose a comprehensive framework   for assessing the potential harmfulness   of LLMs within the software engineering domain.   We begin by developing a taxonomy of potentially harmful software engineering scenarios  and subsequently, create a dataset of prompts based on this taxonomy.   To systematically assess the responses,   we design and validate   an automatic evaluator   that classifies the outputs   of a variety of LLMs   both open-source and closed-source models,   as well as general-purpose and code-specific LLMs.   Furthermore, we investigate the impact of   models' size, architecture family, and alignment strategies   on their tendency to generate harmful content.   \% Results   The results show significant disparities in the alignment of various LLMs for harmlessness.  We find that   some models   and model families, such as Openhermes,   are more harmful than others   and that code-specific models   do not perform better   than their general-purpose counterparts.   Notably, some fine-tuned models   perform significantly worse than their base-models   due to their design choices.   On the other side,   we find that   larger models tend to be more helpful   and are less likely to respond with harmful information.   These results highlight the importance of targeted alignment strategies tailored to the unique challenges of software engineering tasks   and provide a foundation for future work in this critical area.

**Link**: [Read Paper](https://doi.org/10.1145/3729380)

**Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [empirical study](../../labels/empirical_study.md)
