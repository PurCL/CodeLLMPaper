# Fixing 7,400 Bugs for 1$: Cheap Crash-Site Program Repair

**Authors**: Han Zheng, Ilia Shumailov, Tianqi Fan, Aiden Hall, Mathias Payer

**Abstract**:

The rapid advancement of bug-finding techniques has led to the discovery of more vulnerabilities than developers can reasonably fix, creating an urgent need for effective Automated Program Repair (APR) methods. However, the complexity of modern bugs often makes precise root cause analysis difficult and unreliable. To address this challenge, we propose crash-site repair to simplify the repair task while still mitigating the risk of exploitation. In addition, we introduce a template-guided patch generation approach that significantly reduces the token cost of Large Language Models (LLMs) while maintaining both efficiency and effectiveness. We implement our prototype system, WILLIAMT, and evaluate it against state-of-the-art APR tools. Our results show that, when combined with the top-performing agent CodeRover-S, WILLIAMT reduces token cost by 45.9% and increases the bug-fixing rate to 73.5% (+29.6%) on ARVO, a ground-truth open source software vulnerabilities benchmark. Furthermore, we demonstrate that WILLIAMT can function effectively even without access to frontier LLMs: even a local model running on a Mac M4 Mini achieves a reasonable repair rate. These findings highlight the broad applicability and scalability of WILLIAMT.

**Link**: [Read Paper](https://arxiv.org/abs/2505.13103)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
