# Program Repair

- [AdverIntent-Agent: Adversarial Reasoning for Repair Based on Inferred Program Intent](../venues/ISSTA2025/paper_18.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Automated program repair (APR) has shown promising results, particularly with the use of neural networks. Currently, most APR tools focus on code transformations specified by test suites, rather than reasoning about the program’s intent and the high-level bug specification. Without a proper understanding of program intent, these tools tend to generate patches that overfit incomplete test suites and fail to reflect the developer’s intentions. However, reasoning about program intent is challenging...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [Agentless: Demystifying LLM-based Software Engineering Agents](../venues/FSE2025/paper_2.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Recent advancements in large language models (LLMs) have significantly advanced the automation of software development tasks, including code synthesis, program repair, and test generation. More recently, researchers and industry practitioners have developed various autonomous LLM agents to perform end-to-end software development tasks. These agents are equipped with the ability to use tools, run commands, observe feedback from the environment, and plan for future actions. However, the complexity...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Aligning the Objective of LLM-Based Program Repair](../venues/ICSE2025/paper_49.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Large language models (LLMs) have achieved decent results on automated program repair (APR). However, the next token prediction training objective of decoder-only LLMs (e.g., GPT-4) is misaligned with the masked span prediction objective of current infilling-style methods, which impedes LLMs from fully leveraging pre-trained knowledge for program repair. In addition, while some LLMs can locate and repair bugs in certain functions using the related artifacts (e.g., test cases), existing methods s...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [An Empirical Study on Fine-Tuning Large Language Models of Code for Automated Program Repair](../venues/ASE2023/paper_2.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: The advent of large language models (LLMs) has opened up new opportunities for automated program repair (APR). In particular, some recent studies have explored how to leverage large language models of code (LLMCs) for program repair tasks and show promising results. However, most of them adopt the zero/few-shot learning paradigm for APR, which directly use LLMCs to generate the possibly correct code given its surrounding context. Though effective, the repair capabilities of LLMCs based on the fi...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Are “Solved Issues” in SWE-bench Really Solved Correctly?](../venues/arXiv2025/paper_15.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Automated issue solving aims to resolve real-world issues in software repositories. The most popular benchmarks for automated issue solving are SWE-bench and its human-filtered subset SWE-bench Verified. These benchmarks leverage testing to validate generated patches. However, because testing is rarely exhaustive, a patch may pass the tests but nevertheless fail to match the developers' expectations. Unfortunately, it is currently unclear to what extent evaluations performed with SWE-bench suffe...
  - **Labels**: [benchmark](benchmark.md), [code generation](code_generation.md), [program repair](program_repair.md)


- [AutoCodeRover: Autonomous Program Improvement](../venues/ISSTA2024/paper_20.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Researchers have made significant progress in automating the software development process in the past decades. Automated techniques for issue summarization, bug reproduction, fault localization, and program repair have been built to ease the workload of developers. Recent progress in Large Language Models (LLMs) has significantly impacted the development process, where developers can use LLM-based programming assistants to achieve automated coding. Nevertheless, software engineering involves the...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automated Program Repair in the Era of Large Pre-Trained Language Models](../venues/ICSE2023/paper_4.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Automated Program Repair (APR) aims to help developers automatically patch software bugs. However, current state-of-the-art traditional and learning-based APR techniques face the problem of limited patch variety, failing to fix complicated bugs. This is mainly due to the reliance on bug-fixing datasets to craft fix templates (traditional) or directly predict potential patches (learning-based). Large Pre-Trained Language Models (LLMs), trained using billions of text/code tokens, can potentially h...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automated Program Repair via Conversation: Fixing 162 out of 337 Bugs for $0.42 Each using ChatGPT](../venues/ISSTA2024/paper_10.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Automated Program Repair (APR) aims to automatically generate patches for buggy programs. Traditional APR techniques suffer from a lack of patch variety as they rely heavily on handcrafted or mined bug fixing patterns and cannot easily generalize to other bug/fix types. To address this limitation, recent APR work has been focused on leveraging modern Large Language Models (LLMs) to directly generate patches for APR. Such LLM-based APR tools work by first constructing an input prompt built using ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automated Program Repair via Conversation:Fixing 162 out of 337 Bugs for $0.42 Each using ChatGPT](../venues/ISSTA2024/paper_2.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Automated Program Repair (APR) aims to automatically generate patches for buggy programs. Traditional APR techniques suffer from a lack of patch variety as they rely heavily on handcrafted or mined bug fixing patterns and cannot easily generalize to other bug/fix types. To address this limitation, recent APR work has been focused on leveraging modern Large Language Models (LLMs) to directly generate patches for APR. Such LLM-based APR tools work by first constructing an input prompt built using ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automated Repair of Programs from Large Language Models](../venues/ICSE2023/paper_3.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Large language models such as Codex, have shown the capability to produce code for many programming tasks. However, the success rate of existing models is low, especially for complex programming tasks. One of the reasons is that language models lack awareness of program semantics, resulting in incorrect programs, or even programs which do not compile. In this paper, we systematically study whether automated program repair (APR) techniques can fix the incorrect solutions produced by language mode...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automatically Fixing Dependency Breaking Changes](../venues/FSE2025/paper_29.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Breaking changes in dependencies are a common challenge in software development, requiring manual intervention to resolve. This study examines how well LLM automate the repair of breaking changes caused by dependency updates in Java projects. Although earlier methods have mostly concentrated on detecting breaking changes or investigating their impact, they have not been able to completely automate the repair process. We introduce and compare two new approaches: an agentic system that combines au...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Benchmarking Automated Program Repair: An Extensive Study on Both Real-World and Artificial Bugs](../venues/ISSTA2024/paper_7.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: As bugs are inevitable and prevalent in real-world programs, many Automated Program Repair (APR) techniques have been proposed to generate patches for them. However, due to the lack of a standard for evaluating APR techniques, prior works tend to use different settings and benchmarks in evaluation, threatening the trustworthiness of the evaluation results. Additionally, they typically only adopt plausibility and genuineness as evaluation metrics, which may potentially mask some underlying issues...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)


- [Better Patching Using LLM Prompting, via Self-Consistency](../venues/ASE2023/paper_5.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Large Language models (LLMs) can be induced to solve non-trivial problems with “few-shot” prompts including illustrative problem-solution examples. Now if the few-shots also include “chain of thought” ($\mathcal{C}oT$) explanations, which are of the form problem-explanation-solution, LLMs will generate a “explained” solution, and perform even better. Recently an exciting, substantially better technique, self-consistency [1] ($\mathcal{S}-C$) has emerged, based on the intuition that there are man...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md)


- [CREF: An LLM-Based Conversational Software Repair Framework for Programming Tutors](../venues/ISSTA2024/paper_11.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: With the proven effectiveness of Large Language Models (LLMs) in code-related tasks, researchers have explored their potential for program repair. However, existing repair benchmarks might have influenced LLM training data, potentially causing data leakage. To evaluate LLMs’ realistic repair capabilities, (i) we introduce an extensive, non-crawled benchmark TutorCode, comprising 1,239 C++ defect codes and associated information such as tutor guidance, solution description, failing test cases, an...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Closing the Gap: A User Study on the Real-world Usefulness of AI-powered Vulnerability Detection & Repair in the IDE](../venues/ICSE2025/paper_1.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: This paper presents the first empirical study of a vulnerability detection and fix tool with professional software developers on real projects that they own. We implemented DeepVulGuard, an IDE-integrated tool based on state-of-the-art detection and fix models, and show that it has promising performance on benchmarks of historic vulnerability data. DeepVulGuard scans code for vulnerabilities (including identifying the vulnerability type and vulnerable region of code), suggests fixes, provides na...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Code Change Intention, Development Artifact, and History Vulnerability: Putting Them Together for Vulnerability Fix Detection by LLM](../venues/FSE2025/paper_8.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Detecting vulnerability fix commits in open-source software is crucial for maintaining software security. To help OSS identify vulnerability fix commits, several automated approaches are developed. However, existing approaches like VulFixMiner and CoLeFunDa, focus solely on code changes, neglecting essential context from development artifacts. Tools like Vulcurator, which integrates issue reports, fail to leverage semantic associations between different development artifacts (e.g., pull requests...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Coffee-Gym: An Environment for Evaluating and Improving Natural Language Feedback on Erroneous Code](../venues/EMNLP2024/paper_38.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: This paper presents Coffee-Gym, a comprehensive RL environment for training models that provide feedback on code editing. Coffee-Gym includes two major components: (1) Coffee, a dataset containing humans’ code edit traces for coding questions and human-written feedback for editing erroneous code; (2) CoffeeEval, a reward function that faithfully reflects the helpfulness of feedback by assessing the performance of the revised code in unit tests. With them, Coffee-Gym addresses the unavailability ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)


- [ContractTinker: LLM-Empowered Vulnerability Repair for Real-World Smart Contracts](../venues/ASE2024/paper_35.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Smart contracts are susceptible to being exploited by attackers, especially when facing real-world vulnerabilities. To mitigate this risk, developers often rely on third-party audit services to identify potential vulnerabilities before project deployment. Nevertheless, repairing the identified vulnerabilities is still complex and laborintensive, particularly for developers lacking security expertise. Moreover, existing pattern-based repair tools mostly fail to address real-world vulnerabilities ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Copilot-in-the-Loop: Fixing Code Smells in Copilot-Generated Python Code using Copilot](../venues/ASE2024/paper_31.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: As one of the most popular dynamic languages, Python experiences a decrease in readability and maintainability when code smells are present. Recent advancements in Large Language Models have sparked growing interest in AI-enabled tools for both code generation and refactoring. GitHub Copilot is one such tool that has gained widespread usage. Copilot Chat, released in September 2023, functions as an interactive tool aimed at facilitating natural language-powered coding. However, limited attention...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Copiloting the Copilots: Fusing Large Language Models with Completion Engines for Automated Program Repair](../venues/FSE2023/paper_1.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: During Automated Program Repair (APR), it can be challenging&nbsp;to synthesize correct patches for real-world systems in general-purpose programming languages. Recent Large Language Models&nbsp;(LLMs) have been shown to be helpful “copilots” in assisting developers with various coding tasks, and have also been directly&nbsp;applied for patch synthesis. However, most LLMs treat programs as&nbsp;sequences of tokens, meaning that they are ignorant of the underlying semantics constraints of the tar...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [DR.FIX: Automatically Fixing Data Races at Industry Scale](../venues/PLDI2025/paper_1.md), ([PLDI2025](../venues/PLDI2025/README.md))

  - **Abstract**: Data races are a prevalent class of concurrency bugs in shared-memory parallel programs, posing significant challenges to software reliability and reproducibility. While there is an extensive body of research on detecting data races and a wealth of practical detection tools across various programming languages, considerably less effort has been directed toward automatically fixing data races at an industrial scale. In large codebases, data races are continuously introduced and exhibit myriad pat...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Demystifying Memorization in LLM-Based Program Repair via a General Hypothesis Testing Framework](../venues/FSE2025/paper_35.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Large Language Models (LLMs) have achieved remarkable success in various applications, particularly in code-related tasks such as code generation and program repair, setting new performance benchmarks. However, the extensive use of large training corpora raises concerns about whether these achievements stem from genuine understanding or mere memorization of training data—a question often overlooked in current research. This paper aims to study the memorization issue within LLM-based program repa...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [DesignRepair: Dual-Stream Design Guideline-Aware Frontend Repair with Large Language Models](../venues/ICSE2025/paper_36.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: The rise of Large Language Models (LLMs) has streamlined frontend interface creation through tools like Vercel's v0, yet surfaced challenges in design quality (e.g., accessibility, and usability). Current solutions, often limited by their focus, generalisability, or data dependency, fall short in addressing these complexities. Moreover, none of them examine the quality of LLM-generated UI design. In this work, we introduce DesignRepair, a novel dual-stream design guideline-aware system to examin...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Element-Based Automated DNN Repair with Fine-Tuned Masked Language Model](../venues/FSE2025/paper_3.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Deep Neural Networks (DNNs) are prevalent across a wide range of applications. Despite their success, the complexity and opaque nature of DNNs pose significant challenges in debugging and repairing DNN models, limiting their reliability and broader adoption. In this paper, we propose MLM4DNN, an element-based automated DNN repair method. Unlike previous techniques that focus on post-training adjustments or rely heavily on predefined bug patterns, MLM4DNN repairs DNNs by leveraging a fine-tuned M...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Error Delayed Is Not Error Handled: Understanding and Fixing Propagated Error-Handling Bugs](../venues/FSE2025/paper_33.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Error handling is critical for software reliability. In software systems, error handling may be delayed to other functions. Such propagated error handling (PEH) could easily be missed and lead to bugs. Our research reveals that PEH bugs are prevalent in software systems and, on average, take 44.1 days to fully address. Existing approaches have primarily focused on the error-handling bug within individual functions, which makes it difficult to fully address PEH bugs. In this paper, we conducted t...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Exploring Parameter-Efficient Fine-Tuning of Large Language Model on Automated Program Repair](../venues/ASE2024/paper_14.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Automated Program Repair (APR) aims to fix bugs by generating patches. And existing work has demonstrated that "pre-training and fine-tuning" paradigm enables Large Language Models (LLMs) improve fixing capabilities on APR. However, existing work mainly focuses on Full-Model Fine-Tuning (FMFT) for APR and limited research has been conducted on the execution-based evaluation of Parameter-Efficient Fine-Tuning (PEFT) for APR. Comparing to FMFT, PEFT can reduce computing resource consumption withou...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [FIXDRIVE: Automatically Repairing Autonomous Vehicle Driving Behaviour for $0.08 per Violation](../venues/ICSE2025/paper_60.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Autonomous Vehicles (AVs) are advancing rapidly, with Level-4 AVs already operating in real-world conditions. Current AVs, however, still lag behind human drivers in adaptability and performance, often exhibiting overly conservative behaviours and occasionally violating traffic laws. Existing solutions, such as runtime enforcement, mitigate this by automatically repairing the AV's planned trajectory at runtime, but such approaches lack transparency and should be a measure of last resort. It woul...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [FastFixer: An Efficient and Effective Approach for Repairing Programming Assignments](../venues/ASE2024/paper_12.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Providing personalized and timely feedback for student's programming assignments is useful for programming education. Automated program repair (APR) techniques have been used to fix the bugs in programming assignments, where the Large Language Models (LLMs) based approaches have shown promising results. Given the growing complexity of identifying and fixing bugs in advanced programming assignments, current fine-tuning strategies for APR are inadequate in guiding the LLM to identify bugs and make...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Fixing 7,400 Bugs for 1$: Cheap Crash-Site Program Repair](../venues/arXiv2025/paper_17.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: The rapid advancement of bug-finding techniques has led to the discovery of more vulnerabilities than developers can reasonably fix, creating an urgent need for effective Automated Program Repair (APR) methods. However, the complexity of modern bugs often makes precise root cause analysis difficult and unreliable. To address this challenge, we propose crash-site repair to simplify the repair task while still mitigating the risk of exploitation. In addition, we introduce a template-guided patch g...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Fixing Large Language Models' Specification Misunderstanding for Better Code Generation](../venues/ICSE2025/paper_35.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Code generation is to automatically generate source code conforming to a given programming specification, which has received extensive attention especially with the development of large language models (LLMs). Due to the inherent difficulty of code generation, the code generated by LLMs may not be aligned with the specification. Although thought-eliciting prompting techniques have been proposed to enhance the code generation performance of LLMs, producing correct understanding for complicated pr...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [How Effective Are Neural Networks for Fixing Security Vulnerabilities](../venues/ISSTA2023/paper_3.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Security vulnerability repair is a difficult task that is in dire need of automation. Two groups of techniques have shown promise: (1) large code language models (LLMs) that have been pre-trained on source code for tasks such as code completion, and (2) automated program repair (APR) techniques that use deep learning (DL) models to automatically fix software bugs. This paper is the first to study and compare Java vulnerability repair capabilities of LLMs and DL-based APR models. The contribution...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)


- [Improving Automated Program Repair with Domain Adaptation](../venues/TOSEM2024/paper_8.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Automated Program Repair (APR) is defined as the process of fixing a bug/defect in the source code, by an automated tool. APR tools have recently experienced promising results by leveraging state-of-the-art Neural Language Processing (NLP) techniques. APR tools such as TFix and CodeXGLUE that combine text-to-text transformers with software-specific techniques are outperforming alternatives, these days. However, in most APR studies, the train and test sets are chosen from the same set of projects...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Improving Transformer-based Program Repair Model through False Behavior Diagnosis](../venues/EMNLP2023/paper_17.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Research on automated program repairs using transformer-based models has recently gained considerable attention. The comprehension of the erroneous behavior of a model enables the identification of its inherent capacity and provides insights for improvement. However, the current landscape of research on program repair models lacks an investigation of their false behavior. Thus, we propose a methodology for diagnosing and treating the false behaviors of transformer-based program repair models. Sp...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [InferFix: End-to-End Program Repair with LLMs](../venues/FSE2023/paper_5.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Software development life cycle is profoundly influenced by bugs; their introduction, identification, and eventual resolution account for a significant portion of software development cost. This has motivated software engineering researchers and practitioners to propose different approaches for automating the identification and repair of software defects. Large Language Models (LLMs) have been adapted to the program repair task through few-shot demonstration learning and instruction prompting, t...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Intention is All you Need: Refining your Code from your Intention](../venues/ICSE2025/paper_55.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Code refinement aims to enhance existing code by addressing issues, refactoring, and optimizing to improve quality and meet specific requirements. As software projects scale in size and complexity, the traditional iterative exchange between re-viewers and developers becomes increasingly burdensome. While recent deep learning techniques have been explored to accelerate this process, their performance remains limited, primarily due to challenges in accurately understanding reviewers' intents. This...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [code summarization](code_summarization.md)


- [Investigating the Transferability of Code Repair for Low-Resource Programming Languages](../venues/NAACL2025/paper_2.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Large language models (LLMs) have shown remarkable performance on code generation tasks. A recent use case is iterative code repair, where an LLM fixes an incorrect program by rationalizing about errors and generating new code. Recent works augment the code repair process by integrating modern techniques such as chain-of-thought reasoning or distillation, but only study their benefits on high-resource languages like Python, and ignore low-resource languages like Perl. To address this gap of know...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Is Self-Repair a Silver Bullet for Code Generation?](../venues/ICLR2023/paper_1.md), ([ICLR2023](../venues/ICLR2023/README.md))

  - **Abstract**: Large language models have shown remarkable aptitude in code generation, but still struggle to perform complex tasks. Self-repair---in which the model debugs and repairs its own code---has recently become a popular way to boost performance in these settings. However, despite its increasing popularity, existing studies of self-repair have been limited in scope; in many settings, its efficacy thus remains poorly understood. In this paper, we analyze Code Llama, GPT-3.5 and GPT-4's ability to perfo...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Knowledge-Enhanced Program Repair for Data Science Code](../venues/ICSE2025/paper_69.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: This paper introduces DSrepair, a knowledge-enhanced program repair approach designed to repair the buggy code generated by LLMs in the data science domain. DSrepair uses knowledge graph based RAG for API knowledge retrieval and bug knowledge enrichment to construct repair prompts for LLMs. Specifically, to enable knowledge graph-based API retrieval, we construct DS-KG (Data Science Knowledge Graph) for widely used data science libraries. For bug knowledge enrichment, we employ an abstract synta...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [LLM-Based Repair of Static Nullability Errors](../venues/arXiv2025/paper_26.md), ([arXiv2025](../venues/arXiv2025/README.md))

  - **Abstract**: Modern Java projects increasingly adopt static analysis tools that prevent null-pointer exceptions by treating nullness as a type property. However, integrating such tools into large, existing codebases remains a significant challenge. While annotation inference can eliminate many errors automatically, a subset of residual errors -- typically a mix of real bugs and false positives -- often persist and can only be resolved via code changes. Manually addressing these errors is tedious and error-pr...
  - **Labels**: [program repair](program_repair.md)


- [LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?): A Comprehensive Evaluation, Framework, and Benchmarks](../venues/S&P2024/paper_1.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have been suggested for use in automated vulnerability repair, but benchmarks showing they can consistently identify security-related bugs are lacking. We thus develop SecLLMHolmes, a fully automated evaluation framework that performs the most detailed investigation to date on whether LLMs can reliably identify and reason about security-related bugs. We construct a set of 228 code scenarios and analyze eight of the most capable LLMs across eight different investigati...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Mining Action Rules for Defect Reduction Planning](../venues/FSE2024/paper_12.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Defect reduction planning plays a vital role in enhancing software quality and minimizing software maintenance costs. By training a black box machine learning model and “explaining” its predictions, explainable AI for software engineering aims to identify the code characteristics that impact maintenance risks. However, post-hoc explanations do not always faithfully reflect what the original model computes. In this paper, we introduce CounterACT, a Counterfactual ACTion rule mining approach that ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Mystique: Automated Vulnerability Patch Porting with Semantic and Syntactic-Enhanced LLM](../venues/FSE2025/paper_4.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Branching repositories facilitates efficient software development but can also inadvertently propagate vulnerabilities. When an original branch is patched, other unfixed branches remain vulnerable unless the patch is successfully ported. However, due to inherent discrepancies between branches, many patches cannot be directly applied and require manual intervention, which is time-consuming and leads to delays in patch porting, increasing vulnerability risks. Existing automated patch porting appro...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [NIODebugger: A Novel Approach to Repair Non-Idempotent-Outcome Tests with LLM-Based Agent](../venues/ICSE2025/paper_61.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Flaky tests, characterized by inconsistent results across repeated executions, present significant challenges in software testing, especially during regression testing. Recently, there has been emerging research interest in non-idempotentoutcome (NIO) flaky tests-tests that pass on the initial run but fail on subsequent executions within the same environment. Despite progress in utilizing Large Language Models (LLMs) to address flaky tests, existing methods have not tackled NIO flaky tests. The ...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [bug reproduction](bug_reproduction.md), [code generation](code_generation.md), [program repair](program_repair.md)


- [Neurosymbolic Repair of Test Flakiness](../venues/ISSTA2024/paper_17.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Test flakiness, a non-deterministic behavior of builds irrelevant to code changes, is a major and continuing impediment to deliver- ing reliable software. The very few techniques for the automated repair of test flakiness are specifically crafted to repair either Order- Dependent (OD) or Implementation-Dependent (ID) flakiness. They are also all symbolic approaches, i.e., they leverage program analy- sis to detect and repair known test flakiness patterns and root causes, failing to generalize. T...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [OmniGIRL: A Multilingual and Multimodal Benchmark for GitHub Issue Resolution](../venues/ISSTA2025/paper_2.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: The GitHub issue resolution task aims to resolve issues reported in repositories automatically. With advances in large language models (LLMs), this task has gained increasing attention, and several benchmarks are proposed to evaluate the issue resolution ability of LLMs. However, existing benchmarks have three main limitations. First, current benchmarks focus on a single programming language, limiting the evaluation of issues from repositories across different languages. Second, they usually cov...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Out of Context: How important is Local Context in Neural Program Repair?](../venues/ICSE2024/paper_27.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Deep learning source code models have been applied very successfully to the problem of automated program repair. One of the standing issues is the small input window of current models which often cannot fully fit the context code required for a bug fix (e.g., method or class declarations of a project). Instead, input is often restricted to the local context, that is, the lines below and above the bug location. In this work we study the importance of this local context on repair success: how much...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Out of Sight, Out of Mind: Better Automatic Vulnerability Repair by Broadening Input Ranges and Sources](../venues/ICSE2024/paper_28.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: The advances of deep learning (DL) have paved the way for automatic software vulnerability repair approaches, which effectively learn the mapping from the vulnerable code to the fixed code. Nevertheless, existing DL-based vulnerability repair methods face notable limitations: 1) they struggle to handle lengthy vulnerable code, 2) they treat code as natural language texts, neglecting its inherent structure, and 3) they do not tap into the valuable expert knowledge present in the expert system. To...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Programming Assistant for Exception Handling with CodeBERT](../venues/ICSE2024/paper_13.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: With practical code reuse, the code fragments from developers' forums often migrate to applications. Owing to the incomplete nature of such fragments, they often lack the details on exception handling. The adaptation for exception handling to the codebase is not trivial as developers must learn and memorize what API methods could cause exceptions and what exceptions need to be handled. We propose Neurex, an exception handling recommender that learns from complete code, and accepts a given Java c...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [PyDex: Repairing Bugs in Introductory Python Assignments using LLMs](../venues/OOPSLA2024/paper_6.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Students often make mistakes in their introductory programming assignments as part of their learning process. Unfortunately, providing custom repairs for these mistakes can require a substantial amount of time and effort from class instructors. Automated program repair (APR) techniques can be used to synthesize such fixes. Prior work has explored the use of symbolic and neural techniques for APR in the education domain. Both types of approaches require either substantial engineering efforts or l...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [PyTy: Repairing Static Type Errors in Python](../venues/ICSE2024/paper_12.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Gradual typing enables developers to annotate types of their own choosing, offering a flexible middle ground between no type annotations and a fully statically typed language. As more and more code bases get type-annotated, static type checkers detect an increasingly large number of type errors. Unfortunately, fixing these errors requires manual effort, hampering the adoption of gradual typing in practice. This paper presents PyTy, an automated program repair approach targeted at statically dete...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [type inference](type_inference.md)


- [RepairAgent: An Autonomous, LLM-Based Agent for Program Repair](../venues/ICSE2025/paper_46.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Automated program repair has emerged as a powerful technique to mitigate the impact of software bugs on system reliability and user experience. This paper introduces Repair Agent, the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM). Unlike existing deep learning-based approaches, which prompt a model with a fixed prompt or in a fixed feedback loop, our work treats the LLM as an agent capable of autonomously planning and executi...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [agent design](agent_design.md)


- [Repairagent: An autonomous, llm-based agent for program repair](../venues/arXiv2024/paper_11.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Automated program repair has emerged as a powerful technique to mitigate the impact of software bugs on system reliability and user experience. This paper introduces RepairAgent, the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM). Unlike existing deep learning-based approaches, which prompt a model with a fixed prompt or in a fixed feedback loop, our work treats the LLM as an agent capable of autonomously planning and executin...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [agent design](agent_design.md), [planning](planning.md)


- [Repairing Bugs with the Introduction of New Variables: A Multi-Agent Large Language Model](../venues/CCS2024/paper_6.md), ([CCS2024](../venues/CCS2024/README.md))

  - **Abstract**: Trained on billions of tokens, large language models (LLMs) have a broad range of empirical knowledge which enables them to generate software patches with complex repair patterns. We leverage the powerful code-fixing capabilities of LLMs and propose VarPatch, a multi-agent conversational automated program repair (APR) technique that iteratively queries the LLM to generate software patches by providing various prompts and context information. VarPatch focuses on the variable addition repair patte...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Revisiting Unnaturalness for Automated Program Repair in the Era of Large Language Models](../venues/ICSE2025/paper_28.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: The problem of software quality has motivated the development of a variety of techniques for Automatic Program Repair (APR). Meanwhile, recent advances in AI and Large Language Models (LLMs) have produced orders of magnitude performance improvements over previous code generation techniques, affording promising opportunities for program repair and its constituent subproblems (e.g., fault localization, patch generation). Because models are trained on large volumes of code in which defects are rela...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [RustAssistant: Using LLMs to Fix Compilation Errors in Rust Code](../venues/ICSE2025/paper_14.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: The Rust programming language, with its safety guarantees, has established itself as a viable choice for low-level systems programming language over the traditional, unsafe alternatives like C/C++. These guarantees come from a strong ownership-based type system, as well as primitive support for features like closures, pattern matching, etc., that make the code more concise and amenable to reasoning. These unique Rust features also pose a steep learning curve for programmers. This paper presents ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Self-Edit: Fault-Aware Code Editor for Code Generation](../venues/ACL2023/paper_1.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated an impressive ability to generate codes on competitive programming tasks. However, with limited sample numbers, LLMs still suffer from poor accuracy. Inspired by the process of human programming, we propose a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task. We execute the generated code on the example test case provided in the q...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)


- [Show Me Why It’s Correct: Saving 1/3 of Debugging Time in Program Repair with Interactive Runtime Comparison](../venues/OOPSLA2025/paper_1.md), ([OOPSLA2025](../venues/OOPSLA2025/README.md))

  - **Abstract**: Automated Program Repair (APR) holds the promise of alleviating the burden of debugging and fixing software bugs. Despite this, developers still need to manually inspect each patch to confirm its correctness, which is tedious and time-consuming. This challenge is exacerbated in the presence of plausible patches, which accidentally pass test cases but may not correctly fix the bug. To address this challenge, we propose an interactive approach called iFix to facilitate patch understanding and comp...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [program testing](program_testing.md), [debugging](debugging.md)


- [SpecRover: Code Intent Extraction via LLMs](../venues/ICSE2025/paper_2.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Autonomous program improvement typically involves automatically producing bug fixes and feature additions. Such program improvement can be accomplished by a combination of large language model (LLM) and program analysis capabilities, in the form of an LLM agent. Since program repair or program improvement typically requires a specification of intended behavior - specification inference can be useful for producing high quality program patches. In this work, we examine efficient and low-cost workf...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [specification inference](specification_inference.md)


- [Swe-bench: Can language models resolve real-world github issues?](../venues/ICLR2024/paper_1.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Language models have outpaced our ability to evaluate them effectively, but for their future development it is essential to study the frontier of their capabilities. We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language models. To this end, we introduce SWE-bench, an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popul...
  - **Labels**: [benchmark](benchmark.md), [code generation](code_generation.md), [program repair](program_repair.md)


- [Template-Guided Program Repair in the Era of Large Language Models](../venues/ICSE2025/paper_17.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Recent advancements in automated program repair (APR) have been significantly driven by the application of Large Language Models (LLMs). In particular, the integration of LLMs with traditional template-based repair methods has demonstrated effective outcomes. Despite this, the synergy between the strengths of traditional methods and LLMs remains underexploited. This oversight originates from the indiscriminate use of templates and their insufficient coverage. Also, using small-scale LLMs within ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [The Best of Both Worlds: Combining Learned Embeddings with Engineered Features for Accurate Prediction of Correct Patches](../venues/TOSEM2023/paper_2.md), ([TOSEM2023](../venues/TOSEM2023/README.md))

  - **Abstract**: A large body of the literature on automated program repair develops approaches where patches are automatically generated to be validated against an oracle (e.g., a test suite). Because such an oracle can be imperfect, the generated patches, although validated by the oracle, may actually be incorrect. While the state-of-the-art explores research directions that require dynamic information or rely on manually-crafted heuristics, we study the benefit of learning code representations in order to lea...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [The Fact Selection Problem in LLM-Based Program Repair](../venues/ICSE2025/paper_47.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Recent research has shown that incorporating bug-related facts, such as stack traces and GitHub issues, into prompts enhances the bug-fixing capabilities of large language models (LLMs). Considering the ever-increasing context window of these models, a critical question arises: what and how many facts should be included in prompts to maximise the chance of correctly fixing bugs? To answer this question, we conducted a large-scale study, employing over 19K prompts featuring various combinations o...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [The Plastic Surgery Hypothesis in the Era of Large Language Models](../venues/ASE2023/paper_9.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Automated Program Repair (APR) aspires to automatically generate patches for an input buggy program. Traditional APR tools typically focus on specific bug types and fixes through the use of templates, heuristics, and formal specifications. However, these techniques are limited in terms of the bug types and patch variety they can produce. As such, researchers have designed various learning-based APR tools with recent work focused on directly using Large Language Models (LLMs) for APR. While LLM-b...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [ThinkRepair: Self-Directed Automated Program Repair](../venues/ISSTA2024/paper_15.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Though many approaches have been proposed for Automated Program Repair (APR) and indeed achieved remarkable performance, they still have limitations in fixing bugs that require analyzing and reasoning about the logic of the buggy program. Recently, large language models (LLMs) instructed by prompt engineering have attracted much attention for their powerful ability to address many kinds of tasks including bug-fixing. However, the quality of the prompt will highly affect the ability of LLMs and m...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Towards Efficient Fine-Tuning of Language Models With Organizational Data for Automated Software Review](../venues/TSE2024/paper_1.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Large language models like BERT and GPT possess significant capabilities and potential impacts across various applications. Software engineers often use these models for code-related tasks, including generating, debugging, and summarizing code. Nevertheless, large language models still have several flaws, including model hallucination. (e.g., generating erroneous code and producing outdated and inaccurate programs) and the substantial computational resources and energy required for training and ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Towards Low-Resource Automatic Program Repair with Meta-Learning and Pretrained Language Models](../venues/EMNLP2023/paper_15.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Automatic program repair (APR) has gained increasing attention as an essential technique in software development to reduce manual debugging efforts and boost developers’ productivity. Recent advances in deep learning (DL) based models have demonstrated promising results by learning from large-scale bug-fix examples in a data-driven manner. However, in practical scenarios, software bugs have an imbalanced distribution, and the fixing knowledge learned by APR models often only capture the patterns...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Vision Transformer Inspired Automated Vulnerability Repair](../venues/TOSEM2024/paper_9.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Recently, automated vulnerability repair approaches have been widely adopted to combat increasing software security issues. In particular, transformer-based encoder-decoder models achieve competitive results. Whereas vulnerable programs may only consist of a few vulnerable code areas that need repair, existing AVR approaches lack a mechanism guiding their model to pay more attention to vulnerable code areas during repair generation. In this article, we propose a novel vulnerability repair framew...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [iSMELL: Assembling LLMs with Expert Toolsets for Code Smell Detection and Refactoring](../venues/ASE2024/paper_22.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Detecting and refactoring code smells is challenging, laborious, and sustaining. Although large language models have demonstrated potential in identifying various types of code smells, they also have limitations such as input-output token restrictions, difficulty in accessing repository-level knowledge, and performing dynamic source code analysis. Existing learning-based methods or commercial expert toolsets have advantages in handling complex smells. They can analyze project structures and cont...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [bug detection](bug_detection.md)
