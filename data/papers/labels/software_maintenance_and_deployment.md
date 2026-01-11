# Software Maintenance And Deployment

## Code Review

- [An Empirical Study on Code Review Activity Prediction and Its Impact in Practice](../venues/FSE2024/paper_10.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: During code reviews, an essential step in software quality assurance, reviewers have the difficult task of understanding and evaluating code changes to validate their quality and prevent introducing faults to the codebase. This is a tedious process where the effort needed is highly dependent on the code submitted, as well as the author’s and the reviewer’s experience, leading to median wait times for review feedback of 15-64 hours. Through an initial user study carried with 29 experts, we found ...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md), [empirical study](empirical_study.md)


- [Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering](../venues/ISSTA2025/paper_30.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Recently, large language models (LLMs) have been deployed to tackle various software engineering (SE) tasks like code generation, significantly advancing the automation of SE tasks. However, assessing the quality of these LLM-generated code and text remains challenging. The commonly used Pass@k metric necessitates extensive unit tests and configured environments, demands a high labor cost, and is not suitable for evaluating LLM-generated text. Conventional metrics like BLEU, which measure only l...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md), [empirical study](empirical_study.md)


- [Code Review Automation: Strengths and Weaknesses of the State of the Art](../venues/TSE2024/paper_9.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: The automation of code review has been tackled by several researchers with the goal of reducing its cost. The adoption of deep learning in software engineering pushed the automation to new boundaries, with techniques &lt;italic&gt;imitating&lt;/italic&gt; developers in generative tasks, such as commenting on a code change as a reviewer would do or addressing a reviewer's comment by modifying code. The performance of these techniques is usually assessed through quantitative metrics, &lt;italic&gt...
  - **Labels**: [code review](code_review.md), [empirical study](empirical_study.md)


- [CodeAgent: Autonomous Communicative Agents for Code Review](../venues/EMNLP2024/paper_26.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Code review, which aims at ensuring the overall quality and reliability of software, is a cornerstone of software development. Unfortunately, while crucial, Code review is a labor-intensive process that the research community is looking to automate. Existing automated methods rely on single input-output generative models and thus generally struggle to emulate the collaborative nature of code review. This work introduces CodeAgent, a novel multi-agent Large Language Model (LLM) system for code re...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md), [agent design](agent_design.md)


- [PatchScope: LLM-Enhanced Fine-Grained Stable Patch Classification for Linux Kernel](../venues/ISSTA2025/paper_21.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Stable patch classification plays a crucial role in vulnerability management for the Linux kernel, significantly contributing to the stability and security of Long-term support(LTS) versions. Although existing tools have effectively assisted in assessing whether patches should be merged into stable versions, they cannot determine which stable patches should be merged into which LTS versions. This process still requires the maintainers of the distribution community to manually screen based on the...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md)


- [SCPatcher: Mining Crowd Security Discussions to Enrich Secure Coding Practices](../venues/ASE2023/paper_8.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Secure coding practices (SCPs) have been proposed to guide software developers to write code securely to prevent potential security vulnerabilities. Yet, they are typically one-sentence principles without detailed specifications, e.g., “Properly free allocated memory upon the completion of functions and at all exit points.”, which makes them difficult to follow in practice, especially for software developers who are not yet experienced in secure programming. To address this problem, this paper p...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md)


- [Semantic GUI Scene Learning and Video Alignment for Detecting Duplicate Video-based Bug Reports](../venues/ICSE2024/paper_32.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Video-based bug reports are increasingly being used to document bugs for programs centered around a graphical user interface (GUI). However, developing automated techniques to manage video-based reports is challenging as it requires identifying and understanding often nuanced visual patterns that capture key information about a reported bug. In this paper, we aim to overcome these challenges by advancing the bug report management task of duplicate detection for video-based reports. To this end, ...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md)


- [Understanding Developer-Analyzer Interactions in Code Reviews](../venues/ASE2024/paper_29.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Static code analyzers are now a common part of the codereview process. These automated tools integrate into the code review process by commenting on code changes and suggesting improvements, in the same way as human reviewers. The comments made by static analyzers often trigger a conversation between developers to align on if and how the issue should be fixed. Because developers rarely give feedback directly to the tool, understanding the sentiment and intent in the conversation triggered by the...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md), [empirical study](empirical_study.md)


- [{CRS}core: Grounding Automated Evaluation of Code Review Comments in Code Claims and Smells](../venues/NAACL2025/paper_7.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: The task of automated code review has recently gained a lot of attention from the machine learning community. However, current review comment evaluation metrics rely on comparisons with a human-written reference for a given code change (also called a diff ). Furthermore, code review is a one-to-many problem, like generation and summarization, with many ``valid reviews'' for a diff. Thus, we develop CRScore {---} a reference-free metric to measure dimensions of review quality like conciseness, co...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md)


## Documentation Generation

- [Cell2Doc: ML Pipeline for Generating Documentation in Computational Notebooks](../venues/ASE2023/paper_17.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Computational notebooks have become the go-to way for solving data-science problems. While they are designed to combine code and documentation, prior work shows that documentation is largely ignored by the developers because of the manual effort. Automated documentation generation can help, but existing techniques fail to capture algorithmic details and developers often end up editing the generated text to provide more explanation and sub-steps. This paper proposes a novel machine-learning pipel...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [documentation generation](documentation_generation.md)


- [Evaluating Transfer Learning for Simplifying GitHub READMEs](../venues/FSE2023/paper_13.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Software documentation captures detailed knowledge about a software product, e.g., code, technologies, and design. It plays an important role in the coordination of development teams and in conveying ideas to various stakeholders. However, software documentation can be hard to comprehend if it is written with jargon and complicated sentence structure. In this study, we explored the potential of text simplification techniques in the domain of software engineering to automatically simplify GitHub ...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [documentation generation](documentation_generation.md)


- [SmartNote: An LLM-Powered, Personalised Release Note Generator That Just Works](../venues/FSE2025/paper_22.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: The release note is a crucial document outlining changes in new software versions. It plays a key role in helping stakeholders recognise important changes and understand the implications behind them. Despite this fact, many developers view the process of writing software release notes as a tedious and dreadful task. Consequently, numerous tools (e.g., DeepRelease and Conventional Changelog) have been developed by researchers and practitioners to automate the generation of software release notes....
  - **Labels**: [documentation generation](documentation_generation.md), [software maintenance and deployment](software_maintenance_and_deployment.md)


- [VerLog: Enhancing Release Note Generation for Android Apps using Large Language Models](../venues/ISSTA2025/paper_29.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Release notes are essential documents that communicate the details of software updates to users and developers, yet their generation remains a time-consuming and error-prone process. In this paper, we present VerLog, a novel technique that enhances the generation of software release notes using Large Language Models (LLMs). VerLog leverages few-shot in-context learning with adaptive prompting to facilitate the graph reasoning capabilities of LLMs, enabling them to accurately interpret and docume...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [documentation generation](documentation_generation.md)


## Commit Message Generation

- [An Empirical Study on Commit Message Generation Using LLMs via In-Context Learning](../venues/ICSE2025/paper_29.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Commit messages concisely describe code changes in natural language and are important for software maintenance. Several approaches have been proposed to automatically generate commit messages, but they still suffer from critical limitations, such as time-consuming training and poor generalization ability. To tackle these limitations, we propose to borrow the weapon of large language models (LLMs) and in-context learning (ICL). Our intuition is based on the fact that the training corpora of LLMs ...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [commit message generation](commit_message_generation.md), [empirical study](empirical_study.md)


- [Automatic Commit Message Generation: A Critical Review and Directions for Future Work](../venues/TSE2024/paper_7.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Commit messages are critical for code comprehension and software maintenance. Writing a high-quality message requires skill and effort. To support developers and reduce their effort on this task, several approaches have been proposed to automatically generate commit messages. Despite the promising performance reported, we have identified three significant and prevalent threats in these automated approaches: 1) the datasets used to train and evaluate these approaches contain a considerable amount...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [commit message generation](commit_message_generation.md), [empirical study](empirical_study.md)


- [Large Language Models are Few-Shot Summarizers: Multi-Intent Comment Generation via In-Context Learning](../venues/ICSE2024/paper_4.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Code comment generation aims at generating natural language descriptions for a code snippet to facilitate developers' program comprehension activities. Despite being studied for a long time, a bottleneck for existing approaches is that given a code snippet, they can only generate one comment while developers usually need to know information from diverse perspectives such as what is the functionality of this code snippet and how to use it. To tackle this limitation, this study empirically investi...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [commit message generation](commit_message_generation.md)


- [Leveraging Context-Aware Prompting for Commit Message Generation](../venues/EMNLP2024/paper_29.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Writing comprehensive commit messages is tedious yet important, because these messages describe changes of code, such as fixing bugs or adding new features. However, most existing methods focus on either only the changed lines or nearest context lines, without considering the effectiveness of selecting useful contexts. On the other hand, it is possible that introducing excessive contexts can lead to noise. To this end, we propose a code model COMMIT (Context-aware prOMpting based comMIt-message ...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [commit message generation](commit_message_generation.md)


- [Only diff Is Not Enough: Generating Commit Messages Leveraging Reasoning and Action of Large Language Model](../venues/FSE2024/paper_21.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Commit messages play a vital role in software development and maintenance. While previous research has introduced various Commit Message Generation (CMG) approaches, they often suffer from a lack of consideration for the broader software context associated with code changes. This limitation resulted in generated commit messages that contained insufficient information and were poorly readable. To address these shortcomings, we approached CMG as a knowledge-intensive reasoning task. We employed Re...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [commit message generation](commit_message_generation.md)


## Software Configuration

- [Face It Yourselves: An LLM-Based Two-Stage Strategy to Localize Configuration Errors via Logs](../venues/ISSTA2024/paper_1.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Configurable software systems are prone to configuration errors, resulting in significant losses to companies. However, diagnosing these errors is challenging due to the vast and complex configuration space. These errors pose significant challenges for both experienced maintainers and new end-users, particularly those without access to the source code of the software systems. Given that logs are easily accessible to most end-users, we conduct a preliminary study to outline the challenges and opp...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [software configuration](software_configuration.md)


## System Log Analysis

- [Go Static: Contextualized Logging Statement Generation](../venues/FSE2024/paper_18.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Logging practices have been extensively investigated to assist developers in writing appropriate logging statements for documenting software behaviors. Although numerous automatic logging approaches have been proposed, their performance remains unsatisfactory due to the constraint of the single-method input, without informative programming context outside the method. Specifically, we identify three inherent limitations with single-method context: limited static scope of logging statements, incon...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [system log analysis](system_log_analysis.md)


- [LILAC: Log Parsing using LLMs with Adaptive Parsing Cache](../venues/FSE2024/paper_15.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Log parsing transforms log messages into structured formats, serving as the prerequisite step for various log analysis tasks. Although a variety of log parsing approaches have been proposed, their performance on complicated log data remains compromised due to the use of human-crafted rules or learning-based models with limited training data. The recent emergence of powerful large language models (LLMs) demonstrates their vast pre-trained knowledge related to code and logging, making it promising...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [system log analysis](system_log_analysis.md)


- [Log Parsing with Generalization Ability under New Log Types](../venues/FSE2023/paper_10.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Log parsing, which converts semi-structured logs into structured logs, is the first step for automated log analysis.  Existing parsers are still unsatisfactory in real-world systems due to new log types in new-coming logs.  In practice, available logs collected during system runtime often do not contain all the possible log types of a system because log types related to infrequently activated system states are unlikely to be recorded and new log types are frequently introduced with system update...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [system log analysis](system_log_analysis.md)


- [UniLog: Automatic Logging via LLM and In-Context Learning](../venues/ICSE2024/paper_1.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Logging, which aims to determine the position of logging statements, the verbosity levels, and the log messages, is a crucial process for software reliability enhancement. In recent years, numerous automatic logging tools have been designed to assist developers in one of the logging tasks (e.g., providing suggestions on whether to log in try-catch blocks). These tools are useful in certain situations yet cannot provide a comprehensive logging solution in general. Moreover, although recent resear...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [system log analysis](system_log_analysis.md)


