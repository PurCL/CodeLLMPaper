# PatchScope: LLM-Enhanced Fine-Grained Stable Patch Classification for Linux Kernel

**Authors**: Liu, Rongkai and Shi, Heyuan and Liu, Shuning and Hu, Chao and Li, Sisheng and Shen, Yuheng and Wang, Runzhe and Shi, Xiaohai and Jiang, Yu

**Abstract**:

Stable patch classification plays a crucial role in vulnerability management for the Linux kernel, significantly contributing to the stability and security of Long-term support(LTS) versions. Although existing tools have effectively assisted in assessing whether patches should be merged into stable versions, they cannot determine which stable patches should be merged into which LTS versions. This process still requires the maintainers of the distribution community to manually screen based on the requirements of their respective versions.To address this issue, we propose PatchScope, which is designed to predict the specific merge status of patches.Patchscope consists of two components: patch analysis and patch classification.Patch analysis leverages Large Language Models(LLMs) to generate detailed patch descriptions from the commit message and code changes, thereby deepening the model's semantic understanding of patches. Patch classification utilizes a pre-trained language model to extract semantic features of the patches and employs a two-stage classifier to predict the merge status of the patches.The model is optimized using the dynamic weighted loss function to handle data imbalance and improve overall performance.Given that the primary focus is maintaining Linux kernel versions 5.10 and 6.6, we have conducted comparative experiments based on these two versions. Experimental results demonstrate that Patchscope can effectively predict the merge status of patches.

**Link**: [Read Paper](https://doi.org/10.1145/3728944)

**Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [code review](../../labels/code_review.md)
