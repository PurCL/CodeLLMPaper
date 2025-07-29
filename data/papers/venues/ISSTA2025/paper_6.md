# Safe4U: Identifying Unsound Safe Encapsulations of Unsafe Calls in Rust using LLMs

**Authors**: Li, Huan and Wang, Bei and Hu, Xing and Xia, Xin

**Abstract**:

Rust is an emerging programming language that ensures safety through strict compile-time checks. A Rust function marked as unsafe indicates it has additional safety requirements (e.g., initialized, not null), known as contracts in the community. These unsafe functions can only be called within explicit unsafe blocks and the contracts must be guaranteed by the caller. To reuse and reduce unsafe code, the community recommends using safe encapsulation of unsafe calls (EUC) in practice. However, an EUC is unsound if any contract is not guaranteed and could lead to undefined behaviors in safe Rust, thus breaking Rust's safety promise. It is challenging to identify unsound EUCs with conventional techniques due to the limitation in cross-lingual comprehension of code and natural language. Large language models (LLMs) have demonstrated impressive capabilities, but their performance is unsatisfactory owing to the complexity of contracts and the lack of domain knowledge. To this end, we propose a novel framework, Safe4U, which incorporates LLMs, static analysis tools, and domain knowledge to identify unsound EUCs. Safe4U first utilizes static analysis tools to retrieve relevant context. Then, it decomposes the primitive contract description into several fine-grained classified contracts. Ultimately, Safe4U introduces domain knowledge and invokes the reasoning capability of LLMs to verify every fine-grained contract. The evaluation results show that Safe4U brings a general performance improvement and the fine-grained results are constructive for locating specific unsound sources. In real-world scenarios, Safe4U can identify 9 out of 11 unsound EUCs from CVE. Furthermore, Safe4U detected 22 new unsound EUCs in the most downloaded crates, 16 of which have been confirmed.

**Link**: [Read Paper](https://doi.org/10.1145/3728890)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
