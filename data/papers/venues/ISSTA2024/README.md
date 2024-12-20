# ISSTA2024

Number of papers: 28

## [AI Coders Are among Us: Rethinking Programming Language Grammar towards Efficient Code Generation](paper_13.md)
- **Authors**: Sun, Zhensu and Du, Xiaoning and Yang, Zhou and Li, Li and Lo, David
- **Abstract**: Artificial Intelligence (AI) models have emerged as another important audience for programming languages alongside humans and machines, as we enter the era of large language models (LLMs). LLMs can now perform well in coding competitions and even write programs like developers to solve various tasks, including mathematical problems. However, the grammar and layout of current programs are designed to cater the needs of human developers -- with many grammar tokens and formatting tokens being used ...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680347)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [AutoCodeRover: Autonomous Program Improvement](paper_20.md)
- **Authors**: Zhang, Yuntong and Ruan, Haifeng and Fan, Zhiyu and Roychoudhury, Abhik
- **Abstract**: Researchers have made significant progress in automating the software development process in the past decades. Automated techniques for issue summarization, bug reproduction, fault localization, and program repair have been built to ease the workload of developers. Recent progress in Large Language Models (LLMs) has significantly impacted the development process, where developers can use LLM-based programming assistants to achieve automated coding. Nevertheless, software engineering involves the...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680384)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [Automated Program Repair via Conversation: Fixing 162 out of 337 Bugs for $0.42 Each using ChatGPT](paper_10.md)
- **Authors**: Xia, Chunqiu Steven and Zhang, Lingming
- **Abstract**: Automated Program Repair (APR) aims to automatically generate patches for buggy programs. Traditional APR techniques suffer from a lack of patch variety as they rely heavily on handcrafted or mined bug fixing patterns and cannot easily generalize to other bug/fix types. To address this limitation, recent APR work has been focused on leveraging modern Large Language Models (LLMs) to directly generate patches for APR. Such LLM-based APR tools work by first constructing an input prompt built using ...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680323)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [Automated Program Repair via Conversation:Fixing 162 out of 337 Bugs for $0.42 Each using ChatGPT](paper_2.md)
- **Authors**: Xia, Chunqiu Steven and Zhang, Lingming
- **Abstract**: Automated Program Repair (APR) aims to automatically generate patches for buggy programs. Traditional APR techniques suffer from a lack of patch variety as they rely heavily on handcrafted or mined bug fixing patterns and cannot easily generalize to other bug/fix types. To address this limitation, recent APR work has been focused on leveraging modern Large Language Models (LLMs) to directly generate patches for APR. Such LLM-based APR tools work by first constructing an input prompt built using ...
- **Link**: [Read Paper](https://dl.acm.org/doi/pdf/10.1145/3650212.3680323)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [Automating Zero-Shot Patch Porting for Hard Forks](paper_6.md)
- **Authors**: Pan, Shengyi and Wang, You and Liu, Zhongxin and Hu, Xing and Xia, Xin and Li, Shanping
- **Abstract**: Forking is a typical way of code reuse, which provides a simple way for developers to create a variant software (denoted as hard fork) by copying and modifying an existing codebase. Despite of the benefits, forking also leads to duplicate efforts in software maintenance. Developers need to port patches across the hard forks to address similar bugs or implement similar features. Due to the divergence between the source project and the hard fork, patch porting is complicated, which requires an ada...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3652134)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [empirical study](../../labels/empirical_study.md)


## [Benchmarking Automated Program Repair: An Extensive Study on Both Real-World and Artificial Bugs](paper_7.md)
- **Authors**: Ouyang, Yicheng and Yang, Jun and Zhang, Lingming
- **Abstract**: As bugs are inevitable and prevalent in real-world programs, many Automated Program Repair (APR) techniques have been proposed to generate patches for them. However, due to the lack of a standard for evaluating APR techniques, prior works tend to use different settings and benchmarks in evaluation, threatening the trustworthiness of the evaluation results. Additionally, they typically only adopt plausibility and genuineness as evaluation metrics, which may potentially mask some underlying issues...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3652140)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [benchmark](../../labels/benchmark.md)


