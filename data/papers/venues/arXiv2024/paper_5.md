# Large Language Model assisted Hybrid Fuzzing

**Authors**: Ruijie Meng, Gregory J. Duck, Abhik Roychoudhury

**Abstract**:

Greybox fuzzing is one of the most popular methods for detecting software vulnerabilities, which conducts a biased random search within the program input space. To enhance its effectiveness in achieving deep coverage of program behaviors, greybox fuzzing is often combined with concolic execution, which performs a path-sensitive search over the domain of program inputs. In hybrid fuzzing, conventional greybox fuzzing is followed by concolic execution in an iterative loop, where reachability roadblocks encountered by greybox fuzzing are tackled by concolic execution. However, such hybrid fuzzing still suffers from difficulties conventionally faced by symbolic execution, such as the need for environment modeling and system call support. In this work, we show how to achieve the effect of concolic execution without having to compute and solve symbolic path constraints. When coverage-based greybox fuzzing reaches a roadblock in terms of reaching certain branches, we conduct a slicing on the execution trace and suggest modifications of the input to reach the relevant branches. A Large Language Model (LLM) is used as a solver to generate the modified input for reaching the desired branches. Compared with both the vanilla greybox fuzzer AFL and hybrid fuzzers Intriguer and Qsym, our LLM-based hybrid fuzzer HyLLfuzz (pronounced "hill fuzz") demonstrates superior coverage. Furthermore, the LLM-based concolic execution in HyLLfuzz takes a time that is 4-19 times faster than the concolic execution running in existing hybrid fuzzing tools. This experience shows that LLMs can be effectively inserted into the iterative loop of hybrid fuzzers, to efficiently expose more program behaviors.

**Link**: [Read Paper](https://doi.org/10.48550/arXiv.2412.15931)

**Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)
