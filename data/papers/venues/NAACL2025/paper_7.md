# {CRS}core: Grounding Automated Evaluation of Code Review Comments in Code Claims and Smells

**Authors**: Naik, Atharva  and      Alenius, Marcus  and      Fried, Daniel  and      Rose, Carolyn

**Abstract**:

The task of automated code review has recently gained a lot of attention from the machine learning community. However, current review comment evaluation metrics rely on comparisons with a human-written reference for a given code change (also called a diff ). Furthermore, code review is a one-to-many problem, like generation and summarization, with many ``valid reviews'' for a diff. Thus, we develop CRScore {---} a reference-free metric to measure dimensions of review quality like conciseness, comprehensiveness, and relevance. We design CRScore to evaluate reviews in a way that is grounded in claims and potential issues detected in the code by LLMs and static analyzers. We demonstrate that CRScore can produce valid, fine-grained scores of review quality that have the greatest alignment with human judgment among open-source metrics (0.54 Spearman correlation) and are more sensitive than reference-based metrics. We also release a corpus of 2.9k human-annotated review quality scores for machine-generated and GitHub review comments to support the development of automated metrics.

**Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.457/)

**Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [code review](../../labels/code_review.md)