## [CREF: An LLM-Based Conversational Software Repair Framework for Programming Tutors](paper_11.md)
- **Authors**: Yang, Boyang and Tian, Haoye and Pian, Weiguo and Yu, Haoran and Wang, Haitao and Klein, Jacques and Bissyand\'{e}, Tegawend\'{e} F. and Jin, Shunfu
- **Abstract**: With the proven effectiveness of Large Language Models (LLMs) in code-related tasks, researchers have explored their potential for program repair. However, existing repair benchmarks might have influenced LLM training data, potentially causing data leakage. To evaluate LLMs’ realistic repair capabilities, (i) we introduce an extensive, non-crawled benchmark TutorCode, comprising 1,239 C++ defect codes and associated information such as tutor guidance, solution description, failing test cases, an...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680328)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [CoEdPilot: Recommending Code Edits with Learned Prior Edit Relevance, Project-wise Awareness, and Interactive Nature](paper_8.md)
- **Authors**: Liu, Chenyan and Cai, Yufan and Lin, Yun and Huang, Yuhuan and Pei, Yunrui and Jiang, Bo and Yang, Ping and Dong, Jin Song and Mei, Hong
- **Abstract**: Recent years have seen the development of LLM-based code generation. Compared to generating code in a software project, incremental code edits are empirically observed to be more frequent. The emerging code editing approaches usually formulate the problem as generating an edit based on known relevant prior edits and context. However, practical code edits can be more complicated. First, an editing session can include multiple (ir)relevant edits to the code under edit. Second, the inference of the...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3652142)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [CoSec: On-the-Fly Security Hardening of Code LLMs via Supervised Co-decoding](paper_18.md)
- **Authors**: Li, Dong and Yan, Meng and Zhang, Yaosheng and Liu, Zhongxin and Liu, Chao and Zhang, Xiaohong and Chen, Ting and Lo, David
- **Abstract**: Large Language Models (LLMs) specialized in code have shown exceptional proficiency across various programming-related tasks, particularly code generation. Nonetheless, due to its nature of pretraining on massive uncritically filtered data, prior studies have shown that code LLMs are prone to generate code with potential vulnerabilities. Existing approaches to mitigate this risk involve crafting data without vulnerability and subsequently retraining or fine-tuning the model. As the number of par...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680371)
- **Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md)


## [CoderUJB: An Executable and Unified Java Benchmark for Practical Programming Scenarios](paper_3.md)
- **Authors**: Zeng, Zhengran and Wang, Yidong and Xie, Rui and Ye, Wei and Zhang, Shikun
- **Abstract**: In the evolving landscape of large language models (LLMs) tailored for software engineering, the need for benchmarks that accurately reflect real-world development scenarios is paramount. Current benchmarks are either too simplistic or fail to capture the multi-tasking nature of software development. To address this, we introduce CoderUJB, a new benchmark designed to evaluate LLMs across diverse Java programming tasks that are executable and reflective of actual development scenarios, acknowledg...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3652115)
- **Labels**: [code generation](../../labels/code_generation.md), [program testing](../../labels/program_testing.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)


## [Collaboration to Repository-Level Vulnerability Detection](paper_26.md)
- **Authors**: Wen, Xin-Cheng
- **Abstract**: Large Language Model (LLM)-based methods have proven to be effective for many software engineering domains, with a potential for substantial productivity effective for software vulnerability detection.    However, due to the limitation of the length of input contexts of LLM, the existing LLM-based methods mainly focus on detecting function-level and leveraging the in-file context information for vulnerability detection (i.e., intra-procedural vulnerabilities), ignoring the more complex inter-pro...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3685562)
- **Labels**: [code generation](../../labels/code_generation.md), [bug detection](../../labels/bug_detection.md)


