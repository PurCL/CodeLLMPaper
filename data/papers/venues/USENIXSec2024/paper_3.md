# When Threads Meet Interrupts: Effective Static Detection of Interrupt-Based Deadlocks in Linux

**Authors**: Chengfeng Ye, Yuandao Cai, and Charles Zhang

**Abstract**:

Deadlocking is an unresponsive state of software that arises when threads hold locks while trying to acquire other locks that are already held by other threads, resulting in a circular lock dependency. Interrupt-based deadlocks, a specific and prevalent type of deadlocks that occur within the OS kernel due to interrupt preemption, pose significant risks to system functionality, performance, and security. However, existing static analysis tools focus on resource-based deadlocks without characterizing the interrupt preemption. In this paper, we introduce Archerfish, the first static analysis approach for effectively identifying interrupt-based deadlocks in the large-scale Linux kernel. At its core, Archerfish utilizes an Interrupt-Aware Lock Graph (ILG) to capture both regular and interrupt-related lock dependencies, reducing the deadlock detection problem to graph cycle discovery and refinement. Furthermore, Archerfish incorporates four effective analysis components to construct ILG and refine the deadlock cycles, addressing three core challenges, including the extensive interrupt-involving concurrency space, identifying potential interrupt handlers, and validating the feasibility of deadlock cycles. Our experimental results show that Archerfish can precisely analyze the Linux kernel (19.8 MLoC) in approximately one hour. At the time of writing, we have discovered 76 previously unknown deadlocks, with 53 bugs confirmed, 46 bugs already fixed by the Linux community, and 2 CVE IDs assigned. Notably, those found deadlocks are long-latent, hiding for an average of 9.9 years.

**Link**: [Read Paper](https://www.usenix.org/system/files/usenixsecurity24-zhao.pdf)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [specification inference](../../labels/specification_inference.md)
