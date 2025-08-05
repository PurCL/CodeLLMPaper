# Interactive Tools Substantially Assist LM Agents in Finding Security Vulnerabilities

**Authors**: Talor Abramovich, Meet Udeshi, Minghao Shao, Kilian Lieret, Haoran Xi, Kimberly Milner, Sofija Jancheska, John Yang, Carlos E. Jimenez, Farshad Khorrami, Prashanth Krishnamurthy, Brendan Dolan-Gavitt, Muhammad Shafique, Karthik Narasimhan, Ramesh Karri, Ofir Press

**Abstract**:

Although language model (LM) agents have demonstrated increased performance in multiple domains, including coding and web-browsing, their success in cybersecurity has been limited. We present EnIGMA, an LM agent for autonomously solving Capture The Flag (CTF) challenges. We introduce new tools and interfaces to improve the agent's ability to find and exploit security vulnerabilities, focusing on interactive terminal programs. These novel Interactive Agent Tools enable LM agents, for the first time, to run interactive utilities, such as a debugger and a server connection tool, which are essential for solving these challenges. Empirical analysis on 390 CTF challenges across four benchmarks demonstrate that these new tools and interfaces substantially improve our agent's performance, achieving state-of-the-art results on NYU CTF, Intercode-CTF, and CyBench. Finally, we analyze data leakage, developing new methods to quantify it and identifying a new phenomenon we term soliloquizing, where the model self-generates hallucinated observations without interacting with the environment. Our code and development dataset are available at this https URL and this https URL respectively.

**Link**: [Read Paper](https://arxiv.org/abs/2409.16165)

**Labels**: [program testing](../../labels/program_testing.md), [vulnerability exploitation](../../labels/vulnerability_exploitation.md), [benchmark](../../labels/benchmark.md)
