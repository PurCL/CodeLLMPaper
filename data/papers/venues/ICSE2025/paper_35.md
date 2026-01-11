# DesignRepair: Dual-Stream Design Guideline-Aware Frontend Repair with Large Language Models

**Authors**: Yuan, Mingyue and Chen, Jieshan and Xing, Zhenchang and Quigley, Aaron and Luo, Yuyu and Luo, Tianqi and Mohammadi, Gelareh and Lu, Qinghua and Zhu, Liming

**Abstract**:

The rise of Large Language Models (LLMs) has streamlined frontend interface creation through tools like Vercel's v0, yet surfaced challenges in design quality (e.g., accessibility, and usability). Current solutions, often limited by their focus, generalisability, or data dependency, fall short in addressing these complexities. Moreover, none of them examine the quality of LLM-generated UI design. In this work, we introduce DesignRepair, a novel dual-stream design guideline-aware system to examine and repair the UI design quality issues from both code aspect and rendered page aspect. We utilised the mature and popular Material Design as our knowledge base to guide this process. Specifically, we first constructed a comprehensive knowledge base encoding Google's Material Design principles into low-level component knowledge base and high-level system design knowledge base. After that, DesignRepair employs a LLM for the extraction of key components and utilizes the Playwright tool for precise page analysis, aligning these with the established knowledge bases. Finally, we integrate Retrieval-Augmented Generation with state-of-the-art LLMs like GPT-4 to holistically refine and repair frontend code through a strategic divide and conquer approach. Our extensive evaluations validated the efficacy and utility of our approach, demonstrating significant enhancements in adherence to design guidelines, accessibility, and user experience metrics.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00109)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