## [Domain Adaptation for Code Model-Based Unit Test Case Generation](paper_28.md)
- **Authors**: Shin, Jiho and Hashtroudi, Sepehr and Hemmati, Hadi and Wang, Song
- **Abstract**: Recently, deep learning-based test case generation approaches have been proposed to automate the generation of unit test cases. In this study, we leverage Transformer-based code models to generate               unit tests with the help of Domain Adaptation (DA) at a project level. Specifically, we use CodeT5, a relatively small language model trained on source code data, and fine-tune it on the test generation               task. Then, we apply domain adaptation to each target project data to le...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680354)
- **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md)


## [Face It Yourselves: An LLM-Based Two-Stage Strategy to Localize Configuration Errors via Logs](paper_1.md)
- **Authors**: Shan, Shiwen and Huo, Yintong and Su, Yuxin and Li, Yichen and Li, Dan and Zheng, Zibin
- **Abstract**: Configurable software systems are prone to configuration errors, resulting in significant losses to companies. However, diagnosing these errors is challenging due to the vast and complex configuration space. These errors pose significant challenges for both experienced maintainers and new end-users, particularly those without access to the source code of the software systems. Given that logs are easily accessible to most end-users, we conduct a preliminary study to outline the challenges and opp...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3652106)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [software configuration](../../labels/software_configuration.md)


## [Fuzzing JavaScript Interpreters with Coverage-Guided Reinforcement Learning for LLM-Based Mutation](paper_22.md)
- **Authors**: Eom, Jueon and Jeong, Seyeon and Kwon, Taekyoung
- **Abstract**: JavaScript interpreters, crucial for modern web browsers, require an effective fuzzing method to identify security-related bugs. However, the strict grammatical requirements for input present significant challenges. Recent efforts to integrate language models for context- aware mutation in fuzzing are promising but lack the necessary coverage guidance to be fully effective. This paper presents a novel technique called CovRL (Coverage-guided Reinforcement Learning) that combines Large Language Mo...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680389)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [compiler testing](../../labels/compiler_testing.md)


## [HECS: A Hypergraph Learning-Based System for Detecting Extract Class Refactoring Opportunities](paper_25.md)
- **Authors**: Wang, Luqiao and Wang, Qiangqiang and Wang, Jiaqi and Zhao, Yutong and Wei, Minjie and Quan, Zhou and Cui, Di and Li, Qingshan
- **Abstract**: HECS is an advanced tool designed for Extract Class refactoring by leveraging hypergraph learning to model complex dependencies within large classes. Unlike traditional tools that rely on direct one-to-one dependency graphs, HECS uses intra-class dependency hypergraphs to capture one-to-many relationships. This allows HECS to provide more accurate and relevant refactoring suggestions. The tool constructs hypergraphs for each target class, attributes nodes using a pre-trained code model, and trai...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3685307)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [How Effective Are They? Exploring Large Language Model Based Fuzz Driver Generation](paper_14.md)
- **Authors**: Zhang, Cen and Zheng, Yaowen and Bai, Mingqiang and Li, Yeting and Ma, Wei and Xie, Xiaofei and Li, Yuekang and Sun, Limin and Liu, Yang
- **Abstract**: Fuzz drivers are essential for library API fuzzing. However, automatically generating fuzz drivers is a complex task, as it demands the creation of high-quality, correct, and robust API usage code. An LLM-based (Large Language Model) approach for generating fuzz drivers is a promising area of research. Unlike traditional program analysis-based generators, this text-based approach is more generalized and capable of harnessing a variety of API usage information, resulting in code that is friendly ...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680355)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


## [LLM4Fin: Fully Automating LLM-Powered Test Case Generation for FinTech Software Acceptance Testing](paper_21.md)
- **Authors**: Xue, Zhiyi and Li, Liangguo and Tian, Senyue and Chen, Xiaohong and Li, Pingping and Chen, Liangyu and Jiang, Tingting and Zhang, Min
- **Abstract**: FinTech software, crucial for both safety and timely market deployment, presents a compelling case for automated acceptance testing against regulatory business rules. However, the inherent challenges of comprehending unstructured natural language descriptions of these rules and crafting comprehensive test cases demand human intelligence. The emergence of Large Language Models (LLMs) holds promise for automated test case generation, leveraging their natural language processing capabilities. Yet, ...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680388)
- **Labels**: [program testing](../../labels/program_testing.md)


