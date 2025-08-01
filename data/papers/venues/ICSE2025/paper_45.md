# LLM Based Input Space Partitioning Testing for Library APIs

**Authors**: Li, Jiageng and Dong, Zhen and Wang, Chong and You, Haozhen and Zhang, Cen and Liu, Yang and Peng, Xin

**Abstract**:

Automated library APIs testing is difficult as it requires exploring a vast space of parameter inputs that may involve objects with complex data types. Existing search based approaches, with limited knowledge of relations between object states and program branches, often suffer from the low efficiency issue, i.e., tending to generate invalid inputs. Symbolic execution based approaches can effectively identify such relations, but fail to scale to large programs. In this work, we present an LLM-based input space partitioning testing approach, LISP, for library APIs. The approach lever-ages LLMs to understand the code of a library API under test and perform input space partitioning based on its understanding and rich common knowledge. Specifically, we provide the signature and code of the API under test to LLMs, with the expectation of obtaining a text description of each input space partition of the API under test. Then, we generate inputs through employing the generated text description to sample inputs from each partition, ultimately resulting in test suites that systematically explore the program behavior of the API. We evaluate LISP on more than 2,205 library API meth-ods taken from 10 popular open-source Java libraries (e.g., $a$p$a$che/commons-lang with 2.6k stars, guava with 48.8k stars on GitHub). Our experiment results show that LISP is effective in library API testing. It significantly outperforms state-of-the-art tool EvoSuite in terms of edge coverage. On average, LISP achieves 67.82 % branch coverage, surpassing EvoSuite by 1.21 times. In total, LISP triggers 404 exceptions or errors in the experiments, and discovers 13 previously unknown vulnerabilities during evaluation, which have been assigned CVE IDs.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00153)

**Labels**: [program testing](../../labels/program_testing.md), [library testing](../../labels/library_testing.md)
