# OOPSLA2025

Number of papers: 4

## [API-Guided Dataset Synthesis to Finetune Large Code Models](paper_4.md)
- **Authors**: Li, Zongjie and Wu, Daoyuan and Wang, Shuai and Su, Zhendong
- **Abstract**: Large code models (LCMs), pre-trained on vast code corpora, have demonstrated remarkable performance across a wide array of code-related tasks. Supervised fine-tuning (SFT) plays a vital role in aligning these models with specific requirements and enhancing their performance in particular domains. However, synthesizing high-quality SFT datasets poses a significant challenge due to the uneven quality of datasets and the scarcity of domain-specific datasets. Inspired by APIs as high-level abstract...
- **Link**: [Read Paper](https://doi.org/10.1145/3720449)
- **Labels**: [source code model](../../labels/source_code_model.md)


## [Artemis: Toward Accurate Detection of Server-Side Request Forgeries through LLM-Assisted Inter-procedural Path-Sensitive Taint Analysis](paper_2.md)
- **Authors**: Yuchen Ji, Ting Dai, Zhichao Zhou, Yutian Tang, Jingzhu He
- **Abstract**: Server-side request forgery (SSRF) vulnerabilities are inevitable in PHP web applications. Existing static tools in detecting vulnerabilities in PHP web applications neither contain SSRF-related features to enhance detection accuracy nor consider PHP’s dynamic type features. In this paper, we present Artemis, a static taint analysis tool for detecting SSRF vulnerabilities in PHP web applications. First, Artemis extracts both PHP built-in and third-party functions as candidate source and sink fun...
- **Link**: [Read Paper](https://dl.acm.org/doi/10.1145/3720488)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Laurel: Unblocking Automated Verification with Large Language Models](paper_3.md)
- **Authors**: YEric Mugnier, Emmanuel Anaya Gonzalez, Nadia Polikarpova, Ranjit Jhala, Zhou Yuanyuan
- **Abstract**: Program verifiers such as Dafny automate proofs by outsourcing them to an SMT solver. This automation is not perfect, however, and the solver often requires hints in the form of assertions, creating a burden for the proof engineer. In this paper, we propose, a tool that alleviates this burden by automatically generating assertions using large language models (LLMs). To improve the success rate of LLMs in this task, we design two domain-specific prompting techniques. First, we help the LLM determ...
- **Link**: [Read Paper](https://dl.acm.org/doi/10.1145/3720499)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


## [Show Me Why It’s Correct: Saving 1/3 of Debugging Time in Program Repair with Interactive Runtime Comparison](paper_1.md)
- **Authors**: Ruixin Wang, Zhongkai Zhao, Le Fang, Nan Jiang, Yiling Lou, Lin Tan, Tianyi Zhang
- **Abstract**: Automated Program Repair (APR) holds the promise of alleviating the burden of debugging and fixing software bugs. Despite this, developers still need to manually inspect each patch to confirm its correctness, which is tedious and time-consuming. This challenge is exacerbated in the presence of plausible patches, which accidentally pass test cases but may not correctly fix the bug. To address this challenge, we propose an interactive approach called iFix to facilitate patch understanding and comp...
- **Link**: [Read Paper](https://dl.acm.org/doi/10.1145/3720510)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md)
