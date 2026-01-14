# QLCoder: A Query Synthesizer For Static Analysis of Security Vulnerabilities

**Authors**: Claire Wang, Ziyang Li, Saikat Dutta, Mayur Naik

**Abstract**:

Static analysis tools provide a powerful means to detect security vulnerabilities by specifying queries that encode vulnerable code patterns. However, writing such queries is challenging and requires diverse expertise in security and program analysis. To address this challenge, we present QLCoder - an agentic framework that automatically synthesizes queries in CodeQL, a powerful static analysis engine, directly from a given CVE metadata. QLCode embeds an LLM in a synthesis loop with execution feedback, while constraining its reasoning using a custom MCP interface that allows structured interaction with a Language Server Protocol (for syntax guidance) and a RAG database (for semantic retrieval of queries and documentation). This approach allows QLCoder to generate syntactically and semantically valid security queries. We evaluate QLCode on 176 existing CVEs across 111 Java projects. Building upon the Claude Code agent framework, QLCoder synthesizes correct queries that detect the CVE in the vulnerable but not in the patched versions for 53.4% of CVEs. In comparison, using only Claude Code synthesizes 10% correct queries.

**Link**: [Read Paper](https://arxiv.org/pdf/2511.08462)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
