# USENIXSec2024

Number of papers: 7

## [CellularLint: A Systematic Approach to Identify Inconsistent Behavior in Cellular Network Specifications](paper_7.md)
- **Authors**: Mirza Masfiqur Rahman, Imtiaz Karim, and Elisa Bertino
- **Abstract**: In recent years, there has been a growing focus on scrutinizing the security of cellular networks, often attributing security vulnerabilities to issues in the underlying protocol design descriptions. These protocol design specifications, typically extensive documents that are thousands of pages long, can harbor inaccuracies, underspecifications, implicit assumptions, and internal inconsistencies. In light of the evolving landscape, we introduce CellularLint—a semi-automatic framework for inconsi...
- **Link**: [Read Paper](https://www.usenix.org/system/files/usenixsecurity24-rahman.pdf)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [specification inference](../../labels/specification_inference.md)


## [From One Thousand Pages of Specification to Unveiling Hidden Bugs:Large Language Model Assisted Fuzzing of Matter IoT Devices](paper_5.md)
- **Authors**: Xiaoyue Ma, Lannan Luo, and Qiang Zeng
- **Abstract**: Matter is an IoT connectivity standard backed by over two hundred companies. Since the release of its specification in October 2022, numerous IoT devices have become Matter-compatible. Identifying bugs and vulnerabilities in Matter devices is thus an emerging important problem. This paper introduces mGPTFuzz, the first Matter fuzzer in the literature. Our approach harnesses the extensive and detailed information within the Matter specification to guide the generation of test inputs. However, due...
- **Link**: [Read Paper](https://www.usenix.org/conference/usenixsecurity24/presentation/ma-xiaoyue)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


## [Fuzzing BusyBox: Leveraging LLM and Crash Reuse for Embedded Bug Unearthing](paper_4.md)
- **Authors**: Asmita, Yaroslav Oliinyk,  Michael Scott, Ryan Tsang, Chongzhou Fang, and Houman Homayoun
- **Abstract**: BusyBox, an open-source software bundling over 300 essential Linux commands into a single executable, is ubiquitous in Linux-based embedded devices. Vulnerabilities in BusyBox can have far-reaching consequences, affecting a wide array of devices. This research, driven by the extensive use of BusyBox, delved into its analysis. The study revealed the prevalence of older BusyBox versions in real-world embedded products, prompting us to conduct fuzz testing on BusyBox. Fuzzing, a pivotal software te...
- **Link**: [Read Paper](https://www.usenix.org/system/files/usenixsecurity24-asmita.pdf)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


## [Hermes: Unlocking Security Analysis of Cellular Network Protocols by Synthesizing Finite State Machines from Natural Language Specifications](paper_6.md)
- **Authors**: Abdullah Al Ishtiaq, Sarkar Snigdha Sarathi Das, Syed Md Mukit Rashid, Ali Ranjbar, Kai Tu, Tianwei Wu, Zhezheng Song, Weixuan Wang, Mujtahid Akon, Rui Zhang, Syed Rafiul Hussain
- **Abstract**: In this paper, we present Hermes, an end-to-end framework to automatically generate formal representations from natural language cellular specifications. We first develop a neural constituency parser, NEUTREX, to process transition-relevant texts and extract transition components (i.e., states, conditions, and actions). We also design a domain-specific language to translate these transition components to logical formulas by leveraging dependency parse trees. Finally, we compile these logical for...
- **Link**: [Read Paper](https://arxiv.org/abs/2310.04381)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [specification inference](../../labels/specification_inference.md)


## [Large Language Models for Code Analysis: Do LLMs Really Do Their Job?](paper_1.md)
- **Authors**: Chongzhou Fang and Ning Miao and Shaurya Srivastav and Jialin Liu and Ruoyu Zhang and Ruijie Fang and Asmita and Ryan Tsang and Najmeh Nazari and Han Wang and Houman Homayoun
- **Abstract**: Large language models (LLMs) have demonstrated significant potential in the realm of natural language understanding and programming code processing tasks. Their capacity to comprehend and generate human-like code has spurred research into harnessing LLMs for code analysis purposes. However, the existing body of literature falls short in delivering a systematic evaluation and assessment of LLMs' effectiveness in code analysis, particularly in the context of obfuscated code.This paper seeks to bri...
- **Link**: [Read Paper](https://www.usenix.org/conference/usenixsecurity24/presentation/fang)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


## [Leveraging Semantic Relations in Code and Data to Enhance Taint Analysis of Embedded Systems](paper_2.md)
- **Authors**: Zhao, Jiaxu and Li, Yuekang and Zou, Yanyan and Liang, Zhaohui and Xiao, Yang and Li, Yeting and Peng, Bingwei and Zhong, Nanyu and Wang, Xinyi and Wang, Wei and others
- **Abstract**: IoT devices have significantly impacted our daily lives, and detecting vulnerabilities in embedded systems early on is critical for ensuring their security. Among the existing vulnerability detection techniques for embedded systems, static taint analysis has been proven effective in detecting severe vulnerabilities, such as command injection vulnerabilities, which can cause remote code execution. Nevertheless, static taint analysis is faced with the problem of identifying sources comprehensively...
- **Link**: [Read Paper](https://www.usenix.org/system/files/usenixsecurity24-zhao.pdf)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [When Threads Meet Interrupts: Effective Static Detection of Interrupt-Based Deadlocks in Linux](paper_3.md)
- **Authors**: Chengfeng Ye, Yuandao Cai, and Charles Zhang
- **Abstract**: Deadlocking is an unresponsive state of software that arises when threads hold locks while trying to acquire other locks that are already held by other threads, resulting in a circular lock dependency. Interrupt-based deadlocks, a specific and prevalent type of deadlocks that occur within the OS kernel due to interrupt preemption, pose significant risks to system functionality, performance, and security. However, existing static analysis tools focus on resource-based deadlocks without characteri...
- **Link**: [Read Paper](https://www.usenix.org/system/files/usenixsecurity24-zhao.pdf)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [specification inference](../../labels/specification_inference.md)
