# COCA: Generative Root Cause Analysis for Distributed Systems with Code Knowledge

**Authors**: Li, Yichen and Wu, Yulun and Liu, Jinyang and Jiang, Zhihan and Chen, Zhuangbin and Yu, Guangba and Lyu, Michael R.

**Abstract**:

Runtime failures are commonplace in modern distributed systems. When such issues arise, users often turn to platforms such as Github or JIRA to report them and request assistance. Automatically identifying the root cause of these failures is critical for ensuring high reliability and availability. However, prevailing automatic root cause analysis (RCA) approaches rely significantly on comprehensive runtime monitoring data, which is often not fully available in issue platforms. Recent methods leverage large language models (LLMs) to analyze issue reports, but their effectiveness is limited by incomplete or ambiguous user-provided information. To obtain more accurate and comprehensive RCA results, the core idea of this work is to extract additional diagnostic clues from code to supplement data-limited issue reports. Specifically, we propose COCA, a code knowledge enhanced root cause analysis approach for issue reports. Based on the data within issue reports, COCA intelligently extracts relevant code snippets and reconstructs execution paths, providing a comprehensive execution context for further RCA. Subsequently, COCA constructs a prompt combining historical issue reports along with profiled code knowledge, enabling the LLMs to generate detailed root cause summaries and localize responsible components. Our evaluation on datasets from five real-world distributed systems demonstrates that COCA significantly outperforms existing methods, achieving a $\mathbf{2 8. 3 \%}$ improvement in root cause localization and a 22.0 % improvement in root cause summarization. Furthermore, COCA's performance consistency across various LLMs underscores its robust generalizability.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00234)

**Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md), [bug reproduction](../../labels/bug_reproduction.md)
