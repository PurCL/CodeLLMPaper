# Empirical Study

## Agent Design

- [Can GPT-4 Replicate Empirical Software Engineering Research?](../venues/FSE2024/paper_3.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Empirical software engineering research on production systems has brought forth a better understanding of the software engineering process for practitioners and researchers alike. However, only a small subset of production systems is studied, limiting the impact of this research. While software engineering practitioners could benefit from replicating research on their own data, this poses its own set of challenges, since performing replications requires a deep understanding of research methodolo...
  - **Labels**: [empirical study](empirical_study.md), [agent design](agent_design.md)

- [Complementary explanations for effective in-context learning](../venues/ACL2023/paper_7.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Large language models (LLMs) have exhibited remarkable capabilities in learning from explanations in prompts, but there has been limited understanding of exactly how these explanations function or why they are effective. This work aims to better understand the mechanisms by which explanations are used for in-context learning. We first study the impact of two different factors on the performance of prompts with explanations: the computation trace (the way the solution is decomposed) and the natur...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md), [empirical study](empirical_study.md)

- [Explanation selection using unlabeled data for chain-of-thought prompting](../venues/EMNLP2023/paper_14.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Recent work has shown how to prompt large language models with explanations to obtain strong performance on textual reasoning tasks, i.e., the chain-of-thought paradigm. However, subtly different explanations can yield widely varying downstream task accuracy. Explanations that have not been "tuned" for a task, such as off-the-shelf explanations written by nonexperts, may lead to mediocre performance. This paper tackles the problem of how to optimize explanation-infused prompts in a blackbox fash...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md), [empirical study](empirical_study.md)

- [Self-Planning Code Generation with Large Language Models](../venues/TOSEM2024/paper_2.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Although large language models (LLMs) have demonstrated impressive ability in code generation, they are still struggling to address the complicated intent provided by humans. It is widely acknowledged that humans typically employ planning to decompose complex problems and schedule solution steps prior to implementation. To this end, we introduce planning into code generation to help the model understand complex intent and reduce the difficulty of problem-solving. This paper proposes a self-plann...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [planning](planning.md), [empirical study](empirical_study.md)

- [When Do Program-of-Thought Works for Reasoning?](../venues/AAAI2024/paper_1.md), ([AAAI2024](../venues/AAAI2024/README.md))

  - **Abstract**: In the realm of embodied artificial intelligence, the reasoning capabilities of Large Language Models (LLMs) play a pivotal role. Although there are effective methods like program-of-thought prompting for LLMs which uses programming language to tackle complex reasoning tasks, the specific impact of code data on the improvement of reasoning capabilities remains under-explored. To address this gap, we propose complexity-impacted reasoning score CIRS, which combines structural and logical attribute...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md), [empirical study](empirical_study.md)

## Code Generation

- [A Closer Look at Different Difficulty Levels Code Generation Abilities of ChatGPT](../venues/ASE2023/paper_6.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Code generation aims to generate source code implementing human requirements illustrated with natural language specifications. With the rapid development of intelligent software engineering, automated code generation has become a hot research topic in both artificial intelligence and software engineering, and researchers have made significant achievements on code generation. More recently, large language models (LLMs) have demonstrated outstanding performance on code generation tasks, such as Ch...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [A Static Evaluation of Code Completion by Large Language Models](../venues/ACL2023/paper_12.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Large language models trained on code have shown great potential to increase productivity of software developers. Several execution-based benchmarks have been proposed to evaluate functional correctness of model-generated code on simple programming problems. Nevertheless, it is expensive to perform the same evaluation on complex real-world projects considering the execution cost. On the other hand, static analysis tools such as linters, which can detect errors without running the program, haven’...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)

- [An Empirical Study on Fine-Tuning Large Language Models of Code for Automated Program Repair](../venues/ASE2023/paper_2.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: The advent of large language models (LLMs) has opened up new opportunities for automated program repair (APR). In particular, some recent studies have explored how to leverage large language models of code (LLMCs) for program repair tasks and show promising results. However, most of them adopt the zero/few-shot learning paradigm for APR, which directly use LLMCs to generate the possibly correct code given its surrounding context. Though effective, the repair capabilities of LLMCs based on the fi...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)

- [Beyond Functional Correctness: Investigating Coding Style Inconsistencies in Large Language Models](../venues/FSE2025/paper_9.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Large language models (LLMs) have brought a paradigm shift to the field of code generation, offering the potential to enhance the software development process. However, previous research mainly focuses on the accuracy of code generation, while coding style differences between LLMs and human developers remain under-explored. In this paper, we empirically analyze the differences in coding style between the code generated by mainstream LLMs and the code written by human developers, and summarize co...
  - **Labels**: [code generation](code_generation.md), [empirical study](empirical_study.md)

- [Bridging Operator Semantic Inconsistencies: A Source-Level Cross-Framework Model Conversion Approach](../venues/FSE2025/paper_27.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: As deep learning (DL) frameworks become widely used, converting models between frameworks is crucial for ecosystem flexibility. However, interestingly, existing model converters commonly focus on syntactic operator API mapping—transpiling operator names and parameters—which results in API compatibility issues (i.e., incompatible parameters, missing operators). These issues arise from semantic inconsistencies due to differences in operator implementation, causing conversion failure or performance...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [empirical study](empirical_study.md)

- [Chain-of-Thought in Neural Code Generation: From and for Lightweight Language Models](../venues/TSE2024/paper_3.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated remarkable potential in code generation. The integration of Chain of Thought (CoT) reasoning can further boost their performance. However, current CoT methods often require manual writing or LLMs with over 100 billion parameters to generate, impeding their applicability in resource-constrained scenarios. In this study, we investigate lightweight Language Models (&lt;inline-formula&gt;&lt;tex-math notation="LaTeX"&gt;$ell$&lt;/tex-math&gt;&lt;alterna...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [Closing the Gap: A User Study on the Real-world Usefulness of AI-powered Vulnerability Detection & Repair in the IDE](../venues/ICSE2025/paper_1.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: This paper presents the first empirical study of a vulnerability detection and fix tool with professional software developers on real projects that they own. We implemented DeepVulGuard, an IDE-integrated tool based on state-of-the-art detection and fix models, and show that it has promising performance on benchmarks of historic vulnerability data. DeepVulGuard scans code for vulnerabilities (including identifying the vulnerability type and vulnerable region of code), suggests fixes, provides na...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)

- [Code4Struct: Code Generation for Few-Shot Event Structure Prediction](../venues/ACL2023/paper_8.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Large Language Model (LLM) trained on a mixture of text and code has demonstrated impressive capability in translating natural language (NL) into structured code. We observe that semantic structures can be conveniently translated into code and propose Code4Struct to leverage such text-to-structure translation capability to tackle structured prediction tasks. As a case study, we formulate Event Argument Extraction (EAE) as converting text into event-argument structures that can be represented as ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [ContractTinker: LLM-Empowered Vulnerability Repair for Real-World Smart Contracts](../venues/ASE2024/paper_35.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Smart contracts are susceptible to being exploited by attackers, especially when facing real-world vulnerabilities. To mitigate this risk, developers often rely on third-party audit services to identify potential vulnerabilities before project deployment. Nevertheless, repairing the identified vulnerabilities is still complex and laborintensive, particularly for developers lacking security expertise. Moreover, existing pattern-based repair tools mostly fail to address real-world vulnerabilities ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)

- [Demystifying Memorization in LLM-Based Program Repair via a General Hypothesis Testing Framework](../venues/FSE2025/paper_35.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have achieved remarkable success in various applications, particularly in code-related tasks such as code generation and program repair, setting new performance benchmarks. However, the extensive use of large training corpora raises concerns about whether these achievements stem from genuine understanding or mere memorization of training data—a question often overlooked in current research. This paper aims to study the memorization issue within LLM-based program repa...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)

- [Do Large Language Models Pay Similar Attention Like Human Programmers When Generating Code?](../venues/FSE2024/paper_11.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have recently been widely used for code generation. Due to the complexity and opacity of LLMs, little is known about how these models generate code. We made the first attempt to bridge this knowledge gap by investigating whether LLMs attend to the same parts of a task description as human programmers during code generation. An analysis of six LLMs, including GPT-4, on two popular code generation benchmarks revealed a consistent misalignment between LLMs' and programm...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [Evaluating In-Context Learning of Libraries for Code Generation](../venues/NAACL2024/paper_4.md), ([NAACL2024](../venues/NAACL2024/README.md))

  - **Abstract**: Contemporary Large Language Models (LLMs) exhibit a high degree of code generation and comprehension capability. A particularly promising area is their ability to interpret code modules from unfamiliar libraries for solving user-instructed tasks. Recent work has shown that large proprietary LLMs can learn novel library usage in-context from demonstrations. These results raise several open questions: whether demonstrations of library usage is required, whether smaller (and more open) models also ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [Evaluating and Improving ChatGPT for Unit Test Generation](../venues/FSE2024/paper_7.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Unit testing plays an essential role in detecting bugs in functionally-discrete program units (e.g., methods). Manually writing high-quality unit tests is time-consuming and laborious. Although the traditional techniques are able to generate tests with reasonable coverage, they are shown to exhibit low readability and still cannot be directly adopted by developers in practice. Recent work has shown the large potential of large language models (LLMs) in unit test generation. By being pre-trained ...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md), [code generation](code_generation.md)

- [Exploring and Unleashing the Power of Large Language Models in Automated Code Translation](../venues/FSE2024/paper_6.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Code translation tools, namely transpilers, are developed for automatic source-to-source translation. Latest learning-based transpilers have shown impressive enhancement against rule-based counterparts in both translation accuracy and readability, owing to their task-specific pre-training on extensive monolingual corpora. Nevertheless, their current performance still remains unsatisfactory for practical deployment, and the associated training resources are also prohibitively expensive. Large Lan...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [code model](code_model.md), [code model training](code_model_training.md), [empirical study](empirical_study.md)

- [Grounded Copilot: How Programmers Interact with Code-Generating Models](../venues/OOPLSA2023/paper_1.md), ([OOPLSA2023](../venues/OOPLSA2023/README.md))

  - **Abstract**: Powered by recent advances in code-generating models, AI assistants like Github Copilot promise to change the face of programming forever. But what is this new face of programming? We present the first grounded theory analysis of how programmers interact with Copilot, based on observing 20 participants—with a range of prior experience using the assistant—as they solve diverse programming tasks across four languages. Our main finding is that interactions with programming assistants are bimodal: i...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)

- [How Do Humans Write Code? Large Models Do It the Same Way Too](../venues/EMNLP2024/paper_20.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Program-of-Thought (PoT) replaces natural language-based Chain-of-Thought (CoT) as the most popular method in Large Language Models (LLMs) mathematical reasoning tasks by utilizing external tool calls to circumvent computational errors. However, our evaluation of the GPT-4 and Llama series reveals that using PoT introduces more reasoning errors, such as incorrect formulas or flawed logic, compared to CoT. To address this issue, we propose Human-Think Language (HTL), which leverages a suite of st...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [HumanEvo: An Evolution-Aware Benchmark for More Realistic Evaluation of Repository-Level Code Generation](../venues/ICSE2025/paper_62.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: To evaluate the repository-level code generation capabilities of Large Language Models (LLMs) in complex real-world software development scenarios, many evaluation methods have been developed. These methods typically leverage contextual code from the latest version of a project to assist LLMs in accurately generating the desired function. However, such evaluation methods fail to consider the dynamic evolution of software projects over time, which we refer to as evolution-ignored settings. This i...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md), [benchmark](benchmark.md)

- [Impeding LLM-assisted Cheating in Introductory Programming Assignments via Adversarial Perturbation](../venues/EMNLP2024/paper_16.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: While Large language model (LLM)-based programming assistants such as CoPilot and ChatGPT can help improve the productivity of professional software developers, they can also facilitate cheating in introductory computer programming courses. Assuming instructors have limited control over the industrial-strength models, this paper investigates the baseline performance of 5 widely used LLMs on a collection of introductory programming problems, examines adversarial perturbations to degrade their per...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [Investigating the Transferability of Code Repair for Low-Resource Programming Languages](../venues/NAACL2025/paper_2.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Large language models (LLMs) have shown remarkable performance on code generation tasks. A recent use case is iterative code repair, where an LLM fixes an incorrect program by rationalizing about errors and generating new code. Recent works augment the code repair process by integrating modern techniques such as chain-of-thought reasoning or distillation, but only study their benefits on high-resource languages like Python, and ignore low-resource languages like Perl. To address this gap of know...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)

- [LLM Hallucinations in Practical Code Generation: Phenomena, Mechanism, and Mitigation](../venues/ISSTA2025/paper_7.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Code generation aims to automatically generate code from input requirements, significantly enhancing development efficiency. Recent large language models (LLMs) based approaches have shown promising results and revolutionized code generation task. Despite the promising performance, LLMs often generate contents with hallucinations, especially for the code generation scenario requiring the handling of complex contextual dependencies in practical development process. Although previous study has ana...
  - **Labels**: [code generation](code_generation.md), [hallucination in reasoning](hallucination_in_reasoning.md), [empirical study](empirical_study.md)

- [LLM-Based Test-Driven Interactive Code Generation: User Study and Empirical Evaluation](../venues/TSE2024/paper_2.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Large language models (LLMs) have shown great potential in automating significant aspects of coding by producing natural code from informal natural language (NL) intent. However, given NL is informal, it does not lend easily to checking that the generated code correctly satisfies the user intent. In this paper, we propose a novel interactive workflow &lt;sc&gt;TiCoder&lt;/sc&gt; for guided intent clarification (i.e., partial formalization) through tests to support the generation of more accurate...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?): A Comprehensive Evaluation, Framework, and Benchmarks](../venues/S&P2024/paper_1.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have been suggested for use in automated vulnerability repair, but benchmarks showing they can consistently identify security-related bugs are lacking. We thus develop SecLLMHolmes, a fully automated evaluation framework that performs the most detailed investigation to date on whether LLMs can reliably identify and reason about security-related bugs. We construct a set of 228 code scenarios and analyze eight of the most capable LLMs across eight different investigati...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)

- [Licoeval: Evaluating LLMs on License Compliance in Code Generation](../venues/ICSE2025/paper_23.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Recent advances in Large Language Models (LLMs) have revolutionized code generation, leading to widespread adoption of AI coding tools by developers. However, LLMs can generate license-protected code without providing the necessary license information, leading to potential intellectual property violations during software production. This paper addresses the critical, yet underexplored, issue of license compliance in LLM-generated code by establishing a benchmark to evaluate the ability of LLMs t...
  - **Labels**: [empirical study](empirical_study.md), [code generation](code_generation.md)

- [Lost at C: a user study on the security implications of large language model code assistants](../venues/USENIXSec2023/paper_1.md), ([USENIXSec2023](../venues/USENIXSec2023/README.md))

  - **Abstract**: Large Language Models (LLMs) such as OpenAI Codex are increasingly being used as AI-based coding assistants. Understanding the impact of these tools on developers' code is paramount, especially as recent work showed that LLMs may suggest cybersecurity vulnerabilities. We conduct a security-driven user study (N=58) to assess code written by student programmers when assisted by LLMs. Given the potential severity of low-level bugs as well as their relative frequency in real-world projects, we taske...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [Lost in Translation: A Study of Bugs Introduced by Large Language Models while Translating Code](../venues/ICSE2024/paper_10.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Code translation aims to convert source code from one programming language (PL) to another. Given the promising abilities of large language models (LLMs) in code synthesis, researchers are exploring their potential to automate code translation. The prerequisite for advancing the state of LLM-based code translation is to understand their promises and limitations over existing techniques. To that end, we present a large-scale empirical study to investigate the ability of general LLMs and code LLMs...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [empirical study](empirical_study.md)

- [Mining Action Rules for Defect Reduction Planning](../venues/FSE2024/paper_12.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Defect reduction planning plays a vital role in enhancing software quality and minimizing software maintenance costs. By training a black box machine learning model and “explaining” its predictions, explainable AI for software engineering aims to identify the code characteristics that impact maintenance risks. However, post-hoc explanations do not always faithfully reflect what the original model computes. In this paper, we introduce CounterACT, a Counterfactual ACTion rule mining approach that ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)

- [No Need to Lift a Finger Anymore? Assessing the Quality of Code Generation by ChatGPT](../venues/TSE2024/paper_6.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated impressive capabilities across various natural language processing (NLP) tasks, such as machine translation, question answering, summarization, and so on. Additionally, LLMs are also highly valuable in supporting software engineering tasks, particularly in the field of code generation. Automatic code generation is a process of automatically generating source code or executable code based on given specifications or requirements, improving developer p...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [On the Evaluation of Neural Code Translation: Taxonomy and Benchmark](../venues/ASE2023/paper_14.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: In recent years, neural code translation has gained increasing attention. While most of the research focuses on improving model architectures and training processes, we notice that the evaluation process and benchmark for code translation models are severely limited: they primarily treat source code as natural languages and provide a holistic accuracy score while disregarding the full spectrum of model capabilities across different translation types and complexity. In this paper, we present a co...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)

- [Out of Context: How important is Local Context in Neural Program Repair?](../venues/ICSE2024/paper_27.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Deep learning source code models have been applied very successfully to the problem of automated program repair. One of the standing issues is the small input window of current models which often cannot fully fit the context code required for a bug fix (e.g., method or class declarations of a project). Instead, input is often restricted to the local context, that is, the lines below and above the bug location. In this work we study the importance of this local context on repair success: how much...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)

- [PTD-SQL: Partitioning and Targeted Drilling with LLMs in Text-to-SQL](../venues/EMNLP2024/paper_19.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have emerged as powerful tools for Text-to-SQL tasks, exhibiting remarkable reasoning capabilities. Different from tasks such as math word problem and commonsense reasoning, SQL solutions have a relatively fixed pattern. This facilitates the investigation of whether LLMs can benefit from categorical thinking, mirroring how humans acquire knowledge through inductive reasoning based on comparable examples. In this study, we propose that employing query group partitioni...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [Programming Assistant for Exception Handling with CodeBERT](../venues/ICSE2024/paper_13.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: With practical code reuse, the code fragments from developers' forums often migrate to applications. Owing to the incomplete nature of such fragments, they often lack the details on exception handling. The adaptation for exception handling to the codebase is not trivial as developers must learn and memorize what API methods could cause exceptions and what exceptions need to be handled. We propose Neurex, an exception handling recommender that learns from complete code, and accepts a given Java c...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)

- [Quantifying Contamination in Evaluating Code Generation Capabilities of Language Models](../venues/ACL2024/paper_4.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: While large language models have achieved remarkable performance on various code generation benchmarks, there have been growing concerns regarding potential contamination of these benchmarks as they may be leaked into pretraining and finetuning data. While recent work has investigated contamination in natural language generation and understanding tasks, there has been less extensive research into how data contamination impacts the evaluation of code generation, which is critical for understandin...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [Revisiting the Impact of Pursuing Modularity for Code Generation](../venues/EMNLP2024/paper_13.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Modular programming, which aims to construct the final program by integrating smaller, independent building blocks, has been regarded as a desirable practice in software development. However, with the rise of recent code generation agents built upon large language models (LLMs), a question emerges: is this traditional practice equally effective for these new tools? In this work, we assess the impact of modularity in code generation by introducing a novel metric for its quantitative measurement. ...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [Rewriting the Code: A Simple Method for Large Language Model Augmented Code Search](../venues/ACL2024/paper_8.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: In code search, the Generation-Augmented Retrieval (GAR) framework, which generates exemplar code snippets to augment queries, has emerged as a promising strategy to address the principal challenge of modality misalignment between code snippets and natural language queries, particularly with the demonstrated code generation capabilities of Large Language Models (LLMs). Nevertheless, our preliminary investigations indicate that the improvements conferred by such an LLM-augmented framework are som...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)

- [Self-Planning Code Generation with Large Language Models](../venues/TOSEM2024/paper_2.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Although large language models (LLMs) have demonstrated impressive ability in code generation, they are still struggling to address the complicated intent provided by humans. It is widely acknowledged that humans typically employ planning to decompose complex problems and schedule solution steps prior to implementation. To this end, we introduce planning into code generation to help the model understand complex intent and reduce the difficulty of problem-solving. This paper proposes a self-plann...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [planning](planning.md), [empirical study](empirical_study.md)

- [Socratic Human Feedback (SoHF): Expert Steering Strategies for LLM Code Generation](../venues/EMNLP2024/paper_21.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large Language Models (LLMs) are increasingly used for generating code solutions, empowered by features like self-debugging and self-reflection. However, LLMs often struggle with complex programming problems without human guidance. This paper investigates the strategies employed by expert programmers to steer code-generating LLMs toward successful outcomes. Through a study involving experts using natural language to guide GPT-4, Gemini Ultra, and, Claude 3.5 Sonnet on highly difficult programmin...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [Statically Contextualizing Large Language Models with Typed Holes](../venues/OOPSLA2024/paper_1.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Large language models (LLMs) have reshaped the landscape of program synthesis. However, contemporary LLM-based code completion systems often hallucinate broken code because they lack appropriate code context, particularly when working with definitions that are neither in the training data nor near the cursor. This paper demonstrates that tighter integration with the type and binding structure of the programming language in use, as exposed by its language server, can help address this contextuali...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [The Best of Both Worlds: Combining Learned Embeddings with Engineered Features for Accurate Prediction of Correct Patches](../venues/TOSEM2023/paper_2.md), ([TOSEM2023](../venues/TOSEM2023/README.md))

  - **Abstract**: A large body of the literature on automated program repair develops approaches where patches are automatically generated to be validated against an oracle (e.g., a test suite). Because such an oracle can be imperfect, the generated patches, although validated by the oracle, may actually be incorrect. While the state-of-the-art explores research directions that require dynamic information or rely on manually-crafted heuristics, we study the benefit of learning code representations in order to lea...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)

- [Towards Greener Yet Powerful Code Generation via Quantization: An Empirical Study](../venues/FSE2023/paper_8.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: ML-powered code generation aims to assist developers to write code in a more productive manner by intelligently generating code blocks based on natural language prompts. Recently, large pretrained deep learning models have pushed the boundary of code generation and achieved impressive performance. However, the huge number of model parameters poses a significant challenge to their adoption in a typical software development environment, where a developer might use a standard laptop or mid-size ser...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [Towards Neural Synthesis for SMT-Assisted Proof-Oriented Programming](../venues/ICSE2025/paper_7.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Proof-oriented programs mix computational content with proofs of program correctness. However, the human effort involved in programming and proving is still substantial, despite the use of Satisfiability Modulo Theories (SMT) solvers to automate proofs in languages such as F*. Seeking to spur research on using AI to automate the construction of proof-oriented programs, we curate a dataset of 600K lines of open-source F* programs and proofs, including software used in production systems ranging f...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [Towards Understanding the Characteristics of Code Generation Errors Made by Large Language Models](../venues/ICSE2025/paper_53.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated unprecedented capabilities in code generation. However, there remains a limited understanding of code generation errors that LLMs can produce. To bridge the gap, we conducted an in-depth analysis of code generation errors across six representative LLMs on the HumanEval dataset. Specifically, we first employed open coding and thematic analysis to distill a comprehensive taxonomy of code generation errors. We analyzed two dimensions of error character...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [empirical study](empirical_study.md)

- [TransLLaMa: LLM-based Simultaneous Translation System](../venues/EMNLP2024/paper_1.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Decoder-only large language models (LLMs) have recently demonstrated impressive capabilities in text generation and reasoning. Nonetheless, they have limited applications in simultaneous machine translation (SiMT), currently dominated by encoder-decoder transformers. This study demonstrates that, after fine-tuning on a small dataset comprising causally aligned source and target sentence pairs, a pre-trained open-source LLM can control input segmentation directly by generating a special “wait” to...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [empirical study](empirical_study.md)

- [Unseen Horizons: Unveiling the Real Capability of LLM Code Generation Beyond the Familiar](../venues/ICSE2025/paper_25.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Recently, large language models (LLMs) have shown strong potential in code generation tasks. However, there are still gaps before they can be fully applied in actual software development processes. Accurately assessing the code generation capabilities of large language models has become an important basis for evaluating and improving the models. Some existing works have constructed datasets to evaluate the capabilities of these models. However, the current evaluation process may encounter the il...
  - **Labels**: [code generation](code_generation.md), [empirical study](empirical_study.md)

- [When Neural Code Completion Models Size up the Situation: Attaining Cheaper and Faster Completion through Dynamic Model Inference](../venues/ICSE2024/paper_7.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Leveraging recent advancements in large language models, modern neural code completion models have demonstrated the capability to generate highly accurate code suggestions. However, their massive size poses challenges in terms of computational costs and environmental impact, hindering their widespread adoption in practical scenarios. Dynamic inference emerges as a promising solution, as it allocates minimal computation during inference while maintaining the model's performance. In this research,...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)

## Code Model

- [An Empirical Study on Automatically Detecting AI-Generated Source Code: How Far are We?](../venues/ICSE2025/paper_24.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Artificial Intelligence (AI) techniques, especially Large Language Models (LLMs), have started gaining popularity among researchers and software developers for generating source code. However, LLMs have been shown to generate code with quality issues and also incurred copyright/licensing infringements. Therefore, detecting whether a piece of source code is written by humans or AI has become necessary. This study first presents an empirical analysis to investigate the effectiveness of the existin...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [empirical study](empirical_study.md)

- [An Extensive Study on Adversarial Attack against Pre-trained Models of Code](../venues/FSE2023/paper_11.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Transformer-based pre-trained models of code (PTMC) have been widely utilized and have achieved state-of-the-art performance in many mission-critical applications. However, they can be vulnerable to adversarial attacks through identifier substitution or coding style transformation, which can significantly degrade accuracy and may further incur security concerns. Although several approaches have been proposed to generate adversarial examples for PTMC, the effectiveness and efficiency of such appr...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [empirical study](empirical_study.md)

- [An investigation into misuse of java security apis by large language models](../venues/ASIACCS2024/paper_1.md), ([ASIACCS2024](../venues/ASIACCS2024/README.md))

  - **Abstract**: The increasing trend of using Large Language Models (LLMs) for code generation raises the question of their capability to generate trustworthy code. While many researchers are exploring the utility of code generation for uncovering software vulnerabilities, one crucial but often overlooked aspect is the security Application Programming Interfaces (APIs). APIs play an integral role in upholding software security, yet effectively integrating security APIs presents substantial challenges. This lead...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [empirical study](empirical_study.md)

- [AutoDetect: Towards a Unified Framework for Automated Weakness Detection in Large Language Models](../venues/EMNLP2024/paper_8.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Although Large Language Models (LLMs) are becoming increasingly powerful, they still exhibit significant but subtle weaknesses, such as mistakes in instruction-following or coding tasks.As these unexpected errors could lead to severe consequences in practical deployments, it is crucial to investigate the limitations within LLMs systematically.Traditional benchmarking approaches cannot thoroughly pinpoint specific model deficiencies, while manual inspections are costly and not scalable. In this p...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [empirical study](empirical_study.md)

- [Automating Code-Related Tasks Through Transformers: The Impact of Pre-Training](../venues/ICSE2023/paper_9.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Transformers have gained popularity in the software engineering (SE) literature. These deep learning models are usually pre-trained through a self-supervised objective, meant to provide the model with basic knowledge about a language of interest (e.g., Java). A classic pre-training objective is the masked language model (MLM), in which a percentage of tokens from the input (e.g., a Java method) is masked, with the model in charge of predicting them. Once pre-trained, the model is then fine-tuned...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)

- [Code Red! On the Harmfulness of Applying Off-the-Shelf Large Language Models to Programming Tasks](../venues/FSE2025/paper_32.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Nowadays, developers increasingly rely on solutions powered by Large Language Models (LLM) to assist them with their coding tasks. This makes it crucial to align these tools with human values to prevent malicious misuse.   In this paper,   we propose a comprehensive framework   for assessing the potential harmfulness   of LLMs within the software engineering domain.   We begin by developing a taxonomy of potentially harmful software engineering scenarios  and subsequently, create a dataset of pr...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [empirical study](empirical_study.md)

- [Dependency-Aware Code Naturalness](../venues/OOPSLA2024/paper_8.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Code naturalness, which captures repetitiveness and predictability in programming languages, has proven valuable for various code-related tasks in software engineering. However, precisely measuring code naturalness remains a fundamental challenge. Existing methods measure code naturalness over individual lines of code while ignoring the deep semantic relations among different lines, e.g., program dependency, which may negatively affect the precision of the measure. Despite the intuitive appeal o...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [empirical study](empirical_study.md)

- [Exploring Distributional Shifts in Large Language Models for Code Analysis](../venues/EMNLP2023/paper_11.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: We systematically study how three large language models with code capabilities - CodeT5, Codex, and ChatGPT - generalize to out-of-domain data. We consider two fundamental applications - code summarization, and code generation. We split data into domains following its natural boundaries - by an organization, by a project, and by a module within the software project. We establish that samples from each new domain present all the models with a significant challenge of distribution shift. We study ...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)

- [Exploring and Unleashing the Power of Large Language Models in Automated Code Translation](../venues/FSE2024/paper_6.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Code translation tools, namely transpilers, are developed for automatic source-to-source translation. Latest learning-based transpilers have shown impressive enhancement against rule-based counterparts in both translation accuracy and readability, owing to their task-specific pre-training on extensive monolingual corpora. Nevertheless, their current performance still remains unsatisfactory for practical deployment, and the associated training resources are also prohibitively expensive. Large Lan...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [code model](code_model.md), [code model training](code_model_training.md), [empirical study](empirical_study.md)

- [LLMs: Understanding Code Syntax and Semantics for Code Analysis](../venues/arXiv2023/paper_1.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Large language models~(LLMs) demonstrate significant potential to revolutionize software engineering (SE) by exhibiting outstanding performance in SE tasks such as code and document generation. However, the high reliability and risk control requirements in software engineering raise concerns about the lack of interpretability of LLMs. To address this concern, we conducted a study to evaluate the capabilities of LLMs and their limitations for code analysis in SE. We break down the abilities neede...
  - **Labels**: [static analysis](static_analysis.md), [data-flow analysis](data-flow_analysis.md), [call graph analysis](call_graph_analysis.md), [data-flow analysis](data-flow_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)

- [Model Editing for LLMs4Code: How Far are we?](../venues/ICSE2025/paper_21.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large Language Models for Code (LLMs4Code) have been found to exhibit outstanding performance in the software engineering domain, especially the remarkable performance in coding tasks. However, even the most advanced LLMs4Code can inevitably contain incorrect or outdated code knowledge. Due to the high cost of training LLMs4Code, it is impractical to re-train the models for fixing these problematic code knowledge. Model editing is a new technical field for effectively and efficiently correcting ...
  - **Labels**: [code model](code_model.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [The EarlyBIRD Catches the Bug: On Exploiting Early Layers of Encoder Models for More Efficient Code Classification](../venues/FSE2023/paper_12.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: The use of modern Natural Language Processing (NLP) techniques has shown to be beneficial for software engineering tasks, such as vulnerability detection and type inference. However, training deep NLP models requires significant computational resources. This paper explores techniques that aim at achieving the best usage of resources and available information in these models.  We propose a generic approach, EarlyBIRD, to build composite representations of code from the early layers of a pre-train...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)

## General Coding Task

- [Automatic Programming: Large Language Models and Beyond](../venues/arXiv2024/paper_12.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Automatic programming has seen increasing popularity due to the emergence of tools like GitHub Copilot which rely on Large Language Models (LLMs). At the same time, automatically generated code faces challenges during deployment due to concerns around quality and trust. In this article, we study automated coding in a general sense and study the concerns around code quality, security and related issues of programmer responsibility. These are key issues for organizations while deciding on the usag...
  - **Labels**: [general coding task](general_coding_task.md), [empirical study](empirical_study.md)

- [Automating Code-Related Tasks Through Transformers: The Impact of Pre-Training](../venues/ICSE2023/paper_9.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Transformers have gained popularity in the software engineering (SE) literature. These deep learning models are usually pre-trained through a self-supervised objective, meant to provide the model with basic knowledge about a language of interest (e.g., Java). A classic pre-training objective is the masked language model (MLM), in which a percentage of tokens from the input (e.g., a Java method) is masked, with the model in charge of predicting them. Once pre-trained, the model is then fine-tuned...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)

- [Codemind: A framework to challenge large language models for code reasoning](../venues/arXiv2024/paper_6.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Solely relying on test passing to evaluate Large Language Models (LLMs) for code synthesis may result in unfair assessment or promoting models with data leakage. As an alternative, we introduce CodeMind, a framework designed to gauge the code reasoning abilities of LLMs. CodeMind currently supports three code reasoning tasks: Independent Execution Reasoning (IER), Dependent Execution Reasoning (DER), and Specification Reasoning (SR). The first two evaluate models to predict the execution output ...
  - **Labels**: [general coding task](general_coding_task.md), [empirical study](empirical_study.md)

- [Exploring Distributional Shifts in Large Language Models for Code Analysis](../venues/EMNLP2023/paper_11.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: We systematically study how three large language models with code capabilities - CodeT5, Codex, and ChatGPT - generalize to out-of-domain data. We consider two fundamental applications - code summarization, and code generation. We split data into domains following its natural boundaries - by an organization, by a project, and by a module within the software project. We establish that samples from each new domain present all the models with a significant challenge of distribution shift. We study ...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)

- [Integrate the Essence and Eliminate the Dross: Fine-Grained Self-Consistency for Free-Form Language Generation](../venues/ACL2024/paper_22.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Self-consistency (SC), leveraging multiple samples from LLMs, shows significant gains on various reasoning tasks but struggles with free-form generation due to the difficulty of aggregating answers. Its variants, UCS and USC, rely on sample selection or voting mechanisms to improve output quality. These methods, however, face limitations due to their inability to fully utilize the nuanced consensus knowledge present within multiple candidate samples, often resulting in suboptimal outputs. We pro...
  - **Labels**: [general coding task](general_coding_task.md), [empirical study](empirical_study.md)

- [Mastering the Craft of Data Synthesis for {C}ode{LLM}s](../venues/NAACL2025/paper_10.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Large language models (LLMs) have shown impressive performance in \textit{code} understanding and generation, making coding tasks a key focus for researchers due to their practical applications and value as a testbed for LLM evaluation. Data synthesis and filtering techniques have been widely adopted and shown to be highly effective in this context. In this paper, we present a focused survey and taxonomy of these techniques, emphasizing recent advancements. We highlight key challenges, explore f...
  - **Labels**: [general coding task](general_coding_task.md), [empirical study](empirical_study.md)

## Hallucination In Reasoning

- [Deceptive Semantic Shortcuts on Reasoning Chains: How Far Can Models Go without Hallucination?](../venues/NAACL2024/paper_6.md), ([NAACL2024](../venues/NAACL2024/README.md))

  - **Abstract**: Despite the high performances of large language models (LLMs) across numerous benchmarks, recent research has unveiled their suffering from hallucinations and unfaithful reasoning. This work studies a type of hallucination induced by semantic associations. We investigate to what extent LLMs take shortcuts from certain keyword/entity biases in the prompt instead of following correct reasoning paths. To quantify this phenomenon, we propose a novel probing method and benchmark called EUREQA. EUREQA...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [empirical study](empirical_study.md)

- [Gsm-symbolic: Understanding the limitations of mathematical reasoning in large language models](../venues/Apple2024/paper_1.md), ([Apple2024](../venues/Apple2024/README.md))

  - **Abstract**: Recent advancements in Large Language Models (LLMs) have sparked interest in their formal reasoning capabilities, particularly in mathematics. The GSM8K benchmark is widely used to assess the mathematical reasoning of models on grade-school-level questions. While the performance of LLMs on GSM8K has significantly improved in recent years, it remains unclear whether their mathematical reasoning capabilities have genuinely advanced, raising questions about the reliability of the reported metrics. ...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [empirical study](empirical_study.md)

- [LLM Hallucinations in Practical Code Generation: Phenomena, Mechanism, and Mitigation](../venues/ISSTA2025/paper_7.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Code generation aims to automatically generate code from input requirements, significantly enhancing development efficiency. Recent large language models (LLMs) based approaches have shown promising results and revolutionized code generation task. Despite the promising performance, LLMs often generate contents with hallucinations, especially for the code generation scenario requiring the handling of complex contextual dependencies in practical development process. Although previous study has ana...
  - **Labels**: [code generation](code_generation.md), [hallucination in reasoning](hallucination_in_reasoning.md), [empirical study](empirical_study.md)

- [Self-contradictory hallucinations of large language models: Evaluation, detection and mitigation](../venues/ICLR2024/paper_8.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Large language models (large LMs) are susceptible to producing text that contains hallucinated content. An important instance of this problem is self-contradiction, where the LM generates two contradictory sentences within the same context. In this work, we present a comprehensive investigation into self-contradiction for various instruction-tuned LMs, covering evaluation, detection, and mitigation. Our primary evaluation task is open-domain text generation, but we also demonstrate the applicabi...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [empirical study](empirical_study.md)

## Program Testing

- [A Large-Scale Empirical Study on Fine-Tuning Large Language Models for Unit Testing](../venues/ISSTA2025/paper_26.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Unit testing plays a pivotal role in software development, improving software quality and reliability. However, generating effective test cases manually is time-consuming, prompting interest in unit testing research.   Recently, Large Language Models (LLMs) have shown potential in various unit testing tasks, including test generation, assertion generation, and test evolution, but existing studies are limited in scope and lack a systematic evaluation of the effectiveness of LLMs.    To bridge thi...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md)

- [An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation](../venues/TSE2024/paper_10.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Unit tests play a key role in ensuring the correctness of software. However, manually creating unit tests is a laborious task, motivating the need for automation. Large Language Models (LLMs) have recently been applied to various aspects of software development, including their suggested use for automated generation of unit tests, but while requiring additional training or few-shot learning on examples of existing tests. This paper presents a large-scale empirical evaluation on the effectiveness...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md)

- [ChatGPT vs SBST: A Comparative Assessment of Unit Test Suite Generation](../venues/TSE2024/paper_5.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Recent advancements in large language models (LLMs) have demonstrated exceptional success in a wide range of general domain tasks, such as question answering and following instructions. Moreover, LLMs have shown potential in various software engineering applications. In this study, we present a systematic comparison of test suites generated by the ChatGPT LLM and the state-of-the-art SBST tool EvoSuite. Our comparison is based on several critical factors, including correctness, readability, code...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md)

- [Doc2OracLL: Investigating the Impact of Documentation on LLM-Based Test Oracle Generation](../venues/FSE2025/paper_23.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Code documentation is a critical artifact of software development, bridging human understanding and machine-   readable code. Beyond aiding developers in code comprehension and maintenance, documentation also plays   a critical role in automating various software engineering tasks, such as test oracle generation (TOG). In Java,   Javadoc comments offer structured, natural language documentation embedded directly within the source   code, typically describing functionality, usage, parameters, ret...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md), [empirical study](empirical_study.md)

- [Evaluating Diverse Large Language Models for Automatic and General Bug Reproduction](../venues/TSE2024/paper_13.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Bug reproduction is a critical developer activity that is also challenging to automate, as bug reports are often in natural language and thus can be difficult to transform to test cases consistently. As a result, existing techniques mostly focused on crash bugs, which are easier to automatically detect and verify. In this work, we overcome this limitation by using large language models (LLMs), which have been demonstrated to be adept at natural language processing and code generation. By prompti...
  - **Labels**: [program testing](program_testing.md), [bug reproduction](bug_reproduction.md), [empirical study](empirical_study.md)

- [Evaluating and Improving ChatGPT for Unit Test Generation](../venues/FSE2024/paper_7.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Unit testing plays an essential role in detecting bugs in functionally-discrete program units (e.g., methods). Manually writing high-quality unit tests is time-consuming and laborious. Although the traditional techniques are able to generate tests with reasonable coverage, they are shown to exhibit low readability and still cannot be directly adopted by developers in practice. Recent work has shown the large potential of large language models (LLMs) in unit test generation. By being pre-trained ...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md), [code generation](code_generation.md)

- [Large Language Models for Equivalent Mutant Detection: How Far Are We?](../venues/ISSTA2024/paper_23.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Mutation testing is vital for ensuring software quality. However, the presence of equivalent mutants is known to introduce redundant cost and bias issues, hindering the effectiveness of mutation testing in practical use. Although numerous equivalent mutant detection (EMD) techniques have been proposed, they exhibit limitations due to the scarcity of training data and challenges in generalizing to unseen mutants. Recently, large language models (LLMs) have been extensively adopted in various code...
  - **Labels**: [program testing](program_testing.md), [mutation testing](mutation_testing.md), [empirical study](empirical_study.md)

- [Less Is More: On the Importance of Data Quality for Unit Test Generation](../venues/FSE2025/paper_18.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Unit testing is crucial for software development and maintenance. Effective unit testing ensures and improves software quality, but writing unit tests is time-consuming and labor-intensive. Recent studies have proposed deep learning (DL) techniques or large language models (LLMs) to automate unit test generation. These models are usually trained or fine-tuned on large-scale datasets. Despite growing awareness of the importance of data quality, there has been limited research on the quality of da...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md)

- [On the Evaluation of Large Language Models in Unit Test Generation](../venues/ASE2024/paper_26.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Unit testing is an essential activity in software development for verifying the correctness of software components. However, manually writing unit tests is challenging and time-consuming. The emergence of Large Language Models (LLMs) offers a new direction for automating unit test generation. Existing research primarily focuses on closed-source LLMs (e.g., ChatGPT and CodeX) with fixed prompting strategies, leaving the capabilities of advanced open-source LLMs with various prompting settings une...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md)

- [Reasoning Runtime Behavior of a Program with LLM: How Far are We?](../venues/ICSE2025/paper_9.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large language models for code (i.e., code LLMs) have shown strong code understanding and generation capabilities. To evaluate the capabilities of code LLMs in various aspects, many benchmarks have been proposed (e.g., HumanEval and ClassEval). Code reasoning is one of the most essential abilities of code LLMs (i.e., predicting code execution behaviors such as program output and execution path), but existing benchmarks for code reasoning are not sufficient. Typically, they focus on predicting th...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [TOGLL: Correct and Strong Test Oracle Generation with LLMS](../venues/ICSE2025/paper_31.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Test oracles play a crucial role in software testing, enabling effective bug detection. Despite initial promise, neural methods for automated test oracle generation often result in a large number of false positives and weaker test oracles. While LLMs have shown impressive effectiveness in various software engineering tasks, including code generation, test case creation, and bug fixing, there remains a notable absence of large-scale studies exploring their effectiveness in test oracle generation....
  - **Labels**: [program testing](program_testing.md), [empirical study](empirical_study.md)

- [Towards Understanding the Effectiveness of Large Language Models on Directed Test Input Generation](../venues/ASE2024/paper_42.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Automatic testing has garnered significant attention and success over the past few decades. Techniques such as unit testing and coverage-guided fuzzing have revealed numerous critical software bugs and vulnerabilities. However, a long-standing, formidable challenge for existing techniques is how to achieve higher testing coverage. Constraint-based techniques, such as symbolic execution and concolic testing, have been well-explored and integrated into the existing approaches. With the popularity ...
  - **Labels**: [program testing](program_testing.md), [unit testing](unit_testing.md), [empirical study](empirical_study.md)

## Software Maintenance And Deployment

- [An Empirical Study on Code Review Activity Prediction and Its Impact in Practice](../venues/FSE2024/paper_10.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: During code reviews, an essential step in software quality assurance, reviewers have the difficult task of understanding and evaluating code changes to validate their quality and prevent introducing faults to the codebase. This is a tedious process where the effort needed is highly dependent on the code submitted, as well as the author’s and the reviewer’s experience, leading to median wait times for review feedback of 15-64 hours. Through an initial user study carried with 29 experts, we found ...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md), [empirical study](empirical_study.md)

- [An Empirical Study on Commit Message Generation Using LLMs via In-Context Learning](../venues/ICSE2025/paper_29.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Commit messages concisely describe code changes in natural language and are important for software maintenance. Several approaches have been proposed to automatically generate commit messages, but they still suffer from critical limitations, such as time-consuming training and poor generalization ability. To tackle these limitations, we propose to borrow the weapon of large language models (LLMs) and in-context learning (ICL). Our intuition is based on the fact that the training corpora of LLMs ...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [commit message generation](commit_message_generation.md), [empirical study](empirical_study.md)

- [Automatic Commit Message Generation: A Critical Review and Directions for Future Work](../venues/TSE2024/paper_7.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Commit messages are critical for code comprehension and software maintenance. Writing a high-quality message requires skill and effort. To support developers and reduce their effort on this task, several approaches have been proposed to automatically generate commit messages. Despite the promising performance reported, we have identified three significant and prevalent threats in these automated approaches: 1) the datasets used to train and evaluate these approaches contain a considerable amount...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [commit message generation](commit_message_generation.md), [empirical study](empirical_study.md)

- [Automating Zero-Shot Patch Porting for Hard Forks](../venues/ISSTA2024/paper_6.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Forking is a typical way of code reuse, which provides a simple way for developers to create a variant software (denoted as hard fork) by copying and modifying an existing codebase. Despite of the benefits, forking also leads to duplicate efforts in software maintenance. Developers need to port patches across the hard forks to address similar bugs or implement similar features. Due to the divergence between the source project and the hard fork, patch porting is complicated, which requires an ada...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [empirical study](empirical_study.md)

- [Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering](../venues/ISSTA2025/paper_30.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Recently, large language models (LLMs) have been deployed to tackle various software engineering (SE) tasks like code generation, significantly advancing the automation of SE tasks. However, assessing the quality of these LLM-generated code and text remains challenging. The commonly used Pass@k metric necessitates extensive unit tests and configured environments, demands a high labor cost, and is not suitable for evaluating LLM-generated text. Conventional metrics like BLEU, which measure only l...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md), [empirical study](empirical_study.md)

- [LLM4SZZ: Enhancing SZZ Algorithm with Context-Enhanced Assessment on Large Language Models](../venues/ISSTA2025/paper_5.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: The SZZ algorithm is the dominant technique for identifying bug-inducing commits and serves as a foundation for many software engineering studies, such as bug prediction and static code analysis, thereby enhancing software quality and facilitating better maintenance practices. Researchers have proposed many variants to enhance the SZZalgorithm’s performance since its introduction. The majority of them rely on static techniques or heuristic assumptions, making them easy to implement, but their pe...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [empirical study](empirical_study.md)

- [Scientific Open-Source Software Is Less Likely to Become Abandoned Than One Might Think! Lessons from Curating a Catalog of Maintained Scientific Software](../venues/FSE2025/paper_30.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Scientific software is essential to scientific innovation and in many ways it is distinct from other types of software. Abandoned (or unmaintained), buggy, and hard to use software, a perception often associated with scientific software can hinder scientific progress, yet, in contrast to other types of software, its longevity is poorly understood. Existing data curation efforts are fragmented by science domain and/or are small in scale and lack key attributes. We use large language models to cla...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [empirical study](empirical_study.md)

- [Understanding Developer-Analyzer Interactions in Code Reviews](../venues/ASE2024/paper_29.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Static code analyzers are now a common part of the codereview process. These automated tools integrate into the code review process by commenting on code changes and suggesting improvements, in the same way as human reviewers. The comments made by static analyzers often trigger a conversation between developers to align on if and how the issue should be fixed. Because developers rarely give feedback directly to the tool, understanding the sentiment and intent in the conversation triggered by the...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md), [empirical study](empirical_study.md)

## Static Analysis

- [A Comprehensive Study of the Capabilities of Large Language Models for Vulnerability Detection](../venues/arXiv2024/paper_16.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated great potential for code generation and other software engineering tasks. Vulnerability detection is of crucial importance to maintaining the security, integrity, and trustworthiness of software systems. Precise vulnerability detection requires reasoning about the code, making it a good case study for exploring the limits of LLMs' reasoning capabilities. Although recent work has applied LLMs to vulnerability detection using generic prompting techniq...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)

- [Can LLMs Reason About Program Semantics? A Comprehensive Evaluation of LLMs on Formal Specification Inference](../venues/arXiv2025/paper_12.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Large Language Models (LLMs) are increasingly being used to automate programming tasks. Yet, LLMs' capabilities in reasoning about program semantics are still inadequately studied, leaving significant potential for further exploration. This paper introduces FormalBench, a comprehensive benchmark designed to evaluate LLMs' reasoning abilities on program semantics, particularly via the task of synthesizing formal program specifications to assist verifying program correctness. This task requires bo...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions?](../venues/FSE2024/paper_9.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Informal natural language that describes code functionality, such as code comments or function documentation, may contain substantial information about a program’s intent. However, there is typically no guarantee that a program’s implementation and natural language documentation are aligned. In the case of a conflict, leveraging information in code-adjacent natural language has the potential to enhance fault localization, debugging, and code trustworthiness. In practice, however, this informatio...
  - **Labels**: [static analysis](static_analysis.md), [specification inference](specification_inference.md), [empirical study](empirical_study.md)

- [Closing the Gap: A User Study on the Real-world Usefulness of AI-powered Vulnerability Detection & Repair in the IDE](../venues/ICSE2025/paper_1.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: This paper presents the first empirical study of a vulnerability detection and fix tool with professional software developers on real projects that they own. We implemented DeepVulGuard, an IDE-integrated tool based on state-of-the-art detection and fix models, and show that it has promising performance on benchmarks of historic vulnerability data. DeepVulGuard scans code for vulnerabilities (including identifying the vulnerability type and vulnerable region of code), suggests fixes, provides na...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)

- [Continuous learning for android malware detection](../venues/USENIXSec2023/paper_2.md), ([USENIXSec2023](../venues/USENIXSec2023/README.md))

  - **Abstract**: Machine learning methods can detect Android malware with very high accuracy. However, these classifiers have an Achilles heel, concept drift: they rapidly become out of date and ineffective, due to the evolution of malware apps and benign apps. Our research finds that, after training an Android malware classifier on one year's worth of data, the F1 score quickly dropped from 0.99 to 0.76 after 6 months of deployment on new test samples....
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)

- [Dependency-Aware Code Naturalness](../venues/OOPSLA2024/paper_8.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Code naturalness, which captures repetitiveness and predictability in programming languages, has proven valuable for various code-related tasks in software engineering. However, precisely measuring code naturalness remains a fundamental challenge. Existing methods measure code naturalness over individual lines of code while ignoring the deep semantic relations among different lines, e.g., program dependency, which may negatively affect the precision of the measure. Despite the intuitive appeal o...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [empirical study](empirical_study.md)

- [Do Language Models Learn Semantics of Code? {A} Case Study in Vulnerability Detection](../venues/arXiv2023/paper_7.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Recently, pretrained language models have shown state-of-the-art performance on the vulnerability detection task. These models are pretrained on a large corpus of source code, then fine-tuned on a smaller supervised vulnerability dataset. Due to the different training objectives and the performance of the models, it is interesting to consider whether the models have learned the semantics of code relevant to vulnerability detection, namely bug semantics, and if so, how the alignment to bug semant...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)

- [Examining Zero-Shot Vulnerability Repair with Large Language Models](../venues/S&P2023/paper_1.md), ([S&P2023](../venues/S&P2023/README.md))

  - **Abstract**: Human developers can produce code with cybersecurity bugs. Can emerging ‘smart’ code completion tools help repair those bugs? In this work, we examine the use of large language models (LLMs) for code (such as OpenAI’s Codex and AI21’s Jurassic J-1) for zero-shot vulnerability repair. We investigate challenges in the design of prompts that coax LLMs into generating repaired versions of insecure code. This is difficult due to the numerous ways to phrase key information— both semantically and synta...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)

- [EyeTrans: Merging Human and Machine Attention for Neural Code Summarization](../venues/FSE2024/paper_30.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Neural code summarization leverages deep learning models to automatically generate brief natural language summaries of code snippets. The development of Transformer models has led to extensive use of attention during model design. While existing work has primarily and almost exclusively focused on static properties of source code and related structural representations like the Abstract Syntax Tree (AST), few studies have considered human attention — that is, where programmers focus while examini...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [empirical study](empirical_study.md)

- [From Large to Mammoth: A Comparative Evaluation of Large Language Models in Vulnerability Detection](../venues/NDSS2025/paper_7.md), ([NDSS2025](../venues/NDSS2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated strong potential in tasks such as code understanding and generation. This study evaluates several advanced LLMs—such as LLaMA-2, CodeLLaMA, LLaMA-3, Mistral, Mixtral, Gemma, CodeGemma, Phi-2, Phi-3, and GPT-4—for vulnerability detection, primarily in Java, with additional tests in C/C++ to assess generalization. We transition from basic positive sample detection to a more challenging task involving both positive and negative samples and evaluate the...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)

- [LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?): A Comprehensive Evaluation, Framework, and Benchmarks](../venues/S&P2024/paper_1.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have been suggested for use in automated vulnerability repair, but benchmarks showing they can consistently identify security-related bugs are lacking. We thus develop SecLLMHolmes, a fully automated evaluation framework that performs the most detailed investigation to date on whether LLMs can reliably identify and reason about security-related bugs. We construct a set of 228 code scenarios and analyze eight of the most capable LLMs across eight different investigati...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)

- [LLMs: Understanding Code Syntax and Semantics for Code Analysis](../venues/arXiv2023/paper_1.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Large language models~(LLMs) demonstrate significant potential to revolutionize software engineering (SE) by exhibiting outstanding performance in SE tasks such as code and document generation. However, the high reliability and risk control requirements in software engineering raise concerns about the lack of interpretability of LLMs. To address this concern, we conducted a study to evaluate the capabilities of LLMs and their limitations for code analysis in SE. We break down the abilities neede...
  - **Labels**: [static analysis](static_analysis.md), [data-flow analysis](data-flow_analysis.md), [call graph analysis](call_graph_analysis.md), [data-flow analysis](data-flow_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)

- [Large Language Models for Code Analysis: Do LLMs Really Do Their Job?](../venues/USENIXSec2024/paper_1.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated significant potential in the realm of natural language understanding and programming code processing tasks. Their capacity to comprehend and generate human-like code has spurred research into harnessing LLMs for code analysis purposes. However, the existing body of literature falls short in delivering a systematic evaluation and assessment of LLMs' effectiveness in code analysis, particularly in the context of obfuscated code.This paper seeks to bri...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)

- [Large Language Models for In-File Vulnerability Localization Can Be “Lost in the End”](../venues/FSE2025/paper_12.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Traditionally, software vulnerability detection research has focused on individual small functions due to earlier language processing technologies’ limitations in handling larger inputs. However, this function-level approach may miss bugs that span multiple functions and code blocks. Recent advancements in artificial intelligence have enabled processing of larger inputs, leading everyday software developers to increasingly rely on chat-based large language models (LLMs) like GPT-3.5 and GPT-4 to...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)

- [Risky Dynamic Typing-related Practices in Python: An Empirical Study](../venues/TOSEM2024/paper_6.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Python’s dynamic typing nature provides developers with powerful programming abstractions. However, many type-related bugs are accumulated in code bases of Python due to the misuse of dynamic typing. The goal of this article is to aid in the understanding of developers’ high-risk practices toward dynamic typing and the early detection of type-related bugs. We first formulate the rules of six types of risky dynamic typing-related practices (type smells for short) in Python. We then develop a rule...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)

- [SV-TrustEval-C: Evaluating Structure and Semantic Reasoning in Large Language Models for Source Code Vulnerability Analysis](../venues/S&P2025/paper_1.md), ([S&P2025](../venues/S&P2025/README.md))

  - **Abstract**: As Large Language Models (LLMs) evolve in understanding and generating code, accurately evaluating their reliability in analyzing source code vulnerabilities becomes in-creasingly vital. While studies have examined LLM capabilities in tasks like vulnerability detection and repair, they often over-look the importance of both structure and semantic reasoning crucial for trustworthy vulnerability analysis. To address this gap, we introduce SV-TRUSTEVAL-C, a benchmark designed to evaluate LLMs' abil...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [Source Code Summarization in the Era of Large Language Models](../venues/ICSE2025/paper_17.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: To support software developers in understanding and maintaining programs, various automatic (source) code summarization techniques have been proposed to generate a concise natural language summary (i.e., comment) for a given code snippet. Recently, the emergence of large language models (LLMs) has led to a great boost in the performance of coderelated tasks. In this paper, we undertake a systematic and comprehensive study on code summarization in the era of LLMs, which covers multiple aspects in...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [empirical study](empirical_study.md)

- [Stanceformer: Target-Aware Transformer for Stance Detection](../venues/EMNLP2024/paper_5.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: The task of Stance Detection involves discerning the stance expressed in a text towards a specific subject or target. Prior works have relied on existing transformer models that lack the capability to prioritize targets effectively. Consequently, these models yield similar performance regardless of whether we utilize or disregard target information, undermining the task’s significance. To address this challenge, we introduce Stanceformer, a target-aware transformer model that incorporates enhanc...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)

- [The EarlyBIRD Catches the Bug: On Exploiting Early Layers of Encoder Models for More Efficient Code Classification](../venues/FSE2023/paper_12.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: The use of modern Natural Language Processing (NLP) techniques has shown to be beneficial for software engineering tasks, such as vulnerability detection and type inference. However, training deep NLP models requires significant computational resources. This paper explores techniques that aim at achieving the best usage of resources and available information in these models.  We propose a generic approach, EarlyBIRD, to build composite representations of code from the early layers of a pre-train...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)

- [The Emergence of Large Language Models in Static Analysis: A First Look through Micro-Benchmarks](../venues/Forge2024/paper_1.md), ([Forge2024](../venues/Forge2024/README.md))

  - **Abstract**: Binary code similarity detection(BCSD), as a fundamental technique in software security, has various applications, including malware family detection, known vulnerability detection and code plagiarism detection. Recent deep learning-based BCSD approaches have demonstrated promising performance. However, they face two significant challenges that limit detection performance. First, most approaches that use sequence networks (like RNN and Transformer) utilize coarse-grained tokenization methods, wh...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)

- [The Struggles of LLMs in Cross-Lingual Code Clone Detection](../venues/FSE2025/paper_15.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: With the involvement of multiple programming languages in modern software development, cross-lingual code clone detection has gained traction within the software engineering community. Numerous studies have explored this topic, proposing various promising approaches. Inspired by the significant advances in machine learning in recent years, particularly Large Language Models (LLMs), which have demonstrated their ability to tackle various tasks, this paper revisits cross-lingual code clone detecti...
  - **Labels**: [empirical study](empirical_study.md), [static analysis](static_analysis.md), [code similarity analysis](code_similarity_analysis.md)

- [Top Score on the Wrong Exam: On Benchmarking in Machine Learning for Vulnerability Detection](../venues/arXiv2024/paper_20.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: According to our survey of the machine learning for vulnerability detection (ML4VD) literature published in the top Software Engineering conferences, every paper in the past 5 years defines ML4VD as a binary classification problem: Given a function, does it contain a security flaw?In this paper, we ask whether this decision can really be made without further context and study both vulnerable and non-vulnerable functions in the most popular ML4VD datasets. A function is vulnerable if it was invol...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)

- [Towards Neural Synthesis for SMT-Assisted Proof-Oriented Programming](../venues/ICSE2025/paper_7.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Proof-oriented programs mix computational content with proofs of program correctness. However, the human effort involved in programming and proving is still substantial, despite the use of Satisfiability Modulo Theories (SMT) solvers to automate proofs in languages such as F*. Seeking to spur research on using AI to automate the construction of proof-oriented programs, we curate a dataset of 600K lines of open-source F* programs and proofs, including software used in production systems ranging f...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [static analysis](static_analysis.md), [program verification](program_verification.md), [benchmark](benchmark.md), [empirical study](empirical_study.md)

- [Understanding the Effectiveness of Large Language Models in Detecting Security Vulnerabilities](../venues/arXiv2023/paper_6.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: While automated vulnerability detection techniques have made promising progress in detecting security vulnerabilities, their scalability and applicability remain challenging. The remarkable performance of Large Language Models (LLMs), such as GPT-4 and CodeLlama, on code-related tasks has prompted recent works to explore if LLMs can be used to detect vulnerabilities. In this paper, we perform a more comprehensive study by concurrently examining a higher number of datasets, languages and LLMs, an...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)

- [Unveiling Code Pre-Trained Models: Investigating Syntax and Semantics Capacities](../venues/TOSEM2024/paper_1.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Code models have made significant advancements in code intelligence by encoding knowledge about programming languages. While previous studies have explored the capabilities of these models in learning code syntax, there has been limited investigation on their ability to understand code semantics. Additionally, existing analyses assume that the number of edges between nodes at the abstract syntax tree&nbsp;(AST) is related to syntax distance, and also often require transforming the high-dimension...
  - **Labels**: [static analysis](static_analysis.md), [pointer analysis](pointer_analysis.md), [data-flow analysis](data-flow_analysis.md), [empirical study](empirical_study.md)

- [What can Large Language Models Capture about Code Functional Equivalence?](../venues/NAACL2025/paper_13.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Code-LLMs, LLMs pre-trained on large code corpora, have shown great progress in learning rich representations of the structure and syntax of code, successfully using it to generate or classify code fragments. At the same time, understanding if they are able to do so because they capture code semantics, and how well, is still an open question. In this paper, we tackle this problem by introducing SeqCoBench, a benchmark for systematically assessing how Code-LLMs can capture code functional equival...
  - **Labels**: [static analysis](static_analysis.md), [equivalence checking](equivalence_checking.md), [empirical study](empirical_study.md), [benchmark](benchmark.md)

- [Which Syntactic Capabilities Are Statistically Learned by Masked Language Models for Code?](../venues/ICSE2024/paper_20.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: This paper discusses the limitations of evaluating Masked Language Models (MLMs) in code completion tasks. We highlight that relying on accuracy-based measurements may lead to an overestimation of models' capabilities by neglecting the syntax rules of programming languages. To address these issues, we introduce a technique called SyntaxEval in which Syntactic Capabilities are used to enhance the evaluation of MLMs. SyntaxEval automates the process of masking elements in the model input based on ...
  - **Labels**: [static analysis](static_analysis.md), [syntactic analysis](syntactic_analysis.md), [empirical study](empirical_study.md)
