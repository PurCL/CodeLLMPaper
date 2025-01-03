# ACL2024

Number of papers: 22

## [AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](paper_6.md)
- **Authors**: Trivedi, Harsh and Khot, Tushar and Hartmann, Mareike and Manku, Ruskin and Dong, Vinty and Li, Edward and Gupta, Shashank and Sabharwal, Ashish and Balasubramanian, Niranjan
- **Abstract**: Autonomous agents that address day-to-day digital tasks (e.g., ordering groceries for a household), must not only operate multiple apps (e.g., notes, messaging, shopping app) via APIs, but also generate rich code with complex control flow in an iterative manner based on their interaction with the environment. However, existing benchmarks for tool use are inadequate, as they only cover tasks that require a simple sequence of API calls. To remedy this gap, we built AppWorld Engine, a high-quality ...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.850)
- **Labels**: [benchmark](../../labels/benchmark.md), [agent design](../../labels/agent_design.md)


## [ArchCode: Incorporating Software Requirements in Code Generation with Large Language Models](paper_1.md)
- **Authors**: Han, Hojae and Kim, Jaejin and Yoo, Jaeseok and Lee, Youngwon and Hwang, Seung-won
- **Abstract**: This paper aims to extend the code generation capability of large language models (LLMs) to automatically manage comprehensive software requirements from given textual descriptions. Such requirements include both functional (i.e. achieving expected behavior for inputs) and non-functional (e.g., time/space performance, robustness, maintainability) requirements. However, textual descriptions can either express requirements verbosely or may even omit some of them. We introduce ARCHCODE, a novel fra...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.730)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [ChatDev: Communicative Agents for Software Development](paper_5.md)
- **Authors**: Qian, Chen and Liu, Wei and Liu, Hongzhang and Chen, Nuo and Dang, Yufan and Li, Jiahao and Yang, Cheng and Chen, Weize and Su, Yusheng and Cong, Xin and Xu, Juyuan and Li, Dahai and Liu, Zhiyuan and Sun, Maosong
- **Abstract**: Software development is a complex task that necessitates cooperation among multiple members with diverse skills. Numerous studies used deep learning to improve specific phases in a waterfall model, such as design, coding, and testing. However, the deep learning model in each phase requires unique designs, leading to technical inconsistencies across various phases, which results in a fragmented and ineffective development process. In this paper, we introduce ChatDev, a chat-powered software devel...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.810)
- **Labels**: [general coding task](../../labels/general_coding_task.md)


## [CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges](paper_3.md)
- **Authors**: Zhang, Kechi and Li, Jia and Li, Ge and Shi, Xianjie and Jin, Zhi
- **Abstract**: Large Language Models (LLMs) have shown promise in automated code generation but typically excel only in simpler tasks such as generating standalone code units. However, real-world software development often involves complex code repositories with complex dependencies and extensive documentation. To enable LLMs to handle these realworld repo-level code generation, we present CodeAgent, a novel LLM-based agent framework that employs external tools for effective repo-level code generation. CodeAge...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.737)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)


## [CodeScope: An Execution-based Multilingual Multitask Multidimensional Benchmark for Evaluating LLMs on Code Understanding and Generation](paper_18.md)
- **Authors**: Yan, Weixiang and Liu, Haitian and Wang, Yunkun and Li, Yunzhe and Chen, Qian and Wang, Wen and Lin, Tingyu and Zhao, Weishan and Zhu, Li and Sundaram, Hari and Deng, Shuiguang
- **Abstract**: Large Language Models (LLMs) have demonstrated remarkable performance on assisting humans in programming and facilitating programming automation. However, existing benchmarks for evaluating the code understanding and generation capacities of LLMs suffer from severe limitations. First, most benchmarks are insufficient as they focus on a narrow range of popular programming languages and specific tasks, whereas real-world software development scenarios show a critical need to implement systems with...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.301)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [benchmark](../../labels/benchmark.md)