## [LPR: Large Language Models-Aided Program Reduction](paper_5.md)
- **Authors**: Zhang, Mengxiao and Tian, Yongqiang and Xu, Zhenyang and Dong, Yiwen and Tan, Shin Hwei and Sun, Chengnian
- **Abstract**: Program reduction is a widely used technique to facilitate debugging                compilers by automatically minimizing programs that trigger                compiler bugs. Existing program reduction techniques are either                generic to a wide range of languages (such as Perses and Vulcan)                or specifically optimized for one certain language by exploiting                language-specific knowledge (e.g., C-Reduce). However, synergistically                combining both g...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3652126)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md)


## [Large Language Models for Equivalent Mutant Detection: How Far Are We?](paper_23.md)
- **Authors**: Tian, Zhao and Shu, Honglin and Wang, Dong and Cao, Xuejie and Kamei, Yasutaka and Chen, Junjie
- **Abstract**: Mutation testing is vital for ensuring software quality. However, the presence of equivalent mutants is known to introduce redundant cost and bias issues, hindering the effectiveness of mutation testing in practical use. Although numerous equivalent mutant detection (EMD) techniques have been proposed, they exhibit limitations due to the scarcity of training data and challenges in generalizing to unseen mutants. Recently, large language models (LLMs) have been extensively adopted in various code...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680395)
- **Labels**: [program testing](../../labels/program_testing.md), [mutation testing](../../labels/mutation_testing.md), [empirical study](../../labels/empirical_study.md)


## [Maltracker: A Fine-Grained NPM Malware Tracker Copiloted by LLM-Enhanced Dataset](paper_24.md)
- **Authors**: Yu, Zeliang and Wen, Ming and Guo, Xiaochen and Jin, Hai
- **Abstract**: As the largest package registry, Node Package Manager (NPM) has become the prime target for various supply chain attacks recently and has been flooded with numerous malicious packages, posing significant security risks to end-users. Learning-based methods have demonstrated promising performance with good adaptability to various types of attacks. However, they suffer from two main limitations. First, they often utilize metadata features or coarse-grained code features extracted at the package lev...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680397)
- **Labels**: [static analysis](../../labels/static_analysis.md), [software composition analysis](../../labels/software_composition_analysis.md)


