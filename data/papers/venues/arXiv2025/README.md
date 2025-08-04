# arXiv2025

Number of papers: 27

## [AI Software Engineer: Programming with Trust](paper_21.md)
- **Authors**: Abhik Roychoudhury, Corina Pasareanu, Michael Pradel, Baishakhi Ray
- **Abstract**: Large Language Models (LLMs) have shown surprising proficiency in generating code snippets, promising to automate large parts of software engineering via artificial intelligence (AI). We argue that successfully deploying AI software engineers requires a level of trust equal to or even greater than the trust established by human-driven software engineering practices. The recent trend toward LLM agents offers a path toward integrating the power of LLMs to create new code with the power of analysis...
- **Link**: [Read Paper](https://arxiv.org/pdf/2502.13767)
- **Labels**: [code generation](../../labels/code_generation.md), [survey](../../labels/survey.md)


## [Are “Solved Issues” in SWE-bench Really Solved Correctly?](paper_15.md)
- **Authors**: You Wang, Michael Pradel, Zhongxin Liu
- **Abstract**: Automated issue solving aims to resolve real-world issues in software repositories. The most popular benchmarks for automated issue solving are SWE-bench and its human-filtered subset SWE-bench Verified. These benchmarks leverage testing to validate generated patches. However, because testing is rarely exhaustive, a patch may pass the tests but nevertheless fail to match the developers' expectations. Unfortunately, it is currently unclear to what extent evaluations performed with SWE-bench suffe...
- **Link**: [Read Paper](https://arxiv.org/abs/2503.15223)
- **Labels**: [benchmark](../../labels/benchmark.md), [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [Automated Static Vulnerability Detection via a Holistic Neuro-symbolic Approach](paper_16.md)
- **Authors**: Penghui Li, Songchen Yao, Josef Sarfati Korich, Changhua Luo, Jianjia Yu, Yinzhi Cao, Junfeng Yang
- **Abstract**: Static vulnerability detection is still a challenging problem and demands excessive human efforts, e.g., manual curation of good vulnerability patterns. None of prior works, including classic program analysis or Large Language Model (LLM)-based approaches, have fully automated such vulnerability pattern generations with reasonable detection accuracy. In this paper, we design and implement, MoCQ, a novel holistic neuro-symbolic framework that combines the complementary strengths of LLMs and class...
- **Link**: [Read Paper](https://arxiv.org/abs/2504.16057)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [BountyBench: Dollar Impact of AI Agent Attackers and Defenders on Real-World Cybersecurity Systems](paper_20.md)
- **Authors**: Andy K. Zhang, Joey Ji, Celeste Menders, Riya Dulepet, Thomas Qin, Ron Y. Wang, Junrong Wu, Kyleen Liao, Jiliang Li, Jinghan Hu, Sara Hong, Nardos Demilew, Shivatmica Murgai, Jason Tran, Nishka Kacheria, Ethan Ho, Denis Liu, Lauren McLane, Olivia Bruvik, Dai-Rong Han, Seungwoo Kim, Akhil Vyas, Cuiyuanxiu Chen, Ryan Li, Weiran Xu, Jonathan Z. Ye, Prerit Choudhary, Siddharth M. Bhatia, Vikram Sivashankar, Yuxuan Bao, Dawn Song, Dan Boneh, Daniel E. Ho, Percy Liang
- **Abstract**: AI agents have the potential to significantly alter the cybersecurity landscape. To help us understand this change, we introduce the first framework to capture offensive and defensive cyber-capabilities in evolving real-world systems. Instantiating this framework with BountyBench, we set up 25 systems with complex, real-world codebases. To capture the vulnerability lifecycle, we define three task types: Detect (detecting a new vulnerability), Exploit (exploiting a specific vulnerability), and Pa...
- **Link**: [Read Paper](https://arxiv.org/abs/2505.15216)
- **Labels**: [program testing](../../labels/program_testing.md), [vulnerability exploitation](../../labels/vulnerability_exploitation.md), [benchmark](../../labels/benchmark.md)


## [C2SaferRust: Transforming C Projects into Safer Rust with NeuroSymbolic Techniques](paper_25.md)
- **Authors**: Vikram Nitin, Rahul Krishna, Luiz Lemos do Valle, Baishakhi Ray
- **Abstract**: In recent years, there has been a lot of interest in converting C code to Rust, to benefit from the memory and thread safety guarantees of Rust. C2Rust is a rule-based system that can automatically convert C code to functionally identical Rust, but the Rust code that it produces is non-idiomatic, i.e., makes extensive use of unsafe Rust, a subset of the language that doesn't have memory or thread safety guarantees. At the other end of the spectrum are LLMs, which produce idiomatic Rust code, but...
- **Link**: [Read Paper](https://arxiv.org/pdf/2501.14257)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [CRUST-Bench: A Comprehensive Benchmark for C-to-safe-Rust Transpilation](paper_6.md)
- **Authors**: Anirudh Khatry, Robert Zhang, Jia Pan, Ziteng Wang, Qiaochu Chen, Greg Durrett, Isil Dillig
- **Abstract**: C-to-Rust transpilation is essential for modernizing legacy C code while enhancing safety and interoperability with modern Rust ecosystems. However, no dataset currently exists for evaluating whether a system can transpile C into safe Rust that passes a set of test cases. We introduce CRUST-Bench, a dataset of 100 C repositories, each paired with manually-written interfaces in safe Rust as well as test cases that can be used to validate correctness of the transpilation. By considering entire rep...
- **Link**: [Read Paper](https://arxiv.org/abs/2504.15254)
- **Labels**: [benchmark](../../labels/benchmark.md), [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [Can LLMs Reason About Program Semantics? A Comprehensive Evaluation of LLMs on Formal Specification Inference](paper_11.md)
- **Authors**: Thanh Le-Cong, Bach Le, Toby Murray
- **Abstract**: Large Language Models (LLMs) are increasingly being used to automate programming tasks. Yet, LLMs' capabilities in reasoning about program semantics are still inadequately studied, leaving significant potential for further exploration. This paper introduces FormalBench, a comprehensive benchmark designed to evaluate LLMs' reasoning abilities on program semantics, particularly via the task of synthesizing formal program specifications to assist verifying program correctness. This task requires bo...
- **Link**: [Read Paper](https://arxiv.org/abs/2503.04779)
- **Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md), [benchmark](../../labels/benchmark.md), [empirical study](../../labels/empirical_study.md)


## [ClassInvGen: Class Invariant Synthesis using Large Language Models](paper_14.md)
- **Authors**: Chuyue Sun, Viraj Agashe, Saikat Chakraborty, Jubi Taneja, Clark Barrett, David Dill, Xiaokang Qiu, Shuvendu K. Lahiri
- **Abstract**: Formal program specifications in the form of preconditions, postconditions, and class invariants have several benefits for the construction and maintenance of programs. They not only aid in program understanding due to their unambiguous semantics but can also be enforced dynamically (or even statically when the language supports a formal verifier). However, synthesizing high-quality specifications in an underlying programming language is limited by the expressivity of the specifications or the n...
- **Link**: [Read Paper](https://www.arxiv.org/abs/2502.18917)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


## [Combining Large Language Models with Static Analyzers for Code Review Generation](paper_13.md)
- **Authors**: Rohit Gheyi, Marcio Ribeiro, Jonhnanthan Oliveira
- **Abstract**: Code review is a crucial but often complex, subjective, and time-consuming activity in software development. Over the past decades, significant efforts have been made to automate this process. Early approaches focused on knowledge-based systems (KBS) that apply rule-based mechanisms to detect code issues, providing precise feedback but struggling with complex, context-dependent cases. More recent work has shifted toward fine-tuning pre-trained language models for code review, enabling broader is...
- **Link**: [Read Paper](https://arxiv.org/pdf/2502.06633)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [CyberGym: Evaluating AI Agents' Cybersecurity Capabilities with Real-World Vulnerabilities at Scale](paper_19.md)
- **Authors**: Zhun Wang, Tianneng Shi, Jingxuan He, Matthew Cai, Jialin Zhang, Dawn Song
- **Abstract**: Large language model (LLM) agents are becoming increasingly skilled at handling cybersecurity tasks autonomously. Thoroughly assessing their cybersecurity capabilities is critical and urgent, given the high stakes in this domain. However, existing benchmarks fall short, often failing to capture real-world scenarios or being limited in scope. To address this gap, we introduce CyberGym, a large-scale and high-quality cybersecurity evaluation framework featuring 1,507 real-world vulnerabilities fou...
- **Link**: [Read Paper](https://arxiv.org/abs/2506.02548)
- **Labels**: [program testing](../../labels/program_testing.md), [vulnerability exploitation](../../labels/vulnerability_exploitation.md), [benchmark](../../labels/benchmark.md)


## [Evaluating the Effectiveness of Small Language Models in Detecting Refactoring Bugs](paper_12.md)
- **Authors**: Rohit Gheyi, Marcio Ribeiro, Jonhnanthan Oliveira
- **Abstract**: Popular IDEs frequently contain bugs in their refactoring implementations. Ensuring that a transformation preserves a program's behavior is a complex task. Traditional detection methods rely on predefined preconditions for each refactoring type, limiting their scalability and adaptability to new transformations. These methods often require extensive static and dynamic analyses, which are computationally expensive, time-consuming, and may still fail to detect certain refactoring bugs. This study ...
- **Link**: [Read Paper](https://arxiv.org/abs/2502.18454)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Fixing 7,400 Bugs for 1$: Cheap Crash-Site Program Repair](paper_17.md)
- **Authors**: Han Zheng, Ilia Shumailov, Tianqi Fan, Aiden Hall, Mathias Payer
- **Abstract**: The rapid advancement of bug-finding techniques has led to the discovery of more vulnerabilities than developers can reasonably fix, creating an urgent need for effective Automated Program Repair (APR) methods. However, the complexity of modern bugs often makes precise root cause analysis difficult and unreliable. To address this challenge, we propose crash-site repair to simplify the repair task while still mitigating the risk of exploitation. In addition, we introduce a template-guided patch g...
- **Link**: [Read Paper](https://arxiv.org/abs/2505.13103)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [From System 1 to System 2: A Survey of Reasoning Large Language Models](paper_22.md)
- **Authors**: Zhong-Zhi Li, Duzhen Zhang, Ming-Liang Zhang, Jiaxin Zhang, Zengyan Liu, Yuxuan Yao, Haotian Xu, Junhao Zheng, Pei-Jie Wang, Xiuyi Chen, Yingying Zhang, Fei Yin, Jiahua Dong, Zhiwei Li, Bao-Long Bi, Ling-Rui Mei, Junfeng Fang, Zhijiang Guo, Le Song, Cheng-Lin Liu
- **Abstract**: Achieving human-level intelligence requires refining the transition from the fast, intuitive System 1 to the slower, more deliberate System 2 reasoning. While System 1 excels in quick, heuristic decisions, System 2 relies on logical reasoning for more accurate judgments and reduced biases. Foundational Large Language Models (LLMs) excel at fast decision-making but lack the depth for complex reasoning, as they have not yet fully embraced the step-by-step analysis characteristic of true System 2 t...
- **Link**: [Read Paper](https://arxiv.org/abs/2502.17419)
- **Labels**: [agent design](../../labels/agent_design.md), [hallucination in reasoning](../../labels/hallucination_in_reasoning.md), [survey](../../labels/survey.md)


## [Hierarchical Repository-Level Code Summarization for Business Applications Using Local LLMs](paper_24.md)
- **Authors**: Nilesh Dhulshette, Sapan Shah, Vinay Kulkarni
- **Abstract**: In large-scale software development, understanding the functionality and intent behind complex codebases is critical for effective development and maintenance. While code summarization has been widely studied, existing methods primarily focus on smaller code units, such as functions, and struggle with larger code artifacts like files and packages. Additionally, current summarization models tend to emphasize low-level implementation details, often overlooking the domain and business context that ...
- **Link**: [Read Paper](https://arxiv.org/pdf/2501.07857)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md), [agent design](../../labels/agent_design.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)


## [Interactive Tools Substantially Assist LM Agents in Finding Security Vulnerabilities](paper_18.md)
- **Authors**: Talor Abramovich, Meet Udeshi, Minghao Shao, Kilian Lieret, Haoran Xi, Kimberly Milner, Sofija Jancheska, John Yang, Carlos E. Jimenez, Farshad Khorrami, Prashanth Krishnamurthy, Brendan Dolan-Gavitt, Muhammad Shafique, Karthik Narasimhan, Ramesh Karri, Ofir Press
- **Abstract**: Although language model (LM) agents have demonstrated increased performance in multiple domains, including coding and web-browsing, their success in cybersecurity has been limited. We present EnIGMA, an LM agent for autonomously solving Capture The Flag (CTF) challenges. We introduce new tools and interfaces to improve the agent's ability to find and exploit security vulnerabilities, focusing on interactive terminal programs. These novel Interactive Agent Tools enable LM agents, for the first ti...
- **Link**: [Read Paper](https://arxiv.org/abs/2409.16165)
- **Labels**: [program testing](../../labels/program_testing.md), [vulnerability exploitation](../../labels/vulnerability_exploitation.md), [benchmark](../../labels/benchmark.md)


## [Is Your Benchmark (Still) Useful? Dynamic Benchmarking for Code Language Models](paper_9.md)
- **Authors**: Batu Guan, Xiao Wu, Yuanyuan Yuan, Shaohua Li
- **Abstract**: In this paper, we tackle a critical challenge in model evaluation: how to keep code benchmarks useful when models might have already seen them during training. We introduce a novel solution, dynamic benchmarking framework, to address this challenge. Given a code understanding or reasoning benchmark, our framework dynamically transforms each input, i.e., programs, with various semantic-preserving mutations to build a syntactically new while semantically identical benchmark. We evaluated ten popul...
- **Link**: [Read Paper](https://arxiv.org/abs/2503.06643)
- **Labels**: [benchmark](../../labels/benchmark.md)


## [KNighter: Transforming Static Analysis with LLM-Synthesized Checkers](paper_10.md)
- **Authors**: Chenyuan Yang, Zijie Zhao, Zichen Xie, Haoyu Li, Lingming Zhang
- **Abstract**: Static analysis is a powerful technique for bug detection in critical systems like operating system kernels. However, designing and implementing static analyzers is challenging, timeconsuming, and typically limited to predefined bug patterns. While large language models (LLMs) have shown promise for static analysis, directly applying them to scan large codebases remains impractical due to computational constraints and contextual limitations. We present KNighter, the first approach that unlocks p...
- **Link**: [Read Paper](https://arxiv.org/pdf/2503.09002)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [LAMD: Context-driven Android Malware Detection and Classification with LLMs](paper_4.md)
- **Authors**: Xingzhi Qian, Xinran Zheng, Yiling He, Shuo Yang, Lorenzo Cavallaro
- **Abstract**: The rapid growth of mobile applications has escalated Android malware threats. Although there are numerous detection methods, they often struggle with evolving attacks, dataset biases, and limited explainability. Large Language Models (LLMs) offer a promising alternative with their zero-shot inference and reasoning capabilities. However, applying LLMs to Android malware detection presents two key challenges: (1)the extensive support code in Android applications, often spanning thousands of class...
- **Link**: [Read Paper](https://www.arxiv.org/pdf/2502.13055)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [LLM-Based Repair of Static Nullability Errors](paper_26.md)
- **Authors**: Karimipour, Nima and Pradel, Michael and Kellogg, Martin and Sridharan, Manu
- **Abstract**: Modern Java projects increasingly adopt static analysis tools that prevent null-pointer exceptions by treating nullness as a type property. However, integrating such tools into large, existing codebases remains a significant challenge. While annotation inference can eliminate many errors automatically, a subset of residual errors -- typically a mix of real bugs and false positives -- often persist and can only be resolved via code changes. Manually addressing these errors is tedious and error-pr...
- **Link**: [Read Paper](https://arxiv.org/pdf/2507.20674)
- **Labels**: [program repair](../../labels/program_repair.md)


## [Language Models for Code Optimization: Survey, Challenges and Future Directions](paper_5.md)
- **Authors**: Jingzhi Gong, Vardan Voskanyan, Paul Brookes, Fan Wu, Wei Jie, Jie Xu, Rafail Giavrimis, Mike Basios, Leslie Kanthan, Zheng Wang
- **Abstract**: Language models (LMs) built upon deep neural networks (DNNs) have recently demonstrated breakthrough effectiveness in software engineering tasks such as code generation, completion, and repair. This has paved the way for the emergence of LM-based code optimization techniques, which are crucial for enhancing the performance of existing programs, such as accelerating program execution time. However, a comprehensive survey dedicated to this specific application has been lacking. To fill this gap, w...
- **Link**: [Read Paper](https://arxiv.org/abs/2501.01277)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program optimization](../../labels/program_optimization.md), [survey](../../labels/survey.md)


## [Large Language Model powered Symbolic Execution](paper_23.md)
- **Authors**: Yihe Li, Ruijie Meng, Gregory J. Duck
- **Abstract**: Large Language Models (LLMs) have emerged as a promising alternative to traditional static program analysis methods, such as symbolic execution, offering the ability to reason over code directly without relying on theorem provers or SMT solvers. However, LLMs are also inherently probabilistic by nature, and therefore face significant challenges in relation to the accuracy and scale of the analysis in real-world application. Such issues often necessitate the use of larger LLMs with higher token l...
- **Link**: [Read Paper](https://arxiv.org/pdf/2505.13452)
- **Labels**: [static analysis](../../labels/static_analysis.md), [symbolic execution](../../labels/symbolic_execution.md)


## [Minimizing False Positives in Static Bug Detection via LLM-Enhanced Path Feasibility Analysis](paper_8.md)
- **Authors**: Xueying Du, Kai Yu, Chong Wang, Yi Zou, Wentai Deng, Zuoyu Ou, Xin Peng, Lingming Zhang, Yiling Lou
- **Abstract**: Static bug analyzers play a crucial role in ensuring software quality. However, existing analyzers for bug detection in large codebases often suffer from high false positive rates. This is primarily due to the limited capabilities of analyzers in path feasibility validation with multiple conditional branches and complex data dependencies. While current LLM-based approaches attempt to address this issue, their effectiveness remains limited due to insufficient constraint cascade analysis and scala...
- **Link**: [Read Paper](https://arxiv.org/abs/2506.10322)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [PoCGen: Generating Proof-of-Concept Exploits for Vulnerabilities in Npm Packages](paper_27.md)
- **Authors**: Simsek, Deniz and Eghbali, Aryaz and Pradel, Michael
- **Abstract**: Security vulnerabilities in software packages are a significant concern for developers and users alike. Patching these vulnerabilities in a timely manner is crucial to restoring the integrity and security of software systems. However, previous work has shown that vulnerability reports often lack proof-of-concept (PoC) exploits, which are essential for fixing the vulnerability, testing patches, and avoiding regressions. Creating a PoC exploit is challenging because vulnerability reports are infor...
- **Link**: [Read Paper](https://arxiv.org/pdf/2506.04962)
- **Labels**: [vulnerability exploitation](../../labels/vulnerability_exploitation.md)


## [Prompting Large Language Models to Tackle the Full Software Development Lifecycle: A Case Study](paper_1.md)
- **Authors**: Bowen Li, Wenhan Wu, Ziwei Tang, Lin Shi, John Yang, Jinyang Li, Shunyu Yao, Chen Qian, Binyuan Hui, Qicheng Zhang, Zhiyin Yu, He Du, Ping Yang, Dahua Lin, Chao Peng, Kai Chen
- **Abstract**: Recent advancements in large language models (LLMs) have significantly enhanced their coding capabilities. However, existing benchmarks predominantly focused on simplified or isolated aspects of coding, such as single-file code generation or repository issue debugging, falling short of measuring the full spectrum of challenges raised by real-world programming activities. In this case study, we explore the performance of LLMs across the entire software development lifecycle with DevEval, encompas...
- **Link**: [Read Paper](https://arxiv.org/abs/2403.08604)
- **Labels**: [benchmark](../../labels/benchmark.md)


## [SecVulEval: Benchmarking LLMs for Real-World C/C++ Vulnerability Detection](paper_2.md)
- **Authors**: Md Basim Uddin Ahmed, Nima Shiri Harzevili, Jiho Shin, Hung Viet Pham, Song Wang
- **Abstract**: Large Language Models (LLMs) have shown promise in software engineering tasks, but evaluating their effectiveness in vulnerability detection is challenging due to the lack of high-quality datasets. Most existing datasets are limited to function-level labels, ignoring finer-grained vulnerability patterns and crucial contextual information. Also, poor data quality such as mislabeling, inconsistent annotations, and duplicates can lead to inflated performance and weak generalization. Moreover, by in...
- **Link**: [Read Paper](https://arxiv.org/abs/2505.19828)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)


## [The Hitchhiker's Guide to Program Analysis, Part II: Deep Thoughts by LLMs](paper_3.md)
- **Authors**: Haonan Li, Hang Zhang, Kexin Pei, Zhiyun Qian
- **Abstract**: Static analysis is a cornerstone for software vulnerability detection, yet it often struggles with the classic precision-scalability trade-off. In practice, such tools often produce high false positive rates, particularly in large codebases like the Linux kernel. This imprecision can arise from simplified vulnerability modeling and over-approximation of path and data constraints. While large language models (LLMs) show promise in code understanding, their naive application to program analysis yi...
- **Link**: [Read Paper](https://arxiv.org/abs/2504.11711)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Training Language Models to Generate Quality Code with Program Analysis Feedback](paper_7.md)
- **Authors**: Feng Yao, Zilong Wang, Liyuan Liu, Junxia Cui, Li Zhong, Xiaohan Fu, Haohui Mai, Vish Krishnan, Jianfeng Gao, Jingbo Shang
- **Abstract**: Code generation with large language models (LLMs), often termed vibe coding, is increasingly adopted in production but fails to ensure code quality, particularly in security (e.g., SQL injection vulnerabilities) and maintainability (e.g., missing type annotations). Existing methods, such as supervised fine-tuning and rule-based post-processing, rely on labor-intensive annotations or brittle heuristics, limiting their scalability and effectiveness. We propose REAL, a reinforcement learning framew...
- **Link**: [Read Paper](https://arxiv.org/abs/2505.22704)
- **Labels**: [code generation](../../labels/code_generation.md), [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md)
