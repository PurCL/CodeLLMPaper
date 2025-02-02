# PELICAN: exploiting backdoors of naturally trained deep learning models in binary code analysis

**Authors**: Zhang, Zhuo and Tao, Guanhong and Shen, Guangyu and An, Shengwei and Xu, Qiuling and Liu, Yingqi and Ye, Yapeng and Wu, Yaoxuan and Zhang, Xiangyu

**Abstract**:

Deep Learning (DL) models are increasingly used in many cyber-security applications and achieve superior performance compared to traditional solutions. In this paper, we study backdoor vulnerabilities in naturally trained models used in binary analysis. These backdoors are not injected by attackers but rather products of defects in datasets and/or training processes. The attacker can exploit these vulnerabilities by injecting some small fixed input pattern (e.g., an instruction) called backdoor trigger to their input (e.g., a binary code snippet for a malware detection DL model) such that misclassification can be induced (e.g., the malware evades the detection). We focus on transformer models used in binary analysis. Given a model, we leverage a trigger inversion technique particularly designed for these models to derive trigger instructions that can induce misclassification. During attack, we utilize a novel trigger injection technique to insert the trigger instruction(s) to the input binary code snippet. The injection makes sure that the code snippets' original program semantics are preserved and the trigger becomes an integral part of such semantics and hence cannot be easily eliminated. We evaluate our prototype PELICAN on 5 binary analysis tasks and 15 models. The results show that PELICAN can effectively induce misclassification on all the evaluated models in both white-box and black-box scenarios. Our case studies demonstrate that PELICAN can exploit the backdoor vulnerabilities of two closed-source commercial tools.

**Link**: [Read Paper](https://www.usenix.org/system/files/usenixsecurity23-zhang-zhuo-pelican.pdf)

**Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)