## [DolphCoder: Echo-Locating Code Large Language Models with Diverse and Multi-Objective Instruction Tuning](paper_14.md)
- **Authors**: Wang, Yejie and He, Keqing and Dong, Guanting and Wang, Pei and Zeng, Weihao and Diao, Muxi and Xu, Weiran and Wang, Jingang and Zhang, Mengdi and Cai, Xunliang
- **Abstract**: Code Large Language Models (Code LLMs) have demonstrated outstanding performance in code-related tasks. Various instruction finetuning approaches have been proposed to boost the code generation performance of pre-trained Code LLMs. In this paper, we introduce a diverse instruction model DolphCoder with self-evaluating for code generation. It learns diverse instruction targets and combines a code evaluation objective to enhance its code generation ability. Our model achieves superior performance ...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.259)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [Enhancing Large Language Models in Coding Through Multi-Perspective Self-Consistency](paper_9.md)
- **Authors**: Huang, Baizhou and Lu, Shuai and Wan, Xiaojun and Duan, Nan
- **Abstract**: Large language models (LLMs) have exhibited remarkable ability in code generation. However, generating the correct solution in a single attempt still remains a challenge. Prior works utilize verification properties in software engineering to verify and re-rank solutions in a majority voting manner. But the assumption behind them that generated verification properties have better qualities than solutions may not always hold. In this paper, we treat them equally as different perspectives of LLMs’ ...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.78)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [Experiential Co-Learning of Software-Developing Agents](paper_19.md)
- **Authors**: Qian, Chen and Dang, Yufan and Li, Jiahao and Liu, Wei and Xie, Zihao and Wang, YiFei and Chen, Weize and Yang, Cheng and Cong, Xin and Che, Xiaoyin and Liu, Zhiyuan and Sun, Maosong
- **Abstract**: Recent advancements in large language models (LLMs) have brought significant changes to various domains, especially through LLM-driven autonomous agents. A representative scenario is in software development, where LLM agents demonstrate efficient collaboration, task division, and assurance of software quality, markedly reducing the need for manual involvement. However, these agents frequently perform a variety of tasks independently, without benefiting from past experiences, which leads to repea...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.305)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [agent design](../../labels/agent_design.md), [planning](../../labels/planning.md)


## [HiRoPE: Length Extrapolation for Code Models Using Hierarchical Position](paper_2.md)
- **Authors**: Zhang, Kechi and Li, Ge and Zhang, Huangzhao and Jin, Zhi
- **Abstract**: Addressing the limitation of context length in large language models for code-related tasks is the primary focus of this paper. Existing LLMs are constrained by their pre-trained context lengths, leading to performance issues in handling long complex code sequences. Inspired by how human programmers navigate code, we introduce Hierarchical Rotary Position Embedding (HiRoPE), a novel approach that enhances the traditional rotary position embedding into a hierarchical format based on the hierarchi...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.735)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [Integrate the Essence and Eliminate the Dross: Fine-Grained Self-Consistency for Free-Form Language Generation](paper_22.md)
- **Authors**: Wang, Xinglin and Li, Yiwei and Feng, Shaoxiong and Yuan, Peiwen and Pan, Boyuan and Wang, Heda and Hu, Yao and Li, Kan
- **Abstract**: Self-consistency (SC), leveraging multiple samples from LLMs, shows significant gains on various reasoning tasks but struggles with free-form generation due to the difficulty of aggregating answers. Its variants, UCS and USC, rely on sample selection or voting mechanisms to improve output quality. These methods, however, face limitations due to their inability to fully utilize the nuanced consensus knowledge present within multiple candidate samples, often resulting in suboptimal outputs. We pro...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.634)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [empirical study](../../labels/empirical_study.md)


