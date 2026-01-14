# General Coding Task

- [ART: A Unified Unsupervised Framework for Incident Management in Microservice Systems](../venues/ASE2024/paper_44.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Automated incident management is critical for large-scale microservice systems, including tasks such as anomaly detection (AD), failure triage (FT), and root cause localization (RCL). Currently, most techniques focus only on a single task, overlooking shared knowledge across closely related tasks. However, employing isolated models for managing multiple tasks may result in inefficiencies, delayed responses, a lack of systemic perspective, and complexity in updates and operations. Therefore we pr...
  - **Labels**: [general coding task](general_coding_task.md)


- [An Empirical Study to Evaluate AIGC Detectors on Code Content](../venues/ASE2024/paper_16.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Artificial Intelligence Generated Content (AIGC) has garnered considerable attention for its impressive performance, with Large Language Models (LLMs), like ChatGPT, emerging as a leading AIGC model that produces high-quality responses across various applications, including software development and maintenance. Despite its potential, the misuse of LLMs, especially in security and safety-critical domains, such as academic integrity and answering questions on Stack Overflow, poses significant conc...
  - **Labels**: [general coding task](general_coding_task.md), [benchmark](benchmark.md)


- [Automatic Programming: Large Language Models and Beyond](../venues/arXiv2024/paper_12.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Automatic programming has seen increasing popularity due to the emergence of tools like GitHub Copilot which rely on Large Language Models (LLMs). At the same time, automatically generated code faces challenges during deployment due to concerns around quality and trust. In this article, we study automated coding in a general sense and study the concerns around code quality, security and related issues of programmer responsibility. These are key issues for organizations while deciding on the usag...
  - **Labels**: [general coding task](general_coding_task.md), [empirical study](empirical_study.md)


- [Automating Code-Related Tasks Through Transformers: The Impact of Pre-Training](../venues/ICSE2023/paper_9.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Transformers have gained popularity in the software engineering (SE) literature. These deep learning models are usually pre-trained through a self-supervised objective, meant to provide the model with basic knowledge about a language of interest (e.g., Java). A classic pre-training objective is the masked language model (MLM), in which a percentage of tokens from the input (e.g., a Java method) is masked, with the model in charge of predicting them. Once pre-trained, the model is then fine-tuned...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)


- [CXXCrafter: An LLM-Based Agent for Automated C/C++ Open Source Software Building](../venues/FSE2025/paper_34.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Project building is pivotal to support various program analysis tasks, such as generating intermediate representation code for static analysis and preparing binary code for vulnerability reproduction. However, automating the building process for C/C++ projects is a highly complex endeavor, involving tremendous technical challenges, such as intricate dependency management, diverse build systems, varied toolchains, and multifaceted error handling mechanisms. Consequently, building C/C++ projects o...
  - **Labels**: [general coding task](general_coding_task.md), [agent design](agent_design.md)


- [Challenges and Paths Towards AI for Software Engineering](../venues/arXiv2025/paper_1.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: AI for software engineering has made remarkable progress recently, becoming a notable success within generative AI. Despite this progress, many challenges remain before automated software engineering can reach its full potential. This paper presents a structured taxonomy of AI-for-SE tasks beyond code generation, identifies key technical bottlenecks limiting current approaches, and outlines promising research directions toward higher levels of automation in software engineering....
  - **Labels**: [survey](survey.md), [general coding task](general_coding_task.md)


- [ChatDev: Communicative Agents for Software Development](../venues/ACL2024/paper_5.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Software development is a complex task that necessitates cooperation among multiple members with diverse skills. Numerous studies used deep learning to improve specific phases in a waterfall model, such as design, coding, and testing. However, the deep learning model in each phase requires unique designs, leading to technical inconsistencies across various phases, which results in a fragmented and ineffective development process. In this paper, we introduce ChatDev, a chat-powered software devel...
  - **Labels**: [general coding task](general_coding_task.md)


- [CodeImprove: Program Adaptation for Deep Code Models](../venues/ICSE2025/paper_42.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Leveraging deep learning (DL)-based code analysis tools to solve software engineering tasks is becoming increasingly popular. Code models often suffer performance degradation due to various reasons (e.g., code data shifts). Retraining is often required to address these issues, but frequent model updates are costly in labeling and deployment. In this paper, we explore an alternative solution: Adapting the program inputs to the code models. This can be achieved by two steps: 1) input validation th...
  - **Labels**: [general coding task](general_coding_task.md), [code generation](code_generation.md), [code model](code_model.md), [code model robustness](code_model_robustness.md)


- [CodeScope: An Execution-based Multilingual Multitask Multidimensional Benchmark for Evaluating LLMs on Code Understanding and Generation](../venues/ACL2024/paper_18.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated remarkable performance on assisting humans in programming and facilitating programming automation. However, existing benchmarks for evaluating the code understanding and generation capacities of LLMs suffer from severe limitations. First, most benchmarks are insufficient as they focus on a narrow range of popular programming languages and specific tasks, whereas real-world software development scenarios show a critical need to implement systems with...
  - **Labels**: [general coding task](general_coding_task.md), [benchmark](benchmark.md)


- [CodeT5+: Open Code Large Language Models for Code Understanding and Generation](../venues/EMNLP2023/paper_1.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Large language models (LLMs) pretrained on vast source code have achieved prominent progress in code intelligence. However, existing code LLMs have two main limitations. First, they often adopt a specific architecture (encoder-only or decoder-only) or rely on a unified encoder-decoder network for different downstream tasks, lacking the flexibility to operate in the optimal architecture for a specific task. Secondly, they often employ a limited set of pretraining objectives which might not be rel...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Codebert: A pre-trained model for programming and natural languages](../venues/EMNLP2020/paper_1.md), ([EMNLP2020](../venues/EMNLP2020/README.md))

  - **Abstract**: We present CodeBERT, a bimodal pre-trained model for programming language (PL) and nat-ural language (NL). CodeBERT learns general-purpose representations that support downstream NL-PL applications such as natural language codesearch, code documentation generation, etc. We develop CodeBERT with Transformer-based neural architecture, and train it with a hybrid objective function that incorporates the pre-training task of replaced token detection, which is to detect plausible alternatives sampled ...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Codemind: A framework to challenge large language models for code reasoning](../venues/arXiv2024/paper_6.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Solely relying on test passing to evaluate Large Language Models (LLMs) for code synthesis may result in unfair assessment or promoting models with data leakage. As an alternative, we introduce CodeMind, a framework designed to gauge the code reasoning abilities of LLMs. CodeMind currently supports three code reasoning tasks: Independent Execution Reasoning (IER), Dependent Execution Reasoning (DER), and Specification Reasoning (SR). The first two evaluate models to predict the execution output ...
  - **Labels**: [general coding task](general_coding_task.md), [empirical study](empirical_study.md)


- [CombTransformers: Statement-Wise Transformers for Statement-Wise Representations](../venues/TSE2023/paper_2.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: This study presents a novel category of Transformer architectures known as comb transformers, which effectively reduce the space complexity of the self-attention layer from a quadratic to a subquadratic level. This is achieved by processing sequence segments independently and incorporating &lt;inline-formula&gt;&lt;tex-math notation="LaTeX"&gt;$mathcal{X}$&lt;/tex-math&gt;&lt;alternatives&gt;&lt;mml:math&gt;&lt;mml:mrow&gt;&lt;mml:mi mathvariant="script"&gt;X&lt;/mml:mi&gt;&lt;/mml:mrow&gt;&lt;/...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [ComplexCodeEval: A Benchmark for Evaluating Large Code Models on More Complex Code](../venues/ASE2024/paper_28.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: In recent years, with the widespread attention of academia and industry on the application of large language models (LLMs) to code-related tasks, an increasing number of large code models (LCMs) have been proposed and corresponding evaluation benchmarks have continually emerged. Although existing evaluation benchmarks are helpful for comparing different LCMs, they may not reflect the performance of LCMs in various development scenarios. Specifically, they might evaluate model performance in only...
  - **Labels**: [general coding task](general_coding_task.md), [benchmark](benchmark.md)


- [Experiential Co-Learning of Software-Developing Agents](../venues/ACL2024/paper_19.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Recent advancements in large language models (LLMs) have brought significant changes to various domains, especially through LLM-driven autonomous agents. A representative scenario is in software development, where LLM agents demonstrate efficient collaboration, task division, and assurance of software quality, markedly reducing the need for manual involvement. However, these agents frequently perform a variety of tasks independently, without benefiting from past experiences, which leads to repea...
  - **Labels**: [general coding task](general_coding_task.md), [agent design](agent_design.md), [planning](planning.md)


- [Exploring Distributional Shifts in Large Language Models for Code Analysis](../venues/EMNLP2023/paper_11.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: We systematically study how three large language models with code capabilities - CodeT5, Codex, and ChatGPT - generalize to out-of-domain data. We consider two fundamental applications - code summarization, and code generation. We split data into domains following its natural boundaries - by an organization, by a project, and by a module within the software project. We establish that samples from each new domain present all the models with a significant challenge of distribution shift. We study ...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)


- [Fair: Flow type-aware pre-training of compiler intermediate representations](../venues/ICSE2024/paper_21.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: While the majority of existing pre-trained models from code learn source code features such as code tokens and abstract syntax trees, there are some other works that focus on learning from compiler intermediate representations (IRs). Existing IR-based models typically utilize IR features such as instructions, control and data flow graphs (CDFGs), call graphs, etc. However, these methods confuse variable nodes and instruction nodes in a CDFG and fail to distinguish different types of flows, and t...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [IR code model](IR_code_model.md)


- [GrammarT5: Grammar-Integrated Pretrained Encoder-Decoder Neural Model for Code](../venues/ICSE2024/paper_24.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Pretrained models for code have exhibited promising performance across various code-related tasks, such as code summarization, code completion, code translation, and bug detection. However, despite their success, the majority of current models still represent code as a token sequence, which may not adequately capture the essence of the underlying code structure.In this work, we propose GrammarT5, a grammar-integrated encoder-decoder pretrained neural model for code. GrammarT5 employs a novel gra...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Graphcodebert: Pre-training code representations with data flow](../venues/ICLR2021/paper_1.md), ([ICLR2021](../venues/ICLR2021/README.md))

  - **Abstract**: Pre-trained models for programming language have achieved dramatic empirical improvements on a variety of code-related tasks such as code search, code completion, code summarization, etc. However, existing pre-trained models regard a code snippet as a sequence of tokens, while ignoring the inherent structure of code, which provides crucial code semantics and would enhance the code understanding process. We present GraphCodeBERT, a pre-trained model for programming language that considers the inh...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [How could neural networks understand programs?](../venues/ICML2021/paper_1.md), ([ICML2021](../venues/ICML2021/README.md))

  - **Abstract**: Semantic understanding of programs is a fundamental problem for programming language processing (PLP). Recent works that learn representations of code based on pre-training techniques in NLP have pushed the frontiers in this direction. However, the semantics of PL and NL have essential differences. These being ignored, we believe it is difficult to build a model to better understand programs, by either directly applying off-the-shelf NLP pre-training techniques to the source code, or adding feat...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [IR code model](IR_code_model.md)


- [Integrate the Essence and Eliminate the Dross: Fine-Grained Self-Consistency for Free-Form Language Generation](../venues/ACL2024/paper_22.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Self-consistency (SC), leveraging multiple samples from LLMs, shows significant gains on various reasoning tasks but struggles with free-form generation due to the difficulty of aggregating answers. Its variants, UCS and USC, rely on sample selection or voting mechanisms to improve output quality. These methods, however, face limitations due to their inability to fully utilize the nuanced consensus knowledge present within multiple candidate samples, often resulting in suboptimal outputs. We pro...
  - **Labels**: [general coding task](general_coding_task.md), [empirical study](empirical_study.md)


- [Large language models for software engineering: A systematic literature review](../venues/TOSEM2023/paper_1.md), ([TOSEM2023](../venues/TOSEM2023/README.md))

  - **Abstract**: Large Language Models (LLMs) have significantly impacted numerous domains, including Software Engineering (SE). Many recent publications have explored LLMs applied to various SE tasks. Nevertheless, a comprehensive understanding of the application, effects, and possible limitations of LLMs on SE is still in its early stages. To bridge this gap, we conducted a systematic literature review (SLR) on LLM4SE, with a particular focus on understanding how LLMs can be exploited to optimize processes and...
  - **Labels**: [survey](survey.md), [general coding task](general_coding_task.md)


- [Mastering the Craft of Data Synthesis for {C}ode{LLM}s](../venues/NAACL2025/paper_10.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Large language models (LLMs) have shown impressive performance in \textit{code} understanding and generation, making coding tasks a key focus for researchers due to their practical applications and value as a testbed for LLM evaluation. Data synthesis and filtering techniques have been widely adopted and shown to be highly effective in this context. In this paper, we present a focused survey and taxonomy of these techniques, emphasizing recent advancements. We highlight key challenges, explore f...
  - **Labels**: [general coding task](general_coding_task.md), [empirical study](empirical_study.md)


- [MiniChain: A Small Library for Coding with Large Language Models](../venues/EMNLP2023/paper_12.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Programming augmented by large language models (LLMs) opens up many new application areas, but also requires care. LLMs are accurate enough, on average, to replace core functionality, yet make basic mistakes that demonstrate a lack of robustness. An ecosystem of prompting tools, from intelligent agents to new programming languages, have emerged with different solutions for patching LLMs with other tools. In this work, we introduce MiniChain, an opinionated tool for LLM augmented programming, wit...
  - **Labels**: [general coding task](general_coding_task.md)


- [Neural code comprehension: A learnable representation of code semantics](../venues/NeurIPS2018/paper_1.md), ([NeurIPS2018](../venues/NeurIPS2018/README.md))

  - **Abstract**: With the recent success of embeddings in natural language processing, research has been conducted into applying similar methods to code analysis. Most works attempt to process the code directly or use a syntactic tree representation, treating it like sentences written in a natural language. However, none of the existing methods are sufficient to comprehend program semantics robustly, due to structural features such as function calls, branching, and interchangeable order of statements. In this pa...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [On Calibration of Pre-trained Code Models](../venues/ICSE2024/paper_25.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Pre-trained code models have achieved notable success in the field of Software Engineering (SE). However, existing studies have predominantly focused on improving model performance, with limited attention given to other critical aspects such as model calibration. Model calibration, which refers to the accurate estimation of predictive uncertainty, is a vital consideration in practical applications. Therefore, in order to advance the understanding of model calibration in SE, we conduct a comprehe...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [On Improving Repository-Level Code QA for Large Language Models](../venues/ACL2024/paper_7.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Large Language Models (LLMs) such as ChatGPT, GitHub Copilot, Llama, or Mistral assist programmers as copilots and knowledge sources to make the coding process faster and more efficient. This paper aims to improve the copilot performance by implementing different self-alignment processes and retrieval-augmented generation (RAG) pipelines, as well as their combination. To test the effectiveness of all approaches, we create a dataset and apply a model-based evaluation, using LLM as a judge. It is ...
  - **Labels**: [general coding task](general_coding_task.md), [benchmark](benchmark.md)


- [PromSec: Prompt Optimization for Secure Generation of Functional Source Code with Large Language Models (LLMs)](../venues/CCS2024/paper_4.md), ([CCS2024](../venues/CCS2024/README.md))

  - **Abstract**: The capability of generating high-quality source code using large language models (LLMs) reduces software development time and costs. However, recent literature and our empirical investigation in this work show that while LLMs can generate functioning code, they inherently tend to introduce security vulnerabilities, limiting their potential. This problem is mainly due to their training on massive open-source corpora exhibiting insecure and inefficient programming practices. Therefore, automatic ...
  - **Labels**: [general coding task](general_coding_task.md), [code generation](code_generation.md), [code model](code_model.md), [code model security](code_model_security.md)


- [Retrieval-Based Prompt Selection for Code-Related Few-Shot Learning](../venues/ICSE2023/paper_10.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Large language models trained on massive code corpora can generalize to new tasks without the need for task-specific fine-tuning. In few-shot learning, these models take as input a prompt, composed of natural language instructions, a few instances of task demonstration, and a query and generate an output. However, the creation of an effective prompt for code-related tasks in few-shot learning has received little attention. We present a technique for prompt creation that automatically retrieves c...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [SWE-GPT: A Process-Centric Language Model for Automated Software Improvement](../venues/ISSTA2025/paper_32.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated remarkable performance in code generation, significantly enhancing the coding efficiency of developers. Recent advancements in LLM-based agents have led to significant progress in end-to-end automatic software engineering (ASE), particularly in software maintenance (e.g., fixing software issues) and evolution (e.g., adding new features). Despite these encouraging advances, current research faces two major challenges. First, state-of-the-art performa...
  - **Labels**: [general coding task](general_coding_task.md), [code generation](code_generation.md), [program synthesis](program_synthesis.md), [software maintenance and deployment](software_maintenance_and_deployment.md), [agent design](agent_design.md)


- [SemCoder: Training Code Language Models with Comprehensive Semantics](../venues/NeurIPS2024/paper_1.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Code Large Language Models (Code LLMs) have excelled at tasks like code completion but often miss deeper semantics such as execution effects and dynamic states. This paper aims to bridge the gap between Code LLMs' reliance on static text data and the need for semantic understanding for complex tasks like debugging and program repair. We introduce a novel strategy, monologue reasoning, to train Code LLMs to reason comprehensive semantics, encompassing high-level functional descriptions, local exe...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Symmetry-Preserving Program Representations for Learning Code Semantics](../venues/ICML2024/paper_3.md), ([ICML2024](../venues/ICML2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have shown promise in automated program reasoning, a crucial aspect of many security tasks. However, existing LLM architectures for code are often borrowed from other domains like natural language processing, raising concerns about their generalization and robustness to unseen code. A key generalization challenge is to incorporate the knowledge of code semantics, including control and data flow, into the LLM architectures. Drawing inspiration from examples of convolu...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Unifying the perspectives of nlp and software engineering: A survey on language models for code](../venues/TMLR2024/paper_1.md), ([TMLR2024](../venues/TMLR2024/README.md))

  - **Abstract**: In this work we systematically review the recent advancements in software engineering with language models, covering 70+ models, 40+ evaluation tasks, 180+ datasets, and 900 related works. Unlike previous works, we integrate software engineering (SE) with natural language processing (NLP) by discussing the perspectives of both sides: SE applies language models for development automation, while NLP adopts SE tasks for language model evaluation. We break down code processing models into general la...
  - **Labels**: [general coding task](general_coding_task.md), [survey](survey.md)


- [Using Transfer Learning for Code-Related Tasks](../venues/TSE2023/paper_5.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: Deep learning (DL) techniques have been used to support several code-related tasks such as code summarization and bug-fixing. In particular, pre-trained transformer models are on the rise, also thanks to the excellent results they achieved in Natural Language Processing (NLP) tasks. The basic idea behind these models is to first pre-train them on a generic dataset using a self-supervised task (e.g., filling masked words in sentences). Then, these models are fine-tuned to support specific tasks o...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [WaveCoder: Widespread And Versatile Enhancement For Code Large Language Models By Instruction Tuning](../venues/ACL2024/paper_17.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Recent work demonstrates that, after instruction tuning, Code Large Language Models (Code LLMs) can obtain impressive capabilities to address a wide range of code-related tasks. However, current instruction tuning methods for Code LLMs mainly focus on the traditional code generation task, resulting in poor performance in complex multi-task scenarios. In this paper, we concentrate on multiple code-related tasks and present WaveCoder, a series of Code LLMs trained with Widespread And Versatile Enh...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [What Makes Good In-Context Demonstrations for Code Intelligence Tasks with LLMs?](../venues/ASE2023/paper_10.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Pre-trained models of source code have gained widespread popularity in many code intelligence tasks. Recently, with the scaling of the model and corpus size, large language models have shown the ability of in-context learning (ICL). ICL employs task instructions and a few examples as demonstrations, and then inputs the demonstrations to the language models for making predictions. This new learning paradigm is training-free and has shown impressive performance in various natural language processi...
  - **Labels**: [general coding task](general_coding_task.md)


- [XCodeEval: An Execution-based Large Scale Multilingual Multitask Benchmark for Code Understanding, Generation, Translation and Retrieval](../venues/ACL2024/paper_20.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Recently, pre-trained large language models (LLMs) have shown impressive abilities in generating codes from natural language descriptions, repairing buggy codes, translating codes between languages, and retrieving relevant code segments. However, the evaluation of these models has often been performed in a scattered way on only one or two specific tasks, in a few languages, at a partial granularity (e.g., function) level, and in many cases without proper training data. Even more concerning is th...
  - **Labels**: [general coding task](general_coding_task.md), [benchmark](benchmark.md)
