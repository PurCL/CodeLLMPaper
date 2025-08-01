# arXiv2024

Number of papers: 39

## [A Comprehensive Study of the Capabilities of Large Language Models for Vulnerability Detection](paper_16.md)
- **Authors**: Benjamin Steenhoek and Md Mahbubur Rahman and Monoshi Kumar Roy and Mirza Sanjida Alam and Earl T. Barr and Wei Le
- **Abstract**: Large Language Models (LLMs) have demonstrated great potential for code generation and other software engineering tasks. Vulnerability detection is of crucial importance to maintaining the security, integrity, and trustworthiness of software systems. Precise vulnerability detection requires reasoning about the code, making it a good case study for exploring the limits of LLMs' reasoning capabilities. Although recent work has applied LLMs to vulnerability detection using generic prompting techniq...
- **Link**: [Read Paper](https://doi.org/10.48550/arXiv.2403.17218)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


## [A Survey on Large Language Models for Code Generation](paper_10.md)
- **Authors**: Jiang, Juyong and Wang, Fan and Shen, Jiasi and Kim, Sungju and Kim, Sunghun
- **Abstract**: Large Language Models (LLMs) have garnered remarkable advancements across diverse code-related tasks, known as Code LLMs, particularly in code generation that generates source code with LLM from natural language descriptions. This burgeoning field has captured significant interest from both academic researchers and industry professionals due to its practical significance in software development, e.g., GitHub Copilot. Despite the active exploration of LLMs for a variety of code tasks, either from...
- **Link**: [Read Paper](https://arxiv.org/pdf/2406.00515)
- **Labels**: [survey](../../labels/survey.md), [code generation](../../labels/code_generation.md)


## [An Empirical Study of Large Language Models for Type and Call Graph Analysis](paper_2.md)
- **Authors**: Ashwin Prasad Shivarpatna Venkatesh, Rose Sunil, Samkutty Sabu, Amir M. Mir, Sofia Reis, Eric Bodden
- **Abstract**: Large Language Models (LLMs) are increasingly being explored for their potential in software engineering, particularly in static analysis tasks. In this study, we investigate the potential of current LLMs to enhance call-graph analysis and type inference for Python and JavaScript programs. We empirically evaluated 24 LLMs, including OpenAI's GPT series and open-source models like LLaMA and Mistral, using existing and newly developed benchmarks. Specifically, we enhanced TypeEvalPy, a micro-bench...
- **Link**: [Read Paper](https://arxiv.org/abs/2410.00603)
- **Labels**: [static analysis](../../labels/static_analysis.md), [type inference](../../labels/type_inference.md), [call graph analysis](../../labels/call_graph_analysis.md)


## [Automatic Programming: Large Language Models and Beyond](paper_12.md)
- **Authors**: Lyu, Michael R and Ray, Baishakhi and Roychoudhury, Abhik and Tan, Shin Hwei and Thongtanunam, Patanamon
- **Abstract**: Automatic programming has seen increasing popularity due to the emergence of tools like GitHub Copilot which rely on Large Language Models (LLMs). At the same time, automatically generated code faces challenges during deployment due to concerns around quality and trust. In this article, we study automated coding in a general sense and study the concerns around code quality, security and related issues of programmer responsibility. These are key issues for organizations while deciding on the usag...
- **Link**: [Read Paper](https://arxiv.org/pdf/2405.02213)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [empirical study](../../labels/empirical_study.md)


## [CodeBenchGen: Creating Scalable Execution-based Code Generation Benchmarks](paper_9.md)
- **Authors**: Xie, Yiqing and Xie, Alex and Sheth, Divyanshu and Liu, Pengfei and Fried, Daniel and Rose, Carolyn
- **Abstract**: To facilitate evaluation of code generation systems across diverse scenarios, we present CodeBenchGen, a framework to create scalable execution-based benchmarks that only requires light guidance from humans. Specifically, we leverage a large language model (LLM) to convert an arbitrary piece of code into an evaluation example, including test cases for execution-based evaluation. We illustrate the usefulness of our framework by creating a dataset, Exec-CSN, which includes 1,931 examples involving...
- **Link**: [Read Paper](https://arxiv.org/pdf/2404.00566)
- **Labels**: [code generation](../../labels/code_generation.md), [benchmark](../../labels/benchmark.md)


## [Codemind: A framework to challenge large language models for code reasoning](paper_6.md)
- **Authors**: Liu, Changshu and Zhang, Shizhuo Dylan and Ibrahimzada, Ali Reza and Jabbarvand, Reyhaneh
- **Abstract**: Solely relying on test passing to evaluate Large Language Models (LLMs) for code synthesis may result in unfair assessment or promoting models with data leakage. As an alternative, we introduce CodeMind, a framework designed to gauge the code reasoning abilities of LLMs. CodeMind currently supports three code reasoning tasks: Independent Execution Reasoning (IER), Dependent Execution Reasoning (DER), and Specification Reasoning (SR). The first two evaluate models to predict the execution output ...
- **Link**: [Read Paper](https://arxiv.org/pdf/2402.09664)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [empirical study](../../labels/empirical_study.md)


## [Constrained Decoding for Secure Code Generation](paper_7.md)
- **Authors**: Fu, Yanjun and Baker, Ethan and Ding, Yu and Chen, Yizheng
- **Abstract**: Code Large Language Models (Code LLMs) have been increasingly used by developers to boost productivity, but they often generate vulnerable code. Thus, there is an urgent need to ensure that code generated by Code LLMs is correct and secure. Previous research has primarily focused on generating secure code, overlooking the fact that secure code also needs to be correct. This oversight can lead to a false sense of security. Currently, the community lacks a method to measure actual progress in this...
- **Link**: [Read Paper](https://arxiv.org/pdf/2405.00218)
- **Labels**: [code generation](../../labels/code_generation.md), [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md)


## [Context-aware Code Segmentation for C-to-Rust Translation using Large Language Models](paper_35.md)
- **Authors**: Momoko Shiraishi and Takahiro Shinagawa
- **Abstract**: There is strong motivation to translate C code into Rust code due to the continuing threat of memory safety vulnerabilities in existing C programs and the significant attention paid to Rust as an alternative to the C language. While large language models (LLMs) show promise for automating this translation by generating more natural and safer code than rule-based methods, previous studies have shown that LLM-generated Rust code often fails to compile, even for relatively small C programs, due to ...
- **Link**: [Read Paper](https://arxiv.org/abs/2409.10506v1)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models](paper_31.md)
- **Authors**: Zhang, Andy K and Perry, Neil and Dulepet, Riya and Ji, Joey and Lin, Justin W and Jones, Eliot and Menders, Celeste and Hussein, Gashon and Liu, Samantha and Jasper, Donovan and others
- **Abstract**: Language Model (LM) agents for cybersecurity that are capable of autonomously identifying vulnerabilities and executing exploits have the potential to cause real-world impact. Policymakers, model providers, and other researchers in the AI and cybersecurity communities are interested in quantifying the capabilities of such agents to help mitigate cyberrisk and investigate opportunities for penetration testing. Toward that end, we introduce Cybench, a framework for specifying cybersecurity tasks a...
- **Link**: [Read Paper](https://arxiv.org/abs/2408.08926)
- **Labels**: [program testing](../../labels/program_testing.md), [vulnerability exploitation](../../labels/vulnerability_exploitation.md), [benchmark](../../labels/benchmark.md)


## [DiffSpec: Differential Testing with LLMs using Natural Language Specifications and Code Artifacts](paper_23.md)
- **Authors**: Nikitha Rao, Elizabeth Gilbert, Tahina Ramananandro, Nikhil Swamy, Claire Le Goues, Sarah Fakhoury
- **Abstract**: Differential testing can be an effective way to find bugs in software systems with multiple implementations that conform to the same specification, like compilers, network protocol parsers, and language runtimes. Specifications for such systems are often standardized in natural language documents, like Instruction Set Architecture (ISA) specifications, Wasm specifications or IETF RFC's. Large Language Models (LLMs) have demonstrated potential in both generating tests and handling large volumes o...
- **Link**: [Read Paper](https://arxiv.org/abs/2410.04249)
- **Labels**: [program testing](../../labels/program_testing.md), [differential testing](../../labels/differential_testing.md), [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)


## [Enabling Memory Safety of C Programs using LLMs](paper_14.md)
- **Authors**: Mohammed, Nausheen and Lal, Akash and Rastogi, Aseem and Roy, Subhajit and Sharma, Rahul
- **Abstract**: Memory safety violations in low-level code, written in languages like C, continues to remain one of the major sources of software vulnerabilities. One method of removing such violations by construction is to port C code to a safe C dialect. Such dialects rely on programmer-supplied annotations to guarantee safety with minimal runtime overhead. This porting, however, is a manual process that imposes significant burden on the programmer and, hence, there has been limited adoption of this technique...
- **Link**: [Read Paper](https://arxiv.org/pdf/2404.01096.pdf)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [Enhancing Automated Loop Invariant Generation for Complex Programs with Large Language Models](paper_24.md)
- **Authors**: Ruibang Liu, Guoqiang Li, Minyu Chen, Ling-I Wu, Jingyu Ke
- **Abstract**: Automated program verification has always been an important component of building trustworthy software. While the analysis of real-world programs remains a theoretical challenge, the automation of loop invariant analysis has effectively resolved the problem. However, real-world programs that often mix complex data structures and control flows pose challenges to traditional loop invariant generation tools. To enhance the applicability of invariant generation techniques, we proposed ACInv, an Auto...
- **Link**: [Read Paper](https://arxiv.org/pdf/2412.10483)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


## [EvoCodeBench: An Evolving Code Generation Benchmark Aligned with Real-World Code Repositories](paper_8.md)
- **Authors**: Li, Jia and Li, Ge and Zhang, Xuanming and Dong, Yihong and Jin, Zhi
- **Abstract**: How to evaluate Large Language Models (LLMs) in code generation is an open question. Existing benchmarks demonstrate poor alignment with real-world code repositories and are insufficient to evaluate the coding abilities of LLMs. This paper proposes a new benchmark - EvoCodeBench to address the preceding problems, which has three primary advances. (1) EvoCodeBench aligns with real-world repositories in multiple dimensions, e.g., code distributions and dependency distributions. (2) EvoCodeBench of...
- **Link**: [Read Paper](https://arxiv.org/pdf/2404.00599)
- **Labels**: [benchmark](../../labels/benchmark.md), [code generation](../../labels/code_generation.md)


## [Formal Mathematical Reasoning: A New Frontier in AI](paper_27.md)
- **Authors**: Kaiyu Yang, Gabriel Poesia, Jingxuan He, Wenda Li, Kristin Lauter, Swarat Chaudhuri, Dawn Song
- **Abstract**: AI for Mathematics (AI4Math) is not only intriguing intellectually but also crucial for AI-driven discovery in science, engineering, and beyond. Extensive efforts on AI4Math have mirrored techniques in NLP, in particular, training large language models on carefully curated math datasets in text form. As a complementary yet less explored avenue, formal mathematical reasoning is grounded in formal systems such as proof assistants, which can verify the correctness of reasoning and provide automatic...
- **Link**: [Read Paper](https://arxiv.org/pdf/2412.16075)
- **Labels**: [hallucination in reasoning](../../labels/hallucination_in_reasoning.md), [survey](../../labels/survey.md)


## [If llm is the wizard, then code is the wand: A survey on how code empowers large language models to serve as intelligent agents](paper_33.md)
- **Authors**: Yang, Ke and Liu, Jiateng and Wu, John and Yang, Chaoqi and Fung, Yi R and Li, Sha and Huang, Zixuan and Cao, Xu and Wang, Xingyao and Wang, Yiquan and others
- **Abstract**: The prominent large language models (LLMs) of today differ from past language models not only in size, but also in the fact that they are trained on a combination of natural language and formal language (code). As a medium between humans and computers, code translates high-level goals into executable steps, featuring standard syntax, logical consistency, abstraction, and modularity. In this survey, we present an overview of the various benefits of integrating code into LLMs' training data. Speci...
- **Link**: [Read Paper](https://arxiv.org/pdf/2401.00812.pdf)
- **Labels**: [survey](../../labels/survey.md), [agent design](../../labels/agent_design.md), [reason with code](../../labels/reason_with_code.md)


## [KernelGPT: Enhanced Kernel Fuzzing via Large Language Models](paper_39.md)
- **Authors**: Chenyuan Yang, Zijie Zhao and Lingming Zhang
- **Abstract**: Bugs in operating system kernels can affect billions of devices and users all over the world. As a result, a large body of research has been focused on kernel fuzzing, i.e., automatically generating syscall (system call) sequences to detect potential kernel bugs or vulnerabilities. Kernel fuzzing aims to generate valid syscall sequences guided by syscall specifications that define both the syntax and semantics of syscalls. While there has been existing work trying to automate syscall specificati...
- **Link**: [Read Paper](https://arxiv.org/pdf/2401.00563)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


## [LLM-Assisted Static Analysis for Detecting Security Vulnerabilities](paper_21.md)
- **Authors**: Li, Ziyang and Dutta, Saikat and Naik, Mayur
- **Abstract**: Software is prone to security vulnerabilities. Program analysis tools to detect them have limited effectiveness in practice due to their reliance on human labeled specifications. Large language models (or LLMs) have shown impressive code generation capabilities but they cannot do complex reasoning over code to detect such vulnerabilities especially since this task requires whole-repository analysis. We propose IRIS, a neuro-symbolic approach that systematically combines LLMs with static analysis...
- **Link**: [Read Paper](https://arxiv.org/abs/2405.17238)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [LLM4Vuln: {A} Unified Evaluation Framework for Decoupling and Enhancing LLMs' Vulnerability Reasoning](paper_19.md)
- **Authors**: Yuqiang Sun and Daoyuan Wu and Yue Xue and Han Liu and Wei Ma and Lyuye Zhang and Miaolei Shi and Yang Liu
- **Abstract**: Large language models (LLMs) have demonstrated significant potential in various tasks, including vulnerability detection. However, current efforts in this area are preliminary, lacking clarity on whether LLMs' vulnerability reasoning capabilities stem from the models themselves or external aids such as knowledge retrieval and tooling support.This paper aims to isolate LLMs' vulnerability reasoning from other capabilities, such as vulnerability knowledge adoption, context information retrieval, a...
- **Link**: [Read Paper](https://doi.org/10.48550/arXiv.2401.16185)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)


## [LLMorpheus: Mutation Testing using Large Language Models](paper_29.md)
- **Authors**: Tip, Frank and Bell, Jonathan and Sch{\"a}fer, Max
- **Abstract**: In mutation testing, the quality of a test suite is evaluated by introducing faults into a program and determining whether the program's tests detect them. Most existing approaches for mutation testing involve the application of a fixed set of mutation operators, e.g., replacing a "+" with a "-" or removing a function's body. However, certain types of real-world bugs cannot easily be simulated by such approaches, limiting their effectiveness. This paper presents a technique where a Large Languag...
- **Link**: [Read Paper](https://arxiv.org/pdf/2404.09952)
- **Labels**: [program testing](../../labels/program_testing.md), [mutation testing](../../labels/mutation_testing.md)


## [Large Language Model assisted Hybrid Fuzzing](paper_5.md)
- **Authors**: Ruijie Meng, Gregory J. Duck, Abhik Roychoudhury
- **Abstract**: Greybox fuzzing is one of the most popular methods for detecting software vulnerabilities, which conducts a biased random search within the program input space. To enhance its effectiveness in achieving deep coverage of program behaviors, greybox fuzzing is often combined with concolic execution, which performs a path-sensitive search over the domain of program inputs. In hybrid fuzzing, conventional greybox fuzzing is followed by concolic execution in an iterative loop, where reachability roadb...
- **Link**: [Read Paper](https://doi.org/10.48550/arXiv.2412.15931)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


## [Large Language Models Based Fuzzing Techniques: A Survey](paper_38.md)
- **Authors**: Misu, Md Rakib Hossain and Lopes, Cristina V. and Ma, Iris and Noble, James
- **Abstract**: In the modern era where software plays a pivotal role, software security and vulnerability analysis have become essential for software development. Fuzzing test, as an efficient software testing method, are widely used in various domains. Moreover, the rapid development of Large Language Models (LLMs) has facilitated their application in the field of software testing, demonstrating remarkable performance. Considering existing fuzzing test techniques are not entirely automated and software vulner...
- **Link**: [Read Paper](https://arxiv.org/pdf/2402.00350)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [survey](../../labels/survey.md)


## [Large language model-based agents for software engineering: A survey](paper_32.md)
- **Authors**: Liu, Junwei and Wang, Kaixin and Chen, Yixuan and Peng, Xin and Chen, Zhenpeng and Zhang, Lingming and Lou, Yiling
- **Abstract**: The recent advance in Large Language Models (LLMs) has shaped a new paradigm of AI agents, i.e., LLM-based agents. Compared to standalone LLMs, LLM-based agents substantially extend the versatility and expertise of LLMs by enhancing LLMs with the capabilities of perceiving and utilizing external resources and tools. To date, LLM-based agents have been applied and shown remarkable effectiveness in Software Engineering (SE). The synergy between multiple agents and human interaction brings further ...
- **Link**: [Read Paper](https://arxiv.org/pdf/2409.02977)
- **Labels**: [survey](../../labels/survey.md), [agent design](../../labels/agent_design.md)


## [Llm4fuzz: Guided fuzzing of smart contracts with large language models](paper_28.md)
- **Authors**: Shou, Chaofan and Liu, Jing and Lu, Doudou and Sen, Koushik
- **Abstract**: As blockchain platforms grow exponentially, millions of lines of smart contract code are being deployed to manage extensive digital assets. However, vulnerabilities in this mission-critical code have led to significant exploitations and asset losses. Thorough automated security analysis of smart contracts is thus imperative. This paper introduces LLM4Fuzz to optimize automated smart contract security analysis by leveraging large language models (LLMs) to intelligently guide and prioritize fuzzin...
- **Link**: [Read Paper](https://arxiv.org/pdf/2401.11108.pdf)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


## [Program Slicing in the Era of Large Language Models](paper_26.md)
- **Authors**: Shahandashti, Kimya Khakzad and Mohajer, Mohammad Mahdi and Belle, Alvine Boaye and Wang, Song and Hemmati, Hadi
- **Abstract**: Program slicing is a critical technique in software engineering, enabling developers to isolate relevant portions of code for tasks such as bug detection, code comprehension, and debugging. In this study, we investigate the application of large language models (LLMs) to both static and dynamic program slicing, with a focus on Java programs. We evaluate the performance of four state-of-the-art LLMs- GPT-4o, GPT-3.5 Turbo, Llama-2, and Gemma-7B leveraging advanced prompting techniques, including f...
- **Link**: [Read Paper](https://arxiv.org/pdf/2409.12369)
- **Labels**: [static analysis](../../labels/static_analysis.md), [data-flow analysis](../../labels/data-flow_analysis.md)


## [Rectifier: Code translation with corrector via llms](paper_13.md)
- **Authors**: Yin, Xin and Ni, Chao and Nguyen, Tien N and Wang, Shaohua and Yang, Xiaohu
- **Abstract**: Software migration is garnering increasing attention with the evolution of software and society. Early studies mainly relied on handcrafted translation rules to translate between two languages, the translation process is error-prone and time-consuming. In recent years, researchers have begun to explore the use of pre-trained large language models (LLMs) in code translation. However, code translation is a complex task that LLMs would generate mistakes during code translation, they all produce cer...
- **Link**: [Read Paper](https://arxiv.org/pdf/2407.07472)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [RedAgent: Red Teaming Large Language Models with Context-aware Autonomous Language Agent](paper_4.md)
- **Authors**: Huiyu Xu, Wenhui Zhang, Zhibo Wang, Feng Xiao, Rui Zheng, Yunhe Feng, Zhongjie Ba, Kui Ren
- **Abstract**: Recently, advanced Large Language Models (LLMs) such as GPT-4 have been integrated into many real-world applications like Code Copilot. These applications have significantly expanded the attack surface of LLMs, exposing them to a variety of threats. Among them, jailbreak attacks that induce toxic responses through jailbreak prompts have raised critical safety concerns. To identify these threats, a growing number of red teaming approaches simulate potential adversarial scenarios by crafting jailb...
- **Link**: [Read Paper](https://arxiv.org/abs/2407.16667)
- **Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [benchmark](../../labels/benchmark.md)


## [Repairagent: An autonomous, llm-based agent for program repair](paper_11.md)
- **Authors**: Bouzenia, Islem and Devanbu, Premkumar and Pradel, Michael
- **Abstract**: Automated program repair has emerged as a powerful technique to mitigate the impact of software bugs on system reliability and user experience. This paper introduces RepairAgent, the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM). Unlike existing deep learning-based approaches, which prompt a model with a fixed prompt or in a fixed feedback loop, our work treats the LLM as an agent capable of autonomously planning and executin...
- **Link**: [Read Paper](https://arxiv.org/pdf/2403.17134)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [agent design](../../labels/agent_design.md), [planning](../../labels/planning.md)


## [SecCodePLT: A Unified Platform for Evaluating the Security of Code GenAI](paper_3.md)
- **Authors**: Yu Yang, Yuzhou Nie, Zhun Wang, Yuheng Tang, Wenbo Guo, Bo Li, Dawn Song
- **Abstract**: Language models for code (CodeLMs) have emerged as powerful tools for code-related tasks, outperforming traditional methods and standard machine learning approaches. However, these models are susceptible to security vulnerabilities, drawing increasing research attention from domains such as software engineering, artificial intelligence, and cybersecurity. Despite the growing body of research focused on the security of CodeLMs, a comprehensive survey in this area remains absent. To address this g...
- **Link**: [Read Paper](https://arxiv.org/abs/2410.11096)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [benchmark](../../labels/benchmark.md)


## [Security of Language Models for Code: A Systematic Literature Review](paper_1.md)
- **Authors**: Chen, Yuchen and Sun, Weisong and Fang, Chunrong and Chen, Zhenpeng and Ge, Yifei and Han, Tingxu and Zhang, Quanjun and Liu, Yang and Chen, Zhenyu and Xu, Baowen
- **Abstract**: Language models for code (CodeLMs) have emerged as powerful tools for code-related tasks, outperforming traditional methods and standard machine learning approaches. However, these models are susceptible to security vulnerabilities, drawing increasing research attention from domains such as software engineering, artificial intelligence, and cybersecurity. Despite the growing body of research focused on the security of CodeLMs, a comprehensive survey in this area remains absent. To address this g...
- **Link**: [Read Paper](https://arxiv.org/pdf/2410.15631)
- **Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [survey](../../labels/survey.md)


## [Source Code Vulnerability Detection: Combining Code Language Models and Code Property Graphs](paper_17.md)
- **Authors**: Ruitong Liu and Yanbin Wang and Haitao Xu and Bin Liu and Jianguo Sun and Zhenhao Guo and Wenrui Ma
- **Abstract**: Currently, deep learning successfully applies to code vulnerability detection by learning from code sequences or property graphs. However, sequence-based methods often overlook essential code attributes such as syntax, control flow, and data dependencies, whereas graph-based approaches might underestimate the semantics of code and face challenges in capturing long-distance contextual information.To address this gap, we propose Vul-LMGNN, a unified model that combines pre-trained code language mo...
- **Link**: [Read Paper](https://doi.org/10.48550/arXiv.2404.14719)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [SpecEval: Evaluating Code Comprehension in Large Language Models via Program Specifications](paper_25.md)
- **Authors**: Ma, Lezhi and Liu, Shangqing and Bu, Lei and Li, Shangru and Wang, Yida and Liu, Yang
- **Abstract**: Large Language models have achieved impressive performance in automated software engineering. Extensive efforts have been made to evaluate the abilities of code LLMs in various aspects, with an increasing number of benchmarks and evaluation frameworks proposed. Apart from the most sought-after capability of code generation, the capability of code comprehension is being granted growing attention. Nevertheless, existing works assessing the code comprehension capability of LLMs exhibit varied limit...
- **Link**: [Read Paper](https://arxiv.org/abs/2409.12866)
- **Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)


## [Specification-Driven Code Translation Powered by Large Language Models: How Far Are We?](paper_22.md)
- **Authors**: Soumit Kanti Saha, Fazle Rabbi, Song Wang, Jinqiu Yang
- **Abstract**: Large Language Models (LLMs) are increasingly being applied across various domains, including code-related tasks such as code translation. Previous studies have explored using LLMs for translating code between different programming languages. Since LLMs are more effective with natural language, using natural language as an intermediate representation in code translation tasks presents a promising approach. In this work, we investigate using NL-specification as an intermediate representation for ...
- **Link**: [Read Paper](https://arxiv.org/pdf/2412.04590)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [Teams of LLM Agents can Exploit Zero-Day Vulnerabilities](paper_30.md)
- **Authors**: Fang, Richard and Bindu, Rohan and Gupta, Akul and Zhan, Qiusi and Kang, Daniel
- **Abstract**: LLM agents have become increasingly sophisticated, especially in the realm of cybersecurity. Researchers have shown that LLM agents can exploit real-world vulnerabilities when given a description of the vulnerability and toy capture-the-flag problems. However, these agents still perform poorly on real-world vulnerabilities that are unknown to the agent ahead of time (zero-day vulnerabilities). In this work, we show that teams of LLM agents can exploit real-world, zero-day vulnerabilities. Prior ...
- **Link**: [Read Paper](https://arxiv.org/abs/2406.01637)
- **Labels**: [program testing](../../labels/program_testing.md), [vulnerability exploitation](../../labels/vulnerability_exploitation.md)


## [Top Score on the Wrong Exam: On Benchmarking in Machine Learning for Vulnerability Detection](paper_20.md)
- **Authors**: Niklas Risse and Marcel B{\"{o}hme
- **Abstract**: According to our survey of the machine learning for vulnerability detection (ML4VD) literature published in the top Software Engineering conferences, every paper in the past 5 years defines ML4VD as a binary classification problem: Given a function, does it contain a security flaw?In this paper, we ask whether this decision can really be made without further context and study both vulnerable and non-vulnerable functions in the most popular ML4VD datasets. A function is vulnerable if it was invol...
- **Link**: [Read Paper](https://doi.org/10.48550/arXiv.2408.12986)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


## [Towards Translating Real-World Code with LLMs: A Study of Translating to Rust](paper_36.md)
- **Authors**: Hasan Ferit Eniser, Hanliang Zhang, Cristina David, Meng Wang, Maria Christakis, Brandon Paulsen, Joey Dodds, and Daniel Kroening
- **Abstract**: Large language models (LLMs) show promise in code translation - the task of translating code written in one programming language to another language - due to their ability to write code in most programming languages. However, LLM's effectiveness on translating real-world code remains largely unstudied. In this work, we perform the first substantial study on LLM-based translation to Rust by assessing the ability of five state-of-the-art LLMs, GPT4, Claude 3, Claude 2.1, Gemini Pro, and Mixtral. W...
- **Link**: [Read Paper](https://arxiv.org/abs/2405.11514)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


## [Utilizing Precise and Complete Code Context to Guide LLM in Automatic False Positive Mitigation](paper_37.md)
- **Authors**: Jinbao Chen, Hongjing Xiang, Luhao Li, Yu Zhang, Boyao Ding, Qingwei Li
- **Abstract**: Static Application Security Testing(SAST) tools are crucial for early bug detection and code quality but often generate false positives that slow development. Automating false positive mitigation is thus essential for advancing SAST tools. Past efforts use static/dynamic analysis or machine learning. The advent of Large Language Models, adept at understanding natural language and code, offers promising ways to improve the accuracy and usability of SAST tools. However, existing LLM-based methods ...
- **Link**: [Read Paper](https://arxiv.org/pdf/2411.03079)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [VERT: Verified Equivalent Rust Transpilation with Large Language Models as Few-Shot Learners](paper_34.md)
- **Authors**: Aidan Z.H. Yang, Yoshiki Takashima, Brandon Paulsen, Josiah Dodds, and Daniel Kroening
- **Abstract**: Rust is a programming language that combines memory safety and low-level control, providing C-like performance while guaranteeing the absence of undefined behaviors by default. Rust's growing popularity has prompted research on safe and correct transpiling of existing code-bases to Rust. Existing work falls into two categories: rule-based and large language model (LLM)-based. While rule-based approaches can theoretically produce correct transpilations that maintain input-output equivalence to th...
- **Link**: [Read Paper](https://arxiv.org/abs/2404.18852)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


## [VulEval: Towards Repository-Level Evaluation of Software Vulnerability Detection](paper_15.md)
- **Authors**: Xin{-}Cheng Wen and Xinchen Wang and Yujia Chen and Ruida Hu and David Lo and Cuiyun Gao
- **Abstract**: Deep Learning (DL)-based methods have proven to be effective for software vulnerability detection, with a potential for substantial productivity enhancements for detecting vulnerabilities. Current methods mainly focus on detecting single functions (i.e., intra-procedural vulnerabilities), ignoring the more complex inter-procedural vulnerability detection scenarios in practice. For example, developers routinely engage with program analysis to detect vulnerabilities that span multiple functions wi...
- **Link**: [Read Paper](https://doi.org/10.48550/arXiv.2404.15596)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)


## [Your Instructions Are Not Always Helpful: Assessing the Efficacy of Instruction Fine-tuning for Software Vulnerability Detection](paper_18.md)
- **Authors**: Imam Nur Bani Yusuf and Lingxiao Jiang
- **Abstract**: Software, while beneficial, poses potential cybersecurity risks due to inherent vulnerabilities. Detecting these vulnerabilities is crucial, and deep learning has shown promise as an effective tool for this task due to its ability to perform well without extensive feature engineering. However, a challenge in deploying deep learning for vulnerability detection is the limited availability of training data. Recent research highlights the deep learning efficacy in diverse tasks. This success is attr...
- **Link**: [Read Paper](https://doi.org/10.48550/arXiv.2401.07466)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)