## [Lightweight reranking for language model generations](paper_21.md)
- **Authors**: Jain, Siddhartha and Ma, Xiaofei and Deoras, Anoop and Xiang, Bing
- **Abstract**: Large Language Models (LLMs) can exhibit considerable variation in the quality of their sampled outputs. Reranking and selecting the best generation from the sampled set is a popular way of obtaining strong gains in generation quality. In this paper, we present a novel approach for reranking LLM generations. Unlike other techniques that might involve additional inferences or training a specialized reranker, our approach relies on easy to compute pairwise statistics between the generations that h...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.376)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [MPCoder: Multi-user Personalized Code Generator with Explicit and Implicit Style Representation Learning](paper_12.md)
- **Authors**: Dai, Zhenlong and Yao, Chang and Han, WenKang and Yuanying, Yuanying and Gao, Zhipeng and Chen, Jingyuan
- **Abstract**: Large Language Models (LLMs) have demonstrated great potential for assisting developers in their daily development. However, most research focuses on generating correct code, how to use LLMs to generate personalized code has seldom been investigated. To bridge this gap, we proposed MPCoder (Multi-user Personalized Code Generator) to generate personalized code for multiple users. To better learn coding style features, we utilize explicit coding style residual learning to capture the syntax code s...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.207)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [MapCoder: Multi-Agent Code Generation for Competitive Problem Solving](paper_16.md)
- **Authors**: Islam, Md. Ashraful and Ali, Mohammed Eunus and Parvez, Md Rizwan
- **Abstract**: Code synthesis, which requires a deep understanding of complex natural language (NL) problem descriptions, generation of code instructions for complex algorithms and data structures, and the successful execution of comprehensive unit tests, presents a significant challenge. Thus, while large language models (LLMs) demonstrate impressive proficiency in natural language processing (NLP), their performance in code generation tasks remains limited. In this paper, we introduce a new approach to code ...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.269)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [agent design](../../labels/agent_design.md)


## [On Improving Repository-Level Code QA for Large Language Models](paper_7.md)
- **Authors**: Strich, Jan and Schneider, Florian and Nikishina, Irina and Biemann, Chris
- **Abstract**: Large Language Models (LLMs) such as ChatGPT, GitHub Copilot, Llama, or Mistral assist programmers as copilots and knowledge sources to make the coding process faster and more efficient. This paper aims to improve the copilot performance by implementing different self-alignment processes and retrieval-augmented generation (RAG) pipelines, as well as their combination. To test the effectiveness of all approaches, we create a dataset and apply a model-based evaluation, using LLM as a judge. It is ...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-srw.28)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [benchmark](../../labels/benchmark.md)


## [Quantifying Contamination in Evaluating Code Generation Capabilities of Language Models](paper_4.md)
- **Authors**: Riddell, Martin and Ni, Ansong and Cohan, Arman
- **Abstract**: While large language models have achieved remarkable performance on various code generation benchmarks, there have been growing concerns regarding potential contamination of these benchmarks as they may be leaked into pretraining and finetuning data. While recent work has investigated contamination in natural language generation and understanding tasks, there has been less extensive research into how data contamination impacts the evaluation of code generation, which is critical for understandin...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.761)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [empirical study](../../labels/empirical_study.md)


## [Rewriting the Code: A Simple Method for Large Language Model Augmented Code Search](paper_8.md)
- **Authors**: Li, Haochen and Zhou, Xin and Shen, Zhiqi
- **Abstract**: In code search, the Generation-Augmented Retrieval (GAR) framework, which generates exemplar code snippets to augment queries, has emerged as a promising strategy to address the principal challenge of modality misalignment between code snippets and natural language queries, particularly with the demonstrated code generation capabilities of Large Language Models (LLMs). Nevertheless, our preliminary investigations indicate that the improvements conferred by such an LLM-augmented framework are som...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.75)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [empirical study](../../labels/empirical_study.md)