## [Neurosymbolic Repair of Test Flakiness](paper_17.md)
- **Authors**: Chen, Yang and Jabbarvand, Reyhaneh
- **Abstract**: Test flakiness, a non-deterministic behavior of builds irrelevant to code changes, is a major and continuing impediment to deliver- ing reliable software. The very few techniques for the automated repair of test flakiness are specifically crafted to repair either Order- Dependent (OD) or Implementation-Dependent (ID) flakiness. They are also all symbolic approaches, i.e., they leverage program analy- sis to detect and repair known test flakiness patterns and root causes, failing to generalize. T...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680369)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [One-to-One or One-to-Many? Suggesting Extract Class Refactoring Opportunities with Intra-class Dependency Hypergraph Neural Network](paper_19.md)
- **Authors**: Cui, Di and Wang, Qiangqiang and Zhao, Yutong and Wang, Jiaqi and Wei, Minjie and Hu, Jingzhao and Wang, Luqiao and Li, Qingshan
- **Abstract**: Excessively large classes that encapsulate multiple responsibilities are challenging to comprehend and maintain. Addressing this issue, several Extract Class refactoring tools have been proposed, employing a two-phase process: identifying suitable fields or methods for extraction, and implementing the mechanics of refactoring. These tools traditionally generate an intra-class dependency graph to analyze the class structure, applying hard-coded rules based on this graph to unearth refactoring opp...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680379)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [Oracle-Guided Program Selection from Large Language Models](paper_9.md)
- **Authors**: Fan, Zhiyu and Ruan, Haifeng and Mechtaev, Sergey and Roychoudhury, Abhik
- **Abstract**: While large language models (LLMs) have shown significant advancements in code generation, their susceptibility to producing incorrect code poses a significant challenge to the adoption of LLM-generated programs. This issue largely stems from the reliance on natural language descriptions as informal oracles in code generation. Current strategies to mitigate this involve selecting the best program from multiple LLM-generated alternatives, judged by criteria like the consistency of their execution...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680308)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [SCALE: Constructing Structured Natural Language Comment Trees for Software Vulnerability Detection](paper_4.md)
- **Authors**: Wen, Xin-Cheng and Gao, Cuiyun and Gao, Shuzheng and Xiao, Yang and Lyu, Michael R.
- **Abstract**: Recently, there has been a growing interest in automatic software vulnerability detection.     Pre-trained model-based approaches have demonstrated superior performance than other Deep Learning (DL)-based approaches in detecting vulnerabilities.     However, the existing pre-trained model-based approaches generally employ code sequences as input during prediction, and may ignore vulnerability-related structural information, as reflected in the following two aspects.     First, they tend to fail ...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3652124)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [SelfPiCo: Self-Guided Partial Code Execution with LLMs](paper_16.md)
- **Authors**: Xue, Zhipeng and Gao, Zhipeng and Wang, Shaohua and Hu, Xing and Xia, Xin and Li, Shanping
- **Abstract**: Code executability plays a vital role in software debugging and testing (e.g., detecting runtime exceptions or assertion violations). However, code execution, especially partial or arbitrary code execution, is a non-trivial task due to missing definitions and complex third-party dependencies. To make partial code (such as code snippets posted on the web or code fragments deep inside complex software projects) executable, the existing study has proposed a machine learning model to predict the und...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680368)
- **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md)


## [ThinkRepair: Self-Directed Automated Program Repair](paper_15.md)
- **Authors**: Yin, Xin and Ni, Chao and Wang, Shaohua and Li, Zhenhao and Zeng, Limin and Yang, Xiaohu
- **Abstract**: Though many approaches have been proposed for Automated Program Repair (APR) and indeed achieved remarkable performance, they still have limitations in fixing bugs that require analyzing and reasoning about the logic of the buggy program. Recently, large language models (LLMs) instructed by prompt engineering have attracted much attention for their powerful ability to address many kinds of tasks including bug-fixing. However, the quality of the prompt will highly affect the ability of LLMs and m...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680359)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [UniTSyn: A Large-Scale Dataset Capable of Enhancing the Prowess of Large Language Models for Program Testing](paper_27.md)
- **Authors**: He, Yifeng and Huang, Jiabo and Rong, Yuyang and Guo, Yiwen and Wang, Ethan and Chen, Hao
- **Abstract**: The remarkable capability of large language models (LLMs) in generating high-quality code has drawn increasing attention in the software testing community. However, existing code LLMs often demonstrate unsatisfactory capabilities in generating accurate, complete tests since they were trained on code snippets collected without differentiating between code for testing and for other purposes. In this paper, we present a large-scale dataset, UniTSyn, which can enhance LLMs for Unit Test Synthesis. A...
- **Link**: [Read Paper](https://haochen.org/publications/he2024unitsyn.pdf)
- **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [benchmark](../../labels/benchmark.md)


## [When to Stop? Towards Efficient Code Generation in LLMs with Excess Token Prevention](paper_12.md)
- **Authors**: Guo, Lianghong and Wang, Yanlin and Shi, Ensheng and Zhong, Wanjun and Zhang, Hongyu and Chen, Jiachi and Zhang, Ruikai and Ma, Yuchi and Zheng, Zibin
- **Abstract**: Code generation aims to automatically generate code snippets that meet given natural language requirements and plays an important role in software development. Although Code LLMs have shown excellent performance in this domain, their long generation time poses a signification limitation in practice use. In this paper, we first conduct an in-depth preliminary study with different Code LLMs on code generation task and identify a significant efficiency issue, i.e., continual generation of excess to...
- **Link**: [Read Paper](https://doi.org/10.1145/3650212.3680343)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)
