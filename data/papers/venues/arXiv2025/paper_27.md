# PoCGen: Generating Proof-of-Concept Exploits for Vulnerabilities in Npm Packages

**Authors**: Simsek, Deniz and Eghbali, Aryaz and Pradel, Michael

**Abstract**:

Security vulnerabilities in software packages are a significant concern for developers and users alike. Patching these vulnerabilities in a timely manner is crucial to restoring the integrity and security of software systems. However, previous work has shown that vulnerability reports often lack proof-of-concept (PoC) exploits, which are essential for fixing the vulnerability, testing patches, and avoiding regressions. Creating a PoC exploit is challenging because vulnerability reports are informal and often incomplete, and because it requires a detailed understanding of how inputs passed to potentially vulnerable APIs may reach security-relevant sinks. In this paper, we present PoCGen, a novel approach to autonomously generate and validate PoC exploits for vulnerabilities in npm packages. This is the first fully autonomous approach to use large language models (LLMs) in tandem with static and dynamic analysis techniques for PoC exploit generation. PoCGen leverages an LLM for understanding vulnerability reports, for generating candidate PoC exploits, and for validating and refining them. Our approach successfully generates exploits for 77% of the vulnerabilities in the SecBench.js dataset and 39% in a new, more challenging dataset of 794 recent vulnerabilities. This success rate significantly outperforms a recent baseline (by 45 absolute percentage points), while imposing an average cost of $0.02 per generated exploit.

**Link**: [Read Paper](https://arxiv.org/pdf/2506.04962)

**Labels**: [vulnerability exploitation](../../labels/vulnerability_exploitation.md)
