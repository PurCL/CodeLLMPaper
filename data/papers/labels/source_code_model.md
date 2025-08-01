# Source Code Model

- [A Learning-Based Approach to Static Program Slicing](../venues/OOPSLA2024/paper_7.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Traditional program slicing techniques are crucial for early bug detection and manual/automated debugging of online code snippets. Nevertheless, their inability to handle incomplete code hinders their real-world applicability in such scenarios. To overcome these challenges, we present NS-Slicer, a novel learning-based approach that predicts static program slices for both complete and partial code Our tool leverages a pre-trained language model to exploit its understanding of fine-grained variabl...
  - **Labels**: [static analysis](static_analysis.md), [data-flow analysis](data-flow_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [AI-Assisted Code Authoring at Scale: Fine-Tuning, Deploying, and Mixed Methods Evaluation](../venues/FSE2024/paper_1.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Generative LLMs have been shown to effectively power AI-based code authoring tools that can suggest entire statements or blocks of code during code authoring. In this paper we present CodeCompose, an AI-assisted code authoring tool developed and deployed at Meta internally. CodeCompose is based on the InCoder LLM that merges generative capabilities with bi-directionality. We have scaled up CodeCompose to serve tens of thousands of developers at Meta, across 9 programming languages and several co...
  - **Labels**: [code generation](code_generation.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [AMR-Evol: Adaptive Modular Response Evolution Elicits Better Knowledge Distillation for Large Language Models in Code Generation](../venues/EMNLP2024/paper_17.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: The impressive performance of proprietary LLMs like GPT4 in code generation has led to a trend to replicate these capabilities in open-source models through knowledge distillation (e.g. Code Evol-Instruct). However, these efforts often neglect the crucial aspect of response quality, relying heavily on teacher models for direct response distillation. This paradigm, especially for complex instructions, can degrade the quality of synthesized data, compromising the knowledge distillation process. To...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Are Human Rules Necessary? Generating Reusable APIs with CoT Reasoning and In-Context Learning](../venues/FSE2024/paper_14.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Inspired by the great potential of Large Language Models (LLMs) for solving complex coding tasks, in this paper, we propose a novel approach, named Code2API, to automatically perform APIzation for Stack Overflow code snippets. Code2API does not require additional model training or any manual crafting rules and can be easily deployed on personal computers without relying on other external tools. Specifically, Code2API guides the LLMs through well-designed prompts to generate well-formed APIs for ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [source code model](source_code_model.md)


- [Automating Code-Related Tasks Through Transformers: The Impact of Pre-Training](../venues/ICSE2023/paper_9.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Transformers have gained popularity in the software engineering (SE) literature. These deep learning models are usually pre-trained through a self-supervised objective, meant to provide the model with basic knowledge about a language of interest (e.g., Java). A classic pre-training objective is the masked language model (MLM), in which a percentage of tokens from the input (e.g., a Java method) is masked, with the model in charge of predicting them. Once pre-trained, the model is then fine-tuned...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)


- [CAT-LM training language models on aligned code and tests](../venues/ASE2023/paper_13.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Testing is an integral but often neglected part of the software development process. Classical test generation tools such as EvoSuite generate behavioral test suites by optimizing for coverage, but tend to produce tests that are hard to understand. Language models trained on code can generate code that is highly similar to that written by humans, but current models are trained to generate each file separately, as is standard practice in natural language processing, and thus fail to consider the ...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [COMEX: A Tool for Generating Customized Source Code Representations](../venues/ASE2023/paper_1.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Learning effective representations of source code is critical for any Machine Learning for Software Engineering (ML4SE) system. Inspired by natural language processing, large language models (LLMs) like Codex and CodeGen treat code as generic sequences of text and are trained on huge corpora of code data, achieving state of the art performance on several software engineering (SE) tasks. However, valid source code, unlike natural language, follows a strict structure and pattern governed by the un...
  - **Labels**: [code generation](code_generation.md), [source code model](source_code_model.md)


- [COSTELLO: Contrastive Testing for Embedding-Based Large Language Model as a Service Embeddings](../venues/FSE2024/paper_24.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Large language models have gained significant popularity and are often provided as a service (i.e., LLMaaS).  Companies like OpenAI and Google provide online APIs of LLMs to allow downstream users to create innovative applications.  Despite its popularity, LLM safety and quality assurance is a well-recognized concern in the real world, requiring extra efforts for testing these LLMs.  Unfortunately, while end-to-end services like ChatGPT have garnered rising attention in terms of testing, the LLM...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [CoEdPilot: Recommending Code Edits with Learned Prior Edit Relevance, Project-wise Awareness, and Interactive Nature](../venues/ISSTA2024/paper_8.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Recent years have seen the development of LLM-based code generation. Compared to generating code in a software project, incremental code edits are empirically observed to be more frequent. The emerging code editing approaches usually formulate the problem as generating an edit based on known relevant prior edits and context. However, practical code edits can be more complicated. First, an editing session can include multiple (ir)relevant edits to the code under edit. Second, the inference of the...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [CoSS: Leveraging Statement Semantics for Code Summarization](../venues/TSE2023/paper_4.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: Automated code summarization tools allow generating descriptions for code snippets in natural language, which benefits software development and maintenance. Recent studies demonstrate that the quality of generated summaries can be improved by using additional code representations beyond token sequences. The majority of contemporary approaches mainly focus on extracting code syntactic and structural information from abstract syntax trees (ASTs). However, from the view of macro-structures, it is c...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [CodeBERTScore: Evaluating Code Generation with Pretrained Models of Code](../venues/EMNLP2023/paper_16.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Since the rise of neural natural-language-to-code models (NL\rightarrowCode) that can generate long expressions and statements rather than a single next-token, one of the major problems has been reliably evaluating their generated output. In this paper, we propose CodeBERTScore: an evaluation metric for code generation, which builds on BERTScore (Zhang et al., 2020). Instead of encoding only the generated tokens as in BERTScore, CodeBERTScore also encodes the natural language input preceding the...
  - **Labels**: [code generation](code_generation.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [CodeT5+: Open Code Large Language Models for Code Understanding and Generation](../venues/EMNLP2023/paper_1.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Large language models (LLMs) pretrained on vast source code have achieved prominent progress in code intelligence. However, existing code LLMs have two main limitations. First, they often adopt a specific architecture (encoder-only or decoder-only) or rely on a unified encoder-decoder network for different downstream tasks, lacking the flexibility to operate in the optimal architecture for a specific task. Secondly, they often employ a limited set of pretraining objectives which might not be rel...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Codebert: A pre-trained model for programming and natural languages](../venues/EMNLP2020/paper_1.md), ([EMNLP2020](../venues/EMNLP2020/README.md))

  - **Abstract**: We present CodeBERT, a bimodal pre-trained model for programming language (PL) and nat-ural language (NL). CodeBERT learns general-purpose representations that support downstream NL-PL applications such as natural language codesearch, code documentation generation, etc. We develop CodeBERT with Transformer-based neural architecture, and train it with a hybrid objective function that incorporates the pre-training task of replaced token detection, which is to detect plausible alternatives sampled ...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [CombTransformers: Statement-Wise Transformers for Statement-Wise Representations](../venues/TSE2023/paper_2.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: This study presents a novel category of Transformer architectures known as comb transformers, which effectively reduce the space complexity of the self-attention layer from a quadratic to a subquadratic level. This is achieved by processing sequence segments independently and incorporating &lt;inline-formula&gt;&lt;tex-math notation="LaTeX"&gt;$mathcal{X}$&lt;/tex-math&gt;&lt;alternatives&gt;&lt;mml:math&gt;&lt;mml:mrow&gt;&lt;mml:mi mathvariant="script"&gt;X&lt;/mml:mi&gt;&lt;/mml:mrow&gt;&lt;/...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection](../venues/ICSE2024/paper_2.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Deep learning-based vulnerability detection has shown great performance and, in some studies, outperformed static analysis tools. However, the highest-performing approaches use token-based transformer models, which are not the most efficient to capture code semantics required for vulnerability detection. Classical program analysis techniques such as dataflow analysis can detect many types of bugs based on their root causes. In this paper, we propose to combine such causal-based vulnerability det...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [DolphCoder: Echo-Locating Code Large Language Models with Diverse and Multi-Objective Instruction Tuning](../venues/ACL2024/paper_14.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Code Large Language Models (Code LLMs) have demonstrated outstanding performance in code-related tasks. Various instruction finetuning approaches have been proposed to boost the code generation performance of pre-trained Code LLMs. In this paper, we introduce a diverse instruction model DolphCoder with self-evaluating for code generation. It learns diverse instruction targets and combines a code evaluation objective to enhance its code generation ability. Our model achieves superior performance ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Domain Adaptive Code Completion via Language Models and Decoupled Domain Databases](../venues/ASE2023/paper_18.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated remarkable performance in code completion. However, due to the lack of domain-specific knowledge, they may not be optimal in completing code that requires intensive domain knowledge for example completing the library names. Although there are several works that have confirmed the effectiveness of fine-tuning techniques to adapt language models for code completion in specific domains. They are limited by the need for constant fine-tuning of the model...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Dynamic Scoring Code Token Tree: A Novel Decoding Strategy for Generating High-Performance Code](../venues/ASE2024/paper_20.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Within the realms of scientific computing, large-scale data processing, and artificial intelligence-powered computation, disparities in performance, which originate from differing code implementations, directly influence the practicality of the code. Although existing works tried to utilize code knowledge to enhance the execution performance of codes generated by large language models, they neglect code evaluation outcomes which directly refer to the code execution details, resulting in ineffici...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Enhancing Discourse Dependency Parsing with Sentence Dependency Parsing: A Unified Generative Method Based on Code Representation](../venues/EMNLP2024/paper_14.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Due to the high complexity of Discourse Dependency Parsing (DDP) tasks, their existing annotation resources are relatively scarce compared to other NLP tasks, and different DDP tasks also have significant differences in annotation schema. These issues have led to the dilemma of low resources for DDP tasks. Thanks to the powerful capabilities of Large Language Models (LLMs) in cross-task learning, we can use LLMs to model dependency parsing under different annotation schema in an unified manner, ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Evaluating the effectiveness of deep learning models for foundational program analysis tasks](../venues/OOPSLA2024/paper_9.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: While deep neural networks provide state-of-the-art solutions to a wide range of programming language tasks, their effectiveness in dealing with foundational program analysis tasks remains under explored. In this paper, we present an empirical study that evaluates four prominent models of code (i.e., CuBERT, CodeBERT, GGNN, and Graph Sandwiches) in two such foundational tasks: (1) alias prediction, in which models predict whether two pointers must alias, may alias or must not alias; and (2) equi...
  - **Labels**: [static analysis](static_analysis.md), [pointer analysis](pointer_analysis.md), [equivalence checking](equivalence_checking.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [EvoR: Evolving Retrieval for Code Generation](../venues/EMNLP2024/paper_3.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Recently the retrieval-augmented generation (RAG) has been successfully applied in code generation. However, existing pipelines for retrieval-augmented code generation (RACG) employ static knowledge bases with a single source, limiting the adaptation capabilities of Large Language Models (LLMs) to domains they have insufficient knowledge of. In this work, we develop a novel pipeline, EVOR, that employs the synchronous evolution of both queries and diverse knowledge bases. On two realistic settin...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [source code model](source_code_model.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [Exploring Distributional Shifts in Large Language Models for Code Analysis](../venues/EMNLP2023/paper_11.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: We systematically study how three large language models with code capabilities - CodeT5, Codex, and ChatGPT - generalize to out-of-domain data. We consider two fundamental applications - code summarization, and code generation. We split data into domains following its natural boundaries - by an organization, by a project, and by a module within the software project. We establish that samples from each new domain present all the models with a significant challenge of distribution shift. We study ...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)


- [Exploring Parameter-Efficient Fine-Tuning of Large Language Model on Automated Program Repair](../venues/ASE2024/paper_14.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Automated Program Repair (APR) aims to fix bugs by generating patches. And existing work has demonstrated that "pre-training and fine-tuning" paradigm enables Large Language Models (LLMs) improve fixing capabilities on APR. However, existing work mainly focuses on Full-Model Fine-Tuning (FMFT) for APR and limited research has been conducted on the execution-based evaluation of Parameter-Efficient Fine-Tuning (PEFT) for APR. Comparing to FMFT, PEFT can reduce computing resource consumption withou...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Follow-Up Attention: An Empirical Study of Developer and Neural Model Code Exploration](../venues/TSE2024/paper_12.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Recent neural models of code, such as OpenAI Codex and AlphaCode, have demonstrated remarkable proficiency at code generation due to the underlying attention mechanism. However, it often remains unclear how the models actually process code, and to what extent their reasoning and the way their attention mechanism scans the code matches the patterns of developers. A poor understanding of the model reasoning process limits the way in which current neural models are leveraged today, so far mostly fo...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [benchmark](benchmark.md)


- [Generating Data for Symbolic Language with Large Language Models](../venues/EMNLP2023/paper_5.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: While large language models (LLMs) bring not only performance but also complexity, recent work has started to turn LLMs into data generators rather than task inferencers, where another affordable task model is trained for efficient deployment and inference. However, such an approach has primarily been applied to natural language tasks, and has not yet been explored for symbolic language tasks with complex structured outputs (e.g., semantic parsing and code generation). In this paper, we propose ...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Grace: Language Models Meet Code Edits](../venues/FSE2023/paper_4.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Developers spend a significant amount of time in editing code for a variety of reasons such as bug fixing or adding new features. Designing effective methods to predict code edits has been an active yet challenging area of research due to the diversity of code edits and the difficulty of capturing the developer intent. In this work, we address these challenges by endowing pre-trained large language models (LLMs) with the knowledge of relevant prior associated edits, which we call the Grace (Gene...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [GrammarT5: Grammar-Integrated Pretrained Encoder-Decoder Neural Model for Code](../venues/ICSE2024/paper_24.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Pretrained models for code have exhibited promising performance across various code-related tasks, such as code summarization, code completion, code translation, and bug detection. However, despite their success, the majority of current models still represent code as a token sequence, which may not adequately capture the essence of the underlying code structure.In this work, we propose GrammarT5, a grammar-integrated encoder-decoder pretrained neural model for code. GrammarT5 employs a novel gra...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Graphcodebert: Pre-training code representations with data flow](../venues/ICLR2021/paper_1.md), ([ICLR2021](../venues/ICLR2021/README.md))

  - **Abstract**: Pre-trained models for programming language have achieved dramatic empirical improvements on a variety of code-related tasks such as code search, code completion, code summarization, etc. However, existing pre-trained models regard a code snippet as a sequence of tokens, while ignoring the inherent structure of code, which provides crucial code semantics and would enhance the code understanding process. We present GraphCodeBERT, a pre-trained model for programming language that considers the inh...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [HiRoPE: Length Extrapolation for Code Models Using Hierarchical Position](../venues/ACL2024/paper_2.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Addressing the limitation of context length in large language models for code-related tasks is the primary focus of this paper. Existing LLMs are constrained by their pre-trained context lengths, leading to performance issues in handling long complex code sequences. Inspired by how human programmers navigate code, we introduce Hierarchical Rotary Position Embedding (HiRoPE), a novel approach that enhances the traditional rotary position embedding into a hierarchical format based on the hierarchi...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [How Do Your Code LLMs perform? Empowering Code Instruction Tuning with Really Good Data](../venues/EMNLP2024/paper_30.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Recently, there has been a growing interest in studying how to construct better code instruction tuning data. However, we observe Code models trained with these datasets exhibit high performance on HumanEval but perform worse on other benchmarks such as LiveCodeBench. Upon further investigation, we find that many datasets suffer from severe data leakage. After cleaning up most of the leaked data, some well-known high-quality datasets perform poorly. This discovery reveals a new challenge: identi...
  - **Labels**: [code generation](code_generation.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Improving Code Extraction from Coding Screencasts Using a Code-Aware Encoder-Decoder Model](../venues/ASE2023/paper_4.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Accurate automatic code extraction from tutorial videos is crucial for software developers seeking to reuse the code contained in these videos. Current methods using optical character recognition (OCR) often yield inaccurate results due to code complexity and variations in screencast formats. To address this issue, we introduce CodeT5-OCRfix, an approach that leverages the pre-trained code-aware large language model CodeT5 to enhance code extraction accuracy by post-processing OCRed code. We fir...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Isolating Compiler Bugs by Generating Effective Witness Programs With Large Language Models](../venues/TSE2024/paper_4.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Compiler bugs pose a significant threat to safety-critical applications, and promptly as well as effectively isolating these bugs is crucial for assuring the quality of compilers. However, the limited availability of debugging information on reported bugs complicates the compiler bug isolation task. Existing compiler bug isolation approaches convert the problem into a test program mutation problem, but they are still limited by ineffective mutation strategies or high human effort requirements. D...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Knowledge Transfer from High-Resource to Low-Resource Programming Languages for Code LLMs](../venues/OOPSLA2024/paper_2.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Over the past few years, Large Language Models of Code (Code LLMs) have started to have a significant impact on programming practice. Code LLMs are also emerging as building blocks for research in programming languages and software engineering. However, the quality of code produced by a Code LLM varies significantly by programming language. Code LLMs produce impressive results on high-resource programming languages that are well represented in their training data (e.g., Java, Python, or JavaScri...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [LLMs: Understanding Code Syntax and Semantics for Code Analysis](../venues/arXiv2023/paper_1.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Large language models~(LLMs) demonstrate significant potential to revolutionize software engineering (SE) by exhibiting outstanding performance in SE tasks such as code and document generation. However, the high reliability and risk control requirements in software engineering raise concerns about the lack of interpretability of LLMs. To address this concern, we conducted a study to evaluate the capabilities of LLMs and their limitations for code analysis in SE. We break down the abilities neede...
  - **Labels**: [static analysis](static_analysis.md), [data-flow analysis](data-flow_analysis.md), [call graph analysis](call_graph_analysis.md), [data-flow analysis](data-flow_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)


- [Large Language Models for Test-Free Fault Localization](../venues/ICSE2024/paper_3.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Fault Localization (FL) aims to automatically localize buggy lines of code, a key first step in many manual and automatic debugging tasks. Previous FL techniques assume the provision of input tests, and often require extensive program analysis, program instrumentation, or data preprocessing. Prior work on deep learning for APR struggles to learn from small datasets and produces limited results on real-world programs. Inspired by the ability of large language models (LLMs) of code to adapt to new...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Learning to Detect and Localize Multilingual Bugs](../venues/FSE2024/paper_31.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Increasing studies have shown bugs in multi-language software as a critical loophole in modern software quality assurance, especially those induced by language interactions (i.e., multilingual bugs). Yet existing tool support for bug detection/localization remains largely limited to single-language software, despite the long-standing prevalence of multi-language systems in various real-world software domains. Extant static/dynamic analysis and deep learning (DL) based approaches all face major c...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Leveraging Semantic Relations in Code and Data to Enhance Taint Analysis of Embedded Systems](../venues/USENIXSec2024/paper_2.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: IoT devices have significantly impacted our daily lives, and detecting vulnerabilities in embedded systems early on is critical for ensuring their security. Among the existing vulnerability detection techniques for embedded systems, static taint analysis has been proven effective in detecting severe vulnerabilities, such as command injection vulnerabilities, which can cause remote code execution. Nevertheless, static taint analysis is faced with the problem of identifying sources comprehensively...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [LongCoder: {A} Long-Range Pre-trained Language Model for Code Completion](../venues/ICML2023/paper_1.md), ([ICML2023](../venues/ICML2023/README.md))

  - **Abstract**: In this paper, we introduce a new task for code completion that focuses on handling long code input and propose a sparse Transformer model, called LongCoder, to address this task. LongCoder employs a sliding window mechanism for self-attention and introduces two types of globally accessible tokens-bridge tokens and memory tokens-to improve performance and efficiency. Bridge tokens are inserted throughout the input sequence to aggregate local information and facilitate global interaction, while m...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [MPCoder: Multi-user Personalized Code Generator with Explicit and Implicit Style Representation Learning](../venues/ACL2024/paper_12.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated great potential for assisting developers in their daily development. However, most research focuses on generating correct code, how to use LLMs to generate personalized code has seldom been investigated. To bridge this gap, we proposed MPCoder (Multi-user Personalized Code Generator) to generate personalized code for multiple users. To better learn coding style features, we utilize explicit coding style residual learning to capture the syntax code s...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Magicoder: Empowering Code Generation with OSS-Instruct](../venues/ICML2024/paper_2.md), ([ICML2024](../venues/ICML2024/README.md))

  - **Abstract**: We introduce Magicoder, a series of fully open-source (code, weights, and data) Large Language Models (LLMs) for code that significantly closes the gap with top code models while having no more than 7B parameters. Magicoder models are trained on 75K synthetic instruction data using OSS-Instruct, a novel approach to enlightening LLMs with open-source code snippets to generate diverse instruction data for code. Our main motivation is to mitigate the inherent bias of the synthetic data generated by...
  - **Labels**: [code generation](code_generation.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Multilingual Code Co-evolution using Large Language Models](../venues/FSE2023/paper_2.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Many software projects implement APIs and algorithms in multiple programming languages. Maintaining such projects is tiresome, as developers have to ensure that any change (e.g., a bug fix or a new feature) is being propagated, timely and without errors, to implementations in other programming languages. In the world of ever-changing software, using rule-based translation tools (i.e., transpilers) or machine learning models for translating code from one language to another provides limited value...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Natural Is the Best: Model-Agnostic Code Simplification for Pre-trained Large Language Models](../venues/FSE2024/paper_17.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Pre-trained Large Language Models (LLM) have achieved remarkable successes in several domains. However, code-oriented LLMs are often heavy in computational complexity, and quadratically with the length of the input code sequence. Toward simplifying the input program of an LLM, the state-of-the-art approach has the strategies to filter the input code tokens based on the attention scores given by the LLM. The decision to simplify the input program should not rely on the attention patterns of an LL...
  - **Labels**: [static analysis](static_analysis.md), [code search](code_search.md), [code summarization](code_summarization.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Neural code comprehension: A learnable representation of code semantics](../venues/NeurIPS2018/paper_1.md), ([NeurIPS2018](../venues/NeurIPS2018/README.md))

  - **Abstract**: With the recent success of embeddings in natural language processing, research has been conducted into applying similar methods to code analysis. Most works attempt to process the code directly or use a syntactic tree representation, treating it like sentences written in a natural language. However, none of the existing methods are sufficient to comprehend program semantics robustly, due to structural features such as function calls, branching, and interchangeable order of statements. In this pa...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [On Calibration of Pre-trained Code Models](../venues/ICSE2024/paper_25.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Pre-trained code models have achieved notable success in the field of Software Engineering (SE). However, existing studies have predominantly focused on improving model performance, with limited attention given to other critical aspects such as model calibration. Model calibration, which refers to the accurate estimation of predictive uncertainty, is a vital consideration in practical applications. Therefore, in order to advance the understanding of model calibration in SE, we conduct a comprehe...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [On the Effectiveness of Transfer Learning for Code Search](../venues/TSE2023/paper_6.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: The Transformer architecture and transfer learning have marked a quantum leap in natural language processing, improving the state of the art across a range of text-based tasks. This paper examines how these advancements can be applied to and improve code search. To this end, we pre-train a BERT-based model on combinations of natural language and source code data and fine-tune it on pairs of StackOverflow question titles and code answers. Our results show that the pre-trained models consistently ...
  - **Labels**: [static analysis](static_analysis.md), [code search](code_search.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Personalized Distillation: Empowering Open-Sourced LLMs with Adaptive Learning for Code Generation](../venues/EMNLP2023/paper_2.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: With the rise of powerful closed-sourced LLMs (ChatGPT, GPT-4), there are increasing interests in distilling the capabilies of close-sourced LLMs to smaller open-sourced LLMs. Previous distillation methods usually prompt ChatGPT to generate a set of instructions and answers, for the student model to learn. However, such standard distillation approach neglects the merits and conditions of the student model. Inspired by modern teaching principles, we design a personalised distillation process, in ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Pre-training by Predicting Program Dependencies for Vulnerability Analysis Tasks](../venues/ICSE2024/paper_30.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Vulnerability analysis is crucial for software security. Inspired by the success of pre-trained models on software engineering tasks, this work focuses on using pre-training techniques to enhance the understanding of vulnerable code and boost vulnerability analysis. The code understanding ability of a pre-trained model is highly related to its pre-training objectives. The semantic structure, e.g., control and data dependencies, of code is important for vulnerability analysis. However, existing p...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning](../venues/FSE2024/paper_29.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Program slicing, the process of extracting program statements that influence values at a designated location (known as the slicing criterion), is helpful in both manual and automated debugging. However, such slicing techniques prove ineffective in scenarios where executing specific inputs is prohibitively expensive, or even impossible, as with partial code. In this paper, we introduce ND-Slicer, a predictive slicing methodology that caters to specific executions based on a particular input, over...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [ReCode: Robustness Evaluation of Code Generation Models](../venues/ACL2023/paper_13.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Code generation models have achieved impressive performance. However, they tend to be brittle as slight edits to a prompt could lead to very different generations; these robustness properties, critical for user experience when deployed in real-life applications, are not well understood. Most existing works on robustness in text or code tasks have focused on classification, while robustness in generation tasks is an uncharted area and to date there is no comprehensive benchmark for robustness in ...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [code model](code_model.md), [code model robustness](code_model_robustness.md)


- [Rethinking Code Refinement: Learning to Judge Code Efficiency](../venues/EMNLP2024/paper_12.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated impressive capabilities in understanding and generating codes. Due to these capabilities, many recent methods are proposed to automatically refine the codes with LLMs. However, we should rethink that the refined codes (from LLMs and even humans) are not always more efficient than their original versions. On the other hand, running two different versions of codes and comparing them every time is not ideal and time-consuming. Therefore, in this work, ...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [SemCoder: Training Code Language Models with Comprehensive Semantics](../venues/NeurIPS2024/paper_1.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Code Large Language Models (Code LLMs) have excelled at tasks like code completion but often miss deeper semantics such as execution effects and dynamic states. This paper aims to bridge the gap between Code LLMs' reliance on static text data and the need for semantic understanding for complex tasks like debugging and program repair. We introduce a novel strategy, monologue reasoning, to train Code LLMs to reason comprehensive semantics, encompassing high-level functional descriptions, local exe...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Smart-LLaMA-DPO: Reinforced Large Language Model for Explainable Smart Contract Vulnerability Detection](../venues/ISSTA2025/paper_4.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Smart contract vulnerability detection is a critical challenge in the rapidly evolving blockchain landscape. Existing vulnerability detection methods face two main issues: (1) Existing datasets lack comprehensiveness and sufficient quality, with limited vulnerability type coverage and insufficient distinction between high-quality and low-quality explanations for preference learning. (2) Large language models (LLMs) often struggle with accurately interpreting specific concepts in smart contract s...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Source Code Vulnerability Detection: Combining Code Language Models and Code Property Graphs](../venues/arXiv2024/paper_17.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Currently, deep learning successfully applies to code vulnerability detection by learning from code sequences or property graphs. However, sequence-based methods often overlook essential code attributes such as syntax, control flow, and data dependencies, whereas graph-based approaches might underestimate the semantics of code and face challenges in capturing long-distance contextual information.To address this gap, we propose Vul-LMGNN, a unified model that combines pre-trained code language mo...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Symmetry-Preserving Program Representations for Learning Code Semantics](../venues/ICML2024/paper_3.md), ([ICML2024](../venues/ICML2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have shown promise in automated program reasoning, a crucial aspect of many security tasks. However, existing LLM architectures for code are often borrowed from other domains like natural language processing, raising concerns about their generalization and robustness to unseen code. A key generalization challenge is to incorporate the knowledge of code semantics, including control and data flow, into the LLM architectures. Drawing inspiration from examples of convolu...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [The EarlyBIRD Catches the Bug: On Exploiting Early Layers of Encoder Models for More Efficient Code Classification](../venues/FSE2023/paper_12.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: The use of modern Natural Language Processing (NLP) techniques has shown to be beneficial for software engineering tasks, such as vulnerability detection and type inference. However, training deep NLP models requires significant computational resources. This paper explores techniques that aim at achieving the best usage of resources and available information in these models.  We propose a generic approach, EarlyBIRD, to build composite representations of code from the early layers of a pre-train...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)


- [Towards Efficient Fine-Tuning of Language Models With Organizational Data for Automated Software Review](../venues/TSE2024/paper_1.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Large language models like BERT and GPT possess significant capabilities and potential impacts across various applications. Software engineers often use these models for code-related tasks, including generating, debugging, and summarizing code. Nevertheless, large language models still have several flaws, including model hallucination. (e.g., generating erroneous code and producing outdated and inaccurate programs) and the substantial computational resources and energy required for training and ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Towards Low-Resource Automatic Program Repair with Meta-Learning and Pretrained Language Models](../venues/EMNLP2023/paper_15.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Automatic program repair (APR) has gained increasing attention as an essential technique in software development to reduce manual debugging efforts and boost developers’ productivity. Recent advances in deep learning (DL) based models have demonstrated promising results by learning from large-scale bug-fix examples in a data-driven manner. However, in practical scenarios, software bugs have an imbalanced distribution, and the fixing knowledge learned by APR models often only capture the patterns...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [UICoder: Finetuning Large Language Models to Generate User Interface Code through Automated Feedback](../venues/NAACL2024/paper_5.md), ([NAACL2024](../venues/NAACL2024/README.md))

  - **Abstract**: Many large language models (LLMs) struggle to consistently generate UI code that compiles and produces visually relevant designs. Existing approaches to improve generation rely either on expensive human feedback or distilling a proprietary model. In this paper, we explore the use of automated feedback (compilers and multi-modal models) to guide LLMs to generate high-quality UI code. Our method starts with an existing LLM and iteratively produces improved models by self-generating a large synthet...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Understanding Code Changes Practically with Small-Scale Language Models](../venues/ASE2024/paper_3.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Recent studies indicate that traditional techniques for understanding code changes are not as effective as techniques that directly prompt language models (LMs). However, current LM-based techniques heavily rely on expensive, large LMs (LLMs) such as GPT-4 and Llama-13b, which are either commercial or prohibitively costly to deploy on a wide scale, thereby restricting their practical applicability. This paper explores the feasibility of deploying small LMs (SLMs) while maintaining comparable or ...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Using Transfer Learning for Code-Related Tasks](../venues/TSE2023/paper_5.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: Deep learning (DL) techniques have been used to support several code-related tasks such as code summarization and bug-fixing. In particular, pre-trained transformer models are on the rise, also thanks to the excellent results they achieved in Natural Language Processing (NLP) tasks. The basic idea behind these models is to first pre-train them on a generic dataset using a self-supervised task (e.g., filling masked words in sentences). Then, these models are fine-tuned to support specific tasks o...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [VGX: Large-Scale Sample Generation for Boosting Learning-Based Software Vulnerability Analyses](../venues/ICSE2024/paper_29.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Accompanying the successes of learning-based defensive software vulnerability analyses is the lack of large and quality sets of labeled vulnerable program samples, which impedes further advancement of those defenses. Existing automated sample generation approaches have shown potentials yet still fall short of practical expectations due to the high noise in the generated samples. This paper proposes VGX, a new technique aimed for large-scale generation of high-quality vulnerability datasets. Give...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Virtual Compiler Is All You Need For Assembly Code Search](../venues/ACL2024/paper_11.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Assembly code search is vital for reducing the burden on reverse engineers, allowing them to quickly identify specific functions using natural language within vast binary programs.Despite its significance, this critical task is impeded by the complexities involved in building high-quality datasets. This paper explores training a Large Language Model (LLM) to emulate a general compiler. By leveraging Ubuntu packages to compile a dataset of 20 billion tokens, we further continue pre-train CodeLlam...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [static analysis](static_analysis.md), [code search](code_search.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [WaveCoder: Widespread And Versatile Enhancement For Code Large Language Models By Instruction Tuning](../venues/ACL2024/paper_17.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Recent work demonstrates that, after instruction tuning, Code Large Language Models (Code LLMs) can obtain impressive capabilities to address a wide range of code-related tasks. However, current instruction tuning methods for Code LLMs mainly focus on the traditional code generation task, resulting in poor performance in complex multi-task scenarios. In this paper, we concentrate on multiple code-related tasks and present WaveCoder, a series of Code LLMs trained with Widespread And Versatile Enh...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [XSemPLR: Cross-Lingual Semantic Parsing in Multiple Natural Languages and Meaning Representations](../venues/ACL2023/paper_6.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Cross-Lingual Semantic Parsing (CLSP) aims to translate queries in multiple natural languages (NLs) into meaning representations (MRs) such as SQL, lambda calculus, and logic forms. However, existing CLSP models are separately proposed and evaluated on datasets of limited tasks and applications, impeding a comprehensive and unified evaluation of CLSP on a diverse range of NLs and MRs. To this end, we present XSemPLR, a unified benchmark for cross-lingual semantic parsing featured with 22 natural...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Your Instructions Are Not Always Helpful: Assessing the Efficacy of Instruction Fine-tuning for Software Vulnerability Detection](../venues/arXiv2024/paper_18.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Software, while beneficial, poses potential cybersecurity risks due to inherent vulnerabilities. Detecting these vulnerabilities is crucial, and deep learning has shown promise as an effective tool for this task due to its ability to perform well without extensive feature engineering. However, a challenge in deploying deep learning for vulnerability detection is the limited availability of training data. Recent research highlights the deep learning efficacy in diverse tasks. This success is attr...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)
