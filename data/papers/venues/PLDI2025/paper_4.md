# Reductive Analysis with Compiler-Guided Large Language Models for Input-Centric Code Optimizations

**Authors**: Xiangwei Wang, Xinning Hui, Chunhua Liao, Xipeng Shen

**Abstract**:

Input-centric program optimization aims to optimize code by considering the relations between program inputs and program behaviors. Despite its promise, a long-standing barrier for its adoption is the difficulty of automatically identifying critical features of complex inputs. This paper introduces a novel technique, reductive analysis through compiler-guided Large Language Models (LLMs), to solve the problem through a synergy between compilers and LLMs. It uses a reductive approach to overcome the scalability and other limitations of LLMs in program code analysis. The solution, for the first time, automates the identification of critical input features without heavy instrumentation or profiling, cutting the time needed for input identification by 44× (or 450× for local LLMs), reduced from 9.6 hours to 13 minutes (with remote LLMs) or 77 seconds (with local LLMs) on average, making input characterization possible to be integrated into the workflow of program compilations. Optimizations on those identified input features show similar or even better results than those identified by previous profiling-based methods, leading to optimizations that yield 92.6% accuracy in selecting the appropriate adaptive OpenMP parallelization decisions, and 20–30% performance improvement of serverless computing while reducing resource usage by 50–60%.

**Link**: [Read Paper](https://dl.acm.org/doi/10.1145/3729282)

**Labels**: [static analysis](../../labels/static_analysis.md), [program optimization](../../labels/program_optimization.md)
