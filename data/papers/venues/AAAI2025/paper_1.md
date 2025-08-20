# Less is more: adaptive program repair with bug localization and preference learning

**Authors**: Dai, Zhenlong and Chen, Bingrui and Zhao, Zhuoluo and Tang, Xiu and Wu, Sai and Yao, Chang and Gao, Zhipeng and Chen, Jingyuan

**Abstract**:

Automated Program Repair (APR) is a task to automatically generate patches for the buggy code. However, most research focuses on generating correct patches while ignoring the consistency between the fixed code and the original buggy code. How to conduct adaptive bug fixing and generate patches with minimal modifications have seldom been investigated. To bridge this gap, we first introduce a novel task, namely AdaPR (Adaptive Program Repair). We then propose a two-stage approach AdaPatcher (Adaptive Patch Generator) to enhance program repair while maintaining the consistency. In the first stage, we utilize a Bug Locator with self-debug learning to accurately pinpoint bug locations. In the second stage, we train a Program Modifier to ensure consistency between the post-modified fixed code and the pre-modified buggy code. The Program Modifier is enhanced with a location-aware repair learning strategy to generate patches based on identified buggy lines, a hybrid training strategy for selective reference and an adaptive preference learning to prioritize fewer changes. The experimental results show that our approach outperforms a set of baselines by a large margin, validating the effectiveness of our two-stage framework for the newly proposed AdaPR task. Code — https://github.com/zhenlongDai/AdaPatcher

**Link**: [Read Paper](https://doi.org/10.1609/aaai.v39i1.31988)

**Labels**: [program repair](../../labels/program_repair.md)
