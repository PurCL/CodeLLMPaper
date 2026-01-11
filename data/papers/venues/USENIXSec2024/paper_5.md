# From One Thousand Pages of Specification to Unveiling Hidden Bugs:Large Language Model Assisted Fuzzing of Matter IoT Devices

**Authors**: Xiaoyue Ma, Lannan Luo, and Qiang Zeng

**Abstract**:

Matter is an IoT connectivity standard backed by over two hundred companies. Since the release of its specification in October 2022, numerous IoT devices have become Matter-compatible. Identifying bugs and vulnerabilities in Matter devices is thus an emerging important problem. This paper introduces mGPTFuzz, the first Matter fuzzer in the literature. Our approach harnesses the extensive and detailed information within the Matter specification to guide the generation of test inputs. However, due to the sheer volume of the Matter specification, surpassing one thousand pages, manually converting human-readable content to machine-readable information is tedious, time-consuming and error-prone. To overcome this challenge, we leverage a large language model to successfully automate the conversion process. mGPTFuzz conducts stateful analysis, which generates message sequences to uncover bugs that would be challenging to discover otherwise. The evaluation involves 23 various Matter devices and discovers 147 new bugs, with three CVEs assigned. In comparison, a state-of-the-art IoT fuzzer finds zero bugs from these devices.

**Link**: [Read Paper](https://www.usenix.org/conference/usenixsecurity24/presentation/ma-xiaoyue)

**Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)