## [StepCoder: Improving Code Generation with Reinforcement Learning from Compiler Feedback](paper_13.md)
- **Authors**: Dou, Shihan and Liu, Yan and Jia, Haoxiang and Zhou, Enyu and Xiong, Limao and Shan, Junjie and Huang, Caishuang and Wang, Xiao and Fan, Xiaoran and Xi, Zhiheng and Zhou, Yuhao and Ji, Tao and Zheng, Rui and Zhang, Qi and Gui, Tao and Huang, Xuanjing
- **Abstract**: The advancement of large language models (LLMs) has significantly propelled the field of code generation. Previous work integrated reinforcement learning (RL) with compiler feedback for exploring the output space of LLMs to enhance code generation quality. However, the lengthy code generated by LLMs in response to complex human requirements makes RL exploration a challenge. Also, since the unit tests may not cover the complicated code, optimizing LLMs by using these unexecuted code snippets is i...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.251)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [UniCoder: Scaling Code Large Language Model via Universal Code](paper_10.md)
- **Authors**: Sun, Tao and Chai, Linzheng and Yang, Jian and Yin, Yuwei and Guo, Hongcheng and Liu, Jiaheng and Wang, Bing and Yang, Liqun and Li, Zhoujun
- **Abstract**: Intermediate reasoning or acting steps have successfully improved large language models (LLMs) for handling various downstream natural language processing (NLP) tasks.When applying LLMs for code generation, recent works mainly focus on directing the models to articulate intermediate natural-language reasoning steps, as in chain-of-thought (CoT) prompting, and then output code with the natural language or other structured intermediate steps. However, such output is not suitable for code translati...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.100)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [IR code model](../../labels/IR_code_model.md)


## [Virtual Compiler Is All You Need For Assembly Code Search](paper_11.md)
- **Authors**: Gao, Zeyu and Wang, Hao and Wang, Yuanda and Zhang, Chao
- **Abstract**: Assembly code search is vital for reducing the burden on reverse engineers, allowing them to quickly identify specific functions using natural language within vast binary programs.Despite its significance, this critical task is impeded by the complexities involved in building high-quality datasets. This paper explores training a Large Language Model (LLM) to emulate a general compiler. By leveraging Ubuntu packages to compile a dataset of 20 billion tokens, we further continue pre-train CodeLlam...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.167)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [WaveCoder: Widespread And Versatile Enhancement For Code Large Language Models By Instruction Tuning](paper_17.md)
- **Authors**: Yu, Zhaojian and Zhang, Xin and Shang, Ning and Huang, Yangyu and Xu, Can and Zhao, Yishujie and Hu, Wenxiang and Yin, Qiufeng
- **Abstract**: Recent work demonstrates that, after instruction tuning, Code Large Language Models (Code LLMs) can obtain impressive capabilities to address a wide range of code-related tasks. However, current instruction tuning methods for Code LLMs mainly focus on the traditional code generation task, resulting in poor performance in complex multi-task scenarios. In this paper, we concentrate on multiple code-related tasks and present WaveCoder, a series of Code LLMs trained with Widespread And Versatile Enh...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.280)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [Who Wrote this Code? Watermarking for Code Generation](paper_15.md)
- **Authors**: Lee, Taehyun and Hong, Seokhee and Ahn, Jaewoo and Hong, Ilgee and Lee, Hwaran and Yun, Sangdoo and Shin, Jamin and Kim, Gunhee
- **Abstract**: Since the remarkable generation performance of large language models raised ethical and legal concerns, approaches to detect machine-generated text by embedding watermarks are being developed.However, we discover that the existing works fail to function appropriately in code generation tasks due to the task’s nature of having low entropy.Extending a logit-modifying watermark method, we propose Selective WatErmarking via Entropy Thresholding (SWEET), which enhances detection ability and mitigates...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.268)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md)


## [XCodeEval: An Execution-based Large Scale Multilingual Multitask Benchmark for Code Understanding, Generation, Translation and Retrieval](paper_20.md)
- **Authors**: Khan, Mohammad Abdullah Matin and Bari, M. Saiful and Long, Do and Wang, Weishi and Parvez, Md Rizwan and Joty, Shafiq
- **Abstract**: Recently, pre-trained large language models (LLMs) have shown impressive abilities in generating codes from natural language descriptions, repairing buggy codes, translating codes between languages, and retrieving relevant code segments. However, the evaluation of these models has often been performed in a scattered way on only one or two specific tasks, in a few languages, at a partial granularity (e.g., function) level, and in many cases without proper training data. Even more concerning is th...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.367)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [benchmark](../../labels/benchmark.md)
