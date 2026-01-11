# Planning a Large Language Model for Static Detection of Runtime Errors in Code Snippets

**Authors**: Patel, Smit and Yadavally, Aashish and Dhulipala, Hridya and Nguyen, Tien N.

**Abstract**:

Large Language Models (LLMs) have been excellent in generating and reasoning about source code and natural-language texts. They can recognize patterns, syntax, and semantics in code, making them effective in several software engineering tasks. However, they exhibit weaknesses in reasoning about the program execution. They primarily operate on static code representations, failing to capture the dynamic behavior and state changes that occur during program execution. In this paper, we advance the capabilities of LLMs in reasoning about dynamic program behaviors. We propose Orca, a novel approach that instructs an LLM to autonomously formulate a plan to navigate through a control flow graph (CFG) for predictive execution of (in)complete code snippets. It acts as a predictive interpreter to “execute” the code. In Orca, we guide the LLM to pause at the branching point, focusing on the state of the symbol tables for variables' values, thus minimizing error propagation in the LLM's computation. We instruct the LLM not to stop at each step in its execution plan, resulting the use of only one prompt for the entire predictive interpreter, thus much cost-saving. As a downstream task, we use Orca to statically identify any runtime errors for online code snippets. Early detection of runtime errors and defects in these snippets is crucial to prevent costly fixes later in the development cycle after they were adapted into a codebase. Our empirical evaluation showed that Orca is effective and improves over the state-of-the-art approaches in predicting the execution traces and in static detection of runtime errors.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00102)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
