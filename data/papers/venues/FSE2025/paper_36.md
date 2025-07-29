# CoverUp: Effective High Coverage Test Generation for Python

**Authors**: Altmayer Pizzorno, Juan and Berger, Emery D.

**Abstract**:

Testing is an essential part of software development. Test generation tools attempt to automate the otherwise labor-intensive task of test creation, but generating high-coverage tests remains challenging. This paper proposes CoverUp, a novel approach to driving the generation of high-coverage Python regression tests. CoverUp combines coverage analysis, code context, and feedback in prompts that iteratively guide the LLM to generate tests that improve line and branch coverage.   We evaluate our prototype CoverUp implementation across a benchmark of challenging code derived from open-source Python projects and show that CoverUp substantially improves on the state of the art. Compared to CodaMosa, a hybrid search/LLM-based test generator, CoverUp achieves a per-module median line+branch coverage of 80\% (vs. 47\%). Compared to MuTAP, a mutation- and LLM-based test generator, CoverUp achieves an overall line+branch coverage of 89\% (vs. 77\%). We also demonstrate that CoverUp’s performance stems not only from the LLM used but from the combined effectiveness of its components.

**Link**: [Read Paper](https://doi.org/10.1145/3729398)

**Labels**: [program testing](../../labels/program_testing.md), [general testing](../../labels/general_testing.md)
